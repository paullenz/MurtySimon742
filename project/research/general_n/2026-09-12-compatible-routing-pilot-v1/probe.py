#!/usr/bin/env python3
"""Bounded numerical discovery with exact integer acceptance and full logs."""
from pathlib import Path
from functools import reduce
from math import gcd
import argparse,json,platform,time
import numpy as np
import scipy
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,csr_matrix,hstack,vstack
from model import MODES,build,capacity,digest,verify
HERE=Path(__file__).resolve().parent

def matrix(rows,n):
    rr=[];cc=[];vv=[]
    for i,row in enumerate(rows):
        for col,c in row['coefficients'].items():rr.append(i);cc.append(col);vv.append(c)
    return coo_matrix((vv,(rr,cc)),shape=(len(rows),n)).tocsr()

def propose(model,limit):
    n=len(model['names']);nu=len(model['ub']);ne=len(model['eq'])
    A=matrix(model['ub'],n);E=matrix(model['eq'],n)
    b=np.array([r['rhs'] for r in model['ub']],float);f=np.array([r['rhs'] for r in model['eq']],float)
    D=vstack([hstack([-A.T,-E.T,E.T],format='csr'),csr_matrix(np.r_[b,f,-f].reshape(1,-1))],format='csr')
    start=time.monotonic()
    result=linprog(np.ones(nu+2*ne),A_ub=D,b_ub=np.r_[np.zeros(n),-1.0],bounds=(0,None),method='highs',options={'time_limit':limit})
    log=dict(status=int(result.status),message=result.message,seconds=time.monotonic()-start,
             objective=float(result.fun) if result.fun is not None else None,
             proposal=result.x.tolist() if result.x is not None else None,rounding=[])
    if not result.success:return None,log
    for scale in (100,10000,1000000,100000000):
        lam=[max(0,round(float(x)*scale)) for x in result.x[:nu]]
        mu=[round(float(x-y)*scale) for x,y in zip(result.x[nu:nu+ne],result.x[nu+ne:])]
        coefficients=[0]*n;rhs=0
        for kind,weights in [('ub',lam),('eq',mu)]:
            for row,w in zip(model[kind],weights):
                rhs+=w*row['rhs']
                for col,c in row['coefficients'].items():coefficients[col]+=w*c
        repairs=[]
        for col,c in enumerate(coefficients):
            if c<0:
                lam[model['bound_start']+col]-=c;rhs-=c*model['bounds'][col];repairs.append([col,-c]);coefficients[col]=0
        log['rounding'].append(dict(scale=scale,repairs=repairs,repaired_rhs=rhs))
        if rhs>=0:continue
        divisor=reduce(gcd,lam+[abs(x) for x in mu]) or 1
        cert=dict(ub=[[i,w//divisor] for i,w in enumerate(lam) if w],eq=[[i,w//divisor] for i,w in enumerate(mu) if w],rhs=rhs//divisor,scale=scale)
        verify(model,cert);return cert,log
    return None,log

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--limit',type=float,default=10);ap.add_argument('--count',type=int);args=ap.parse_args()
    inputs=json.loads((HERE/'pilot_inputs.json').read_text())['sample']
    if args.count:inputs=inputs[:args.count]
    start=time.monotonic();counts={m:0 for m in MODES};attempts=0
    with (HERE/'pilot_results.jsonl').open('w') as out:
        for rec in inputs:
            result=dict(layer=rec['layer'],state_id=rec['state_id'],modes={},attempts=[])
            for mode in MODES:
                witness=None
                for h in range(2,max(rec['s'])+1):
                    W=sum(s for s in rec['s'] if s>=h);cases=[]
                    for j,cap in enumerate(capacity(rec,h)):
                        if W>cap:cases.append(dict(j=j,source_capacity=cap));continue
                        model=build(rec,h,j,mode);certificate,log=propose(model,args.limit);attempts+=1
                        log.update(h=h,j=j,mode=mode,model_sha256=digest(model),variables=len(model['names']),equalities=len(model['eq']),inequalities=len(model['ub']),certificate=certificate)
                        result['attempts'].append(log)
                        if certificate is None:break
                        cases.append(dict(j=j,attempt_index=len(result['attempts'])-1))
                    else:witness=dict(h=h,cases=cases);break
                result['modes'][mode]=witness;counts[mode]+=witness is not None
                print('MODE',rec['layer'],rec['state_id'],mode,bool(witness),'elapsed',round(time.monotonic()-start,2),flush=True)
            out.write(json.dumps(result,separators=(',',':'))+'\n');out.flush()
    report=dict(schema='compatible-routing-pilot-summary-v1',selected=len(inputs),exclusions=counts,attempts=attempts,seconds=time.monotonic()-start,
        thresholds='h=2..max(s), T=4h',early_stopping='First uncertified j blocks a threshold; first fully excluded threshold ends a mode for a state.',external_review='OPEN')
    (HERE/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report),flush=True)

if __name__=='__main__':main()
