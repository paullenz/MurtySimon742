#!/usr/bin/env python3
"""Add receiver-layer reach instrumentation to the compatible-copy pilot scanner.

Run after make_antichain_stats_scanner.py, make_band_reach_scanner.py and
make_compatible_copy_band_reach_scanner.py. Canonical relational decisions are
unchanged. The added counters ask whether the comonotone receiver-layer upper
bound already certifies each exact target-Hall failure.
"""
from pathlib import Path

HERE=Path(__file__).resolve().parent
SRC=HERE/'scan_compatible_copy_band_reach_stats.cpp'
OUT=HERE/'scan_layered_receiver_reach_stats.cpp'
s=SRC.read_text()

old='''    int coarseflow=coarse.flow(BS,BT);\n    int refinedflow=refined.flow(BS,BT);\n    if(refinedflow>coarseflow){\n        cerr<<"CCBAND_FLOW_EXCEEDS_COARSE refined="<<refinedflow<<" coarse="<<coarseflow<<"\\n";\n        exit(76);\n    }\n    return {coarseflow,refinedflow,demand,h};\n}'''
new='''    int coarseflow=coarse.flow(BS,BT);\n    int refinedflow=refined.flow(BS,BT);\n    if(refinedflow>coarseflow){\n        cerr<<"CCBAND_FLOW_EXCEEDS_COARSE refined="<<refinedflow<<" coarse="<<coarseflow<<"\\n";\n        exit(76);\n    }\n\n    vector<int> pv,yv;\n    long long exactcap=0;\n    for(int j=0;j<k;++j){\n        int incoming=0;\n        for(int t=0;t<k;++t)if(selected[t]&&compat_hall_type(types[t],types[j])) incoming+=types[t].n;\n        if(selected[j]) --incoming;\n        if(incoming<0){cerr<<"LAYER_NEGATIVE_INCOMING\\n";exit(78);}\n        exactcap += 1LL*types[j].n*min(types[j].P,incoming);\n        for(int z=0;z<types[j].n;++z){pv.push_back(types[j].P);yv.push_back(incoming);}\n    }\n    if(exactcap>=demand){\n        cerr<<"LAYER_CANONICAL_WITNESS_NOT_DEFICIENT exactcap="<<exactcap<<" demand="<<demand<<"\\n";\n        exit(79);\n    }\n    sort(pv.begin(),pv.end(),greater<int>());\n    sort(yv.begin(),yv.end(),greater<int>());\n    long long layerupper=0;\n    for(int z=0;z<(int)pv.size();++z) layerupper+=min(pv[z],yv[z]);\n    if(layerupper<exactcap){cerr<<"LAYER_UPPER_BELOW_EXACT\\n";exit(80);}\n    return {coarseflow,refinedflow,demand,h,(int)exactcap,(int)layerupper};\n}'''
if s.count(old)!=1:
    raise SystemExit('canonical flow return block not unique')
s=s.replace(old,new,1)
s=s.replace('static tuple<int,int,int,int> canonical_band_flows','static tuple<int,int,int,int,int,int> canonical_band_flows',1)

old='    long long ccband_fail=0,ccband_pass=0;\n'
new=old+'    long long layer_fail=0,layer_pass=0; long long layer_excess_sum=0; int layer_max_excess=0;\n'
if s.count(old)!=1:
    raise SystemExit('result counter insertion point not unique')
s=s.replace(old,new,1)

old='''            auto [bflow,ccflow,bdemand,bgen]=canonical_band_flows(q,o,Q);\n            if(bgen!=gcount){cerr<<"BAND_GENERATOR_COUNT_MISMATCH state="<<st.id<<" E="<<E<<" antichain="<<gcount<<" band="<<bgen<<"\\n";exit(11);}\n'''
new='''            auto [bflow,ccflow,bdemand,bgen,bexact,layerupper]=canonical_band_flows(q,o,Q);\n            if(bgen!=gcount){cerr<<"BAND_GENERATOR_COUNT_MISMATCH state="<<st.id<<" E="<<E<<" antichain="<<gcount<<" band="<<bgen<<"\\n";exit(11);}\n            if(bexact>=bdemand){cerr<<"LAYER_EXACT_MARGIN_SIGN_FAILURE state="<<st.id<<" E="<<E<<"\\n";exit(81);}\n'''
if s.count(old)!=1:
    raise SystemExit('instrumentation destructuring point not unique')
s=s.replace(old,new,1)

old='''            if(ccflow<bdemand)++res.ccband_fail;\n            else ++res.ccband_pass;\n            if(bflow<bdemand && ccflow>=bdemand){'''
new='''            if(ccflow<bdemand)++res.ccband_fail;\n            else ++res.ccband_pass;\n            if(layerupper<bdemand)++res.layer_fail;\n            else {++res.layer_pass; int ex=layerupper-bdemand; res.layer_excess_sum+=ex; res.layer_max_excess=max(res.layer_max_excess,ex);}\n            if(bflow<bdemand && ccflow>=bdemand){'''
if s.count(old)!=1:
    raise SystemExit('layer counter point not unique')
s=s.replace(old,new,1)

old='band_fail_gen9plus\\tband_maxgen\\tccband_fail\\tccband_pass\\tcost_fail'
new='band_fail_gen9plus\\tband_maxgen\\tccband_fail\\tccband_pass\\tlayer_fail\\tlayer_pass\\tlayer_excess_sum\\tlayer_max_excess\\tcost_fail'
if s.count(old)!=1:
    raise SystemExit('header point not unique')
s=s.replace(old,new,1)

old="           <<r.band_fail_genhist[9]<<'\\t'<<r.band_maxgen<<'\\t'<<r.ccband_fail<<'\\t'<<r.ccband_pass<<'\\t'<<r.cost_fail<<'\\t'\n"
new="           <<r.band_fail_genhist[9]<<'\\t'<<r.band_maxgen<<'\\t'<<r.ccband_fail<<'\\t'<<r.ccband_pass<<'\\t'<<r.layer_fail<<'\\t'<<r.layer_pass<<'\\t'<<r.layer_excess_sum<<'\\t'<<r.layer_max_excess<<'\\t'<<r.cost_fail<<'\\t'\n"
if s.count(old)!=1:
    raise SystemExit('output point not unique')
s=s.replace(old,new,1)

OUT.write_text('/* GENERATED layered-receiver reach scanner; canonical decisions unchanged. */\n'+s)
print(OUT)
