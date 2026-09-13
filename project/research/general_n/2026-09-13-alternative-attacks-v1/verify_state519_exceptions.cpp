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

// Exact source-availability replay for the only coarse nonpositive layers
// of N34 state 519: E=6,8,9.
// State: a=15,b=18,t=1, s=2,3^14, rho=1^6,3^12, r=42, S=44.
//
// When the unique demand-two label has e=0, it has x=2 and selected-excess
// forces p<=rho-1=2 at BOTH of its two distinct selected rho=3 sources.
// We enumerate that pair, their allowed p-values, and then greedily allocate
// the remaining incoming mass to the cheapest q sources.  The label endpoint
// load contributes C_2 >= max(q_i+p_i,q_j+p_j), retained jointly with T.

constexpr int M=12;
struct QT { array<int,M> q{}; int sq=0; };
static map<pair<int,int>,vector<QT>> qcache;

static void genq(int pos,int last,int rem,int qmax,array<int,M>&q,vector<QT>&out){
    if(pos==M){
        if(rem==0){ int sq=0; for(int x:q) sq+=x*x; out.push_back({q,sq}); }
        return;
    }
    int slots=M-pos-1;
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
    array<int,M> q{}; vector<QT> out;
    genq(0,0,total,qmax,q,out);
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

struct Sol { bool feasible=false; long long gap=LLONG_MAX; };

static Sol solve_profile(int e2,const vector<int>&e3){
    int E=e2+accumulate(e3.begin(),e3.end(),0);
    int Q=44+E;
    int base=3*(42+Q);

    array<int,20> H{};
    for(int l=1;l<20;++l){
        H[l]+=(e2>=l);
        for(int e:e3) H[l]+=(e>=l);
    }

    int xmax=max(2+e2,3);
    for(int e:e3) xmax=max(xmax,3+e);
    int qmax=0;
    for(int q=0;q<=12;++q)
        if(1LL*q*max(0,q-xmax)<=42) qmax=q;

    // Coarse residual support function.
    vector<pair<int,int>> labels;
    long long ucoarse=0;
    int x=2+e2;
    ucoarse+=1LL*x*x; labels.push_back({x,11});
    for(int e:e3){ x=3+e; ucoarse+=1LL*x*x; labels.push_back({x,10}); }
    sort(labels.begin(),labels.end(),[](auto&a,auto&b){ return a.first>b.first; });
    int rr=42;
    for(auto [xx,cap]:labels){ int take=min(rr,cap); ucoarse+=1LL*xx*take; rr-=take; if(!rr) break; }
    assert(rr==0);

    Sol best;
    for(const auto&qt:qtuples(Q,qmax)){
        array<int,M> pmax{};
        bool ok=true;
        for(int j=0;j<M;++j){
            int q=qt.q[j], cap=min(5,17-q), bp=-1;
            for(int p=0;p<=cap;++p){
                if(q==0){ bp=p; continue; }
                int L=max({0,p-2,q+p-13});
                if(L==0 || (L<20 && q<=H[L])) bp=p;
            }
            if(bp<0){ ok=false; break; }
            pmax[j]=bp;
        }
        if(!ok) continue;

        long long P=0;
        for(int e:e3) if(e>=1){
            int k=3+e;
            if(k>M || qt.q[M-k]<=0){ ok=false; break; }
            P+=1LL*e*(e+2+qt.q[M-k]);
        }
        if(!ok) continue;
        if(e2>=2){
            int k=2+e2;
            if(k>M || qt.q[M-k]<=0) continue;
            P+=1LL*(e2-1)*(e2+2+qt.q[M-k]);
        }

        // Six rho=1 sources (q=0) absorb at most 18 incoming units for free.
        int required=max(0,Q-18);
        long long pcost=LLONG_MAX;
        long long joint=LLONG_MAX; // min(sum q*p + retained lower bound on C_2)

        if(e2==0){
            // The zero-excess demand-two label must select two distinct
            // rho=3 sources.  At each selected incidence, p<=2.
            for(int i=0;i<M;++i) if(qt.q[i]>0)
                for(int j=i+1;j<M;++j) if(qt.q[j]>0)
                    for(int pi=0;pi<=min(pmax[i],2);++pi)
                        for(int pj=0;pj<=min(pmax[j],2);++pj){
                            int rem=required-pi-pj;
                            if(rem<0) rem=0;
                            long long cost=1LL*qt.q[i]*pi+1LL*qt.q[j]*pj;
                            vector<pair<int,int>> other;
                            for(int k=0;k<M;++k) if(k!=i && k!=j)
                                other.push_back({qt.q[k],pmax[k]});
                            sort(other.begin(),other.end());
                            for(auto [q,cap]:other){
                                int take=min(rem,cap); cost+=1LL*q*take; rem-=take; if(!rem) break;
                            }
                            if(rem) continue;
                            long long C2=max(qt.q[i]+pi,qt.q[j]+pj);
                            long long value=cost+C2;
                            if(value<joint){ joint=value; pcost=cost; }
                        }
            if(joint==LLONG_MAX) continue;
        } else {
            vector<pair<int,int>> src;
            int capacity=0;
            for(int j=0;j<M;++j){ src.push_back({qt.q[j],pmax[j]}); capacity+=pmax[j]; }
            if(required>capacity) continue;
            sort(src.begin(),src.end());
            int rem=required; long long cost=0;
            for(auto [q,cap]:src){ int take=min(rem,cap); cost+=1LL*q*take; rem-=take; if(!rem) break; }
            if(rem) continue;
            pcost=joint=cost;
        }

        long long T=qt.sq+pcost;
        long long gap_top=(e2==0 ? qt.sq+joint-P-base : T-P-base);
        long long gap_coarse=T-ucoarse;
        long long gap=max(gap_top,gap_coarse);
        best.feasible=true;
        best.gap=min(best.gap,gap);
    }
    return best;
}

int main(){
    struct Row { int E,profiles,strict,equality,negative,infeasible,minGap; };
    const vector<Row> expected={
        {6,30,30,0,0,0,2},
        {8,67,67,0,0,0,4},
        {9,97,97,0,0,0,2}
    };

    for(const auto&w:expected){
        long long total=0,strict=0,eq=0,neg=0,inf=0;
        long long mingap=LLONG_MAX;
        for(int e2=0;e2<=w.E;++e2)
            for(const auto&e3:parts(w.E-e2,14,12)){
                ++total;
                auto z=solve_profile(e2,e3);
                if(!z.feasible){ ++inf; continue; }
                mingap=min(mingap,z.gap);
                if(z.gap>0) ++strict; else if(z.gap==0) ++eq; else ++neg;
            }
        Row got{w.E,(int)total,(int)strict,(int)eq,(int)neg,(int)inf,(int)mingap};
        assert(tie(got.E,got.profiles,got.strict,got.equality,got.negative,got.infeasible,got.minGap)
            == tie(w.E,w.profiles,w.strict,w.equality,w.negative,w.infeasible,w.minGap));
        assert(got.minGap>0);
        cout<<"PASS E="<<got.E<<" profiles="<<got.profiles
            <<" minimum_gap="<<got.minGap<<'\n';
    }

    cout<<"PASS state 519 source-availability replay: all three coarse exceptional layers E=6,8,9 are strictly excluded.\n";
}
