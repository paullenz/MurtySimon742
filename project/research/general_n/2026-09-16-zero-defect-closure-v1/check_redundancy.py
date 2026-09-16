#!/usr/bin/env python3
"""Reproduce finite tests of the zero-defect deletion lemma.

Positive tests are graph completions of the displayed local structural lemma,
not diameter-two edge-critical graphs. Canonical controls satisfy the earlier
selected-system boundary but FAIL global criticality, as the new proof predicts.
"""
from __future__ import annotations
from itertools import combinations
from pathlib import Path
import gzip, hashlib, json, random, subprocess, tempfile

ROOT=Path(__file__).resolve().parent

def edge(a:list[int],u:int,v:int)->None:
    assert u!=v
    a[u]|=1<<v;a[v]|=1<<u

def reachable(a:list[int])->list[int]:
    out=[]
    for u,row in enumerate(a):
        reach=row|(1<<u); bits=row
        while bits:
            bit=bits&-bits;bits-=bit
            reach|=a[bit.bit_length()-1]
        out.append(reach)
    return out

def decision(name:str,a:list[int],d:int)->str:
    n=len(a); full=(1<<n)-1; before=reachable(a)
    diam=int(all(r==full for r in before)); edges=losing=losttotal=afterdiam=0
    for s,t in combinations(range(d),2):
        if not (a[s]>>t)&1:continue
        edges+=1;a[s]^=1<<t;a[t]^=1<<s
        after=reachable(a)
        # Undirected lost pairs are counted just once.
        lost=sum(((before[x]&~after[x])&~((1<<(x+1))-1)).bit_count() for x in range(n))
        losttotal+=lost;losing+=bool(lost);afterdiam+=all(r==full for r in after)
        a[s]^=1<<t;a[t]^=1<<s
    return f'{name}\t{n}\t{d}\t{diam}\t{edges}\t{losing}\t{losttotal}\t{afterdiam}\n'

def skeleton(d:int,z:int,q:list[int],p:list[int],o:int=0,neutral:int=0):
    assert d>=2 and z>=1 and len(q)==len(p)==d and min(p)>=1
    assert d>=3 or not any(q)
    nxt=d;C=list(range(nxt,nxt+z));nxt+=z
    Q=[];V=[]
    for count in q:Q.append(list(range(nxt,nxt+count)));nxt+=count
    for count in p:V.append(list(range(nxt,nxt+count)));nxt+=count
    O=list(range(nxt,nxt+o));nxt+=o
    U=list(range(nxt,nxt+neutral));nxt+=neutral
    assert nxt<=63
    a=[0]*nxt
    for s,t in combinations(range(d),2):edge(a,s,t)
    for t in range(d):
        for x in C+O+V[t]:edge(a,t,x)
        for r in range(d):
            if r!=t:
                for x in Q[r]:edge(a,t,x)
    for c in C:
        for pool in V:
            for v in pool:edge(a,c,v)
    free=[(u,v) for u,v in combinations(range(d,nxt),2) if not (a[u]>>v)&1]
    return a,free,dict(C=C,Q=Q,V=V,O=O,U=U)

def canonical_control(d:int):
    # Vertex order is T,C,H,V,O,pivot, so the generic deletion tests use T=0..d-1.
    T=list(range(d));C=list(range(d,2*d));H=list(range(2*d,3*d));V=list(range(3*d,4*d))
    O=[4*d,4*d+1];pivot=4*d+2;n=pivot+1;a=[0]*n
    for t,s in combinations(T,2):edge(a,t,s)
    for t in T:
        for c in C:edge(a,t,c)
        edge(a,t,V[t])
    for h in H:
        for v in V:edge(a,h,v)
    for c in C:
        for v in V:edge(a,c,v)
    for u in H+V+O:edge(a,pivot,u)
    for o in O:
        for x in T+C:edge(a,o,x)
    full=(1<<n)-1;assert all(x==full for x in reachable(a))
    B=H+V+O;A=T+C;Abits=sum(1<<x for x in A)
    J=[full^row^(1<<u) for u,row in enumerate(a)]
    assert a[pivot].bit_count()==max(row.bit_count() for row in a)
    assert [x for x in range(n) if (J[pivot]>>x)&1]==A
    chosen=[(h,t,V[t]) for h in H for t in T]
    represented={tuple(sorted((u,v))) for u,i,v in chosen}
    actual={(u,v) for u,v in combinations(B,2) if (a[u]>>v)&1}
    assert represented==actual and len(chosen)==len(actual)
    S={u:0 for u in B};R={u:J[u]&Abits for u in B}
    for u,i,v in chosen:
        assert (J[u]|J[i])==full^(1<<v)
        assert (J[u]>>i)&1 and not (S[u]>>i)&1
        S[u]|=1<<i;R[u]^=1<<i
    rho={u:R[u].bit_count() for u in B}
    Ri={i:sum((R[u]>>i)&1 for u in B) for i in A}
    delta={i:(a[i]&Abits).bit_count() for i in A}
    s={i:max(0,delta[i]-Ri[i]) for i in A}
    x={i:sum((S[u]>>i)&1 for u in B) for i in A}
    assert [i for i in A if s[i]==d]==T
    assert [u for u in B if rho[u]>=d]==H
    assert all(x[i]>=s[i] for i in A)
    for u,i,v in chosen:
        Fi=a[i]&Abits
        assert not (Fi&~(R[u]|R[v])) and Fi.bit_count()<=rho[u]+Ri[i]
        assert not ((S[u]^(1<<i))&~J[v]) and not (S[v]&~J[u])
    assert all(s[c]==0 for c in C)
    W=d*d;m=d
    assert W-d-(d-1)*m==0
    tau=sum(delta.values())//2-sum(rho.values())
    assert tau==-d*(d-1)//2
    return a,dict(d=d,n=n,W=W,m=m,tau=tau,selected_obligations=len(chosen),
       exact_tight_block=True,minimum_complement_pivot=True,diameter_two=True,
       critical=False,scope='Constructed noncritical graph; not a counterexample to the conjecture.')

def negative_controls():
    out=[]
    # No common label: clique T with private leaves joined through a neutral hub.
    d=3;a=[0]*7
    for s,t in combinations(range(d),2):edge(a,s,t)
    for t in range(d):edge(a,t,3+t);edge(a,6,3+t)
    out.append(('missing_common_label',a,d))
    # C--V adjacency is essential. All other displayed d=2 classes are respected.
    a=[0]*6
    for u,v in [(0,1),(0,2),(1,2),(0,3),(1,4),(2,3),(5,3),(5,4)]:edge(a,u,v)
    out.append(('missing_common_to_pool_edge',a,2))
    # d=2 one-hole labels cannot occur in the zero-defect canonical regime.
    a=[0]*7
    for u,v in [(0,1),(0,2),(1,2),(0,3),(1,4),(2,3),(2,4),(1,5),(6,3),(6,4),(6,5),(6,2)]:edge(a,u,v)
    out.append(('d2_one_hole_not_permitted',a,2))
    # Extra vertex adjacent to just one tight label: a two-hole label or off-pool leakage.
    a,_,_=skeleton(3,1,[0,0,0],[1,1,1],neutral=2)
    q=len(a)-2;hub=len(a)-1;edge(a,2,q)
    for v in range(3,len(a)-1):edge(a,hub,v)
    out.append(('two_hole_or_off_pool_leakage',a,3))
    # A missing internal tight edge spoils the alternative tight-label path.
    a,_,_=skeleton(3,1,[1,0,0],[1,1,1],neutral=1)
    a[0]^=1<<2;a[2]^=1<<0
    hub=len(a)-1
    for v in range(3,hub):edge(a,hub,v)
    out.append(('tight_graph_not_complete',a,3))
    return out

def main()->None:
    rows=[];specs=[];records=[];canonical=[]
    def add(name,a,d,kind):
        line=decision(name,a,d)
        f=line.strip().split('\t')
        if kind=='negative':assert int(f[6])>0,(name,line)
        else:assert int(f[6])==0,(name,line)
        rows.append(line);records.append((name,d,a[:],kind))
    parameters=[(2,1,[0,0],[1,1]),(2,2,[0,0],[1,1]),
       (3,1,[1,0,0],[1,1,1]),(3,1,[1,1,0],[1,1,1]),
       (3,1,[1,0,0],[2,1,1]),(3,2,[0,0,0],[1,1,1]),
       (4,1,[1,0,0,0],[1,1,1,1])]
    for ci,(d,z,q,p) in enumerate(parameters):
        base,free,info=skeleton(d,z,q,p); assert len(free)<=12
        count=1<<len(free)
        for mask in range(count):
            a=base[:]
            for bit,(u,v) in enumerate(free):
                if mask&(1<<bit):edge(a,u,v)
            add(f'e{ci}_{mask}',a,d,'exhaustive')
        specs.append(dict(d=d,z=z,q=q,p=p,free_edges=len(free),graphs=count))
    rng=random.Random(7420916)
    for ci in range(240):
        d=rng.randrange(3,9);z=rng.randrange(1,3)
        q=[rng.randrange(3) for _ in range(d)];p=[rng.randrange(1,4) for _ in range(d)]
        a,free,_=skeleton(d,z,q,p,o=rng.randrange(3),neutral=rng.randrange(3))
        for u,v in free:
            if rng.getrandbits(1):edge(a,u,v)
        add(f's{ci}',a,d,'sampled')
    for d in range(2,16):
        a,result=canonical_control(d);add(f'canonical_d{d}',a,d,'canonical_control');canonical.append(result)
    for name,a,d in negative_controls():add(name,a,d,'negative')
    text=''.join(rows)
    inputs=''.join(name+'\t'+str(d)+'\t'+str(len(a))+'\t'+'\t'.join(map(str,a))+'\n' for name,d,a,_ in records)
    with tempfile.TemporaryDirectory() as temp:
        temp=Path(temp); inp=temp/'graphs.tsv';exe=temp/'check'
        inp.write_text(inputs)
        subprocess.run(['g++','-O2','-std=c++17',str(ROOT/'check_redundancy.cpp'),'-o',str(exe)],check=True,timeout=30)
        checked=subprocess.run([str(exe),str(inp)],check=True,text=True,capture_output=True,timeout=35).stdout
    assert checked==text,'Python/C++ per-graph mismatch'
    (ROOT/'GRAPH_INPUTS.tsv.gz').write_bytes(gzip.compress(inputs.encode(),mtime=0))
    (ROOT/'DELETION_DECISIONS.tsv.gz').write_bytes(gzip.compress(text.encode(),mtime=0))
    groups={}
    for row,rec in zip(rows,records):
        f=row.strip().split('\t');g=groups.setdefault(rec[3],dict(graphs=0,diameter_two_graphs=0,
          tight_edge_deletions=0,losing_deletions=0,lost_close_pairs=0,diameter_two_after_deletions=0))
        for key,val in zip(g,[1,int(f[3]),int(f[4]),int(f[5]),int(f[6]),int(f[7])]):g[key]+=val
    # Pure arithmetic check of the forced common label at zero defect, independent of graph tests.
    arithmetic=[]
    for d in range(2,31):
        count=0
        for m in range(d,6*d+1):
            for z in range(0,6*d+2):
                rem=d+(d-1)*m-d*z
                if rem<0 or rem%(d-1):continue
                p=rem//(d-1)
                if d==2 and p:continue # positive-demand K labels impossible for d=2
                assert z>=1
                count+=1
        arithmetic.append(dict(d=d,solutions=count))
    result=dict(status='PASS_INTERNAL_ZERO_DEFECT_DELETION_LEMMA',groups=groups,
      exhaustive_specs=specs,sample_seed=7420916,canonical_controls=canonical,
      negative_controls=[name for name,_,_ in negative_controls()],
      arithmetic_cases=sum(r['solutions'] for r in arithmetic),arithmetic_rows=arithmetic,
      python_cpp_records=len(records),
      input_sha256=hashlib.sha256(inputs.encode()).hexdigest(),
      decisions_sha256=hashlib.sha256(text.encode()).hexdigest(),
      limits=['No catalogue scan or promotion.',
        'Positive completion tests are the local structural lemma, not full canonical realizations.',
        'Canonical controls are diameter-two NONCRITICAL graphs satisfying the selected-system boundary.',
        'The 240 varied completions are sampled, not exhaustive.',
        'Both implementations and the proof are from the same assistant; external review open.'])
    (ROOT/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','groups','arithmetic_cases','python_cpp_records','input_sha256','decisions_sha256']},indent=2))
if __name__=='__main__':main()
