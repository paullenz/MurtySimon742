#include <cassert>
#include <algorithm>
#include <array>
#include <climits>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;
constexpr int M3=11, A=15;
struct QT{array<int,M3>q{};int sq=0;}; static map<int,vector<QT>> qc;
static void genq(int p,int last,int rem,array<int,M3>&q,vector<QT>&o){
 if(p==M3){if(rem==0){int s=0;for(int x:q)s+=x*x;o.push_back({q,s});}return;}
 int sl=M3-1-p; for(int x=last;x<=min(12,rem);++x){int rr=rem-x; if(rr<x*sl||rr>12*sl)continue;q[p]=x;genq(p+1,x,rr,q,o);} }
static const vector<QT>& qtuples(int t){auto it=qc.find(t);if(it!=qc.end())return it->second;array<int,M3>q{};vector<QT>o;genq(0,0,t,q,o);return qc.emplace(t,move(o)).first->second;}
static array<int,A+1> maxP(const array<int,M3>&q3,int q2a,int q2b,int E){
 vector<int> qall(q3.begin(),q3.end()); qall.push_back(q2a);qall.push_back(q2b); sort(qall.begin(),qall.end(),greater<int>());
 array<int,M3> desc{};for(int i=0;i<M3;++i)desc[i]=q3[M3-1-i];
 vector<pair<int,int>> opt2,opt3;
 for(int e=0;e<=11;++e){int x=2+e;if(x>13)continue;int w=(e>=2)?(e-1)*(e+2+qall[x-1]):0;opt2.push_back({e,w});}
 for(int e=0;e<=8;++e){int x=3+e;if(x>M3)continue;int w=(e>=1)?e*(e+2+desc[x-1]):0;opt3.push_back({e,w});}
 const int NEG=-1000000000;vector<array<int,A+1>>dp(E+1),nd(E+1);for(auto&x:dp)x.fill(NEG);dp[0][0]=0;
 auto step=[&](const vector<pair<int,int>>&opt){for(auto&x:nd)x.fill(NEG);for(int se=0;se<=E;++se)for(int h=0;h<=A;++h)if(dp[se][h]>NEG)for(auto[e,w]:opt){if(se+e>E)continue;int nh=h+(e>=2);if(nh<=A)nd[se+e][nh]=max(nd[se+e][nh],dp[se][h]+w);}dp.swap(nd);};
 step(opt2);for(int i=0;i<14;++i)step(opt3);array<int,A+1>out;out.fill(NEG);for(int h=0;h<=A;++h)out[h]=dp[E][h];return out;
}
int main(int argc,char**argv){
 struct Row{int E,h,gap,q2;};
 const vector<Row> expected={
  {16,4,0,2},{17,4,5,2},{18,4,8,2},{19,5,8,2},{20,5,8,2},{21,5,7,2},{22,5,6,2},{23,5,10,2},{24,6,10,2},{25,6,13,2},{26,6,16,2},{27,6,18,2},{28,6,22,2},{29,6,25,2},{30,6,28,2},{31,7,40,2},{32,7,40,2},{33,7,44,2},{34,7,42,2}
 };
 if(argc!=2){cerr<<"usage: verify_state526_tail E  (16<=E<=34)\n";return 2;}
 int E=stoi(argv[1]); auto it=find_if(expected.begin(),expected.end(),[&](const Row&r){return r.E==E;}); if(it==expected.end()) return 2; const Row&w=*it;
 int Q=44+E,base=3*(86+E),best=INT_MAX,bh=-1,bq2=-1;
 for(int q2a=0;q2a<=1;++q2a)for(int q2b=q2a;q2b<=1;++q2b){int t3=Q-q2a-q2b;if(t3<0||t3>132)continue;
  for(auto&qt:qtuples(t3)){auto pp=maxP(qt.q,q2a,q2b,E);for(int h=0;h<=A;++h){if(pp[h]<-100000000)continue;vector<pair<int,int>>src;for(int i=0;i<5;++i)src.push_back({0,3});src.push_back({q2a,q2a<=h?4:2});src.push_back({q2b,q2b<=h?4:2});for(int q:qt.q)src.push_back({q,q<=h?5:3});sort(src.begin(),src.end());int left=Q,pc=0;for(auto[q,c]:src){int take=min(left,c);pc+=q*take;left-=take;if(!left)break;}if(left)continue;int sq=qt.sq+q2a*q2a+q2b*q2b;int gap=sq+pc-pp[h]-base;if(gap<best){best=gap;bh=h;bq2=q2a+q2b;}}}
 }
 assert(best==w.gap && bh==w.h && bq2==w.q2); if(E>=17) assert(best>0);
 cout<<"PASS E="<<E<<" h="<<bh<<" gap="<<best<<" q2_total="<<bq2<<"\n";
}
