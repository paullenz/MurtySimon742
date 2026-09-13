#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <iostream>
#include <map>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

// Exact finite replay of the refined baseline-three / h_2 relaxation
// for N34 state 519 on E=25,...,34.
// State: a=15,b=18,t=1,s=2,3^14,rho=1^6,3^12,r=42,S=44.

const long long NEG=-(1LL<<55), INF=(1LL<<55);
struct QT { array<int,12> q{}; int sq=0; };
static map<int,vector<QT>> qcache;

static void genq(int pos,int last,int rem,array<int,12>&q,vector<QT>&out){
    if(pos==12){
        if(rem==0){ int sq=0; for(int x:q) sq+=x*x; out.push_back({q,sq}); }
        return;
    }
    int slots=11-pos;
    for(int x=last;x<=12 && x<=rem;++x){
        int rr=rem-x;
        if(rr<x*slots || rr>12*slots) continue;
        q[pos]=x; genq(pos+1,x,rr,q,out);
    }
}

static const vector<QT>& qtuples(int total){
    auto it=qcache.find(total); if(it!=qcache.end()) return it->second;
    array<int,12> q{}; vector<QT> out;
    genq(0,0,total,q,out);
    return qcache.emplace(total,move(out)).first->second;
}

// For fixed q-vector and E, maximize the baseline-three correction separately
// for each h=#{labels with e>=2}.  The single demand-two label uses the exact
// rho=3 score q+2 because state 519 has no rho=2 selected source class.
static array<long long,16> correction_by_h(const array<int,12>&q,int E){
    array<int,12> desc{};
    for(int i=0;i<12;++i) desc[i]=q[11-i];

    vector<pair<int,long long>> opt2,opt3;
    for(int e=0;e<=10;++e){
        long long w=0;
        int x=2+e;
        if(e==0) w=-2;
        else if(e>=2){
            if(x>12) continue;
            w=1LL*(e-1)*(e+2+desc[x-1]);
        }
        opt2.push_back({e,w});
    }
    for(int e=0;e<=9;++e){
        long long w=0;
        int x=3+e;
        if(e>=1){
            if(x>12) continue;
            w=1LL*e*(e+2+desc[x-1]);
        }
        opt3.push_back({e,w});
    }

    vector<vector<long long>> dp(E+1,vector<long long>(16,NEG));
    dp[0][0]=0;
    auto step=[&](const vector<pair<int,long long>>&options){
        vector<vector<long long>> nd(E+1,vector<long long>(16,NEG));
        for(int s=0;s<=E;++s) for(int h=0;h<=15;++h){
            if(dp[s][h]==NEG) continue;
            for(auto [e,w]:options){
                int ns=s+e, nh=h+(e>=2);
                if(ns<=E && nh<=15) nd[ns][nh]=max(nd[ns][nh],dp[s][h]+w);
            }
        }
        dp.swap(nd);
    };
    step(opt2);
    for(int z=0;z<14;++z) step(opt3);

    array<long long,16> out{};
    for(int h=0;h<=15;++h) out[h]=dp[E][h];
    return out;
}

struct Row { int E,h,gap; };

static Row solve_E(int E){
    int Q=44+E;
    long long base=3LL*(42+Q);
    long long best=INF;
    int besth=-1;

    for(const auto&qt:qtuples(Q)){
        auto corr=correction_by_h(qt.q,E);
        for(int h=0;h<=15;++h){
            if(corr[h]==NEG) continue;

            // Six rho=1 sources have q=0.  Generic h_2 cap:
            // q>h => p<=rho; otherwise p<=rho+2; always q+p<=17.
            vector<pair<int,int>> src;
            for(int z=0;z<6;++z) src.push_back({0,3});
            for(int q:qt.q){
                int cap=(q>h)?3:5;
                cap=min(cap,17-q);
                cap=max(cap,0);
                src.push_back({q,cap});
            }
            sort(src.begin(),src.end());

            int left=Q;
            long long pcost=0;
            for(auto [q,cap]:src){
                int take=min(left,cap);
                pcost+=1LL*q*take;
                left-=take;
                if(!left) break;
            }
            if(left) continue;

            long long gap=qt.sq+pcost-base-corr[h];
            if(gap<best){ best=gap; besth=h; }
        }
    }
    return {E,besth,(int)best};
}

int main(){
    const vector<Row> expected={
        {25,5,4},{26,6,5},{27,6,12},{28,6,2},{29,6,1},
        {30,6,2},{31,6,5},{32,6,10},{33,7,21},{34,7,20}
    };

    cout<<"E h minimum_gap\n";
    for(const auto&w:expected){
        Row got=solve_E(w.E);
        assert(tie(got.E,got.h,got.gap)==tie(w.E,w.h,w.gap));
        assert(got.gap>0);
        cout<<got.E<<' '<<got.h<<' '<<got.gap<<'\n';
    }

    // Basic incoming-capacity ceiling: rho=1 cap3, rho=3 cap5.
    // 6*3+12*5=78, while Q=44+E.  Therefore E>=35 gives Q>=79>78.
    assert(6*3+12*5==78);
    assert(44+35==79);
    cout<<"PASS state 519 refined tail E=25..34 strict; E>=35 impossible by incoming capacity.\n";
}
