#!/usr/bin/env python3
"""Instrument the layered-receiver pilot scanner to print every layer false negative.

Run after the antichain, coarse-band, compatible-copy and layered-receiver
generators. Canonical pass/fail decisions are unchanged. Each exact target-Hall
failure which is not detected by the comonotone receiver-layer upper bound is
printed with its canonical type table and incoming counts.
"""
from pathlib import Path

HERE=Path(__file__).resolve().parent
SRC=HERE/'scan_layered_receiver_reach_stats.cpp'
OUT=HERE/'scan_layered_receiver_exception_diagnostic.cpp'
s=SRC.read_text()

needle='static tuple<int,int,int,int,int,int> canonical_band_flows'
if s.count(needle)!=1:
    raise SystemExit('canonical band function not unique')
s=s.replace(needle,'static string LAST_LAYER_TYPE_PROFILE;\n\n'+needle,1)

old='''    vector<int> pv,yv;\n    long long exactcap=0;\n    for(int j=0;j<k;++j){\n        int incoming=0;\n        for(int t=0;t<k;++t)if(selected[t]&&compat_hall_type(types[t],types[j])) incoming+=types[t].n;\n        if(selected[j]) --incoming;\n        if(incoming<0){cerr<<"LAYER_NEGATIVE_INCOMING\\n";exit(78);}\n        exactcap += 1LL*types[j].n*min(types[j].P,incoming);\n        for(int z=0;z<types[j].n;++z){pv.push_back(types[j].P);yv.push_back(incoming);}\n    }'''
new='''    vector<int> pv,yv;\n    long long exactcap=0;\n    ostringstream layerprof;\n    for(int j=0;j<k;++j){\n        int incoming=0;\n        for(int t=0;t<k;++t)if(selected[t]&&compat_hall_type(types[t],types[j])) incoming+=types[t].n;\n        if(selected[j]) --incoming;\n        if(incoming<0){cerr<<"LAYER_NEGATIVE_INCOMING\\n";exit(78);}\n        exactcap += 1LL*types[j].n*min(types[j].P,incoming);\n        for(int z=0;z<types[j].n;++z){pv.push_back(types[j].P);yv.push_back(incoming);}\n        if(j)layerprof<<';';\n        layerprof<<types[j].q<<','<<types[j].c<<','<<types[j].P<<','<<types[j].n<<','<<(int)selected[j]<<','<<band[j]<<','<<incoming;\n    }\n    LAST_LAYER_TYPE_PROFILE=layerprof.str();'''
if s.count(old)!=1:
    raise SystemExit('layer target loop not unique')
s=s.replace(old,new,1)

old='''            if(layerupper<bdemand)++res.layer_fail;\n            else {++res.layer_pass; int ex=layerupper-bdemand; res.layer_excess_sum+=ex; res.layer_max_excess=max(res.layer_max_excess,ex);}'''
new='''            if(layerupper<bdemand)++res.layer_fail;\n            else {\n                ++res.layer_pass; int ex=layerupper-bdemand; res.layer_excess_sum+=ex; res.layer_max_excess=max(res.layer_max_excess,ex);\n                cerr<<"LAYER_EXCEPTION\\tstate="<<st.id<<"\\tE="<<E<<"\\tQ="<<Q\n                    <<"\\tdemand="<<bdemand<<"\\texactcap="<<bexact<<"\\texactdef="<<(bdemand-bexact)\n                    <<"\\tlayerupper="<<layerupper<<"\\tlayerexcess="<<ex<<"\\tgens="<<bgen\n                    <<"\\ttypes="<<LAST_LAYER_TYPE_PROFILE<<"\\n";\n            }'''
if s.count(old)!=1:
    raise SystemExit('layer pass branch not unique')
s=s.replace(old,new,1)

OUT.write_text('/* GENERATED detailed receiver-layer exception diagnostic. */\n'+s)
print(OUT)
