#!/usr/bin/env python3
"""Independent finite necessary-code replay; never substitutes for a graph proof."""
from itertools import product, combinations
from pathlib import Path
import json

B=range(8)
Q={s:{s^(1<<i) for i in range(3)} for s in B}
CODES={**{f'C{i}{e}':frozenset(s for s in B if (s>>i)&1==e) for i in range(3) for e in range(2)},
       **{f'P{e}':frozenset(s for s in B if s.bit_count()%2==e) for e in range(2)},
       **{f'S{c}':frozenset({c}|Q[c]) for c in B}}
ALL=frozenset(B)
UNDOM={k:ALL-(h|frozenset().union(*(Q[s] for s in h))) for k,h in CODES.items()}

def relation(stars, affine=None):
    """Overapproximate every possible A-edge for the given code support.

    Copies are unbounded, uniqueness restrictions are discarded. Hence every
    actual graph edge survives; removal is a necessary obstruction only.
    """
    names=sorted((set(CODES)-{f'S{x}' for x in B} if affine is None else set(affine))|{f'S{x}' for x in stars})
    R={(h,k) for h in names for k in names}
    trace=[]
    def ab_ok(h,k,rel):
        H,K=CODES[h],CODES[k]
        for s in H:
            # Direct endpoint certificate, not killed by the given A-neighbour.
            if not(Q[s]&H) and s not in K:continue
            # A-to-B length-two certificate through the deleted spoke.
            if any(t not in H and Q[t]&H=={s} and t not in K for t in Q[s]):continue
            # A-side target. A distinct copy can exist even when code equals k.
            if any(H&CODES[l]=={s} for l in names):continue
            # B-side target through an A-neighbour of the source.
            if any(not(CODES[l]&({s}|Q[s])) and (h,l) in rel for l in names):continue
            return False
        return True
    def aa_side(h,k,rel):
        if not(CODES[h]&CODES[k]):return True
        if UNDOM[h]&CODES[k]:return True
        return any(not(CODES[h]&CODES[l]) and (k,l) in rel for l in names)
    while True:
        removed=[]
        for h,k in sorted(R):
            if not(ab_ok(h,k,R) and ab_ok(k,h,R)):removed.append((h,k,'A-B criticality'))
            elif not(aa_side(h,k,R) or aa_side(k,h,R)):removed.append((h,k,'A-A criticality'))
        if not removed:break
        trace.append(removed)
        R-=set((h,k) for h,k,_ in removed)
    no_bridge=[]
    for h in names:
        for t in UNDOM[h]:
            if not any((h,k) in R and t in CODES[k] for k in names):no_bridge.append((h,t))
    incompatible=[]
    for h,k in combinations(names,2):
        if CODES[h]&CODES[k]:continue
        if (h,k) in R:continue
        if not any((h,l) in R and (k,l) in R for l in names):incompatible.append((h,k))
    return {'stars':list(stars),'names':names,'allowed_pairs':[(h,k) for h,k in sorted(R) if h<=k],
            'rounds':trace,'no_antipode_bridge':no_bridge,'diameter_incompatible_codes':incompatible}

def graph(codes, aedges):
    n=9+len(codes);adj=[set() for _ in range(n)]
    def add(x,y):adj[x].add(y);adj[y].add(x)
    for b in B:add(8,b)
    for b in B:
        for c in Q[b]:
            if b<c:add(b,c)
    for i,k in enumerate(codes):
        for b in CODES[k]:add(9+i,b)
    for i,j in aedges:add(9+i,9+j)
    return adj

def d2c(adj):
    n=len(adj)
    def diameter_two():return all(j in adj[i] or adj[i]&adj[j] for i in range(n) for j in range(i+1,n))
    if not diameter_two():return False
    for i in range(n):
        for j in sorted(adj[i]):
            if i>=j:continue
            adj[i].remove(j);adj[j].remove(i)
            critical=not diameter_two()
            adj[i].add(j);adj[j].add(i)
            if not critical:return False
    return True

def main():
    transversals={frozenset(choice) for choice in product(*[(i,i^7) for i in range(4)])}
    assert transversals==set(CODES.values()) and len(transversals)==16
    for h,H in CODES.items():
        assert sum(not(H&K) for K in CODES.values())==1
    controls=[]
    for p,q in product(range(4),repeat=2):
        codes=['C00','C10','C20']+['P0']*p+['P1']*q
        aedges=[(3+i,3+p+j) for i in range(p) for j in range(q)]
        adj=graph(codes,aedges)
        assert d2c(adj),(p,q)
        controls.append({'p':p,'q':q,'n':len(adj),'m':sum(map(len,adj))//2,'d2c':True})
    x3=graph(['C00','C10','C20'],[])
    assert len(x3)==12 and sum(map(len,x3))//2==32
    bad=graph(['C00','C10','C20'],[(0,1)])
    assert not d2c(bad)
    antipodal=[relation((c,c^7)) for c in range(4)]
    for r in antipodal:
        assert all(not(h.startswith('C') or k.startswith('C')) for h,k in r['allowed_pairs'])
        assert len([p for p in r['diameter_incompatible_codes'] if p[0][0]=='C' and p[1][0]=='C'])==3
    singles=[relation((c,)) for c in B]
    assert all(r['no_antipode_bridge'] for r in singles)
    def summary(r):
        return {**{k:v for k,v in r.items() if k!='rounds'},'elimination_round_sizes':[len(t) for t in r['rounds']]}
    output={'description':'Necessary code-relation replay, not enumeration of all graphs',
            'antipodal_pairs':[summary(r) for r in antipodal],'single_centres':[summary(r) for r in singles],'graph_controls':controls,
            'negative_control_added_coordinate_edge_rejected':True,
            'two_centre_distances':{str(d):summary(relation((0,(1<<d)-1))) for d in (1,2,3)}}
    path=Path(__file__).with_name('STAR_SUPPORT_CHECK_RESULTS.json')
    path.write_text(json.dumps(output,indent=2)+'\n')
    print('PASS: 16-code identities, four antipodal supports, eight single supports, 16 raw D2C controls, one negative control')
    for d,r in output['two_centre_distances'].items():
        print('distance',d,'allowed pairs',r['allowed_pairs'],'unbridgeable',r['no_antipode_bridge'])

if __name__=='__main__':main()
