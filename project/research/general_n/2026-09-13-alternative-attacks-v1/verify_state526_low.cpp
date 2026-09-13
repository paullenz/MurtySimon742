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
constexpr int M3=11;
struct QT{array<int,M3>q{};int sq=0;};static map<pair<int,int>,vector<QT>> qc;
static void genq(int p,int last,int rem,int qm,array<int,M3>&q,vector<QT>&o){if(p==M3){if(rem==0){int s=0;for(int x:q)s+=x*x;o.push_back({q,s});}return;}int sl=M3-1-p;for(int x=last;x<=min(qm,rem);++x){int rr=rem-x;if(rr<x*sl||rr>qm*sl)continue;q[p]=x;genq(p+1,x,rr,qm,q,o);}}
static const vector<QT>&qtuples(int total,int qm){auto k=make_pair(total,qm);auto it=qc.find(k);if(it!=qc.end())return it->second;array<int,M3>q{};vector<QT>o;genq(0,0,total,qm,q,o);return qc.emplace(k,move(o)).first->second;}
static vector<vector<int>>parts(int total,int n,int mv){vector<vector<int>>o;vector<int>p;function<void(int,int,int)>rec=[&](int pos,int last,int rem){if(pos==n){if(rem==0)o.push_back(p);return;}int sl=n-pos-1;for(int v=last;v<=min(mv,rem);++v){int rr=rem-v;if(rr<v*sl||rr>mv*sl)continue;p.push_back(v);rec(pos+1,v,rr);p.pop_back();}};rec(0,0,total);return o;}
struct Sol{bool f=false;int best=INT_MAX,base=0;vector<int>arg;};
static Sol solve(int e2,const vector<int>&e3){int E=e2+accumulate(e3.begin(),e3.end(),0),Q=44+E,base=3*(86+E);if(e2>11)return{false,INT_MAX,base,{}};for(int e:e3)if(e>8)return{false,INT_MAX,base,{}};array<int,5>H{};for(int l=1;l<=4;++l){H[l]+=(e2>=l);for(int e:e3)H[l]+=(e>=l);}array<int,5>H2{};for(int l=1;l<=4;++l)H2[l]=(e2>=l);int xmax=max(2+e2,3);for(int e:e3)xmax=max(xmax,3+e);int qmax=0;for(int q=0;q<=12;++q)if(q*max(0,q-xmax)<=42)qmax=q;
 array<int,13>pm3;pm3.fill(-1);for(int q=0;q<=qmax;++q){int cap=min(5,17-q),best=-1;for(int p=0;p<=cap;++p){if(q==0){best=p;continue;}int L=max({0,p-2,q+p-13});if(L==0||(L<=4&&q<=H[L]))best=p;}pm3[q]=best;}
 auto pm2=[&](int q){int cap=min(4,17-q),best=-1;for(int p=0;p<=cap;++p){if(q==0){best=p;continue;}int L=max({0,p-1,q+p-13});if(L==0||(L<=4&&q<=H2[L]))best=p;}return best;};
 bool f=false;int bestB=INT_MAX;vector<int>bestarg;
 for(int q2a=0;q2a<=1;++q2a)for(int q2b=q2a;q2b<=1;++q2b){int p2a=pm2(q2a),p2b=pm2(q2b);if(p2a<0||p2b<0)continue;int target=Q-q2a-q2b;for(const auto&qt:qtuples(target,qmax)){int caps[M3];bool ok=true;for(int j=0;j<M3;++j){caps[j]=pm3[qt.q[j]];if(caps[j]<0){ok=false;break;}}if(!ok)continue;
   int Pplus=0;for(int e:e3)if(e>=1){int k=3+e;if(k>M3||qt.q[M3-k]<=0){ok=false;break;}Pplus+=e*(e+2+qt.q[M3-k]);}if(!ok)continue;
   vector<int> qall(qt.q.begin(),qt.q.end());qall.push_back(q2a);qall.push_back(q2b);sort(qall.begin(),qall.end(),greater<int>());
   if(e2>=2){int k=2+e2;if(k>(int)qall.size()||qall[k-1]<=0)continue;Pplus+=(e2-1)*(e2+2+qall[k-1]);}
   struct Src{int q,cap;}; vector<Src> src;src.push_back({q2a,p2a});src.push_back({q2b,p2b});for(int j=0;j<M3;++j)src.push_back({qt.q[j],caps[j]});sort(src.begin(),src.end(),[](auto&a,auto&b){return a.q<b.q;});int left=max(0,Q-15),pc=0,cs=0;for(auto&s:src)cs+=s.cap;if(left>cs)continue;for(auto&s:src){int take=min(left,s.cap);pc+=s.q*take;left-=take;if(!left)break;}if(left)continue;
   int T=qt.sq+q2a*q2a+q2b*q2b+pc;int C0=(e2==0?2:0);int B=T+C0-Pplus;f=true;if(B<bestB){bestB=B;bestarg={q2a,q2b};bestarg.insert(bestarg.end(),qt.q.begin(),qt.q.end());}
 }}return{f,bestB,base,bestarg};}
int main(){
 struct Row {int E,profiles,strict,equality,negative,src,minGap,minFinite;};
 const vector<Row> expected={
  {0,1,1,0,0,0,4,4},{1,2,2,0,0,0,9,9},{2,4,4,0,0,0,15,15},{3,7,7,0,0,0,8,8},
  {4,12,12,0,0,0,8,8},{5,19,19,0,0,0,6,6},{6,30,30,0,0,0,3,3},{7,45,44,1,0,0,5,0},
  {8,67,67,0,0,0,5,5},{9,96,96,0,0,0,3,3},{10,136,136,0,0,0,5,5},{11,188,188,0,0,0,11,11},
  {12,257,257,0,0,0,7,7},{13,345,345,0,0,0,12,12},{14,459,459,0,0,0,18,18},{15,601,601,0,0,0,14,14},{16,780,780,0,0,0,23,23}
 };
 cout<<"E profiles strict equality negative src minGap minFinite\n";
 for(const auto&w:expected){long long total=0,st=0,eq=0,neg=0,src=0;int mg=INT_MAX,minf=INT_MAX;int eq_e2=-1;vector<int>eq_e3,eq_q;
  for(int e2=0;e2<=min(11,w.E);++e2){auto ps=parts(w.E-e2,14,8);for(auto&e3:ps){total++;auto z=solve(e2,e3);if(!z.f){src++;continue;}int g=z.best-z.base;minf=min(minf,g);if(g>0){st++;mg=min(mg,g);}else if(g==0){eq++;eq_e2=e2;eq_e3=e3;eq_q=z.arg;}else neg++;}}
  Row got{w.E,(int)total,(int)st,(int)eq,(int)neg,(int)src,mg==INT_MAX?0:mg,minf==INT_MAX?999:minf};
  assert(tie(got.E,got.profiles,got.strict,got.equality,got.negative,got.src,got.minGap,got.minFinite)==tie(w.E,w.profiles,w.strict,w.equality,w.negative,w.src,w.minGap,w.minFinite));
  cout<<got.E<<' '<<got.profiles<<' '<<got.strict<<' '<<got.equality<<' '<<got.negative<<' '<<got.src<<' '<<got.minGap<<' '<<got.minFinite<<"\n";
  if(w.E==7){assert(eq_e2==7);assert(all_of(eq_e3.begin(),eq_e3.end(),[](int x){return x==0;}));vector<int>wq={1,1,1,1,5,5,5,5,5,5,5,6,6};assert(eq_q==wq);}
 }
 // Dedicated uniqueness check for the E=7 coarse equality q-vector.
 int e2=7,E=7,Q=51,base=3*93,count_nonpositive=0;vector<int>e3(14,0),onlyq;
 array<int,5>H{};for(int l=1;l<=4;++l){H[l]+=(e2>=l);for(int e:e3)H[l]+=(e>=l);}array<int,5>H2{};for(int l=1;l<=4;++l)H2[l]=(e2>=l);int xmax=9,qmax=0;for(int q=0;q<=12;++q)if(q*max(0,q-xmax)<=42)qmax=q;
 array<int,13>pm3;pm3.fill(-1);for(int q=0;q<=qmax;++q){int cap=min(5,17-q),best=-1;for(int p=0;p<=cap;++p){if(q==0){best=p;continue;}int L=max({0,p-2,q+p-13});if(L==0||(L<=4&&q<=H[L]))best=p;}pm3[q]=best;}
 auto pm2=[&](int q){int cap=min(4,17-q),best=-1;for(int p=0;p<=cap;++p){if(q==0){best=p;continue;}int L=max({0,p-1,q+p-13});if(L==0||(L<=4&&q<=H2[L]))best=p;}return best;};
 for(int q2a=0;q2a<=1;++q2a)for(int q2b=q2a;q2b<=1;++q2b){int target=Q-q2a-q2b;for(const auto&qt:qtuples(target,qmax)){int caps[M3];bool ok=true;for(int j=0;j<M3;++j){caps[j]=pm3[qt.q[j]];if(caps[j]<0){ok=false;break;}}if(!ok)continue;vector<int>qall(qt.q.begin(),qt.q.end());qall.push_back(q2a);qall.push_back(q2b);sort(qall.begin(),qall.end(),greater<int>());if(qall[8]<=0)continue;int Pplus=6*(9+qall[8]);struct Src{int q,cap;};vector<Src>src{{q2a,pm2(q2a)},{q2b,pm2(q2b)}};for(int j=0;j<M3;++j)src.push_back({qt.q[j],caps[j]});sort(src.begin(),src.end(),[](auto&a,auto&b){return a.q<b.q;});int left=36,pc=0;for(auto&s:src){int take=min(left,s.cap);pc+=s.q*take;left-=take;if(!left)break;}if(left)continue;int T=qt.sq+q2a*q2a+q2b*q2b+pc;int gap=T-Pplus-base;if(gap<=0){assert(gap==0);count_nonpositive++;onlyq={q2a,q2b};onlyq.insert(onlyq.end(),qt.q.begin(),qt.q.end());}}}
 assert(count_nonpositive==1);vector<int>wq={1,1,1,1,5,5,5,5,5,5,5,6,6};assert(onlyq==wq);
 cout<<"PASS low layers E=0..16; unique coarse equality is E=7, e2=7, e3=0^14, q2=1^2, q3=1^2,5^7,6^2.\n";
}
