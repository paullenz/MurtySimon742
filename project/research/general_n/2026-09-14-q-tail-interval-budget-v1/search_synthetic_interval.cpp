// Seeded hostile search in a SPECIFIED bridge relaxation, not graph realization.
#define main original_frozen_main
#include "project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/scan_q_crossing_stats.cpp"
#undef main
#include <random>
int main(int argc,char**argv){
    int trials=argc>1?stoi(argv[1]):100000;
    mt19937_64 rng(74220260914ULL);
    auto pick=[&](int n){return int(rng()%n);};
    ofstream out("SYNTHETIC_INTERVAL_PROFILES.tsv");
    out<<"a\tb\tt\tD0\tEsel\tz\tHall_fail\tbest_tail\tbest_interval\ts\tq\trho\tP\n";
    long long domain=0,capok=0,incok=0,pairok=0,hallfail=0,tailmiss=0,intervalmiss=0,zero=0;
    for(int trial=0;trial<trials;++trial){
        State st;st.layer=9;st.id=trial;st.a=8+pick(17);st.b=st.a+2+pick(5);st.t=1+pick(3);
        int h=2+pick(min(8,st.a-1)-1),z=pick(4)==0?1+pick(2):0,D0=z?pick(4):0;
        st.rho.resize(st.b);for(int& r:st.rho)r=pick(5)<2?1:max(1,h-1+pick(3));
        int r=accumulate(st.rho.begin(),st.rho.end(),0),S=r+2*st.t+D0;
        if(r+st.t>st.a*(st.a-1)/2||S>(st.a-z)*h||S<st.a-z)continue;
        st.s.assign(st.a,0);for(int i=z;i<st.a;++i)st.s[i]=1;
        int remain=S-(st.a-z);
        while(remain){int i=z+pick(st.a-z);if(st.s[i]<h){++st.s[i];--remain;}}
        sort(st.s.begin(),st.s.end());
        vector<int>mx(st.b),q(st.b,0);
        for(int u=0;u<st.b;++u)mx[u]=max(0,min(st.a-st.rho[u],int(count_if(st.s.begin(),st.s.end(),[&](int s){return s<=st.rho[u];}))));
        int maxQ=min({accumulate(mx.begin(),mx.end(),0),r+st.b*(st.b-st.a-1),st.b*(st.b-1)/2});
        if(maxQ<S)continue;
        int Q=S+pick(maxQ-S+1),E=Q-S;
        remain=Q;while(remain){int u=pick(st.b);if(q[u]<mx[u]){++q[u];--remain;}}
        ++domain;auto o=pair_capacity(st,q,st.rho,E);
        if(!o.pass)continue;++capok;
        if(!variable_incidence(st,q,st.rho))continue;++incok;
        if(pair_flow(q,o)<Q)continue;++pairok;
        if(z)++zero;
        auto [f,cost]=target_cost_flow(q,st.rho,o,Q);bool fail=f<Q;hallfail+=fail;
        int exactbest=0,intervalbest=0;
        for(int tau=1;tau<=*max_element(q.begin(),q.end());++tau){
            int demand=0,H=0,U=0;
            for(int u=0;u<st.b;++u)if(q[u]>=tau)demand+=q[u];
            for(int w=0;w<st.b;++w){int y=0,J=0;for(int u=0;u<st.b;++u)if(q[u]>=tau){y+=o.D[u][w];J+=(u!=w&&q[u]<=o.c[w]+1);}H+=min(o.P[w],y);U+=min(o.P[w],J);}
            exactbest=max(exactbest,demand-H);intervalbest=max(intervalbest,demand-U);
        }
        tailmiss+=fail&&exactbest==0;intervalmiss+=fail&&intervalbest==0;
        out<<st.a<<'\t'<<st.b<<'\t'<<st.t<<'\t'<<D0<<'\t'<<E<<'\t'<<z<<'\t'<<fail<<'\t'<<exactbest<<'\t'<<intervalbest<<'\t'<<vs(st.s)<<'\t'<<vs(q)<<'\t'<<vs(st.rho)<<'\t'<<vs(o.P)<<'\n';
    }
    cout<<"{\n  \"seed\":74220260914,\n  \"trials\":"<<trials<<",\n  \"domain\":"<<domain<<",\n  \"cap_pass\":"<<capok<<",\n  \"incidence_pass\":"<<incok<<",\n  \"pair_flow_pass\":"<<pairok<<",\n  \"zero_demand_profiles\":"<<zero<<",\n  \"Hall_failures\":"<<hallfail<<",\n  \"tail_detection_misses\":"<<tailmiss<<",\n  \"interval_detection_misses\":"<<intervalmiss<<"\n}\n";
}
