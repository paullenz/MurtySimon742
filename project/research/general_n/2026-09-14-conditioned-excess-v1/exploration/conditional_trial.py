import json,time
import verify_block_pressure as b
import verify_capped_spill as c

def condcaps(s,q,rho,P,eta,eL):
 low,SL,forced=c.spill_data(s,q,rho,eta);M=sum(forced);E=sum(q)-sum(s)
 J=eL+SL-M
 if J<0 or eL<0 or eL>E:return None
 out=list(P)
 for u,(qq,r) in enumerate(zip(q,rho)):
  k=min(qq,sum(d<=min(eta,r) for d in s),forced[u]+J)
  if qq>k:out[u]=min(out[u],r-1+(E-eL)//(qq-k))
 return out

def cond_dp(s,q,rho,P,eta,eL,chargeeta,alpha):
 ss,E,lim,fl=b.projection(s,q,rho);idx=sum(d<=eta for d in ss)
 if E<0 or min(lim)<0:return None
 table=b.scores(ss,q,rho,P,chargeeta,alpha,E,lim);best={0:0}
 for i,(h,row) in enumerate(zip(lim,table),1):
  nxt={}
  for used,value in best.items():
   for e in range(min(h,E-used)+1):
    t=used+e
    if t<fl.get(i,0) or (i==idx and t!=eL) or (i<idx and t>eL):continue
    nxt[t]=max(nxt.get(t,-1),value+row[e])
  best=nxt
 return best.get(E)

def run():
 rows=json.load(open('REMAINDER_12.json'))['rows'];outputs=[]
 for p in rows:
  s,q,rho=p['s'],p['q'],p['rho'];P=c.spill_caps(s,q,rho,c.prior_localized(s,q,rho,c.old_caps(p['a'],s,q,rho)));E=p['Esel'];w=0;report=[]
  for eta in sorted(set(s))[:-1]:
   passed=[];evidence=[]
   M=sum(c.spill_data(s,q,rho,eta)[2]);SL=sum(d for d in s if d<=eta)
   for eL in range(max(0,M-SL),E+1):
    pc=condcaps(s,q,rho,P,eta,eL)
    if pc is None:continue
    if sum(pc)<sum(q):evidence.append(dict(eL=eL,reason='sum_cap',gap=sum(q)-sum(pc)));continue
    best=None
    for ce in sorted({0,eta}):
     for alpha in ([1]*len(q),[1 if qq<=2 else 3 for qq in q]):
      upper=cond_dp(s,q,rho,pc,eta,eL,ce,alpha)
      if upper is None:best=dict(eL=eL,reason='empty');break
      low=b.best_lower(q,rho,s,pc,ce,alpha);gap=low['lower']-upper
      if best is None or gap>best.get('gap',-999999):best=dict(eL=eL,reason='price',upper=upper,lower=low['lower'],gap=gap,charge_eta=ce,weighted=alpha!=[1]*len(q),tau=low['tau'],theta=low['theta'])
      if gap>0:break
     if best['reason']=='empty' or best.get('gap',0)>0:break
    if best['reason']!='empty' and best.get('gap',0)<=0:passed.append(eL)
    evidence.append(best)
   report.append(dict(eta=eta,not_rejected_eL=passed,evidence=evidence))
   if not passed:break
  rec=dict(row=p['row'],excluded=not report[-1]['not_rejected_eL'],report=report);outputs.append(rec)
  print('row',p['row'],'excluded',rec['excluded'],[(t['eta'],t['not_rejected_eL']) for t in report],flush=True)
  json.dump(outputs,open('conditional_trial.json','w'),indent=2)
if __name__=='__main__':run()
