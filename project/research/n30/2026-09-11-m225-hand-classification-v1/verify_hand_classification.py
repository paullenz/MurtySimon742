#!/usr/bin/env python3
"""Audit the written, bounded threshold-table classification; no profile sweep.

The historical 100-profile file is read only under --compare-historical, after
the new list has been derived. No discovery imports, solver or float is used.
"""
from __future__ import annotations
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
HISTORICAL = HERE.parent / '2026-09-11-threshold-tail-v1/N30_M225_QGE18_PROFILES.txt'

# Table 1 of the proof: (p,x) -> z -> precisely the allowed y values.
CAP4 = {
    (12, 12): {0: [11, 12], 11: [12], 12: [12]},
    (13, 11): {0: [9, 11]},
    (13, 12): {
        0: [0, 7, 9, 10, 11, 12], 3: [12], 4: [10, 11, 12],
        5: [12], 6: [12], 9: [11, 12], 10: [12],
        11: [11, 12], 12: [12],
    },
    (13, 13): {
        0: [0, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13], 2: [13],
        3: [10, 12, 13], 4: [9, 10, 11, 12, 13],
        5: [11, 12, 13], 6: [11, 12, 13], 7: [11, 12, 13],
        8: [11, 12, 13], 9: [10, 11, 12, 13],
        10: [10, 11, 12, 13], 11: [11, 12, 13],
        12: [12, 13], 13: [13],
    },
}

# Table 2: a cap-five survivor has p=x=13 and these (y,z,k).
CAP5 = {
    (12, 10): [5],
    (12, 12): [5, 6, 7, 12],
    (13, 10): [5, 6],
    (13, 11): [5, 6, 7, 8, 10, 11],
    (13, 12): [4, 5, 6, 7, 10, 12],
    (13, 13): [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
}
CAP6_MAX = {(12, 10): 14, (12, 12): 15, (13, 10): 15,
            (13, 11): 15, (13, 12): 16, (13, 13): 16}


def capacity(h, z):
    return (z * (z - 1) + h * (h + 1)) // 2


def threshold(h, w):
    if w == 0:
        return 0
    return next(z for z in range(h, 17) if w <= capacity(h, z))


def score(s):
    return sum(s) - sum(threshold(h, sum(v for v in s if v >= h))
                        for h in range(2, 13))


def deficit4(x, y, z):
    return x + y + z - threshold(2, 2*x+y+z) - threshold(3, 3*y+z) - threshold(4, 4*z)


def score5(p, x, y, z, k):
    return p+x+y+z+k-threshold(2, 2*x+y+z+k)-threshold(3, 3*y+z+k)-threshold(4, 4*z+k)-threshold(5, 5*k)


def score6(y, z, k, j):
    return 26+y+z+k+j-threshold(2, 26+y+z+k+j)-threshold(3, 3*y+z+k+j)-threshold(4, 4*z+k+j)-threshold(5, 5*k+j)-threshold(6, 6*j)


def demands(p, x, y, z, k=0):
    return (0,)*(13-p)+(1,)*(p-x)+(2,)*(x-y)+(3,)*(y-z)+(4,)*(z-k)+(5,)*k


def interval_values(limit, terms, constant, cutoff=18):
    """Invert capacities independently of threshold() and of score5/score6.

    For f(v)=constant+v-sum g_h(base+slope*v), all bases here are
    nonnegative and slopes positive. A threshold changes just after
    floor((C_h(z)-base)/slope). Between those boundaries f rises by one.
    """
    cuts = {1, limit+1}
    for h, base, slope in terms:
        for z in range(h, 17):
            after = (capacity(h, z)-base)//slope+1
            if 1 < after <= limit:
                cuts.add(after)
    cuts = sorted(cuts)
    segments = []
    accepted = []
    for lo, stop in zip(cuts, cuts[1:]):
        hi = stop-1
        # g_h(w)=h + #{z>=h:C_h(z)<w}, independently of first-fit.
        gs = [h+sum(capacity(h,z)<base+slope*lo for z in range(h,16))
              for h,base,slope in terms]
        offset = constant-sum(gs)
        accepted.extend(range(max(lo, cutoff-offset), hi+1))
        segments.append({'lo':lo,'hi':hi,'thresholds':gs,'offset':offset,'max_score':offset+hi})
    return accepted, segments


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path)
    ap.add_argument('--profiles-output', type=Path)
    ap.add_argument('--appendix', type=Path)
    ap.add_argument('--compare-historical', action='store_true')
    args = ap.parse_args()
    checks = {}

    # The clipping proof holds with arbitrary 0/1 entries, not just s_i>=2.
    high_defects = {str(h): [-e*e+3*e+2*h-2 for e in range(14-h)] for h in range(8,13)}
    assert all(v>0 for a in high_defects.values() for v in a)
    for k in range(1,13):
        assert k-threshold(7,7*k)<=0
    assert 13-threshold(7,91)==1
    assert threshold(6,91)-threshold(6,78)==1
    clip6=[]
    clip5=[]
    for k in range(1,14):
        d6=k-threshold(6,6*k)
        if d6>0:
            assert k in (11,12,13) and d6==1
            for l in range(14-k):
                drop=threshold(5,6*k+5*l)-threshold(5,5*(k+l))
                assert drop>=d6
                clip6.append([k,l,d6,drop])
        d5=k-threshold(5,5*k)
        if d5>0:
            assert k in (10,11,12,13)
            for l in range(14-k):
                drop4=threshold(4,5*k+4*l)-threshold(4,4*(k+l))
                # At most one non-4/5 label remains when another unit is needed.
                extra=0
                if k==12 and l==0:
                    extra=min(threshold(3,60+(3 if v==3 else 0))-threshold(3,48+(3 if v==3 else 0)) for v in range(4))
                elif k==12 and l==1:
                    extra=threshold(3,64)-threshold(3,52)
                elif k==13:
                    extra=threshold(3,65)-threshold(3,52)
                assert drop4+extra>=d5
                clip5.append([k,l,d5,drop4,extra])
    checks['clipping_with_zero_and_one_entries']=True

    # Padding the >=2 part by a 2: threshold rises by at most one.
    assert all(threshold(2,w+2)-threshold(2,w)<=1 for w in range(2,51))
    f10=[deficit4(10,y,0) for y in range(11)]
    assert f10==[3,1,2,3,3,2,2,3,3,4,4]
    assert all(z-threshold(4,4*z)<=0 for z in range(9))
    f10_high=[deficit4(10,y,z) for z in (9,10) for y in range(z,11)]
    assert f10_high==[2,3,2]
    f11_edge=[deficit4(11,11,z) for z in range(12)]
    assert f11_edge==[5,2,2,3,4,4,4,3,3,4,3,4]
    checks['N2_at_most_10_deficit_at_most_4']=True
    checks['N2_at_most_11_deficit_at_most_5']=True

    cap4=[]
    cap4_states=0
    cap4_max={}
    for (p,x),table in CAP4.items():
        got={}
        values=[]
        for z in range(x+1):
            good=[]
            for y in range(z,x+1):
                q=p+deficit4(x,y,z)
                cap4_states+=1
                values.append(q-p)
                assert q==score(demands(p,x,y,z))
                if q>=18:
                    good.append(y)
                    cap4.append((p,x,y,z))
            if good:
                got[z]=good
        assert got==table, ((p,x),got)
        cap4_max[f'{p},{x}']=max(values)
    assert len(cap4)==70
    assert cap4_max=={'12,12':6,'13,11':5,'13,12':6,'13,13':8}
    checks['cap_four_table_complete']=True

    five_details=[]
    derived5=[]
    cap5_states=0
    for p,x,y,z in cap4:
        if not z:
            continue
        direct=[k for k in range(1,z+1) if score5(p,x,y,z,k)>=18]
        intervals,segments=interval_values(z,[(2,2*x+y+z,1),(3,3*y+z,1),(4,4*z,1),(5,0,5)],p+x+y+z)
        assert direct==intervals
        # Verify the complete affine intervals, not only their accepted points.
        for segment in segments:
            for k in range(segment['lo'],segment['hi']+1):
                assert score5(p,x,y,z,k)==segment['offset']+k
                assert score5(p,x,y,z,k)==score(demands(p,x,y,z,k))
                cap5_states+=1
        derived5.extend((p,x,y,z,k) for k in intervals)
        five_details.append({'p':p,'x':x,'y':y,'z':z,'accepted_k':intervals,'segments':segments})
    expected5=sorted((13,13,y,z,k) for (y,z),ks in CAP5.items() for k in ks)
    assert sorted(derived5)==expected5 and len(derived5)==30
    assert cap5_states==366
    checks['all_cap_five_preimages_classified']=True

    six_details=[]
    group_max={}
    cap6_states=0
    for p,x,y,z,k in expected5:
        direct=[score6(y,z,k,j) for j in range(1,k+1)]
        accepted,segments=interval_values(k,[(2,26+y+z+k,1),(3,3*y+z+k,1),(4,4*z+k,1),(5,5*k,1),(6,0,6)],26+y+z+k)
        for segment in segments:
            for j in range(segment['lo'],segment['hi']+1):
                assert score6(y,z,k,j)==segment['offset']+j
                s=(2,)*(13-y)+(3,)*(y-z)+(4,)*(z-k)+(5,)*(k-j)+(6,)*j
                assert score6(y,z,k,j)==score(s)
                cap6_states+=1
        assert not accepted and max(direct)<=16
        assert max(s['max_score'] for s in segments)==max(direct)
        group_max[y,z]=max(group_max.get((y,z),-100),max(direct))
        six_details.append({'y':y,'z':z,'k':k,'max_Q':max(direct),'scores_by_j':direct,'segments':segments})
    assert group_max==CAP6_MAX
    checks['no_preimage_with_six_or_more']=True

    profiles=sorted([demands(*r) for r in cap4]+[demands(*r) for r in expected5])
    assert len(profiles)==len(set(profiles))==100
    distribution=dict(sorted(Counter(score(s) for s in profiles).items()))
    text='# Hand-classified n=30 Delta=16 m=225 demand frontier: Q>=18\n# Derived by the clipping and preimage tables; no historical list used.\n'
    text+=''.join(' '.join(map(str,s))+f' | Q={score(s)}\n' for s in profiles)
    historical=None
    if args.compare_historical:
        old=[]
        for line in HISTORICAL.read_text().splitlines():
            if not line or line.startswith('#'):
                continue
            left,right=line.split('|')
            old.append((tuple(map(int,left.split())),int(right.strip().split('=')[1])))
        assert old==[(s,score(s)) for s in profiles]
        historical={'match':True,'sha256':sha256(HISTORICAL.read_bytes()).hexdigest()}
    out={
        'schema':'n30-m225-hand-classification-v1','status':'PASS',
        'solver_used':False,'floating_point_used':False,'full_multiset_sweep_used':False,
        'historical_profiles_used_for_derivation':False,
        'checks':checks,'cap4_profiles':70,'cap5_profiles':30,'total_profiles':100,
        'score_distribution':distribution,'maximum_demand':5,
        'cap4_arithmetic_states':cap4_states,'cap5_arithmetic_states':cap5_states,'cap6_arithmetic_states':cap6_states,
        'high_tail_defects':high_defects,'clip6_payment_table':clip6,'clip5_payment_table':clip5,
        'N2_10_z0_deficits':f10,'N2_10_high_z_deficits':f10_high,'N2_11_y11_deficits':f11_edge,
        'cap4_max_D':cap4_max,'cap4_table':[{'p':p,'x':x,'z':z,'y':ys} for (p,x),rows in CAP4.items() for z,ys in rows.items()],
        'cap5_table':[{'y':y,'z':z,'k':ks,'max_cap6_Q':CAP6_MAX[y,z]} for (y,z),ks in CAP5.items()],
        'cap5_preimage_intervals':five_details,'cap6_preimage_intervals':six_details,
        'generated_profiles_sha256':sha256(text.encode()).hexdigest(),'historical_comparison':historical,
        'trust_boundary':'Candidate written hand classification with explicit finite arithmetic tables; code internally corroborates those tables. Universal bridge and external specialist review remain separate obligations.',
    }
    if args.profiles_output:
        args.profiles_output.write_text(text)
    if args.output:
        args.output.write_text(json.dumps(out,indent=2)+'\n')
    if args.appendix:
        lines=['# Complete preimage arithmetic','',
               'Companion to the written hand classification. Each interval records the affine formula `Q(v)=offset+v`; threshold vectors are constant throughout it. The final point therefore attains the interval maximum. All omitted accepted-value sets below are empty.','',
               '## Cap-five lifts of every cap-four profile containing a four','',
               '| p,x,y,z | k interval | (g2,g3,g4,g5) | Q(k) | accepted k |','|---|---|---|---|---|']
        for r in five_details:
            for a in r['segments']:
                good=[k for k in r['accepted_k'] if a['lo']<=k<=a['hi']]
                lines.append(f"| {r['p']},{r['x']},{r['y']},{r['z']} | {a['lo']}–{a['hi']} | {','.join(map(str,a['thresholds']))} | {a['offset']}+k | {','.join(map(str,good)) or 'none'} |")
        lines+=['','## Cap-six lifts of all thirty cap-five survivors','',
                '| y,z,k | j interval | (g2,g3,g4,g5,g6) | Q(j) | interval maximum |','|---|---|---|---|---|']
        for r in six_details:
            for a in r['segments']:
                lines.append(f"| {r['y']},{r['z']},{r['k']} | {a['lo']}–{a['hi']} | {','.join(map(str,a['thresholds']))} | {a['offset']}+j | {a['max_score']} |")
        lines+=['','No interval in the second table reaches 18.','']
        args.appendix.write_text('\n'.join(lines))
    print(json.dumps({k:out[k] for k in ['status','cap4_profiles','cap5_profiles','total_profiles','score_distribution','maximum_demand','cap4_arithmetic_states','cap5_arithmetic_states','cap6_arithmetic_states','historical_comparison']}))


if __name__=='__main__':
    main()
