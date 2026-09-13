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
static string qs(const array<int,M>&q){string s;for(int i=0;i<M;++i){if(i)s+=",";s+=to_string(q[i]);}return s;}
int main(){
    struct Row {int E,profiles,strict,equality,negative,src,minGap;};
    const vector<Row> expected={
      {0,1,1,0,0,0,6},{1,1,1,0,0,0,12},{2,2,2,0,0,0,17},{3,3,3,0,0,0,10},
      {4,5,5,0,0,0,9},{5,7,7,0,0,0,8},{6,11,11,0,0,0,3},{7,15,15,0,0,0,4},
      {8,22,22,0,0,0,5},{9,30,29,1,0,0,12},{10,41,41,0,0,0,7},{11,54,54,0,0,0,8},
      {12,73,73,0,0,0,6},{13,94,94,0,0,0,15},{14,123,123,0,0,0,16},{15,157,157,0,0,0,8}
    };
    cout<<"E profiles strict equality negative src minGap\n";
    for(const auto&w:expected){
        int E=w.E; auto ps=parts(E,15,9); long long st=0,eq=0,neg=0,src=0; int mg=INT_MAX;
        for(auto&e:ps){auto z=solve(e); if(!z.f){src++;continue;} int g=z.best-z.base;if(g>0){st++;mg=min(mg,g);} else if(!g){eq++;} else neg++;}
        Row got{E,(int)ps.size(),(int)st,(int)eq,(int)neg,(int)src,mg==INT_MAX?0:mg};
        assert(tie(got.E,got.profiles,got.strict,got.equality,got.negative,got.src,got.minGap)==tie(w.E,w.profiles,w.strict,w.equality,w.negative,w.src,w.minGap));
        cout<<got.E<<' '<<got.profiles<<' '<<got.strict<<' '<<got.equality<<' '<<got.negative<<' '<<got.src<<' '<<got.minGap<<"\n";
    }
    vector<int> eqprof(15,0); eqprof[12]=eqprof[13]=eqprof[14]=3;
    int E=9,Q=54,base=3*(88+E), countq=0; array<int,M> aq{};
    array<int,5> H{}; for(int l=1;l<=4;++l) for(int e:eqprof) H[l]+=(e>=l);
    int xmax=6, qmax=0; for(int q=0;q<=12;++q) if(q*max(0,q-xmax)<=43) qmax=q;
    array<int,13> pm; pm.fill(-1);
    for(int q=0;q<=qmax;++q){int cap=min(5,17-q),best=-1;for(int p=0;p<=cap;++p){if(q==0){best=p;continue;}int L=max({0,p-2,q+p-13});if(L==0||(L<=4&&q<=H[L]))best=p;}pm[q]=best;}
    for(const auto&qt:qtuples(Q,qmax)){
        int caps[M],cs=0; bool ok=true; for(int j=0;j<M;++j){caps[j]=pm[qt.q[j]];if(caps[j]<0){ok=false;break;}cs+=caps[j];} if(!ok||cs<35)continue;
        int P=3*3*(3+2+qt.q[M-6]); int left=35,pc=0; for(int j=0;j<M&&left;++j){int take=min(left,caps[j]);pc+=qt.q[j]*take;left-=take;} if(left)continue;
        int gap=qt.sq+pc-P-base; if(gap<=0){countq++;aq=qt.q;assert(gap==0);}
    }
    assert(countq==1);
    array<int,M> want{3,3,3,3,3,3,6,6,6,6,6,6}; assert(aq==want);
    cout<<"PASS low layers E=0..15; unique coarse equality is E=9, e=0^12,3^3, q=3^6,6^6.\n";
}
