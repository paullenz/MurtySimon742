#!/usr/bin/env python3
"""Materialize the canonical n29 generated BC/SH staircase dictionary.

The canonical full dictionary is the dmax=10 specialization of the n30 shared
base support plus every generated n29 pairwise correction shape. This utility is
pure Python and writes stable sorted indices to generators so support records can
be interpreted without rebuilding the dictionary mentally.
"""
from pathlib import Path
import argparse,json,hashlib

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def min_gens(g):
    pts=sorted(set(tuple(p) for p in g))
    return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))
def trim(g,dmax):return min_gens(p for p in g if p[0]<=dmax)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--base-json',type=Path,required=True);ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--dmax',type=int,default=10);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.base_json.read_text());C=json.loads(z.correction_json.read_text())
    bc={trim(tuple(tuple(p) for p in x['generators']),z.dmax) for x in B['active_BC']};sh={tuple(tuple(p) for p in x['generators']) for x in B['active_SH']}
    for r in C['records']:
        for x in r['cuts']:
            g=tuple(tuple(p) for p in x['generators']);(bc if x['family']=='BC' else sh).add(g)
    bc=sorted(bc);sh=sorted(sh)
    def rows(gs):return [{'index':i,'generators':[list(p) for p in g]} for i,g in enumerate(gs)]
    out={'schema':'n29-canonical-staircase-dictionary-v1','dmax':z.dmax,'BC_count':len(bc),'SH_count':len(sh),'BC':rows(bc),'SH':rows(sh),'provenance':{'base':str(z.base_json),'correction':str(z.correction_json)}}
    payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['dictionary_sha256']=hashlib.sha256(payload).hexdigest()
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'BC_count':len(bc),'SH_count':len(sh),'dictionary_sha256':out['dictionary_sha256']},indent=2))
if __name__=='__main__':main()
