#!/usr/bin/env python3
"""Independent scaled-integer oracle, flow producer and deletion-predicate audit.
python test_residual.py OUT integer|rational|focused|sample
"""
from collections import Counter, deque
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from math import lcm
from pathlib import Path
import json
import random
import sys
import verify_residual as v


def encode(x):
    if isinstance(x,Q): return x.numerator if x.denominator==1 else str(x)
    raise TypeError(type(x).__name__)


def write(p,data):
    p.write_text(json.dumps(data,indent=2,sort_keys=True,default=encode)+'\n')


def wire(x): return json.loads(json.dumps(x,default=encode))


def instance(n,blocks,p,d,arcs):
    return wire(dict(version=2,rule='path',n=n,blocks=blocks,capacities=p,demands=d,
                     arcs=sorted(arcs),flow=[],deletions=[],terminal=[]))


def prepare(c, fullcuts=False):
    n=c['n']; arcs={tuple(a) for a in c['arcs']}; N=2*n+2; s,t=N-2,N-1
    scale=lcm(*(Q(q).denominator for q in c['capacities']+c['demands']))
    p=[int(Q(q)*scale) for q in c['capacities']]
    d=[int(Q(q)*scale) for q in c['demands']]
    cap=[[0]*N for _ in range(N)]
    for i in range(n): cap[s][i]=d[i]; cap[n+i][t]=p[i]
    for i,j in arcs: cap[i][n+j]=scale
    res=[row[:] for row in cap]
    while True:
        prev={s:None}; todo=deque([s])
        while todo and t not in prev:
            i=todo.popleft()
            for j in range(N):
                if res[i][j]>0 and j not in prev: prev[j]=i; todo.append(j)
        if t not in prev: break
        j=t; values=[]
        while j!=s: i=prev[j]; values.append(res[i][j]); j=i
        amount=min(values); j=t
        while j!=s:
            i=prev[j]; res[i][j]-=amount; res[j][i]+=amount; j=i
    c['flow']=wire([[i,j,Q(cap[i][n+j]-res[i][n+j],scale)] for i,j in sorted(arcs)
                   if cap[i][n+j]>res[i][n+j]])
    paths=[]
    for root in range(N):
        ps={root:[root]}; queue=deque([root])
        while queue:
            i=queue.popleft()
            for j in range(N):
                if res[i][j]>0 and j not in ps: ps[j]=ps[i]+[j]; queue.append(j)
        paths.append(ps)
    components=set()
    for i in range(n):
        components.add(sum(1<<j for j in range(n) if j in paths[i] and i in paths[j]))
    rows=[]
    for m in range(1<<n):
        counts=[sum(bool(m>>i&1) for i in range(n) if (i,j) in arcs) for j in range(n)]
        h=sum(min(p[j],counts[j]*scale) for j in range(n))
        u=sum(sum(min(a,b) for a,b in zip(sorted(p[j] for j in block),
                                          sorted(counts[j]*scale for j in block))) for block in c['blocks'])
        demand=sum(d[i] for i in range(n) if m>>i&1)
        rows.append(dict(mask=m,counts=counts,H=h,U=u,F=h-demand,G=u-demand))
    gamma=min(r['F'] for r in rows)
    minima={r['mask'] for r in rows if r['F']==gamma}
    tight={m for m in minima if rows[m]['H']==rows[m]['U']}
    M=0
    for m in minima: M|=m
    greatest=next((m for m in tight if all(z&~m==0 for z in tight)),None)
    assert M==sum(1<<i for i in range(n) if t not in paths[i])
    for m in minima:
        for i in range(n):
            if m>>i&1:
                assert all(m>>j&1 for j in range(n) if j in paths[i])
    # A full-cut oracle compares original capacities, not the verifier's residual graph.
    cuts=[]
    if fullcuts:
        mincut=sum(d)+gamma
        for left in range(1<<n):
            yy=rows[left]['counts']
            prefix=sum(d[i] for i in range(n) if not left>>i&1)
            for right in range(1<<n):
                cost=prefix+sum(p[j] if right>>j&1 else yy[j]*scale for j in range(n))
                A={s}|{i for i in range(n) if left>>i&1}|{n+j for j in range(n) if right>>j&1}
                closed=all(not res[i][j] for i in A for j in range(N) if j not in A)
                assert (cost==mincut)==closed
                if cost==mincut: cuts.append([left,right])
        assert {l for l,r in cuts}==minima
    return dict(n=n,scale=scale,p=p,d=d,arcs=arcs,paths=paths,components=components,
                rows=rows,gamma=gamma,minima=minima,tight=tight,M=M,greatest=greatest,cuts=cuts)


def moves(c,o,m,rule):
    """Independent predicate; does not call any verifier function."""
    n=o['n']; p=o['p']; sc=o['scale']; E=o['arcs']; yy=o['rows'][m]['counts']
    ks=[1<<i for i in range(n) if m>>i&1] if rule!='block' else sorted(o['components'])
    ans=[]
    for k in ks:
        if k&~m or (m^k) not in o['minima']: continue
        K=[i for i in range(n) if k>>i&1]; a=K[0]
        for block in c['blocks']:
            for x in block:
                if not any((i,x) in E for i in K): continue
                for y in block:
                    if not p[x]<p[y]: continue
                    if not max(p[x],yy[y]*sc)<min(p[y],yy[x]*sc): continue
                    if any((z,y) in E and (z,x) not in E for z in range(n) if m>>z&1): continue
                    for b in range(n):
                        if (b,x) not in E or (b,y) in E: continue
                        if rule=='local' and b!=a: continue
                        if b not in o['paths'][a]: continue
                        ans.append(dict(remove=K,anchor=a,strict=b,x=x,y=y,path=o['paths'][a][b]))
    return ans


def explore(c,o,rule,counts):
    todo=[(o['M'],[])]; seen=set(); terminals=[]; certificates=[]
    inst=v.parse_instance(c); start,gamma,value,adj=v.flow_start(c,inst)
    assert sum(1<<i for i in start)==o['M'] and gamma==Q(o['gamma'],o['scale'])
    components=v.source_components(adj,o['n'])
    while todo:
        m,path=todo.pop()
        if m in seen: continue
        seen.add(m)
        ms=moves(c,o,m,rule)
        counts[rule+'_states']+=1; counts[rule+'_witness_transitions']+=len(ms)
        if not ms:
            terminals.append(m)
            if m in o['tight']:
                cert=deepcopy(c); cert.update(rule='block' if rule=='block' else 'path',deletions=path,
                                            terminal=[i for i in range(o['n']) if m>>i&1])
                result=v.verify(cert)
                assert m==o['greatest']
                certificates.append(cert)
            continue
        for step in ms:
            k=sum(1<<i for i in step['remove']); after=m^k
            # Check EVERY exact-minimum restriction, not just reachable states.
            for t in o['minima']:
                if t&~m or not t&k: continue
                S={i for i in range(o['n']) if t>>i&1}
                new,_=v.deletion_step(inst,S,gamma,adj,components,step,'block' if rule=='block' else 'path')
                assert sum(1<<i for i in new)==t^k and t not in o['tight']
                counts[rule+'_persistence_checks']+=1
            todo.append((after,path+[step]))
    assert len(terminals)==1, ('nonconfluence',c,rule,terminals)
    counts[rule+'_accepted']+=bool(certificates)
    counts[rule+'_nonempty']+=bool(certificates and certificates[0]['deletions'])
    counts[rule+'_missing_greatest']+=bool(o['greatest'] is not None and not certificates)
    return terminals[0],certificates


def record(c,o,results):
    return {'instance':c,'scale':o['scale'],'all_subsets':o['rows'],
            'minima':sorted(o['minima']),'tight_minima':sorted(o['tight']),
            'greatest_exact':o['M'],'greatest_tight':o['greatest'],
            'source_components':sorted(o['components']),'results':results,'minimum_cuts':o['cuts']}


def run_case(c,counts,fullcuts=False):
    o=prepare(c,fullcuts); results={}
    for rule in ('local','path','block'):
        terminal,certs=explore(c,o,rule,counts)
        results[rule]={'terminal':terminal,'accepted':bool(certs),'certificate':certs[0] if certs else None}
    assert results['path']['terminal']&~results['local']['terminal']==0
    assert results['block']['terminal']&~results['path']['terminal']==0
    assert not results['local']['accepted'] or results['path']['accepted']
    assert not results['path']['accepted'] or results['block']['accepted']
    counts['instances']+=1; counts['source_subsets']+=1<<o['n']
    if fullcuts: counts['complete_cuts']+=1<<(2*o['n'])
    return o,results


def exhaustive(out,mode):
    vals=[0,1,2] if mode=='integer' else [0,Q(1,2),1]
    counts=Counter(); digest=sha256(); examples={}; n=3
    slots=[(i,j) for i in range(n) for j in range(n) if i!=j]
    for bits in range(64):
        arcs=[e for k,e in enumerate(slots) if bits>>k&1]
        for p in product(vals,repeat=n):
            for d in product(vals,repeat=n):
                c=instance(n,[list(range(n))],p,d,arcs)
                o,r=run_case(c,counts,True)
                if r['path']['accepted'] and not r['local']['accepted']:
                    counts['path_gain']+=1
                    examples.setdefault('path_gain',record(c,o,r))
                if r['block']['accepted'] and not r['path']['accepted']:
                    counts['block_gain']+=1
                    examples.setdefault('block_gain',record(c,o,r))
                if o['greatest'] is not None and not r['block']['accepted']:
                    examples.setdefault('block_incomplete',record(c,o,r))
                line=[bits,p,d,o['gamma'],o['M'],o['greatest'],{k:[z['terminal'],z['accepted']] for k,z in r.items()}]
                digest.update((json.dumps(line,default=encode,separators=(',',':'))+'\n').encode())
        if bits%16==15: print(mode,bits+1,'supports',counts['instances'],flush=True)
    assert counts['instances']==46656
    data=dict(regime=mode,n=3,quota_values=vals,blocks=[[0,1,2]],counts=dict(counts),
              ordered_record_sha256=digest.hexdigest(),examples=examples,discrepancies=0,
              limits='All 64 labelled loopless n=3 supports, one block. Regimes overlap in 4096 instances.')
    write(out/(mode.upper()+'_RESULTS.json'),data)
    print(json.dumps(data['counts'],sort_keys=True),flush=True)


def focused(out):
    counts=Counter(); records={}
    cases=[('frozen',3,[[0,1,2]],[0,2,1],[1,1,0],[(0,1),(0,2),(1,2)]),
           ('fractional',2,[[0,1]],[0,Q(3,4)],[Q(1,2),0],[(0,1),(1,0)]),
           ('multiple_completions',2,[[0,1]],[0,0],[0,0],[])]
    # Four disjoint copies of the frozen path example: 16 reachable states.
    k=4;n=3*k
    cases.append(('four_path_choices',n,[list(range(3*i,3*i+3)) for i in range(k)],
                  [0,2,1]*k,[1,1,0]*k,[(3*i+a,3*i+b) for i in range(k) for a,b in [(0,1),(0,2),(1,2)]]))
    for name,n,bs,p,d,arcs in cases:
        c=instance(n,bs,p,d,arcs); o,r=run_case(c,counts,n<=3); records[name]=record(c,o,r)
    base=records['frozen']['results']['path']['certificate']; mutations=[]
    def add(name,f,b=None):
        c=deepcopy(base if b is None else b); f(c); mutations.append((name,c))
    add('bool_version',lambda c:c.update(version=True))
    add('float_quota',lambda c:c['capacities'].__setitem__(1,2.0))
    add('negative_quota',lambda c:c['demands'].__setitem__(0,-1))
    add('bad_fraction',lambda c:c['demands'].__setitem__(0,'1/0'))
    add('duplicate_arc',lambda c:c['arcs'].append(c['arcs'][0]))
    add('loop',lambda c:c['arcs'].append([0,0]))
    add('partition',lambda c:c.update(blocks=[[0,1],[1,2]]))
    add('wrong_terminal',lambda c:c.update(terminal=[0,1,2]))
    add('duplicate_terminal',lambda c:c['terminal'].append(1))
    add('no_deletions',lambda c:c.update(deletions=[]))
    add('no_maximum_flow',lambda c:c.update(flow=[]))
    add('flow_overload',lambda c:c['flow'][0].__setitem__(2,2))
    add('unsupported_flow',lambda c:c.update(flow=[[0,0,1]]))
    add('duplicate_flow',lambda c:c['flow'].append(c['flow'][0]))
    add('nonneutral',lambda c:c['demands'].__setitem__(0,2))
    add('no_path',lambda c:c['deletions'][0].update(path=[]))
    add('invented_direct_edge',lambda c:c['deletions'][0].update(path=[0,1]))
    add('reverse_path',lambda c:c['deletions'][0].update(path=[1,5,0]))
    add('bool_node',lambda c:c['deletions'][0].update(path=[False,5,1]))
    add('right_as_left',lambda c:c['deletions'][0].update(strict=5))
    add('wrong_strict_source',lambda c:c['deletions'][0].update(strict=0,path=[0]))
    add('bad_remove',lambda c:c['deletions'][0].update(remove=[0,0]))
    add('wrong_anchor',lambda c:c['deletions'][0].update(anchor=1))
    add('invented_block',lambda c:(c.update(rule='block'),c['deletions'][0].update(remove=[0,1])))
    corrupt=[]
    for name,c in mutations:
        try:v.verify(c)
        except v.Invalid as e:corrupt.append({'name':name,'rejected':True,'reason':str(e),'certificate':c})
        else:raise AssertionError(('corruption accepted',name))
    write(out/'FOCUSED_RESULTS.json',dict(counts=dict(counts),cases=records,corruptions=corrupt,rejections=len(corrupt)))
    print(dict(counts), 'rejections',len(corrupt),flush=True)


def sample(out):
    rng=random.Random(74220260927); counts=Counter(); examples={}; digest=sha256()
    vals=[0,Q(1,2),1,Q(3,2),2,3]
    for i in range(500):
        n=4+i%3
        bs=[list(range(n))] if i%2==0 else [list(range(0,n//2)),list(range(n//2,n))]
        c=instance(n,bs,[rng.choice(vals) for _ in range(n)],[rng.choice(vals) for _ in range(n)],
                   [(a,b) for a in range(n) for b in range(n) if a!=b and rng.random()<.4])
        o,r=run_case(c,counts,i<30)
        if r['block']['accepted'] and not r['path']['accepted']:
            examples.setdefault('block_gain',record(c,o,r));counts['block_gain']+=1
        if o['greatest'] is not None and not r['block']['accepted']:
            examples.setdefault('block_incomplete',record(c,o,r));counts['block_incomplete']+=1
        digest.update((json.dumps([c,{k:z['terminal'] for k,z in r.items()}],sort_keys=True)+'\n').encode())
    write(out/'SAMPLE_RESULTS.json',dict(seed=74220260927,counts=dict(counts),examples=examples,
                                      ordered_record_sha256=digest.hexdigest(),discrepancies=0))
    print(dict(counts),flush=True)


if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit(__doc__)
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);mode=sys.argv[2]
    if mode in ('integer','rational'):exhaustive(out,mode)
    elif mode=='focused':focused(out)
    elif mode=='sample':sample(out)
    else:raise SystemExit(__doc__)
