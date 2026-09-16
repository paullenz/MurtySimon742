#!/usr/bin/env python3
"""Deterministic local graph, support-charge and tight-graph envelope checks.
Python 3.10+ and g++ with C++17. No network or third-party Python package.
All tests are local lemmas/relaxations, not canonical exact-block graph censuses.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json, pathlib, subprocess
from collections import Counter


def tight(d: int, mask: int) -> list[int]:
    a=[0]*d
    for bit,(i,j) in enumerate(itertools.combinations(range(d),2)):
        if mask>>bit&1: a[i]|=1<<j; a[j]|=1<<i
    return a


def reach(a: list[int]) -> list[int]:
    out=[]
    for i,ns in enumerate(a):
        r=ns | (1<<i)
        while ns:
            bit=ns & -ns; r|=a[bit.bit_length()-1]; ns^=bit
        out.append(r)
    return out


def graph_decision(d: int, km: int, vm: int, t: int, s: int, a: list[int]) -> tuple[int,int,int,int,int,str]:
    n=len(a); tm=(1<<d)-1
    pc=int(all(a[i]&a[j]&km for i in range(d) for j in range(i+1,d)))
    pp=1
    for v in range(d,n):
        if vm>>v&1:
            sup=a[v]&tm
            if sup.bit_count()!=1: pp=0; continue
            label=sup.bit_length()-1
            if (a[label]&km)&~a[v]: pp=0
    threat=0
    for x in range(d,n):
        if vm>>x&1: continue
        sup=a[x]&tm
        for u,v in ((t,s),(s,t)):
            if not(sup>>u&1) and sup>>v&1 and a[u]&sup&tm==(1<<v): threat=1
    before=reach(a); b=a.copy(); b[t]&=~(1<<s); b[s]&=~(1<<t); after=reach(b)
    lost=''.join('1' if before[i]>>j&1 and not(after[i]>>j&1) else '0' for i in range(n) for j in range(i+1,n))
    dia=int(all(x==(1<<n)-1 for x in before))
    return pc,pp,threat,dia,lost.count('1'),lost


def build_graph(d: int, q: int, covers: list[int], sx: int, kx: int, vx: int) -> tuple[list[int],int,int]:
    k=len(covers); v=d+k; x=v+1; n=x+1; a=tight(d,q)+[0]*(k+2)
    def edge(i: int,j: int) -> None: a[i]|=1<<j; a[j]|=1<<i
    for j,sup in enumerate(covers):
        for i in range(d):
            if sup>>i&1: edge(i,d+j)
        if sup>>1&1: edge(d+j,v)
        if kx>>j&1: edge(d+j,x)
    edge(1,v)
    for i in range(d):
        if sx>>i&1: edge(i,x)
    if vx: edge(v,x)
    return a,((1<<k)-1)<<d,1<<v


def q_decision(d: int,q: int,charge: bool) -> tuple[list[int],int]:
    a=tight(d,q); pairs=list(itertools.combinations(range(d),2)); deg=[x.bit_count() for x in a]
    mu=len(pairs)-q.bit_count(); g=deg.count(d-1)
    em=[sum(bool(q>>b&1) and min(deg[i],deg[j])>=h+1 for b,(i,j) in enumerate(pairs)) for h in range(1,d)]
    bound=2*mu+max((d-2)*max(0,g-1),max((h*em[h-1]+h)//(h+1) for h in range(1,d)))
    # A degree-one vertex uses d-2 missing incidences; every non-E_1 edge
    # is incident to such a vertex. This supports the quadratic corollary.
    assert em[0]>=len(pairs)-mu-(2*mu)//(d-2)
    assert 2*mu+(em[0]+1)//2 >= (d*(d-1)+3)//4
    result=[mu,g,bound,*em]; checks=0
    if charge:
        for sup in range(1,1<<d):
            ell=sup.bit_count(); threats=[]
            for t in range(d):
                if sup>>t&1: continue
                hit=a[t]&sup
                if hit.bit_count()==1:
                    s=hit.bit_length()-1; b=pairs.index(tuple(sorted((t,s)))); threats.append((b,min(deg[t],deg[s])))
            for h in range(1,d):
                mask=sum(1<<b for b,degree in threats if degree>=h+1)
                count=mask.bit_count(); assert count<=d-ell
                for weight in (d-1,d):
                    if weight<ell: continue
                    loss=weight-ell
                    assert not count or loss>=h
                    assert count<=loss+1
                    checks+=1
                result.append(mask)
    return result,checks


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--out',type=pathlib.Path)
    args=ap.parse_args(); root=pathlib.Path(__file__).resolve().parent; out=(args.out or root/'evidence').resolve(); out.mkdir(parents=True,exist_ok=True)
    inp=(out/'INPUT.txt').open('w'); pred=(out/'PYTHON_DECISIONS.txt').open('w'); ident=0
    counts=Counter(); families={}; controls=[]; algebra=0; minima={}
    def graph_row(d,km,vm,t,s,a,name=None):
        nonlocal ident
        dec=graph_decision(d,km,vm,t,s,a)
        inp.write('G '+ ' '.join(map(str,[ident,len(a),d,km,vm,t,s,*a]))+'\n')
        pred.write('G '+ ' '.join(map(str,[ident,*dec]))+'\n')
        if dec[0] and dec[1] and not dec[2]:
            assert dec[4]==0,('counterexample',ident,d,a,dec)
            counts['eligible_local_records']+=1
        if name: controls.append({'name':name,'record':ident,'pair_covered':dec[0],'pool_protected':dec[1],'threat':dec[2],'diameter_two':dec[3],'lost_pairs':dec[4]})
        else:
            counts['positive_family_records']+=1
            counts['diameter_two_records']+=dec[3]
            counts['threat_present_but_no_lost_pair']+=int(dec[2] and not dec[4])
            counts['threat_present_with_lost_pair']+=int(dec[2] and bool(dec[4]))
        ident+=1; return dec
    # All Q with distinguished edge 0--1 for d=3,4; all Q with 2 or 3 missing
    # edges and that distinguished edge at d=5. One pool probe and one arbitrary
    # support probe. All support-to-K and support-to-pool edges are varied.
    for d in (3,4,5):
        full=(1<<d)-1; pairs=d*(d-1)//2
        for style,covers in [('single_common',[full]),('pair_cover_no_common',[full^(1<<i) for i in range(3)])]:
            start=ident; qcount=0
            for q in range(1,1<<pairs,2):
                if d==5 and pairs-q.bit_count() not in (2,3): continue
                qcount+=1
                for sx in range(1<<d):
                    for kx in range(1<<len(covers)):
                        for vx in (0,1):
                            a,km,vm=build_graph(d,q,covers,sx,kx,vx)
                            dec=graph_row(d,km,vm,0,1,a)
                            assert dec[0] and dec[1]
            families[f'd{d}_{style}']={'tight_graphs':qcount,'records':ident-start}
    # Three premise-failure controls, all initially diameter two.
    a=tight(3,5)
    dec=graph_row(3,0,0,0,1,a,'pair_coverage_removed'); assert dec[:5]==(0,1,0,1,2)
    a,km,vm=build_graph(3,7,[7],7,1,0)
    a[3]&=~(1<<4);a[4]&=~(1<<3)
    dec=graph_row(3,km,vm,0,1,a,'pool_protection_removed'); assert dec[0:4]==(1,0,0,1) and dec[4]>0
    a,km,vm=build_graph(3,7,[7],2,0,0)
    dec=graph_row(3,km,vm,0,1,a,'uncovered_threat_allowed'); assert dec[0:4]==(1,1,1,1) and dec[4]>0
    a,km,vm=build_graph(3,7,[7],2,1,0)
    dec=graph_row(3,km,vm,0,1,a,'threat_not_sufficient_for_criticality'); assert dec[:5]==(1,1,1,1,0)
    a,km,vm=build_graph(4,63,[14,13,11],15,7,1)
    dec=graph_row(4,km,vm,0,1,a,'pair_cover_without_common_label'); assert dec[:5]==(1,1,0,1,0)
    graph_records=ident
    # Complete per-Q envelopes at d=3..6; all support/weight/h charge tests
    # at d<=5. Output retains every support's actual threatened-edge mask.
    for d in range(3,7):
        best=10**9; attaining=[]
        for q in range(1<<(d*(d-1)//2)):
            values,checks=q_decision(d,q,d<=5); algebra+=checks
            inp.write(f'Q {ident} {d} {q} {int(d<=5)}\n')
            pred.write('Q '+' '.join(map(str,[ident,*values]))+'\n')
            if values[2]<best: best=values[2];attaining=[]
            if values[2]==best: attaining.append(q)
            ident+=1
        minima[d]={'minimum':best,'attaining_count':len(attaining),'attaining_masks':attaining}
    inp.close();pred.close()
    # Exact numerical pair-coverage and floor/ceiling checks; arbitrary nonnegative
    # row increments only increase the tested lower bound, so use their zero case.
    pair_checks=0; ceiling_checks=0
    for d in range(3,11):
        for pools in itertools.product((1,2),repeat=d):
            m=sum(pools)
            for D in range(d*(d-2)):
                upper=m+(d+D)//(d-1)
                for t,s in itertools.combinations(range(d),2):
                    row_sum=2+2*m-pools[t]-pools[s]
                    assert row_sum-upper>=d-(d+D)//(d-1)>=1
                    pair_checks+=1
    for h in range(1,21):
        for q in range(101):
            for e in range(121):
                assert (e<=q+q//h)==(q>=(h*e+h)//(h+1));ceiling_checks+=1
    binary=out/'check_support_charge'
    subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',str(root/'check_support_charge.cpp'),'-o',str(binary)],check=True)
    with (out/'INPUT.txt').open('rb') as f,(out/'CPP_DECISIONS.txt').open('wb') as g:
        subprocess.run([str(binary)],stdin=f,stdout=g,check=True)
    expected=(out/'PYTHON_DECISIONS.txt').read_bytes();actual=(out/'CPP_DECISIONS.txt').read_bytes()
    if actual!=expected:
        for i,(x,y) in enumerate(zip(expected.splitlines(),actual.splitlines())):
            if x!=y: raise AssertionError(('Python/C++ mismatch',i,x,y))
        raise AssertionError('Python/C++ stream length mismatch')
    for name in ('INPUT.txt','PYTHON_DECISIONS.txt','CPP_DECISIONS.txt'):
        data=(out/name).read_bytes();(out/(name+'.gz')).write_bytes(gzip.compress(data,compresslevel=9,mtime=0))
    summary={'status':'PASS_LOCAL_PAIR_COVER_AND_SUPPORT_CHARGE','records':ident,'graph_records':graph_records,
             'tight_graph_records':ident-graph_records,'families':families,'counts':dict(counts),'controls':controls,
             'support_weight_h_checks':algebra,'pair_row_integer_checks':pair_checks,'floor_ceiling_checks':ceiling_checks,
             'envelope_minima':minima,
             'input_sha256':hashlib.sha256((out/'INPUT.txt').read_bytes()).hexdigest(),
             'decision_sha256':hashlib.sha256(expected).hexdigest(),'cpp_decision_sha256':hashlib.sha256(actual).hexdigest(),
             'scope':'Local graph deletion, exact support threats, row arithmetic and tight-graph envelopes only. Not a canonical exact-block graph census or catalogue application.',
             'independence':'Python bitset reachability and C++ explicit middle-vertex paths, same assistant; not independent expert review.',
             'old_replay':'Older 11357/324554/407741 streams not rerun by this new package.'}
    (out/'CHECK_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='envelope_minima'},indent=2))
    print('Envelope minima:',{d:(x['minimum'],x['attaining_count']) for d,x in minima.items()})
if __name__=='__main__': main()
