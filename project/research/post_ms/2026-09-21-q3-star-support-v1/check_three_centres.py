#!/usr/bin/env python3
"""Replay the three explicit physical obstructions, without solving for graphs."""
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
import json
from check_star_support import relation,CODES,Q

def symmetric_pairs(r):
    R=set(r['allowed_pairs'])
    return R|{(b,a) for a,b in R}

def forced_halfcubes(centres,R):
    forced=set()
    for c in centres:
        h=f'S{c}'
        for s in CODES[h]:
            if (h,f'S{s^7}') not in R:
                L=[l for l in CODES if not l.startswith('S') and CODES[h]&CODES[l]=={s}]
                assert len(L)==1
                forced.add(L[0])
    return forced

def replay(centres):
    r=relation(centres); R=symmetric_pairs(r)
    mandatory={f'S{c}' for c in centres}|forced_halfcubes(centres,R)
    incompatible=[(h,k) for h,k in r['diameter_incompatible_codes'] if h in mandatory and k in mandatory]
    if incompatible:return {'centres':centres,'reason':'mandatory diameter-incompatible codes','pairs':incompatible}
    # A clean coordinate witness cannot be adjacent to the complementary face,
    # and any two-step connection to a mandatory opposite-face vertex must use
    # a common A-neighbour code avoiding the outside cube target.
    for s in range(8):
        for i in range(3):
            t=s^(1<<i)
            if s>t:continue
            h=f'C{i}{(s>>i)&1}';k=f'C{i}{(t>>i)&1}'
            badh=k in mandatory and not any(t not in CODES[l] and (h,l) in R and (k,l) in R for l in r['names'])
            badk=h in mandatory and not any(s not in CODES[l] and (h,l) in R and (k,l) in R for l in r['names'])
            if badh and badk:return {'centres':centres,'reason':'no clean cube-entry witness','cube_edge':[s,t]}
    # For the parity-triangle class, forbidden complementary coordinate codes
    # force two different star-neighbour types at every star vertex.
    forbidden=set()
    for h,k in r['diameter_incompatible_codes']:
        if h in mandatory:forbidden.add(k)
        if k in mandatory:forbidden.add(h)
    required={}
    for c in centres:
        targets=set()
        for s in CODES[f'S{c}']:
            L=[l for l in CODES if not l.startswith('S') and CODES[f'S{c}']&CODES[l]=={s}]
            assert len(L)==1
            if L[0] in forbidden:
                k=f'S{s^7}'
                assert (f'S{c}',k) in R
                targets.add(k)
        required[f'S{c}']=targets
    if all(len({k for k in required[f'S{c}'] if (c^7) in CODES[k]})>=2 for c in centres):
        # Check that no other certificate can rescue any surviving star edge.
        for h,k in R:
            if not h.startswith('S'):continue
            assert k.startswith('S')
            assert CODES[h]&CODES[k]
            assert not any(not(CODES[h]&CODES[l]) and (k,l) in R for l in r['names'])
            assert not any(not(CODES[k]&CODES[l]) and (h,l) in R for l in r['names'])
        return {'centres':centres,'reason':'two mandatory bridges disable every star-edge certificate','required_types':{h:sorted(v) for h,v in required.items()}}
    raise AssertionError(('Unclosed three-centre support',centres))

def main():
    data=[replay(c) for c in combinations(range(8),3)]
    kinds=Counter(tuple(sorted((a^b).bit_count() for a,b in combinations(d['centres'],2))) for d in data)
    assert kinds=={(1,1,2):24,(1,2,3):24,(2,2,2):8}
    # Independently confirm cube automorphism coverage of the representatives.
    covered=set()
    for rep in ((0,1,2),(0,1,6),(0,3,5)):
        for p in permutations(range(3)):
            for t in range(8):
                covered.add(tuple(sorted(t^sum(((c>>j)&1)<<p[j] for j in range(3)) for c in rep)))
    assert covered==set(combinations(range(8),3))
    result={'scope':'All 56 supports of exactly three distinct star centres; arbitrary multiplicities',
            'symmetry_counts':{str(k):v for k,v in kinds.items()},'exclusions':data}
    Path(__file__).with_name('THREE_CENTRE_REPLAY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:',dict(kinds),'; all 56 supports excluded by the stated physical obstructions')

if __name__=='__main__':main()
