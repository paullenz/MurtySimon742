#!/usr/bin/env python3
"""Preserve the full RX/Hall test of the first adaptive-envelope survivor."""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[1]/'general_n/2026-09-09-rx-hall-v1/rx_hall_exact.py'
spec=spec_from_file_location('preserved_rx_exact',SOURCE)
ex=module_from_spec(spec);spec.loader.exec_module(ex)
s=(1,1)+(2,)*13
rho=(1,)*10+(2,)*8
model=ex.rx.build_rx_hall(15,18,13,s,rho)
ex.add_unit_density_bounds(model)
print('MODEL',len(model.names),len(model.ub),len(model.eq),flush=True)
res=model.solve()
out=dict(state_id=1,s=s,rho=rho,solver_status=int(res.status),
         variables=len(model.names),inequalities=len(model.ub),equalities=len(model.eq))
if res.success:
    out['interpretation']='Numerical feasible relaxation only; not a graph.'
    out['nonzero_proposal']=[[model.names[j],float(x)] for j,x in enumerate(res.x) if abs(x)>1e-9]
else:
    cert=ex.exact_certificate(model)
    out['certificate']=cert
    if cert:out['verified_integer_rhs']=ex.verify_certificate(model,cert)
(HERE/'low_state_rx.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print({k:v for k,v in out.items() if k not in ('nonzero_proposal','certificate')},flush=True)
