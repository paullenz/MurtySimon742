#!/usr/bin/env python3
"""Exact row-wise audit of the written threshold-capacity lemma on n=29,t=3.

This is deliberately a diagnostic, not a proof-status promotion.  It takes the
fresh minimal-kernel demand records and residual-row survivors and applies the
standalone threshold-capacity inequality literally to each paired (s,rho) row:

    I_h={i:s_i>=h}, W_h=sum_{i in I_h}s_i,
    z_h=#{u:rho_u>=h},
    2 W_h <= z_h^2-z_h+h(h+1).

The script records, but does not assume in advance, how many current abstract
rows survive the row-specific inequality.  All arithmetic is integer exact.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import json

A=12
B=16
T=3


def threshold_violations(s,rho):
    out=[]
    for h in range(2,A):
        high=[x for x in s if x>=h]
        if not high:
            continue
        W=sum(high)
        z=sum(r>=h for r in rho)
        lhs=2*W
        rhs=z*z-z+h*(h+1)
        if lhs>rhs:
            out.append({'h':h,'W':W,'z':z,'lhs':lhs,'rhs':rhs,'excess':lhs-rhs})
    return out


def source_count_violations(s,rho):
    H=max(s,default=0)
    if H<=0:
        return []
    z=sum(r>=H for r in rho)
    return [] if z>=H else [{'H':H,'z_H':z,'deficit':H-z}]


def main():
    ap=ArgumentParser()
    ap.add_argument('--demands-json',type=Path,required=True)
    ap.add_argument('--rows',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    z=ap.parse_args()

    D=json.loads(z.demands_json.read_text())
    rows=[]
    for line in z.rows.read_text().splitlines():
        if not line.strip():
            continue
        v=list(map(int,line.split()))
        if len(v)!=18:
            raise AssertionError(('row_width',len(v),line))
        did,total=v[0],v[1]
        rho=v[2:]
        if not (0<=did<len(D)):
            raise AssertionError(('demand_id',did,len(D)))
        if sum(rho)!=total:
            raise AssertionError(('row_total',did,total,sum(rho)))
        s=D[did]['s']
        if len(s)!=A or len(rho)!=B:
            raise AssertionError(('dimensions',len(s),len(rho)))
        tv=threshold_violations(s,rho)
        sv=source_count_violations(s,rho)
        rows.append({
            'demand_id':did,
            'total_r':total,
            's':s,
            'rho':rho,
            'positive_demands':min(s)>0,
            'zero_slack':sum(s)==sum(rho)+2*T,
            'threshold_pass':not tv,
            'threshold_violations':tv,
            'source_count_pass':not sv,
            'source_count_violations':sv,
        })

    # Canonical t=3 minimal-kernel count; protects against silently auditing a
    # different frontier while leaving the mathematical outcome unconstrained.
    if len(rows)!=126:
        raise AssertionError(('expected_126_minimal_rows',len(rows)))

    first_h=Counter()
    all_h=Counter()
    source_bad=0
    for r in rows:
        if r['threshold_violations']:
            first_h[r['threshold_violations'][0]['h']]+=1
            for q in r['threshold_violations']:
                all_h[q['h']]+=1
        if not r['source_count_pass']:
            source_bad+=1

    zp=[r for r in rows if r['positive_demands'] and r['zero_slack']]
    if len(zp)!=94:
        raise AssertionError(('expected_94_positive_zero_slack_rows',len(zp)))

    survivors=[r for r in rows if r['threshold_pass']]
    zp_survivors=[r for r in zp if r['threshold_pass']]

    out={
        'schema':'n29-t3-rowwise-threshold-audit-exact-v1',
        'status':'PASS',
        'scope':{'n':29,'Delta':16,'a':A,'b':B,'t':T,'m':211},
        'minimal_rows':len(rows),
        'rowwise_threshold_pass':len(survivors),
        'rowwise_threshold_rejected':len(rows)-len(survivors),
        'all_minimal_rows_rejected':len(survivors)==0,
        'positive_zero_slack_rows':len(zp),
        'positive_zero_slack_threshold_pass':len(zp_survivors),
        'all_positive_zero_slack_rows_rejected':len(zp_survivors)==0,
        'first_violation_h_census':{str(k):v for k,v in sorted(first_h.items())},
        'all_violation_h_census':{str(k):v for k,v in sorted(all_h.items())},
        'source_count_rejections':source_bad,
        'threshold_survivors':survivors,
        'arithmetic':'exact integer',
        'solver_used':False,
        'floating_point_used':False,
        'interpretation':'Diagnostic application of the written threshold-capacity lemma to each freshly regenerated minimal-kernel (s,rho) row. Any apparent simplification must still be reconciled with the graph-to-profile semantics and the standalone lemma before changing proof status.'
    }
    z.output.parent.mkdir(parents=True,exist_ok=True)
    z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:out[k] for k in ['status','minimal_rows','rowwise_threshold_pass','rowwise_threshold_rejected','positive_zero_slack_rows','positive_zero_slack_threshold_pass','first_violation_h_census','source_count_rejections']},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
