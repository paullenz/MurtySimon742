#!/usr/bin/env python3
"""Discover exact Farkas coefficients for the explicit low-demand exception."""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import json
from heavy_model import build,verify

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[1]/'general_n/2026-09-09-rx-hall-v1/rx_hall_exact.py'
spec=spec_from_file_location('rx_exact_heavy',SOURCE)
ex=module_from_spec(spec);spec.loader.exec_module(ex)
s=(1,1)+(2,)*13;rho=(1,)*10+(2,)*8
m=build(s,rho,2)
m._mat=ex.rx.LP._mat
print('MODEL',len(m.names),len(m.ub),len(m.eq),flush=True)
cert=ex.exact_certificate(m)
out=dict(state_id=1,s=s,rho=rho,h=2,certificate=cert)
if cert:out['verification']=verify(m,cert)
(HERE/'heavy_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('EXACT',out.get('verification'),flush=True)
