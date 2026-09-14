#!/usr/bin/env python3
"""Generate a diagnostic scanner for receiver-layer false negatives.

Run after the antichain, coarse-band, compatible-copy and layered-receiver
scanner generators.  Mathematical decisions are unchanged.  The generated
scanner writes one diagnostic TSV row exactly when exact canonical target Hall
fails but the one-dimensional layered-receiver rearrangement upper bound does
not certify that failure.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'scan_layered_receiver_reach_stats.cpp'
OUT = HERE / 'scan_layered_receiver_exception_diagnostic.cpp'
s = SRC.read_text()

sig = 'static tuple<int,int,int,int,int,int> canonical_band_flows(const vector<int>&q,const OD&o,int Q){'
repl = r'''static ofstream* LAYER_EXCEPTION_OUT=nullptr;
static string diag_join(const vector<int>&v){
    ostringstream o;for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}return o.str();
}
static tuple<int,int,int,int,int,int> canonical_band_flows(const State&st,int E,const vector<int>&q,const vector<int>&rho,const OD&o,int Q){'''
if s.count(sig) != 1:
    raise SystemExit('canonical_band_flows signature not unique')
s = s.replace(sig, repl, 1)

old = r'''    vector<int> pv,yv;
    long long exactcap=0;
    for(int j=0;j<k;++j){
        int incoming=0;
        for(int t=0;t<k;++t)if(selected[t]&&compat_hall_type(types[t],types[j])) incoming+=types[t].n;
        if(selected[j]) --incoming;
        if(incoming<0){cerr<<"LAYER_NEGATIVE_INCOMING\n";exit(78);}
        exactcap += 1LL*types[j].n*min(types[j].P,incoming);
        for(int z=0;z<types[j].n;++z){pv.push_back(types[j].P);yv.push_back(incoming);}
    }
    if(exactcap>=demand){
        cerr<<"LAYER_CANONICAL_WITNESS_NOT_DEFICIENT exactcap="<<exactcap<<" demand="<<demand<<"\n";
        exit(79);
    }
    sort(pv.begin(),pv.end(),greater<int>());
    sort(yv.begin(),yv.end(),greater<int>());
    long long layerupper=0;
    for(int z=0;z<(int)pv.size();++z) layerupper+=min(pv[z],yv[z]);
    if(layerupper<exactcap){cerr<<"LAYER_UPPER_BELOW_EXACT\n";exit(80);}
    return {coarseflow,refinedflow,demand,h,(int)exactcap,(int)layerupper};'''
new = r'''    vector<int> pv,yv,incoming_type(k,0);
    long long exactcap=0;
    for(int j=0;j<k;++j){
        int incoming=0;
        for(int t=0;t<k;++t)if(selected[t]&&compat_hall_type(types[t],types[j])) incoming+=types[t].n;
        if(selected[j]) --incoming;
        if(incoming<0){cerr<<"LAYER_NEGATIVE_INCOMING\n";exit(78);}
        incoming_type[j]=incoming;
        exactcap += 1LL*types[j].n*min(types[j].P,incoming);
        for(int z=0;z<types[j].n;++z){pv.push_back(types[j].P);yv.push_back(incoming);}
    }
    if(exactcap>=demand){
        cerr<<"LAYER_CANONICAL_WITNESS_NOT_DEFICIENT exactcap="<<exactcap<<" demand="<<demand<<"\n";
        exit(79);
    }
    vector<int> psort=pv,ysort=yv;
    sort(psort.begin(),psort.end(),greater<int>());
    sort(ysort.begin(),ysort.end(),greater<int>());
    long long layerupper=0;
    for(int z=0;z<(int)psort.size();++z) layerupper+=min(psort[z],ysort[z]);
    if(layerupper<exactcap){cerr<<"LAYER_UPPER_BELOW_EXACT\n";exit(80);}

    if(layerupper>=demand && LAYER_EXCEPTION_OUT){
        int selected_types=0,selected_copies=0; long long exterior_demand=0,slack_mass=0;
        for(int j=0;j<k;++j){
            if(selected[j]){++selected_types;selected_copies+=types[j].n;}
            else exterior_demand += 1LL*types[j].n*types[j].q;
            slack_mass += 1LL*types[j].n*max(0,types[j].P-incoming_type[j]);
        }
        int maxlev=0;for(int x:pv)maxlev=max(maxlev,x);for(int x:yv)maxlev=max(maxlev,x);
        ostringstream layergap;
        int max_single_gap=0,positive_gap_levels=0;
        for(int ell=1;ell<=maxlev;++ell){
            int A=0,B=0,I=0;
            for(int j=0;j<k;++j){
                int a=(types[j].P>=ell),b=(incoming_type[j]>=ell);
                A+=types[j].n*a;B+=types[j].n*b;I+=types[j].n*(a&&b);
            }
            int g=min(A,B)-I;
            if(g){if(layergap.tellp()>0)layergap<<';';layergap<<ell<<':'<<A<<':'<<B<<':'<<I<<':'<<g;max_single_gap=max(max_single_gap,g);++positive_gap_levels;}
        }
        ostringstream tt;
        for(int j=0;j<k;++j){
            if(j)tt<<';';
            tt<<types[j].q<<','<<types[j].c<<','<<types[j].P<<','<<types[j].n<<','
              <<int(selected[j])<<','<<band[j]<<','<<incoming_type[j]<<','<<max(0,types[j].P-incoming_type[j]);
        }
        *LAYER_EXCEPTION_OUT
          <<st.layer<<'\t'<<st.id<<'\t'<<st.a<<'\t'<<st.b<<'\t'<<st.t<<'\t'<<E<<'\t'<<Q<<'\t'
          <<demand<<'\t'<<exactcap<<'\t'<<(demand-exactcap)<<'\t'<<layerupper<<'\t'<<(layerupper-demand)<<'\t'
          <<(layerupper-exactcap)<<'\t'<<h<<'\t'<<k<<'\t'<<selected_types<<'\t'<<selected_copies<<'\t'
          <<exterior_demand<<'\t'<<slack_mass<<'\t'<<(slack_mass-exterior_demand)<<'\t'
          <<positive_gap_levels<<'\t'<<max_single_gap<<'\t'<<diag_join(rho)<<'\t'<<diag_join(q)<<'\t'
          <<layergap.str()<<'\t'<<tt.str()<<'\n';
    }
    return {coarseflow,refinedflow,demand,h,(int)exactcap,(int)layerupper};'''
if s.count(old) != 1:
    raise SystemExit('layer capacity block not unique')
s = s.replace(old, new, 1)

old = 'auto [bflow,ccflow,bdemand,bgen,bexact,layerupper]=canonical_band_flows(q,o,Q);'
new = 'auto [bflow,ccflow,bdemand,bgen,bexact,layerupper]=canonical_band_flows(st,E,q,rho,o,Q);'
if s.count(old) != 1:
    raise SystemExit('canonical band call not unique')
s = s.replace(old, new, 1)

old = r'''int main(int argc,char**argv){
    if(argc<3){cerr<<"usage: scan_post_pair_relational INPUT OUTPUT.tsv\n";return 2;}
    ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;int N;in>>N;'''
new = r'''int main(int argc,char**argv){
    if(argc<4){cerr<<"usage: scan_layered_receiver_exception_diagnostic INPUT OUTPUT.tsv EXCEPTIONS.tsv\n";return 2;}
    ifstream in(argv[1]);ofstream out(argv[2]);ofstream diag(argv[3]);if(!in||!out||!diag)return 2;LAYER_EXCEPTION_OUT=&diag;
    diag<<"layer\tstate_id\ta\tb\tt\tE\tQ\tdemand\texact_capacity\thall_deficit\tlayer_upper\tlayer_excess\tcorrelation_loss\tgenerator_count\ttype_count\tselected_type_count\tselected_copy_count\texterior_demand\tresidual_slack_mass\tslack_minus_exterior_demand\tpositive_gap_levels\tmax_single_layer_gap\trho\tq\tlayer_gaps\ttypes_q_c_P_n_selected_band_incoming_slack\n";
    int N;in>>N;'''
if s.count(old) != 1:
    raise SystemExit('main opening block not unique')
s = s.replace(old, new, 1)

OUT.write_text('/* GENERATED receiver-layer exception diagnostic; canonical decisions unchanged. */\n'+s)
print(OUT)
