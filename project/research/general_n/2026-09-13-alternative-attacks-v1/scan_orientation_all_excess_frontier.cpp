#include <algorithm>
#include <cassert>
#include <chrono>
#include <climits>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

/*
All-excess orientation/selected-incidence relaxation.

Unlike scan_orientation_e0_frontier.cpp, this scanner does NOT fix x=s.
For each scalar state it quantifies all source selected-degree profiles q with
Q=sum q >= S=sum s, up to equal-rho permutation.  For a fixed q it asks only
for existence of some selected-label degrees x>=s, using an exact lower-bound
bipartite circulation.  It then imposes universal orientation pair/target Hall
conditions with only caps valid at every excess profile.

Thus ALL_EXCESS_EXCLUDED is a whole-scalar-state exclusion under the stated
canonical bridge constraints.  SURVIVES_RELAXATION is not graph feasibility.
*/

struct Edge{int to,rev,cap;};
struct Dinic{
    int n;vector<vector<Edge>>g;vector<int>lev,it;
    Dinic(int n):n(n),g(n),lev(n),it(n){}
    void add(int u,int v,int c){Edge a{v,(int)g[v].size(),c},b{u,(int)g[u].size(),0};g[u].push_back(a);g[v].push_back(b);}
    bool bfs(int s,int t){fill(lev.begin(),lev.end(),-1);queue<int>q;lev[s]=0;q.push(s);while(!q.empty()){int u=q.front();q.pop();for(auto const&e:g[u])if(e.cap&&lev[e.to]<0){lev[e.to]=lev[u]+1;q.push(e.to);}}return lev[t]>=0;}
    int dfs(int u,int t,int f){if(u==t)return f;for(int &k=it[u];k<(int)g[u].size();++k){Edge&e=g[u][k];if(!e.cap||lev[e.to]!=lev[u]+1)continue;int z=dfs(e.to,t,min(f,e.cap));if(z){e.cap-=z;g[e.to][e.rev].cap+=z;return z;}}return 0;}
    int flow(int s,int t){int a=0;while(bfs(s,t)){fill(it.begin(),it.end(),0);while(int z=dfs(s,t,INT_MAX/4))a+=z;}return a;}
};
struct State{int layer,id,a,b,t;vector<int>s,rho;};
struct Cls{int rho,cnt,qmax;};
static map<tuple<int,int,int>,vector<vector<int>>> cachep;
static void gp(int p,int n,int last,int mx,int rem,vector<int>&cur,vector<vector<int>>&out){if(p==n){if(rem==0)out.push_back(cur);return;}int left=n-p-1;for(int x=last;x<=mx&&x<=rem;++x){int rr=rem-x;if(rr<x*left||rr>mx*left)continue;cur[p]=x;gp(p+1,n,x,mx,rr,cur,out);}}
static const vector<vector<int>>& parts(int n,int mx,int sm){auto key=make_tuple(n,mx,sm);auto it=cachep.find(key);if(it!=cachep.end())return it->second;vector<vector<int>>o;if(n==0){if(sm==0)o.push_back({});}else if(sm>=0&&sm<=n*mx){vector<int>c(n);gp(0,n,0,mx,sm,c,o);}return cachep.emplace(key,move(o)).first->second;}

static void lower_edge(Dinic&F,vector<int>&bal,int u,int v,int lo,int hi){assert(0<=lo&&lo<=hi);F.add(u,v,hi-lo);bal[u]-=lo;bal[v]+=lo;}
static bool variable_incidence(const State&st,const vector<int>&q,const vector<int>&rho){
    int n=q.size(),m=st.s.size();int S0=n+m,T0=S0+1,SS=T0+1,TT=SS+1,N=TT+1;Dinic F(N);vector<int>bal(N,0);
    int Q=accumulate(q.begin(),q.end(),0);
    for(int u=0;u<n;++u)lower_edge(F,bal,S0,u,q[u],q[u]);
    for(int u=0;u<n;++u)for(int i=0;i<m;++i)if(st.s[i]<=rho[u])lower_edge(F,bal,u,n+i,0,1);
    for(int i=0;i<m;++i){int up=0;for(int u=0;u<n;++u)if(st.s[i]<=rho[u])++up;if(st.s[i]>up)return false;lower_edge(F,bal,n+i,T0,st.s[i],up);}
    lower_edge(F,bal,T0,S0,0,Q);
    int need=0;
    for(int v=0;v<=T0;++v){if(bal[v]>0){F.add(SS,v,bal[v]);need+=bal[v];}else if(bal[v]<0)F.add(v,TT,-bal[v]);}
    return F.flow(SS,TT)==need;
}

struct OD{vector<vector<unsigned char>>D;vector<int>deg,P,c;bool caps=true,prefix=true;};
static OD orient(const State&st,const vector<int>&q,const vector<int>&rho){int n=q.size(),Q=accumulate(q.begin(),q.end(),0);OD z;z.c.resize(n);for(int i=0;i<n;++i)z.c[i]=q[i]+rho[i];z.D.assign(n,vector<unsigned char>(n));for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(i!=j&&q[i]<=z.c[j]+1&&q[j]<=z.c[i])z.D[i][j]=1;z.deg.assign(n,0);for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(z.D[i][j]||z.D[j][i]){++z.deg[i];++z.deg[j];}z.P.resize(n);long long sp=0;for(int i=0;i<n;++i){int p=rho[i]+st.b-st.a-1;p=min(p,st.b-1-q[i]);p=min(p,z.deg[i]-q[i]);z.P[i]=p;if(p<0)z.caps=false;else sp+=p;}if(sp<Q)z.caps=false;if(z.caps){int mc=*max_element(z.c.begin(),z.c.end());for(int k=0;k<=mc;++k){long long v=0;for(int i=0;i<n;++i)if(q[i]<=k+1)v+=q[i];for(int j=0;j<n;++j)if(z.c[j]>k)v+=z.P[j];if(v<Q){z.prefix=false;break;}}}else z.prefix=false;return z;}
static int pairflow(const vector<int>&q,const OD&z){int n=q.size();vector<pair<int,int>>ps;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(z.D[i][j]||z.D[j][i])ps.push_back({i,j});int S=n+ps.size(),T=S+1;Dinic F(T+1);for(int i=0;i<n;++i)F.add(S,i,q[i]);for(int k=0;k<(int)ps.size();++k){auto[i,j]=ps[k];int x=n+k;if(z.D[i][j])F.add(i,x,1);if(z.D[j][i])F.add(j,x,1);F.add(x,T,1);}return F.flow(S,T);}
static int targetflow(const vector<int>&q,const OD&z){int n=q.size(),S=2*n,T=S+1;Dinic F(T+1);for(int i=0;i<n;++i)F.add(S,i,q[i]);for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(z.D[i][j])F.add(i,n+j,1);for(int j=0;j<n;++j)F.add(n+j,T,max(0,z.P[j]));return F.flow(S,T);}

struct Res{long long prof=0,incfail=0,capfail=0,prefixfail=0,pairfail=0,targetfail=0;bool pass=false;int wQ=-1;vector<int>wq,wrho;double sec=0;};
struct Scan{
    const State&st;int baseS,Qmax;vector<Cls>cs;vector<int>tailmax,highbase;Res r;bool stop=false;
    Scan(const State&s):st(s){baseS=accumulate(st.s.begin(),st.s.end(),0);map<int,int>ct;for(int x:st.rho)++ct[x];for(auto [rho,c]:ct){int m=0;for(int x:st.s)if(x<=rho)++m;cs.push_back({rho,c,min(st.a-rho,m)});}tailmax.assign(cs.size()+1,0);for(int i=(int)cs.size()-1;i>=0;--i)tailmax[i]=tailmax[i+1]+cs[i].cnt*cs[i].qmax;int rsum=accumulate(st.rho.begin(),st.rho.end(),0);long long pinc=rsum+1LL*st.b*(st.b-st.a-1);Qmax=min<long long>(tailmax[0],pinc);Qmax=min<long long>(Qmax,1LL*st.b*(st.b-1)/2);highbase.resize(cs.size());for(int i=0;i<(int)cs.size();++i){int R=cs[i].rho,h=0;for(int x:st.s)if(x>R)h+=x;highbase[i]=h;}}
    void eval(const vector<int>&q,const vector<int>&rho,int Q){++r.prof;if(!variable_incidence(st,q,rho)){++r.incfail;return;}OD z=orient(st,q,rho);if(!z.caps){++r.capfail;return;}if(!z.prefix){++r.prefixfail;return;}int pf=pairflow(q,z);if(pf<Q){++r.pairfail;return;}int tf=targetflow(q,z);if(tf<Q){++r.targetfail;return;}r.pass=true;r.wQ=Q;r.wq=q;r.wrho=rho;stop=true;}
    void rec(int ci,int used,int Q,vector<int>&q,vector<int>&rho){if(stop)return;if(ci==(int)cs.size()){if(used==Q)eval(q,rho,Q);return;}auto C=cs[ci];int lo=max(0,Q-used-tailmax[ci+1]),hi=min(C.cnt*C.qmax,Q-used); // Sources above this rho must still carry every base demand s>rho.
        hi=min(hi,Q-highbase[ci]-used);if(lo>hi)return;vector<int>sums;for(int sm=lo;sm<=hi;++sm)if(!parts(C.cnt,C.qmax,sm).empty())sums.push_back(sm);double tgt=(double)(Q-used)*C.cnt/max(1,accumulate(cs.begin()+ci,cs.end(),0,[](int z,const Cls&x){return z+x.cnt;}));stable_sort(sums.begin(),sums.end(),[&](int x,int y){return abs(x-tgt)<abs(y-tgt);});for(int sm:sums)for(auto const&pv:parts(C.cnt,C.qmax,sm)){size_t old=q.size();q.insert(q.end(),pv.begin(),pv.end());rho.insert(rho.end(),C.cnt,C.rho);rec(ci+1,used+sm,Q,q,rho);q.resize(old);rho.resize(old);if(stop)return;}}
    Res run(){auto t0=chrono::steady_clock::now();vector<int>q,rho;for(int Q=baseS;Q<=Qmax&&!stop;++Q)rec(0,0,Q,q,rho);r.sec=chrono::duration<double>(chrono::steady_clock::now()-t0).count();return r;}
};
static string vs(const vector<int>&v){ostringstream o;for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}return o.str();}
int main(int argc,char**argv){if(argc<3){cerr<<"usage: scan_orientation_all_excess_frontier INPUT OUTPUT.tsv\n";return 2;}ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;int N;in>>N;out<<"layer\tstate_id\tmax_s\tS\tprofiles_tested\tincidence_fail\tcap_fail\tprefix_fail\tpair_fail\ttarget_fail\tstatus\twitness_Q\tseconds\twitness_rho\twitness_q\n";int ex=0,su=0;for(int z=0;z<N;++z){State st;int ns,nr;in>>st.layer>>st.id>>st.a>>st.b>>st.t>>ns;st.s.resize(ns);for(int&i:st.s)in>>i;in>>nr;st.rho.resize(nr);for(int&i:st.rho)in>>i;Scan sc(st);Res r=sc.run();string status=r.pass?"SURVIVES_RELAXATION":"ALL_EXCESS_EXCLUDED";if(r.pass)++su;else ++ex;out<<st.layer<<'\t'<<st.id<<'\t'<<*max_element(st.s.begin(),st.s.end())<<'\t'<<accumulate(st.s.begin(),st.s.end(),0)<<'\t'<<r.prof<<'\t'<<r.incfail<<'\t'<<r.capfail<<'\t'<<r.prefixfail<<'\t'<<r.pairfail<<'\t'<<r.targetfail<<'\t'<<status<<'\t'<<r.wQ<<'\t'<<r.sec<<'\t'<<vs(r.wrho)<<'\t'<<vs(r.wq)<<'\n';cerr<<"state "<<st.id<<" "<<status<<" profiles="<<r.prof<<" Q="<<r.wQ<<" sec="<<r.sec<<"\n";}cerr<<"SUMMARY states="<<N<<" all_excess_excluded="<<ex<<" survives="<<su<<"\n";}
