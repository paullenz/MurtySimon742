#!/usr/bin/env python3
"""Add q-stratified receiver-layer instrumentation only on the global-layer residue.

Run after make_antichain_stats_scanner.py, make_band_reach_scanner.py,
make_compatible_copy_band_reach_scanner.py and make_layered_receiver_reach_scanner.py.

Canonical relational decisions are unchanged. The extra counters test whether
grouping targets only by q restores the correlation lost by the global
receiver-layer rearrangement. The q-only calculation is performed only when
the global rearrangement fails to detect an exact Hall failure; elsewhere
q-stratified detection follows automatically because q-stratification can only
lower the rearrangement upper bound.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'scan_layered_receiver_reach_stats.cpp'
OUT = HERE / 'scan_q_stratified_receiver_residue_stats.cpp'
s = SRC.read_text()

old = '''    if(layerupper<exactcap){cerr<<"LAYER_UPPER_BELOW_EXACT\\n";exit(80);}
    return {coarseflow,refinedflow,demand,h,(int)exactcap,(int)layerupper};
}'''
new = '''    if(layerupper<exactcap){cerr<<"LAYER_UPPER_BELOW_EXACT\\n";exit(80);}

    long long qlayerupper=layerupper;
    int qmixed=0;
    if(layerupper>=demand){
        constexpr int QMAX=32, BMAX=32;
        int qn[QMAX]={0}, qselmask[QMAX]={0};
        int qpv[QMAX][BMAX]={{0}}, qyv[QMAX][BMAX]={{0}};
        for(int j=0;j<k;++j){
            int incoming=0;
            for(int t=0;t<k;++t)if(selected[t]&&compat_hall_type(types[t],types[j])) incoming+=types[t].n;
            if(selected[j]) --incoming;
            if(incoming<0){cerr<<"QSTRAT_NEGATIVE_INCOMING\\n";exit(82);}
            int qj=types[j].q;
            if(qj<0||qj>=QMAX){cerr<<"QSTRAT_Q_RANGE\\n";exit(83);}
            for(int z=0;z<types[j].n;++z){
                if(qn[qj]>=BMAX){cerr<<"QSTRAT_B_RANGE\\n";exit(84);}
                qpv[qj][qn[qj]]=types[j].P;
                qyv[qj][qn[qj]]=incoming;
                ++qn[qj];
            }
            qselmask[qj] |= selected[j] ? 2 : 1;
        }
        qlayerupper=0;
        for(int qj=0;qj<QMAX;++qj)if(qn[qj]){
            sort(qpv[qj],qpv[qj]+qn[qj],greater<int>());
            sort(qyv[qj],qyv[qj]+qn[qj],greater<int>());
            for(int z=0;z<qn[qj];++z) qlayerupper+=min(qpv[qj][z],qyv[qj][z]);
        }
        if(qlayerupper<exactcap){cerr<<"QSTRAT_UPPER_BELOW_EXACT\\n";exit(85);}
        for(int qj=0;qj<QMAX;++qj)if(qselmask[qj]==3) ++qmixed;
    }

    return {coarseflow,refinedflow,demand,h,(int)exactcap,(int)layerupper,(int)qlayerupper,qmixed};
}'''
if s.count(old) != 1:
    raise SystemExit('q-stratified return insertion point not unique')
s = s.replace(old, new, 1)

old = 'static tuple<int,int,int,int,int,int> canonical_band_flows'
new = 'static tuple<int,int,int,int,int,int,int,int> canonical_band_flows'
if s.count(old) != 1:
    raise SystemExit('canonical_band_flows signature not unique')
s = s.replace(old, new, 1)

old = '    long long layer_fail=0,layer_pass=0; long long layer_excess_sum=0; int layer_max_excess=0;\n'
new = old + '    long long qlayer_fail=0,qlayer_pass=0,qlayer_exact=0,qlayer_gap_sum=0,qmixed_profiles=0; int qlayer_max_gap=0,qmixed_max_levels=0;\n'
if s.count(old) != 1:
    raise SystemExit('result counter insertion point not unique')
s = s.replace(old, new, 1)

old = '''            auto [bflow,ccflow,bdemand,bgen,bexact,layerupper]=canonical_band_flows(q,o,Q);
            if(bgen!=gcount){cerr<<"BAND_GENERATOR_COUNT_MISMATCH state="<<st.id<<" E="<<E<<" antichain="<<gcount<<" band="<<bgen<<"\\n";exit(11);}
            if(bexact>=bdemand){cerr<<"LAYER_EXACT_MARGIN_SIGN_FAILURE state="<<st.id<<" E="<<E<<"\\n";exit(81);}
'''
new = '''            auto [bflow,ccflow,bdemand,bgen,bexact,layerupper,qlayerupper,qmixed]=canonical_band_flows(q,o,Q);
            if(bgen!=gcount){cerr<<"BAND_GENERATOR_COUNT_MISMATCH state="<<st.id<<" E="<<E<<" antichain="<<gcount<<" band="<<bgen<<"\\n";exit(11);}
            if(bexact>=bdemand){cerr<<"LAYER_EXACT_MARGIN_SIGN_FAILURE state="<<st.id<<" E="<<E<<"\\n";exit(81);}
'''
if s.count(old) != 1:
    raise SystemExit('destructuring insertion point not unique')
s = s.replace(old, new, 1)

old = '''            if(layerupper<bdemand)++res.layer_fail;
            else {++res.layer_pass; int ex=layerupper-bdemand; res.layer_excess_sum+=ex; res.layer_max_excess=max(res.layer_max_excess,ex);}
            if(bflow<bdemand && ccflow>=bdemand){'''
new = '''            if(layerupper<bdemand)++res.layer_fail;
            else {++res.layer_pass; int ex=layerupper-bdemand; res.layer_excess_sum+=ex; res.layer_max_excess=max(res.layer_max_excess,ex);}

            if(qlayerupper<bdemand)++res.qlayer_fail;
            else ++res.qlayer_pass;
            if(layerupper>=bdemand){
                if(qlayerupper==bexact)++res.qlayer_exact;
                int qgap=qlayerupper-bexact;
                if(qgap<0){cerr<<"QSTRAT_NEGATIVE_GAP state="<<st.id<<" E="<<E<<"\\n";exit(86);}
                res.qlayer_gap_sum+=qgap;
                res.qlayer_max_gap=max(res.qlayer_max_gap,qgap);
                if(qmixed>0){
                    ++res.qmixed_profiles;
                    res.qmixed_max_levels=max(res.qmixed_max_levels,qmixed);
                }
            }
            if(bflow<bdemand && ccflow>=bdemand){'''
if s.count(old) != 1:
    raise SystemExit('q-stratified counter insertion point not unique')
s = s.replace(old, new, 1)

old = 'layer_fail\\tlayer_pass\\tlayer_excess_sum\\tlayer_max_excess\\tcost_fail'
new = 'layer_fail\\tlayer_pass\\tlayer_excess_sum\\tlayer_max_excess\\tqlayer_fail\\tqlayer_pass\\tqlayer_exact\\tqlayer_gap_sum\\tqlayer_max_gap\\tqmixed_profiles\\tqmixed_max_levels\\tcost_fail'
if s.count(old) != 1:
    raise SystemExit('header insertion point not unique')
s = s.replace(old, new, 1)

old = "<<r.layer_fail<<'\\t'<<r.layer_pass<<'\\t'<<r.layer_excess_sum<<'\\t'<<r.layer_max_excess<<'\\t'<<r.cost_fail<<'\\t'\n"
new = "<<r.layer_fail<<'\\t'<<r.layer_pass<<'\\t'<<r.layer_excess_sum<<'\\t'<<r.layer_max_excess<<'\\t'<<r.qlayer_fail<<'\\t'<<r.qlayer_pass<<'\\t'<<r.qlayer_exact<<'\\t'<<r.qlayer_gap_sum<<'\\t'<<r.qlayer_max_gap<<'\\t'<<r.qmixed_profiles<<'\\t'<<r.qmixed_max_levels<<'\\t'<<r.cost_fail<<'\\t'\n"
if s.count(old) != 1:
    raise SystemExit('row output insertion point not unique')
s = s.replace(old, new, 1)

OUT.write_text('/* GENERATED q-stratified receiver residue scanner; canonical decisions unchanged. */\n' + s)
print(OUT)
