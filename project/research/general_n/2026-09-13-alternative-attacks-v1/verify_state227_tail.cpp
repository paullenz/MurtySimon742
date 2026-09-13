// Exact finite replay of the h_2 high-excess relaxation for N34 state 227.
// Checks E=21,...,34 with integer arithmetic only.
#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;

struct QTuple { array<int,10> q{}; int sq=0; };
static map<int,vector<QTuple>> qcache;

static void gen_q(int pos,int last,int rem,array<int,10>& q,vector<QTuple>& out){
    if(pos==10){
        if(rem==0){ int sq=0; for(int x:q) sq+=x*x; out.push_back({q,sq}); }
        return;
    }
    int slots=9-pos;
    for(int x=last;x<=min(12,rem);++x){
        int rr=rem-x;
        if(rr<x*slots || rr>12*slots) continue;
        q[pos]=x;
        gen_q(pos+1,x,rr,q,out);
    }
}

static const vector<QTuple>& qtuples(int total){
    auto it=qcache.find(total);
    if(it!=qcache.end()) return it->second;
    array<int,10> q{}; vector<QTuple> out;
    gen_q(0,0,total,q,out);
    return qcache.emplace(total,move(out)).first->second;
}

// For fixed q-vector and total E, compute the exact maximum P_+ separately
// for each h=#{labels with e>=2}. Demand-two excess is bounded by 9 and
// demand-three excess by 7 because larger values require too many sources.
static array<int,16> max_pplus_by_h(const array<int,10>& qs,int q2,int E){
    array<int,10> desc3{};
    for(int i=0;i<10;++i) desc3[i]=qs[9-i];
    array<int,11> all{};
    for(int i=0;i<10;++i) all[i]=qs[i];
    all[10]=q2;
    sort(all.begin(),all.end(),greater<int>());

    vector<pair<int,int>> opt2,opt3;
    for(int e=0;e<=9;++e){
        int w=0;
        if(e>=2) w=(e-1)*(e+2+all[1+e]); // k=2+e -> zero-based k-1=1+e
        opt2.push_back({e,w});
    }
    for(int e=0;e<=7;++e){
        int w=0;
        if(e>=1) w=e*(e+2+desc3[2+e]); // k=3+e -> zero-based k-1=2+e
        opt3.push_back({e,w});
    }

    const int NEG=-1000000000;
    vector<vector<int>> dp(E+1,vector<int>(16,NEG));
    dp[0][0]=0;

    auto step=[&](const vector<pair<int,int>>& options){
        vector<vector<int>> nd(E+1,vector<int>(16,NEG));
        for(int s=0;s<=E;++s) for(int h=0;h<=15;++h){
            if(dp[s][h]<=NEG) continue;
            for(auto [e,w]:options){
                int ns=s+e, nh=h+(e>=2);
                if(ns<=E && nh<=15) nd[ns][nh]=max(nd[ns][nh],dp[s][h]+w);
            }
        }
        dp.swap(nd);
    };

    for(int z=0;z<4;++z) step(opt2);
    for(int z=0;z<11;++z) step(opt3);

    array<int,16> out{};
    for(int h=0;h<=15;++h) out[h]=dp[E][h];
    return out;
}

struct TailRow {
    int E,h,gap,q2,T,Pplus;
    array<int,10> q3{};
};

static TailRow solve_E(int E){
    int Q=41+E;
    int incoming_needed=Q-21;
    int best=INT_MAX,bh=-1,bq2=-1,bT=0,bP=0;
    array<int,10> bq{};

    for(int q2=0;q2<=4;++q2){
        for(const auto& qt:qtuples(Q-q2)){
            auto Ptable=max_pplus_by_h(qt.q,q2,E);
            for(int h=0;h<=15;++h){
                int P=Ptable[h];
                if(P<-100000000) continue;

                // High-excess relaxation:
                // rho=2 source: retain only basic p<=4;
                // rho=3 source: p<=5 if q<=h, else p<=3.
                vector<pair<int,int>> sources;
                sources.push_back({q2,4});
                for(int q:qt.q) sources.push_back({q,q<=h?5:3});
                sort(sources.begin(),sources.end());

                int left=incoming_needed,pcost=0;
                for(auto [q,cap]:sources){
                    int take=min(left,cap);
                    pcost+=q*take;
                    left-=take;
                    if(left==0) break;
                }
                if(left) continue;

                int T=q2*q2+qt.sq+pcost;
                int B=T-P;
                if(B<best){
                    best=B; bh=h; bq2=q2; bq=qt.q; bT=T; bP=P;
                }
            }
        }
    }
    return {E,bh,best-3*(80+E),bq2,bT,bP,bq};
}

int main(){
    const int expected_gap[35]={
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        8,13,14,15,15,15,15,26,32,40,44,39,34,56
    };
    const int expected_h[35]={
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        5,6,6,6,6,6,6,6,7,7,7,7,7,8
    };

    cout << "E h min_gap q2 T Pplus q3\n";
    for(int E=21;E<=34;++E){
        TailRow row=solve_E(E);
        assert(row.gap==expected_gap[E]);
        assert(row.h==expected_h[E]);
        assert(row.gap>0);
        cout<<row.E<<' '<<row.h<<' '<<row.gap<<' '<<row.q2<<' '
            <<row.T<<' '<<row.Pplus<<' ';
        for(int q:row.q3) cout<<q<<',';
        cout<<'\n';
    }

    // Basic incoming capacity over all 18 B-sources:
    // 7*(rho=1 cap 3) + 1*(rho=2 cap 4) + 10*(rho=3 cap 5)=75.
    assert(7*3+4+10*5==75);
    assert(41+35==76);
    cout << "PASS E=21..34 strict; E>=35 impossible because Q=41+E>75.\n";
}
