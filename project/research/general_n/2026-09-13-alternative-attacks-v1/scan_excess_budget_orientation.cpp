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
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

/*
Targeted exact necessary-condition scan coupling selected incidence, orientation,
and the global excess budget.

For each requested scalar state and each admissible total excess E this scanner
enumerates source selected-degree profiles q up to permutation within equal-rho
classes.  At each q it checks:

  (1) exact lower-bound selected-incidence circulation with variable x>=s;
  (2) directed orientation compatibility D(u,w);
  (3) potential-pair degree / incoming caps, including TOTAL_EXCESS_SOURCE_CAP;
  (4) the old one-dimensional orientation prefix cuts;
  (5) cheap global excess-cost slot bound C0 <= M(E) when all s_i>0;
  (6) unordered-pair Hall flow;
  (7) directed target min-cost flow, requiring both value Q and cost <= M(E)
      when all s_i>0.

M(E) is the exact selection-free envelope from EXCESS_BUDGET_ORIENTATION_COST.md:
  max sum_i (s_i+e_i)e_i
  subject sum e_i=E and 0<=e_i<=#{u:rho_u>=s_i}-s_i.

If every q profile fails for every admissible E, the scalar state is excluded
under the retained canonical bridge conditions.  A surviving q is only a
relaxation witness, not a graph.
*/

struct Edge { int to, rev, cap; };
struct Dinic {
    vector<vector<Edge>> g;
    vector<int> lev, it;
    explicit Dinic(int n): g(n), lev(n), it(n) {}
    void add(int u,int v,int c){
        Edge a{v,(int)g[v].size(),c}, b{u,(int)g[u].size(),0};
        g[u].push_back(a); g[v].push_back(b);
    }
    bool bfs(int s,int t){
        fill(lev.begin(),lev.end(),-1); queue<int>q; lev[s]=0; q.push(s);
        while(!q.empty()){
            int u=q.front();q.pop();
            for(auto const&e:g[u]) if(e.cap&&lev[e.to]<0){lev[e.to]=lev[u]+1;q.push(e.to);}
        }
        return lev[t]>=0;
    }
    int dfs(int u,int t,int f){
        if(u==t)return f;
        for(int &k=it[u];k<(int)g[u].size();++k){
            Edge &e=g[u][k];
            if(!e.cap||lev[e.to]!=lev[u]+1)continue;
            int z=dfs(e.to,t,min(f,e.cap));
            if(z){e.cap-=z;g[e.to][e.rev].cap+=z;return z;}
        }
        return 0;
    }
    int flow(int s,int t){
        int ans=0;
        while(bfs(s,t)){
            fill(it.begin(),it.end(),0);
            while(int z=dfs(s,t,INT_MAX/4))ans+=z;
        }
        return ans;
    }
};

struct CEdge { int to, rev, cap, cost; };
struct MinCostFlow {
    vector<vector<CEdge>> g;
    explicit MinCostFlow(int n): g(n) {}
    void add(int u,int v,int cap,int cost){
        CEdge a{v,(int)g[v].size(),cap,cost};
        CEdge b{u,(int)g[u].size(),0,-cost};
        g[u].push_back(a); g[v].push_back(b);
    }
    pair<int,long long> flow(int s,int t,int need){
        const long long INFLL=(1LL<<60);
        int sent=0; long long total=0;
        int n=g.size();
        while(sent<need){
            vector<long long>d(n,INFLL); vector<int>pv(n,-1),pe(n,-1); vector<char>inq(n,0);
            queue<int>q; d[s]=0;q.push(s);inq[s]=1;
            while(!q.empty()){
                int u=q.front();q.pop();inq[u]=0;
                for(int k=0;k<(int)g[u].size();++k){
                    auto const&e=g[u][k]; if(!e.cap)continue;
                    long long nd=d[u]+e.cost;
                    if(d[u]<INFLL&&nd<d[e.to]){
                        d[e.to]=nd;pv[e.to]=u;pe[e.to]=k;
                        if(!inq[e.to]){inq[e.to]=1;q.push(e.to);}
                    }
                }
            }
            if(d[t]==INFLL)break;
            int add=need-sent;
            for(int v=t;v!=s;v=pv[v]) add=min(add,g[pv[v]][pe[v]].cap);
            for(int v=t;v!=s;v=pv[v]){
                CEdge &e=g[pv[v]][pe[v]];
                e.cap-=add; g[v][e.rev].cap+=add;
            }
            sent+=add; total+=1LL*add*d[t];
        }
        return {sent,total};
    }
};

struct State { int layer,id,a,b,t; vector<int>s,rho; };
struct Cls { int rho,cnt,qmax; };

static map<tuple<int,int,int>,vector<vector<int>>> part_cache;
static void gen_parts(int pos,int cnt,int last,int mx,int rem,vector<int>&cur,vector<vector<int>>&out){
    if(pos==cnt){if(rem==0)out.push_back(cur);return;}
    int left=cnt-pos-1;
    for(int x=last;x<=mx&&x<=rem;++x){
        int rr=rem-x;
        if(rr<x*left||rr>mx*left)continue;
        cur[pos]=x; gen_parts(pos+1,cnt,x,mx,rr,cur,out);
    }
}
static const vector<vector<int>>& parts(int cnt,int mx,int sum){
    auto key=make_tuple(cnt,mx,sum); auto it=part_cache.find(key); if(it!=part_cache.end())return it->second;
    vector<vector<int>>out;
    if(cnt==0){if(sum==0)out.push_back({});}
    else if(sum>=0&&sum<=cnt*mx){vector<int>cur(cnt);gen_parts(0,cnt,0,mx,sum,cur,out);}
    return part_cache.emplace(key,move(out)).first->second;
}

static void lowedge(Dinic&F,vector<int>&bal,int u,int v,int lo,int hi){
    assert(0<=lo&&lo<=hi); F.add(u,v,hi-lo); bal[u]-=lo; bal[v]+=lo;
}
static bool variable_incidence(const State&st,const vector<int>&q,const vector<int>&rho){
    int n=q.size(),m=st.s.size(); int S0=n+m,T0=S0+1,SS=T0+1,TT=SS+1;
    Dinic F(TT+1); vector<int>bal(TT+1,0); int Q=accumulate(q.begin(),q.end(),0);
    for(int u=0;u<n;++u)lowedge(F,bal,S0,u,q[u],q[u]);
    for(int u=0;u<n;++u)for(int i=0;i<m;++i)if(st.s[i]<=rho[u])lowedge(F,bal,u,n+i,0,1);
    for(int i=0;i<m;++i){
        int hi=0;for(int u=0;u<n;++u)if(st.s[i]<=rho[u])++hi;
        if(st.s[i]>hi)return false;
        lowedge(F,bal,n+i,T0,st.s[i],hi);
    }
    lowedge(F,bal,T0,S0,0,Q);
    int need=0;
    for(int v=0;v<=T0;++v){
        if(bal[v]>0){F.add(SS,v,bal[v]);need+=bal[v];}
        else if(bal[v]<0)F.add(v,TT,-bal[v]);
    }
    return F.flow(SS,TT)==need;
}

static long long excess_envelope(const State&st,int E){
    // The weighted theorem is currently asserted only for all-positive demand.
    if(any_of(st.s.begin(),st.s.end(),[](int x){return x<=0;}))return -1;
    const long long NEG=-(1LL<<50);
    vector<long long>dp(E+1,NEG);dp[0]=0;
    for(int s:st.s){
        int h=count_if(st.rho.begin(),st.rho.end(),[&](int r){return r>=s;});
        if(h<s)return NEG;
        int cap=h-s;
        vector<long long>ndp(E+1,NEG);
        for(int used=0;used<=E;++used)if(dp[used]>NEG/2){
            for(int e=0;e<=cap&&used+e<=E;++e){
                long long val=dp[used]+1LL*(s+e)*e;
                ndp[used+e]=max(ndp[used+e],val);
            }
        }
        dp.swap(ndp);
    }
    return dp[E];
}

struct OD { vector<vector<unsigned char>>D; vector<int>pairdeg,P,c; bool caps=true,prefix=true; };
static OD orient_data(const State&st,const vector<int>&q,const vector<int>&rho,int E){
    int n=q.size(),Q=accumulate(q.begin(),q.end(),0),z=count(st.s.begin(),st.s.end(),0);
    OD o;o.c.resize(n);for(int i=0;i<n;++i)o.c[i]=q[i]+rho[i];
    o.D.assign(n,vector<unsigned char>(n,0));
    for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(i!=j&&q[i]<=o.c[j]+1&&q[j]<=o.c[i])o.D[i][j]=1;
    o.pairdeg.assign(n,0);
    for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(o.D[i][j]||o.D[j][i]){++o.pairdeg[i];++o.pairdeg[j];}
    o.P.resize(n); long long sp=0;
    for(int i=0;i<n;++i){
        int p=rho[i]+st.b-st.a-1;
        p=min(p,st.b-1-q[i]);
        p=min(p,o.pairdeg[i]-q[i]);
        if(q[i]>0){
            int kstar=min(z,min(q[i],E));
            if(q[i]>kstar){
                int extra=(E-kstar)/(q[i]-kstar);
                p=min(p,rho[i]+extra-1);
            }
        }
        o.P[i]=p;
        if(p<0)o.caps=false; else sp+=p;
    }
    if(sp<Q)o.caps=false;
    if(o.caps){
        int mc=*max_element(o.c.begin(),o.c.end());
        for(int k=0;k<=mc;++k){
            long long cap=0;
            for(int i=0;i<n;++i)if(q[i]<=k+1)cap+=q[i];
            for(int j=0;j<n;++j)if(o.c[j]>k)cap+=o.P[j];
            if(cap<Q){o.prefix=false;break;}
        }
    }else o.prefix=false;
    return o;
}

static long long cheap_cost(const vector<int>&q,const vector<int>&rho,const vector<int>&P,int Q){
    int free=0; vector<int>paid;
    for(int i=0;i<(int)q.size();++i){
        if(P[i]<0)return (1LL<<50);
        int f=min(P[i],max(0,rho[i]-1)); free+=f;
        for(int k=f;k<P[i];++k)paid.push_back(q[i]);
    }
    if(free>=Q)return 0;
    int need=Q-free;
    if((int)paid.size()<need)return (1LL<<50);
    nth_element(paid.begin(),paid.begin()+need,paid.end());
    sort(paid.begin(),paid.begin()+need);
    long long ans=0;for(int i=0;i<need;++i)ans+=paid[i];
    return ans;
}

static int pair_flow(const vector<int>&q,const OD&o){
    int n=q.size();vector<pair<int,int>>ps;
    for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(o.D[i][j]||o.D[j][i])ps.push_back({i,j});
    int S=n+ps.size(),T=S+1;Dinic F(T+1);
    for(int i=0;i<n;++i)F.add(S,i,q[i]);
    for(int k=0;k<(int)ps.size();++k){auto [i,j]=ps[k];int x=n+k;if(o.D[i][j])F.add(i,x,1);if(o.D[j][i])F.add(j,x,1);F.add(x,T,1);}
    return F.flow(S,T);
}

static pair<int,long long> target_min_cost(const vector<int>&q,const vector<int>&rho,const OD&o,int Q){
    int n=q.size(),S=2*n,T=S+1;MinCostFlow F(T+1);
    for(int i=0;i<n;++i)F.add(S,i,q[i],0);
    for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(o.D[i][j])F.add(i,n+j,1,0);
    for(int j=0;j<n;++j){
        int f=min(max(0,o.P[j]),max(0,rho[j]-1));
        if(f)F.add(n+j,T,f,0);
        int paid=max(0,o.P[j]-f);if(paid)F.add(n+j,T,paid,q[j]);
    }
    return F.flow(S,T,Q);
}

struct LayerResult{
    long long profiles=0,incfail=0,capfail=0,prefixfail=0,cheapcostfail=0,pairfail=0,targetfail=0,costfail=0;
    bool pass=false; long long envelope=-1,witness_cost=-1; vector<int>wq,wrho; double sec=0;
};

struct Scanner{
    const State&st;int S,E,Q;vector<Cls>cls;vector<int>tailmax,highbase;LayerResult r;bool stop=false;
    Scanner(const State&s,int e):st(s),S(accumulate(s.s.begin(),s.s.end(),0)),E(e),Q(S+e){
        map<int,int>ct;for(int x:st.rho)++ct[x];
        for(auto [rho,c]:ct){int m=count_if(st.s.begin(),st.s.end(),[&](int d){return d<=rho;});cls.push_back({rho,c,min(st.a-rho,m)});}
        tailmax.assign(cls.size()+1,0);for(int i=(int)cls.size()-1;i>=0;--i)tailmax[i]=tailmax[i+1]+cls[i].cnt*cls[i].qmax;
        highbase.resize(cls.size());for(int i=0;i<(int)cls.size();++i){int h=0;for(int d:st.s)if(d>cls[i].rho)h+=d;highbase[i]=h;}
        r.envelope=excess_envelope(st,E);
    }
    void eval(const vector<int>&q,const vector<int>&rho){
        ++r.profiles;
        if(!variable_incidence(st,q,rho)){++r.incfail;return;}
        OD o=orient_data(st,q,rho,E);
        if(!o.caps){++r.capfail;return;}
        if(!o.prefix){++r.prefixfail;return;}
        if(r.envelope>=0){
            long long cc=cheap_cost(q,rho,o.P,Q);
            if(cc>r.envelope){++r.cheapcostfail;return;}
        }
        if(pair_flow(q,o)<Q){++r.pairfail;return;}
        auto [f,cost]=target_min_cost(q,rho,o,Q);
        if(f<Q){++r.targetfail;return;}
        if(r.envelope>=0&&cost>r.envelope){++r.costfail;return;}
        r.pass=true;r.witness_cost=cost;r.wq=q;r.wrho=rho;stop=true;
    }
    void rec(int ci,int used,vector<int>&q,vector<int>&rho){
        if(stop)return;
        if(ci==(int)cls.size()){if(used==Q)eval(q,rho);return;}
        auto C=cls[ci];
        int lo=max(0,Q-used-tailmax[ci+1]),hi=min(C.cnt*C.qmax,Q-used);
        hi=min(hi,Q-highbase[ci]-used);if(lo>hi)return;
        vector<int>sums;for(int sm=lo;sm<=hi;++sm)if(!parts(C.cnt,C.qmax,sm).empty())sums.push_back(sm);
        double tgt=(double)(Q-used)*C.cnt/max(1,accumulate(cls.begin()+ci,cls.end(),0,[](int z,const Cls&x){return z+x.cnt;}));
        stable_sort(sums.begin(),sums.end(),[&](int x,int y){return abs(x-tgt)<abs(y-tgt);});
        for(int sm:sums)for(auto const&pv:parts(C.cnt,C.qmax,sm)){
            size_t old=q.size();q.insert(q.end(),pv.begin(),pv.end());rho.insert(rho.end(),C.cnt,C.rho);
            rec(ci+1,used+sm,q,rho);q.resize(old);rho.resize(old);if(stop)return;
        }
    }
    LayerResult run(){
        auto t0=chrono::steady_clock::now();
        int D=st.b-st.a-1,U=accumulate(st.rho.begin(),st.rho.end(),0)+st.b*D;
        int qmax=tailmax[0],pairmax=st.b*(st.b-1)/2;
        if(Q<=qmax&&Q<=U&&Q<=pairmax&&r.envelope!=-(1LL<<50)){
            vector<int>q,rho;rec(0,0,q,rho);
        }
        r.sec=chrono::duration<double>(chrono::steady_clock::now()-t0).count();return r;
    }
};

static string vs(const vector<int>&v){ostringstream o;for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}return o.str();}

int main(int argc,char**argv){
    if(argc<3){cerr<<"usage: scan_excess_budget_orientation INPUT OUTPUT.tsv\n";return 2;}
    ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;
    int N;in>>N;
    out<<"layer\tstate_id\tE\tQ\tS\tenvelope\tprofiles_tested\tincidence_fail\tcap_fail\tprefix_fail\tcheap_cost_fail\tpair_fail\ttarget_fail\tcost_fail\tstatus\twitness_cost\tseconds\twitness_rho\twitness_q\n";
    for(int z=0;z<N;++z){
        State st;int ns,nr;in>>st.layer>>st.id>>st.a>>st.b>>st.t>>ns;st.s.resize(ns);for(int&i:st.s)in>>i;in>>nr;st.rho.resize(nr);for(int&i:st.rho)in>>i;
        int S=accumulate(st.s.begin(),st.s.end(),0),D=st.b-st.a-1,U=accumulate(st.rho.begin(),st.rho.end(),0)+st.b*D;
        int qmax=0;for(int rho:st.rho){int m=count_if(st.s.begin(),st.s.end(),[&](int d){return d<=rho;});qmax+=min(st.a-rho,m);}int Emax=min({qmax,U,st.b*(st.b-1)/2})-S;
        cerr<<"STATE "<<st.id<<" S="<<S<<" Emax="<<Emax<<"\n";
        for(int E=0;E<=Emax;++E){
            Scanner sc(st,E);auto r=sc.run();string status=r.pass?"SURVIVES_RELAXATION":"LAYER_EXCLUDED";
            out<<st.layer<<'\t'<<st.id<<'\t'<<E<<'\t'<<(S+E)<<'\t'<<S<<'\t'<<r.envelope<<'\t'<<r.profiles<<'\t'<<r.incfail<<'\t'<<r.capfail<<'\t'<<r.prefixfail<<'\t'<<r.cheapcostfail<<'\t'<<r.pairfail<<'\t'<<r.targetfail<<'\t'<<r.costfail<<'\t'<<status<<'\t'<<r.witness_cost<<'\t'<<r.sec<<'\t'<<vs(r.wrho)<<'\t'<<vs(r.wq)<<'\n';
            cerr<<"  E="<<E<<" "<<status<<" profiles="<<r.profiles<<" env="<<r.envelope<<" cost="<<r.witness_cost<<" sec="<<r.sec<<"\n";
        }
    }
}
