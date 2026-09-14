import baseline as old
from collections import Counter
from pathlib import Path
import json

def spill(s,q,rho,P):
    E=sum(q)-sum(s); out=list(P); trace=[]
    # All changes of the eligible label block: no rho breakpoint needed.
    for eta in sorted({0,*s}):
        low=[i for i,d in enumerate(s) if d<=eta]; SL=sum(s[i] for i in low)
        forced=[max(0,qq-sum(eta<d<=r for d in s)) for qq,r in zip(q,rho)]
        M=sum(forced)
        if M>SL+E:raise ValueError('spill infeasible')
        for w,(qq,r) in enumerate(zip(q,rho)):
            if qq==0:continue
            eligible=sum(d<=min(eta,r) for d in s)
            C=E+SL-M+forced[w]
            k=min(qq,eligible,C)
            if qq>k:
                cap=r-1+(C-k)//(qq-k)
                if cap<out[w]:trace.append((w,eta,cap,C,forced[w],M,SL));out[w]=cap
    return out,trace

# Exact separable upper envelope with necessary column eligibility and prefix bounds.
# Each candidate e vector may still fail the incidence matching: an upper bound only.
def envelope(s,q,rho):
    E=sum(q)-sum(s)
    cols=sorted(s)
    h=[sum(qq>0 and r>=d for qq,r in zip(q,rho))-d for d in cols]
    if min(h)<0:return None
    dp={0:0}; lower={}
    for d in set(cols):
        upto=sum(x<=d for x in cols)
        spilltot=sum(max(0,qq-sum(d<x<=r for x in cols)) for qq,r in zip(q,rho))
        lower[upto]=max(0,spilltot-sum(x for x in cols if x<=d))
    for i,(d,hi) in enumerate(zip(cols,h),1):
        nxt={}
        for total,cost in dp.items():
            for e in range(min(hi,E-total)+1):
                v=cost+e*(d+e); ee=total+e
                if ee>=lower.get(i,0) and v>nxt.get(ee,-1):nxt[ee]=v
        dp=nxt
    return dp.get(E)

def priced(q,rho,s,P,env=None):
    E=sum(q)-sum(s);z=s.count(0);c=[qq+r for qq,r in zip(q,rho)];v=[max(0,qq-z) for qq in q]
    if env is None:env=E*(E+max(s))
    best=(-10**9,None)
    for tau in range(1,max(q)+1):
        A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 for u in range(len(q)))) for w in range(len(q))]
        demand=sum(qq for qq in q if qq>=tau)
        f=[min(a,r-1) for a,r in zip(A,rho)];g=[a-b for a,b in zip(A,f)]
        for theta in {0,*v,env+max(v)+1}:
            score=theta*(demand-sum(f))-sum(max(0,theta-vv)*gg for vv,gg in zip(v,g))-env
            if score>best[0]:best=(score,(tau,theta,demand,sum(A)))
    return best

example=dict(a=24,b=27,t=2,D0=0,Esel=34,z=2,q=[7,2,2,2,2,2,2,6,3,4,5,2,3,8,6,2,2,6,2,3,6,4,6,2,4,1,2],rho=[3,1,1,1,1,1,1,4,4,3,3,1,4,3,4,1,1,2,1,2,3,3,3,1,3,2,1],s=[0,0,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
q,rho,s=[example[x] for x in ('q','rho','s')]
P=old.old_caps(example['a'],s,q,rho);L=old.localized(s,q,rho,P);new,tr=spill(s,q,rho,L);env=envelope(s,q,rho)
print('example E',sum(q)-sum(s),'old sum',sum(L),'new sum',sum(new),'Q',sum(q),'trace',tr,'oldenv',34*37,'newenv',env,'price',priced(q,rho,s,new,env))

root=Path('/mnt/data/work');pilot=next(root.rglob('Q_STRATIFIED_RECEIVER_REACH_PILOT_INPUT.txt'));exc=next(root.rglob('LAYER_EXCEPTION_DIAGNOSTIC.tsv'))
states={}
for line in pilot.read_text().splitlines()[1:]:
 v=list(map(int,line.split()));layer,i,a,b,t,ns=v[:6];states[i]=dict(a=a,b=b,t=t,s=v[6:6+ns],rho=v[7+ns:])
C=Counter();examples=[]
for row,line in enumerate(exc.read_text().splitlines()):
 fields=dict(x.split('=',1) for x in line.split('\t')[1:]);st=states[int(fields['state'])]
 q=[];rho=[];P=[]
 for item in fields['types'].split(';'):
  qq,c,p,n,*_=map(int,item.split(','));q +=[qq]*n;rho +=[c-qq]*n;P +=[p]*n
 s=st['s'];L=old.localized(s,q,rho,P);new,tr=spill(s,q,rho,L);E=sum(q)-sum(s)
 C['profiles']+=1;C['tighter']+=new!=L
 if new!=L and len(examples)<3:examples.append(dict(row=row,state=int(fields['state']),q=q,rho=rho,s=s,old=L,new=new,trace=tr))
 tt=old.tails(st['a'],q,rho,new)
 C['sumP']+=sum(new)<sum(q);C['tau1']+=tt[0]['deficiency']>0;C['uniform']+=sum(t['deficiency'] for t in tt)>0
 C['tau3']+=tt[2]['deficiency']>0
 en=envelope(s,q,rho);C['envelope_stricter']+=en<E*(E+max(s));C['envelope_improvement']+=E*(E+max(s))-en
print(C);print(json.dumps(examples,indent=2))
