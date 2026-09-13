#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

/*
Endpoint-order triage for the three remaining narrow N34 companions.

This strengthens the refined h2 scanner when zero-excess demand-two labels
occur.  For fixed source margins, let lambda_2 be the second-smallest q+p
among active sources with rho>=2 and p<=rho-1.  Every zero-excess demand-two
label has C_i>=max(2,lambda_2).  We lower-bound

    sum q_u p_u + z0 * max(2,lambda_2)

by enumerating two eligible witness sources and their p-values, then greedily
allocating the remaining incoming mass to the cheapest q sources.  This is a
safe relaxation: for any full p-vector, choosing its two smallest eligible
sources is among the enumerated pairs; greedy reallocation can only decrease
sum q p.

Positive baseline-three corrections retain the exact selected-source score
rho+q-1, using only active q>0 sources in the order statistics.  The scan is
an exact integer necessary-condition relaxation, not a graph search.
*/

static const long long NEG = -(1LL<<55);
static const long long INF =  (1LL<<55);

struct QT { vector<int> q; int sq=0; };
struct State {
    int id=0, closed=0, a=0, b=0, t=0;
    vector<int> s, rho;
    int n2=0,n3=0,r1=0,r2=0,r3=0,S=0,r=0,Emax=0;
};
struct Scan {
    State st;
    vector<long long> gap;
    vector<int> nonstrict;
    long long severity=0;
};

static map<tuple<int,int,int>,vector<QT>> part_cache;

static void gen_parts_rec(int pos,int cnt,int last,int mx,int rem,
                          vector<int>&cur,vector<QT>&out){
    if(pos==cnt){
        if(rem==0){
            int sq=0; for(int x:cur) sq+=x*x;
            out.push_back({cur,sq});
        }
        return;
    }
    int slots=cnt-pos-1;
    for(int x=last;x<=mx && x<=rem;++x){
        int rr=rem-x;
        if(rr<x*slots || rr>mx*slots) continue;
        cur[pos]=x;
        gen_parts_rec(pos+1,cnt,x,mx,rr,cur,out);
    }
}

static const vector<QT>& parts(int cnt,int mx,int sum){
    auto key=make_tuple(cnt,mx,sum);
    auto it=part_cache.find(key); if(it!=part_cache.end()) return it->second;
    vector<QT> out;
    if(cnt==0){ if(sum==0) out.push_back({{},0}); }
    else if(sum>=0 && sum<=cnt*mx){
        vector<int> cur(cnt);
        gen_parts_rec(0,cnt,0,mx,sum,cur,out);
    }
    return part_cache.emplace(key,move(out)).first->second;
}

// Maximum positive baseline-three correction by (h2,z0) for fixed E/q.
// z0 counts zero-excess demand-two labels.  Their negative term is moved to
// the source-side endpoint-order objective, so they contribute 0 here.
static vector<vector<long long>> correction_dp(const State&st,
                                                const vector<int>&q2,
                                                const vector<int>&q3,
                                                int E){
    vector<int> score2,score3;
    for(int q:q2) if(q>0) score2.push_back(q+1); // rho=2 => rho+q-1
    for(int q:q3) if(q>0){
        score2.push_back(q+2);                    // rho=3
        score3.push_back(q+2);
    }
    sort(score2.begin(),score2.end(),greater<int>());
    sort(score3.begin(),score3.end(),greater<int>());

    vector<vector<vector<long long>>> dp(
        E+1, vector<vector<long long>>(16, vector<long long>(st.n2+1,NEG)));
    dp[0][0][0]=0;

    auto apply=[&](int demand,const vector<int>&scores){
        vector<vector<vector<long long>>> nd(
            E+1, vector<vector<long long>>(16, vector<long long>(st.n2+1,NEG)));
        int maxe=(int)scores.size()-demand;
        if(maxe<0){ dp.swap(nd); return; }
        for(int se=0;se<=E;++se) for(int h=0;h<=15;++h)
            for(int z=0;z<=st.n2;++z){
                long long cur=dp[se][h][z];
                if(cur==NEG) continue;
                for(int e=0;e<=maxe && se+e<=E;++e){
                    int x=demand+e;
                    long long w=0;
                    int nz=z;
                    if(demand==2){
                        if(e==0) ++nz;
                        else if(e>=2) w=1LL*(e-1)*(e+scores[x-1]);
                    }else{
                        assert(demand==3);
                        if(e>=1) w=1LL*e*(e+scores[x-1]);
                    }
                    if(nz>st.n2) continue;
                    int nh=h+(e>=2);
                    if(nh<=15)
                        nd[se+e][nh][nz]=max(nd[se+e][nh][nz],cur+w);
                }
            }
        dp.swap(nd);
    };

    for(int i=0;i<st.n2;++i) apply(2,score2);
    for(int i=0;i<st.n3;++i) apply(3,score3);

    vector<vector<long long>> out(16,vector<long long>(st.n2+1,NEG));
    for(int h=0;h<=15;++h) for(int z=0;z<=st.n2;++z)
        out[h][z]=dp[E][h][z];
    return out;
}

struct Src { int q=0,rho=0,cap=0; };

static vector<Src> make_sources(const State&st,const vector<int>&q2,
                                const vector<int>&q3,int h){
    vector<Src> src;
    for(int i=0;i<st.r1;++i) src.push_back({0,1,3});
    auto add=[&](int q,int rho){
        int cap=(q>h)?rho:(rho+2); // here b-a-1=2
        cap=min(cap,st.b-1-q);
        cap=max(cap,0);
        src.push_back({q,rho,cap});
    };
    for(int q:q2) add(q,2);
    for(int q:q3) add(q,3);
    assert((int)src.size()==st.b);
    return src;
}

static long long greedy_remaining_cost(const vector<Src>&src,int skip1,int skip2,
                                       int required){
    vector<pair<int,int>> v;
    for(int i=0;i<(int)src.size();++i){
        if(i==skip1 || i==skip2) continue;
        v.push_back({src[i].q,src[i].cap});
    }
    sort(v.begin(),v.end());
    long long cost=0;
    for(auto [q,cap]:v){
        int take=min(required,cap);
        cost+=1LL*q*take;
        required-=take;
        if(!required) break;
    }
    return required?INF:cost;
}

// Lower bound on sum q*p + z0*max(2,lambda_2) for fixed q,h.
static long long source_objective(const State&st,const vector<int>&q2,
                                  const vector<int>&q3,int h,int z0,int Q){
    vector<Src> src=make_sources(st,q2,q3,h);

    if(z0==0){
        vector<pair<int,int>> v;
        for(auto&s:src) v.push_back({s.q,s.cap});
        sort(v.begin(),v.end());
        int left=Q; long long cost=0;
        for(auto [q,cap]:v){
            int take=min(left,cap);
            cost+=1LL*q*take;
            left-=take;
            if(!left) break;
        }
        return left?INF:cost;
    }

    long long best=INF;
    const int n=src.size();
    for(int i=0;i<n;++i){
        if(src[i].rho<2 || src[i].q<=0) continue;
        int pmaxi=min(src[i].cap,src[i].rho-1);
        for(int j=i+1;j<n;++j){
            if(src[j].rho<2 || src[j].q<=0) continue;
            int pmaxj=min(src[j].cap,src[j].rho-1);
            for(int pi=0;pi<=pmaxi;++pi) for(int pj=0;pj<=pmaxj;++pj){
                int rem=Q-pi-pj;
                if(rem<0) continue;
                long long rest=greedy_remaining_cost(src,i,j,rem);
                if(rest==INF) continue;
                long long cost=1LL*src[i].q*pi+1LL*src[j].q*pj+rest;
                int lambda=max({2,src[i].q+pi,src[j].q+pj});
                best=min(best,cost+1LL*z0*lambda);
            }
        }
    }
    return best;
}

static long long layer_gap(const State&st,int E){
    int Q=st.S+E;
    int qmax2=min(st.a-2,st.n2);
    int qmax3=st.a-3;
    long long best=INF;

    for(int sum2=0;sum2<=st.r2*qmax2 && sum2<=Q;++sum2){
        int sum3=Q-sum2;
        if(sum3<0 || sum3>st.r3*qmax3) continue;
        const auto&p2=parts(st.r2,qmax2,sum2);
        const auto&p3=parts(st.r3,qmax3,sum3);
        for(const auto&a2:p2) for(const auto&a3:p3){
            auto corr=correction_dp(st,a2.q,a3.q,E);
            long long sq=1LL*a2.sq+a3.sq;
            map<pair<int,int>,long long> source_cache;
            for(int h=0;h<=15;++h) for(int z=0;z<=st.n2;++z){
                if(corr[h][z]==NEG) continue;
                auto key=make_pair(h,z);
                auto it=source_cache.find(key);
                long long so;
                if(it==source_cache.end()){
                    so=source_objective(st,a2.q,a3.q,h,z,Q);
                    source_cache[key]=so;
                }else so=it->second;
                if(so==INF) continue;
                long long gap=sq+so-3LL*(st.r+Q)-corr[h][z];
                best=min(best,gap);
            }
        }
    }
    return best;
}

static State read_state(istream&in){
    State st; int ns,nr;
    in>>st.id>>st.closed>>st.a>>st.b>>st.t>>ns;
    st.s.resize(ns); for(int&x:st.s) in>>x;
    in>>nr; st.rho.resize(nr); for(int&x:st.rho) in>>x;
    assert(st.a==15 && st.b==18 && st.t==1 && ns==15 && nr==18);
    for(int x:st.s){ assert(x==2||x==3); st.n2+=(x==2); st.n3+=(x==3); st.S+=x; }
    for(int x:st.rho){
        assert(1<=x&&x<=3);
        st.r1+=(x==1); st.r2+=(x==2); st.r3+=(x==3); st.r+=x;
    }
    assert(st.n2+st.n3==15 && st.r1+st.r2+st.r3==18);
    st.Emax=st.r+36-st.S; // total basic incoming capacity is r+18*2
    assert(st.Emax==34);
    return st;
}

int main(int argc,char**argv){
    if(argc!=3){
        cerr<<"usage: scan_endpoint_order_companions INPUT.txt OUTPUT.tsv\n";
        return 2;
    }
    ifstream in(argv[1]); if(!in) return 2;
    int n; in>>n; assert(n==4);
    vector<Scan> scans;
    set<int> ids;
    for(int k=0;k<n;++k){
        State st=read_state(in);
        ids.insert(st.id);
        Scan sc; sc.st=st;
        cerr<<"scan state "<<st.id<<"\n";
        for(int E=0;E<=st.Emax;++E){
            long long g=layer_gap(st,E);
            sc.gap.push_back(g);
            if(g<=0){
                sc.nonstrict.push_back(E);
                sc.severity+=1LL*(E+1)*(1-g);
            }
            cout<<"state="<<st.id<<" E="<<E<<" gap="<<g<<"\n";
        }
        scans.push_back(move(sc));
    }
    assert(ids==set<int>({230,282,385,519}));

    vector<int> active;
    for(int i=0;i<(int)scans.size();++i) if(!scans[i].st.closed) active.push_back(i);
    assert(active.size()==3);
    sort(active.begin(),active.end(),[&](int i,int j){
        const auto&a=scans[i]; const auto&b=scans[j];
        int ama=a.nonstrict.empty()?-1:a.nonstrict.back();
        int bma=b.nonstrict.empty()?-1:b.nonstrict.back();
        return make_tuple(a.nonstrict.size(),ama,a.severity,a.st.id)
             < make_tuple(b.nonstrict.size(),bma,b.severity,b.st.id);
    });

    ofstream out(argv[2]); if(!out) return 2;
    out<<"rank\tstate_id\tclosed\tn2\tn3\tr1\tr2\tr3\tnonstrict_count\tmax_nonstrict\tseverity\tnonstrict_E:gaps\n";
    int rank=0;
    auto emit=[&](const Scan&sc,int rk){
        out<<rk<<'\t'<<sc.st.id<<'\t'<<sc.st.closed<<'\t'
           <<sc.st.n2<<'\t'<<sc.st.n3<<'\t'<<sc.st.r1<<'\t'<<sc.st.r2<<'\t'<<sc.st.r3<<'\t'
           <<sc.nonstrict.size()<<'\t'<<(sc.nonstrict.empty()?-1:sc.nonstrict.back())<<'\t'
           <<sc.severity<<'\t';
        for(size_t z=0;z<sc.nonstrict.size();++z){
            if(z) out<<',';
            int E=sc.nonstrict[z]; out<<E<<':'<<sc.gap[E];
        }
        out<<'\n';
    };
    for(int i:active) emit(scans[i],++rank);
    for(const auto&sc:scans) if(sc.st.closed) emit(sc,0);

    cout<<"PASS endpoint-order companion scan active=3 reference=519\n";
    cout<<"RANKING\n";
    for(int z=0;z<(int)active.size();++z){
        const auto&sc=scans[active[z]];
        cout<<z+1<<" state="<<sc.st.id<<" nonstrict="<<sc.nonstrict.size()
            <<" max="<<(sc.nonstrict.empty()?-1:sc.nonstrict.back())<<" E=";
        for(size_t j=0;j<sc.nonstrict.size();++j){
            if(j) cout<<',';
            int E=sc.nonstrict[j]; cout<<E<<':'<<sc.gap[E];
        }
        cout<<"\n";
    }
    return 0;
}
