#!/usr/bin/env python3
"""Demand-only inequalities and joint tail closure, before residual expansion."""
from collections import Counter
from pathlib import Path
import csv
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
CSV=ROOT/'project/research/n34/2026-09-12-frontier-v1/FRONTIER.csv'


def main():
    summary={}
    with (HERE/'profile_results.jsonl').open('w') as output:
        for b,t in ((18,1),(19,3),(19,2)):
            counts=Counter();a=15
            for row in csv.DictReader(CSV.open()):
                if int(row['Q_monotone'])<b+2*t:continue
                s=tuple(int(row[f's{i}']) for i in range(a));S=sum(s)
                bounds=[];old={a:0};new={a:0};single=[]
                for h in range(a-1,1,-1):
                    W=sum(v for v in s if v>=h);z=h if W else 0
                    while z*(z-1)+h*(h+1)<2*W:z+=1
                    G=sum(max(4*h,v) for v in s if v>=h)
                    active=b-a<=2*h+1
                    load=(G-2*S+b+4*t+3*h)//(3*h+1) if active else 0
                    old[h]=max(z,old[h+1]);new[h]=max(z,load,new[h+1])
                    gap=(h-1)*G+4*h*b-(5*h-1)*(S-2*t)
                    if active and gap>0:single.append(dict(h=h,gap=gap))
                    bounds.append(dict(h=h,capacity_tail=z,load_tail=load,closed_tail=new[h],active=active))
                before=b+sum(old[h] for h in range(2,a))
                after=b+sum(new[h] for h in range(2,a));budget=S-2*t
                assert before<=budget
                result=('single_threshold_exclusion' if single else
                        'joint_tail_exclusion' if after>budget else 'survives_joint_tail')
                if single:assert after>budget
                counts[result]+=1;counts['profiles']+=1
                if after>before:counts['raised_minimum_residual_budget']+=1
                rec=dict(a=a,b=b,t=t,s=s,result=result,single_threshold_witnesses=single,
                         old_minimum_residual=before,new_minimum_residual=after,residual_budget=budget,tails=bounds)
                output.write(json.dumps(rec,separators=(',',':'))+'\n')
            summary[f'n{a+b+1}-m{b*(a+1)+t}']=dict(counts)
    report=dict(status='COMPLETE_PROFILE_SCAN',layers=summary,external_review='OPEN',
                scope='New necessary profile constraints; surviving profiles are not graphs.')
    (HERE/'profile_summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
