#include <algorithm>
#include <cassert>
#include <array>
#include <climits>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std; constexpr int M3=11;
struct QT{array<int,M3>q{};int sq=0;}; static map<pair<int,int>,vector<QT>>qc;
static void genq(int p,int last,int rem,int qm,array<int,M3>&q,vector<QT>&o){if(p==M3){if(!rem){int s=0;for(int x:q)s+=x*x;o.push_back({q,s});}return;}int sl=M3-1-p;for(int x=last;x<=min(qm,rem);++x){int rr=rem-x;if(rr<x*sl||rr>qm*sl)continue;q[p]=x;genq(p+1,x,rr,qm,q,o);}}
static const vector<QT>&qtuples(int t,int qm){auto k=make_pair(t,qm);auto it=qc.find(k);if(it!=qc.end())return it->second;array<int,M3>q{};vector<QT>o;genq(0,0,t,qm,q,o);return qc.emplace(k,move(o)).first->second;}
static vector<vector<int>> parts(int total,int n,int mv){vector<vector<int>>o;vector<int>p;function<void(int,int,int)> rec=[&](int pos,int last,int rem){if(pos==n){if(!rem)o.push_back(p);return;}int sl=n-pos-1;for(int v=last;v<=min(mv,rem);++v){int rr=rem-v;if(rr<v*sl||rr>mv*sl)continue;p.push_back(v);rec(pos+1,v,rr);p.pop_back();}};rec(0,0,total);return o;}
struct Sol{bool f=false;int best=INT_MAX,base=0;vector<int>arg;};
static Sol solve(const vector<int>&e2,const vector<int>&e3){int E=accumulate(e2.begin(),e2.end(),0)+accumulate(e3.begin(),e3.end(),0),Q=43+E,base=3*(84+E);for(int e:e2)if(e>10)return{false,INT_MAX,base,{}};for(int e:e3)if(e>8)return{false,INT_MAX,base,{}};array<int,5>H{},H2{};for(int l=1;l<=4;++l){for(int e:e2){H[l]+=(e>=l);H2[l]+=(e>=l);}for(int e:e3)H[l]+=(e>=l);}int xmax=0;for(int e:e2)xmax=max(xmax,2+e);for(int e:e3)xmax=max(xmax,3+e);int qmax=0;for(int q=0;q<=12;++q)if(q*max(0,q-xmax)<=41)qmax=q;
 array<int,13>pm3;pm3.fill(-1);for(int q=0;q<=qmax;++q){int cap=min(5,17-q),best=-1;for(int p=0;p<=cap;++p){if(!q){best=p;continue;}int L=max({0,p-2,q+p-13});if(L==0||(L<=4&&q<=H[L]))best=p;}pm3[q]=best;}
 auto pm2=[&](int q){int cap=min(4,17-q),best=-1;for(int p=0;p<=cap;++p){if(!q){best=p;continue;}int L=max({0,p-1,q+p-13});if(L==0||(L<=4&&q<=H2[L]))best=p;}return best;};
 bool f=false;int bestB=INT_MAX;vector<int>arg;for(int q2=0;q2<=2;++q2){int p2=pm2(q2);if(p2<0)continue;int target=Q-q2;for(auto&qt:qtuples(target,qmax)){int caps[M3];bool ok=true;for(int j=0;j<M3;++j){caps[j]=pm3[qt.q[j]];if(caps[j]<0){ok=false;break;}}if(!ok)continue;int P=0;for(int e:e3)if(e>=1){int k=3+e;if(k>M3||qt.q[M3-k]<=0){ok=false;break;}P+=e*(e+2+qt.q[M3-k]);}if(!ok)continue;vector<int>all(qt.q.begin(),qt.q.end());all.push_back(q2);sort(all.begin(),all.end(),greater<int>());for(int e:e2)if(e>=2){int k=2+e;if(k>(int)all.size()||all[k-1]<=0){ok=false;break;}P+=(e-1)*(e+2+all[k-1]);}if(!ok)continue;struct Src{int q,cap;};vector<Src>src{{q2,p2}};for(int j=0;j<M3;++j)src.push_back({qt.q[j],caps[j]});sort(src.begin(),src.end(),[](auto&a,auto&b){return a.q<b.q;});int left=max(0,Q-18),pc=0,cs=0;for(auto&s:src)cs+=s.cap;if(left>cs)continue;for(auto&s:src){int take=min(left,s.cap);pc+=s.q*take;left-=take;if(!left)break;}if(left)continue;int z0=count(e2.begin(),e2.end(),0);int B=qt.sq+q2*q2+pc+2*z0-P;f=true;if(B<bestB){bestB=B;arg={q2};arg.insert(arg.end(),qt.q.begin(),qt.q.end());}}
 }return{f,bestB,base,arg};}
int main(int argc,char**argv){
 struct Row{int E,profiles,gap;}; const vector<Row> expected={{0,1,3},{1,2,6},{2,5,13},{3,9,8},{4,17,7},{5,28,5},{6,47,3},{7,73,3},{8,114,7},{9,169,5},{10,250,8},{11,356,10},{12,505,4},{13,697,15},{14,956,18},{15,1284,17},{16,1713,17},{17,2246,21}};
 if(argc!=2){cerr<<"usage: verify_state382_low E  (0<=E<=17)\n";return 2;}int E=stoi(argv[1]);auto it=find_if(expected.begin(),expected.end(),[&](const Row&r){return r.E==E;});if(it==expected.end())return 2;long long tot=0,st=0,eq=0,neg=0,src=0;int mg=INT_MAX,mf=INT_MAX;
 for(int t2=0;t2<=E;++t2){for(auto&e2:parts(t2,2,10))for(auto&e3:parts(E-t2,13,8)){tot++;auto z=solve(e2,e3);if(!z.f){src++;continue;}int g=z.best-z.base;mf=min(mf,g);if(g>0){st++;mg=min(mg,g);}else if(!g)eq++;else neg++;}}
 assert(tot==it->profiles && st==tot && eq==0 && neg==0 && src==0 && mg==it->gap && mf==it->gap);
 cout<<"PASS E="<<E<<" profiles="<<tot<<" minimum_gap="<<mg<<"\n";
}
