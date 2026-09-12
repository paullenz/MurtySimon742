#!/usr/bin/env python3
"""Bounded profile pilot: floating proposals, exact integer acceptance."""
from pathlib import Path
from collections import Counter
import argparse,json,sys,time
import numpy as np
from scipy.optimize import linprog
from projection import baseline,context,evaluate
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'2026-09-12-heavy-load-family-v1'))
from evidence_io import read_records


def propose(ctx,j,penalty=True):
    # lambda, mu, eta, kappa, A0, A1; two class envelopes.
    rows=[];rhs=[];h,z=ctx['h'],ctx['z']
    for e in (0,1):
        if (e==1 and j==0) or (e==0 and j==z):continue
        for rv,H,p,B in ctx['options'][e]:
            row=[min(p,j-e)-e*H,-e*H,H,-(rv-h),0,0];row[4+e]=-1
            rows.append(row);rhs.append(-B)
    pair=j*(z-j)+j*(j-1)//2
    obj=[0,pair,-ctx['W'],ctx['E'],z-j,j]
    limits=[(0,16*h)]*4+[(None,None)]*2
    if not penalty:limits[3]=(0,0)
    if not j:limits[5]=(0,0)
    if j==z:limits[4]=(0,0)
    res=linprog(obj,A_ub=np.asarray(rows),b_ub=np.asarray(rhs),bounds=limits,method='highs',options={'time_limit':10})
    log=dict(h=h,z=z,j=j,residual_penalty=penalty,status=int(res.status),message=res.message)
    if not res.success:return None,log
    log['objective']=float(res.fun);log['variables']=[float(x) for x in res.x]
    best=None;log['rounding_attempts']=[]
    for den in (1,2,10,100,1000):
        coef=[max(0,round(float(v)*den)) for v in res.x[:4]]
        c=evaluate(ctx,j,*coef,den);log['rounding_attempts'].append(c)
        if best is None or c['gap']*best['denominator']>best['gap']*den:best=c
        if c['gap']>0:break
    return best,log


def profile(rec,penalty=True):
    L=baseline(rec);M=sum(rec['s'])-2*rec['t'];results=[];attempts=[]
    if rec['new_minimum_residual']>M:return dict(prior_excluded=True),attempts
    new=dict(L)
    for h in range(1,max(rec['s'])+1):
        tests=[];feasible=None
        zrange=[rec['b']] if h==1 else range(L[h],rec['b']+1)
        for z in zrange:
            ctx=context(rec,L,h,z)
            if not ctx['options'][0]:
                # Larger z cannot restore the residual budget.
                tests.append(dict(z=z,existing_tail_budget_exclusion=True,E=ctx['E'],Rmax=ctx['Rmax']));continue
            cases=[]
            for j,upper in enumerate(ctx['jbounds']):
                if ctx['W']>upper:cases.append(dict(j=j,capacity_exclusion=True,upper=upper));continue
                c,log=propose(ctx,j,penalty);attempts.append(log)
                if not c or c['gap']<=0:
                    feasible=z;tests.append(dict(z=z,first_failed_j=j,best=c));break
                cases.append(c)
            else:
                tests.append(dict(z=z,cases=cases));continue
            break
        results.append(dict(h=h,baseline=L[h],new_minimum=feasible,tests=tests))
        if feasible is None:return dict(result='single_threshold_profile_exclusion',h=h,thresholds=results),attempts
        new[h]=max(new[h],feasible)
    for h in range(rec['a'],1,-1):new[h]=max(new[h],new[h+1])
    lower=rec['b']+sum(new[h] for h in range(2,rec['a']+1))
    return dict(result='joint_tail_profile_exclusion' if lower>M else 'survives_projection',minimum_residual=lower,thresholds=results),attempts


def inputs():
    all_records=read_records('profile_results.jsonl')
    pilot=json.loads((HERE.parent/'2026-09-12-joint-routing-pilot-v1/pilot_inputs.json').read_text())['sample']
    keys={(r['a'],r['b'],r['t'],tuple(r['s'])) for r in pilot}
    records=[r for r in all_records if (r['a'],r['b'],r['t'],tuple(r['s'])) in keys]
    assert len({(r['a'],r['b'],r['t'],tuple(r['s'])) for r in records})==len(records)
    return records


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--penalty',choices=['both','yes'],default='both');args=ap.parse_args()
    records=inputs();(HERE/'pilot_inputs.json').write_text(json.dumps(records,indent=2)+'\n');start=time.monotonic()
    with (HERE/'pilot_results.jsonl').open('w') as out:
        for i,rec in enumerate(records):
            row=dict(profile_id=i,a=rec['a'],b=rec['b'],t=rec['t'],s=rec['s'],modes={},attempts=[])
            for penalty in ([False,True] if args.penalty=='both' else [True]):
                result,attempts=profile(rec,penalty);row['modes']['penalty' if penalty else 'no_penalty']=result;row['attempts']+=attempts
            out.write(json.dumps(row,separators=(',',':'))+'\n');out.flush()
            print('PROFILE',i,rec['b'],rec['t'],{k:v.get('result',v) for k,v in row['modes'].items()},len(row['attempts']),round(time.monotonic()-start,2),flush=True)

if __name__=='__main__':main()
