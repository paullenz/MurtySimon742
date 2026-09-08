#!/usr/bin/env python3
"""Additional n27 audit: independently rederive all terminal source caps.
Python 3.10+, standard library; no imports from frozen verifiers.
Does not replace complete outer/column replay. Output must be a new file.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path

def need(x,detail):
    if not x:raise ValueError(detail)

def strict_ints(x):
    if type(x) is list:
        for y in x:strict_ints(y)
    else:need(type(x) is int and 0<=x<=2**31-1,'nonnegative integer expected')

def rowcheck(row,e):
    strict_ints(row);need(len(row)==7,'row length')
    state,k,r,d,rho,R,c=row
    need((len(d),len(rho),len(R),len(c))==(11,15,11,15),'dimensions')
    need(1<=k<=6 and 15<=r and d==sorted(d) and max(d)==10-k,'degree domain')
    need(sum(d)==2*(r+e-180) and max(d)<=10,'degree sum')
    need(rho==sorted(rho) and min(rho)>=1 and max(rho)<=11 and sum(rho)==r,'residual row')
    need(sum(R)==r and max(R)<=15 and max(c)<=11,'residual column')
    need(all(d[i]!=d[i-1] or R[i]>=R[i-1] for i in range(1,11)),'column symmetry')

@lru_cache(maxsize=200000)
def matching(labels,supplies):
    owners=[-1]*len(supplies)
    def extend(i,seen):
        for j,s in enumerate(supplies):
            if j in seen or labels[i]>s:continue
            seen.add(j)
            if owners[j]<0 or extend(owners[j],seen):
                owners[j]=i;return True
        return False
    return sum(extend(i,set()) for i in range(len(labels)))

@lru_cache(maxsize=100000)
def one_cap(d,rho,R,rb):
    suppliers=list(rho);suppliers.remove(rb)
    suppliers=tuple(rb+x for x in reversed(suppliers))
    feasible=[0]
    for q in range(1,12-rb):
        labels=tuple(d[i] for i in reversed(range(11)) if d[i]<=rb+R[i] and d[i]<rb+q)
        if matching(labels,suppliers)>=q:feasible.append(q)
    return max(feasible)

def caps(d,rho,R):
    ds,rs,cs=tuple(d),tuple(rho),tuple(R)
    current=[one_cap(ds,rs,cs,rb) for rb in rs]
    while True:
        nxt=[max(q for q in range(old+1) if sum(j!=i and rho[j]+current[j]>=q-1 for j in range(15))>=q) for i,old in enumerate(current)]
        need(all(x<=y for x,y in zip(nxt,current)),'nonmonotone refinement')
        if nxt==current:return current
        current=nxt

def contradiction(row):
    _,k,r,d,rho,R,c=row
    dem=[max(0,d[i]-R[i]) for i in range(11)]
    for h in range(1,max(d)+1):
        lhs=sum(dem[i] for i in range(11) if d[i]>=h)
        rhs=sum(rho[u]+rho[v]>=h for u,v in combinations(range(15),2))
        if lhs>rhs:return {'method':'pair','threshold':h,'demand':lhs,'capacity':rhs}
    E=[{b for b in range(15) if d[i]<=rho[b]+R[i] and d[i]<rho[b]+c[b]} for i in range(11)]
    if any(dem[i]>len(E[i]) for i in range(11)):return {'method':'label_capacity'}
    forced=[sum(dem[i]>0 and dem[i]==len(E[i]) and b in E[i] for i in range(11)) for b in range(15)]
    pairs=[]
    for u,v in combinations(range(15),2):
        ok=False
        for b,w in ((u,v),(v,u)):
            for i in range(11):
                qlow=max(1,forced[b],d[i]-rho[b]+1)
                if b in E[i] and d[i]<=rho[b]+rho[w] and qlow<=c[b] and qlow<=rho[w]+c[w]+1:ok=True
        if ok:pairs.append([u,v])
    need(sum(dem)>len(pairs),'unresolved final row')
    return {'method':'supplement','demand':sum(dem),'capacity':len(pairs),'forced':forced,'pairs':pairs}

def check(root):
    manifest=json.loads((root/'MANIFEST.json').read_text());present=missing=0
    for item in manifest['files']:
        p=root/item['path']
        if not p.exists():missing+=1;continue
        need(p.stat().st_size==item['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],('original hash',item['path']));present+=1
    scopes=[];digest=hashlib.sha256();finals=[]
    for e in (183,182):
        hist=Counter();seen=set();count=0
        with gzip.open(root/f'd15_{e}_survivors.jsonl.gz','rt') as f:
            for line in f:
                row=json.loads(line);rowcheck(row,e);canonical=json.dumps(row,separators=(',',':'))
                need(canonical not in seen,'duplicate original survivor');seen.add(canonical)
                rederived=caps(row[3],row[4],row[5]);need(rederived==row[6],('cap disagreement',e,row[0],row[5],row[6],rederived))
                proof=contradiction(row);hist[proof['method']]+=1;count+=1
                digest.update((json.dumps([e,row,proof],sort_keys=True,separators=(',',':'))+'\n').encode())
                if proof['method']=='supplement':finals.append({'edges':e,'row':row,'proof':proof})
        need(count==(190 if e==183 else 35245),'terminal coverage')
        scopes.append({'edges':e,'terminal_rows':count,'recomputed_source_cap_vectors':count,'dispositions':dict(hist)})
    negatives=[]
    for x in ([-1],[True],[1.0],[2**31]):
        try:strict_ints(x)
        except ValueError:negatives.append(x)
        else:raise ValueError('bad integer accepted')
    for item in finals:
        row=item['row'];d,rho,R=row[3:6];perm=list(reversed(range(11)))
        c2=caps([d[i] for i in perm],list(reversed(rho)),[R[i] for i in perm])
        need(c2==list(reversed(row[6])),'permutation invariance')
    return {'status':'PASS','input_manifest_present_files':present,'input_manifest_omitted_files':missing,'scopes':scopes,'ordered_audit_sha256':digest.hexdigest(),'final_four':finals,'strict_integer_negative_controls':negatives,'source_cap_algorithm':'augmenting paths plus synchronous fixed point','full_outer_or_column_replay_in_this_program':False,'external_independent_authorship':False}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();need(not a.output.exists(),'output exists');result=check(a.root)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='final_four'},indent=2))
if __name__=='__main__':main()
