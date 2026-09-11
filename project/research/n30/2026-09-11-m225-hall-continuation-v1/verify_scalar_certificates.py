#!/usr/bin/env python3
"""Independent standard-library acceptance of the seven N30 m225 scalar cuts.

Imports no discovery program, solver, old row generator or floating-point code.
The preserved 100-profile list is an explicit input, not proved complete here.
Every source minimum is computed twice: full integer (q,p) domain and the
proved three-endpoint formula. No optimiser status is used as evidence.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import argparse
import json

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'2026-09-11-threshold-tail-v1'
A=13
B=16

def read_profiles(path):
    answer=[]
    for line in path.read_text().splitlines():
        if not line or line.startswith('#'):continue
        lhs,rhs=line.split('|')
        s=tuple(int(x) for x in lhs.split())
        assert len(s)==A and s==tuple(sorted(s)) and 0<=min(s)<=max(s)<=12
        W={h:sum(x for x in s if x>=h) for h in range(2,13)}
        g={}
        for h,w in W.items():
            z=0 if w==0 else h
            while w and 2*w>z*(z-1)+h*(h+1):z+=1
            assert z<=B
            g[h]=z
        g[13]=0
        Q=sum(s)-sum(g.values())
        assert Q==int(rhs.strip().split('=')[1]) and 18<=Q<=21
        answer.append((s,Q,g))
    assert len(answer)==100 and len({s for s,Q,g in answer})==100
    assert Counter(Q for s,Q,g in answer)=={18:64,19:29,20:6,21:1}
    return answer

def rebuild_rows(profiles):
    answer=[]
    for s,Q,g in profiles:
        # Recurse over decreasing residual tails; any unused budget is lambda.
        def extend(h,previous,budget,tails):
            if h==14:
                ns=[B-tails[0]]+[tails[i]-tails[i+1] for i in range(11)]+[tails[-1]]
                rho=tuple(r for r,n in enumerate(ns,1) for _ in range(n))
                assert len(rho)==B and min(rho)>=1 and sum(s)==sum(rho)+2+budget
                answer.append((s,rho,budget))
                return
            for z in range(g[h],min(previous,g[h]+budget)+1):
                extend(h+1,z,budget-(z-g[h]),tails+[z])
        extend(2,B,Q-18,[])
    assert len(answer)==272 and len({(s,rho) for s,rho,lam in answer})==272
    assert sum(lam>0 for s,rho,lam in answer)==61
    assert all(min(s)>0 for s,rho,lam in answer if lam>0)
    tight=sorted((s,rho) for s,rho,lam in answer if lam==0)
    assert len(tight)==211 and sum(min(s)>0 for s,rho in tight)==207
    return tight

def source_minimum(s,r,D,z):
    c=max(s)+3
    qmax=min(A-r,sum(x<=r for x in s))
    # Independent literal evaluation over the entire admissible integer domain.
    values=[]
    for q in range(qmax+1):
        for p in range(r+3):
            assert q+p<=B-1
            alpha=max(0,p-r+1)
            val=D*q*(alpha-c)
            for k,w in z.items():
                val+=w*((q if q>=k+1 else 0)-(p if r+q>=k else 0))
            values.append((val,q,p))
    direct=min(v for v,q,p in values)
    # Separately evaluate the proved closed minimum at p=0,r-1,r+2.
    def Z(j):return sum(w for k,w in z.items() if k<=j)
    closed=min(q*(Z(q-1)-D*c)+min(0,-(r-1)*Z(r+q),3*D*q-(r+2)*Z(r+q)) for q in range(qmax+1))
    assert direct==closed,(s,r,D,z,direct,closed)
    return direct,[(q,p) for v,q,p in values if v==direct],len(values)

def evaluate(s,rho,T):
    D=T['D'];z={int(k):w for k,w in T['weights'].items()}
    assert isinstance(D,int) and not isinstance(D,bool) and D>0
    assert all(isinstance(w,int) and not isinstance(w,bool) and w>=0 and 1<=k<=12 for k,w in z.items())
    mins={};total_checks=0;points={}
    for r,n in Counter(rho).items():
        mins[r],points[r],checks=source_minimum(s,r,D,z);total_checks+=checks
    numerator=D*(max(s)+3)*sum(s)+sum(n*mins[r] for r,n in Counter(rho).items())
    return numerator,mins,points,total_checks

def short_profile(v):
    return ','.join(str(k) if n==1 else f'{k}^{n}' for k,n in sorted(Counter(v).items()))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--certificates',type=Path,default=HERE/'SCALAR_CERTIFICATES.json')
    ap.add_argument('--profiles',type=Path,default=OLD/'N30_M225_QGE18_PROFILES.txt')
    ap.add_argument('--output',type=Path)
    ap.add_argument('--appendix',type=Path)
    ap.add_argument('--remaining',type=Path)
    args=ap.parse_args()
    frontier=rebuild_rows(read_profiles(args.profiles));frontier_set=set(frontier)
    cert=json.loads(args.certificates.read_text());templates=cert['templates']
    assert len(templates)==7 and [T['name'] for T in templates]==[f'T{i}' for i in range(1,8)]
    covered=set();checks=0;records=[]
    appendix=['# Exact scalar-certificate appendix','',
              'Rows are sorted demand/residual multisets. The numerator is `D*c*S + sum n_r L_r`; a positive value is the contradiction. All entries are independently recomputed in integer arithmetic.','',
              '| Template | Demand s | Residual rho | S | L_r by residual degree | Positive numerator | D |',
              '|---|---|---|---:|---|---:|---:|']
    for T,expected in zip(templates,[30,20,3,1,1,1,1]):
        assert len(T['assigned_rows'])==expected
        gaps=[];row_records=[]
        for row in T['assigned_rows']:
            s=tuple(row['s']);rho=tuple(row['rho']);key=(s,rho)
            assert key in frontier_set and key not in covered and min(s)>0
            numerator,mins,points,nchecks=evaluate(s,rho,T);checks+=nchecks
            assert numerator>0,(T['name'],s,rho,numerator)
            covered.add(key);gaps.append(Fraction(numerator,T['D']))
            row_records.append({'s':s,'rho':rho,'minima':mins,'minimizers':points,'numerator':numerator})
            appendix.append(f"| {T['name']} | ({short_profile(s)}) | ({short_profile(rho)}) | {sum(s)} | {mins} | {numerator} | {T['D']} |")
        # Test every template on every row, without using assignment labels.
        coverage=[]
        for s,rho in frontier:
            numerator,mins,points,nchecks=evaluate(s,rho,T);checks+=nchecks
            if numerator>0:coverage.append((s,rho))
        records.append({'name':T['name'],'assigned_count':expected,'full_frontier_coverage':coverage,
                        'minimum_assigned_gap':str(min(gaps)),'rows':row_records})
    assert len(covered)==57
    all_covered={tuple(map(tuple,row)) for rec in records for row in rec['full_frontier_coverage']}
    assert all_covered==covered
    remaining=[{'s':s,'rho':rho} for s,rho in frontier if min(s)>0 and (s,rho) not in covered]
    assert len(remaining)==150
    # Check the label-side algebra over the complete finite degree/excess range.
    label_checks=0
    for s in range(13):
        for e in range(B-s+1):
            assert (s+e)*min(e,3)<=(s+3)*e
            label_checks+=1
    out={'schema':'n30-m225-seven-scalar-exact-audit-v1','status':'PASS',
         'solver_used':False,'floating_point_used':False,'discovery_imported':False,
         'profile_classification_is_external_input':True,
         'profile_input_sha256':sha256(args.profiles.read_bytes()).hexdigest(),
         'certificate_sha256':sha256(args.certificates.read_bytes()).hexdigest(),
         'reconstructed_rows':272,'tight_rows':211,'positive_tight_rows':207,
         'new_scalar_exclusions':57,'positive_rows_remaining_for_stronger_methods':150,
         'zero_demand_rows_with_prior_certificates':4,'integer_source_cases_checked':checks,
         'label_algebra_cases_checked':label_checks,'templates':records}
    if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
    if args.appendix:args.appendix.write_text('\n'.join(appendix)+'\n')
    if args.remaining:args.remaining.write_text(json.dumps(remaining,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='templates'},indent=2))

if __name__=='__main__':main()
