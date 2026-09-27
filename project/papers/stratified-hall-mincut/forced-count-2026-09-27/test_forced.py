#!/usr/bin/env python3
"""python test_forced.py OUT integer|rational|focused|sample
Uses the frozen predecessor's independent scaled-integer flow/cut/subset oracle.
The new predicate below is independent of verify_forced.py.
"""
from collections import Counter
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'residual-certificate-2026-09-27'))
import test_residual as old
import verify_forced as v


def make(n,bs,p,d,arcs):
    c=old.instance(n,bs,p,d,arcs);c['version']=3;return c


def moves(c,o,m,rule):
    n=o['n'];E=o['arcs'];sc=o['scale'];p=o['p'];yy=o['rows'][m]['counts']
    ks=[1<<a for a in range(n) if m>>a&1] if rule=='path' else sorted(o['components'])
    ans=[]
    for k in ks:
        if k&~m or (m^k) not in o['minima']:continue
        K=[i for i in range(n) if k>>i&1];a=K[0]
        for bs in c['blocks']:
            for x in bs:
                incidence=any((i,x) in E for i in K)
                forced=[i for i in range(n) if i in o['paths'][a] and (i,x) in E]
                if not incidence and len(forced)*sc<=p[x]:continue
                for y in bs:
                    if not p[x]<p[y]:continue
                    if not max(p[x],yy[y]*sc)<min(p[y],yy[x]*sc):continue
                    if any((z,y) in E and (z,x) not in E for z in range(n) if m>>z&1):continue
                    for b in range(n):
                        if b not in o['paths'][a] or (b,x) not in E or (b,y) in E:continue
                        step=dict(remove=K,anchor=a,strict=b,x=x,y=y,path=o['paths'][a][b],
                                  guard='incidence' if incidence else 'forced')
                        if not incidence:step['forced_sources']=forced
                        ans.append(step)
    return ans


def explore(c,o,rule,counts):
    inst=v.parse_instance(c);S,gamma,value,adj=v.flow_start(c,inst)
    assert sum(1<<a for a in S)==o['M'] and gamma==Q(o['gamma'],o['scale'])
    comps=v.source_components(adj,o['n']);todo=[(o['M'],[])];seen=set();terminals=[];certs=[]
    while todo:
        m,path=todo.pop()
        if m in seen:continue
        seen.add(m);ms=moves(c,o,m,rule)
        counts[rule+'_states']+=1;counts[rule+'_witness_transitions']+=len(ms)
        if not ms:
            terminals.append(m)
            if m in o['tight']:
                c2=deepcopy(c);c2.update(rule=rule,deletions=path,terminal=[a for a in range(o['n']) if m>>a&1])
                r=v.verify(c2);assert m==o['greatest'];certs.append(c2)
            continue
        for step in ms:
            k=sum(1<<i for i in step['remove'])
            counts[rule+'_'+step['guard']+'_transitions']+=1
            for t in o['minima']:
                if t&~m or not t&k:continue
                T={i for i in range(o['n']) if t>>i&1}
                new,r=v.deletion_step(inst,T,gamma,adj,comps,step,rule)
                assert sum(1<<i for i in new)==t^k and t not in o['tight']
                counts[rule+'_persistence_checks']+=1
            todo.append((m^k,path+[step]))
    assert len(terminals)==1,('nonconfluence',c,rule,terminals)
    counts[rule+'_accepted']+=bool(certs)
    counts[rule+'_nonempty']+=bool(certs and certs[0]['deletions'])
    counts[rule+'_missing_greatest']+=bool(o['greatest'] is not None and not certs)
    return {'terminal':terminals[0],'accepted':bool(certs),'certificate':certs[0] if certs else None}


def run_case(c,counts,fullcuts=False):
    o=old.prepare(c,fullcuts);r={};prev=Counter();c2=deepcopy(c);c2['version']=2
    for rule in ('path','block'):
        term,certs=old.explore(c2,o,rule,prev)
        r['v2_'+rule]={'terminal':term,'accepted':bool(certs),'certificate':certs[0] if certs else None}
        r[rule]=explore(c,o,rule,counts)
        assert not r[rule]['terminal']&~term
        assert not certs or r[rule]['accepted']
    counts.update({'v2_'+k:v for k,v in prev.items()})
    assert not r['block']['terminal']&~r['path']['terminal']
    counts['instances']+=1;counts['source_subsets']+=1<<o['n']
    if fullcuts:counts['complete_cuts']+=1<<(2*o['n'])
    return o,r


def save_example(c,o,r):return old.record(c,o,r)


def exhaustive(out,mode):
    vals=[0,1,2] if mode=='integer' else [0,Q(1,2),1]
    counts=Counter();examples={};digest=sha256();n=3
    slots=[(i,j) for i in range(n) for j in range(n) if i!=j]
    for bits in range(64):
        E=[e for k,e in enumerate(slots) if bits>>k&1]
        for p in product(vals,repeat=n):
            for d in product(vals,repeat=n):
                c=make(n,[[0,1,2]],p,d,E);o,r=run_case(c,counts,True)
                for rule in ('path','block'):
                    if r[rule]['accepted'] and not r['v2_'+rule]['accepted']:
                        counts[rule+'_gain']+=1;examples.setdefault(rule+'_gain',save_example(c,o,r))
                if o['greatest'] is not None and not r['block']['accepted']:
                    examples.setdefault('incomplete',save_example(c,o,r))
                line=[bits,p,d,o['gamma'],o['M'],o['greatest'],{k:[z['terminal'],z['accepted']] for k,z in r.items()}]
                digest.update((json.dumps(line,default=old.encode,separators=(',',':'))+'\n').encode())
        if bits%16==15:print(mode,bits+1,'supports',counts['instances'],flush=True)
    assert counts['instances']==46656
    expected=(33609,33609) if mode=='integer' else (32292,32430)
    assert (counts['v2_path_accepted'],counts['v2_block_accepted'])==expected
    old.write(out/(mode.upper()+'_RESULTS.json'),dict(regime=mode,n=3,quota_values=vals,counts=dict(counts),
      examples=examples,ordered_record_sha256=digest.hexdigest(),discrepancies=0,overlap_with_other_regime=4096))
    print(dict(counts),flush=True)


def sample(out):
    rng=random.Random(74220260927);counts=Counter();examples={};digest=sha256()
    vals=[0,Q(1,2),1,Q(3,2),2,3]
    for i in range(500):
        n=4+i%3;bs=[list(range(n))] if i%2==0 else [list(range(0,n//2)),list(range(n//2,n))]
        c=make(n,bs,[rng.choice(vals) for _ in range(n)],[rng.choice(vals) for _ in range(n)],
               [(a,b) for a in range(n) for b in range(n) if a!=b and rng.random()<.4])
        o,r=run_case(c,counts,i<30)
        if o['greatest'] is not None and not r['block']['accepted']:examples.setdefault('incomplete',save_example(c,o,r))
        if r['block']['accepted'] and not r['v2_block']['accepted']:
            counts['block_gain']+=1;examples.setdefault('block_gain',save_example(c,o,r))
        digest.update((json.dumps([c,{k:z['terminal'] for k,z in r.items()}],sort_keys=True)+'\n').encode())
    assert counts['v2_path_accepted']==198 and counts['v2_block_accepted']==199
    old.write(out/'SAMPLE_RESULTS.json',dict(seed=74220260927,counts=dict(counts),examples=examples,
       ordered_record_sha256=digest.hexdigest(),discrepancies=0))
    print(dict(counts),flush=True)


def focused(out):
    E=[(0,1),(0,2),(1,2)];cases=[
      ('frozen_path',3,[[0,1,2]],[0,2,1],[1,1,0],E),
      ('forced_repair',3,[[0,1,2]],[1,0,1],[1,0,0],E),
      ('scc_gain',3,[[0,1,2]],[Q(1,2),0,1],[Q(1,2),Q(1,2),0],E),
      ('unsafe_equality',3,[[0,1],[2]],[1,2,1],[0,2,0],[(0,2),(1,0),(1,2),(2,0)]),
      ('three_forced_chains',9,[list(range(3*i,3*i+3)) for i in range(3)],[1,0,1]*3,[1,0,0]*3,
       [(3*i+a,3*i+b) for i in range(3) for a,b in E])]
    counts=Counter();examples={}
    for name,n,bs,p,d,arcs in cases:
        c=make(n,bs,p,d,arcs);o,r=run_case(c,counts,n<=3);examples[name]=save_example(c,o,r)
        assert r['block']['accepted']
        if name=='forced_repair':
            assert not r['v2_block']['accepted'] and r['block']['terminal']==4
            old.write(out/'DEMO_CERTIFICATE.json',r['block']['certificate'])
            old.write(out/'DEMO_RESULT.json',v.verify(r['block']['certificate']))
        if name=='three_forced_chains':
            cc=Counter();explore(c,o,'block',cc)
            assert cc['block_states']==27 and cc['block_witness_transitions']==54
    base=examples['forced_repair']['results']['block']['certificate'];mutations=[]
    def add(name,f):
        c=deepcopy(base);f(c);mutations.append((name,c))
    add('wrong_version',lambda c:c.update(version=2))
    add('bool_version',lambda c:c.update(version=True))
    add('missing_guard',lambda c:c['deletions'][0].pop('guard'))
    add('fake_incidence',lambda c:c['deletions'][0].update(guard='incidence'))
    add('unknown_guard',lambda c:c['deletions'][0].update(guard='magic'))
    add('missing_contributors',lambda c:c['deletions'][0].pop('forced_sources'))
    add('omitted_contributor',lambda c:c['deletions'][0].update(forced_sources=[]))
    add('invented_contributor',lambda c:c['deletions'][0].update(forced_sources=[0,1]))
    add('duplicate_contributor',lambda c:c['deletions'][0].update(forced_sources=[0,0]))
    add('receiver_as_source',lambda c:c['deletions'][0].update(forced_sources=[5]))
    add('bool_contributor',lambda c:c['deletions'][0].update(forced_sources=[False]))
    add('missing_residual_edge',lambda c:c['deletions'][0].update(path=[1,0]))
    add('bad_terminal',lambda c:c.update(terminal=[0,2]))
    add('nonmaximum_flow',lambda c:c.update(flow=[]))
    add('float_capacity',lambda c:c['capacities'].__setitem__(0,1.0))
    rejected=[]
    for name,c in mutations:
        try:v.verify(c)
        except v.Invalid as e:rejected.append(dict(case=name,certificate=c,reason=str(e)))
        else:raise AssertionError(('corruption accepted',name))
    c=examples['unsafe_equality']['instance'];inst=v.parse_instance(c)
    S,g,f,adj=v.flow_start(c,inst)
    bad=dict(remove=[0],anchor=0,strict=1,x=0,y=1,path=[0,5,1],guard='forced',forced_sources=[1])
    try:v.deletion_step(inst,S,g,adj,v.source_components(adj,3),bad,'block')
    except v.Invalid as e:
        assert str(e)=='forced count does not strictly exceed low capacity'
        rejected.append(dict(case='nonstrict_bound_step',step=bad,instance=c,reason=str(e)))
    else:raise AssertionError('unsafe equality accepted')
    old.write(out/'FOCUSED_RESULTS.json',dict(counts=dict(counts),examples=examples,rejections=rejected,
      complete_certificate_rejections=len(mutations),unsafe_step_rejections=1))
    print(dict(counts),'rejected',len(rejected),flush=True)


if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit(__doc__)
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);mode=sys.argv[2]
    if mode in ('integer','rational'):exhaustive(out,mode)
    elif mode=='sample':sample(out)
    elif mode=='focused':focused(out)
    else:raise SystemExit(__doc__)
