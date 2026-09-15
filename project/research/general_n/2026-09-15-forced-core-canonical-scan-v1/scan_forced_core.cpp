#include <algorithm>
#include <cassert>
#include <chrono>
#include <climits>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

struct Edge { int to, rev, cap; };
struct Dinic {
    vector<vector<Edge>> g; vector<int> level,it;
    explicit Dinic(int n):g(n),level(n),it(n){}
    void add(int u,int v,int cap){Edge a{v,(int)g[v].size(),cap},b{u,(int)g[u].size(),0};g[u].push_back(a);g[v].push_back(b);}
    bool bfs(int s,int t){fill(level.begin(),level.end(),-1);queue<int>q;level[s]=0;q.push(s);while(!q.empty()){int u=q.front();q.pop();for(auto const&e:g[u])if(e.cap&&level[e.to]<0){level[e.to]=level[u]+1;q.push(e.to);}}return level[t]>=0;}
    int dfs(int u,int t,int f){if(u==t)return f;for(int &k=it[u];k<(int)g[u].size();++k){Edge &e=g[u][k];if(!e.cap||level[e.to]!=level[u]+1)continue;int z=dfs(e.to,t,min(f,e.cap));if(z){e.cap-=z;g[e.to][e.rev].cap+=z;return z;}}return 0;}
    int flow(int s,int t){int ans=0;while(bfs(s,t)){fill(it.begin(),it.end(),0);while(int z=dfs(s,t,INT_MAX/4))ans+=z;}return ans;}
};
struct CEdge{int to,rev,cap,cost;};
struct MinCostFlow{
    vector<vector<CEdge>>g; explicit MinCostFlow(int n):g(n){}
    void add(int u,int v,int cap,int cost){CEdge a{v,(int)g[v].size(),cap,cost},b{u,(int)g[u].size(),0,-cost};g[u].push_back(a);g[v].push_back(b);}
    pair<int,long long> flow(int s,int t,int need){const long long INF=(1LL<<60);int sent=0;long long total=0;int n=g.size();while(sent<need){vector<long long>d(n,INF);vector<int>pv(n,-1),pe(n,-1);vector<char>inq(n,0);queue<int>q;d[s]=0;q.push(s);inq[s]=1;while(!q.empty()){int u=q.front();q.pop();inq[u]=0;for(int k=0;k<(int)g[u].size();++k){auto const&e=g[u][k];if(!e.cap||d[u]==INF)continue;long long nd=d[u]+e.cost;if(nd<d[e.to]){d[e.to]=nd;pv[e.to]=u;pe[e.to]=k;if(!inq[e.to]){inq[e.to]=1;q.push(e.to);}}}}if(d[t]==INF)break;int add=need-sent;for(int v=t;v!=s;v=pv[v])add=min(add,g[pv[v]][pe[v]].cap);for(int v=t;v!=s;v=pv[v]){CEdge&e=g[pv[v]][pe[v]];e.cap-=add;g[v][e.rev].cap+=add;}sent+=add;total+=1LL*add*d[t];}return{sent,total};}
};
struct State{int layer,id,a,b,t;vector<int>s,rho;};
struct Cls{int rho,cnt,qmax;};
static map<tuple<int,int,int>,vector<vector<int>>> part_cache;
static void gen_parts(int pos,int cnt,int last,int mx,int rem,vector<int>&cur,vector<vector<int>>&out){if(pos==cnt){if(rem==0)out.push_back(cur);return;}int left=cnt-pos-1;for(int x=last;x<=mx&&x<=rem;++x){int rr=rem-x;if(rr<x*left||rr>mx*left)continue;cur[pos]=x;gen_parts(pos+1,cnt,x,mx,rr,cur,out);}}
static const vector<vector<int>>& parts(int cnt,int mx,int sum){auto key=make_tuple(cnt,mx,sum);auto it=part_cache.find(key);if(it!=part_cache.end())return it->second;vector<vector<int>>out;if(cnt==0){if(sum==0)out.push_back({});}else if(sum>=0&&sum<=cnt*mx){vector<int>cur(cnt);gen_parts(0,cnt,0,mx,sum,cur,out);}return part_cache.emplace(key,move(out)).first->second;}
static void lowedge(Dinic&F,vector<int>&bal,int u,int v,int lo,int hi){assert(0<=lo&&lo<=hi);F.add(u,v,hi-lo);bal[u]-=lo;bal[v]+=lo;}
static bool variable_incidence(const State&st,const vector<int>&q,const vector<int>&rho){int n=q.size(),m=st.s.size(),S0=n+m,T0=S0+1,SS=T0+1,TT=SS+1;Dinic F(TT+1);vector<int>bal(TT+1,0);int Q=accumulate(q.begin(),q.end(),0);for(int u=0;u<n;++u)lowedge(F,bal,S0,u,q[u],q[u]);for(int u=0;u<n;++u)for(int i=0;i<m;++i)if(st.s[i]<=rho[u])lowedge(F,bal,u,n+i,0,1);for(int i=0;i<m;++i){int hi=0;for(int u=0;u<n;++u)if(st.s[i]<=rho[u])++hi;if(st.s[i]>hi)return false;lowedge(F,bal,n+i,T0,st.s[i],hi);}lowedge(F,bal,T0,S0,0,Q);int need=0;for(int v=0;v<=T0;++v){if(bal[v]>0){F.add(SS,v,bal[v]);need+=bal[v];}else if(bal[v]<0)F.add(v,TT,-bal[v]);}return F.flow(SS,TT)==need;}
static long long excess_envelope(const State&st,int E){if(any_of(st.s.begin(),st.s.end(),[](int x){return x<=0;}))return -1;const long long NEG=-(1LL<<50);vector<long long>dp(E+1,NEG);dp[0]=0;for(int s:st.s){int h=count_if(st.rho.begin(),st.rho.end(),[&](int r){return r>=s;});if(h<s)return NEG;int cap=h-s;vector<long long>ndp(E+1,NEG);for(int used=0;used<=E;++used)if(dp[used]>NEG/2)for(int e=0;e<=cap&&used+e<=E;++e)ndp[used+e]=max(ndp[used+e],dp[used]+1LL*(s+e)*e);dp.swap(ndp);}return dp[E];}
struct OD{vector<vector<unsigned char>>D;vector<int>pairdeg,P,c;bool pass=false;int margin=INT_MIN;};
static OD pair_capacity(const State&st,const vector<int>&q,const vector<int>&rho,int E){int n=q.size(),Q=accumulate(q.begin(),q.end(),0),z=count(st.s.begin(),st.s.end(),0);OD o;o.c.resize(n);for(int i=0;i<n;++i)o.c[i]=q[i]+rho[i];o.D.assign(n,vector<unsigned char>(n,0));for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(i!=j&&q[i]<=o.c[j]+1&&q[j]<=o.c[i])o.D[i][j]=1;o.pairdeg.assign(n,0);for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(o.D[i][j]||o.D[j][i]){++o.pairdeg[i];++o.pairdeg[j];}o.P.resize(n);long long sumP=0;bool nonneg=true;for(int i=0;i<n;++i){int p=min(rho[i]+st.b-st.a-1,st.b-1-q[i]);if(q[i]>0){int kstar=min(z,min(q[i],E));if(q[i]>kstar){int extra=(E-kstar)/(q[i]-kstar);p=min(p,rho[i]+extra-1);}}p=min(p,o.pairdeg[i]-q[i]);o.P[i]=p;if(p<0)nonneg=false;else sumP+=p;}o.margin=nonneg?(int)(sumP-Q):INT_MIN/2;o.pass=nonneg&&sumP>=Q;return o;}
static int pair_flow(const vector<int>&q,const OD&o){int n=q.size();vector<pair<int,int>>ps;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(o.D[i][j]||o.D[j][i])ps.push_back({i,j});int S=n+ps.size(),T=S+1;Dinic F(T+1);for(int i=0;i<n;++i)F.add(S,i,q[i]);for(int k=0;k<(int)ps.size();++k){auto[i,j]=ps[k];int x=n+k;if(o.D[i][j])F.add(i,x,1);if(o.D[j][i])F.add(j,x,1);F.add(x,T,1);}return F.flow(S,T);}
static pair<int,long long> target_cost_flow(const vector<int>&q,const vector<int>&rho,const OD&o,int Q){int n=q.size(),S=2*n,T=S+1;MinCostFlow F(T+1);for(int i=0;i<n;++i)F.add(S,i,q[i],0);for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(o.D[i][j])F.add(i,n+j,1,0);for(int j=0;j<n;++j){int freecap=min(max(0,o.P[j]),max(0,rho[j]-1));if(freecap)F.add(n+j,T,freecap,0);int paid=max(0,o.P[j]-freecap);if(paid)F.add(n+j,T,paid,q[j]);}return F.flow(S,T,Q);}

static pair<bool,int> core_partition(const vector<int>&caps,const vector<int>&loss,int h,int m){
    if(h<=0||m<=0)return {true,0};
    long long tot=0;for(int c:caps)tot+=min(c,m);if(tot<1LL*h*m)return {false,INT_MAX};
    map<vector<int>,int> dp;dp[vector<int>(h,0)]=0;
    for(size_t z=0;z<caps.size();++z){int cap=min(caps[z],m),w=loss.empty()?0:loss[z];map<vector<int>,int> nd=dp;for(auto const&kv:dp){auto const&st=kv.first;int base=kv.second;int last=-1;for(int j=0;j<h;++j){if(st[j]==last)continue;last=st[j];vector<int> ns=st;ns[j]=min(m,ns[j]+cap);sort(ns.begin(),ns.end());auto it=nd.find(ns);int nc=base+w;if(it==nd.end()||nc<it->second)nd[move(ns)]=nc;}}dp.swap(nd);}
    vector<int> target(h,m);auto it=dp.find(target);return it==dp.end()?make_pair(false,INT_MAX):make_pair(true,it->second);
}
struct CoreCert{bool reject=false;string why;int r=-1,h=0,u=0,tau=-1,raw=0,loss=0,demand=0;vector<int>cand,caps;};
static CoreCert forced_core_test(const State&st,const vector<int>&q,const vector<int>&rho){
    CoreCert best; set<int> rs(rho.begin(),rho.end());
    for(int r:rs){
        int h=count_if(st.s.begin(),st.s.end(),[&](int d){return d<=r;});if(h<=0)continue;
        vector<int> U;for(int u=0;u<(int)q.size();++u)if(rho[u]==r&&q[u]==h)U.push_back(u);if(U.empty())continue;int m=U.size();
        vector<char> isU(q.size(),0);for(int u:U)isU[u]=1;vector<int>cand,caps;
        for(int v=0;v<(int)q.size();++v){int c=rho[v]+st.b-st.a-1;if(!isU[v]&&q[v]<=h+r-1&&q[v]+rho[v]>=h-1&&c>0){cand.push_back(v);caps.push_back(c);}}
        vector<int> zero(caps.size(),0);auto [ok,zloss]=core_partition(caps,zero,h,m);
        if(!ok){best.reject=true;best.why="CAPACITY_PARTITION";best.r=r;best.h=h;best.u=m;best.cand=cand;best.caps=caps;return best;}
        set<int> taus;for(int d:st.s)if(d>r)taus.insert(d);
        for(int tau:taus){int raw=0;for(int v=0;v<(int)q.size();++v)if(rho[v]>=tau)raw+=q[v];int demand=0;for(int d:st.s)if(d>=tau)demand+=d;vector<int>loss;for(int v:cand)loss.push_back(rho[v]>=tau?max(0,q[v]-r):0);auto [ok2,minloss]=core_partition(caps,loss,h,m);assert(ok2);if(raw-minloss<demand){best.reject=true;best.why="HIGH_SQUEEZE";best.r=r;best.h=h;best.u=m;best.tau=tau;best.raw=raw;best.loss=minloss;best.demand=demand;best.cand=cand;best.caps=caps;return best;}}
    }
    return best;
}

struct Result{long long profiles=0,paircap_fail=0,incidence_fail=0,pairhall_fail=0,targethall_fail=0,cost_fail=0,core_fail=0,core_capacity_fail=0,core_high_fail=0;long long paircap_pass=0,incidence_pass=0,pairhall_pass=0,targethall_pass=0,cost_pass=0;bool survives=false;int witness_E=-1;long long witness_cost=-1,witness_envelope=-1;vector<int>wq,wrho;int Emax=-1;double seconds=0;CoreCert lastcore;};
struct Scanner{
    const State&st;int S,Emax;vector<Cls>cls;vector<int>suffix;Result res;bool stop=false;
    explicit Scanner(const State&s):st(s){S=accumulate(st.s.begin(),st.s.end(),0);map<int,int>ct;for(int r:st.rho)++ct[r];for(auto [rho,cnt]:ct){int labels=count_if(st.s.begin(),st.s.end(),[&](int d){return d<=rho;});cls.push_back({rho,cnt,max(0,min(st.a-rho,labels))});}suffix.assign(cls.size()+1,0);for(int i=(int)cls.size()-1;i>=0;--i)suffix[i]=suffix[i+1]+cls[i].cnt*cls[i].qmax;int U=accumulate(st.rho.begin(),st.rho.end(),0)+st.b*(st.b-st.a-1);int Qmax=min({suffix[0],U,st.b*(st.b-1)/2});Emax=Qmax-S;res.Emax=Emax;}
    void eval(int E,const vector<int>&q,const vector<int>&rho,long long envelope){++res.profiles;int Q=S+E;CoreCert cc=forced_core_test(st,q,rho);if(cc.reject){++res.core_fail;if(cc.why=="CAPACITY_PARTITION")++res.core_capacity_fail;else ++res.core_high_fail;res.lastcore=cc;return;}OD o=pair_capacity(st,q,rho,E);if(!o.pass){++res.paircap_fail;return;}++res.paircap_pass;if(!variable_incidence(st,q,rho)){++res.incidence_fail;return;}++res.incidence_pass;if(pair_flow(q,o)<Q){++res.pairhall_fail;return;}++res.pairhall_pass;auto [f,cost]=target_cost_flow(q,rho,o,Q);if(f<Q){++res.targethall_fail;return;}++res.targethall_pass;if(envelope>=0&&cost>envelope){++res.cost_fail;return;}++res.cost_pass;res.survives=true;res.witness_E=E;res.witness_cost=cost;res.witness_envelope=envelope;res.wq=q;res.wrho=rho;stop=true;}
    void rec(int ci,int used,int Q,int E,long long envelope,vector<int>&q,vector<int>&rho){if(stop)return;if(ci==(int)cls.size()){if(used==Q)eval(E,q,rho,envelope);return;}auto C=cls[ci];int lo=max(0,Q-used-suffix[ci+1]),hi=min(C.cnt*C.qmax,Q-used);if(lo>hi)return;vector<int>sums;for(int sm=lo;sm<=hi;++sm)if(!parts(C.cnt,C.qmax,sm).empty())sums.push_back(sm);int rem=0;for(int j=ci;j<(int)cls.size();++j)rem+=cls[j].cnt;double tgt=rem?(double)(Q-used)*C.cnt/rem:0.0;stable_sort(sums.begin(),sums.end(),[&](int x,int y){return abs(x-tgt)<abs(y-tgt);});for(int sm:sums)for(auto const&pv:parts(C.cnt,C.qmax,sm)){size_t old=q.size();q.insert(q.end(),pv.begin(),pv.end());rho.insert(rho.end(),C.cnt,C.rho);rec(ci+1,used+sm,Q,E,envelope,q,rho);q.resize(old);rho.resize(old);if(stop)return;}}
    Result run(){auto t0=chrono::steady_clock::now();vector<int>q,rho;if(Emax>=0)for(int E=0;E<=Emax&&!stop;++E){long long env=excess_envelope(st,E);if(env==-(1LL<<50))continue;rec(0,0,S+E,E,env,q,rho);}res.seconds=chrono::duration<double>(chrono::steady_clock::now()-t0).count();return res;}
};
static string vs(const vector<int>&v){ostringstream o;for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}return o.str();}
int main(int argc,char**argv){if(argc<3){cerr<<"usage: scan_forced_core INPUT OUTPUT.tsv\n";return 2;}ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;int N;in>>N;out<<"layer\tstate_id\tS\tEmax\tprofiles_tested\tpaircap_fail\tpaircap_pass\tincidence_fail\tincidence_pass\tpairhall_fail\tpairhall_pass\ttargethall_fail\ttargethall_pass\tcost_fail\tcost_pass\tcore_fail\tcore_capacity_fail\tcore_high_fail\tstatus\twitness_E\twitness_cost\twitness_envelope\tseconds\twitness_rho\twitness_q\tlast_core_reason\tlast_core_r\tlast_core_h\tlast_core_U\tlast_core_tau\tlast_core_raw\tlast_core_loss\tlast_core_demand\n";int excluded=0,survived=0;long long profiles=0;for(int z=0;z<N;++z){State st;int ns,nr;in>>st.layer>>st.id>>st.a>>st.b>>st.t>>ns;st.s.resize(ns);for(int&x:st.s)in>>x;in>>nr;st.rho.resize(nr);for(int&x:st.rho)in>>x;Scanner sc(st);Result r=sc.run();string status=r.survives?"SURVIVES_FORCED_CORE":"FORCED_CORE_EXCLUDED";if(r.survives)++survived;else++excluded;profiles+=r.profiles;out<<st.layer<<'\t'<<st.id<<'\t'<<accumulate(st.s.begin(),st.s.end(),0)<<'\t'<<r.Emax<<'\t'<<r.profiles<<'\t'<<r.paircap_fail<<'\t'<<r.paircap_pass<<'\t'<<r.incidence_fail<<'\t'<<r.incidence_pass<<'\t'<<r.pairhall_fail<<'\t'<<r.pairhall_pass<<'\t'<<r.targethall_fail<<'\t'<<r.targethall_pass<<'\t'<<r.cost_fail<<'\t'<<r.cost_pass<<'\t'<<r.core_fail<<'\t'<<r.core_capacity_fail<<'\t'<<r.core_high_fail<<'\t'<<status<<'\t'<<r.witness_E<<'\t'<<r.witness_cost<<'\t'<<r.witness_envelope<<'\t'<<r.seconds<<'\t'<<vs(r.wrho)<<'\t'<<vs(r.wq)<<'\t'<<r.lastcore.why<<'\t'<<r.lastcore.r<<'\t'<<r.lastcore.h<<'\t'<<r.lastcore.u<<'\t'<<r.lastcore.tau<<'\t'<<r.lastcore.raw<<'\t'<<r.lastcore.loss<<'\t'<<r.lastcore.demand<<'\n';cerr<<"state "<<st.layer<<":"<<st.id<<" "<<status<<" E="<<r.witness_E<<" profiles="<<r.profiles<<" oldpass="<<r.cost_pass<<" corefail="<<r.core_fail<<" sec="<<r.seconds<<"\n";}cerr<<"SUMMARY states="<<N<<" forced_core_excluded="<<excluded<<" survives="<<survived<<" profiles="<<profiles<<"\n";}
