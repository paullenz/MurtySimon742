#!/usr/bin/env python3
"""Generate a one-witness diagnostic scanner for the unique band false-negative.

Run make_antichain_stats_scanner.py and make_band_reach_scanner.py first.  The
resulting scanner preserves the canonical enumeration and exits successfully
as soon as an exact target-Hall failure passes the staircase-band relaxation,
writing a complete diagnostic JSON record.
"""
from pathlib import Path

HERE=Path(__file__).resolve().parent
SRC=HERE/'scan_band_reach_stats.cpp'
OUT=HERE/'scan_band_exception.cpp'
s=SRC.read_text()

needle='static pair<int,long long> target_cost_flow'
if s.count(needle)!=1:
    raise SystemExit('target_cost_flow insertion point not unique')

block=r'''static void write_band_exception_witness(
    int state_id,int E,const vector<int>&q,const vector<int>&rho,const OD&o,int Q,
    int labelled_flow,int band_flow,int band_demand)
{
    map<tuple<int,int,int>,int> ct;
    for(int i=0;i<(int)q.size();++i)++ct[make_tuple(q[i],o.c[i],o.P[i])];
    vector<HallType> types;types.reserve(ct.size());
    for(auto const&kv:ct){auto [qq,cc,pp]=kv.first;types.push_back({qq,cc,pp,kv.second});}
    int k=types.size(),S=2*k,T=S+1;Dinic F(T+1);
    for(int i=0;i<k;++i)F.add(S,i,types[i].n*types[i].q);
    for(int i=0;i<k;++i)for(int j=0;j<k;++j)if(compat_hall_type(types[i],types[j])){
        int cap=(i==j)?types[i].n*(types[i].n-1):types[i].n*types[j].n;
        if(cap)F.add(i,k+j,cap);
    }
    for(int j=0;j<k;++j)F.add(k+j,T,types[j].n*types[j].P);
    for(int x=0;x<k;++x)for(int y=0;y<k;++y)
        if(x!=y&&sharp_dominates(types[x],types[y]))F.add(y,x,Q+1);
    int qflow=F.flow(S,T);
    if(qflow!=labelled_flow){cerr<<"EXCEPTION_DIAGNOSTIC_FLOW_MISMATCH\n";exit(21);}

    vector<vector<int>> rev(T+1);
    for(int u=0;u<=T;++u)for(auto const&e:F.g[u])if(e.cap>0)rev[e.to].push_back(u);
    vector<unsigned char> can(T+1,0);queue<int>qq;can[T]=1;qq.push(T);
    while(!qq.empty()){
        int v=qq.front();qq.pop();
        for(int u:rev[v])if(!can[u]){can[u]=1;qq.push(u);}
    }
    vector<unsigned char> selected(k,0);
    for(int i=0;i<k;++i)selected[i]=!can[i];

    vector<int> gens;
    for(int i=0;i<k;++i)if(selected[i]){
        bool nonminimal=false;
        for(int j=0;j<k;++j)if(j!=i&&selected[j]&&sharp_dominates(types[i],types[j])){nonminimal=true;break;}
        if(!nonminimal)gens.push_back(i);
    }
    stable_sort(gens.begin(),gens.end(),[&](int x,int y){return types[x].c<types[y].c;});
    int h=gens.size();
    vector<int> band(k,-1),M(h,0),D(h,0);
    for(int t=0;t<k;++t)if(selected[t]){
        int b=-1;for(int i=0;i<h;++i)if(types[t].c<=types[gens[i]].c){b=i;break;}
        if(b<0){cerr<<"EXCEPTION_BAND_ASSIGNMENT_FAILURE\n";exit(22);}
        band[t]=b;M[b]+=types[t].n;D[b]+=types[t].n*types[t].q;
    }

    long long exact_demand=0,exact_capacity=0;
    for(int i=0;i<k;++i)if(selected[i])exact_demand+=1LL*types[i].n*types[i].q;
    for(int j=0;j<k;++j){
        int incoming=0;
        for(int i=0;i<k;++i)if(selected[i]&&compat_hall_type(types[i],types[j]))
            incoming+=types[i].n-(i==j?1:0);
        exact_capacity+=1LL*types[j].n*min(types[j].P,incoming);
    }

    ofstream w("BAND_EXCEPTION_WITNESS.json");
    w<<"{\n";
    w<<"  \"schema\": \"staircase-band-exception-witness-v1\",\n";
    w<<"  \"state_id\": "<<state_id<<",\n";
    w<<"  \"E\": "<<E<<",\n";
    w<<"  \"Q\": "<<Q<<",\n";
    w<<"  \"labelled_flow\": "<<labelled_flow<<",\n";
    w<<"  \"quotient_flow\": "<<qflow<<",\n";
    w<<"  \"exact_canonical_demand\": "<<exact_demand<<",\n";
    w<<"  \"exact_canonical_capacity\": "<<exact_capacity<<",\n";
    w<<"  \"exact_canonical_margin\": "<<(exact_capacity-exact_demand)<<",\n";
    w<<"  \"band_flow\": "<<band_flow<<",\n";
    w<<"  \"band_demand\": "<<band_demand<<",\n";
    w<<"  \"band_margin\": "<<(band_flow-band_demand)<<",\n";
    w<<"  \"rho\": [";for(size_t i=0;i<rho.size();++i){if(i)w<<",";w<<rho[i];}w<<"],\n";
    w<<"  \"q\": [";for(size_t i=0;i<q.size();++i){if(i)w<<",";w<<q[i];}w<<"],\n";
    w<<"  \"generators\": [";for(size_t z=0;z<gens.size();++z){if(z)w<<",";w<<gens[z];}w<<"],\n";
    w<<"  \"band_M\": [";for(size_t i=0;i<M.size();++i){if(i)w<<",";w<<M[i];}w<<"],\n";
    w<<"  \"band_D\": [";for(size_t i=0;i<D.size();++i){if(i)w<<",";w<<D[i];}w<<"],\n";
    w<<"  \"types\": [\n";
    for(int i=0;i<k;++i){
        int L=-1,R=-1;
        for(int b=0;b<h;++b)if(compat_hall_type(types[gens[b]],types[i])){if(L<0)L=b;R=b;}
        w<<"    {\"index\":"<<i<<",\"q\":"<<types[i].q<<",\"c\":"<<types[i].c<<",\"P\":"<<types[i].P
         <<",\"n\":"<<types[i].n<<",\"selected\":"<<(selected[i]?"true":"false")
         <<",\"band\":"<<band[i]<<",\"target_L\":"<<L<<",\"target_R\":"<<R<<"}";
        if(i+1<k)w<<",";w<<"\n";
    }
    w<<"  ],\n";
    w<<"  \"promotion_status\": \"DIAGNOSTIC_ONLY\",\n";
    w<<"  \"external_review\": \"OPEN\"\n";
    w<<"}\n";
    w.close();
    cerr<<"BAND_EXCEPTION_FOUND state="<<state_id<<" E="<<E<<" exact="<<labelled_flow<<"/"<<Q
        <<" band="<<band_flow<<"/"<<band_demand<<" generators="<<h<<"\n";
}

'''
s=s.replace(needle,block+needle,1)

old='''            if(bflow<bdemand){++res.band_fail;++res.band_fail_genhist[min(bgen,9)];}\n            else ++res.band_pass;\n            return;\n'''
new='''            if(bflow<bdemand){++res.band_fail;++res.band_fail_genhist[min(bgen,9)];}\n            else {\n                ++res.band_pass;\n                write_band_exception_witness(st.id,E,q,rho,o,Q,f,bflow,bdemand);\n                exit(0);\n            }\n            return;\n'''
if s.count(old)!=1:
    raise SystemExit('band pass replacement point not unique')
s=s.replace(old,new,1)

OUT.write_text('/* GENERATED diagnostic scanner; exits successfully on first band false-negative. */\n'+s)
print(OUT)
