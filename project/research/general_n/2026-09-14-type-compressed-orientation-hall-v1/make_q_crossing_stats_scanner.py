#!/usr/bin/env python3
"""Instrument the frozen layered-receiver pilot with the exact q-crossing statistic.

Canonical scanner decisions are unchanged. For every exact target-Hall failure,
the generated scanner computes

    C_q = sum_{q,m} min(H^S_{q,m}, L^O_{q,m})

from Q_STRATIFIED_CROSSING_GAP.md and therefore the q-stratified upper bound
`exactcap + C_q`. This adds only O(number of target types) work per Hall failure.
"""
from pathlib import Path

HERE=Path(__file__).resolve().parent
SRC=HERE/'scan_layered_receiver_reach_stats.cpp'
OUT=HERE/'scan_q_crossing_stats.cpp'
s=SRC.read_text()

old='''    vector<int> pv,yv;\n    long long exactcap=0;\n    for(int j=0;j<k;++j){\n        int incoming=0;\n        for(int t=0;t<k;++t)if(selected[t]&&compat_hall_type(types[t],types[j])) incoming+=types[t].n;\n        if(selected[j]) --incoming;\n        if(incoming<0){cerr<<"LAYER_NEGATIVE_INCOMING\\n";exit(78);}\n        exactcap += 1LL*types[j].n*min(types[j].P,incoming);\n        for(int z=0;z<types[j].n;++z){pv.push_back(types[j].P);yv.push_back(incoming);}\n    }'''
new='''    vector<int> pv,yv;\n    long long exactcap=0;\n    map<pair<int,int>,array<int,2>> crossing_blocks;\n    for(int j=0;j<k;++j){\n        int incoming=0;\n        for(int t=0;t<k;++t)if(selected[t]&&compat_hall_type(types[t],types[j])) incoming+=types[t].n;\n        if(selected[j]) --incoming;\n        if(incoming<0){cerr<<"LAYER_NEGATIVE_INCOMING\\n";exit(78);}\n        exactcap += 1LL*types[j].n*min(types[j].P,incoming);\n        for(int z=0;z<types[j].n;++z){pv.push_back(types[j].P);yv.push_back(incoming);}\n        int preincoming=incoming+(selected[j]?1:0);\n        auto &blk=crossing_blocks[{types[j].q,preincoming}];\n        if(selected[j] && types[j].P>=preincoming) blk[0]+=types[j].n;\n        if(!selected[j] && types[j].P<preincoming) blk[1]+=types[j].n;\n    }'''
if s.count(old)!=1:
    raise SystemExit('target loop insertion point not unique')
s=s.replace(old,new,1)

old='''    if(layerupper<exactcap){cerr<<"LAYER_UPPER_BELOW_EXACT\\n";exit(80);}\n    return {coarseflow,refinedflow,demand,h,(int)exactcap,(int)layerupper};\n}'''
new='''    if(layerupper<exactcap){cerr<<"LAYER_UPPER_BELOW_EXACT\\n";exit(80);}\n    int crossing=0;\n    for(auto const&kv:crossing_blocks) crossing+=min(kv.second[0],kv.second[1]);\n    long long qlayerupper=exactcap+crossing;\n    if(qlayerupper>layerupper){cerr<<"QCROSS_Q_UPPER_EXCEEDS_GLOBAL\\n";exit(82);}\n    return {coarseflow,refinedflow,demand,h,(int)exactcap,(int)layerupper,crossing,(int)qlayerupper};\n}'''
if s.count(old)!=1:
    raise SystemExit('return insertion point not unique')
s=s.replace(old,new,1)

old='static tuple<int,int,int,int,int,int> canonical_band_flows'
new='static tuple<int,int,int,int,int,int,int,int> canonical_band_flows'
if s.count(old)!=1:
    raise SystemExit('signature not unique')
s=s.replace(old,new,1)

old='    long long layer_fail=0,layer_pass=0; long long layer_excess_sum=0; int layer_max_excess=0;\n'
new=old+'    long long qlayer_fail=0,qlayer_pass=0,qcross_zero=0,qcross_positive=0,qcross_sum=0; array<long long,10> qcross_hist{}; int qcross_max=0;\n'
if s.count(old)!=1:
    raise SystemExit('counter insertion point not unique')
s=s.replace(old,new,1)

old='''            auto [bflow,ccflow,bdemand,bgen,bexact,layerupper]=canonical_band_flows(q,o,Q);\n            if(bgen!=gcount){cerr<<"BAND_GENERATOR_COUNT_MISMATCH state="<<st.id<<" E="<<E<<" antichain="<<gcount<<" band="<<bgen<<"\\n";exit(11);}\n            if(bexact>=bdemand){cerr<<"LAYER_EXACT_MARGIN_SIGN_FAILURE state="<<st.id<<" E="<<E<<"\\n";exit(81);}\n'''
new='''            auto [bflow,ccflow,bdemand,bgen,bexact,layerupper,qcross,qlayerupper]=canonical_band_flows(q,o,Q);\n            if(bgen!=gcount){cerr<<"BAND_GENERATOR_COUNT_MISMATCH state="<<st.id<<" E="<<E<<" antichain="<<gcount<<" band="<<bgen<<"\\n";exit(11);}\n            if(bexact>=bdemand){cerr<<"LAYER_EXACT_MARGIN_SIGN_FAILURE state="<<st.id<<" E="<<E<<"\\n";exit(81);}\n'''
if s.count(old)!=1:
    raise SystemExit('destructuring point not unique')
s=s.replace(old,new,1)

old='''            if(layerupper<bdemand)++res.layer_fail;\n            else {++res.layer_pass; int ex=layerupper-bdemand; res.layer_excess_sum+=ex; res.layer_max_excess=max(res.layer_max_excess,ex);}\n            if(bflow<bdemand && ccflow>=bdemand){'''
new='''            if(layerupper<bdemand)++res.layer_fail;\n            else {++res.layer_pass; int ex=layerupper-bdemand; res.layer_excess_sum+=ex; res.layer_max_excess=max(res.layer_max_excess,ex);}\n            if(qlayerupper<bdemand)++res.qlayer_fail; else ++res.qlayer_pass;\n            if(qcross==0)++res.qcross_zero; else ++res.qcross_positive;\n            res.qcross_sum+=qcross; res.qcross_max=max(res.qcross_max,qcross); ++res.qcross_hist[min(qcross,9)];\n            if(bflow<bdemand && ccflow>=bdemand){'''
if s.count(old)!=1:
    raise SystemExit('counter point not unique')
s=s.replace(old,new,1)

old='layer_fail\\tlayer_pass\\tlayer_excess_sum\\tlayer_max_excess\\tcost_fail'
new='layer_fail\\tlayer_pass\\tlayer_excess_sum\\tlayer_max_excess\\tqlayer_fail\\tqlayer_pass\\tqcross_zero\\tqcross_positive\\tqcross_sum\\tqcross_max\\tqcross_0\\tqcross_1\\tqcross_2\\tqcross_3\\tqcross_4\\tqcross_5\\tqcross_6\\tqcross_7\\tqcross_8\\tqcross_9plus\\tcost_fail'
if s.count(old)!=1:
    raise SystemExit('header point not unique')
s=s.replace(old,new,1)

old="<<r.layer_fail<<'\\t'<<r.layer_pass<<'\\t'<<r.layer_excess_sum<<'\\t'<<r.layer_max_excess<<'\\t'<<r.cost_fail<<'\\t'\n"
new="<<r.layer_fail<<'\\t'<<r.layer_pass<<'\\t'<<r.layer_excess_sum<<'\\t'<<r.layer_max_excess<<'\\t'<<r.qlayer_fail<<'\\t'<<r.qlayer_pass<<'\\t'<<r.qcross_zero<<'\\t'<<r.qcross_positive<<'\\t'<<r.qcross_sum<<'\\t'<<r.qcross_max<<'\\t'<<r.qcross_hist[0]<<'\\t'<<r.qcross_hist[1]<<'\\t'<<r.qcross_hist[2]<<'\\t'<<r.qcross_hist[3]<<'\\t'<<r.qcross_hist[4]<<'\\t'<<r.qcross_hist[5]<<'\\t'<<r.qcross_hist[6]<<'\\t'<<r.qcross_hist[7]<<'\\t'<<r.qcross_hist[8]<<'\\t'<<r.qcross_hist[9]<<'\\t'<<r.cost_fail<<'\\t'\n"
if s.count(old)!=1:
    raise SystemExit('output point not unique')
s=s.replace(old,new,1)

OUT.write_text('/* GENERATED q-crossing statistics scanner; canonical decisions unchanged. */\n'+s)
print(OUT)
