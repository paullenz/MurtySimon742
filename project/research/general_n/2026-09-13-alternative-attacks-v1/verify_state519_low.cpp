#include <algorithm>
#include <cassert>
#include <climits>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std;

// Exact integer profile replay for N34 state 519:
//   a=15,b=18,t=1, s=2,3^14, rho=1^6,3^12, r=42, S=44.
// This is a necessary-condition relaxation inside the canonical bridge.
// It combines the selected-excess/no-isolated-C source restriction,
// the residual-budget q cap, the coarse residual support function, and
// the refined baseline-three top-k envelope.

struct QT { vector<int> q; int sq=0; };
static map<tuple<int,int,int>,vector<QT>> qcache;

static void genq(int pos,int n,int last,int rem,int qmax,
                 vector<int>&q,vector<QT>&out){
    if(pos==n){
        if(rem==0){ int sq=0; for(int x:q) sq+=x*x; out.push_back({q,sq}); }
        return;
    }
    int slots=n-pos-1;
    for(int x=last;x<=min(qmax,rem);++x){
        int rr=rem-x;
        if(rr<x*slots || rr>qmax*slots) continue;
        q[pos]=x;
        genq(pos+1,n,x,rr,qmax,q,out);
    }
}

static const vector<QT>& qtuples(int n,int total,int qmax){
    auto key=make_tuple(n,total,qmax);
    auto it=qcache.find(key);
    if(it!=qcache.end()) return it->second;
    vector<int> q(n); vector<QT> out;
    genq(0,n,0,total,qmax,q,out);
    return qcache.emplace(key,move(out)).first->second;
}

static vector<vector<int>> parts(int total,int n,int maxv){
    vector<vector<int>> out; vector<int> p;
    function<void(int,int,int)> rec=[&](int pos,int last,int rem){
        if(pos==n){ if(rem==0) out.push_back(p); return; }
        int slots=n-pos-1;
        for(int v=last;v<=min(maxv,rem);++v){
            int rr=rem-v;
            if(rr<v*slots || rr>maxv*slots) continue;
            p.push_back(v); rec(pos+1,v,rr); p.pop_back();
        }
    };
    rec(0,0,total);
    return out;
}

struct State { int n2,n3,r1,r2,r3,S,r; };

static long long solve_profile(const State&st,const vector<int>&e2,
                               const vector<int>&e3){
    int E=accumulate(e2.begin(),e2.end(),0)+accumulate(e3.begin(),e3.end(),0);
    int Q=st.S+E;
    int base=3*(st.r+Q);

    int maxe=0,xmax=0;
    for(int e:e2){ maxe=max(maxe,e); xmax=max(xmax,2+e); }
    for(int e:e3){ maxe=max(maxe,e); xmax=max(xmax,3+e); }

    vector<int> H3(maxe+2),H2(maxe+2);
    for(int l=1;l<(int)H3.size();++l){
        for(int e:e2){ H3[l]+=(e>=l); H2[l]+=(e>=l); }
        for(int e:e3) H3[l]+=(e>=l);
    }

    // Residual-budget cap: r >= q*max(0,q-xmax).
    int qmax=0;
    for(int q=0;q<=12;++q)
        if(1LL*q*max(0,q-xmax)<=st.r) qmax=q;

    // For rho=2 or 3, selected labels at this source must all have
    // e_i >= L=max(0,p-rho+1,q+p-13).  The last term uses d_i<=13.
    auto pmax=[&](int q,int rho)->int{
        int cap=min(rho+2,17-q),best=-1;
        for(int p=0;p<=cap;++p){
            if(q==0){ best=p; continue; }
            int L=max({0,p-rho+1,q+p-13});
            const auto&H=(rho==2?H2:H3);
            if(L==0 || (L<(int)H.size() && q<=H[L])) best=p;
        }
        return best;
    };

    // Coarse support function: sum x_i^2 + max sum x_i R_i, with
    // sum R_i=r, R_i<=11 for demand two and <=10 for demand three.
    long long ucoarse=0;
    vector<pair<int,int>> labels;
    for(int e:e2){ int x=2+e; ucoarse+=1LL*x*x; labels.push_back({x,11}); }
    for(int e:e3){ int x=3+e; ucoarse+=1LL*x*x; labels.push_back({x,10}); }
    sort(labels.begin(),labels.end(),[](auto&a,auto&b){ return a.first>b.first; });
    int rr=st.r;
    for(auto [x,cap]:labels){
        int take=min(rr,cap); ucoarse+=1LL*x*take; rr-=take; if(!rr) break;
    }
    if(rr) return LLONG_MAX;

    long long best=LLONG_MAX;
    int qmax2=min(13,st.n2);
    for(int sum2=0;sum2<=st.r2*qmax2 && sum2<=Q;++sum2){
        int target=Q-sum2;
        if(target<0 || target>st.r3*qmax) continue;
        for(const auto&q2:qtuples(st.r2,sum2,qmax2)){
            vector<int> p2(st.r2); bool ok=true;
            for(int j=0;j<st.r2;++j){ p2[j]=pmax(q2.q[j],2); if(p2[j]<0) ok=false; }
            if(!ok) continue;

            for(const auto&q3:qtuples(st.r3,target,qmax)){
                vector<int> p3(st.r3);
                ok=true;
                for(int j=0;j<st.r3;++j){ p3[j]=pmax(q3.q[j],3); if(p3[j]<0){ok=false;break;} }
                if(!ok) continue;

                // Positive baseline-three correction, with exact top-k q bounds.
                long long P=0;
                for(int e:e3) if(e>=1){
                    int k=3+e;
                    if(k>st.r3 || q3.q[st.r3-k]<=0){ ok=false; break; }
                    P+=1LL*e*(e+2+q3.q[st.r3-k]);
                }
                if(!ok) continue;

                vector<int> all=q3.q;
                all.insert(all.end(),q2.q.begin(),q2.q.end());
                sort(all.begin(),all.end(),greater<int>());
                for(int e:e2) if(e>=2){
                    int k=2+e;
                    if(k>(int)all.size() || all[k-1]<=0){ ok=false; break; }
                    P+=1LL*(e-1)*(e+2+all[k-1]);
                }
                if(!ok) continue;

                struct Src { int q,cap; };
                vector<Src> src;
                for(int j=0;j<st.r2;++j) src.push_back({q2.q[j],p2[j]});
                for(int j=0;j<st.r3;++j) src.push_back({q3.q[j],p3[j]});
                sort(src.begin(),src.end(),[](auto&a,auto&b){ return a.q<b.q; });

                // rho=1 sources have q=0 and can absorb 3 incoming each at zero q*p cost.
                int left=max(0,Q-3*st.r1),capacity=0;
                for(auto&s:src) capacity+=s.cap;
                if(left>capacity) continue;
                long long pcost=0;
                for(auto&s:src){
                    int take=min(left,s.cap); pcost+=1LL*s.q*take; left-=take; if(!left) break;
                }
                if(left) continue;

                int z0=count(e2.begin(),e2.end(),0);
                long long T=q2.sq+q3.sq+pcost;
                long long gap_top=T+2LL*z0-P-base;
                long long gap_coarse=T-ucoarse;
                best=min(best,max(gap_top,gap_coarse));
            }
        }
    }
    return best;
}

int main(){
    const State st{1,14,6,0,12,44,42};
    struct Row { int E,profiles,strict,equality,negative,infeasible,minFinite; };
    const vector<Row> expected={
        {0,1,1,0,0,0,4},{1,2,2,0,0,0,9},{2,4,4,0,0,0,15},{3,7,7,0,0,0,7},
        {4,12,12,0,0,0,6},{5,19,19,0,0,0,3},{6,30,29,0,1,0,-2},{7,45,45,0,0,0,3},
        {8,67,66,1,0,0,0},{9,97,96,0,1,0,-2},{10,139,138,0,0,1,2},{11,195,191,0,0,4,6},
        {12,272,263,0,0,9,2},{13,371,355,0,0,16,8},{14,503,475,0,0,28,10},{15,672,626,0,0,46,7},
        {16,891,818,0,0,73,9},{17,1167,1055,0,0,112,3},{18,1519,1351,0,0,168,6},
        {19,1956,1709,0,0,247,12},{20,2504,2118,0,0,386,20},{21,3177,2478,0,0,699,13},
        {22,4007,3161,0,0,846,17},{23,5014,3228,0,0,1786,21},{24,6241,3816,0,0,2425,22}
    };

    cout<<"E profiles strict equality negative infeasible minFinite\n";
    for(const auto&w:expected){
        long long total=0,strict=0,eq=0,neg=0,inf=0;
        long long minf=LLONG_MAX;
        for(int t2=0;t2<=w.E;++t2){
            // maxv=12 is a safe superset; profiles requiring more eligible selected
            // sources are subsequently reported as source-infeasible.
            for(const auto&e2:parts(t2,st.n2,12))
                for(const auto&e3:parts(w.E-t2,st.n3,12)){
                    ++total;
                    long long g=solve_profile(st,e2,e3);
                    if(g==LLONG_MAX){ ++inf; continue; }
                    minf=min(minf,g);
                    if(g>0) ++strict; else if(g==0) ++eq; else ++neg;
                }
        }
        Row got{w.E,(int)total,(int)strict,(int)eq,(int)neg,(int)inf,(int)minf};
        assert(tie(got.E,got.profiles,got.strict,got.equality,got.negative,got.infeasible,got.minFinite)
            == tie(w.E,w.profiles,w.strict,w.equality,w.negative,w.infeasible,w.minFinite));
        cout<<got.E<<' '<<got.profiles<<' '<<got.strict<<' '<<got.equality<<' '
            <<got.negative<<' '<<got.infeasible<<' '<<got.minFinite<<'\n';
    }

    cout<<"PASS state 519 low/profile sweep E=0..24. Only coarse nonpositive profiles occur at E=6,8,9; dedicated availability replay must close those three layers.\n";
}
