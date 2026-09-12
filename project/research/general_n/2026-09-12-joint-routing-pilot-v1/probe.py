#!/usr/bin/env python3
"""Small LPs propose rational multipliers; integer envelopes decide exclusions."""
from pathlib import Path
import argparse,json,time,platform
import numpy as np
import scipy
from scipy.optimize import linprog
from joint_bound import context,evaluate
HERE=Path(__file__).resolve().parent


def propose(ctx,j,mode):
    # Variables lambda, mu, eta, theta, and one free local upper envelope per rho.
    rows=[];rhs=[];gs=ctx['groups'];h=ctx['h']
    for k,g in enumerate(gs):
        for H,p,B in g['options']:
            hi=int(H>h);D=H*hi
            incoming=p if mode=='aggregate' else min(p,j-hi)
            row=[0]*(4+len(gs));row[0]=incoming-D;row[1]=-D;row[2]=H
            row[3]=-hi;row[4+k]=-1
            rows.append(row);rhs.append(-B)
    pair=j*ctx['z']-j*(j+1)//2
    obj=[0,pair,-ctx['W'],j]+[g['n'] for g in gs]
    bounds=[(0,16*h),(0,16*h),(0,16*h),(None,None)]+[(None,None)]*len(gs)
    if mode=='local':bounds[0]=(0,0);bounds[1]=(0,0)
    if mode=='aggregate':bounds[1]=(0,0)
    if mode=='pair':bounds[0]=(0,0)
    res=linprog(obj,A_ub=np.asarray(rows),b_ub=np.asarray(rhs),bounds=bounds,method='highs',options={'time_limit':10})
    log=dict(h=h,T=ctx['T'],j=j,mode=mode,status=int(res.status),message=res.message)
    if not res.success:return None,log
    log['proposed_objective']=float(res.fun)
    best=None
    for den in (1,2,10,100,1000):
        vals=[max(0,round(float(x)*den)) for x in res.x[:3]]
        check=evaluate(ctx,j,*vals,den,mode)
        if best is None or check['gap']*best['denominator']>best['gap']*den:best=check
        if check['gap']>0:break
    log['exact']=best
    return best,log


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='pilot_results.jsonl');args=ap.parse_args()
    records=json.loads((HERE/'pilot_inputs.json').read_text())['sample'];start=time.monotonic()
    with (HERE/args.output).open('w') as out:
        for rec in records:
            result=dict(layer=rec['layer'],state_id=rec['state_id'],attempts=[],modes={})
            # Complete the same cutoff/threshold search for all ablations.
            for mode in ('local','aggregate','pair','joint'):
                witness=None
                for h in range(1,max(rec['s'])+1):
                    ctx=context(rec,h,4*h);cases=[]
                    for j,upper in enumerate(ctx['jbounds']):
                        if ctx['W']>upper:
                            cases.append(dict(j=j,source_capacity_exclusion=True,upper=upper));continue
                        cert,log=propose(ctx,j,mode);result['attempts'].append(log)
                        if not cert or cert['gap']<=0:break
                        cases.append(cert)
                    else:
                        witness=dict(h=h,T=4*h,cases=cases);break
                result['modes'][mode]=witness
            out.write(json.dumps(result,separators=(',',':'))+'\n');out.flush()
            print('STATE',result['layer'],result['state_id'],{k:v is not None for k,v in result['modes'].items()},round(time.monotonic()-start,2),flush=True)
    (HERE/'environment.json').write_text(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform(),solver='scipy.optimize.linprog(method=highs)',time_limit_per_lp=10,multiplier_bound='0..16h',rational_denominators=[1,2,10,100,1000]),indent=2)+'\n')

if __name__=='__main__':main()
