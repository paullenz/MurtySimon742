#!/usr/bin/env python3
"""Solver-free exact audit of N30_M226_HAND_ENDPOINT_REDUCTION.md.

Checks every allowed integer source type (rho,q,p) in the eight table rows,
verifies the stated pointwise minima L_rho, and recomputes delta exactly.
No LP solver and no floating point are used.
"""
from fractions import Fraction
import json,argparse
from pathlib import Path

A=13;B=16
ROWS=[
 {
  'tag':'2233','s':[2,2]+[3]*11,'rho':[1]*7+[2]+[3]*8,'D':2,'c':6,
  'z':{2:6,5:1,6:1,8:1},'L':{1:0,2:-42,3:-50},'delta':Fraction(1,1)},
 {
  'tag':'2331','s':[2]+[3]*12,'rho':[1]*7+[3]*9,'D':2,'c':6,
  'z':{2:3,3:4,6:1,8:1},'L':{1:0,3:-50},'delta':Fraction(3,1)},
 {
  'tag':'3^13-r35a','s':[3]*13,'rho':[1]*7+[3]*8+[4],'D':2,'c':6,
  'z':{2:7,6:1,7:1},'L':{1:0,3:-48,4:-60},'delta':Fraction(12,1)},
 {
  'tag':'3^13-r35b','s':[3]*13,'rho':[1]*6+[2]+[3]*9,'D':2,'c':6,
  'z':{2:3,3:4,6:1,8:1},'L':{1:0,2:-12,3:-50},'delta':Fraction(3,1)},
 {
  'tag':'3344','s':[3]*4+[4]*9,'rho':[1]*6+[3]*2+[4]*8,'D':3,'c':7,
  'z':{2:11,5:1,6:1,7:2},'L':{1:0,3:-90,4:-102},'delta':Fraction(4,1)},
 {
  'tag':'3344b','s':[3]*2+[4]*11,'rho':[1]*5+[2]+[3]+[4]*9,'D':3,'c':7,
  'z':{2:6,3:3,4:3,6:1,7:1,8:1},'L':{1:0,2:-24,3:-90,4:-102},'delta':Fraction(6,1)},
 {
  'tag':'3444','s':[3]+[4]*12,'rho':[1]*5+[2]+[4]*10,'D':2,'c':7,
  'z':{2:3,3:3,5:3,8:1},'L':{1:0,2:-12,4:-70},'delta':Fraction(1,1)},
 {
  'tag':'4^13','s':[4]*13,'rho':[1]*5+[3]+[4]*10,'D':2,'c':7,
  'z':{1:1,2:5,4:1,5:1,6:1,7:1},'L':{1:-3,3:-30,4:-68},'delta':Fraction(3,2)},
]

def h(k,rho,q,p):
    return (q if q>=k+1 else 0) - (p if rho+q>=k else 0)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');z=ap.parse_args()
    out={'schema':'n30-m226-hand-endpoint-table-exact-v1','status':'PASS','rows':[],'solver_used':False,'floating_point_used':False}
    for R in ROWS:
        mins={}
        minimizers={}
        smin=min(R['s'])
        for rho in sorted(set(R['rho'])):
            vals=[]
            for q in range(A-rho+1):
                if rho<smin and q>0:
                    continue
                for p in range(min(rho+2,B-1-q)+1):
                    alpha=max(0,p-rho+1)
                    F=R['D']*q*(alpha-R['c'])+sum(w*h(k,rho,q,p) for k,w in R['z'].items())
                    vals.append((F,q,p,alpha))
                    assert F>=R['L'][rho],(R['tag'],rho,q,p,F,R['L'][rho])
            m=min(v[0] for v in vals)
            assert m==R['L'][rho],(R['tag'],rho,m,R['L'][rho])
            mins[str(rho)]=m
            minimizers[str(rho)]=[(q,p,a) for F,q,p,a in vals if F==m]
        S=sum(R['s'])
        Lsum=sum(R['rho'].count(rho)*L for rho,L in R['L'].items())
        delta=Fraction(R['D']*R['c']*S+Lsum,R['D'])
        assert delta==R['delta'] and delta>0,(R['tag'],delta,R['delta'])
        out['rows'].append({
            'tag':R['tag'],'S':S,'D':R['D'],'c':R['c'],'weights':R['z'],
            'minima':mins,'minimizers':minimizers,
            'delta_numerator':delta.numerator,'delta_denominator':delta.denominator,
        })
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if z.output:Path(z.output).write_text(text)
    print(text,end='')
if __name__=='__main__':main()
