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
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;

/*
Exact E=0 necessary-condition scanner for the canonical frozen frontier.

For every scalar state and every source-degree vector q, up to permutation of
sources having equal rho, retain:
  * selected-edge forcing at x=s;
  * exact selected source-label incidence max flow;
  * E=0 incoming caps p<=rho-1 on active sources;
  * canonical/simple incoming caps on inactive sources;
  * directed orientation compatibility D(u,w);
  * potential-pair missing-degree cap;
  * old one-dimensional orientation-prefix cuts;
  * unordered-pair Hall flow;
  * target-capacity Hall flow.

If every q profile fails at least one necessary condition, the E=0 layer of
that scalar state is excluded. Survival is only survival of this relaxation.
All arithmetic is integral; no floating-point solver or timeout is proof.
*/

struct Edge { int to, rev, cap; };
struct Dinic {
    int n; vector<vector<Edge>> g; vector<int> level, it;
    Dinic(int n):n(n),g(n),level(n),it(n){}
    void add(int u,int v,int c){ Edge a{v,(int)g[v].size(),c}, b{u,(int)g[u].size(),0}; g[u].push_back(a); g[v].push_back(b); }
    int bfs(int s,int t){ fill(level.begin(),level.end(),-1); queue<int>q; level[s]=0;q.push(s); while(!q.empty()){int u=q.front();q.pop();for(auto const&e:g[u])if(e.cap&&level[e.to]<0){level[e.to]=level[u]+1;q.push(e.to);}}return level[t]>=0; }
    int dfs(int u,int t,int f){ if(u==t)return f; for(int &k=it[u];k<(int)g[u].size();++k){Edge &e=g[u][k];if(!e.cap||level[e.to]!=level[u]+1)continue;int z=dfs(e.to,t,min(f,e.cap));if(z){e.cap-=z;g[e.to][e.rev].cap+=z;return z;}}return 0; }
    int flow(int s,int t){ int ans=0;while(bfs(s,t)){fill(it.begin(),it.end(),0);while(int z=dfs(s,t,INT_MAX/4))ans+=z;}return ans; }
};

struct State { int layer,id,a,b,t; vector<int>s,rho; };
struct Cls { int rho,cnt,qmax; };

static map<tuple<int,int,int>, vector<vector<int>>> part_cache;
static void gen_parts_rec(int pos,int cnt,int last,int mx,int rem,vector<int>&cur,vector<vector<int>>&out){
    if(pos==cnt){ if(rem==0) out.push_back(cur); return; }
    int slots=cnt-pos-1;
    for(int x=last;x<=mx&&x<=rem;++x){
        int rr=rem-x;
        if(rr < x*slots || rr > mx*slots) continue;
        cur[pos]=x; gen_parts_rec(pos+1,cnt,x,mx,rr,cur,out);
    }
}
static const vector<vector<int>>& parts(int cnt,int mx,int sum){
    auto key=make_tuple(cnt,mx,sum); auto it=part_cache.find(key); if(it!=part_cache.end())return it->second;
    vector<vector<int>> out;
    if(cnt==0){ if(sum==0)out.push_back({}); }
    else if(sum>=0 && sum<=cnt*mx){ vector<int>cur(cnt); gen_parts_rec(0,cnt,0,mx,sum,cur,out); }
    return part_cache.emplace(key,move(out)).first->second;
}

static int selected_flow(const State&st,const vector<int>&q,const vector<int>&rho){
    int n=q.size(), m=st.s.size(), SRC=n+m, SNK=SRC+1; Dinic F(SNK+1); int Q=accumulate(q.begin(),q.end(),0);
    for(int u=0;u<n;++u)F.add(SRC,u,q[u]);
    for(int u=0;u<n;++u)for(int i=0;i<m;++i)if(st.s[i]>0&&st.s[i]<=rho[u])F.add(u,n+i,1);
    for(int i=0;i<m;++i)if(st.s[i]>0)F.add(n+i,SNK,st.s[i]);
    int f=F.flow(SRC,SNK); assert(f<=Q); return f;
}

struct OrientData { vector<vector<unsigned char>> D; vector<int> pairdeg,P,c; bool caps_ok=true,prefix_ok=true; };
static OrientData orient_data(const State&st,const vector<int>&q,const vector<int>&rho){
    int n=q.size(), Q=accumulate(q.begin(),q.end(),0); OrientData z;
    z.c.resize(n); for(int i=0;i<n;++i)z.c[i]=q[i]+rho[i];
    z.D.assign(n,vector<unsigned char>(n,0));
    for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(i!=j && q[i]<=z.c[j]+1 && q[j]<=z.c[i])z.D[i][j]=1;
    z.pairdeg.assign(n,0);
    for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(z.D[i][j]||z.D[j][i]){++z.pairdeg[i];++z.pairdeg[j];}
    z.P.resize(n);
    long long sump=0;
    for(int i=0;i<n;++i){
        int cap=(q[i]>0 ? rho[i]-1 : rho[i]+st.b-st.a-1);
        cap=min(cap,st.b-1-q[i]);
        cap=min(cap,z.pairdeg[i]-q[i]);
        z.P[i]=cap;
        if(cap<0)z.caps_ok=false; else sump+=cap;
    }
    if(sump<Q)z.caps_ok=false;
    if(z.caps_ok){
        int maxc=*max_element(z.c.begin(),z.c.end());
        for(int k=0;k<=maxc;++k){
            long long cap=0;
            for(int i=0;i<n;++i)if(q[i]<=k+1)cap+=q[i];
            for(int j=0;j<n;++j)if(z.c[j]>k)cap+=z.P[j];
            if(cap<Q){z.prefix_ok=false;break;}
        }
    } else z.prefix_ok=false;
    return z;
}

static int pair_flow(const vector<int>&q,const OrientData&z){
    int n=q.size(); vector<pair<int,int>> ps;
    for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(z.D[i][j]||z.D[j][i])ps.push_back({i,j});
    int SRC=n+ps.size(), SNK=SRC+1; Dinic F(SNK+1);
    for(int i=0;i<n;++i)F.add(SRC,i,q[i]);
    for(int k=0;k<(int)ps.size();++k){int i=ps[k].first,j=ps[k].second,node=n+k;if(z.D[i][j])F.add(i,node,1);if(z.D[j][i])F.add(j,node,1);F.add(node,SNK,1);}
    return F.flow(SRC,SNK);
}
static int target_flow(const vector<int>&q,const OrientData&z){
    int n=q.size(), SRC=2*n, SNK=SRC+1; Dinic F(SNK+1);
    for(int i=0;i<n;++i)F.add(SRC,i,q[i]);
    for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(z.D[i][j])F.add(i,n+j,1);
    for(int j=0;j<n;++j)F.add(n+j,SNK,max(0,z.P[j]));
    return F.flow(SRC,SNK);
}

struct Result {
    long long profiles=0, incidence_fail=0, cap_fail=0, prefix_fail=0, pair_fail=0, target_fail=0;
    int best_inc_def=INT_MAX,best_pair_def=INT_MAX,best_target_def=INT_MAX;
    bool pass=false; vector<int>wq,wrho; double seconds=0;
};

static int local_qmax(const State&st,int rho){
    vector<int> compat; for(int s:st.s)if(s>0&&s<=rho)compat.push_back(s);
    sort(compat.begin(),compat.end(),greater<int>());
    int mx=min(st.a-rho,(int)compat.size());
    int rsum=accumulate(st.rho.begin(),st.rho.end(),0), ans=0;
    for(int q=1;q<=mx;++q){
        long long need=0; for(int j=0;j<q;++j)need+=max(0,q-compat[j]);
        if(need<=rsum)ans=q;
    }
    return ans;
}

struct Scanner {
    const State&st; int Q; vector<Cls>cls; vector<int>labelcap; vector<int>tailmax; Result res; bool stop=false;
    Scanner(const State&s):st(s){
        Q=accumulate(st.s.begin(),st.s.end(),0);
        map<int,int>cnt;for(int r:st.rho)++cnt[r];
        for(auto [r,c]:cnt)cls.push_back({r,c,local_qmax(st,r)});
        int maxr=cls.empty()?0:cls.back().rho; labelcap.assign(maxr+1,0);
        for(int R=0;R<=maxr;++R)for(int x:st.s)if(x>0&&x<=R)labelcap[R]+=x;
        tailmax.assign(cls.size()+1,0); for(int i=(int)cls.size()-1;i>=0;--i)tailmax[i]=tailmax[i+1]+cls[i].cnt*cls[i].qmax;
    }
    void evaluate(const vector<int>&q,const vector<int>&rho){
        ++res.profiles; int inc=selected_flow(st,q,rho); if(inc<Q){++res.incidence_fail;res.best_inc_def=min(res.best_inc_def,Q-inc);return;}
        auto z=orient_data(st,q,rho); if(!z.caps_ok){++res.cap_fail;return;} if(!z.prefix_ok){++res.prefix_fail;return;}
        int pf=pair_flow(q,z); if(pf<Q){++res.pair_fail;res.best_pair_def=min(res.best_pair_def,Q-pf);return;}
        int tf=target_flow(q,z); if(tf<Q){++res.target_fail;res.best_target_def=min(res.best_target_def,Q-tf);return;}
        res.pass=true;res.wq=q;res.wrho=rho;stop=true;
    }
    void rec(int ci,int used,vector<int>&q,vector<int>&rho){
        if(stop)return;
        if(ci==(int)cls.size()){ if(used==Q)evaluate(q,rho); return; }
        auto C=cls[ci];
        int lo=max(0,Q-used-tailmax[ci+1]), hi=min(C.cnt*C.qmax,Q-used);
        // Hall prefix for all source classes rho<=C.rho.
        hi=min(hi,labelcap[C.rho]-used); if(lo>hi)return;
        vector<int>sums;for(int sm=lo;sm<=hi;++sm)if(!parts(C.cnt,C.qmax,sm).empty())sums.push_back(sm);
        // Try class sums near the proportional remaining target first, so a
        // surviving witness is usually found before exhaustive enumeration.
        double target=(double)(Q-used)*C.cnt/max(1,accumulate(cls.begin()+ci,cls.end(),0,[](int z,const Cls&x){return z+x.cnt;}));
        stable_sort(sums.begin(),sums.end(),[&](int x,int y){return abs(x-target)<abs(y-target);});
        for(int sm:sums){
            for(auto const&pv:parts(C.cnt,C.qmax,sm)){
                size_t old=q.size(); q.insert(q.end(),pv.begin(),pv.end()); rho.insert(rho.end(),C.cnt,C.rho);
                rec(ci+1,used+sm,q,rho);
                q.resize(old);rho.resize(old);
                if(stop)return;
            }
        }
    }
    Result run(){
        auto t0=chrono::steady_clock::now(); vector<int>q,rho;
        if(Q<=tailmax[0])rec(0,0,q,rho);
        res.seconds=chrono::duration<double>(chrono::steady_clock::now()-t0).count(); return res;
    }
};

static string vecstr(const vector<int>&v){ostringstream o;for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}return o.str();}

int main(int argc,char**argv){
    if(argc<3){cerr<<"usage: scan_orientation_e0_frontier INPUT OUTPUT.tsv\n";return 2;}
    ifstream in(argv[1]); if(!in){cerr<<"cannot open input\n";return 2;} ofstream out(argv[2]); if(!out){cerr<<"cannot open output\n";return 2;}
    int N;in>>N;
    out<<"layer\tstate_id\tmax_s\tS\tprofiles_tested\tincidence_fail\tcap_fail\tprefix_fail\tpair_fail\ttarget_fail\tstatus\tbest_inc_def\tbest_pair_def\tbest_target_def\tseconds\twitness_rho\twitness_q\n";
    int closed=0,survive=0;
    for(int z=0;z<N;++z){
        State st;int ns,nr;in>>st.layer>>st.id>>st.a>>st.b>>st.t>>ns;st.s.resize(ns);for(int&i:st.s)in>>i;in>>nr;st.rho.resize(nr);for(int&i:st.rho)in>>i;
        Scanner sc(st);Result r=sc.run();int S=accumulate(st.s.begin(),st.s.end(),0),ms=*max_element(st.s.begin(),st.s.end());
        string status=r.pass?"SURVIVES_RELAXATION":"E0_EXCLUDED";if(r.pass)++survive;else ++closed;
        auto bd=[](int x){return x==INT_MAX?-1:x;};
        out<<st.layer<<'\t'<<st.id<<'\t'<<ms<<'\t'<<S<<'\t'<<r.profiles<<'\t'<<r.incidence_fail<<'\t'<<r.cap_fail<<'\t'<<r.prefix_fail<<'\t'<<r.pair_fail<<'\t'<<r.target_fail<<'\t'<<status<<'\t'<<bd(r.best_inc_def)<<'\t'<<bd(r.best_pair_def)<<'\t'<<bd(r.best_target_def)<<'\t'<<r.seconds<<'\t'<<vecstr(r.wrho)<<'\t'<<vecstr(r.wq)<<'\n';
        cerr<<"state "<<st.id<<" "<<status<<" profiles="<<r.profiles<<" sec="<<r.seconds<<"\n";
    }
    cerr<<"SUMMARY states="<<N<<" e0_excluded="<<closed<<" survives="<<survive<<"\n";
    return 0;
}
