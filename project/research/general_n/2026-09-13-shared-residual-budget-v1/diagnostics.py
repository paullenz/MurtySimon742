#!/usr/bin/env python3
"""Preserve the diagnostic explaining why the incoming vector must vary."""
import json
from pathlib import Path
from verify import inputs,data,PREV
HERE=Path(__file__).resolve().parent
P,_=inputs()
old={(w['layer'],w['state_id']):w for w in json.loads((PREV/'FULL_DOMAIN_SPILL_EXACT.json').read_text())['witnesses']}
counts={'patterns':len(P),'minimum_endpoint_total_failures':0,'stored_incoming_endpoint_total_failures':0}
for key,(rec,S) in P.items():
    a,b,q,x,r,L,U,h=data(rec,S)
    counts['minimum_endpoint_total_failures']+=sum(L)>r
    forced=[max([0]+[q[u]+old[key]['p'][u]-x[i] for u in range(b) if i in S[u]]) for i in range(a)]
    counts['stored_incoming_endpoint_total_failures']+=sum(forced)>r
out={'scope':'Diagnostic on frozen selected patterns; old p was only a scalar transport witness. New models permit p to vary.','counts':counts}
(HERE/'DIAGNOSTICS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
