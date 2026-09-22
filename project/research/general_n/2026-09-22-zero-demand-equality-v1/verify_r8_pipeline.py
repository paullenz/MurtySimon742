#!/usr/bin/env python3
"""Independent consistency checks for the committed r=8 finite pipeline."""
import json

core=json.load(open('R8_CORE_ORBITS.json'))
strict=json.load(open('R8_ORBIT_SOURCE_SCREEN.json'))
eqcore=json.load(open('R8_EQUALITY_CORE_SCREEN.json'))
eqsrc=json.load(open('R8_EQUALITY_SOURCE_FEASIBILITY.json'))
supp=json.load(open('R8_EQUALITY_SUPPLEMENT_SCREEN.json'))

assert sum(x['strict_survivors_labelled'] for x in core.values())==11350
assert sum(x['strict_survivor_orbits'] for x in core.values())==68
assert sum(x['source_feasible_orbits'] for x in strict.values())==1
assert strict['(2, 2, 2, 1, 1)']['source_feasible_orbits']==1
assert sum(x['labelled_equality_candidates'] for x in eqcore.values())==26838
assert sum(x['candidate_orbits'] for x in eqcore.values())==203
feasible={(p,r['orbit']) for p,e in eqsrc.items() for r in e['rows'] if r['source_feasible']}
keys={(k.split('/orbit_')[0],int(k.split('/orbit_')[1])) for k in supp}
assert feasible==keys and len(keys)==39
assert sum(x['source_multisets_tested'] for x in supp.values())==2103
assert sum(x['supplement_feasible'] for x in supp.values())==0
print(json.dumps({'strict_labelled':11350,'strict_orbits':68,'strict_source_feasible':1,
 'equality_labelled':26838,'equality_orbits':203,'equality_source_feasible':39,
 'equality_source_populations':2103,'equality_supplement_survivors':0,
 'all_cross_file_assertions':'PASS'},indent=2))
