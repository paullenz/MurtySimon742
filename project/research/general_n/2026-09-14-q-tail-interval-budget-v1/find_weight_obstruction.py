from pathlib import Path
import json,sys
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction
from explore_thresholds import profiles
ROOT=Path(__file__).parent
K=max(max(p['q']) for p in profiles)
D=np.array([[next((r['exact'] for r in p['rows'] if r['tau']==tau),0) for tau in range(1,K+1)] for p in profiles],dtype=int)
sol=linprog(np.zeros(len(profiles)),A_ub=D.T,b_ub=np.zeros(K),A_eq=np.ones((1,len(profiles))),b_eq=[1],bounds=(0,None),method='highs')
print('feasible',sol.success)
if not sol.success: raise SystemExit('No numerical obstruction found; no conclusion')
ids=np.where(sol.x>1e-8)[0];weights=[Fraction(float(sol.x[i])).limit_denominator(1000000) for i in ids]
from functools import reduce
from math import lcm,gcd
scale=lcm(*(x.denominator for x in weights));ints=[int(x*scale) for x in weights];g=reduce(gcd,ints);ints=[x//g for x in ints]
combo=[sum(ints[j]*int(D[i,tau]) for j,i in enumerate(ids)) for tau in range(K)]
assert all(x<=0 for x in combo)
examples=[]
for i,weight in zip(ids,ints):
 p=profiles[i]; examples.append(dict(index=int(i),state=p['state'],weight=weight,a=p['a'],b=p['b'],t=p['t'],D0=p['D0'],Esel=p['Esel'],q=p['q'],rho=p['rho'],P=p['P'],s=p['s'],deficiencies=D[i].tolist()))
result=dict(status='EXACT_INTEGER_CERTIFICATE',K=K,profiles=examples,weighted_sum_deficiencies=combo,total_weight=sum(ints),
 interpretation='No single nonnegative threshold-weight vector gives strictly positive pressure on every frozen difficult profile. Adaptive profile-dependent weights remain possible.')
(ROOT/'FIXED_WEIGHT_OBSTRUCTION_DISCOVERED.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2))
