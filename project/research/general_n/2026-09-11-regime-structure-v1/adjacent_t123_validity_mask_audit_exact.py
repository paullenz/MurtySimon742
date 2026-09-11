#!/usr/bin/env python3
"""Non-circular exact validity-mask and common-regime audit for t=1,2,3.

For each laboratory this script recomputes the exact rational gap of *every*
preserved scalar template before constructing any feature labels.  It then asks
two deliberately different questions:

1. MASK PURITY: does a feature cell determine the complete set of templates
   having positive exact gap?  This is a strong geometry question.
2. COMMON-TEMPLATE SUFFICIENCY: does every profile in the feature cell share at
   least one positive-gap template?  This is the weaker condition actually
   needed for a finite regime-wise proof/cover.

No chosen assignment labels are used to define either target.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter,defaultdict
from pathlib import Path
import importlib.util,json


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);assert spec.loader is not None
    spec.loader.exec_module(m);return m

def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k:h=k
        else:break
    return h

def feat(p):
    rho=p['rho'];s=p['s'];z2=sum(x>=2 for x in rho);D1=s.count(1)
    return {'h':h_res(rho),'J':2*z2-D1,'D1':D1,'rho1':rho.count(1),'z2':z2}

def summarize(P,masks):
    records=[];mc=Counter();mult=Counter()
    for i,p in enumerate(P):
        mask=tuple(k for k in sorted(masks) if masks[k][i])
        if not mask:raise AssertionError(('uncovered',i))
        mid='+'.join(mask);f=feat(p);records.append((i,mask,mid,f));mc[mid]+=1;mult[len(mask)]+=1

    def partition(fields):
        cells=defaultdict(list)
        for i,mask,mid,f in records:
            cells[tuple(f[x] for x in fields)].append((i,set(mask),mid))
        out=[];mixed=0;mixed_profiles=0;empty=0;empty_profiles=0
        for key in sorted(cells):
            rows=cells[key]
            maskids=Counter(mid for _,_,mid in rows)
            if len(maskids)>1:
                mixed+=1;mixed_profiles+=len(rows)
            common=set.intersection(*(m for _,m,_ in rows))
            if not common:
                empty+=1;empty_profiles+=len(rows)
            out.append({'key':list(key),'profiles':len(rows),'mask_ids':dict(sorted(maskids.items())),
                        'common_templates':sorted(common),'mask_pure':len(maskids)==1,'common_template_exists':bool(common)})
        return {'fields':list(fields),'occupied_cells':len(cells),'mixed_mask_cells':mixed,
                'profiles_in_mixed_mask_cells':mixed_profiles,'empty_common_template_cells':empty,
                'profiles_in_empty_common_template_cells':empty_profiles,'cells':out}

    return {'profiles':len(P),'mask_counts':dict(sorted(mc.items())),'coverage_multiplicity':dict(sorted(mult.items())),
            'J_partition':partition(('J',)),'h_J_partition':partition(('h','J')),
            'h_J_D1_rho1_partition':partition(('h','J','D1','rho1')),
            'records':[{'index':i,'mask':mid,**f} for i,mask,mid,f in records]}

def finite_rule(lab,f):
    h,J=f['h'],f['J']
    if lab=='t1':
        return 'A' if J in (14,16) else 'B'
    if lab=='t2':
        if J==12:return 'T0'
        if J%2:return 'T1'
        return 'T2'
    if lab=='t3':
        if h==5:return 'A38'
        if (h,J)==(4,13):return 'A0'
        if (h,J)==(4,14):return 'A1'
        return 'A530'
    raise ValueError(lab)

def rule_audit(lab,summary):
    bad=[];counts=Counter()
    for r in summary['records']:
        choice=finite_rule(lab,r);counts[choice]+=1
        if choice not in r['mask'].split('+'):
            bad.append({'index':r['index'],'h':r['h'],'J':r['J'],'choice':choice,'mask':r['mask']})
    return {'status':'PASS' if not bad else 'FAIL','bad':bad,'assigned_template_counts':dict(sorted(counts.items())),
            'rule':{'t1':'A iff J in {14,16}, else B',
                    't2':'T0 iff J=12; T1 iff J odd; otherwise T2',
                    't3':'A38 if h=5; at h=4 use A0 for J=13, A1 for J=14, otherwise A530'}[lab]}

def main():
    ap=ArgumentParser();ap.add_argument('--t1-script',type=Path,required=True);ap.add_argument('--t2-script',type=Path,required=True);ap.add_argument('--t3-script',type=Path,required=True);ap.add_argument('--t2-demands-json',type=Path,required=True);ap.add_argument('--t2-rows',type=Path,required=True);ap.add_argument('--t3-demands-json',type=Path,required=True);ap.add_argument('--t3-rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    t1=load_module('t1',z.t1_script);t2=load_module('t2',z.t2_script);t3=load_module('t3',z.t3_script)
    P1=[{'s':list(p['s']),'rho':list(p['rho'])} for p in t1.PROFILES]
    M1={name:[t1.certificate_gap(p,th)[0]>0 for p in t1.PROFILES] for name,th in t1.TEMPLATES.items()}
    P2=t2.load(z.t2_demands_json,z.t2_rows);M2={name:[g>0 for g in t2.gaps(P2,th)] for name,th in t2.TEMPLATES.items()}
    P3=t3.load(z.t3_demands_json,z.t3_rows);M3={name:[g>0 for g in t3.gaps_for(P3,th)] for name,th in t3.TEMPLATES.items()}
    if (len(P1),len(P2),len(P3))!=(7,902,94):raise AssertionError((len(P1),len(P2),len(P3)))
    labs={'t1':summarize(P1,M1),'t2':summarize(P2,M2),'t3':summarize(P3,M3)}
    rules={lab:rule_audit(lab,s) for lab,s in labs.items()}
    ok=(all(r['status']=='PASS' for r in rules.values()) and
        all(s['h_J_partition']['empty_common_template_cells']==0 for s in labs.values()) and
        labs['t1']['J_partition']['empty_common_template_cells']==0 and
        labs['t2']['J_partition']['empty_common_template_cells']==0 and
        labs['t3']['J_partition']['empty_common_template_cells']>0)
    out={'schema':'adjacent-t123-validity-mask-audit-exact-v2','status':'PASS' if ok else 'FAIL','labs':labs,'finite_rules':rules,
         'acceptance':'every template gap is recomputed exactly before masks/features; no assignment labels are used to define targets',
         'conclusion':'Complete masks are not determined by (h,J), but every occupied (h,J) cell in t=1,2,3 has a nonempty common exact-template intersection. J alone suffices at t=1,2 and fails at t=3. The displayed finite rules are then checked directly against the independently recomputed masks.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':out['status'],'finite_rules':rules,'partitions':{lab:{'J':{k:v for k,v in s['J_partition'].items() if k!='cells'},'h_J':{k:v for k,v in s['h_J_partition'].items() if k!='cells'}} for lab,s in labs.items()}},indent=2,sort_keys=True))
    if not ok:raise SystemExit(1)
if __name__=='__main__':main()
