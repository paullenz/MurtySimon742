#!/usr/bin/env python3
"""python test_closure.py OUT integer|rational|focused|sample"""
from collections import Counter,deque
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import random
import sys
import test_forced as prev
import verify_closure as v
old=prev.old


def maxflow(cap,s,t):
    N=len(cap);r=[row[:] for row in cap];value=0
    while True:
        back={s:None};queue=deque([s])
        while queue and t not in back:
            u=queue.popleft()
            for w in range(N):
                if r[u][w]>0 and w not in back:back[w]=u;queue.append(w)
        if t not in back:break
        vals=[];w=t
        while w!=s:u=back[w];vals.append(r[u][w]);w=u
        f=min(vals);value+=f;w=t
        while w!=s:u=back[w];r[u][w]-=f;r[w][u]+=f;w=u
    # Net antiparallel flow can be represented using only its positive direction.
    flow=[[u,w,cap[u][w]-r[u][w]] for u in range(N) for w in range(N) if cap[u][w]>r[u][w]]
    return value,flow


def auxiliary(o,m,a,x,y):
    """Independent construction from producer's residual shortest-path records."""
    n=o['n'];N=2*n+4;s,t=N-2,N-1;cap=[[0]*N for _ in range(N)]
    for u,ps in enumerate(o['paths']):
        for w,path in ps.items():
            if len(path)==2:cap[u][w]=n+1
    cap[s][2*n]=n+1;cap[s][a]=n+1
    cap[2*n+1][t]=n+1
    for u in range(n):
        if not m>>u&1:cap[u][t]=n+1
    negative=0
    for u in range(n):
        low=(u,x) in o['arcs'];high=(u,y) in o['arcs']
        if low and not high:cap[u][t]+=1
        if high and not low:cap[s][u]+=1;negative+=1
    value,flow=maxflow(cap,s,t)
    return value-negative,flow


def moves(c,o,m,counts):
    n=o['n'];E=o['arcs'];sc=o['scale'];yy=o['rows'][m]['counts'];ans=[]
    forced_core=set(o['paths'][2*n])&set(range(n))
    for a in range(n):
        if not m>>a&1 or a in forced_core:continue
        forced=forced_core|({u for u in o['paths'][a] if u<n})
        anchored=[t for t in o['minima'] if t&~m==0 and t>>a&1]
        least=(1<<n)-1
        for t in anchored:least&=t
        assert least==sum(1<<u for u in forced)
        for bs in c['blocks']:
            for x in bs:
                q=sum((u,x) in E for u in forced)
                if q*sc<=o['p'][x]:continue
                for y in bs:
                    if not o['p'][x]<o['p'][y] or yy[y]*sc>=o['p'][y]:continue
                    exact=min(o['rows'][t]['counts'][x]-o['rows'][t]['counts'][y] for t in anchored)
                    delta,flow=auxiliary(o,m,a,x,y)
                    assert delta==exact,('signed optimization mismatch',c,m,a,x,y,delta,exact)
                    counts['signed_optimizations_checked']+=1
                    if delta>=1:ans.append(dict(anchor=a,x=x,y=y,difference_flow=flow))
    return ans


def explore(c,o,counts):
    inst=v.parse_instance(c);S,gamma,f,adj=v.flow_start(c,inst)
    assert gamma==Q(o['gamma'],o['scale'])
    todo=[(o['M'],[])];seen=set();terminals=[];certs=[]
    while todo:
        m,path=todo.pop()
        if m in seen:continue
        seen.add(m);ms=moves(c,o,m,counts);counts['states']+=1;counts['witness_transitions']+=len(ms)
        if not ms:
            terminals.append(m)
            if m in o['tight']:
                cert=deepcopy(c);cert.update(deletions=path,terminal=[u for u in range(o['n']) if m>>u&1])
                result=v.verify(cert);assert m==o['greatest'];certs.append(cert)
            continue
        for step in ms:
            a=step['anchor'];pred=sum(1<<u for u in range(o['n']) if a in o['paths'][u])
            after=m&~pred;assert after in o['minima']
            for t in o['minima']:
                if t&~m or not t>>a&1:continue
                T={u for u in range(o['n']) if t>>u&1}
                new,trace=v.closure_step(inst,T,gamma,adj,step)
                assert sum(1<<u for u in new)==t&~pred and t not in o['tight']
                counts['same_flow_persistence_checks']+=1
            if (m&pred).bit_count()>1:counts['multiple_source_removals']+=1
            todo.append((after,path+[step]))
    assert len(terminals)==1,('nonconfluence',c,terminals)
    counts['accepted']+=bool(certs);counts['nonempty']+=bool(certs and certs[0]['deletions'])
    counts['missing_greatest']+=bool(o['greatest'] is not None and not certs)
    return dict(terminal=terminals[0],accepted=bool(certs),certificate=certs[0] if certs else None)


def run_case(c,counts,fullcuts=False):
    o=old.prepare(c,fullcuts);r={};c3=deepcopy(c);c3['version']=3;cs=Counter()
    r['v3_block']=prev.explore(c3,o,'block',cs);counts.update({'v3_'+k:z for k,z in cs.items()})
    r['closure']=explore(c,o,counts)
    assert not r['closure']['terminal']&~r['v3_block']['terminal']
    assert not r['v3_block']['accepted'] or r['closure']['accepted']
    counts['instances']+=1;counts['source_subsets']+=1<<o['n']
    if fullcuts:counts['complete_cuts']+=1<<(2*o['n'])
    return o,r


def make(n,bs,p,d,E):
    c=prev.make(n,bs,p,d,E);c['version']=4;c.pop('rule');return c


def exhaustive(out,mode):
    vals=[0,1,2] if mode=='integer' else [0,Q(1,2),1]
    counts=Counter();examples={};digest=sha256();slots=[(u,w) for u in range(3) for w in range(3) if u!=w]
    for bits in range(64):
        E=[e for k,e in enumerate(slots) if bits>>k&1]
        for p in product(vals,repeat=3):
            for d in product(vals,repeat=3):
                c=make(3,[[0,1,2]],p,d,E);o,r=run_case(c,counts)
                if r['closure']['accepted'] and not r['v3_block']['accepted']:
                    counts['gain']+=1;examples.setdefault('gain',old.record(c,o,r))
                if o['greatest'] is not None and not r['closure']['accepted']:
                    examples.setdefault('incomplete',old.record(c,o,r))
                digest.update((json.dumps([bits,p,d,o['gamma'],o['greatest'],{k:z['terminal'] for k,z in r.items()}],
                             default=old.encode,separators=(',',':'))+'\n').encode())
        if bits%16==15:print('closure',mode,bits+1,'supports',flush=True)
    assert counts['instances']==46656
    assert counts['v3_block_accepted']==(33657 if mode=='integer' else 32556)
    old.write(out/('CLOSURE_'+mode.upper()+'.json'),dict(regime=mode,counts=dict(counts),examples=examples,
       ordered_record_sha256=digest.hexdigest(),discrepancies=0,overlap=4096))
    print(dict(counts),flush=True)


def focused(out):
    E=[(0,1),(1,0),(2,0)];cases=[
      ('mandatory_compensation',3,[[0,1,2]],[0,2,0],[1,0,1],E),
      ('forced_count_predecessor',3,[[0,1,2]],[1,0,1],[1,0,0],[(0,1),(0,2),(1,2)]),
      ('scc_predecessor',3,[[0,1,2]],[Q(1,2),0,1],[Q(1,2),Q(1,2),0],[(0,1),(0,2),(1,2)]),
      ('three_compensations',9,[list(range(3*i,3*i+3)) for i in range(3)],[0,2,0]*3,[1,0,1]*3,
       [(3*i+a,3*i+b) for i in range(3) for a,b in E])]
    counts=Counter();examples={}
    for name,n,bs,p,d,arcs in cases:
        c=make(n,bs,p,d,arcs);o,r=run_case(c,counts,n<=3);examples[name]=old.record(c,o,r)
        assert r['closure']['accepted']
        if name=='mandatory_compensation':
            assert not r['v3_block']['accepted'] and o['greatest']==5
            old.write(out/'CLOSURE_DEMO.json',r['closure']['certificate'])
            old.write(out/'CLOSURE_DEMO_RESULT.json',v.verify(r['closure']['certificate']))
        if name=='three_compensations':
            cc=Counter();explore(c,o,cc);assert cc['states']==8 and cc['witness_transitions']==12
    base=examples['mandatory_compensation']['results']['closure']['certificate'];bad=[]
    def add(name,f):
        c=deepcopy(base);f(c);bad.append((name,c))
    add('missing_aux_flow',lambda c:c['deletions'][0].pop('difference_flow'))
    add('insufficient_aux_value',lambda c:c['deletions'][0].update(difference_flow=[]))
    add('aux_overload',lambda c:c['deletions'][0]['difference_flow'][0].__setitem__(2,999))
    add('aux_bool',lambda c:c['deletions'][0]['difference_flow'][0].__setitem__(2,True))
    add('aux_float',lambda c:c['deletions'][0]['difference_flow'][0].__setitem__(2,1.0))
    add('aux_conservation',lambda c:c['deletions'][0]['difference_flow'].pop())
    add('aux_duplicate',lambda c:c['deletions'][0]['difference_flow'].append(c['deletions'][0]['difference_flow'][0]))
    add('mandatory_anchor',lambda c:c['deletions'][0].update(anchor=2))
    add('wrong_pair',lambda c:c['deletions'][0].update(x=1,y=0))
    rejected=[]
    for name,c in bad:
        try:v.verify(c)
        except v.Invalid as e:rejected.append(dict(case=name,certificate=c,reason=str(e)))
        else:raise AssertionError(('corruption accepted',name))
    old.write(out/'CLOSURE_FOCUSED.json',dict(counts=dict(counts),examples=examples,rejections=rejected))
    print(dict(counts),'rejections',len(rejected),flush=True)


def sample(out):
    rng=random.Random(74220260927);vals=[0,Q(1,2),1,Q(3,2),2,3];counts=Counter();examples={};digest=sha256()
    for i in range(500):
        n=4+i%3;bs=[list(range(n))] if i%2==0 else [list(range(n//2)),list(range(n//2,n))]
        c=make(n,bs,[rng.choice(vals) for _ in range(n)],[rng.choice(vals) for _ in range(n)],
          [(a,b) for a in range(n) for b in range(n) if a!=b and rng.random()<.4])
        o,r=run_case(c,counts,i<30)
        if r['closure']['accepted'] and not r['v3_block']['accepted']:
            counts['gain']+=1;examples.setdefault('gain',old.record(c,o,r))
        if o['greatest'] is not None and not r['closure']['accepted']:
            examples.setdefault('incomplete',old.record(c,o,r))
        digest.update((json.dumps([c,{k:z['terminal'] for k,z in r.items()}],sort_keys=True)+'\n').encode())
    assert counts['v3_block_accepted']==200
    old.write(out/'CLOSURE_SAMPLE.json',dict(seed=74220260927,counts=dict(counts),examples=examples,
       ordered_record_sha256=digest.hexdigest(),discrepancies=0))
    print(dict(counts),flush=True)


if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit(__doc__)
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);mode=sys.argv[2]
    if mode in ('integer','rational'):exhaustive(out,mode)
    elif mode=='focused':focused(out)
    elif mode=='sample':sample(out)
    else:raise SystemExit(__doc__)
