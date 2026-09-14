#!/usr/bin/env python3
"""Add staircase-band reach instrumentation to the generated antichain scanner.

Run make_antichain_stats_scanner.py first. This script preserves all canonical
relational pass/fail decisions. For each exact target-Hall failure it extracts
the canonical maximal sharp-upset witness, builds the staircase-band relaxation
for that witness, and records whether the smaller band flow also fails.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "scan_antichain_profile_stats.cpp"
OUT = HERE / "scan_band_reach_stats.cpp"
s = SRC.read_text()

needle = "static pair<int,long long> target_cost_flow"
if s.count(needle) != 1:
    raise SystemExit("target_cost_flow insertion point not unique")

block = r'''static tuple<int,int,int> canonical_band_flow(const vector<int>&q,const OD&o,int Q){
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
    int exactflow=F.flow(S,T);

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
    if(h==0){cerr<<"BAND_EMPTY_GENERATORS_ON_FAILURE\n";exit(7);}

    vector<int> band(k,-1),M(h,0),D(h,0);
    for(int t=0;t<k;++t)if(selected[t]){
        int b=-1;
        for(int i=0;i<h;++i)if(types[t].c<=types[gens[i]].c){b=i;break;}
        if(b<0){cerr<<"BAND_ASSIGNMENT_FAILURE\n";exit(8);}
        auto const&G=types[gens[b]];
        if(!(types[t].q>=G.q&&types[t].c<=G.c)){
            cerr<<"BAND_INTERVAL_CONTAINMENT_FAILURE\n";exit(9);
        }
        band[t]=b;M[b]+=types[t].n;D[b]+=types[t].n*types[t].q;
    }

    int demand=accumulate(D.begin(),D.end(),0);
    int BS=h+k,BT=BS+1;Dinic B(BT+1);
    for(int i=0;i<h;++i)B.add(BS,i,D[i]);
    for(int i=0;i<h;++i)for(int j=0;j<k;++j)if(compat_hall_type(types[gens[i]],types[j])){
        int copies=M[i]-(selected[j]&&band[j]==i?1:0);
        if(copies<0){cerr<<"BAND_NEGATIVE_COPIES\n";exit(10);}
        int cap=types[j].n*copies;
        if(cap)B.add(i,h+j,cap);
    }
    for(int j=0;j<k;++j)B.add(h+j,BT,types[j].n*types[j].P);
    int bandflow=B.flow(BS,BT);
    return {bandflow,demand,h};
}

'''
s = s.replace(needle, block + needle, 1)

old = "    array<long long,10> target_genhist{}; int target_maxgen=0;\n"
new = old + "    long long band_fail=0,band_pass=0; array<long long,10> band_fail_genhist{}; int band_maxgen=0;\n"
if s.count(old) != 1:
    raise SystemExit("Result counter insertion point not unique")
s = s.replace(old, new, 1)

old = "            int bin=min(gcount,9);++res.target_genhist[bin];res.target_maxgen=max(res.target_maxgen,gcount);\n            return;\n"
new = r'''            int bin=min(gcount,9);++res.target_genhist[bin];res.target_maxgen=max(res.target_maxgen,gcount);
            auto [bflow,bdemand,bgen]=canonical_band_flow(q,o,Q);
            if(bgen!=gcount){cerr<<"BAND_GENERATOR_COUNT_MISMATCH state="<<st.id<<" E="<<E<<" antichain="<<gcount<<" band="<<bgen<<"\n";exit(11);}
            res.band_maxgen=max(res.band_maxgen,bgen);
            if(bflow<bdemand){++res.band_fail;++res.band_fail_genhist[min(bgen,9)];}
            else ++res.band_pass;
            return;
'''
if s.count(old) != 1:
    raise SystemExit("target failure instrumentation point not unique")
s = s.replace(old, new, 1)

old = "target_gen9plus\\ttarget_maxgen\\tcost_fail"
new = "target_gen9plus\\ttarget_maxgen\\tband_fail\\tband_pass\\tband_fail_gen1\\tband_fail_gen2\\tband_fail_gen3\\tband_fail_gen4\\tband_fail_gen5\\tband_fail_gen6\\tband_fail_gen7\\tband_fail_gen8\\tband_fail_gen9plus\\tband_maxgen\\tcost_fail"
if s.count(old) != 1:
    raise SystemExit("header replacement point not unique")
s = s.replace(old, new, 1)

old = "           <<r.target_genhist[9]<<'\\t'<<r.target_maxgen<<'\\t'<<r.cost_fail<<'\\t'\n"
new = "           <<r.target_genhist[9]<<'\\t'<<r.target_maxgen<<'\\t'<<r.band_fail<<'\\t'<<r.band_pass<<'\\t'\n           <<r.band_fail_genhist[1]<<'\\t'<<r.band_fail_genhist[2]<<'\\t'<<r.band_fail_genhist[3]<<'\\t'<<r.band_fail_genhist[4]<<'\\t'\n           <<r.band_fail_genhist[5]<<'\\t'<<r.band_fail_genhist[6]<<'\\t'<<r.band_fail_genhist[7]<<'\\t'<<r.band_fail_genhist[8]<<'\\t'\n           <<r.band_fail_genhist[9]<<'\\t'<<r.band_maxgen<<'\\t'<<r.cost_fail<<'\\t'\n"
if s.count(old) != 1:
    raise SystemExit("output replacement point not unique")
s = s.replace(old, new, 1)

banner = r'''/* GENERATED by make_band_reach_scanner.py after make_antichain_stats_scanner.py.
   Canonical relational decisions are unchanged. Extra instrumentation measures
   whether the verified staircase-band necessary relaxation already rejects
   each exact target-Hall-failing canonical witness. */
'''
OUT.write_text(banner + s)
print(OUT)
