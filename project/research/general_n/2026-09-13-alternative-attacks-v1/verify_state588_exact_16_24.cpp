#include <cassert>
#include <algorithm>
#include <array>
#include <climits>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std;
constexpr int M=12;
struct QT{array<int,M>q{};int sq=0;};static map<pair<int,int>,vector<QT>>qc;
static void genq(int p,int last,int rem,int qm,array<int,M>&q,vector<QT>&o){if(p==M){if(!rem){int z=0;for(int x:q)z+=x*x;o.push_back({q,z});}return;}int sl=M-1-p;for(int x=last;x<=min(qm,rem);++x){int rr=rem-x;if(rr<x*sl||rr>qm*sl)continue;q[p]=x;genq(p+1,x,rr,qm,q,o);}}
static const vector<QT>&qtuples(int tot,int qm){auto k=make_pair(tot,qm);auto it=qc.find(k);if(it!=qc.end())return it->second;array<int,M>q{};vector<QT>o;genq(0,0,tot,qm,q,o);return qc.emplace(k,move(o)).first->second;}
static vector<vector<int>>parts(int tot,int n,int mv){vector<vector<int>>o;vector<int>p;function<void(int,int,int)> rec=[&](int pos,int last,int rem){if(pos==n){if(!rem)o.push_back(p);return;}int sl=n-pos-1;for(int v=last;v<=min(mv,rem);++v){int rr=rem-v;if(rr<v*sl||rr>mv*sl)continue;p.push_back(v);rec(pos+1,v,rr);p.pop_back();}};rec(0,0,tot);return o;}
struct Sol{bool f=false;int best=INT_MAX,base=0;array<int,M>arg{};};
static Sol solve(const vector<int>&e3){int E=accumulate(e3.begin(),e3.end(),0),Q=45+E,base=3*(88+E);for(int e:e3)if(e>9)return {false,INT_MAX,base,{}};array<int,5>H{};for(int l=1;l<=4;++l)for(int e:e3)H[l]+=(e>=l);int xmax=0;for(int e:e3)xmax=max(xmax,3+e);int qmax=0;for(int q=0;q<=12;++q)if(q*max(0,q-xmax)<=43)qmax=q;array<int,13>pm;pm.fill(-1);for(int q=0;q<=qmax;++q){int cap=min(5,17-q),best=-1;for(int p=0;p<=cap;++p){if(!q){best=p;continue;}int L=max({0,p-2,q+p-13});if(L==0||(L<=4&&q<=H[L]))best=p;}pm[q]=best;}vector<tuple<int,int,int>>pos;for(int e:e3)if(e>=1)pos.push_back({3+e,e,e});int need=Q-19;bool f=false;int best=INT_MAX;array<int,M>ba{};for(auto&qt:qtuples(Q,qmax)){int caps[M],cs=0;bool ok=true;for(int j=0;j<M;++j){caps[j]=pm[qt.q[j]];if(caps[j]<0){ok=false;break;}cs+=caps[j];}if(!ok||need>cs)continue;int P=0;for(auto[k,e,w]:pos){if(k>M||qt.q[M-k]<=0){ok=false;break;}P+=w*(e+2+qt.q[M-k]);}if(!ok)continue;int left=need,pc=0;for(int j=0;j<M&&left;++j){int take=min(left,caps[j]);pc+=qt.q[j]*take;left-=take;}if(left)continue;int B=qt.sq+pc-P;f=true;if(B<best){best=B;ba=qt.q;}}return {f,best,base,ba};}
int main(){
    struct Want{int E,profiles,strict,eq,neg,src,minGap;};
    const vector<Want> expected={{16,200,200,0,0,0,17},{24,1009,793,0,0,216,32}};
    cout<<"E profiles strict equality negative src minGap\n";
    for(const auto&w:expected){auto ps=parts(w.E,15,9);int st=0,eq=0,neg=0,src=0,mg=INT_MAX;for(auto&e:ps){auto z=solve(e);if(!z.f){src++;continue;}int g=z.best-z.base;if(g>0){st++;mg=min(mg,g);}else if(!g)eq++;else neg++;}assert((int)ps.size()==w.profiles&&st==w.strict&&eq==w.eq&&neg==w.neg&&src==w.src&&mg==w.minGap);cout<<w.E<<' '<<ps.size()<<' '<<st<<' '<<eq<<' '<<neg<<' '<<src<<' '<<mg<<"\n";}
    cout<<"PASS E=16 and E=24: every excess profile is strictly excluded or source-infeasible.\n";
}
