#!/usr/bin/env python3
"""Standard-library verification of all saved certificates and witnesses.

Does not import either discovery model, SciPy, NumPy, or the earlier pair
checker. Reconstructs the frozen input and all acceptance arithmetic.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations,product
from collections import Counter
import base64,gzip,hashlib,json,math

HERE=Path(__file__).resolve().parent
PREV=HERE.parent/'2026-09-13-constraint-respecting-cross-v1'
CAT=HERE.parent/'2026-09-12-compatible-routing-catalogue-v1'
F=Fraction

def load(name):return json.loads((HERE/name).read_text())
def pool():
    meta=json.loads((CAT/'EVIDENCE_STORAGE.json').read_text())['files']['pool_inputs.jsonl']
    stored=(CAT/meta['stored_file']).read_bytes()
    assert hashlib.sha256(stored).hexdigest()==meta['stored_sha256']
    raw=gzip.decompress(base64.b64decode(stored))
    assert hashlib.sha256(raw).hexdigest()==meta['original_sha256']
    return {(x['layer'],x['state_id']):x for x in map(json.loads,raw.splitlines())}

def inputs():
    P=pool();full=json.loads((PREV/'FULL_DOMAIN_SPILL_EXACT.json').read_text())
    prior=json.loads((PREV/'PAIR_OVERLAP_CHECK.json').read_text())
    switches={(x['layer'],x['state_id']):x['switches'] for x in prior['pair_repairs']}
    out={}
    for w in full['witnesses']:
        key=w['layer'],w['state_id'];rec=P[key];S=[set(row) for row in w['selected']]
        for u,v,i,j in switches.get(key,[]):
            assert i in S[u]-S[v] and j in S[v]-S[u]
            assert rec['rho'][u]>=rec['s'][j] and rec['rho'][v]>=rec['s'][i]
            S[u]^={i,j};S[v]^={i,j}
        assert [len(row) for row in S]==w['q']
        assert [sum(i in row for row in S) for i in range(rec['a'])]==rec['s']
        assert key not in out;out[key]=(rec,S)
    assert len(out)==4584
    return out,{(x['layer'],x['state_id']) for x in prior['local_residual_cover_failures']}

def data(rec,S):
    a,b=rec['a'],rec['b'];q=[len(v) for v in S];x=[sum(i in row for row in S) for i in range(a)]
    r=sum(rec['rho']);E=sum(rec['s'])-r-2*rec['t']
    assert E>=0 and rec['t']>0 and b>a-1-rec['t']
    L=[max([0]+[q[u]-x[i] for u in range(b) if i in S[u]]) for i in range(a)]
    U=[min(b-x[i],a-2-rec['s'][i]+(E if rec['s'][i]==0 else 0)) for i in range(a)]
    h=[min(rec['rho'][u]+b-a-1,b-1-q[u]) for u in range(b)]
    assert sum(L)<=r<=sum(U) and all(0<=L[i]<=U[i] for i in range(a))
    return a,b,q,x,r,L,U,h

def price(v,L,U,r):
    allocated=list(L);left=r-sum(L)
    for i in sorted(range(len(v)),key=lambda i:(v[i],-i),reverse=True):
        add=min(U[i]-allocated[i],left);allocated[i]+=add;left-=add
    assert left==0
    return sum((v[i]*allocated[i] for i in range(len(v))),F(0))

def deficits(S,a):
    out={}
    for i,j in combinations(range(a),2):
        rows=[row for row in S if i in row and j in row]
        need=max([0]+[len(row)-1 for row in rows])-len(rows)
        if need>0:out[i,j]=need
    return out

def endpoint(rec,S,item):
    a,b,q,x,r,L,U,h=data(rec,S);c=item['certificate']
    A={(u,i):F(v) for u,i,v in c['alpha']};B=list(map(F,c['beta']))
    assert len(A)==len(c['alpha']) and len(B)==b
    assert all(i in S[u] and v>=0 for (u,i),v in A.items()) and all(v>=0 for v in B)
    assert all(B[u]+sum((A.get((u,i),F(0)) for i in S[u]),F(0))>=1 for u in range(b))
    weights=[sum((v for (u,j),v in A.items() if j==i),F(0)) for i in range(a)]
    rhs=sum((B[u]*h[u] for u in range(b)),F(0))+sum((v*(x[i]-q[u]) for (u,i),v in A.items()),F(0))+price(weights,L,U,r)
    assert F(item['exact_upper_bound'])==rhs and F(item['exact_gap'])==sum(q)-rhs>0

def balanced(rec,S,item):
    a,b,q,x,r,L,U,h=data(rec,S);m=sum(v>0 for v in q);c=sum(v>0 for v in x);Q=sum(q);H0=sum(h[u] for u in range(b) if not q[u])
    gap=(2*c-m)*Q-c*H0-m*r
    assert item['integer_bound_gap']==gap
    if item['balanced']:
        cert=item['integer_cover'];assert all(isinstance(v,int) and v>0 and i in S[u] for u,i,v in cert)
        assert len({(u,i) for u,i,v in cert})==len(cert)
        assert all(sum(v for u0,i,v in cert if u0==u)==c for u in range(b) if q[u])
        assert all(sum(v for u,i0,v in cert if i0==i)==m for i in range(a) if x[i])
        assert item['exact_pattern_exclusion']==(gap>0)
    else:
        T=item['concentrated_sources'];I=set(item['concentrated_labels'])
        assert len(T)==len(set(T)) and all(q[u]>0 and S[u]<=I for u in T)
        assert c*len(T)>m*len(I) and not item['exact_pattern_exclusion']

def combined(rec,S,item):
    a,b,q,x,r,L,U,h=data(rec,S);D=deficits(S,a);c=item['certificate']
    W={(i,j):F(v) for i,j,v in c['pair_weights']};A={(u,i):F(v) for u,i,v in c['endpoint_weights']};V=list(map(F,c['residual_prices']));mu=F(c['incoming_multiplier'])
    assert all(e in D and v>=0 for e,v in W.items()) and all(i in S[u] and v>=0 for (u,i),v in A.items())
    assert len(V)==a and len(W)==len(c['pair_weights']) and len(A)==len(c['endpoint_weights'])
    # Use one exact integer scale for an independently structured local maximization.
    den=math.lcm(*(v.denominator for v in list(W.values())+list(A.values())+V+[mu]))
    wi={e:int(v*den) for e,v in W.items()};ai={e:int(v*den) for e,v in A.items()};vi=[int(v*den) for v in V];mi=int(mu*den)
    lam=[sum(v for (u,j),v in ai.items() if j==i) for i in range(a)]
    mass=[sum(v for (u0,i),v in ai.items() if u0==u) for u in range(b)]
    maxima=[]
    for u in range(b):
        best=None
        for R in combinations([i for i in range(a) if i not in S[u]],rec['rho'][u]):
            N=S[u]|set(R)
            v=sum(value for (i,j),value in wi.items() if i in N and j in N and not(i in S[u] and j in S[u]))+sum(lam[i]-vi[i] for i in R)
            best=v if best is None else max(best,v)
        maxima.append(best)
    lhs=sum(v*D[e] for e,v in wi.items())+mi*sum(q)
    rhs=sum(maxima)+price(vi,L,U,r)+sum(v*(x[i]-q[u]) for (u,i),v in ai.items())+sum(h[u]*max(0,mi-mass[u]) for u in range(b))
    assert F(lhs-rhs,den)==F(item['exact_gap'])>0
    assert F(lhs,den)==F(item['exact_lhs']) and F(rhs,den)==F(item['exact_rhs'])
    assert [str(F(v,den)) for v in maxima]==c['local_maxima']

def fractional(rec,S,item,pairs):
    a,b,q,x,r,L,U,h=data(rec,S);w=item['exact_fractional_witness'];p=list(map(F,w['incoming']))
    configs=[(u,set(R),F(v)) for u,R,v in w['configurations']]
    assert len(p)==b and sum(p)==sum(q) and all(0<=p[u]<=h[u] for u in range(b))
    assert all(v>=0 and len(R)==rec['rho'][u] and not(R&S[u]) and R<=set(range(a)) for u,R,v in configs)
    assert all(sum((v for u0,R,v in configs if u0==u),F(0))==1 for u in range(b))
    rd=[sum((v for u,R,v in configs if i in R),F(0)) for i in range(a)]
    assert sum(rd)==r and all(L[i]<=rd[i]<=U[i] for i in range(a))
    assert all(p[u]<=rd[i]+x[i]-q[u] for u in range(b) for i in S[u])
    if pairs:
        for (i,j),need in deficits(S,a).items():
            have=sum((v for u,R,v in configs if i in S[u]|R and j in S[u]|R and not(i in S[u] and j in S[u])),F(0))
            assert have>=need

def tiny_challenge():
    # Every selected/residual/absent assignment on a=2,b=3: 3^6=729.
    # Accept only actual row placements with sufficient endpoint/incoming and
    # pair capacity, then challenge the signed-price inequality directly.
    checked=0;positive_pair_checks=0;cases=[]
    for trits in product(range(3),repeat=6):
        a,b=2,3;S=[{i for i in range(a) if trits[a*u+i]==1} for u in range(b)];R=[{i for i in range(a) if trits[a*u+i]==2} for u in range(b)]
        cases.append((a,b,S,R))
    # Positive pair deficits: one three-label selected source and three
    # residual rows. Enumerate all 27 choices of two-label residual rows.
    for rows in product(list(combinations(range(3),2)),repeat=3):
        cases.append((3,4,[{0,1,2},set(),set(),set()],[set()]+[set(v) for v in rows]))
    for a,b,S,R in cases:
        q=list(map(len,S));Q=sum(q)
        if not Q:continue
        x=[sum(i in row for row in S) for i in range(a)];rd=[sum(i in row for row in R) for i in range(a)];rho=list(map(len,R));r=sum(rho)
        h=[min(rho[u]+b-a-1,b-1-q[u]) for u in range(b)]
        caps=[min([h[u]]+[rd[i]+x[i]-q[u] for i in S[u]]) for u in range(b)]
        if min(caps)<0 or sum(caps)<Q:continue
        D=deficits(S,a)
        if any(sum(i in S[u]|R[u] and j in S[u]|R[u] and not(i in S[u] and j in S[u]) for u in range(b))<d for (i,j),d in D.items()):continue
        L=[max([0]+[q[u]-x[i] for u in range(b) if i in S[u]]) for i in range(a)];U=[b-x[i] for i in range(a)]
        for trial in range(4):
            A={(u,i):(u+i+trial)%3 for u in range(b) for i in S[u]};W={e:1+(sum(e)+trial)%3 for e in D};V=[(trial+i)%5-2 for i in range(a)];mu=trial-1
            lam=[sum(v for (u,j),v in A.items() if i==j) for i in range(a)];mass=[sum(v for (v0,i),v in A.items() if u==v0) for u in range(b)]
            C=[]
            for u in range(b):
                C.append(max(sum(v for (i,j),v in W.items() if i in S[u]|set(T) and j in S[u]|set(T) and not(i in S[u] and j in S[u]))+sum(lam[i]-V[i] for i in T) for T in combinations([i for i in range(a) if i not in S[u]],rho[u])))
            lhs=sum(W[e]*d for e,d in D.items())+mu*Q
            rhs=sum(C)+price(V,L,U,r)+sum(v*(x[i]-q[u]) for (u,i),v in A.items())+sum(h[u]*max(0,mu-mass[u]) for u in range(b))
            assert lhs<=rhs
            checked+=1
            positive_pair_checks+=bool(D)
    return {'cross_assignments_enumerated':len(cases),'valid_placement_weight_checks':checked,'positive_pair_deficit_checks':positive_pair_checks,'scope':'Abstract necessary-condition data, not a D2C graph enumeration.'}

def main():
    P,oldfail=inputs();A=load('ENDPOINT_CONTROL.json');B=load('BALANCED_COVER.json');C=load('SHARED_PAIR.json')
    ea=set();ba=set();pc=set();pa=set();fc=fp=0
    for doc in (A,B):assert len(doc['records'])==len(P) and {(v['layer'],v['state_id']) for v in doc['records']}==set(P)
    for item in A['records']:
        key=item['layer'],item['state_id']
        if item.get('exact_pattern_exclusion'):endpoint(*P[key],item);ea.add(key)
    for item in B['records']:
        key=item['layer'],item['state_id'];balanced(*P[key],item)
        if item['exact_pattern_exclusion']:ba.add(key)
    assert ba<=ea and oldfail<=ea
    assert {(v['layer'],v['state_id']) for v in C['records']}==set(P)-ea
    for item in C['records']:
        key=item['layer'],item['state_id'];control=item['placement_control']
        if control.get('exact_pattern_exclusion'):combined(*P[key],control);pc.add(key);assert 'shared_pair' not in item
        else:
            fractional(*P[key],control,False);fc+=1;pair=item['shared_pair']
            if pair.get('exact_pattern_exclusion'):combined(*P[key],pair);pa.add(key)
            else:fractional(*P[key],pair,True);fp+=1
    assert (len(ea),len(ba),len(pc),len(pa),fc,fp)==(4449,1871,13,25,122,97)
    compact=load('COMPACT_CERTIFICATES.json')['records']
    assert len(compact)==38 and {(x['layer'],x['state_id']) for x in compact}==pc|pa
    for item in compact:combined(*P[item['layer'],item['state_id']],item)
    solo=load('PAIR_ONLY_CONTROL.json')['records'];solo_negative=joint_only=0
    assert len(solo)==25 and {(x['layer'],x['state_id']) for x in solo}==pa
    for item in solo:
        rec,S=P[item['layer'],item['state_id']]
        if item.get('exact_pattern_exclusion'):
            combined(rec,S,item);solo_negative+=1
        else:
            z=[(u,set(R),F(v)) for u,R,v in item['exact_pair_only_fractional_witness']]
            assert all(v>=0 and len(R)==rec['rho'][u] and not(R&S[u]) and R<=set(range(rec['a'])) for u,R,v in z)
            assert all(sum((v for u0,R,v in z if u0==u),F(0))==1 for u in range(rec['b']))
            for (i,j),need in deficits(S,rec['a']).items():
                assert sum((v for u,R,v in z if i in S[u]|R and j in S[u]|R and not(i in S[u] and j in S[u])),F(0))>=need
            joint_only+=1
    assert (solo_negative,joint_only)==(3,22)
    report={'status':'PASS','date':'2026-09-13','verifier':'Python standard library; discovery modules and solvers not imported','patterns':len(P),'endpoint_certificates':len(ea),'balanced_short_certificates':len(ba),'concentration_witnesses':sum(not x['balanced'] for x in B['records']),'additional_placement_certificates':len(pc),'additional_pair_certificates':len(pa),'exact_control_fractional_witnesses':fc,'exact_pair_fractional_witnesses':fp,'combined_fixed_pattern_exclusions':len(ea|pc|pa),'whole_state_exclusions':0,'generalisation_frontier_survivors':4584,'tiny_challenge':tiny_challenge()}
    report.update(integer_compressed_certificates=len(compact),weighted_pair_only_exclusions=solo_negative,joint_exclusions_with_both_controls_separately_feasible=joint_only)
    report['input_sha256']={name:hashlib.sha256((PREV/name).read_bytes()).hexdigest() for name in ('FULL_DOMAIN_SPILL_EXACT.json','PAIR_OVERLAP_CHECK.json')}
    (HERE/'VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
