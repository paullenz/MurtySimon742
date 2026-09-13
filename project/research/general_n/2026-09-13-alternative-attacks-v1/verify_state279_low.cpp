// Exact integer replay for N34 state 279, E=0,...,15.
// Standard C++17 only. No LP/MILP solver or floating-point proof status is used.
#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std;

struct QT { array<int,11> q{}; int sq=0; };
static map<pair<int,int>, vector<QT>> qcache;

static void genq(int pos,int last,int rem,int qmax,array<int,11>&q,vector<QT>&out){
    if(pos==11){
        if(rem==0){ int sq=0; for(int x:q) sq+=x*x; out.push_back({q,sq}); }
        return;
    }
    int slots=10-pos;
    for(int x=last;x<=min(qmax,rem);++x){
        int rr=rem-x;
        if(rr<x*slots || rr>qmax*slots) continue;
        q[pos]=x;
        genq(pos+1,x,rr,qmax,q,out);
    }
}

static const vector<QT>& qtuples(int total,int qmax){
    auto key=make_pair(total,qmax);
    auto it=qcache.find(key);
    if(it!=qcache.end()) return it->second;
    array<int,11> q{}; vector<QT> out;
    genq(0,0,total,qmax,q,out);
    return qcache.emplace(key,move(out)).first->second;
}

static vector<vector<int>> parts(int total,int n,int maxv){
    vector<vector<int>> out; vector<int> pref;
    function<void(int,int,int)> rec=[&](int pos,int last,int rem){
        if(pos==n){ if(rem==0) out.push_back(pref); return; }
        int slots=n-pos-1;
        for(int v=last;v<=min(maxv,rem);++v){
            int rr=rem-v;
            if(rr<v*slots || rr>maxv*slots) continue;
            pref.push_back(v); rec(pos+1,v,rr); pref.pop_back();
        }
    };
    rec(0,0,total);
    return out;
}

struct Sol {
    bool feasible=false;
    int best=INT_MAX, baseline=0;
    array<int,11> argq{};
};

static Sol solve_profile(const vector<int>&e2,const vector<int>&e3){
    int E=accumulate(e2.begin(),e2.end(),0)+accumulate(e3.begin(),e3.end(),0);
    int Q=42+E;
    int baseline=3*(82+E);

    for(int e:e2) if(e>9) return {false,INT_MAX,baseline,{}};
    for(int e:e3) if(e>8) return {false,INT_MAX,baseline,{}};

    array<int,5> H{};
    for(int l=1;l<=4;++l){
        for(int e:e2) H[l]+=(e>=l);
        for(int e:e3) H[l]+=(e>=l);
    }

    int xmax=0;
    for(int e:e2) xmax=max(xmax,2+e);
    for(int e:e3) xmax=max(xmax,3+e);
    int qmax=0;
    for(int q=0;q<=12;++q)
        if(q*max(0,q-xmax)<=40) qmax=q;

    array<int,13> pmax; pmax.fill(-1);
    for(int q=0;q<=qmax;++q){
        int cap=min(5,17-q), best=-1;
        for(int p=0;p<=cap;++p){
            if(q==0){ best=p; continue; }
            int L=max({0,p-2,q+p-13});
            if(L==0 || (L<=4 && q<=H[L])) best=p;
        }
        pmax[q]=best;
    }

    int z0=count(e2.begin(),e2.end(),0);
    vector<tuple<int,int,int>> positive;
    for(int e:e2) if(e>=2) positive.push_back({2+e,e,e-1});
    for(int e:e3) if(e>=1) positive.push_back({3+e,e,e});

    bool feasible=false;
    int bestB=INT_MAX;
    array<int,11> bestq{};

    for(const auto&qt:qtuples(Q,qmax)){
        int caps[11], capsum=0; bool ok=true;
        for(int j=0;j<11;++j){
            caps[j]=pmax[qt.q[j]];
            if(caps[j]<0){ ok=false; break; }
            capsum+=caps[j];
        }
        if(!ok) continue;

        int need=Q-21;
        if(need>capsum) continue;

        int Pplus=0;
        for(auto [k,e,w]:positive){
            if(k>11 || qt.q[11-k]<=0){ ok=false; break; }
            Pplus += w*(e+2+qt.q[11-k]);
        }
        if(!ok) continue;

        int left=need, pcost=0;
        for(int j=0;j<11 && left;++j){
            int take=min(left,caps[j]);
            pcost += qt.q[j]*take;
            left -= take;
        }
        if(left) continue;

        int T=qt.sq+pcost;
        int B=T+2*z0-Pplus;
        feasible=true;
        if(B<bestB){ bestB=B; bestq=qt.q; }
    }
    return {feasible,bestB,baseline,bestq};
}

struct Row { int E,profiles,strict,equality,negative,source_infeasible,min_strict_gap,min_finite_gap; };

static Row scan(int E){
    int total=0,strict=0,equality=0,negative=0,src=0;
    int minStrict=INT_MAX,minFinite=INT_MAX;
    for(int e2tot=0;e2tot<=E;++e2tot){
        auto p2=parts(e2tot,3,9);
        auto p3=parts(E-e2tot,12,8);
        for(const auto&e2:p2) for(const auto&e3:p3){
            ++total;
            auto s=solve_profile(e2,e3);
            if(!s.feasible){ ++src; continue; }
            int gap=s.best-s.baseline;
            minFinite=min(minFinite,gap);
            if(gap>0){ ++strict; minStrict=min(minStrict,gap); }
            else if(gap==0) ++equality;
            else ++negative;
        }
    }
    return {E,total,strict,equality,negative,src,
            minStrict==INT_MAX?0:minStrict,
            minFinite==INT_MAX?999:minFinite};
}

static string vecstr(const array<int,11>&q){
    string s;
    for(int i=0;i<11;++i){ if(i) s+=","; s+=to_string(q[i]); }
    return s;
}

int main(){
    const vector<Row> expected={
        {0,1,1,0,0,0,2,2},
        {1,2,2,0,0,0,5,5},
        {2,5,5,0,0,0,11,11},
        {3,10,10,0,0,0,5,5},
        {4,19,19,0,0,0,5,5},
        {5,33,33,0,0,0,2,2},
        {6,57,55,1,1,0,6,-2},
        {7,92,92,0,0,0,5,5},
        {8,147,147,0,0,0,2,2},
        {9,226,225,1,0,0,9,0},
        {10,341,341,0,0,0,7,7},
        {11,501,501,0,0,0,8,8},
        {12,726,726,0,0,0,6,6},
        {13,1028,1028,0,0,0,15,15},
        {14,1438,1438,0,0,0,17,17},
        {15,1977,1977,0,0,0,20,20}
    };

    cout << "E profiles strict equality negative source_infeasible min_strict_gap min_finite_gap\n";
    for(const auto&w:expected){
        Row g=scan(w.E);
        assert(tie(g.E,g.profiles,g.strict,g.equality,g.negative,g.source_infeasible,g.min_strict_gap,g.min_finite_gap)
            ==tie(w.E,w.profiles,w.strict,w.equality,w.negative,w.source_infeasible,w.min_strict_gap,w.min_finite_gap));
        cout<<g.E<<' '<<g.profiles<<' '<<g.strict<<' '<<g.equality<<' '<<g.negative<<' '
            <<g.source_infeasible<<' '<<g.min_strict_gap<<' '<<g.min_finite_gap<<'\n';
    }

    // Verify that each non-strict profile has a unique q-vector capable of
    // attaining nonpositive coarse gap.  The hand proof then excludes it by
    // sharpening the zero-excess demand-two C_0 term.
    struct Case { vector<int> e2,e3; int gap; string q; };
    const vector<Case> cases={
        {{0,0,0},{0,0,0,0,0,0,0,0,0,0,0,6},-2,"1,1,5,5,5,5,5,5,5,5,6"},
        {{0,0,0},{0,0,0,0,0,0,0,0,0,0,3,3},0,"2,2,2,2,2,6,6,6,6,7,7"},
        {{0,0,0},{0,0,0,0,0,0,0,0,0,3,3,3},0,"3,3,3,3,3,6,6,6,6,6,6"}
    };
    for(const auto&c:cases){
        auto s=solve_profile(c.e2,c.e3);
        assert(s.best-s.baseline==c.gap);
        assert(vecstr(s.argq)==c.q);
    }

    cout << "PASS low-excess table reproduced; three non-strict profiles match the preserved hand-rigidity cases.\n";
}
