#define main forced_core_types_original_main
#include "../2026-09-15-forced-core-canonical-audit-v1/scan_forced_core_types.cpp"
#undef main

struct AggCoreCert {
    bool reject=false;
    string why;
    int r=-1,h=0,u=0,tau=-1,raw=0,demand=0;
    long long ceil_loss=0;
};

static long long fractional_cover_ceil(const vector<int>&caps,const vector<int>&loss,long long need){
    assert(caps.size()==loss.size());
    vector<int> ord;
    long long total=0;
    for(int i=0;i<(int)caps.size();++i) if(caps[i]>0){ord.push_back(i);total+=caps[i];}
    if(total<need) return (1LL<<60);
    stable_sort(ord.begin(),ord.end(),[&](int i,int j){
        __int128 lhs=(__int128)loss[i]*caps[j];
        __int128 rhs=(__int128)loss[j]*caps[i];
        if(lhs!=rhs) return lhs<rhs;
        if(loss[i]!=loss[j]) return loss[i]<loss[j];
        return caps[i]>caps[j];
    });
    long long rem=need,ans=0;
    for(int i:ord){
        if(rem<=0) break;
        long long c=caps[i],w=loss[i];
        if(rem>=c){ans+=w;rem-=c;}
        else{ans+=(w*rem+c-1)/c;rem=0;}
    }
    assert(rem==0);
    return ans;
}

static AggCoreCert aggregate_core_types(const State&st,const vector<Type>&types){
    AggCoreCert out;
    set<int> rs;
    for(auto const&T:types) rs.insert(T.rho);
    for(int r:rs){
        int h=count_if(st.s.begin(),st.s.end(),[&](int d){return d<=r;});
        if(h<=0) continue;
        int m=0;
        for(auto const&T:types) if(T.rho==r&&T.q==h) m+=T.count;
        if(!m) continue;
        vector<int> caps,rr,qq;
        long long total=0;
        for(auto const&T:types){
            bool isU=T.rho==r&&T.q==h;
            if(isU) continue;
            int cap0=T.rho+st.b-st.a-1;
            if(T.q<=h+r-1&&T.q+T.rho>=h-1&&cap0>0){
                int cap=min(cap0,m);
                for(int k=0;k<T.count;++k){caps.push_back(cap);rr.push_back(T.rho);qq.push_back(T.q);total+=cap;}
            }
        }
        long long need=1LL*h*m;
        if(total<need){
            out.reject=true;out.why="CAPACITY_SCALAR";out.r=r;out.h=h;out.u=m;return out;
        }
        set<int> taus;
        for(int d:st.s) if(d>r) taus.insert(d);
        for(int tau:taus){
            int raw=0,demand=0;
            for(auto const&T:types) if(T.rho>=tau) raw+=T.count*T.q;
            for(int d:st.s) if(d>=tau) demand+=d;
            vector<int> loss(caps.size());
            for(size_t i=0;i<caps.size();++i) loss[i]=rr[i]>=tau?max(0,qq[i]-r):0;
            long long ceilF=fractional_cover_ceil(caps,loss,need);
            if(ceilF>=(1LL<<59)) continue;
            if((long long)raw-ceilF<demand){
                out.reject=true;out.why="HIGH_RECEIVER_PRICE";out.r=r;out.h=h;out.u=m;
                out.tau=tau;out.raw=raw;out.demand=demand;out.ceil_loss=ceilF;return out;
            }
        }
    }
    return out;
}

struct GapResult{
    long long profiles=0,agg_capacity_fail=0,agg_high_fail=0;
    long long partition_only_fail=0,partition_high_only_fail=0,exact_core_pass=0;
    int Emax=-1,gap_E=-1;
    string gap_reason,gap_types;
    CoreCert gap_core;
    double seconds=0;
};

static string type_string(const vector<Type>&types){
    ostringstream o;
    for(size_t i=0;i<types.size();++i){if(i)o<<';';o<<types[i].rho<<':'<<types[i].q<<':'<<types[i].count;}
    return o.str();
}

struct GapScanner{
    const State&st;
    int S,Emax;
    vector<Class>cls;
    vector<int>suffix;
    GapResult res;
    explicit GapScanner(const State&s):st(s){
        S=accumulate(st.s.begin(),st.s.end(),0);
        map<int,int>ct;for(int r:st.rho)++ct[r];
        for(auto[r,cnt]:ct){int labels=count_if(st.s.begin(),st.s.end(),[&](int d){return d<=r;});cls.push_back({r,cnt,max(0,min(st.a-r,labels))});}
        suffix.assign(cls.size()+1,0);
        for(int i=(int)cls.size()-1;i>=0;--i)suffix[i]=suffix[i+1]+cls[i].cnt*cls[i].qmax;
        int U=accumulate(st.rho.begin(),st.rho.end(),0)+st.b*(st.b-st.a-1);
        int Qmax=min({suffix[0],U,st.b*(st.b-1)/2});
        Emax=Qmax-S;res.Emax=Emax;
    }
    void eval(int E,const vector<Type>&types){
        ++res.profiles;
        AggCoreCert ac=aggregate_core_types(st,types);
        if(ac.reject){
            if(ac.why=="CAPACITY_SCALAR") ++res.agg_capacity_fail;
            else ++res.agg_high_fail;
            return;
        }
        CoreCert ec=forced_core_types(st,types);
        if(ec.reject){
            if(ec.why=="CAPACITY_PARTITION") ++res.partition_only_fail;
            else ++res.partition_high_only_fail;
            if(res.gap_E<0){res.gap_E=E;res.gap_reason=ec.why;res.gap_core=ec;res.gap_types=type_string(types);}
            return;
        }
        ++res.exact_core_pass;
    }
    void rec(int ci,int used,int Q,int E,vector<Type>&types){
        if(ci==(int)cls.size()){if(used==Q)eval(E,types);return;}
        auto C=cls[ci];
        int lo=max(0,Q-used-suffix[ci+1]),hi=min(C.cnt*C.qmax,Q-used);
        if(lo>hi)return;
        vector<int>sums;
        for(int sm=lo;sm<=hi;++sm)if(!distributions(C.cnt,C.qmax,sm).empty())sums.push_back(sm);
        int rem=0;for(int j=ci;j<(int)cls.size();++j)rem+=cls[j].cnt;
        double tgt=rem?(double)(Q-used)*C.cnt/rem:0.0;
        stable_sort(sums.begin(),sums.end(),[&](int x,int y){return abs(x-tgt)<abs(y-tgt);});
        for(int sm:sums)for(auto const&dist:distributions(C.cnt,C.qmax,sm)){
            size_t old=types.size();
            for(int qq=0;qq<=C.qmax;++qq)if(dist[qq])types.push_back({C.rho,qq,dist[qq],qq+C.rho,0});
            rec(ci+1,used+sm,Q,E,types);
            types.resize(old);
        }
    }
    GapResult run(){
        auto t0=chrono::steady_clock::now();
        vector<Type>types;
        if(Emax>=0)for(int E=0;E<=Emax;++E){
            long long env=excess_envelope(st,E);
            if(env==-(1LL<<50))continue;
            rec(0,0,S+E,E,types);
        }
        res.seconds=chrono::duration<double>(chrono::steady_clock::now()-t0).count();
        return res;
    }
};

int main(int argc,char**argv){
    if(argc<3){cerr<<"usage: gap_census INPUT OUTPUT.tsv\n";return 2;}
    ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;
    int N;in>>N;
    out<<"layer\tstate_id\tS\tEmax\tprofiles_tested\tagg_capacity_fail\tagg_high_fail\tagg_fail\tpartition_only_fail\tpartition_high_only_fail\tpartition_gap_fail\texact_core_pass\tpredicted_core_fail\tseconds\tgap_E\tgap_reason\tgap_r\tgap_h\tgap_U\tgap_tau\tgap_raw\tgap_loss\tgap_demand\tgap_types\n";
    for(int z=0;z<N;++z){
        State st;int ns,nr;in>>st.layer>>st.id>>st.a>>st.b>>st.t>>ns;st.s.resize(ns);for(int&x:st.s)in>>x;in>>nr;st.rho.resize(nr);for(int&x:st.rho)in>>x;
        GapScanner sc(st);GapResult r=sc.run();
        long long af=r.agg_capacity_fail+r.agg_high_fail;
        long long gap=r.partition_only_fail+r.partition_high_only_fail;
        long long pred=af+gap;
        out<<st.layer<<'\t'<<st.id<<'\t'<<accumulate(st.s.begin(),st.s.end(),0)<<'\t'<<r.Emax<<'\t'<<r.profiles<<'\t'
           <<r.agg_capacity_fail<<'\t'<<r.agg_high_fail<<'\t'<<af<<'\t'<<r.partition_only_fail<<'\t'<<r.partition_high_only_fail<<'\t'<<gap<<'\t'
           <<r.exact_core_pass<<'\t'<<pred<<'\t'<<r.seconds<<'\t'<<r.gap_E<<'\t'<<r.gap_reason<<'\t'
           <<r.gap_core.r<<'\t'<<r.gap_core.h<<'\t'<<r.gap_core.u<<'\t'<<r.gap_core.tau<<'\t'<<r.gap_core.raw<<'\t'<<r.gap_core.loss<<'\t'<<r.gap_core.demand<<'\t'<<r.gap_types<<'\n';
        cerr<<"state "<<st.layer<<":"<<st.id<<" profiles="<<r.profiles<<" agg="<<af<<" gap="<<gap<<" sec="<<r.seconds<<"\n";
    }
    return 0;
}
