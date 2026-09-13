#include <algorithm>
#include <chrono>
#include <climits>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

/*
Independent type-count implementation of the potential-pair capacity scan.

This does NOT expand an equal-rho class into a sorted q vector and does NOT
construct the directed relation pair-by-pair.  Instead it enumerates, for each
rho class, counts m_q of vertices having each q, and evaluates the exact closed
formula from POTENTIAL_PAIR_CAPACITY.md on (rho,q)-types:

 d_KD(rho,q)
   = sum_(R,Q) m_(R,Q) [Q+R >= q-1 and Q <= q+rho+1]
     - 1
     - sum_(R,Q) m_(R,Q) [Q+R == q-1 and Q == q+rho+1].

The q universe and incoming caps are deliberately the same *mathematical
relaxation* as scan_pair_capacity_frontier.cpp, but the enumeration and
potential-degree calculation are independently represented.  Agreement on
whole-state exclusions is therefore a useful implementation cross-check.
*/

struct State { int layer,id,a,b,t; vector<int>s,rho; };
struct Class { int rho,cnt,qmax; };
struct Type { int rho,q,count,c; };

// Cache distributions m[0..qmax] with sum m=cnt and sum q*m=qsum.
static map<tuple<int,int,int>, vector<vector<int>>> dist_cache;

static void dist_rec(int q, int qmax, int left_count, int left_sum,
                     vector<int>& cur, vector<vector<int>>& out) {
    if (q == qmax) {
        if (left_sum == q * left_count) {
            cur[q] = left_count;
            out.push_back(cur);
        }
        return;
    }
    for (int m = 0; m <= left_count; ++m) {
        int rem_count = left_count - m;
        int rem_sum = left_sum - q * m;
        if (rem_sum < (q + 1) * rem_count) continue;
        if (rem_sum > qmax * rem_count) continue;
        cur[q] = m;
        dist_rec(q + 1, qmax, rem_count, rem_sum, cur, out);
    }
}

static const vector<vector<int>>& distributions(int cnt,int qmax,int qsum) {
    auto key=make_tuple(cnt,qmax,qsum);
    auto it=dist_cache.find(key);
    if(it!=dist_cache.end()) return it->second;
    vector<vector<int>> out;
    if(qsum>=0 && qsum<=cnt*qmax) {
        vector<int> cur(qmax+1,0);
        dist_rec(0,qmax,cnt,qsum,cur,out);
    }
    return dist_cache.emplace(key,move(out)).first->second;
}

struct Eval {
    bool pass=false;
    int pre_margin=INT_MIN;
    int pair_margin=INT_MIN;
};

static Eval evaluate_types(const State&st,int E,const vector<Type>&types) {
    const int z=count(st.s.begin(),st.s.end(),0);
    long long Q=0;
    for(auto const&t:types) Q+=1LL*t.count*t.q;

    vector<int> base(types.size()), dK(types.size()), cap(types.size());
    long long base_sum=0;
    bool base_ok=true;

    for(size_t i=0;i<types.size();++i) {
        auto const&A=types[i];
        int p=min(A.rho+st.b-st.a-1, st.b-1-A.q);
        if(A.q>0) {
            int kstar=min(z,min(A.q,E));
            if(A.q>kstar) {
                int extra=(E-kstar)/(A.q-kstar);
                p=min(p,A.rho+extra-1);
            }
        }
        base[i]=p;
        if(p<0) base_ok=false;
        else base_sum+=1LL*A.count*p;
    }

    Eval ans;
    ans.pre_margin=base_ok ? (int)(base_sum-Q) : INT_MIN/2;
    if(!base_ok || base_sum<Q) return ans;

    for(size_t i=0;i<types.size();++i) {
        auto const&A=types[i];
        long long weak=0,boundary=0;
        for(auto const&B:types) {
            if(B.c>=A.q-1 && B.q<=A.c+1) weak+=B.count;
            if(B.c==A.q-1 && B.q==A.c+1) boundary+=B.count;
        }
        long long deg=weak-1-boundary;
        if(deg<INT_MIN || deg>INT_MAX) return ans;
        dK[i]=(int)deg;
    }

    long long pair_sum=0;
    bool pair_ok=true;
    for(size_t i=0;i<types.size();++i) {
        int p=min(base[i],dK[i]-types[i].q);
        cap[i]=p;
        if(p<0) pair_ok=false;
        else pair_sum+=1LL*types[i].count*p;
    }
    ans.pair_margin=pair_ok ? (int)(pair_sum-Q) : INT_MIN/2;
    ans.pass=pair_ok && pair_sum>=Q;
    return ans;
}

struct Result {
    long long profiles=0, pre_pass=0, pair_pass=0;
    int best_pre=INT_MIN,best_pair=INT_MIN,witness_E=-1,Emax=-1;
    bool survives=false;
    vector<Type>witness;
    double seconds=0;
};

struct Scanner {
    const State&st;
    int S,Emax;
    vector<Class> cls;
    vector<int> suffix_qmax;
    Result res;
    bool stop=false;

    explicit Scanner(const State&s):st(s) {
        S=accumulate(st.s.begin(),st.s.end(),0);
        map<int,int>ct;for(int r:st.rho)++ct[r];
        for(auto [rho,cnt]:ct) {
            int labels=count_if(st.s.begin(),st.s.end(),[&](int d){return d<=rho;});
            cls.push_back({rho,cnt,max(0,min(st.a-rho,labels))});
        }
        suffix_qmax.assign(cls.size()+1,0);
        for(int i=(int)cls.size()-1;i>=0;--i)
            suffix_qmax[i]=suffix_qmax[i+1]+cls[i].cnt*cls[i].qmax;
        int U=accumulate(st.rho.begin(),st.rho.end(),0)+st.b*(st.b-st.a-1);
        int Qmax=min({suffix_qmax[0],U,st.b*(st.b-1)/2});
        Emax=Qmax-S;res.Emax=Emax;
    }

    void eval(int E,const vector<Type>&types) {
        ++res.profiles;
        Eval x=evaluate_types(st,E,types);
        res.best_pre=max(res.best_pre,x.pre_margin);
        if(x.pre_margin>=0)++res.pre_pass;
        res.best_pair=max(res.best_pair,x.pair_margin);
        if(x.pass) {
            ++res.pair_pass;
            res.survives=true;
            res.witness_E=E;
            res.witness=types;
            stop=true;
        }
    }

    void rec(int ci,int used,int Q,int E,vector<Type>&types) {
        if(stop)return;
        if(ci==(int)cls.size()) {
            if(used==Q) eval(E,types);
            return;
        }
        auto C=cls[ci];
        int lo=max(0,Q-used-suffix_qmax[ci+1]);
        int hi=min(C.cnt*C.qmax,Q-used);
        if(lo>hi)return;

        vector<int>sums;
        for(int sm=lo;sm<=hi;++sm)
            if(!distributions(C.cnt,C.qmax,sm).empty())sums.push_back(sm);

        int rem_sources=0;
        for(int j=ci;j<(int)cls.size();++j)rem_sources+=cls[j].cnt;
        double target=rem_sources ? (double)(Q-used)*C.cnt/rem_sources : 0.0;
        stable_sort(sums.begin(),sums.end(),[&](int x,int y){return abs(x-target)<abs(y-target);});

        for(int sm:sums) {
            for(auto const&dist:distributions(C.cnt,C.qmax,sm)) {
                size_t old=types.size();
                for(int q=0;q<=C.qmax;++q) if(dist[q])
                    types.push_back({C.rho,q,dist[q],q+C.rho});
                rec(ci+1,used+sm,Q,E,types);
                types.resize(old);
                if(stop)return;
            }
        }
    }

    Result run() {
        auto t0=chrono::steady_clock::now();
        vector<Type>types;
        if(Emax>=0) for(int E=0;E<=Emax&&!stop;++E)
            rec(0,0,S+E,E,types);
        res.seconds=chrono::duration<double>(chrono::steady_clock::now()-t0).count();
        return res;
    }
};

static string typestr(const vector<Type>&v) {
    ostringstream o;
    for(size_t i=0;i<v.size();++i) {
        if(i)o<<';';
        o<<v[i].rho<<':'<<v[i].q<<'x'<<v[i].count;
    }
    return o.str();
}

int main(int argc,char**argv) {
    if(argc<3){cerr<<"usage: scan_pair_capacity_types INPUT OUTPUT.tsv\n";return 2;}
    ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;
    int N;in>>N;
    out<<"layer\tstate_id\tS\tEmax\tprofiles_tested\tpre_pair_passes\tpair_passes\tbest_pre_margin\tbest_pair_margin\tstatus\twitness_E\tseconds\twitness_types\n";
    int excluded=0,survived=0;long long total=0;
    for(int z=0;z<N;++z) {
        State st;int ns,nr;
        in>>st.layer>>st.id>>st.a>>st.b>>st.t>>ns;
        st.s.resize(ns);for(int&x:st.s)in>>x;
        in>>nr;st.rho.resize(nr);for(int&x:st.rho)in>>x;
        Scanner sc(st);Result r=sc.run();
        string status=r.survives?"SURVIVES_PAIR_CAPACITY":"PAIR_CAPACITY_EXCLUDED";
        if(r.survives)++survived;else++excluded;total+=r.profiles;
        auto show=[](int x){return x<=INT_MIN/4?-999999999:x;};
        out<<st.layer<<'\t'<<st.id<<'\t'<<accumulate(st.s.begin(),st.s.end(),0)<<'\t'<<r.Emax<<'\t'
           <<r.profiles<<'\t'<<r.pre_pass<<'\t'<<r.pair_pass<<'\t'<<show(r.best_pre)<<'\t'<<show(r.best_pair)<<'\t'
           <<status<<'\t'<<r.witness_E<<'\t'<<r.seconds<<'\t'<<typestr(r.witness)<<'\n';
        cerr<<"state "<<st.id<<" "<<status<<" Emax="<<r.Emax<<" profiles="<<r.profiles
            <<" best_pair_margin="<<show(r.best_pair)<<" sec="<<r.seconds<<"\n";
    }
    cerr<<"SUMMARY states="<<N<<" pair_capacity_excluded="<<excluded<<" survives="<<survived<<" profiles="<<total<<"\n";
    return 0;
}
