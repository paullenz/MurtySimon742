import csv,json
from collections import Counter
import spill_math as m
C=Counter();extra=[]
for j,raw in enumerate(csv.DictReader(open('/mnt/data/work/q-stratified-receiver-reach-pilot/SYNTHETIC_INTERVAL_PROFILES.tsv'),delimiter='\t')):
 p={k:([int(x) for x in v.split(',')] if k in ('q','rho','s','P') else int(v)) for k,v in raw.items()};s,q,rho=p['s'],p['q'],p['rho'];E=p['Esel'];delta=p['b']-p['a'];z=s.count(0)
 L=m.old.localized(s,q,rho,p['P']);new,tr=m.spill(s,q,rho,L)
 M0=sum(max(0,qq-sum(0<d<=r for d in s)) for qq,r in zip(q,rho));ep=E-M0
 simple=ep*(max(s)+min(ep,delta));dp=m.envelope(s,q,rho,delta)
 ol=m.priced(q,rho,s,L)[0]>0;ns=m.priced(q,rho,s,new)[0]>0
 ls=m.priced(q,rho,s,L,simple)[0]>0;ss=m.priced(q,rho,s,new,simple)[0]>0;dd=m.priced(q,rho,s,new,dp)[0]>0
 for key,v in [('profiles',1),('old',ol),('spill',ns),('old_caps_simple',ls),('spill_simple',ss),('spill_dp',dd)]:C[key]+=v
 if dd and not ss:extra.append(dict(row=j,s=s,q=q,rho=rho,E=E,delta=delta,simple=simple,dp=dp,price=m.priced(q,rho,s,new,dp)))
print(C);print(extra)
