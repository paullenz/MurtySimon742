#!/usr/bin/env python3
"""Search for simple exact regime rules for the n=29,t=2 three-template certificate.

This is a structural diagnostic, not a proof event.  It regenerates the same
902-profile frontier consumed by n29_t2_sh3_c11_three_scalar_exact.py, computes
which of the three exact rational scalar templates covers each profile, and then
asks whether elementary integer statistics of (s,rho) give a transparent exact
partition into template-valid regimes.

Searches performed:
  * coverage-mask census;
  * one-feature partitions into <=3 intervals;
  * two-predicate decision lists with one leaf per template;
  * largest pure threshold predicates for each template.

No ML package is used.  Every reported exact partition is checked directly
against the exact Fraction template gaps.
"""
from __future__ import annotations
from pathlib import Path
from collections import Counter, defaultdict
import argparse, importlib.util, json, sys


def load_exact_module(path: Path):
    spec = importlib.util.spec_from_file_location("t2exact", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def feature_vector(pf):
    s=list(pf['s']); r=list(pf['rho'])
    f={}
    f['sum_s']=sum(s); f['sum_rho']=sum(r)
    f['sq_s']=sum(x*x for x in s); f['sq_rho']=sum(x*x for x in r)
    f['cube_s']=sum(x*x*x for x in s); f['cube_rho']=sum(x*x*x for x in r)
    f['max_s']=max(s); f['max_rho']=max(r)
    f['distinct_s']=len(set(s)); f['distinct_rho']=len(set(r))
    for k in range(1,11):
        se=sum(x==k for x in s); re=sum(x==k for x in r)
        sge=sum(x>=k for x in s); rge=sum(x>=k for x in r)
        sle=sum(x<=k for x in s); rle=sum(x<=k for x in r)
        f[f's_eq_{k}']=se; f[f'r_eq_{k}']=re
        f[f's_ge_{k}']=sge; f[f'r_ge_{k}']=rge
        f[f's_le_{k}']=sle; f[f'r_le_{k}']=rle
        f[f'ge_diff_{k}']=sge-rge
        f[f'le_diff_{k}']=sle-rle
        f[f'excess_s_{k}']=sum(max(x-k,0) for x in s)
        f[f'excess_r_{k}']=sum(max(x-k,0) for x in r)
        f[f'excess_diff_{k}']=f[f'excess_s_{k}']-f[f'excess_r_{k}']
        f[f'qcap_{k}']=min(12-k, sle)
    return f


def mask_from_indices(indices):
    z=0
    for i in indices:z|=1<<i
    return z


def mask_count(x): return x.bit_count()


def templates_covering(mask, cover_masks, names):
    return [n for n in names if mask & ~cover_masks[n] == 0]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--demands-json',type=Path,required=True)
    ap.add_argument('--rows',type=Path,required=True)
    ap.add_argument('--exact-script',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    z=ap.parse_args()

    ex=load_exact_module(z.exact_script)
    P=ex.load(z.demands_json,z.rows)
    if len(P)!=902: raise SystemExit(f'expected 902 profiles, got {len(P)}')
    names=list(ex.TEMPLATES)
    gap_map={n:ex.gaps(P,ex.TEMPLATES[n]) for n in names}
    covers={n:[g>0 for g in gap_map[n]] for n in names}
    cover_masks={n:mask_from_indices(i for i,v in enumerate(covers[n]) if v) for n in names}
    ALL=(1<<len(P))-1
    if (cover_masks[names[0]]|cover_masks[names[1]]|cover_masks[names[2]]) != ALL:
        raise SystemExit('three-template union does not cover frontier')

    feats=[feature_vector(p) for p in P]
    keys=sorted(feats[0])
    vals={k:[f[k] for f in feats] for k in keys}

    # Coverage-mask census.
    census=Counter()
    examples=defaultdict(list)
    for i in range(len(P)):
        m=''.join('1' if covers[n][i] else '0' for n in names)
        census[m]+=1
        if len(examples[m])<8:examples[m].append(i)

    # Feature ranges by exact coverage mask and for unique-template profiles.
    range_summary={}
    for m in sorted(census):
        ids=[i for i in range(len(P)) if ''.join('1' if covers[n][i] else '0' for n in names)==m]
        range_summary[m]={k:[min(vals[k][i] for i in ids),max(vals[k][i] for i in ids)] for k in keys if len({vals[k][i] for i in ids})>1}

    unique={n:[i for i in range(len(P)) if covers[n][i] and sum(covers[o][i] for o in names)==1] for n in names}
    unique_stats={}
    for n,ids in unique.items():
        unique_stats[n]={'count':len(ids),'indices':ids,'feature_ranges':({k:[min(vals[k][i] for i in ids),max(vals[k][i] for i in ids)] for k in keys} if ids else {})}

    # Build threshold predicates feature <= c and feature >= c.
    predicates=[]
    for k in keys:
        uv=sorted(set(vals[k]))
        for c in uv[:-1]:
            m=mask_from_indices(i for i,x in enumerate(vals[k]) if x<=c)
            if m and m!=ALL: predicates.append({'feature':k,'op':'<=','cut':c,'mask':m})
        for c in uv[1:]:
            m=mask_from_indices(i for i,x in enumerate(vals[k]) if x>=c)
            if m and m!=ALL: predicates.append({'feature':k,'op':'>=','cut':c,'mask':m})

    # Largest pure threshold regions for each template.
    pure_top={}
    for n in names:
        good=[]
        C=cover_masks[n]
        for p in predicates:
            m=p['mask']
            if m & ~C == 0:
                good.append((mask_count(m),p['feature'],p['op'],p['cut']))
        good.sort(reverse=True)
        pure_top[n]=[{'size':a,'feature':b,'op':c,'cut':d} for a,b,c,d in good[:25]]

    # One-feature exact partitions into 2 or 3 contiguous intervals.
    interval_solutions=[]
    for k in keys:
        uv=sorted(set(vals[k]))
        if len(uv)<2: continue
        prefix=[]
        for c in uv:
            prefix.append(mask_from_indices(i for i,x in enumerate(vals[k]) if x<=c))
        # 2 intervals
        for a in range(len(uv)-1):
            ms=[prefix[a], ALL & ~prefix[a]]
            choices=[templates_covering(m,cover_masks,names) for m in ms]
            if all(choices):
                interval_solutions.append({'feature':k,'cuts':[uv[a]],'interval_templates':choices,'sizes':[mask_count(m) for m in ms]})
        # 3 intervals
        for a in range(len(uv)-2):
            for b in range(a+1,len(uv)-1):
                ms=[prefix[a], prefix[b]&~prefix[a], ALL&~prefix[b]]
                if any(m==0 for m in ms):continue
                choices=[templates_covering(m,cover_masks,names) for m in ms]
                if all(choices):
                    interval_solutions.append({'feature':k,'cuts':[uv[a],uv[b]],'interval_templates':choices,'sizes':[mask_count(m) for m in ms]})
    interval_solutions.sort(key=lambda x:(len(x['cuts']), len(x['feature']), x['feature'], x['cuts']))

    # Exact two-predicate decision lists with three leaves, using each template once.
    # leaf1 = P1 -> A; leaf2 = remaining & P2 -> B; leaf3 -> C.
    decision_lists=[]
    import itertools
    for A,B,C in itertools.permutations(names):
        CA,CB,CC=cover_masks[A],cover_masks[B],cover_masks[C]
        pureA=[p for p in predicates if p['mask'] & ~CA == 0]
        # Prefer large/simple first regions, but keep all for exact search.
        pureA.sort(key=lambda p:(-mask_count(p['mask']),p['feature'],p['op'],p['cut']))
        for p1 in pureA:
            m1=p1['mask']; rem=ALL & ~m1
            if not rem:continue
            required=rem & ~CC   # must go to B leaf
            forbidden=rem & ~CB  # must NOT go to B leaf
            for p2 in predicates:
                seg=rem & p2['mask']
                if not seg or seg==rem:continue
                if required & ~p2['mask']:continue
                if forbidden & p2['mask']:continue
                if seg & ~CB:continue
                tail=rem & ~p2['mask']
                if tail & ~CC:continue
                decision_lists.append({
                    'order':[A,B,C],
                    'rule1':{'feature':p1['feature'],'op':p1['op'],'cut':p1['cut']},
                    'rule2':{'feature':p2['feature'],'op':p2['op'],'cut':p2['cut']},
                    'sizes':[mask_count(m1),mask_count(seg),mask_count(tail)],
                })
                if len(decision_lists)>=200:break
            if len(decision_lists)>=200:break
        if len(decision_lists)>=200:break

    # Triangle diagnostics for the exact lower-bound witnesses.
    witness_ids=[0,3,77]
    witness=[]
    for i in witness_ids:
        witness.append({'index':i,'demand_id':P[i]['demand_id'],'s':P[i]['s'],'rho':P[i]['rho'],
                        'coverage':{n:covers[n][i] for n in names},
                        'features':feats[i]})

    out={
        'schema':'n29-t2-regime-structure-scan-v1',
        'status':'PASS',
        'profiles':len(P),
        'templates':names,
        'coverage_mask_census':dict(sorted(census.items())),
        'coverage_mask_examples':dict(sorted(examples.items())),
        'unique_template_profiles':unique_stats,
        'feature_count':len(keys),
        'predicate_count':len(predicates),
        'one_feature_exact_partitions_found':len(interval_solutions),
        'one_feature_exact_partitions':interval_solutions[:100],
        'two_rule_exact_decision_lists_found':len(decision_lists),
        'two_rule_exact_decision_lists':decision_lists[:100],
        'largest_pure_threshold_regions':pure_top,
        'lower_bound_triangle_profiles':witness,
        'interpretation':(
            'Structural diagnostic only. Any listed partition is exact with respect to the three '
            'already-exact rational template gaps, but no general-n inference follows from it.'
        ),
    }
    z.output.parent.mkdir(parents=True,exist_ok=True)
    z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
