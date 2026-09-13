// Exact integer replay for N34 state 227, excess layers E=0,...,20.
// Standard C++17 only. No LP/MILP solver or floating-point proof status is used.
#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <iostream>
#include <map>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std;

struct QTuple { array<int,10> q{}; int sq=0; };
static map<pair<int,int>, vector<QTuple>> qcache;

static void gen_q(int pos,int last,int rem,int qmax,array<int,10>& q,vector<QTuple>& out){
    if(pos==10){
        if(rem==0){ int sq=0; for(int x:q) sq+=x*x; out.push_back({q,sq}); }
        return;
    }
    int slots=9-pos;
    for(int x=last;x<=min(qmax,rem);++x){
        int rr=rem-x;
        if(rr<x*slots || rr>qmax*slots) continue;
        q[pos]=x;
        gen_q(pos+1,x,rr,qmax,q,out);
    }
}

static const vector<QTuple>& qtuples(int total,int qmax){
    auto key=make_pair(total,qmax);
    auto it=qcache.find(key);
    if(it!=qcache.end()) return it->second;
    array<int,10> q{}; vector<QTuple> out;
    gen_q(0,0,total,qmax,q,out);
    return qcache.emplace(key,move(out)).first->second;
}

static vector<vector<int>> parts(int total,int n,int maxv){
    vector<vector<int>> out,prefixes;
    vector<int> pref;
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

static array<int,13> pmax3(const array<int,5>& H,int qmax){
    array<int,13> out; out.fill(-1);
    for(int q=0;q<=qmax;++q){
        int cap=min(5,17-q),best=-1;
        for(int p=0;p<=cap;++p){
            if(q==0){ best=p; continue; }
            int L=max({0,p-2,q+p-13});
            if(L==0 || (L<=4 && q<=H[L])) best=p;
        }
        out[q]=best;
    }
    return out;
}

static array<int,5> pmax2(const array<int,4>& H2){
    array<int,5> out; out.fill(-1);
    for(int q=0;q<=4;++q){
        int cap=min(4,17-q),best=-1;
        for(int p=0;p<=cap;++p){
            if(q==0){ best=p; continue; }
            int L=max({0,p-1,q+p-13});
            if(L==0 || (L<=3 && q<=H2[L])) best=p;
        }
        out[q]=best;
    }
    return out;
}

struct SolveResult { bool feasible=false; int best=INT_MAX; int baseline=0; };

static SolveResult solve_profile(const vector<int>& e2,const vector<int>& e3){
    int E=accumulate(e2.begin(),e2.end(),0)+accumulate(e3.begin(),e3.end(),0);
    int Q=41+E, need=Q-21, baseline=3*(80+E);

    // Source-count impossibilities.
    for(int e:e3) if(e>7) return {false,INT_MAX,baseline};
    for(int e:e2) if(e>9) return {false,INT_MAX,baseline};

    array<int,5> H{}; array<int,4> H2{};
    for(int l=1;l<=4;++l){
        for(int e:e2) H[l]+=(e>=l);
        for(int e:e3) H[l]+=(e>=l);
    }
    for(int l=1;l<=3;++l) for(int e:e2) H2[l]+=(e>=l);

    int xmax=0;
    for(int e:e2) xmax=max(xmax,2+e);
    for(int e:e3) xmax=max(xmax,3+e);
    int qmax=0;
    for(int q=0;q<=12;++q) if(q*max(0,q-xmax)<=39) qmax=q;

    auto p3=pmax3(H,qmax); auto p2=pmax2(H2);
    int z0=count(e2.begin(),e2.end(),0), hpos=4-z0;

    vector<tuple<int,int,int>> d3,d2;
    for(int e:e3) if(e>=1) d3.push_back({e,3+e,e});
    for(int e:e2) if(e>=2) d2.push_back({e,2+e,e-1});

    int best=INT_MAX; bool feasible=false;
    for(int q2=0;q2<=4;++q2){
        int pm2=p2[q2]; if(pm2<0) continue;
        int target=Q-q2;
        for(const auto& qt:qtuples(target,qmax)){
            int caps[10],capsum=0; bool ok=true;
            for(int j=0;j<10;++j){
                caps[j]=p3[qt.q[j]];
                if(caps[j]<0){ ok=false; break; }
                capsum+=caps[j];
            }
            if(!ok) continue;

            int Pplus=0;
            for(auto [e,k,w]:d3){
                if(k>10 || qt.q[10-k]<=0){ ok=false; break; }
                Pplus+=w*(e+2+qt.q[10-k]);
            }
            if(!ok) continue;

            array<int,11> all{};
            for(int j=0;j<10;++j) all[j]=qt.q[j];
            all[10]=q2;
            sort(all.begin(),all.end(),greater<int>());
            for(auto [e,k,w]:d2){
                if(k>11 || all[k-1]<=0){ ok=false; break; }
                Pplus+=w*(e+2+all[k-1]);
            }
            if(!ok) continue;

            for(int pp2=0;pp2<=pm2;++pp2){
                int rem=max(0,need-pp2);
                if(rem>capsum) continue;
                int left=rem,pcost=0;
                // q-vector is nondecreasing: greedy incoming placement is exact.
                for(int j=0;j<10 && left;++j){
                    int take=min(left,caps[j]);
                    pcost+=qt.q[j]*take;
                    left-=take;
                }
                if(left) continue;

                int T=q2*q2+qt.sq+q2*pp2+pcost;
                int C0=2*z0+max(0,q2-hpos)*max(0,q2+pp2-2);
                int B=T+C0-Pplus;
                feasible=true;
                best=min(best,B);
            }
        }
    }
    return {feasible,best,baseline};
}

struct Row { int E,profiles,strict,equality,source_infeasible,min_strict_gap; };

static Row scan(int E){
    int total=0,strict=0,equality=0,src=0,mingap=INT_MAX;
    for(int e2tot=0;e2tot<=E;++e2tot){
        auto p2s=parts(e2tot,4,E);
        auto p3s=parts(E-e2tot,11,E);
        for(const auto& e2:p2s) for(const auto& e3:p3s){
            ++total;
            auto s=solve_profile(e2,e3);
            if(!s.feasible){ ++src; continue; }
            int gap=s.best-s.baseline;
            assert(gap>=0);
            if(gap==0) ++equality;
            else { ++strict; mingap=min(mingap,gap); }
        }
    }
    return {E,total,strict,equality,src,mingap==INT_MAX?0:mingap};
}

int main(){
    const vector<Row> expected={
        {0,1,1,0,0,1},{1,2,2,0,0,5},{2,5,5,0,0,9},{3,10,10,0,0,7},
        {4,20,20,0,0,6},{5,35,35,0,0,4},{6,62,61,1,0,4},{7,102,101,1,0,8},
        {8,167,166,0,1,9},{9,262,259,0,3,10},{10,407,398,0,9,12},
        {11,614,593,0,21,13},{12,918,872,0,46,14},{13,1342,1251,0,91,22},
        {14,1944,1772,0,172,26},{15,2770,2463,0,307,26},{16,3912,3381,0,531,31},
        {17,5451,4567,0,884,38},{18,7536,6101,0,1435,34},
        {19,10303,8037,0,2266,40},{20,13984,10453,0,3531,44}
    };

    long long profiles=0,strict=0,src=0,eq=0;
    cout << "E profiles strict equality source_infeasible min_strict_gap\n";
    for(const auto& want:expected){
        Row got=scan(want.E);
        assert(tie(got.E,got.profiles,got.strict,got.equality,got.source_infeasible,got.min_strict_gap)
            ==tie(want.E,want.profiles,want.strict,want.equality,want.source_infeasible,want.min_strict_gap));
        cout<<got.E<<' '<<got.profiles<<' '<<got.strict<<' '<<got.equality<<' '
            <<got.source_infeasible<<' '<<got.min_strict_gap<<'\n';
        profiles+=got.profiles; strict+=got.strict; src+=got.source_infeasible; eq+=got.equality;
    }
    assert(profiles==49847 && strict==40548 && src==9297 && eq==2);
    cout << "PASS profiles=49847 strict=40548 source_infeasible=9297 equality=2\n";
    cout << "The two equality profiles are E=6 and E=7 and require the preserved hand-rigidity exclusions in EXCESS_SWEEP_TO_8.md.\n";
}
