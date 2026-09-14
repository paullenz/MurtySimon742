#!/usr/bin/env python3
"""Generate an antichain-statistics scanner from the canonical relational scanner.

The generated scanner preserves the original state/q-profile enumeration and
all proof screens.  When the labelled target flow fails, it independently
builds the sharp-dominance-closed quotient network, checks that its maximum
flow agrees exactly, extracts the canonical maximal minimum cut, and records
its minimal antichain generator count.

Reconnaissance only: this generator never promotes a state.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "2026-09-13-alternative-attacks-v1" / "scan_post_pair_relational.cpp"
OUT = HERE / "scan_antichain_profile_stats.cpp"
s = SRC.read_text()

s = s.replace("#include <algorithm>\n", "#include <algorithm>\n#include <array>\n", 1)

needle = "static pair<int,long long> target_cost_flow"
if s.count(needle) != 1:
    raise SystemExit("target_cost_flow insertion point not unique")

block = r'''struct HallType { int q,c,P,n; };
static bool compat_hall_type(const HallType&a,const HallType&b){
    return a.q<=b.c+1 && b.q<=a.c;
}
static bool sharp_dominates(const HallType&x,const HallType&y){
    return x.c<=y.c && (x.q>y.q || (x.q==y.q && x.P>=y.P));
}

static pair<int,int> canonical_antichain_stats(const vector<int>&q,const OD&o,int Q){
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

    int flow=F.flow(S,T);

    vector<vector<int>> rev(T+1);
    for(int u=0;u<=T;++u)for(auto const&e:F.g[u])if(e.cap>0)rev[e.to].push_back(u);
    vector<unsigned char> can(T+1,0);queue<int>qq;can[T]=1;qq.push(T);
    while(!qq.empty()){
        int v=qq.front();qq.pop();
        for(int u:rev[v])if(!can[u]){can[u]=1;qq.push(u);}
    }
    vector<unsigned char> selected(k,0);
    for(int i=0;i<k;++i)selected[i]=!can[i];

    // The residual maximal source-side cut must be a sharp hardness up-set.
    for(int y=0;y<k;++y)if(selected[y])for(int x=0;x<k;++x)
        if(x!=y&&sharp_dominates(types[x],types[y])&&!selected[x]){
            cerr<<"ANTICHAIN_UPSET_MISMATCH y="<<y<<" x="<<x<<"\n";exit(4);
        }

    int generators=0;vector<int> gens;
    for(int i=0;i<k;++i)if(selected[i]){
        bool nonminimal=false;
        for(int j=0;j<k;++j)if(j!=i&&selected[j]&&sharp_dominates(types[i],types[j])){nonminimal=true;break;}
        if(!nonminimal){++generators;gens.push_back(i);}
    }
    stable_sort(gens.begin(),gens.end(),[&](int x,int y){return types[x].c<types[y].c;});
    for(int z=1;z<(int)gens.size();++z){
        auto const&A=types[gens[z-1]];auto const&B=types[gens[z]];
        if(!(A.c<B.c&&A.q<=B.q&&(A.q!=B.q||A.P<B.P))){
            cerr<<"ANTICHAIN_STAIRCASE_MISMATCH\n";exit(5);
        }
    }
    return {flow,generators};
}

'''
s = s.replace(needle, block + needle, 1)

old = "    long long paircap_pass=0,incidence_pass=0,pairhall_pass=0,targethall_pass=0;\n"
new = old + "    array<long long,10> target_genhist{}; int target_maxgen=0;\n"
if s.count(old) != 1:
    raise SystemExit("Result insertion point not unique")
s = s.replace(old, new, 1)

old = "        if(f<Q){++res.targethall_fail;return;}++res.targethall_pass;\n"
new = r'''        if(f<Q){
            ++res.targethall_fail;
            auto [qflow,gcount]=canonical_antichain_stats(q,o,Q);
            if(qflow!=f){cerr<<"ANTICHAIN_FLOW_MISMATCH state="<<st.id<<" E="<<E<<" labelled="<<f<<" quotient="<<qflow<<"\n";exit(6);}
            int bin=min(gcount,9);++res.target_genhist[bin];res.target_maxgen=max(res.target_maxgen,gcount);
            return;
        }++res.targethall_pass;
'''
if s.count(old) != 1:
    raise SystemExit("target failure replacement point not unique")
s = s.replace(old, new, 1)

old = "targethall_fail\\ttargethall_pass\\tcost_fail"
new = "targethall_fail\\ttargethall_pass\\ttarget_gen1\\ttarget_gen2\\ttarget_gen3\\ttarget_gen4\\ttarget_gen5\\ttarget_gen6\\ttarget_gen7\\ttarget_gen8\\ttarget_gen9plus\\ttarget_maxgen\\tcost_fail"
if s.count(old) != 1:
    raise SystemExit("header replacement point not unique")
s = s.replace(old, new, 1)

old = "           <<r.pairhall_fail<<'\\t'<<r.pairhall_pass<<'\\t'<<r.targethall_fail<<'\\t'<<r.targethall_pass<<'\\t'<<r.cost_fail<<'\\t'\n"
new = "           <<r.pairhall_fail<<'\\t'<<r.pairhall_pass<<'\\t'<<r.targethall_fail<<'\\t'<<r.targethall_pass<<'\\t'\n           <<r.target_genhist[1]<<'\\t'<<r.target_genhist[2]<<'\\t'<<r.target_genhist[3]<<'\\t'<<r.target_genhist[4]<<'\\t'\n           <<r.target_genhist[5]<<'\\t'<<r.target_genhist[6]<<'\\t'<<r.target_genhist[7]<<'\\t'<<r.target_genhist[8]<<'\\t'\n           <<r.target_genhist[9]<<'\\t'<<r.target_maxgen<<'\\t'<<r.cost_fail<<'\\t'\n"
if s.count(old) != 1:
    raise SystemExit("output replacement point not unique")
s = s.replace(old, new, 1)

banner = r'''/* GENERATED by make_antichain_stats_scanner.py.
   Mathematical decisions in the canonical scanner are unchanged.
   Extra work is audit/reconnaissance only: every labelled target-flow failure
   is cross-checked against the sharp-dominance-closed quotient max flow and
   its canonical antichain generator count is recorded. */
'''
OUT.write_text(banner + s)
print(OUT)
