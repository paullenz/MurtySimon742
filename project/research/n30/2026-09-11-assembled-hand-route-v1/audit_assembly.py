#!/usr/bin/env python3
"""Independent integer audit of the assembled N30 supplementary route.

No imports from earlier checkers or discovery programs. The C++ exhaustive
profile data are corroboration of the written classification, not premises
of the mathematical proof. Local envelopes use literal potential formulas.
"""
import argparse
from collections import Counter
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
N30=HERE.parent
CLASS=N30/'2026-09-11-m225-hand-classification-v1'
ENV=N30/'2026-09-11-m225-resource-envelope-v1'

# Transcribed from the four displayed formulas, independently of JSON parser.
RESOURCE={
 'B1':(150,88,150,{2:11,3:107,5:5}),
 'B2':(15,8,17,{2:3,3:4}),
 'B3':(18,4,24,{2:2,3:4}),
 'C1':(25,28,0,{2:22,4:6}),
}
RECT={
 'B1':[(1,13,91),(1,14,142),(2,10,36),(2,11,37),(2,12,61),(4,7,21),(4,8,21),(4,9,32),(4,10,1)],
 'B2':[(1,14,11),(2,7,3),(2,8,2),(2,9,5),(2,10,5),(2,11,5),(2,12,7),(2,13,8)],
 'B3':[(1,12,2),(1,13,11),(1,14,14),(3,11,3),(3,12,1),(4,9,1),(4,10,3)],
 'C1':[],
}
DIAG={'B1':(51,40,40),'B2':(3,6,3),'B3':(4,8,3),'C1':(0,0,0)}
SV={'B1':4,'B2':0,'B3':1,'C1':1}
SH={'B1':150,'B2':14,'B3':7,'C1':0}


def potential(name,s,d,v):
    value=SV[name]*s*v+SH[name]*(s>=2)
    value+=sum(w for k,w in enumerate(DIAG[name]) if d+v+k>=16)
    value+=sum(w for D,V,w in RECT[name] if D<=d and V<=v)
    return value


def g(h,w):
    if w==0:return 0
    z=h
    while z*(z-1)+h*(h+1)<2*w:z+=1
    return z


def tails(s):
    return tuple(g(h,sum(v for v in s if v>=h)) for h in range(2,14))


def reconstruct(s,t):
    base=tails(s);budget=sum(s)-sum(base)-16-2*t
    if budget<0:return []
    # Monotone closure, then add single boxes to a residual Ferrers diagram.
    closed=tuple(max(base[i:]) for i in range(12))
    cost=sum(closed)-sum(base)
    if cost>budget or closed[0]>16:return []
    frontier={closed};rows=[]
    for used in range(cost,budget+1):
        following=set()
        for tail in sorted(frontier):
            full=(16,)+tail+(0,)
            rho=tuple(h for h in range(1,14) for _ in range(full[h-1]-full[h]))
            assert len(rho)==16
            lam=budget-used
            assert sum(s)==sum(rho)+2*t+lam
            rows.append((s,rho,lam))
            if used<budget:
                for i in range(12):
                    if tail[i]+1<=(16 if i==0 else tail[i-1]):
                        nxt=list(tail);nxt[i]+=1;following.add(tuple(nxt))
        frontier=following
    return rows


@lru_cache(None)
def label_min(name,s,H):
    lam,c,mu,tau=RESOURCE[name]
    states=[]
    # Opposite iteration order from the original acceptance checker.
    for x in range(s,H+1):
        for R in range(min(12-s,16-x)+1):
            val=lam*R+c*x+x*potential(name,s,R+s,16-R-x)
            states.append((val,R,x))
    if not states:raise AssertionError('Empty label box')
    return min(states),len(states)


@lru_cache(None)
def source_min(name,r,Q):
    lam,c,mu,tau=RESOURCE[name]
    states=[]
    for p in range(r+3):
        for q in range(Q+1):
            # Written as separate outgoing and incoming tail penalties.
            outgoing=sum(w*q for j,w in tau.items() if j<q)
            incoming=sum(w*p for j,w in tau.items() if j<=r+q)
            val=mu*q-mu*p-c*q+outgoing-incoming-q*potential(name,r,r+q-1,16-q-p)
            assert q+p<=15
            states.append((val,q,p))
    return min(states),len(states)


# Eight m226 certificates, transcribed from the hand endpoint table.
M226=[
 ((2,2)+(3,)*11,(1,)*7+(2,)+(3,)*8,2,6,{2:6,5:1,6:1,8:1},{1:0,2:-42,3:-50},2),
 ((2,)+(3,)*12,(1,)*7+(3,)*9,2,6,{2:3,3:4,6:1,8:1},{1:0,3:-50},6),
 ((3,)*13,(1,)*7+(3,)*8+(4,),2,6,{2:7,6:1,7:1},{1:0,3:-48,4:-60},24),
 ((3,)*13,(1,)*6+(2,)+(3,)*9,2,6,{2:3,3:4,6:1,8:1},{1:0,2:-12,3:-50},6),
 ((3,)*4+(4,)*9,(1,)*6+(3,)*2+(4,)*8,3,7,{2:11,5:1,6:1,7:2},{1:0,3:-90,4:-102},12),
 ((3,)*2+(4,)*11,(1,)*5+(2,)+(3,)+(4,)*9,3,7,{2:6,3:3,4:3,6:1,7:1,8:1},{1:0,2:-24,3:-90,4:-102},18),
 ((3,)+(4,)*12,(1,)*5+(2,)+(4,)*10,2,7,{2:3,3:3,5:3,8:1},{1:0,2:-12,4:-70},2),
 ((4,)*13,(1,)*5+(3,)+(4,)*10,2,7,{1:1,2:5,4:1,5:1,6:1,7:1},{1:-3,3:-30,4:-68},3),
]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--envelopes-output',type=Path);args=ap.parse_args()
    reg=json.loads((HERE/'PROFILE_REGRESSION.json').read_text())
    r13,r12=reg['runs']
    assert reg['status']=='PASS' and r13['a']==13 and r12['a']==12
    assert r13['profiles_tested']==5200300 and r12['profiles_tested']==1352078
    assert r13['maximum_Q']==21 and r12['maximum_Q']==18
    historical=[]
    for line in (CLASS/'HAND_CLASSIFIED_PROFILES.txt').read_text().splitlines():
        if line and not line.startswith('#'):
            left,right=line.split('|');historical.append({'s':list(map(int,left.split())),'Q':int(right.split('=')[1])})
    assert historical==r13['high_profiles']
    profiles=[tuple(r['s']) for r in historical]
    assert len(profiles)==100
    # Check every independent literal potential coefficient against the saved
    # final certificate; no saved evaluator is imported or called.
    saved=json.loads((ENV/'JOINT_CERTIFICATES.json').read_text())
    for T in saved['templates']:
        name=T['name'];lam,c,mu,tau=RESOURCE[name]
        assert (T['lambda'],T['c'],T['mu'])==(lam,c,mu)
        assert {int(k):v for k,v in T['tau'].items()}==tau
        expected={}
        if SV[name]:expected['sv']=SV[name]
        if SH[name]:expected['sh2']=SH[name]
        expected.update({f'diag_{k}':w for k,w in enumerate(DIAG[name]) if w})
        expected.update({f'bc_{D}_{V}':w for D,V,w in RECT[name]})
        assert expected==T['potential']
    old=json.loads((ENV/'EXACT_AUDIT.json').read_text())
    old_by_row={(tuple(r['s']),tuple(r['rho'])):r for r in old['rows']}
    all225=[r for s in profiles for r in reconstruct(s,1)]
    all226=[r for s in profiles for r in reconstruct(s,2)]
    assert len(all225)==len(set(all225))==272
    assert len(all226)==len(set(all226))==9
    tight225=[(s,r) for s,r,l in all225 if not l]
    tight226=[(s,r) for s,r,l in all226 if not l]
    assert len(tight225)==211 and len(tight226)==8
    assert all(min(s)>0 for s,r,l in all225+all226 if l)
    assert set(tight225)==set(old_by_row)
    counts=Counter();records=[];local_labels={};local_sources={}
    for s,rho in sorted(tight225):
        row_gaps={};chosen=None
        for name in RESOURCE:
            ell={};sigma={}
            for si in set(s):
                H=sum(r>=si for r in rho)
                val,n=label_min(name,si,H);ell[si]=val[0]
                local_labels[name,si,H]={'name':name,'demand':si,'H':H,'minimum':val[0],'R':val[1],'x':val[2],'states':n}
            for r in set(rho):
                Q=min(13-r,sum(si<=r for si in s))
                val,n=source_min(name,r,Q);sigma[r]=val[0]
                local_sources[name,r,Q]={'name':name,'rho':r,'Q':Q,'minimum':val[0],'q':val[1],'p':val[2],'states':n}
            gap=sum(ell[si] for si in s)+sum(sigma[r] for r in rho)-RESOURCE[name][0]*sum(rho)
            row_gaps[name]=gap
            if gap>0 and chosen is None:chosen=name;counts[name]+=1
            if name==old_by_row[s,rho]['assigned']:
                original=old_by_row[s,rho]['chosen_envelopes']
                assert ell=={int(k):v for k,v in original['ell'].items()}
                assert sigma=={int(k):v for k,v in original['sigma'].items()}
        assert chosen is not None
        assert row_gaps==old_by_row[s,rho]['template_gaps']
        records.append({'s':s,'rho':rho,'gaps':row_gaps,'assigned':chosen,'assigned_gap':row_gaps[chosen]})
    assert dict(counts)=={'B1':195,'B3':2,'B2':13,'C1':1}
    assert min(r['assigned_gap'] for r in records)==1

    expected226={(s,rho) for s,rho,D,c,z,L,gap in M226}
    assert set(tight226)==expected226
    m226_checks=0;m226_records=[]
    for s,rho,D,c,z,L,expected_gap in M226:
        found={}
        for r in set(rho):
            values=[]
            for p in range(r+3):
                for q in range((13-r if r>=min(s) else 0)+1):
                    alpha=max(0,p-r+1)
                    val=D*q*(alpha-c)+sum(w*q for k,w in z.items() if q>k)-sum(w*p for k,w in z.items() if r+q>=k)
                    values.append(val);m226_checks+=1
            found[r]=min(values)
        assert found==L
        gap=D*c*sum(s)+sum(L[r] for r in rho)
        assert gap==expected_gap and gap>0
        m226_records.append({'s':s,'rho':rho,'D':D,'integer_gap':gap})

    # The source-independent Q_12<=18 lemma pads any a<=12 with zeros.
    outer=[]
    for b in range(17,29):
        a=29-b;t=225-b*(30-b);lower=b+2*t
        assert 1<=a<=12 and t>0 and lower>18
        outer.append({'Delta':b,'a':a,'t_at_m225':t,'necessary_Q_at_m225':lower,'hand_Q_upper':18,'strict_margin':lower-18})
    result={
      'schema':'n30-independent-assembly-audit-v1','status':'PASS',
      'earlier_checker_or_discovery_imports':False,'solver_used':False,'floating_point_used':False,
      'profile_regression_is_corroboration_only':True,
      'profile_regression_counts':[r13['profiles_tested'],r12['profiles_tested']],
      'profile_list_match':True,'m225_rows':272,'m225_ledger_exclusions':61,'m225_envelope_exclusions':211,
      'm225_assigned_counts':dict(counts),'m225_minimum_gap':1,
      'm225_local_states':sum(x['states'] for x in local_labels.values())+sum(x['states'] for x in local_sources.values()),
      'all_original_844_template_gaps_match':True,
      'm226_rows':9,'m226_ledger_exclusions':1,'m226_hand_exclusions':8,'m226_source_states':m226_checks,
      'Delta16_m_ge_227':'Q>=22 contradicts hand Q<=21',
      'Delta17_all_positive_surplus':'Q>=19 contradicts source-independent hand Q<=18; m<=221',
      'higher_degrees':outer,
      'Delta15_equality':'Direct regular-critical argument in ASSEMBLED_PROOF.md; no dominating-edge theorem premise',
      'external_review':'OPEN','governed_ledger_promotion':False,
      'm226_certificates':m226_records,
      'proof_critical_finite_arithmetic_retained':'The explicit 100-profile tables, residual-tail reconstruction and endpoint integer-envelope tables remain part of the written proof route.',
      'input_hashes':{str(p.relative_to(N30.parents[2])):sha256(p.read_bytes()).hexdigest() for p in [HERE/'PROFILE_REGRESSION.json',CLASS/'HAND_CLASSIFIED_PROFILES.txt',ENV/'JOINT_CERTIFICATES.json',ENV/'EXACT_AUDIT.json']},
    }
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    if args.envelopes_output:args.envelopes_output.write_text(json.dumps({'labels':list(local_labels.values()),'sources':list(local_sources.values()),'rows':records},indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['higher_degrees','m226_certificates','input_hashes']},indent=2))


if __name__=='__main__':main()
