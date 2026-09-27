#!/usr/bin/env python3
"""Independent exhaustive oracle and certificate producer; not part of verifier.
Run: python test_local.py OUTPUT_DIRECTORY [integer|rational|hostile|orders|limits]
"""
from __future__ import annotations
from collections import Counter, deque
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, permutations, product
from math import factorial, comb, lcm
from pathlib import Path
import json
import sys
import verify_local as v


def encode(x):
    if isinstance(x, Q):
        return x.numerator if x.denominator == 1 else str(x)
    raise TypeError(type(x).__name__)


def write(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=encode)+'\n')


def network_flow(n, p, d, arcs):
    scale = lcm(*(Q(q).denominator for q in p+d))
    N, a, b = 2*n+2, 2*n, 2*n+1
    cap = [[0]*N for _ in range(N)]
    for i in range(n):
        cap[a][i] = int(Q(d[i])*scale)
        cap[n+i][b] = int(Q(p[i])*scale)
    for i, j in arcs:
        cap[i][n+j] = scale
    r = [row[:] for row in cap]
    while True:
        prev, todo = {a: None}, deque([a])
        while todo and b not in prev:
            i = todo.popleft()
            for j in range(N):
                if r[i][j] and j not in prev:
                    prev[j] = i
                    todo.append(j)
        if b not in prev:
            break
        amount, j = None, b
        while j != a:
            i = prev[j]
            amount = r[i][j] if amount is None else min(amount, r[i][j])
            j = i
        j = b
        while j != a:
            i = prev[j]
            r[i][j] -= amount
            r[j][i] += amount
            j = i
    return [[i,j,Q(cap[i][n+j]-r[i][n+j],scale)]
            for i,j in sorted(arcs) if cap[i][n+j] > r[i][n+j]]


def brute(n, blocks, p, d, arcs):
    """Compute margins by direct source subsets and rational scaling.
    Does not call the verifier's quantity, residual or local-step routines.
    """
    scale = lcm(*(Q(q).denominator for q in p+d))
    pp = [int(Q(q)*scale) for q in p]
    dd = [int(Q(q)*scale) for q in d]
    rows=[]
    for mask in range(1<<n):
        S=[i for i in range(n) if mask>>i&1]
        yy=[sum((i,j) in arcs for i in S)*scale for j in range(n)]
        h=sum(min(pp[j], yy[j]) for j in range(n))
        u=sum(sum(min(a,b) for a,b in zip(sorted(pp[j] for j in block),
                                            sorted(yy[j] for j in block))) for block in blocks)
        demand=sum(dd[i] for i in S)
        rows.append((mask,h,u,h-demand,u-demand))
    gamma=min(row[3] for row in rows)
    mins=[row[0] for row in rows if row[3]==gamma]
    tight=[row[0] for row in rows if row[3]==gamma and row[1]==row[2]]
    maxmin=0
    for m in mins: maxmin |= m
    greatest=None
    for m in tight:
        if all(t & ~m == 0 for t in tight): greatest=m
    return Q(gamma,scale), maxmin, greatest, rows


def global_wcd(n, blocks, p, d, arcs):
    for block in blocks:
        for x in block:
            for y in block:
                if p[x] >= p[y]: continue
                if d[y] > Q(d[x]).__floor__(): return False
                if (y,x) in arcs and (x,y) not in arcs: return False
                for z in range(n):
                    if z in (x,y): continue
                    if (z,x) in arcs and (z,y) not in arcs: return False
                    if (x,z) in arcs and (y,z) not in arcs: return False
    return True


def make(n, blocks, p, d, arcs, flow=None):
    return {"version":1,"n":n,"blocks":blocks,"capacities":p,"demands":d,
            "arcs":[list(e) for e in sorted(arcs)],
            "flow": network_flow(n,p,d,arcs) if flow is None else flow,
            "deletions":[],"terminal":[]}


def wire(c):
    return json.loads(json.dumps(c,default=encode))


def explore(c, oracle, all_orders=True):
    """Visit all locally certified deletion choices from residual maximum."""
    c = wire(c)
    inst = v.parse_instance(c)
    s, gamma, value = v.flow_start(c,inst)
    assert gamma == oracle[0]
    assert sum(1<<i for i in s) == oracle[1]
    pending=[(s,[])]; seen=set(); terminals=[]; transitions=0; stuck=[]
    while pending:
        S,path=pending.pop()
        mask=sum(1<<i for i in S)
        if mask in seen: continue
        seen.add(mask)
        counts,h,u,f=v.quantities(*inst,S)
        assert f == gamma
        if h==u:
            z=deepcopy(c); z['deletions']=path; z['terminal']=sorted(S)
            result=v.verify(z)
            assert mask == oracle[2], (c,oracle,z,result)
            terminals.append(z)
            continue
        moves=[]
        for a in sorted(S):
            for y in range(c['n']):
                for x in range(c['n']):
                    if not inst[2][x] < inst[2][y] or not any(x in b and y in b for b in inst[1]):
                        continue
                    if (a,x) not in inst[4] or (a,y) in inst[4]:
                        continue
                    try:
                        after,_=v.local_step(inst,S,x,y,gamma,a)
                    except v.Invalid:
                        continue
                    moves.append((after,path+[{'x':x,'y':y,'delete':a}]))
                    transitions+=1
        if not moves: stuck.append(mask)
        pending.extend(moves if all_orders else moves[:1])
    assert len(terminals)+len(stuck)==1, ("local confluence failure", c, terminals, stuck)
    return {"states":len(seen),"transitions":transitions,"stuck":len(stuck)},terminals


def exhaustive(out, mode):
    n=3
    blocks=[[0,1,2]]
    # The two regimes intentionally overlap at quotas 0 and 1.
    vals=[0,1,2] if mode=='integer' else [Q(0),Q(1,2),Q(1)]
    edge_slots=[(i,j) for i in range(n) for j in range(n) if i!=j]
    counts=Counter(); digest=sha256(); examples={}
    for bits in range(1<<len(edge_slots)):
        arcs={e for k,e in enumerate(edge_slots) if bits>>k&1}
        for p in product(vals,repeat=n):
            for d in product(vals,repeat=n):
                p,d=list(p),list(d)
                oracle=brute(n,blocks,p,d,arcs)
                c=make(n,blocks,p,d,arcs)
                stats,terminals=explore(c,oracle)
                counts['instances']+=1
                counts['subset_records']+=1<<n
                counts['states']+=stats['states']
                counts['transitions']+=stats['transitions']
                counts['stuck_states']+=stats['stuck']
                counts['certified_instances']+=bool(terminals)
                counts['certificates_checked']+=len(terminals)
                wcd=global_wcd(n,blocks,p,d,arcs)
                counts['wcd_rd_instances']+=wcd
                if wcd: assert terminals and stats['stuck']==0
                if terminals and not wcd:
                    counts['certified_outside_wcd_rd']+=1
                    if len(terminals[0]['deletions']) and 'outside_wcd' not in examples:
                        examples['outside_wcd']=terminals[0]
                if oracle[2] is not None and not terminals:
                    counts['greatest_tight_exists_but_no_local_certificate']+=1
                    if 'incomplete' not in examples: examples['incomplete']=wire(c)
                if any(t['deletions'] for t in terminals):
                    counts['instances_with_nonempty_certificate']+=1
                if bool(terminals) and stats['stuck']:
                    counts['successful_and_stuck_orders']+=1
                row=[bits,p,d,oracle[0],oracle[1],oracle[2],stats,bool(terminals)]
                digest.update((json.dumps(row,separators=(',',':'),default=encode)+'\n').encode())
    assert counts['instances'] == 64*27*27
    result={'regime':mode,'n':n,'blocks':blocks,'quota_values':vals,
            'loopless_supports':64,'counts':dict(counts),'ordered_record_sha256':digest.hexdigest(),
            'mismatches':0,'examples':examples,
            'limits':'all labelled n=3 supports only; regimes overlap; no inference by extrapolation'}
    write(out/(mode.upper()+'_RESULTS.json'),result)
    print(json.dumps(result,default=encode))


def hostile(out):
    examples={}
    # Non-WCD, strict local reverse nesting, with a neutral deletion.
    cases=[('separate_source',3,[[0,1,2]],[0,0,1],[0,0,0],{(0,1)}),
           ('reverse_nesting',3,[[0,1],[2]],[1,3,0],[0,0,1],{(1,0),(2,0)}),
           ('selected_low',2,[[0,1]],[0,1],[Q(1,2),0],{(1,0)}),
           ('fractional_capacity',2,[[0,1]],[0,Q(3,4)],[Q(1,2),0],{(0,1),(1,0)}),
           ('intersection_obstruction',3,[[0,1],[2]],[0,2,0],[1,1,1],{(0,1),(1,0),(2,1)})]
    for name,n,bs,p,d,arcs in cases:
        c=make(n,bs,p,d,arcs); o=brute(n,bs,p,d,arcs)
        st,cs=explore(c,o); assert cs
        examples[name]={'certificate':wire(cs[0]),'verification':v.verify(wire(cs[0])),
                        'oracle_margin':o[0],'global_wcd_rd':global_wcd(n,bs,p,d,arcs),'exploration':st}
    # 8 independent deletion pairs and a compulsory isolated demand source.
    k=8; n=2*k+1; bs=[[2*i,2*i+1] for i in range(k)]+[[n-1]]
    p=[x for _ in range(k) for x in (0,1)]+[0]; d=[0]*(n-1)+[1]
    arcs={(i,i^1) for i in range(n-1)}
    c=make(n,bs,p,d,arcs)
    # Direct known optimum and canonical terminal; no full 2^17 subset oracle here.
    M=sum(1<<(2*i+1) for i in range(k)) | 1<<(n-1)
    stats,cs=explore(c,(Q(-1),M,1<<(n-1),None))
    assert stats['states']==2**k and stats['transitions']==k*2**(k-1)
    examples['eight_deletions']={'certificate':wire(cs[0]),'verification':v.verify(wire(cs[0])),
                                'exploration':stats,'orders':factorial(k)}
    base=examples['fractional_capacity']['certificate']
    mutations=[]
    def add(name, fn, b=None):
        c=deepcopy(base if b is None else b); fn(c); mutations.append((name,c))
    add('bool_version',lambda c:c.update(version=True))
    add('float_quota',lambda c:c['capacities'].__setitem__(1,0.75))
    add('negative_quota',lambda c:c['demands'].__setitem__(0,-1))
    add('bad_fraction',lambda c:c['demands'].__setitem__(0,'1/0'))
    add('duplicate_arc',lambda c:c['arcs'].append(c['arcs'][0]))
    add('loop',lambda c:c['arcs'].append([0,0]))
    add('bad_partition',lambda c:c.update(blocks=[[0],[0]]))
    add('wrong_terminal',lambda c:c.update(terminal=[0,1]))
    add('duplicate_terminal', lambda c:c.update(terminal=c['terminal']*2), examples['selected_low']['certificate'])
    add('truncated_deletions',lambda c:c.update(deletions=[]))
    add('invalid_endpoint',lambda c:c['deletions'][0].update(delete=2))
    add('no_maximum_flow',lambda c:c.update(flow=[]))
    add('flow_overload',lambda c:c['flow'][0].__setitem__(2,'1'))
    add('unsupported_flow',lambda c:c.update(flow=[[0,0,'1/2']]))
    add('duplicate_flow',lambda c:c['flow'].append(c['flow'][0]))
    add('nonneutral_deletion',lambda c:c['demands'].__setitem__(1,'1/2'))
    records=[]
    for name,c in mutations:
        try: v.verify(c)
        except v.Invalid as e: records.append({'case':name,'rejected':True,'reason':str(e)})
        else: raise AssertionError(('corrupt certificate accepted',name,c))
    write(out/'HOSTILE_RESULTS.json',{'examples':examples,'mutations':records,'rejected':len(records)})
    write(out/'DEMO_CERTIFICATE.json',base)
    print(json.dumps({'hostile_rejected':len(records),'examples':list(examples),'eight_deletions':stats}))


def order_tests(out):
    k,p=4,2; n=k+2; h=n-1
    arcs={(0,i) for i in range(1,k+1)}|{(i,0) for i in range(1,k+1)}
    arcs |= {(h,i) for i in range(n-1)}|{(i,h) for i in range(n-1)}
    B=[[int((i,j) in arcs) for j in range(n)] for i in range(n)]+[[1]*n]
    r=[1]*(n+1); c=[1]*(n-1)+[p]
    def rank(A,quota,cols): return sum(min(q,sum(row[j] for j in cols)) for row,q in zip(A,quota))
    original=[]; transpose=[]
    for rest in permutations(range(n-1)):
        order=(h,)+rest
        vals=[rank(B,r,order[:q])-sum(c[j] for j in order[:q]) for q in range(1,n+1)]
        assert min(vals)>=0
        original.append([order,vals])
    T=list(map(list,zip(*B)))
    for order in permutations(range(n+1)):
        vals=[rank(T,c,order[:q])-q for q in range(1,n+2)]
        fails=min(vals)<0
        assert fails == (set(order[:4])=={1,2,3,4})
        transpose.append([order,vals])
    fail=sum(min(row[1])<0 for row in transpose)
    assert len(original)==120 and fail==144 and len(transpose)==5040
    # A feasible dominant reference and one infeasible dominated target.
    # The general impossibility argument is supplied in COMPARISON.md.
    ref=[6,1,0,0,0,0]; bad=[2,1,1,1,1,1]
    assert all(sum(bad[:i])<=sum(ref[:i]) for i in range(1,7))
    record={'original_sorted_orders':120,'original_failing_orders':0,
            'transposed_orders':5040,'transposed_failing_orders':144,
            'transposed_passing_orders':4896,'deficient_subset':[1,2,3,4],
            'dominance_reference':ref,'infeasible_dominated_target':bad,
            'original_order_records_sha256':sha256(json.dumps(original,separators=(',',':')).encode()).hexdigest(),
            'transpose_order_records_sha256':sha256(json.dumps(transpose,separators=(',',':')).encode()).hexdigest(),
            'formula':'detection fraction = C(k,p+2)/C(k+p+1,p+2), k>=p+2, p>=2',
            'scope':'prefix/generalized-conjugate representation only; Chen premises not inspected'}
    write(out/'ORDER_RESULTS.json',record)
    print(json.dumps(record))


def limit_test(out):
    p,d,arcs=[0,2,1],[1,1,0],{(0,1),(0,2),(1,2)}
    c=make(3,[[0,1,2]],p,d,arcs)
    oracle=brute(3,[[0,1,2]],p,d,arcs)
    stats,certificates=explore(c,oracle)
    assert oracle[0]==0 and oracle[1]==7 and oracle[2]==6
    assert not certificates and stats=={'states':1,'transitions':0,'stuck':1}
    # Under the produced flow, 0_L -> 2_R has unused unit capacity and
    # 2_R -> 1_L is the reverse of a unit flow: hence 0 forces 1 in every min-cut.
    assert wire(c['flow'])==[[0,1,1],[1,2,1]]
    record={'instance':wire(c),
            'all_subsets':[{'set':[i for i in range(3) if row[0]>>i&1],
                            'H':row[1],'U':row[2],'F':row[3],'G':row[4]}
                           for row in oracle[3]],
            'exact_margin':str(oracle[0]),'greatest_exact_minimum':[0,1,2],
            'greatest_tight_minimum':[1,2],'local_exploration':stats,
            'certificate_found':False,
            'neutral_but_unlicensed_deletion':{'x':2,'y':1,'delete':0},
            'residual_implication_path':['0_L','2_R','1_L'],
            'missing_feature':'source 0 forces source 1 in every exact minimum; source 1 supplies the strict incoming-row difference'}
    write(out/'INCOMPLETENESS.json',record)
    print(json.dumps(record))


def main():
    if len(sys.argv)!=3 or sys.argv[2] not in ('integer','rational','hostile','orders','limits'):
        raise SystemExit(__doc__)
    out=Path(sys.argv[1]); out.mkdir(parents=True,exist_ok=True)
    mode=sys.argv[2]
    if mode in ('integer','rational'): exhaustive(out,mode)
    elif mode=='hostile': hostile(out)
    elif mode=='orders': order_tests(out)
    else: limit_test(out)


if __name__=='__main__': main()
