#!/usr/bin/env python3
"""Reproduce local short-path tests, independent C++ decisions and arithmetic checks.
Python 3.10+ and a C++17 compiler; no third-party package or network needed.
These are local-lemma tests, NOT a census of canonical exact-block graphs.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json, pathlib, subprocess

def tight_graph(d: int, mask: int) -> list[int]:
    a = [0] * (d + 2)
    for b, (i, j) in enumerate(itertools.combinations(range(d), 2)):
        if mask >> b & 1:
            a[i] |= 1 << j
            a[j] |= 1 << i
    return a

def decide(d: int, q: int, cm: int, xm: int, cx: int) -> tuple[int, int, int, int]:
    a = tight_graph(d, q)
    full = (1 << d) - 1
    endpoint_ok = bool(a[0] & 2) and a[0].bit_count() >= 2 and a[1].bit_count() >= 2
    support_ok = xm in (0, full) or xm.bit_count() == d - 1 or (xm.bit_count() == 1 and cx == 1)
    eligible = int(endpoint_ok and cm == full and support_ok)
    for i in range(d):
        if cm >> i & 1:
            a[i] |= 1 << d
            a[d] |= 1 << i
        if xm >> i & 1:
            a[i] |= 1 << (d + 1)
            a[d + 1] |= 1 << i
    if cx:
        a[d] |= 1 << (d + 1)
        a[d + 1] |= 1 << d
    def reach(adj: list[int]) -> list[int]:
        ans = []
        for i, mask in enumerate(adj):
            r = mask | (1 << i)
            while mask:
                bit = mask & -mask
                r |= adj[bit.bit_length() - 1]
                mask ^= bit
            ans.append(r)
        return ans
    before = reach(a)
    a[0] &= ~2
    a[1] &= ~1
    after = reach(a)
    lost = 0
    for b, (i, j) in enumerate(itertools.combinations(range(d + 2), 2)):
        if (before[i] >> j & 1) and not (after[i] >> j & 1):
            lost |= 1 << b
    diameter_two = int(all(v == (1 << (d + 2)) - 1 for v in before))
    return eligible, diameter_two, lost.bit_count(), lost

def write_gzip(path: pathlib.Path, content: bytes) -> None:
    path.write_bytes(gzip.compress(content, compresslevel=9, mtime=0))

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent / 'evidence')
    args = ap.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    rows: list[str] = []
    results: list[str] = []
    by_d: dict[int, dict[str, int]] = {}
    def add(d: int, q: int, cm: int, xm: int, cx: int, control: bool = False) -> tuple[int,int,int,int]:
        ident = len(rows)
        rows.append(f'{ident} {d} {q} {cm} {xm} {cx}\n')
        dec = decide(d,q,cm,xm,cx)
        results.append(f'{ident} {dec[0]} {dec[1]} {dec[2]} {dec[3]}\n')
        if not control:
            if dec[0] != 1 or dec[2] != 0:
                raise AssertionError(('local lemma counterexample', rows[-1], dec))
            by_d[d]['records'] += 1
            by_d[d]['diameter_two'] += dec[1]
        return dec
    # Exhaust ALL labelled tight graphs with distinguished edge 0--1 and
    # endpoint degrees >=2, for 3 <= d <=6. Every allowed probe support and
    # common/probe adjacency is tested. Roles fixed: no isomorphism pruning.
    for d in range(3,7):
        by_d[d] = {'tight_graphs':0, 'records':0, 'diameter_two':0}
        full = (1 << d) - 1
        supports = [(0,0),(0,1),(full,0),(full,1)]
        supports += [(full ^ (1<<t),cx) for t in range(d) for cx in (0,1)]
        supports += [(1<<t,1) for t in range(d)]
        for q in range(1,1 << (d*(d-1)//2),2):
            a = tight_graph(d,q)
            if min(a[0].bit_count(),a[1].bit_count()) < 2:
                continue
            by_d[d]['tight_graphs'] += 1
            for xm,cx in supports:
                add(d,q,full,xm,cx)
    controls = []
    specifications = [
        ('first_endpoint_degree',3,5,7,6,0),
        ('second_endpoint_degree',3,3,7,5,0),
        ('singleton_pool_protection',3,7,7,2,0),
        ('one_hole_support_restriction',4,51,15,10,0),
        ('common_label',4,51,9,1,1),
    ]
    for name,d,q,cm,xm,cx in specifications:
        dec = add(d,q,cm,xm,cx,control=True)
        if dec[0] != 0 or dec[1] != 1 or dec[2] == 0:
            raise AssertionError(('ineffective negative control',name,dec))
        controls.append({'name':name,'record':len(rows)-1,'lost_pairs':dec[2]})
    inputs = ''.join(rows).encode('ascii')
    expected = ''.join(results).encode('ascii')
    (out/'INPUT.txt').write_bytes(inputs)
    (out/'PYTHON_DECISIONS.txt').write_bytes(expected)
    source = pathlib.Path(__file__).resolve().with_name('check_star_forest.cpp')
    binary = out/'check_star_forest'
    subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',str(source),'-o',str(binary)],check=True)
    with (out/'INPUT.txt').open('rb') as inp, (out/'CPP_DECISIONS.txt').open('wb') as dest:
        subprocess.run([str(binary)],stdin=inp,stdout=dest,check=True)
    actual = (out/'CPP_DECISIONS.txt').read_bytes()
    if actual != expected:
        raise AssertionError('Python and C++ per-record outputs differ')
    # Integer equality classification: no approximation or randomized step.
    arithmetic = 0
    for d in range(5,1001):
        r = 2*(d//2)
        allowed = []
        for mu in range(r//2+1):
            lower = 2*mu+(d-2)*max(0,d-2*mu-1)
            if lower <= r:
                allowed.append(mu)
            arithmetic += 1
        assert allowed == [r//2]
        residue = (d+r) % (d-1)
        assert residue == (1 if d%2 else 2)
        assert (d-1)*(d-2)>r
    summary = {
        'status':'PASS_FRESH_LOCAL_LEMMA_AND_INTEGER_CHECKS',
        'scope':'All distinguished-edge tight graphs d=3..6 with both endpoint degrees >=2; all allowed one-probe support types. Local short-path preservation, not canonical graph realizations or catalogue exclusions.',
        'by_d':by_d, 'eligible_records':sum(x['records'] for x in by_d.values()),
        'negative_controls':controls, 'records':len(rows),
        'arithmetic_parameter_range':[5,1000], 'arithmetic_mu_checks':arithmetic,
        'input_sha256':hashlib.sha256(inputs).hexdigest(),
        'decision_sha256':hashlib.sha256(expected).hexdigest(),
        'cpp_decision_sha256':hashlib.sha256(actual).hexdigest(),
        'independence':'Python bitset reachability and C++ explicit intermediate-vertex search; same assistant, not external independent review.',
        'inherited_11357_replay':'NOT_RERUN_IN_THIS_PACKAGE'
    }
    for filename,data in [('INPUT.txt',inputs),('PYTHON_DECISIONS.txt',expected),('CPP_DECISIONS.txt',actual)]:
        write_gzip(out/(filename+'.gz'),data)
    (out/'CHECK_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__ == '__main__':
    main()
