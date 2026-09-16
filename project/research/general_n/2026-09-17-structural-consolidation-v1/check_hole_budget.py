#!/usr/bin/env python3
"""Fresh h=2 bounded-hole tests. Depends only on the adjacent published checker.
Both input generation and full per-record Python/C++ comparison are deterministic.
No canonical-graph or catalogue claim follows from these local tests.
"""
from __future__ import annotations
import gzip, hashlib, itertools, json, pathlib, subprocess
from check_star_forest import tight_graph, decide

def main() -> None:
    root=pathlib.Path(__file__).resolve().parent
    out=root/'hole_evidence'; out.mkdir(exist_ok=True)
    rows=[]; decisions=[]; counts={}
    def add(d,q,cm,xm,cx,control=False):
        a=tight_graph(d,q); full=(1<<d)-1
        ok=int(bool(a[0]&2) and min(a[0].bit_count(),a[1].bit_count())>=3 and cm==full
               and (xm==0 or d-xm.bit_count()<=2 or (xm.bit_count()==1 and cx==1)))
        _,diameter,lost,mask=decide(d,q,cm,xm,cx)
        ident=len(rows); rows.append(f'{ident} {d} {q} {cm} {xm} {cx}\n')
        decisions.append(f'{ident} {ok} {diameter} {lost} {mask}\n')
        if not control:
            if not ok or lost: raise AssertionError(('counterexample',rows[-1],decisions[-1]))
            counts[d]['records']+=1; counts[d]['diameter_two']+=diameter
        elif ok or not diameter or not lost:
            raise AssertionError(('ineffective control',rows[-1],decisions[-1]))
        return {'record':ident,'lost_pairs':lost}
    for d in range(4,7):
        full=(1<<d)-1; counts[d]={'tight_graphs':0,'records':0,'diameter_two':0}
        supports=[(0,0),(0,1)]
        for holes in range(3):
            for hs in itertools.combinations(range(d),holes):
                xm=full ^ sum(1<<i for i in hs)
                supports.extend((xm,cx) for cx in (0,1))
        supports.extend((1<<i,1) for i in range(d))
        assert len(set(supports))==len(supports)
        for q in range(1,1<<(d*(d-1)//2),2):
            a=tight_graph(d,q)
            if min(a[0].bit_count(),a[1].bit_count())<3: continue
            counts[d]['tight_graphs']+=1
            for xm,cx in supports: add(d,q,full,xm,cx)
    controls=[]
    for name,d,q,cm,xm,cx in [
        ('first_endpoint_degree_two',4,59,15,10,0),
        ('second_endpoint_degree_two',4,55,15,5,0),
        ('three_hole_probe',5,887,31,18,0),
        ('unprotected_singleton',4,63,15,2,0),
        ('common_label_absent',4,63,14,2,1),
    ]:
        controls.append({'name':name,**add(d,q,cm,xm,cx,True)})
    inp=''.join(rows).encode(); expected=''.join(decisions).encode()
    (out/'INPUT.txt').write_bytes(inp); (out/'PYTHON_DECISIONS.txt').write_bytes(expected)
    exe=out/'check_hole_budget'
    subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',str(root/'check_hole_budget.cpp'),'-o',str(exe)],check=True)
    with (out/'INPUT.txt').open('rb') as f, (out/'CPP_DECISIONS.txt').open('wb') as dest:
        subprocess.run([str(exe)],stdin=f,stdout=dest,check=True)
    actual=(out/'CPP_DECISIONS.txt').read_bytes()
    if actual!=expected: raise AssertionError('Python/C++ disagreement')
    mu_checks=0
    for d in range(5,1001):
        r=2*(d//2); allowed=[]
        for mu in range(r//2+1):
            mu_checks+=1
            if 2*mu+(d-2)*max(0,d-2*mu-1)<=r+1: allowed.append(mu)
        assert allowed==[r//2]
        assert (d+r+1)%(d-1)==(2 if d%2 else 3)
        for g in (0,1):
            assert (d-1)-(r-d+g+1)>=3
    summary={
        'status':'PASS_FRESH_BOUNDED_HOLE_CHECKS','hole_budget':2,
        'scope':'All labelled distinguished-edge Q with endpoint degrees >=3 for d=4..6; all zero-, one-, two-hole probe supports and protected singletons. Local short-path tests, not canonical exact-block graph realizations.',
        'by_d':counts,'eligible_records':sum(x['records'] for x in counts.values()),
        'controls':controls,'records':len(rows),
        'arithmetic_d_range':[5,1000],'arithmetic_mu_checks':mu_checks,
        'input_sha256':hashlib.sha256(inp).hexdigest(),
        'decision_sha256':hashlib.sha256(expected).hexdigest(),
        'cpp_decision_sha256':hashlib.sha256(actual).hexdigest(),
        'independence':'Python bitsets and C++ explicit intermediate-vertex search; same assistant, not independent expert review.'
    }
    for name,data in [('INPUT.txt',inp),('PYTHON_DECISIONS.txt',expected),('CPP_DECISIONS.txt',actual)]:
        (out/(name+'.gz')).write_bytes(gzip.compress(data,compresslevel=9,mtime=0))
    (out/'CHECK_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
