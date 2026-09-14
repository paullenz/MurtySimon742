#!/usr/bin/env python3
"""Add equal-(q,preincoming) source-selection inversion instrumentation.

Run after make_q_crossing_stats_scanner.py. Canonical scanner decisions are
unchanged. For every exact target-Hall failure, record whether some equal
(q,m) block contains an exterior lower-c target and a selected higher-c target.
Every positive q-crossing implies such an inversion, but not conversely.
"""
from pathlib import Path

HERE=Path(__file__).resolve().parent
SRC=HERE/'scan_q_crossing_stats.cpp'
OUT=HERE/'scan_q_selection_inversion_stats.cpp'
s=SRC.read_text()

old='static tuple<int,int,int,int,int,int,int,int> canonical_band_flows'
new='static tuple<int,int,int,int,int,int,int,int,int> canonical_band_flows'
if s.count(old)!=1:
    raise SystemExit('canonical_band_flows signature not unique')
s=s.replace(old,new,1)

old='''    map<pair<int,int>,array<int,2>> crossing_blocks;\n    for(int j=0;j<k;++j){'''
new='''    map<pair<int,int>,array<int,2>> crossing_blocks;\n    map<pair<int,int>,pair<int,int>> inversion_span; // min exterior c, max selected c\n    for(int j=0;j<k;++j){'''
if s.count(old)!=1:
    raise SystemExit('crossing map insertion point not unique')
s=s.replace(old,new,1)

old='''        int preincoming=incoming+(selected[j]?1:0);\n        auto &blk=crossing_blocks[{types[j].q,preincoming}];\n        if(selected[j] && types[j].P>=preincoming) blk[0]+=types[j].n;\n        if(!selected[j] && types[j].P<preincoming) blk[1]+=types[j].n;\n    }'''
new='''        int preincoming=incoming+(selected[j]?1:0);\n        auto key=make_pair(types[j].q,preincoming);\n        auto &blk=crossing_blocks[key];\n        if(selected[j] && types[j].P>=preincoming) blk[0]+=types[j].n;\n        if(!selected[j] && types[j].P<preincoming) blk[1]+=types[j].n;\n        auto it=inversion_span.find(key);\n        if(it==inversion_span.end())\n            it=inversion_span.emplace(key,make_pair(INT_MAX,INT_MIN)).first;\n        if(selected[j]) it->second.second=max(it->second.second,types[j].c);\n        else it->second.first=min(it->second.first,types[j].c);\n    }'''
if s.count(old)!=1:
    raise SystemExit('target block insertion point not unique')
s=s.replace(old,new,1)

old='''    int crossing=0;\n    for(auto const&kv:crossing_blocks) crossing+=min(kv.second[0],kv.second[1]);\n    long long qlayerupper=exactcap+crossing;'''
new='''    int crossing=0;\n    for(auto const&kv:crossing_blocks) crossing+=min(kv.second[0],kv.second[1]);\n    int inversion_exists=0;\n    for(auto const&kv:inversion_span)\n        if(kv.second.first<kv.second.second){inversion_exists=1;break;}\n    long long qlayerupper=exactcap+crossing;'''
if s.count(old)!=1:
    raise SystemExit('crossing calculation point not unique')
s=s.replace(old,new,1)

old='''    return {coarseflow,refinedflow,demand,h,(int)exactcap,(int)layerupper,crossing,(int)qlayerupper};'''
new='''    return {coarseflow,refinedflow,demand,h,(int)exactcap,(int)layerupper,crossing,(int)qlayerupper,inversion_exists};'''
if s.count(old)!=1:
    raise SystemExit('return point not unique')
s=s.replace(old,new,1)

old='''    long long qlayer_fail=0,qlayer_pass=0,qcross_zero=0,qcross_positive=0,qcross_sum=0; array<long long,10> qcross_hist{}; int qcross_max=0;\n'''
new=old+'''    long long qselection_inversion_profiles=0;\n'''
if s.count(old)!=1:
    raise SystemExit('result field point not unique')
s=s.replace(old,new,1)

old='''            auto [bflow,ccflow,bdemand,bgen,bexact,layerupper,qcross,qlayerupper]=canonical_band_flows(q,o,Q);'''
new='''            auto [bflow,ccflow,bdemand,bgen,bexact,layerupper,qcross,qlayerupper,inversion_exists]=canonical_band_flows(q,o,Q);'''
if s.count(old)!=1:
    raise SystemExit('destructuring point not unique')
s=s.replace(old,new,1)

old='''            res.qcross_sum+=qcross; res.qcross_max=max(res.qcross_max,qcross); ++res.qcross_hist[min(qcross,9)];\n            if(bflow<bdemand && ccflow>=bdemand){'''
new='''            res.qcross_sum+=qcross; res.qcross_max=max(res.qcross_max,qcross); ++res.qcross_hist[min(qcross,9)];\n            if(inversion_exists) ++res.qselection_inversion_profiles;\n            if(bflow<bdemand && ccflow>=bdemand){'''
if s.count(old)!=1:
    raise SystemExit('counter point not unique')
s=s.replace(old,new,1)

old='qcross_8\\tqcross_9plus\\tcost_fail'
new='qcross_8\\tqcross_9plus\\tqselection_inversion_profiles\\tcost_fail'
if s.count(old)!=1:
    raise SystemExit('header point not unique')
s=s.replace(old,new,1)

old="<<r.qcross_hist[8]<<'\\t'<<r.qcross_hist[9]<<'\\t'<<r.cost_fail<<'\\t'\n"
new="<<r.qcross_hist[8]<<'\\t'<<r.qcross_hist[9]<<'\\t'<<r.qselection_inversion_profiles<<'\\t'<<r.cost_fail<<'\\t'\n"
if s.count(old)!=1:
    raise SystemExit('output point not unique')
s=s.replace(old,new,1)

OUT.write_text('/* GENERATED q-selection-inversion scanner; canonical decisions unchanged. */\n'+s)
print(OUT)
