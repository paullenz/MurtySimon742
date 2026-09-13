#include <algorithm>
#include <cassert>
#include <array>
#include <climits>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;
constexpr int M3=11,A=15,N2=2,N3=13;
struct QT{array<int,M3>q{};int sq=0;};static map<int,vector<QT>>qc;
static void genq(int p,int last,int rem,array<int,M3>&q,vector<QT>&o){if(p==M3){if(!rem){int s=0;for(int x:q)s+=x*x;o.push_back({q,s});}return;}int sl=M3-1-p;for(int x=last;x<=min(12,rem);++x){int rr=rem-x;if(rr<x*sl||rr>12*sl)continue;q[p]=x;genq(p+1,x,rr,q,o);}}
static const vector<QT>&qtuples(int t){auto it=qc.find(t);if(it!=qc.end())return it->second;array<int,M3>q{};vector<QT>o;genq(0,0,t,q,o);return qc.emplace(t,move(o)).first->second;}
static array<int,A+1> maxP(const array<int,M3>&q3,int q2,int E){vector<int>all(q3.begin(),q3.end());all.push_back(q2);sort(all.begin(),all.end(),greater<int>());array<int,M3>d{};for(int i=0;i<M3;++i)d[i]=q3[M3-1-i];vector<pair<int,int>>o2,o3;for(int e=0;e<=10;++e){int x=2+e;int w=(e>=2)?(e-1)*(e+2+all[x-1]):(e==0?-2:0);o2.push_back({e,w});}for(int e=0;e<=8;++e){int x=3+e;int w=e?e*(e+2+d[x-1]):0;o3.push_back({e,w});}const int NEG=-1000000000;vector<array<int,A+1>>dp(E+1),nd(E+1);for(auto&x:dp)x.fill(NEG);dp[0][0]=0;auto step=[&](auto&opt){for(auto&x:nd)x.fill(NEG);for(int se=0;se<=E;++se)for(int h=0;h<=A;++h)if(dp[se][h]>NEG)for(auto[e,w]:opt){if(se+e>E)continue;int nh=h+(e>=2);if(nh<=A)nd[se+e][nh]=max(nd[se+e][nh],dp[se][h]+w);}dp.swap(nd);};for(int i=0;i<N2;++i)step(o2);for(int i=0;i<N3;++i)step(o3);array<int,A+1>out;out.fill(NEG);for(int h=0;h<=A;++h)out[h]=dp[E][h];return out;}
int main(int argc,char**argv){
 struct Row{int E,h,gap,q2;};const vector<Row> expected={{16,4,-1,2},{17,4,3,2},{18,4,6,2},{19,4,6,2},{20,5,5,2},{21,5,3,2},{22,5,2,2},{23,5,12,2},{24,5,14,2},{25,6,12,2},{26,6,13,2},{27,6,14,2},{28,6,15,2},{29,6,16,2},{30,6,20,2},{31,7,34,2},{32,7,34,2},{33,7,42,2},{34,7,38,2}};
 if(argc!=2){cerr<<"usage: verify_state382_tail E  (16<=E<=34)\n";return 2;}int E=stoi(argv[1]);auto it=find_if(expected.begin(),expected.end(),[&](const Row&r){return r.E==E;});if(it==expected.end())return 2;int Q=43+E,base=3*(84+E),best=INT_MAX,bh=-1,bq2=-1;for(int q2=0;q2<=2;++q2){int t=Q-q2;if(t<0||t>132)continue;for(auto&qt:qtuples(t)){auto pp=maxP(qt.q,q2,E);for(int h=0;h<=A;++h){if(pp[h]<-100000000)continue;vector<pair<int,int>>src;for(int i=0;i<6;++i)src.push_back({0,3});src.push_back({q2,q2<=h?4:2});for(int q:qt.q)src.push_back({q,q<=h?5:3});sort(src.begin(),src.end());int left=Q,pc=0;for(auto[q,c]:src){int take=min(left,c);pc+=q*take;left-=take;if(!left)break;}if(left)continue;int gap=qt.sq+q2*q2+pc-pp[h]-base;if(gap<best){best=gap;bh=h;bq2=q2;}}}}
 assert(best==it->gap && bh==it->h && bq2==it->q2);if(E>=17)assert(best>0);cout<<"PASS E="<<E<<" h="<<bh<<" gap="<<best<<" q2="<<bq2<<"\n";
}
