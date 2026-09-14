#include <algorithm>
#include <chrono>
#include <climits>
#include <cmath>
#include <fstream>
#include <functional>
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
Independent cross-check for scan_post_pair_relational.cpp.

Differences from the primary implementation:
  * q-profiles are enumerated as multiplicities m_q inside each equal-rho class,
    rather than nondecreasing q-vectors;
  * potential-pair degrees are evaluated from the closed type-count formula,
    rather than constructing K_D pair-by-pair to obtain degrees;
  * min-cost target flow uses reduced-cost Dijkstra with vertex potentials,
    rather than the primary queue-based shortest-path routine.

The same mathematical relaxations are intentionally tested. On a fully
excluded state every admissible profile is exhausted, so the per-stage counts
must agree exactly with the primary implementation. A mismatch is an audit
failure and no closure may be promoted.
*/

struct State { int layer,id,a,b,t; vector<int>s,rho; };
struct Class { int rho,cnt,qmax; };
struct Type { int rho,q,count,c,dK,cap; };

struct Edge { int to, rev, cap; };
struct Dinic {
    vector<vector<Edge>> g; vector<int> level,it;
    explicit Dinic(int n):g(n),level(n),it(n){}
    void add(int u,int v,int cap){Edge a{v,(int)g[v].size(),cap},b{u,(int)g[u].size(),0};g[u].push_back(a);g[v].push_back(b);}
    bool bfs(int s,int t){fill(level.begin(),level.end(),-1);queue<int>q;level[s]=0;q.push(s);while(!q.empty()){int u=q.front();q.pop();for(auto const&e:g[u])if(e.cap&&level[e.to]<0){level[e.to]=level[u]+1;q.push(e.to);}}return level[t]>=0;}
    int dfs(int u,int t,int f){if(u==t)return f;for(int &k=it[u];k<(int)g[u].size();++k){Edge &e=g[u][k];if(!e.cap||level[e.to]!=level[u]+1)continue;int z=dfs(e.to,t,min(f,e.cap));if(z){e.cap-=z;g[e.to][e.rev].cap+=z;return z;}}return 0;}
    int flow(int s,int t){int ans=0;while(bfs(s,t)){fill(it.begin(),it.end(),0);while(int z=dfs(s,t,INT_MAX/4))ans+=z;}return ans;}
};

struct CEdge { int to,rev,cap,cost; };
struct MinCost {
    vector<vector<CEdge>> g;
    explicit MinCost(int n):g(n){}
    void add(int u,int v,int cap,int cost){CEdge a{v,(int)g[v].size(),cap,cost},b{u,(int)g[u].size(),0,-cost};g[u].push_back(a);g[v].push_back(b);}
    pair<int,long long> flow(int s,int t,int need){
        const long long INF=(1LL<<60);int n=g.size(),sent=0;long long total=0;vector<long long>pot(n,0);
        while(sent<need){
            vector<long long>d(n,INF);vector<int>pv(n,-1),pe(n,-1);priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<pair<long long,int>>>pq;
            d[s]=0;pq.push({0,s});
            while(!pq.empty()){
                auto [du,u]=pq.top();pq.pop();if(du!=d[u])continue;
                for(int k=0;k<(int)g[u].size();++k){auto const&e=g[u][k];if(!e.cap)continue;long long nd=du+e.cost+pot[u]-pot[e.to];if(nd<d[e.to]){d[e.to]=nd;pv[e.to]=u;pe[e.to]=k;pq.push({nd,e.to});}}
            }
            if(d[t]==INF)break;
            for(int v=0;v<n;++v)if(d[v]<INF)pot[v]+=d[v];
            int add=need-sent;for(int v=t;v!=s;v=pv[v])add=min(add,g[pv[v]][pe[v]].cap);
            long long path=0;for(int v=t;v!=s;v=pv[v]){CEdge &e=g[pv[v]][pe[v]];path+=e.cost;e.cap-=add;g[v][e.rev].cap+=add;}
            sent+=add;total+=1LL*add*path;
        }
        return {sent,total};
    }
};

static map<tuple<int,int,int>,vector<vector<int>>> dist_cache;
static void dist_rec(int q,int qmax,int left_count,int left_sum,vector<int>&cur,vector<vector<int>>&out){
    if(q==qmax){if(left_sum==q*left_count){cur[q]=left_count;out.push_back(cur);}return;}
    for(int m=0;m<=left_count;++m){int rc=left_count-m,rs=left_sum-q*m;if(rs<(q+1)*rc||rs>qmax*rc)continue;cur[q]=m;dist_rec(q+1,qmax,rc,rs,cur,out);}
}
static const vector<vector<int>>& distributions(int cnt,int qmax,int sum){
    auto key=make_tuple(cnt,qmax,sum);
    auto it=dist_cache.find(key);
    if(it!=dist_cache.end()) return it->second;
    vector<vector<int>> out;
    if(sum>=0&&sum<=cnt*qmax){
        if(qmax==0){
            if(sum==0) out.push_back(vector<int>{cnt});
        } else {
            vector<int> cur(qmax+1);
            dist_rec(0,qmax,cnt,sum,cur,out);
        }
    }
    return dist_cache.emplace(key,move(out)).first->second;
}

static long long excess_envelope(const State&st,int E){
    if(any_of(st.s.begin(),st.s.end(),[](int x){return x<=0;}))return -1;
    const long long NEG=-(1LL<<50);vector<long long>dp(E+1,NEG);dp[0]=0;
    for(int s:st.s){
        int h=count_if(st.rho.begin(),st.rho.end(),[&](int r){return r>=s;});
        if(h<s) return NEG;
        int cap=h-s;
        vector<long long> ndp(E+1,NEG);
        for(int used=0;used<=E;++used){
            if(dp[used]<=NEG/2) continue;
            for(int e=0;e<=cap&&used+e<=E;++e){
                ndp[used+e]=max(ndp[used+e],dp[used]+1LL*(s+e)*e);
            }
        }
        dp.swap(ndp);
    }
    return dp[E];
}

static void lowedge(Dinic&F,vector<int>&bal,int u,int v,int lo,int hi){F.add(u,v,hi-lo);bal[u]-=lo;bal[v]+=lo;}
static bool variable_incidence(const State&st,const vector<int>&q,const vector<int>&rho){
    int n=q.size(),m=st.s.size(),S=n+m,T=S+1,SS=T+1,TT=SS+1;Dinic F(TT+1);vector<int>bal(TT+1);int Q=accumulate(q.begin(),q.end(),0);
    for(int u=0;u<n;++u)lowedge(F,bal,S,u,q[u],q[u]);
    for(int u=0;u<n;++u)for(int i=0;i<m;++i)if(st.s[i]<=rho[u])lowedge(F,bal,u,n+i,0,1);
    for(int i=0;i<m;++i){int hi=0;for(int u=0;u<n;++u)if(st.s[i]<=rho[u])++hi;if(st.s[i]>hi)return false;lowedge(F,bal,n+i,T,st.s[i],hi);}
    lowedge(F,bal,T,S,0,Q);int need=0;for(int v=0;v<=T;++v){if(bal[v]>0){F.add(SS,v,bal[v]);need+=bal[v];}else if(bal[v]<0)F.add(v,TT,-bal[v]);}return F.flow(SS,TT)==need;
}

static bool compat_dir(int qu,int ru,int qw,int rw){return qu<=qw+rw+1 && qw<=qu+ru;}

struct PairEval { bool pass=false; vector<int>P; int margin=INT_MIN; };
static PairEval pair_capacity_types(const State&st,const vector<Type>&types,int E,vector<int>&q,vector<int>&rho){
    const int z=count(st.s.begin(),st.s.end(),0);vector<Type> tv=types;
    for(size_t i=0;i<tv.size();++i){long long weak=0,boundary=0;auto const&A=tv[i];for(auto const&B:tv){if(B.c>=A.q-1&&B.q<=A.c+1)weak+=B.count;if(B.c==A.q-1&&B.q==A.c+1)boundary+=B.count;}tv[i].dK=(int)(weak-1-boundary);}
    q.clear();rho.clear();vector<int>P;long long sumP=0;bool ok=true;int Q=0;
    for(auto const&A:tv){int p=min(A.rho+st.b-st.a-1,st.b-1-A.q);if(A.q>0){int kstar=min(z,min(A.q,E));if(A.q>kstar)p=min(p,A.rho+(E-kstar)/(A.q-kstar)-1);}p=min(p,A.dK-A.q);
        for(int k=0;k<A.count;++k){q.push_back(A.q);rho.push_back(A.rho);P.push_back(p);Q+=A.q;if(p<0)ok=false;else sumP+=p;}}
    PairEval ans;ans.P=move(P);ans.margin=ok?(int)(sumP-Q):INT_MIN/2;ans.pass=ok&&sumP>=Q;return ans;
}

static int pair_flow(const vector<int>&q,const vector<int>&rho){
    int n=q.size();vector<pair<int,int>>pairs;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(compat_dir(q[i],rho[i],q[j],rho[j])||compat_dir(q[j],rho[j],q[i],rho[i]))pairs.push_back({i,j});
    int S=n+pairs.size(),T=S+1;Dinic F(T+1);for(int i=0;i<n;++i)F.add(S,i,q[i]);for(int k=0;k<(int)pairs.size();++k){auto [i,j]=pairs[k];int x=n+k;if(compat_dir(q[i],rho[i],q[j],rho[j]))F.add(i,x,1);if(compat_dir(q[j],rho[j],q[i],rho[i]))F.add(j,x,1);F.add(x,T,1);}return F.flow(S,T);
}

static pair<int,long long> target_cost_flow(const vector<int>&q,const vector<int>&rho,const vector<int>&P,int Q){
    int n=q.size(),S=2*n,T=S+1;MinCost F(T+1);for(int i=0;i<n;++i)F.add(S,i,q[i],0);
    for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(i!=j&&compat_dir(q[i],rho[i],q[j],rho[j]))F.add(i,n+j,1,0);
    for(int j=0;j<n;++j){int freecap=min(max(0,P[j]),max(0,rho[j]-1));if(freecap)F.add(n+j,T,freecap,0);int paid=max(0,P[j]-freecap);if(paid)F.add(n+j,T,paid,q[j]);}return F.flow(S,T,Q);
}

struct Result {long long profiles=0,paircap_fail=0,paircap_pass=0,incidence_fail=0,incidence_pass=0,pairhall_fail=0,pairhall_pass=0,targethall_fail=0,targethall_pass=0,cost_fail=0;bool survives=false;int witness_E=-1,Emax=-1;long long witness_cost=-1,witness_envelope=-1;vector<int>wq,wrho;double seconds=0;};

struct Scanner {
    const State&st;int S,Emax;vector<Class>cls;vector<int>suffix;Result res;bool stop=false;
    explicit Scanner(const State&s):st(s){S=accumulate(st.s.begin(),st.s.end(),0);map<int,int>ct;for(int r:st.rho)++ct[r];for(auto [rho,cnt]:ct){int labels=count_if(st.s.begin(),st.s.end(),[&](int d){return d<=rho;});cls.push_back({rho,cnt,max(0,min(st.a-rho,labels))});}suffix.assign(cls.size()+1,0);for(int i=(int)cls.size()-1;i>=0;--i)suffix[i]=suffix[i+1]+cls[i].cnt*cls[i].qmax;int U=accumulate(st.rho.begin(),st.rho.end(),0)+st.b*(st.b-st.a-1);int Qmax=min({suffix[0],U,st.b*(st.b-1)/2});Emax=Qmax-S;res.Emax=Emax;}
    void eval(int E,const vector<Type>&types,long long env){++res.profiles;vector<int>q,rho;PairEval pe=pair_capacity_types(st,types,E,q,rho);int Q=S+E;if(!pe.pass){++res.paircap_fail;return;}++res.paircap_pass;if(!variable_incidence(st,q,rho)){++res.incidence_fail;return;}++res.incidence_pass;if(pair_flow(q,rho)<Q){++res.pairhall_fail;return;}++res.pairhall_pass;auto [f,cost]=target_cost_flow(q,rho,pe.P,Q);if(f<Q){++res.targethall_fail;return;}++res.targethall_pass;if(env>=0&&cost>env){++res.cost_fail;return;}res.survives=true;res.witness_E=E;res.witness_cost=cost;res.witness_envelope=env;res.wq=q;res.wrho=rho;stop=true;}
    void rec(int ci,int used,int Q,int E,long long env,vector<Type>&types){if(stop)return;if(ci==(int)cls.size()){if(used==Q)eval(E,types,env);return;}auto C=cls[ci];int lo=max(0,Q-used-suffix[ci+1]),hi=min(C.cnt*C.qmax,Q-used);if(lo>hi)return;vector<int>sums;for(int sm=lo;sm<=hi;++sm)if(!distributions(C.cnt,C.qmax,sm).empty())sums.push_back(sm);int rem=0;for(int j=ci;j<(int)cls.size();++j)rem+=cls[j].cnt;double tgt=rem?(double)(Q-used)*C.cnt/rem:0.0;stable_sort(sums.begin(),sums.end(),[&](int x,int y){return abs(x-tgt)<abs(y-tgt);});for(int sm:sums)for(auto const&dist:distributions(C.cnt,C.qmax,sm)){size_t old=types.size();for(int qq=0;qq<=C.qmax;++qq)if(dist[qq])types.push_back({C.rho,qq,dist[qq],qq+C.rho,0,0});rec(ci+1,used+sm,Q,E,env,types);types.resize(old);if(stop)return;}}
    Result run(){auto t0=chrono::steady_clock::now();vector<Type>types;if(Emax>=0)for(int E=0;E<=Emax&&!stop;++E){long long env=excess_envelope(st,E);if(env==-(1LL<<50))continue;rec(0,0,S+E,E,env,types);}res.seconds=chrono::duration<double>(chrono::steady_clock::now()-t0).count();return res;}
};

static string vs(const vector<int>&v){ostringstream o;for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}return o.str();}
int main(int argc,char**argv){if(argc<3){cerr<<"usage: scan_post_pair_relational_types INPUT OUTPUT.tsv\n";return 2;}ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;int N;in>>N;out<<"layer\tstate_id\tS\tEmax\tprofiles_tested\tpaircap_fail\tpaircap_pass\tincidence_fail\tincidence_pass\tpairhall_fail\tpairhall_pass\ttargethall_fail\ttargethall_pass\tcost_fail\tstatus\twitness_E\twitness_cost\twitness_envelope\tseconds\twitness_rho\twitness_q\n";int excluded=0,survived=0;long long profiles=0;for(int z=0;z<N;++z){State st;int ns,nr;in>>st.layer>>st.id>>st.a>>st.b>>st.t>>ns;st.s.resize(ns);for(int&x:st.s)in>>x;in>>nr;st.rho.resize(nr);for(int&x:st.rho)in>>x;Scanner sc(st);Result r=sc.run();string status=r.survives?"SURVIVES_RELATIONAL":"RELATIONAL_EXCLUDED";if(r.survives)++survived;else++excluded;profiles+=r.profiles;out<<st.layer<<'\t'<<st.id<<'\t'<<accumulate(st.s.begin(),st.s.end(),0)<<'\t'<<r.Emax<<'\t'<<r.profiles<<'\t'<<r.paircap_fail<<'\t'<<r.paircap_pass<<'\t'<<r.incidence_fail<<'\t'<<r.incidence_pass<<'\t'<<r.pairhall_fail<<'\t'<<r.pairhall_pass<<'\t'<<r.targethall_fail<<'\t'<<r.targethall_pass<<'\t'<<r.cost_fail<<'\t'<<status<<'\t'<<r.witness_E<<'\t'<<r.witness_cost<<'\t'<<r.witness_envelope<<'\t'<<r.seconds<<'\t'<<vs(r.wrho)<<'\t'<<vs(r.wq)<<'\n';cerr<<"state "<<st.id<<" "<<status<<" E="<<r.witness_E<<" profiles="<<r.profiles<<" pairpass="<<r.paircap_pass<<" incpass="<<r.incidence_pass<<" sec="<<r.seconds<<"\n";}cerr<<"SUMMARY states="<<N<<" relational_excluded="<<excluded<<" survives="<<survived<<" profiles="<<profiles<<"\n";return 0;}
