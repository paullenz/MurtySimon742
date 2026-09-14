#!/usr/bin/env python3
"""Strengthen the generated staircase-band pilot scanner with compatible-copy flow.

Run, in order:
  make_antichain_stats_scanner.py
  make_band_reach_scanner.py
  make_compatible_copy_band_reach_scanner.py

The resulting scanner keeps the canonical relational decisions unchanged and
measures both the coarse generator-band relaxation and the stronger
compatible-copy band refinement on every exact target-Hall failure.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "scan_band_reach_stats.cpp"
OUT = HERE / "scan_compatible_copy_band_reach_stats.cpp"
s = SRC.read_text()

start = s.find("static tuple<int,int,int> canonical_band_flow")
end = s.find("static pair<int,long long> target_cost_flow", start)
if start < 0 or end < 0 or end <= start:
    raise SystemExit("canonical_band_flow block not found uniquely")

block = r'''static tuple<int,int,int,int> canonical_band_flows(const vector<int>&q,const OD&o,int Q){
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
    (void)F.flow(S,T);

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
    if(h==0){cerr<<"CCBAND_EMPTY_GENERATORS_ON_FAILURE\n";exit(70);}

    vector<int> band(k,-1),M(h,0),D(h,0);
    for(int t=0;t<k;++t)if(selected[t]){
        int b=-1;
        for(int i=0;i<h;++i)if(types[t].c<=types[gens[i]].c){b=i;break;}
        if(b<0){cerr<<"CCBAND_ASSIGNMENT_FAILURE\n";exit(71);}
        auto const&G=types[gens[b]];
        if(!(types[t].q>=G.q&&types[t].c<=G.c)){
            cerr<<"CCBAND_INTERVAL_CONTAINMENT_FAILURE\n";exit(72);
        }
        band[t]=b;M[b]+=types[t].n;D[b]+=types[t].n*types[t].q;
    }

    int demand=accumulate(D.begin(),D.end(),0);
    int BS=h+k,BT=BS+1;Dinic coarse(BT+1),refined(BT+1);
    for(int i=0;i<h;++i){coarse.add(BS,i,D[i]);refined.add(BS,i,D[i]);}

    for(int i=0;i<h;++i)for(int j=0;j<k;++j){
        int delta=(selected[j]&&band[j]==i)?1:0;
        int coarsecap=0;
        if(compat_hall_type(types[gens[i]],types[j])){
            int copies=M[i]-delta;
            if(copies<0){cerr<<"CCBAND_NEGATIVE_COARSE_COPIES\n";exit(73);}
            coarsecap=types[j].n*copies;
            if(coarsecap)coarse.add(i,h+j,coarsecap);
        }

        int actualcopies=0;
        for(int t=0;t<k;++t)if(selected[t]&&band[t]==i&&compat_hall_type(types[t],types[j]))
            actualcopies+=types[t].n;
        int rcopies=actualcopies-delta;
        if(rcopies<0){cerr<<"CCBAND_NEGATIVE_REFINED_COPIES\n";exit(74);}
        int refinedcap=types[j].n*rcopies;
        if(refinedcap>coarsecap){
            cerr<<"CCBAND_REFINEMENT_EXCEEDS_COARSE i="<<i<<" target="<<j
                <<" refined="<<refinedcap<<" coarse="<<coarsecap<<"\n";
            exit(75);
        }
        if(refinedcap)refined.add(i,h+j,refinedcap);
    }
    for(int j=0;j<k;++j){
        int cap=types[j].n*types[j].P;
        coarse.add(h+j,BT,cap);refined.add(h+j,BT,cap);
    }
    int coarseflow=coarse.flow(BS,BT);
    int refinedflow=refined.flow(BS,BT);
    if(refinedflow>coarseflow){
        cerr<<"CCBAND_FLOW_EXCEEDS_COARSE refined="<<refinedflow<<" coarse="<<coarseflow<<"\n";
        exit(76);
    }
    return {coarseflow,refinedflow,demand,h};
}

'''
s = s[:start] + block + s[end:]

old = "    long long band_fail=0,band_pass=0; array<long long,10> band_fail_genhist{}; int band_maxgen=0;\n"
new = old + "    long long ccband_fail=0,ccband_pass=0;\n"
if s.count(old) != 1:
    raise SystemExit("band result counter insertion point not unique")
s = s.replace(old, new, 1)

old = r'''            auto [bflow,bdemand,bgen]=canonical_band_flow(q,o,Q);
            if(bgen!=gcount){cerr<<"BAND_GENERATOR_COUNT_MISMATCH state="<<st.id<<" E="<<E<<" antichain="<<gcount<<" band="<<bgen<<"\n";exit(11);}
            res.band_maxgen=max(res.band_maxgen,bgen);
            if(bflow<bdemand){++res.band_fail;++res.band_fail_genhist[min(bgen,9)];}
            else ++res.band_pass;
            return;
'''
new = r'''            auto [bflow,ccflow,bdemand,bgen]=canonical_band_flows(q,o,Q);
            if(bgen!=gcount){cerr<<"BAND_GENERATOR_COUNT_MISMATCH state="<<st.id<<" E="<<E<<" antichain="<<gcount<<" band="<<bgen<<"\n";exit(11);}
            res.band_maxgen=max(res.band_maxgen,bgen);
            if(bflow<bdemand){++res.band_fail;++res.band_fail_genhist[min(bgen,9)];}
            else ++res.band_pass;
            if(ccflow<bdemand)++res.ccband_fail;
            else ++res.ccband_pass;
            if(bflow<bdemand && ccflow>=bdemand){
                cerr<<"CCBAND_MONOTONICITY_FAILURE state="<<st.id<<" E="<<E<<" coarse="<<bflow<<" refined="<<ccflow<<" demand="<<bdemand<<"\n";
                exit(77);
            }
            return;
'''
if s.count(old) != 1:
    raise SystemExit("band failure instrumentation point not unique")
s = s.replace(old, new, 1)

old = "band_fail_gen9plus\\tband_maxgen\\tcost_fail"
new = "band_fail_gen9plus\\tband_maxgen\\tccband_fail\\tccband_pass\\tcost_fail"
if s.count(old) != 1:
    raise SystemExit("header replacement point not unique")
s = s.replace(old, new, 1)

old = "           <<r.band_fail_genhist[9]<<'\\t'<<r.band_maxgen<<'\\t'<<r.cost_fail<<'\\t'\n"
new = "           <<r.band_fail_genhist[9]<<'\\t'<<r.band_maxgen<<'\\t'<<r.ccband_fail<<'\\t'<<r.ccband_pass<<'\\t'<<r.cost_fail<<'\\t'\n"
if s.count(old) != 1:
    raise SystemExit("output replacement point not unique")
s = s.replace(old, new, 1)

banner = r'''/* GENERATED by make_compatible_copy_band_reach_scanner.py after the
   antichain and coarse-band generators. Canonical relational decisions are
   unchanged. Extra instrumentation compares coarse and compatible-copy band
   flows on each exact target-Hall-failing canonical witness. */
'''
OUT.write_text(banner + s)
print(OUT)
