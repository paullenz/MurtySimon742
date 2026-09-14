from pathlib import Path
import argparse,sys,json,csv,hashlib
from collections import Counter
import verify_shared_slack as new
ROOT=Path(__file__).parent
# Prior mathematical routines are supplied explicitly; no session-local paths.
prior=None
block=None

def conditioned_upper(s,q,rho,P,eta,e_low,ce,alpha):
 ss,E,lim,floor=block.projection(s,q,rho);nlow=sum(d<=eta for d in ss)
 if E<0 or min(lim,default=0)<0:return None
 if nlow==0 and e_low!=0:return None
 score=block.scores(ss,q,rho,P,ce,alpha,E,lim);dp={0:0}
 for i,(h,sc) in enumerate(zip(lim,score),1):
  nd={}
  for used,val in dp.items():
   for e in range(min(h,E-used)+1):
    total=used+e
    if total<floor.get(i,0) or (i<nlow and total>e_low) or (i==nlow and total!=e_low):continue
    nd[total]=max(nd.get(total,-1),val+sc[e])
  dp=nd
 return dp.get(E)

def conditional_scan(p,P):
 s,q,r=p['s'],p['q'],p['rho'];E=p['Esel'];old_ex=False;new_ex=False;tested=0;newproof=None
 for eta in sorted(set(s))[:-1]:
  low={i for i,d in enumerate(s) if d<=eta};SL=sum(s[i] for i in low)
  M=sum(max(0,qq-sum(eta<d<=rr for d in s)) for qq,rr in zip(q,r))
  old_un=[];new_un=[];records=[]
  for e_low in range(max(0,M-SL),E+1):
   data=new.block_options(s,q,r,P,low,e_low);tested+=1
   if data is None:records.append(dict(e_low=e_low,reason='empty_block'));continue
   J,oo=data;pc=[min(pp,rr-1+max(d for d,cost in op if cost<=J)) for pp,rr,op in zip(P,r,oo)]
   if sum(pc)<sum(q):records.append(dict(e_low=e_low,reason='cap'));continue
   ok=False
   for ce in sorted({0,eta}):
    for alpha in ([1]*len(q),[1 if qq<=2 else 3 for qq in q]):
     up=conditioned_upper(s,q,r,pc,eta,e_low,ce,alpha)
     lc=block.best_lower(q,r,s,pc,ce,alpha)
     if up is None or lc['lower']>up:ok=True;break
    if ok:break
   if ok:records.append(dict(e_low=e_low,reason='conditioned_price'));continue
   old_un.append(e_low)
   cert=new.best_shared(q,r,P,J,oo)
   if cert['kind']!='shared_slack' or cert['gap']>0:records.append(dict(e_low=e_low,reason='shared_slack',certificate=cert))
   else:new_un.append(e_low)
  old_ex|=not old_un;new_ex|=not new_un
  if not new_un and newproof is None:newproof=dict(eta=eta,range=[max(0,M-SL),E],branches=records)
  if old_ex:break
 return old_ex,new_ex,tested,newproof

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--synthetic',required=True,type=Path);ap.add_argument('--prior',required=True,type=Path);ap.add_argument('--block',required=True,type=Path);args=ap.parse_args()
 prior=new.load_module(args.prior,'fresh_prior');block=new.load_module(args.block,'fresh_block')
 source=args.synthetic
 assert hashlib.sha256(source.read_bytes()).hexdigest()=='f0e32e99a66d51027d1ad89d9f3874a8d50b3d4d215e8e1dd0d816786504dc2e'
 ct=Counter();un=[];certs=[]
 for row,raw in enumerate(csv.DictReader(source.open(),delimiter='\t')):
  p={k:([int(x) for x in v.split(',')] if k in ('s','q','rho','P') else int(v)) for k,v in raw.items()};p['row']=row
  s,q,r=p['s'],p['q'],p['rho'];ct['profiles']+=1
  P=new.baseline(p,prior)
  old=prior.priced_lower(q,r,s,P);env=prior.envelope(s,q,r,p['b']-p['a'])
  if env is None or prior.rejected(old,env):ct['capped_rejected']+=1;continue
  found=False
  for alpha in ([1]*len(q),[1 if qq<=2 else 3 for qq in q]):
   for eta in sorted({0,*s}):
    if eta>=max(s):continue
    up=block.dp_upper(s,q,r,P,eta,alpha);lo=block.best_lower(q,r,s,P,eta,alpha)
    if up is None or lo['lower']>up:found=True;break
   if found:break
  if found:ct['additional_block_rejected']+=1;continue
  a,b,trials,proof=conditional_scan(p,P);ct['conditional_splits_tested']+=trials
  if a:ct['additional_conditioned_rejected']+=1
  elif b:ct['additional_shared_rejected']+=1;certs.append(dict(profile=p,certificate=proof))
  else:un.append(p);ct['unrejected']+=1
  print('row',row,dict(ct),file=sys.stderr,flush=True)
 out=dict(schema='fresh-shared-slack-reconnaissance-v1',seed=74220260919,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
          counts=dict(ct),new_shared_certificates=certs,unrejected=un,
          scope='new seed, same explicit scalar/incidence/pair-flow generator; not independent generation or realized graphs')
 assert [x['profile']['row'] for x in certs]==[163,362,687]
 assert [x['row'] for x in un]==[20,91,391,490,528,562,677]
 print(json.dumps(out,sort_keys=True,indent=2))
