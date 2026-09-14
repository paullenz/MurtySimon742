"""Numerical discovery only: all bound evaluations use scaled integers."""
import json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
from scipy.optimize import linprog
from source_price_core import envelope,receiver_lower
SCALE=100
rows=json.load(open(HERE/'inputs.json'))['rows']
row=rows[int(sys.argv[1])]
results=[]
for mode in [0,1]:
 for xi in sorted(set([0,min(v for v in row['s'] if v>0)])):
  alpha=[SCALE*(1 if mode==0 or v<=2 else 3) for v in row['q']]
  lower=receiver_lower(row,alpha,xi)
  b=len(row['q']); q=row['q']; price=[0]*b
  types=sorted(set(zip(q,row['rho'],row['P'],alpha)))
  group=[types.index(t) for t in zip(q,row['rho'],row['P'],alpha)]
  k=len(types)
  constraints=[];rhs=[];seen=set(); trace=[];best=None
  for iteration in range(120):
   e=envelope(row,alpha,price,xi)
   if e is None: raise RuntimeError('empty domain: investigate')
   U=e['upper']
   record={'iteration':iteration,'price':price,'upper':U,'source_use':e['source_use']}
   trace.append(record)
   if best is None or U<best['upper']: best=dict(record)
   gradient=[q[u]-e['source_use'][u] for u in range(b)]
   base=U-sum(gradient[u]*price[u] for u in range(b))
   cut=tuple(gradient+[base])
   if cut in seen: break
   seen.add(cut)
   gg=[sum(gradient[u] for u in range(b) if group[u]==g) for g in range(k)]
   constraints.append(gg+[-1]);rhs.append(-base)
   res=linprog([0]*k+[1],A_ub=constraints,b_ub=rhs,
               bounds=[(-20*SCALE,20*SCALE)]*k+[(None,None)],method='highs')
   if not res.success: break
   price=[int(round(res.x[group[u]])) for u in range(b)]
  rec={'row':row['row'],'scale':SCALE,'mode':mode,'xi':xi,'alpha':alpha,
       'lower':lower,'zero_upper':trace[0]['upper'],'best':best,'trace':trace}
  results.append(rec)
  print(row['row'],mode,xi,'lower',lower['lower']/SCALE,'zero',trace[0]['upper']/SCALE,
        'best',best['upper']/SCALE,'iterations',len(trace),flush=True)
json.dump({'scope':'type-constant numerical discovery, 120 iterations, original six retained profiles; finite price search only','results':results},
          open(HERE/('prices_'+str(row['row'])+'.json'),'w'),indent=2)
