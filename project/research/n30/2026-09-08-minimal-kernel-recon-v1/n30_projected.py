#!/usr/bin/env python3
"""Necessary pair-threshold projection for n=30, Delta=16.

This is the parameterised form of the already-audited n=29 projected screen.
It uses only:
- if every s_i>0, then S=r+2t exactly;
- for selected ui->w, d_i<=rho_u+rho_w;
- one selected orientation per unordered B-pair;
- d_i<=11 from delta(C)>=1.

It never claims graph realizability of a survivor.
"""
import argparse,json,itertools
from pathlib import Path
A=13;B=16;DMAX=11

def load_demands(path):
    with open(path) as f:
        N=int(f.readline());out=[]
        for _ in range(N):
            z=list(map(int,f.readline().split()));out.append(z[:A])
    return out

def reject(s,rho,r,t):
    slack=sum(s)-r-2*t
    if slack and all(x>0 for x in s):return 'zero_slack'
    D=2*r+2*t
    for j in range(2,DMAX+1):
        pairs=sum(u+v>=j for u,v in itertools.combinations(rho,2))
        forced=[v for v in s if v>=j]
        optional=sorted(v for v in s if v<j)
        bounds=[]
        # h = number of labels whose actual F-degree is >=j.
        for h in range(len(forced),A+1):
            # Can h high labels carry total F-degree D at all?
            if DMAX*h+(A-h)*(j-1)<D or j*h>D:continue
            # Demand alone forces this many selected incidences into those h labels.
            q=sum(forced)+sum(optional[:h-len(forced)])
            # Degree total forces at least 'high' F-incidences into the h labels.
            high=max(h*j,D-(A-h)*(j-1))
            # At most min(rho_u,h) residual incidences from source u can land there.
            q=max(q,high-sum(min(x,h) for x in rho))
            bounds.append(q)
        if not bounds or min(bounds)>pairs:return 'projected_pair'
    return None

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--m',type=int,choices=[225,226],required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    D=load_demands(z.demands);t=z.m-224;cnt={'rows':0,'zero_slack':0,'projected_pair':0,'survivors':0};kept=[]
    for line in z.rows.read_text().splitlines():
        row=list(map(int,line.split()));did,total=row[0],row[1];rho=row[2:];cnt['rows']+=1
        kind=reject(D[did],rho,total,t)
        if kind:cnt[kind]+=1
        else:cnt['survivors']+=1;kept.append(row)
    z.output.write_text('\n'.join(' '.join(map(str,r)) for r in kept)+('\n' if kept else ''))
    print(json.dumps({'schema':'n30-d16-projected-v1','scope':{'n':30,'Delta':16,'m':z.m,'t':t},'counts':cnt},sort_keys=True))
if __name__=='__main__':main()
