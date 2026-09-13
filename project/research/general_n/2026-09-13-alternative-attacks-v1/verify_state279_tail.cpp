// Exact integer replay of the h_2 tail relaxation for N34 state 279.
// Checks E=16,...,34; E>=35 is then excluded by total incoming capacity.
#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;

struct QT { array<int,11> q{}; int sq=0; };
static map<int,vector<QT>> qcache;

static void genq(int pos,int last,int rem,array<int,11>&q,vector<QT>&out){
    if(pos==11){
        if(rem==0){ int sq=0; for(int x:q) sq+=x*x; out.push_back({q,sq}); }
        return;
    }
    int slots=10-pos;
    for(int x=last;x<=min(12,rem);++x){
        int rr=rem-x;
        if(rr<x*slots || rr>12*slots) continue;
        q[pos]=x;
        genq(pos+1,x,rr,q,out);
    }
}

static const vector<QT>& qtuples(int total){
    auto it=qcache.find(total);
    if(it!=qcache.end()) return it->second;
    array<int,11> q{}; vector<QT> out;
    genq(0,0,total,q,out);
    return qcache.emplace(total,move(out)).first->second;
}

static array<int,16> max_pplus_by_h(const array<int,11>&q,int E){
    array<int,11> v{};
    for(int i=0;i<11;++i) v[i]=q[10-i]+2;

    vector<pair<int,int>> opt2,opt3;
    for(int e=0;e<=9;++e){
        int x=2+e;
        int w=(e>=2)?(e-1)*(e+v[x-1]):0;
        opt2.push_back({e,w});
    }
    for(int e=0;e<=8;++e){
        int x=3+e;
        int w=(e>=1)?e*(e+v[x-1]):0;
        opt3.push_back({e,w});
    }

    const int NEG=-1000000000;
    vector<array<int,16>> dp(E+1),nd(E+1);
    for(auto&a:dp) a.fill(NEG);
    dp[0][0]=0;

    auto step=[&](const vector<pair<int,int>>&options){
        for(auto&a:nd) a.fill(NEG);
        for(int se=0;se<=E;++se) for(int h=0;h<=15;++h){
            if(dp[se][h]<=NEG) continue;
            for(auto [e,w]:options){
                if(se+e>E) continue;
                int nh=h+(e>=2);
                nd[se+e][nh]=max(nd[se+e][nh],dp[se][h]+w);
            }
        }
        dp.swap(nd);
    };

    for(int i=0;i<3;++i) step(opt2);
    for(int i=0;i<12;++i) step(opt3);

    array<int,16> out; out.fill(NEG);
    for(int h=0;h<=15;++h) out[h]=dp[E][h];
    return out;
}

struct Row { int E,h,gap; };

static Row solve(int E){
    int Q=42+E;
    int baseline=3*(82+E);
    int best=INT_MAX,besth=-1;

    for(const auto&qt:qtuples(Q)){
        auto pp=max_pplus_by_h(qt.q,E);
        for(int h=0;h<=15;++h){
            if(pp[h]<-100000000) continue;

            vector<pair<int,int>> sources;
            for(int i=0;i<7;++i) sources.push_back({0,3});
            for(int q:qt.q) sources.push_back({q,q<=h?5:3});
            sort(sources.begin(),sources.end());

            int left=Q,pcost=0;
            for(auto [q,cap]:sources){
                int take=min(left,cap);
                pcost+=q*take;
                left-=take;
                if(left==0) break;
            }
            if(left) continue;

            int gap=qt.sq+pcost-pp[h]-baseline;
            if(gap<best){ best=gap; besth=h; }
        }
    }
    return {E,besth,best};
}

int main(){
    const vector<Row> expected={
        {16,4,2},{17,4,7},{18,4,10},{19,5,10},{20,5,10},
        {21,5,9},{22,5,8},{23,5,12},{24,6,12},{25,6,15},
        {26,6,18},{27,6,20},{28,6,24},{29,6,27},{30,6,30},
        {31,7,42},{32,7,42},{33,7,46},{34,7,44}
    };

    cout << "E minimizing_h minimum_gap\n";
    for(const auto&w:expected){
        Row g=solve(w.E);
        assert(g.E==w.E && g.h==w.h && g.gap==w.gap);
        assert(g.gap>0);
        cout<<g.E<<' '<<g.h<<' '<<g.gap<<'\n';
    }

    assert(7*3+11*5==76);
    assert(42+35==77);
    cout << "PASS E=16..34 strict; E>=35 impossible because Q=42+E>76.\n";
}
