#!/usr/bin/env python3
"""Exact finite diagnostic for the eight-star parity-star interface."""
import sys,json
from pathlib import Path
sys.path.insert(0,'/workspace/scratch/a4369cb67676/deps')
from maxsat_fixed_codes import maximize
base=['C00','C01','C10','C11','C20','C21']+['S0']*2+['S3']*2+['S5']*2+['S6']*2
rows=[]; out=Path(__file__).with_name('PARITY_STAR_MAXSAT_GRID.json')
for r,q in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3)]:
 z=maximize(base+['P0']*r+['P1']*q)
 rows.append({'r':r,'q':q,**z,'matches_rq_plus_14':z['max_A_edges']==r*q+14})
 out.write_text(json.dumps({'scope':'exact fixed-code MaxSAT diagnostic; not a general theorem','base_codes':base,'rows':rows},indent=2)+'\n')
 print(r,q,z['max_A_edges'],round(z['seconds'],3),flush=True)
assert all(x['matches_rq_plus_14'] for x in rows)
