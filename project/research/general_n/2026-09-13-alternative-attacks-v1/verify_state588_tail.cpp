#include <cassert>
#include <algorithm>
#include <array>
#include <climits>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;
constexpr int M=12,A=15;
struct QT{array<int,M>q{};int sq=0;};static map<int,vector<QT>>qc;
static void genq(int p,int last,int rem,array<int,M>&q,vector<QT>&o){if(p==M){if(!rem){int s=0;for(int x:q)s+=x*x;o.push_back({q,s});}return;}int sl=M-1-p;for(int x=last;x<=min(12,rem);++x){int rr=rem-x;if(rr<x*sl||rr>12*sl)continue;q[p]=x;genq(p+1,x,rr,q,o);}}
static const vector<QT>&qtuples(int t){auto it=qc.find(t);if(it!=qc.end())return it->second;array<int,M>q{};vector<QT>o;genq(0,0,t,q,o);return qc.emplace(t,move(o)).first->second;}
static array<int,A+1> maxP(const array<int,M>&q,int E){array<int,M>v{};for(int i=0;i<M;++i)v[i]=q[M-1-i]+2;vector<pair<int,int>>opt;for(int e=0;e<=9;++e){int x=3+e,w=e?e*(e+v[x-1]):0;opt.push_back({e,w});}const int NEG=-1000000000;vector<array<int,A+1>>dp(E+1),nd(E+1);for(auto&x:dp)x.fill(NEG);dp[0][0]=0;for(int z=0;z<15;++z){for(auto&x:nd)x.fill(NEG);for(int se=0;se<=E;++se)for(int h=0;h<=A;++h)if(dp[se][h]>NEG)for(auto[e,w]:opt){if(se+e>E)continue;int nh=h+(e>=2);nd[se+e][nh]=max(nd[se+e][nh],dp[se][h]+w);}dp.swap(nd);}array<int,A+1>out;out.fill(NEG);for(int h=0;h<=A;++h)out[h]=dp[E][h];return out;}
int main(){
    struct Row{int E,h,gap;};
    const vector<Row> expected={{16,4,-3},{17,4,1},{18,4,6},{19,5,8},{20,5,8},{21,5,6},{22,5,6},{23,5,4},{24,5,0},{25,5,14},{26,6,13},{27,6,6},{28,6,7},{29,6,8},{30,6,12},{31,6,18},{32,6,26},{33,7,31},{34,7,30}};
    cout<<"E h gap\n";
    for(const auto&w:expected){int E=w.E,Q=45+E,base=3*(88+E),best=INT_MAX,bh=-1;for(auto&qt:qtuples(Q)){auto pp=maxP(qt.q,E);for(int h=0;h<=A;++h){if(pp[h]<-100000000)continue;vector<pair<int,int>>src;for(int i=0;i<5;++i)src.push_back({0,3});src.push_back({0,4});for(int q:qt.q)src.push_back({q,q<=h?5:3});sort(src.begin(),src.end());int left=Q,pc=0;for(auto[q,c]:src){int take=min(left,c);pc+=q*take;left-=take;if(!left)break;}if(left)continue;int gap=qt.sq+pc-pp[h]-base;if(gap<best){best=gap;bh=h;}}}assert(best==w.gap&&bh==w.h);cout<<E<<' '<<bh<<' '<<best<<"\n";}
    cout<<"PASS h2 relaxation: all E=17..23 and 25..34 strict; only E=16 and E=24 need exact-profile replay.\n";
}
