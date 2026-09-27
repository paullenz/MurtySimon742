#!/usr/bin/env python3
"""Targeted exact tests of new reductions, minimax boundary and certificates.
No dependencies, network, external solver, services or schedules.
"""
from __future__ import annotations
import argparse, copy, hashlib, itertools, json
from collections import deque
from pathlib import Path
from verify_certificate import verify


def dump(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n', encoding='utf-8')


def graph(n, mask):
    positions = [(u,w) for u in range(n) for w in range(n) if u != w]
    return frozenset(e for k,e in enumerate(positions) if mask >> k & 1)


def profile(P, d, layers, arcs):
    n = len(P); groups = [[w for w in range(n) if layers[w] == g] for g in sorted(set(layers))]
    rows = []
    for mask in range(1 << n):
        S = {u for u in range(n) if mask >> u & 1}
        y = [sum((u,w) in arcs for u in S) for w in range(n)]
        H = sum(min(p,z) for p,z in zip(P,y))
        U = sum(sum(min(p,z) for p,z in zip(sorted(P[w] for w in ids), sorted(y[w] for w in ids))) for ids in groups)
        D = sum(d[u] for u in S)
        rows.append((H-D, U-D, H, U, y))
    return rows


def hypotheses(P, d, layers, arcs):
    n = len(P)
    for x in range(n):
        for y in range(n):
            if layers[x] != layers[y] or P[x] >= P[y]:
                continue
            if d[x] < d[y] or ((y,x) in arcs and (x,y) not in arcs):
                return False
            for z in range(n):
                if z in (x,y):
                    continue
                if (z,x) in arcs and (z,y) not in arcs:
                    return False
                if (x,z) in arcs and (y,z) not in arcs:
                    return False
    return True


def flow(P, d, arcs):
    n = len(P); N = 2*n+2; s = 2*n; t = s+1
    residual = [[0]*N for _ in range(N)]
    for u in range(n):
        residual[s][u] = d[u]; residual[n+u][t] = P[u]
    for u,w in arcs:
        residual[u][n+w] = 1
    value = 0
    while True:
        parent = [-1]*N; parent[s] = s; queue = deque([s])
        while queue and parent[t] < 0:
            u = queue.popleft()
            for v,c in enumerate(residual[u]):
                if c and parent[v] < 0:
                    parent[v] = u; queue.append(v)
        if parent[t] < 0:
            break
        v = t; path = []
        while v != s:
            u = parent[v]; path.append((u,v)); v = u
        delta = min(residual[u][v] for u,v in path)
        for u,v in path:
            residual[u][v] -= delta; residual[v][u] += delta
        value += delta
    reaches = {t}; queue = deque([t])
    while queue:
        v = queue.popleft()
        for u in range(N):
            if residual[u][v] > 0 and u not in reaches:
                reaches.add(u); queue.append(u)
    M = sum(1 << u for u in range(n) if u not in reaches)
    used = sorted((u,w) for u,w in arcs if residual[u][n+w] == 0)
    assert len(used) == value
    return value, M, used


def capacity_permutations(P, layers):
    groups = [[w for w in range(len(P)) if layers[w] == g] for g in sorted(set(layers))]
    choices = [sorted(set(itertools.permutations(P[w] for w in ids))) for ids in groups]
    for values in itertools.product(*choices):
        Q = list(P)
        for ids, vals in zip(groups, values):
            for w, val in zip(ids, vals):
                Q[w] = val
        yield Q


def make_certificate(P, d, layers, arcs):
    value, M, used = flow(P, d, arcs)
    rows = profile(P,d,layers,arcs); gamma = value-sum(d)
    minimizers = [s for s,row in enumerate(rows) if row[0] == gamma]
    union = 0
    for s in minimizers:
        union |= s
    assert M == union and gamma == min(row[0] for row in rows)
    S = M; trace = []
    while rows[S][2] != rows[S][3]:
        yv = rows[S][4]
        choices = [(x,y) for x in range(len(P)) for y in range(len(P))
                   if layers[x] == layers[y] and max(P[x],yv[y]) < min(P[y],yv[x])]
        assert choices
        x,y = choices[0]
        assert not (M >> x & 1) and (S >> y & 1)
        trace.append([x,y]); S &= ~(1 << y)
        assert rows[S][0] == gamma
    cert = {'schema':'hall-saddle-v1', 'P':list(P), 'd':list(d), 'layers':list(layers),
            'arcs':[list(e) for e in sorted(arcs)], 'flow':[list(e) for e in used],
            'source_set':[u for u in range(len(P)) if S >> u & 1], 'claimed_flow_value':value}
    verify(cert)
    return cert, trace, rows


def test_small():
    counts = {'instances':0, 'capacity_placements':0, 'payoff_entries':0, 'deletions':0,
              'nontrivial_flow_deficiencies':0}
    digest = hashlib.sha256(); example = None
    n = 3
    for layers in ((0,0,0),(0,0,1)):
        for P in itertools.product(range(3), repeat=n):
            for gm in range(1 << (n*(n-1))):
                arcs = graph(n,gm)
                for d in itertools.product(range(3), repeat=n):
                    if not hypotheses(P,d,layers,arcs):
                        continue
                    cert, trace, rows = make_certificate(P,d,layers,arcs)
                    gamma = min(row[0] for row in rows); upper = min(row[1] for row in rows)
                    assert gamma == upper
                    worst = []; envelope = [-10**9]*len(rows)
                    S = sum(1 << u for u in cert['source_set'])
                    for Q in capacity_permutations(P,layers):
                        qrows = profile(Q,d,layers,arcs); gq = min(r[0] for r in qrows)
                        assert gq <= gamma and qrows[S][0] <= gamma
                        worst.append(gq)
                        envelope = [max(a,b[0]) for a,b in zip(envelope,qrows)]
                        counts['capacity_placements'] += 1; counts['payoff_entries'] += len(rows)
                    assert max(worst) == gamma
                    assert envelope == [row[1] for row in rows]
                    counts['instances'] += 1; counts['deletions'] += len(trace)
                    nontrivial = cert['claimed_flow_value'] < min(sum(P),sum(d))
                    counts['nontrivial_flow_deficiencies'] += nontrivial
                    if example is None and nontrivial and min(worst)<gamma and cert['claimed_flow_value']>0:
                        example = cert
                    digest.update(json.dumps([layers,P,gm,d,gamma,trace,worst], separators=(',',':')).encode()+b'\n')
    return counts,digest.hexdigest(),example


def test_dummy():
    count = 0; entries = 0; preserved = 0
    for layers in ((0,0),(0,1)):
        for P in itertools.product(range(3),repeat=2):
            for d in itertools.product(range(3),repeat=2):
                for gm in range(4):
                    arcs = graph(2,gm); old = profile(P,d,layers,arcs)
                    gh = min(r[0] for r in old); gu = min(r[1] for r in old)
                    for q in range(4):
                        Q = P+(1,)*q; dd = d+(0,)*q; ll = layers+(max(layers)+1,)*q
                        aa = arcs | frozenset((u,w) for u in range(2) for w in range(2,2+q))
                        new = profile(Q,dd,ll,aa)
                        assert min(r[0] for r in new) == min(0,gh+q)
                        assert min(r[1] for r in new) == min(0,gu+q)
                        for s,row in enumerate(new):
                            original = s & 3; offset = q if original else 0
                            assert row[:2] == tuple(old[original][j]+offset for j in (0,1))
                        if hypotheses(P,d,layers,arcs):
                            assert hypotheses(Q,dd,ll,aa); preserved += 1
                        count += 1; entries += len(new)
    return {'augmented_instances':count,'source_subset_entries':entries,'hypothesis_preservations':preserved}


def test_padding():
    """Compare original feasible flows with exhaustive padded-matrix search.
    Matrix search stops at the first witness, or exhausts every binary matrix.
    """
    instances=0; feasible=0; matrices=0
    for P in itertools.product(range(3),repeat=2):
        for d in itertools.product(range(3),repeat=2):
            for gm in range(4):
                arcs=graph(2,gm); edges=sorted(arcs)
                possible=[]
                for bits in range(1 << len(edges)):
                    used=[e for k,e in enumerate(edges) if bits >> k & 1]
                    rr=[sum(u==i for u,w in used) for i in range(2)]
                    cc=[sum(w==j for u,w in used) for j in range(2)]
                    if all(rr[i]<=d[i] and cc[i]<=P[i] for i in range(2)):
                        possible.append((used,rr,cc))
                maximum=max(len(u) for u,r,c in possible)
                assert flow(P,d,arcs)[0]==maximum
                for target in range(min(sum(P),sum(d))+1):
                    A=sum(d)-target; B=sum(P)-target; instances+=1
                    witnesses=[z for z in possible if len(z[0])==target]
                    assert bool(witnesses)==(target<=maximum)
                    if witnesses:feasible+=1
                    # Enumerate padded matrices until a witness or complete exhaustion.
                    allowed=edges+[(i,j) for i in range(2) for j in range(2,2+A)]+[(i,j) for i in range(2,2+B) for j in range(2)]
                    targetr=list(d)+[1]*B; targetc=list(P)+[1]*A
                    exists=False
                    for bits in range(1 << len(allowed)):
                        matrices+=1
                        rr=[0]*(2+B); cc=[0]*(2+A)
                        for k,(i,j) in enumerate(allowed):
                            if bits >> k & 1:rr[i]+=1;cc[j]+=1
                        if rr==targetr and cc==targetc:exists=True;break
                    assert exists==bool(witnesses)
    return {'threshold_instances':instances,'feasible_thresholds':feasible,'padded_matrices_examined':matrices}


def fano_example():
    n=7; lines=[{j,(j+1)%7,(j+3)%7} for j in range(7)]
    assert all(len(a&b)==1 for a,b in itertools.combinations(lines,2))
    arcs=frozenset((u,w) for u in range(n) for w in range(n) if u not in lines[w])
    assert all((u,u) not in arcs for u in range(n))
    assert all(sum((u,w) in arcs for w in range(n))==4 for u in range(n))
    d=(1,)*n; layers=(0,)*n; P=(4,4,0,0,0,0,0)
    tables=[]; minima=[]; optimal=0
    for Q in capacity_permutations(P,layers):
        rows=profile(Q,d,layers,arcs); value,_,used=flow(Q,d,arcs)
        assert value==6 and min(r[0] for r in rows)==-1 and min(r[1] for r in rows)==0
        assert not hypotheses(Q,d,layers,arcs)
        active=[w for w,p in enumerate(Q) if p]
        missing=sorted(lines[active[0]]&lines[active[1]])
        assert len(missing)==1
        tables.append({'P':Q,'flow_value':value,'flow':[list(e) for e in used],
                       'uncovered_source':missing[0], 'minimum_H_margin':-1,
                       'H_margins':[r[0] for r in rows]})
        minima.append(min(r[0] for r in rows));optimal+=1
    base=profile(P,d,layers,arcs)
    return {'lines':[sorted(z) for z in lines], 'arcs':[list(e) for e in sorted(arcs)],
            'd':list(d),'layers':list(layers), 'capacity_multiset':list(P),
            'capacity_placements':optimal,'source_subsets_per_placement':128,
            'max_min_margin':max(minima),'min_max_margin':min(r[1] for r in base),
            'U_margins':[r[1] for r in base], 'placements':tables,
            'scope':'counterexample to unrestricted minimax, NOT to Theorem A'}


def prefix_example():
    P=(1,1,1,1);d=P;layers=(0,0,0,0)
    arcs=frozenset([(0,i) for i in (1,2,3)]+[(i,0) for i in (1,2,3)])
    rows=profile(P,d,layers,arcs)
    assert hypotheses(P,d,layers,arcs)
    assert [rows[(1<<k)-1][0] for k in range(1,5)]==[2,2,1,0]
    assert rows[14][0]==-2 and flow(P,d,arcs)[0]==2
    return {'P':list(P),'d':list(d),'layers':list(layers),'arcs':[list(e) for e in sorted(arcs)],
            'prefix_H_margins':[2,2,1,0],'obstruction_source_set':[1,2,3],
            'obstruction_margin':-2,'fixed_support_flow':2,'complete_off_diagonal_flow':4}


def test_rejection(cert):
    cases=[]
    def bad(name,modify):
        c=copy.deepcopy(cert);modify(c)
        try:verify(c)
        except (ValueError,TypeError,KeyError):cases.append(name);return
        raise AssertionError('Accepted corruption: '+name)
    bad('wrong_value',lambda c:c.__setitem__('claimed_flow_value',-1))
    bad('duplicate_arc',lambda c:c['arcs'].append(c['arcs'][0]))
    bad('duplicate_flow',lambda c:c['flow'].append(c['flow'][0]))
    bad('forbidden_loop',lambda c:c['flow'].append([0,0]))
    bad('boolean_capacity',lambda c:c['P'].__setitem__(0,True))
    bad('negative_demand',lambda c:c['d'].__setitem__(0,-1))
    bad('dimension',lambda c:c['layers'].append(0))
    bad('unknown_schema',lambda c:c.__setitem__('schema','untrusted'))
    bad('unknown_field',lambda c:c.__setitem__('unchecked','value'))
    bad('missing_field',lambda c:c.pop('flow'))
    bad('bad_cut_index',lambda c:c['source_set'].append(len(c['P'])))
    bad('wrong_cut',lambda c:c.__setitem__('source_set',[]))
    bad('out_of_range_edge',lambda c:c['arcs'].append([0,len(c['P'])]))
    bad('flow_removed',lambda c:c['flow'].pop())
    bad('duplicate_source',lambda c:c['source_set'].append(c['source_set'][0]))
    used_u,used_w=cert['flow'][0]
    bad('source_capacity_exceeded',lambda c:c['d'].__setitem__(used_u,0))
    bad('receiver_capacity_exceeded',lambda c:c['P'].__setitem__(used_w,0))
    bad('flow_outside_support',lambda c:c['arcs'].remove([used_u,used_w]))
    # This is a valid optimal primal-dual flow/cut pair, but its exact cut has H<U.
    # It must be rejected for the mathematical reason, not malformed input.
    gap={'schema':'hall-saddle-v1','P':[0,1],'d':[1,1],'layers':[0,0],
         'arcs':[[0,1],[1,0]],'flow':[[0,1]],'source_set':[1],'claimed_flow_value':1}
    try:verify(gap)
    except ValueError as error:
        assert str(error)=='cut has a rearrangement gap'
        cases.append('optimal_cut_but_positive_rearrangement_gap')
    else:raise AssertionError('Accepted a positive rearrangement gap')
    return cases


def proper_cut_example():
    P=(0,1,3);d=(1,1,2);layers=(0,0,1)
    arcs=frozenset([(0,1),(1,0),(0,2),(1,2),(2,1)])
    assert hypotheses(P,d,layers,arcs)
    cert,trace,_=make_certificate(P,d,layers,arcs)
    assert cert['claimed_flow_value']==3
    # A smaller common saddle cut is the singleton source 2.
    cert['source_set']=[2]
    assert verify(cert)['minimum_margin']==-1
    swapped=flow((1,0,3),d,arcs)[0]
    assert swapped==2
    return cert, {'original_flow':3,'swapped_flow':2,'common_cut':[2],
                  'original_margin':-1,'swapped_margin_at_common_cut':-2}



def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--part',choices=('core','padding'),default='core');args=ap.parse_args()
    if not __debug__:ap.error('Assertions must be enabled; do not use -O.')
    args.output.mkdir(parents=True,exist_ok=True)
    if args.part=='padding':
        result={'status':'PASS','padding':test_padding()}
    else:
        counts,digest,cert=test_small();assert cert is not None
        fano=fano_example();prefix=prefix_example()
        dump(args.output/'FANO_COUNTEREXAMPLE.json',fano)
        dump(args.output/'CERTIFICATE.json',cert)
        proper,proper_result=proper_cut_example()
        dump(args.output/'PROPER_CUT_CERTIFICATE.json',proper)
        result={'status':'PASS','domain':{'n':3,'P_and_d_values':[0,1,2],'layers':[[0,0,0],[0,0,1]],
                'graphs':'all 64 labelled loopless directed supports; all Theorem A eligible instances'},
                'saddle_checks':counts,'ordered_record_sha256':digest,'dummy':test_dummy(),
                'fano':{'placements':21,'subsets_per_placement':128,'max_min_margin':-1,'min_max_margin':0},
                'prefix_counterexample':prefix, 'rejected_corruptions':test_rejection(cert),
                'certificate_result':verify(cert), 'proper_cut_example':proper_result}
    result['source_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),Path(__file__).with_name('verify_certificate.py'))}
    dump(args.output/('RESULTS.json' if args.part=='core' else 'PADDING_RESULTS.json'),result)
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
