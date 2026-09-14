import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'lib'))
import prior,block
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'remainder12.json').read_text())['rows']
old=json.loads((ROOT/'conditioned_full.json').read_text())
prior_reports={p['row']:p for p in old['replay']['reports']}

def baseline(p):
 s,q,r=p['s'],p['q'],p['rho']
 return prior.spill_caps(s,q,r,prior.prior_localized(s,q,r,prior.old_caps(p['a'],s,q,r)))

def branch_data(p,eta,e):
 s,q,r=p['s'],p['q'],p['rho'];E=p['Esel'];P=baseline(p)
 f=[max(0,qq-sum(eta<d<=rr for d in s)) for qq,rr in zip(q,r)]
 m=[sum(d<=min(eta,rr) for d in s) for rr in r]
 J=sum(d for d in s if d<=eta)+e-sum(f);H=E-e
 if J<0:return None
 D=[max(0,pp-rr+1) for pp,rr in zip(P,r)]
 options=[]
 for u in range(len(q)):
  oo=[]
  for d in range(D[u]+1):
   k=max(f[u],q[u]-H//d) if d else f[u]
   if k<=m[u]:oo.append((d,k-f[u]))
  options.append(oo)
 return J,options

def dp_tail(p,J,options,tau):
 q,r=p['q'],p['rho'];P=baseline(p);c=[qq+rr for qq,rr in zip(q,r)];n=len(q)
 A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 for u in range(n))) for w in range(n)]
 free=[min(aa,rr-1) for aa,rr in zip(A,r)]
 limits=[aa-ff for aa,ff in zip(A,free)]
 dp={0:0}
 for lim,oo in zip(limits,options):
  nd={}
  for used,score in dp.items():
   for d,cost in oo:
    if d>lim or used+cost>J:continue
    nd[used+cost]=max(nd.get(used+cost,-1),score+d)
  dp=nd
 bound=sum(free)+max(dp.values(),default=-10**6)
 demand=sum(qq for qq in q if qq>=tau)
 return {'tau':tau,'capacity':bound,'demand':demand,'gap':demand-bound}

if __name__=='__main__':
 reports=[]
 for p in rows:
  pr=prior_reports[p['row']];sp=[]
  for old_split in pr['splits']:
   eta=old_split['eta'];un=[];new=[]
   for e in old_split['unrejected_e_low']:
    data=branch_data(p,eta,e)
    best=max((dp_tail(p,*data,tau) for tau in range(1,max(p['q'])+1)),key=lambda d:d['gap'])
    if best['gap']>0:new.append(dict(e=e,**best))
    else:un.append(e)
   sp.append(dict(eta=eta,new=new,remaining=un))
  reports.append(dict(row=p['row'],splits=sp))
  print(p['row'],[(s['eta'],len(s['new']),s['remaining']) for s in sp],flush=True)
 (ROOT/'slack_trial.json').write_text(json.dumps(reports,indent=2))
