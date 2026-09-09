#!/usr/bin/env python3
"""Analyze the exact n29 t=3 pure-BC potential as a monotone grid surface.

Transforms BC coordinates (d,-h) to (d,v=b-h), evaluates the exact integer
staircase sum on the finite d=0..dmax, v=0..b grid, and computes first and mixed
finite differences. Nonnegative product-hinge sums have nonnegative mixed
second differences; negative cells therefore obstruct that analytic cone from
representing this exact surface literally.
"""
from pathlib import Path
import argparse,json

def inside(d,v,g,b):
    # generator is (gd,-h0); transformed v0=b-h0=b+second
    return any(d>=p[0] and v>=b+p[1] for p in g)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--exact-json',type=Path,required=True);ap.add_argument('--b',type=int,default=16);ap.add_argument('--dmax',type=int,default=10);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();J=json.loads(z.exact_json.read_text());shapes=[tuple(tuple(p) for p in g) for g in J['BC_shapes']]
    nums=[]
    for i in range(len(shapes)):nums.append(int(J['integer_BC_numerators'].get(str(('BC',i)),0)))
    F=[[sum(w for w,g in zip(nums,shapes) if w and inside(d,v,g,z.b)) for v in range(z.b+1)] for d in range(z.dmax+1)]
    dd=[F[d+1][v]-F[d][v] for d in range(z.dmax) for v in range(z.b+1)]
    dv=[F[d][v+1]-F[d][v] for d in range(z.dmax+1) for v in range(z.b)]
    mixed=[]
    for d in range(z.dmax):
        for v in range(z.b):
            q=F[d+1][v+1]-F[d+1][v]-F[d][v+1]+F[d][v]
            if q:mixed.append({'d':d,'v':v,'value':q})
    out={'schema':'exact-bc-grid-analysis-v1','source':str(z.exact_json),'denominator_scale':J.get('denominator_scale'),'input_shape_count':len(shapes),'nonzero_shape_count':sum(w!=0 for w in nums),'grid_d':[0,z.dmax],'grid_v':[0,z.b],'distinct_surface_values':len({x for row in F for x in row}),'monotone_d':min(dd)>=0,'monotone_v':min(dv)>=0,'mixed_nonzero_count':len(mixed),'mixed_positive_count':sum(x['value']>0 for x in mixed),'mixed_negative_count':sum(x['value']<0 for x in mixed),'mixed_min':min((x['value'] for x in mixed),default=0),'mixed_max':max((x['value'] for x in mixed),default=0),'product_hinge_supermodularity_obstruction':any(x['value']<0 for x in mixed),'mixed_nonzero':mixed,'surface':F,'interpretation':'Negative mixed differences prove this exact staircase surface is not itself a nonnegative sum of product hinges on the same integer grid. This does not rule out a different feasible product-hinge potential.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('surface','mixed_nonzero')},indent=2,sort_keys=True))
if __name__=='__main__':main()
