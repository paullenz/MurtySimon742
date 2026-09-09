#!/usr/bin/env python3
"""Compare the exact n30 nine-shape support with the canonical n29 75+12 dictionary.

BC shapes are specialized from dmax=11 to dmax=10 by discarding generators with
first coordinate >10 and re-minimizing. SH shapes are compared literally. The
output records exact dictionary matches and therefore distinguishes reuse of the
generated family from genuinely new staircase geometry.
"""
from pathlib import Path
import argparse,json

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def min_gens(g):
    pts=sorted(set(tuple(p) for p in g));return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))
def trim(g,dmax):return min_gens(p for p in g if p[0]<=dmax)
def tup(g):return tuple(tuple(p) for p in g)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n29-dictionary',type=Path,required=True);ap.add_argument('--n30-exact',type=Path,required=True);ap.add_argument('--dmax29',type=int,default=10);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    D=json.loads(z.n29_dictionary.read_text());E=json.loads(z.n30_exact.read_text())
    bc29={tup(x['generators']):x['index'] for x in D['BC']};sh29={tup(x['generators']):x['index'] for x in D['SH']}
    rb=[]
    for i,g0 in enumerate(E['BC_shapes']):
        g=tup(g0);gt=trim(g,z.dmax29);rb.append({'n30_position':i,'n30_generators':[list(p) for p in g],'specialized_dmax10':[list(p) for p in gt],'n29_exact_index':bc29.get(gt),'exact_match':gt in bc29})
    rs=[]
    for i,g0 in enumerate(E['SH_shapes']):
        g=tup(g0);rs.append({'n30_position':i,'generators':[list(p) for p in g],'n29_exact_index':sh29.get(g),'exact_match':g in sh29})
    out={'schema':'n30-exact-vs-n29-canonical-dictionary-v1','n29_BC_count':len(bc29),'n29_SH_count':len(sh29),'n30_BC_count':len(rb),'n30_SH_count':len(rs),'BC_exact_matches':sum(x['exact_match'] for x in rb),'SH_exact_matches':sum(x['exact_match'] for x in rs),'BC_records':rb,'SH_records':rs,'interpretation':'BC comparison first specializes n30 generators to dmax=10; SH comparison is literal.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
