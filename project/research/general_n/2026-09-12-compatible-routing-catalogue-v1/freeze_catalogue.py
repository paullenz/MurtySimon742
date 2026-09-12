#!/usr/bin/env python3
"""Deterministic simplicity ranking; no full-pool results are read."""
from pathlib import Path
from functools import reduce
from math import gcd
import hashlib,json
HERE=Path(__file__).resolve().parent

def normalize(terms):
    terms=[(kind,tuple(desc),weight) for kind,desc,weight in terms if weight]
    divisor=reduce(gcd,(abs(t[2]) for t in terms),0) or 1
    return tuple(sorted((kind,desc,weight//divisor) for kind,desc,weight in terms))

def rank(vector):return sum(abs(t[2]) for t in vector),len(vector),vector

def main():
    raw=(HERE.parent/'2026-09-12-compatible-routing-pilot-v1/envelopes.json').read_bytes()
    candidates={}
    for env in json.loads(raw):
        if env['mode']=='joint_transport':continue
        vector=normalize(env['weights'])
        candidates.setdefault(vector,[]).append({k:env[k] for k in ['mode','layer','state_id','h','j','attempt_index']})
    ordered=sorted(candidates,key=rank);seeds=ordered[:20]
    heavy={normalize([t for t in v if t[1][0] not in ('selected_balance','all_transport','forced_transport')]) for v in seeds}
    selected=heavy|{normalize([t for t in v if t[1][0] not in ('all_transport','forced_transport')]) for v in seeds}
    eligible=selected|set(seeds)
    assert () not in eligible
    vectors=sorted(eligible,key=rank);ids={v:i for i,v in enumerate(vectors)}
    catalogue=dict(schema='compatible-routing-catalogue-v1',baseline_commit='be45e9c540ece11290e6f07e3a31bd8dcc3da2d0',
        pilot_envelopes_sha256=hashlib.sha256(raw).hexdigest(),candidate_count=len(ordered),seed_count=20,
        ranking='sum absolute primitive integer weights, number of terms, lexicographic vector',
        thresholds='h=2..max(s), T=4h; transport cutoffs retain their absolute integer values',
        templates=[dict(id=ids[v],weights=v) for v in vectors],
        modes={m:sorted(ids[v] for v in group) for m,group in [('heavy_only',heavy),('selected_degree',selected),('eligible',eligible)]},
        seeds=[dict(template_id=ids[v],rank=i+1,weights=v,provenance=candidates[v]) for i,v in enumerate(seeds)],
        external_review='OPEN')
    (HERE/'catalogue.json').write_text(json.dumps(catalogue,indent=2)+'\n')
    (HERE/'catalogue_candidates.json').write_text(json.dumps([dict(rank=i+1,weights=v,selected=i<20,provenance=candidates[v]) for i,v in enumerate(ordered)],indent=2)+'\n')
    print(json.dumps(dict(candidates=len(ordered),seeds=20,templates=len(vectors),modes={m:len(v) for m,v in catalogue['modes'].items()},
                         catalogue_sha256=hashlib.sha256((HERE/'catalogue.json').read_bytes()).hexdigest())))

if __name__=='__main__':main()
