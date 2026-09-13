#include <algorithm>
#include <cassert>
#include <climits>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

/*
Exact integer triage for the adjacent N34 low-demand family.

Scope deliberately matches prepare_refined_h2_family_scan.py:
  a=15,b=18,t=1; every label demand is 2 or 3; every source residual
  degree is 1,2 or 3; at most four demand-two labels and at most three
  rho=2 sources.

The screen is a necessary-condition relaxation, not a graph search.
It combines:
  * s_i <= rho_u at every selected incidence;
  * q_u + rho_u <= a;
  * basic incoming cap p_u <= rho_u+b-a-1;
  * q_u+p_u <= b-1;
  * h_2 threshold cap: q_u>h_2 => p_u<=rho_u;
  * C_i=d_i+e_i and d_i<=rho_u+q_u-1 at selected incidences;
  * the exact baseline-3 correction, retaining -2 for every
    zero-excess demand-two label.

For fixed q and excess count h_2, incoming p is allocated greedily to
smallest q to obtain the exact minimum of sum q_u p_u under the relaxed
caps.  Label correction is maximised by dynamic programming.  A positive
minimum gap therefore excludes that entire excess layer.
*/

static const long long NEG = -(1LL<<55);
static const long long INF =  (1LL<<55);

struct QT {
    vector<int> q;
    int sq = 0;
};

struct State {
    int id=0, closed=0, a=0, b=0, t=0;
    vector<int> s, rho;
    int n2=0,n3=0,r1=0,r2=0,r3=0,S=0,r=0,Emax=0;
};

struct Scan {
    State st;
    vector<long long> gaps;
    vector<int> nonstrict;
    long long difficulty=0;
};

static map<tuple<int,int,int>, vector<QT>> part_cache;

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
        if(rr < x*slots || rr > mx*slots) continue;
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

static vector<long long> correction_dp(const State&st,const vector<int>&q2,
                                       const vector<int>&q3,int E){
    vector<int> score2,score3;
    for(int q:q2) score2.push_back(q+1); // rho=2: rho+q-1
    for(int q:q3){ score2.push_back(q+2); score3.push_back(q+2); }
    sort(score2.begin(),score2.end(),greater<int>());
    sort(score3.begin(),score3.end(),greater<int>());

    if(st.n2 && (int)score2.size()<2) return {};
    if(st.n3 && (int)score3.size()<3) return {};

    vector<vector<long long>> dp(E+1,vector<long long>(st.a+1,NEG));
    dp[0][0]=0;
    auto apply=[&](int demand,const vector<int>&scores){
        vector<vector<long long>> nd(E+1,vector<long long>(st.a+1,NEG));
        int maxe=(int)scores.size()-demand;
        for(int se=0;se<=E;++se) for(int h=0;h<=st.a;++h){
            if(dp[se][h]==NEG) continue;
            for(int e=0;e<=maxe && se+e<=E;++e){
                int x=demand+e;
                long long w=0;
                if(demand==2){
                    if(e==0) w=-2;             // -(C_i), with C_i>=x_i=2
                    else if(e>=2){
                        long long Cub=e + scores[x-1];
                        w=(long long)(e-1)*Cub;
                    }
                }else{
                    assert(demand==3);
                    if(e>=1){
                        long long Cub=e + scores[x-1];
                        w=(long long)e*Cub;
                    }
                }
                int nh=h+(e>=2);
                if(nh<=st.a) nd[se+e][nh]=max(nd[se+e][nh],dp[se][h]+w);
            }
        }
        dp.swap(nd);
    };
    for(int i=0;i<st.n2;++i) apply(2,score2);
    for(int i=0;i<st.n3;++i) apply(3,score3);

    vector<long long> out(st.a+1,NEG);
    for(int h=0;h<=st.a;++h) out[h]=dp[E][h];
    return out;
}

static long long min_p_cost(const State&st,const vector<int>&q2,const vector<int>&q3,
                            int h,int Q){
    vector<pair<int,int>> src;
    for(int i=0;i<st.r1;++i) src.push_back({0,1});
    for(int q:q2) src.push_back({q,2});
    for(int q:q3) src.push_back({q,3});
    assert((int)src.size()==st.b);
    sort(src.begin(),src.end());
    int left=Q;
    long long cost=0;
    for(auto [q,rho]:src){
        int cap=(q>h)?rho:(rho+st.b-st.a-1);
        cap=min(cap,st.b-1-q);
        cap=max(cap,0);
        int take=min(left,cap);
        cost+=(long long)q*take;
        left-=take;
        if(!left) break;
    }
    return left?INF:cost;
}

static long long layer_gap(const State&st,int E){
    int Q=st.S+E;
    int qmax2=min(st.a-2,st.n2); // s_i<=rho and q+rho<=a
    int qmax3=st.a-3;
    long long best=INF;
    int maxsum2=st.r2*qmax2;
    for(int sum2=0;sum2<=maxsum2 && sum2<=Q;++sum2){
        int sum3=Q-sum2;
        if(sum3<0 || sum3>st.r3*qmax3) continue;
        const auto&p2=parts(st.r2,qmax2,sum2);
        const auto&p3=parts(st.r3,qmax3,sum3);
        for(const auto&a2:p2) for(const auto&a3:p3){
            auto corr=correction_dp(st,a2.q,a3.q,E);
            if(corr.empty()) continue;
            long long sq=(long long)a2.sq+a3.sq;
            long long base=3LL*(st.r+Q);
            for(int h=0;h<=st.a;++h){
                if(corr[h]==NEG) continue;
                long long pc=min_p_cost(st,a2.q,a3.q,h,Q);
                if(pc==INF) continue;
                long long gap=sq+pc-base-corr[h];
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
    for(int x:st.rho){ assert(1<=x&&x<=3); st.r1+=(x==1); st.r2+=(x==2); st.r3+=(x==3); st.r+=x; }
    assert(st.n2<=4 && st.r2<=3 && st.n2+st.n3==15 && st.r1+st.r2+st.r3==18);
    int maxQ=min(st.r + st.b*(st.b-st.a-1), st.r2*min(st.a-2,st.n2)+st.r3*(st.a-3));
    st.Emax=maxQ-st.S;
    assert(st.Emax>=0);
    return st;
}

static bool must_be_strict_regression(int id,int E){
    if(id==227) return E>=21;
    if(id==279) return E>=16;
    if(id==382) return E>=17;
    if(id==526) return E>=17;
    if(id==588) return (E>=17 && E<=23) || E>=25;
    return false;
}

int main(int argc,char**argv){
    if(argc!=3){
        cerr<<"usage: scan_refined_h2_family INPUT.txt OUTPUT.tsv\n";
        return 2;
    }
    ifstream in(argv[1]); if(!in) return 2;
    int n; in>>n; vector<Scan> scans; scans.reserve(n);
    set<int> seen;
    for(int k=0;k<n;++k){
        State st=read_state(in); assert(seen.insert(st.id).second);
        Scan sc; sc.st=st;
        for(int E=0;E<=st.Emax;++E){
            long long g=layer_gap(st,E);
            sc.gaps.push_back(g);
            if(g<=0){
                sc.nonstrict.push_back(E);
                long long deficit=1-g;
                sc.difficulty+=(long long)(E+1)*deficit;
            }
            if(st.closed && must_be_strict_regression(st.id,E)) assert(g>0);
        }
        scans.push_back(move(sc));
    }
    assert(seen.count(227)&&seen.count(279)&&seen.count(382)&&seen.count(526)&&seen.count(588));

    vector<int> idx;
    for(int i=0;i<(int)scans.size();++i) if(!scans[i].st.closed) idx.push_back(i);
    sort(idx.begin(),idx.end(),[&](int i,int j){
        const auto&a=scans[i]; const auto&b=scans[j];
        int ama=a.nonstrict.empty()?-1:a.nonstrict.back();
        int bma=b.nonstrict.empty()?-1:b.nonstrict.back();
        return tie(a.nonstrict.size(),ama,a.difficulty,a.st.id)
             < tie(b.nonstrict.size(),bma,b.difficulty,b.st.id);
    });

    ofstream out(argv[2]); if(!out) return 2;
    out<<"rank\tstate_id\tclosed\tn2\tn3\tr1\tr2\tr3\tS\tr\tEmax\tnonstrict_count\tmax_nonstrict\tdifficulty\tnonstrict_E:gaps\n";
    int rank=0;
    auto emit=[&](const Scan&sc,int rk){
        out<<rk<<'\t'<<sc.st.id<<'\t'<<sc.st.closed<<'\t'
           <<sc.st.n2<<'\t'<<sc.st.n3<<'\t'<<sc.st.r1<<'\t'<<sc.st.r2<<'\t'<<sc.st.r3<<'\t'
           <<sc.st.S<<'\t'<<sc.st.r<<'\t'<<sc.st.Emax<<'\t'<<sc.nonstrict.size()<<'\t'
           <<(sc.nonstrict.empty()?-1:sc.nonstrict.back())<<'\t'<<sc.difficulty<<'\t';
        for(size_t z=0;z<sc.nonstrict.size();++z){
            if(z) out<<','; int E=sc.nonstrict[z]; out<<E<<':'<<sc.gaps[E];
        }
        out<<'\n';
    };
    for(int i:idx) emit(scans[i],++rank);
    for(const auto&sc:scans) if(sc.st.closed) emit(sc,0);

    cout<<"PASS family_records="<<scans.size()<<" active="<<idx.size()<<"\n";
    cout<<"REGRESSION strict published tail ranges reproduced for states 227,279,382,526,588\n";
    cout<<"TOP_CANDIDATES\n";
    for(int z=0;z<min<int>(20,idx.size());++z){
        const auto&sc=scans[idx[z]];
        cout<<z+1<<" state="<<sc.st.id<<" profile=n2:"<<sc.st.n2<<",r1:"<<sc.st.r1<<",r2:"<<sc.st.r2<<",r3:"<<sc.st.r3
            <<" Emax="<<sc.st.Emax<<" nonstrict="<<sc.nonstrict.size()<<" max="
            <<(sc.nonstrict.empty()?-1:sc.nonstrict.back())<<" E=";
        for(size_t j=0;j<sc.nonstrict.size();++j){ if(j) cout<<','; cout<<sc.nonstrict[j]<<':'<<sc.gaps[sc.nonstrict[j]]; }
        cout<<"\n";
    }
    return 0;
}
