#!/usr/bin/env python3
"""Exact row-level threshold-capacity screen for n=30 Delta=16.

The demand stage used only an optimistic upper bound on z_h.  Once a concrete
residual row rho is present, the exact theorem
  z_h >= max{s_i:s_i>=h},
  2 W_h <= z_h^2-z_h+h(h+1)
can be applied directly.  This is a necessary condition already proved in the
standalone graph-to-model bridge.
"""
import argparse,json
from pathlib import Path
A=13

def load_demands(path):
    with open(path) as f:
        N=int(f.readline());out=[]
        for _ in range(N):
            z=list(map(int,f.readline().split()));out.append(z[:A])
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--m',type=int,choices=[225,226],required=True);z=ap.parse_args()
    D=load_demands(z.demands);cnt={'rows':0,'source_count':0,'threshold':0,'survivors':0};kept=[]
    for line in z.rows.read_text().splitlines():
        row=list(map(int,line.split()));did=row[0];rho=row[2:];s=D[did];cnt['rows']+=1;bad=None
        for h in range(2,A):
            high=[x for x in s if x>=h]
            if not high:continue
            zh=sum(x>=h for x in rho)
            if max(high)>zh:bad='source_count';break
            W=sum(high)
            if 2*W>zh*zh-zh+h*(h+1):bad='threshold';break
        if bad:cnt[bad]+=1
        else:cnt['survivors']+=1;kept.append(row)
    z.output.write_text('\n'.join(' '.join(map(str,r)) for r in kept)+('\n' if kept else ''))
    print(json.dumps({'schema':'n30-d16-row-threshold-v1','scope':{'n':30,'Delta':16,'m':z.m},'counts':cnt},sort_keys=True))
if __name__=='__main__':main()
