#!/usr/bin/env python3
"""Independent exact structure scan of the n=29,t=3 four-template COVER.

Important audit distinction: this script does NOT classify a previously chosen
count-tree assignment.  It recomputes, by Fraction arithmetic through the
preserved exact four-template checker, the complete validity mask

    {template T : exact gap_T(profile) > 0}

for each of the 94 regenerated frontier profiles.  Feature-compression claims
below concern that independently determined mask, not an assignment rule.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter, defaultdict
from pathlib import Path
import importlib.util
import json


def load_module(path: Path):
    spec=importlib.util.spec_from_file_location("t3cover",path)
    mod=importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k: h=k
        else: break
    return h


def features(p):
    rho=p['rho']; s=p['s']; b=len(rho)
    rho1=rho.count(1); z2=sum(x>=2 for x in rho)
    return {
        'D1':s.count(1),
        'D2':s.count(2),
        'D3':s.count(3),
        'D4':s.count(4),
        'D5':s.count(5),
        'Smax':max(s),
        'rho1':rho1,
        'z2':z2,
        'h':h_res(rho),
        'half':int(2*z2>=b),
        'J':2*z2-s.count(1),
        'r':sum(rho),
        'S':sum(s),
    }


def key_census(records, fields):
    cells=defaultdict(Counter)
    for r in records:
        key=tuple(r['f'][x] for x in fields)
        cells[key][r['mask_id']]+=1
    out=[]
    for key in sorted(cells):
        mc=cells[key]
        out.append({
            'key':list(key),
            'profiles':sum(mc.values()),
            'mask_ids':dict(sorted(mc.items())),
            'mixed':len(mc)>1,
        })
    return out


def summarize(rows):
    mixed=[x for x in rows if x['mixed']]
    return {
        'occupied_cells':len(rows),
        'mixed_cells':len(mixed),
        'profiles_in_mixed_cells':sum(x['profiles'] for x in mixed),
    }


def main():
    ap=ArgumentParser()
    ap.add_argument('--cover-script',type=Path,required=True)
    ap.add_argument('--demands-json',type=Path,required=True)
    ap.add_argument('--rows',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    z=ap.parse_args()

    mod=load_module(z.cover_script)
    P=mod.load(z.demands_json,z.rows)
    if len(P)!=94: raise SystemExit(f'expected 94 profiles, got {len(P)}')

    names=sorted(mod.TEMPLATES)
    gaps={name:mod.gaps_for(P,mod.TEMPLATES[name]) for name in names}
    records=[]; mask_counts=Counter(); mask_members=defaultdict(list)
    for i,p in enumerate(P):
        mask=tuple(name for name in names if gaps[name][i]>0)
        if not mask: raise AssertionError(('uncovered',i))
        mask_id='+'.join(mask)
        f=features(p)
        records.append({'index':i,'demand_id':p['demand_id'],'mask':list(mask),'mask_id':mask_id,'f':f})
        mask_counts[mask_id]+=1; mask_members[mask_id].append(i)

    tests={}
    field_sets=[
        ('h',),('D1',),('D5',),('rho1',),('half',),('J',),
        ('h','J'),('h','D1'),('h','D1','D5'),('h','D1','half'),
        ('h','D1','D5','half'),('h','D1','rho1'),('h','D1','D5','rho1'),
        ('D1','D5','rho1'),('D1','D5','half'),
    ]
    for fs in field_sets:
        rows=key_census(records,fs)
        tests['+'.join(fs)]={'fields':list(fs),'summary':summarize(rows),'cells':rows}

    # Threshold tests are independent of the old assignment: they ask whether
    # exact validity masks are determined by the stated features plus one bit.
    threshold_scans=[]
    for k in range(0,17):
        cells=defaultdict(Counter)
        for r in records:
            f=r['f']; key=(f['h'],f['D1'],f['D5'],int(f['rho1']<=k))
            cells[key][r['mask_id']]+=1
        rows=[{'key':list(key),'profiles':sum(mc.values()),'mask_ids':dict(sorted(mc.items())),'mixed':len(mc)>1}
              for key,mc in sorted(cells.items())]
        threshold_scans.append({'k':k,'summary':summarize(rows),'pure':all(not x['mixed'] for x in rows)})

    # Search all subsets of a compact interpretable primitive feature family.
    primitive=['h','D1','D5','rho1']
    subset_scan=[]
    from itertools import combinations
    for m in range(1,len(primitive)+1):
        for fs in combinations(primitive,m):
            rows=key_census(records,fs); sm=summarize(rows)
            subset_scan.append({'fields':list(fs),**sm,'pure':sm['mixed_cells']==0})

    # Preserve exact masks of the four lower-bound clique profiles.
    clique=[]
    for i in (0,1,38,30):
        clique.append(records[i])

    out={
        'schema':'n29-t3-template-validity-mask-structure-exact-v1',
        'status':'PASS',
        'profiles':len(P),
        'template_names':names,
        'mask_count':len(mask_counts),
        'mask_counts':dict(sorted(mask_counts.items())),
        'mask_members':{k:v for k,v in sorted(mask_members.items())},
        'feature_tests':tests,
        'rho1_threshold_scan_with_h_D1_D5':threshold_scans,
        'primitive_subset_scan':subset_scan,
        'lower_bound_clique_profiles':clique,
        'records':records,
        'acceptance':'all masks recomputed from exact positive Fraction gaps; no chosen assignment is used as target',
        'interpretation':'This artifact is the non-circular replacement for any scan that classified the old rho1<=8 count-tree assignment itself.',
    }
    z.output.parent.mkdir(parents=True,exist_ok=True)
    z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({
        'status':'PASS','mask_count':len(mask_counts),'mask_counts':dict(sorted(mask_counts.items())),
        'pure_feature_tests':[k for k,v in tests.items() if v['summary']['mixed_cells']==0],
        'pure_rho1_thresholds':[x['k'] for x in threshold_scans if x['pure']],
        'pure_primitive_subsets':[x['fields'] for x in subset_scan if x['pure']],
        'clique_masks':[{ 'index':x['index'],'mask':x['mask'],'f':x['f']} for x in clique],
    },indent=2,sort_keys=True))

if __name__=='__main__': main()
