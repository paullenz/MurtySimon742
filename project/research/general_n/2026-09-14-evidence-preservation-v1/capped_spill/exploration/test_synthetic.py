import csv,json,time
from collections import Counter
import spill_math as m
from pathlib import Path
rows=list(csv.DictReader(open('/mnt/data/work/q-stratified-receiver-reach-pilot/SYNTHETIC_INTERVAL_PROFILES.tsv'),delimiter='\t'))
C=Counter();survivors=[];newex=[]
for j,raw in enumerate(rows):
 p={k:([int(x) for x in v.split(',')] if k in ('q','rho','s','P') else int(v)) for k,v in raw.items()}
 q,rho,s=[p[k] for k in ('q','rho','s')];P=p['P'];L=m.old.localized(s,q,rho,P);new,tr=m.spill(s,q,rho,L)
 E=p['Esel'];env=m.envelope(s,q,rho)
 oldscore=m.priced(q,rho,s,L)[0];midscore=m.priced(q,rho,s,new)[0];score=m.priced(q,rho,s,new,env)
 C['profiles']+=1;C['old_rejected']+=oldscore>0;C['spill_rejected']+=midscore>0;C['new_rejected']+=score[0]>0;C['unrejected']+=score[0]<=0;C['cap_stricter']+=new!=L
 C['envelope_stricter']+=env<E*(E+max(s))
 if oldscore<=0 and score[0]>0:
  p.update(row=j,oldcap=L,newcap=new,new_envelope=env,old_envelope=E*(E+max(s)),score=score,trace=tr)
  newex.append(p)
 if score[0]<=0:survivors.append(dict(p,row=j,newcap=new,new_envelope=env,score=score))
print(C)
print('new sample',json.dumps(newex[:2],indent=2))
print('unrejected sample',json.dumps(survivors[:1],indent=2))
Path('/mnt/data/work/spill/synthetic_results.json').write_text(json.dumps(dict(counts=dict(C),newly_rejected=newex,survivors=survivors),indent=2))
