#!/usr/bin/env python3
"""Exact regression on the finite N34 domain; the theorem has a hand proof."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent


def main():
    def f(load):return sum(load<=k for k in (2,3,4,5))
    labels=[];sources=[]
    for R in range(12):
        for x in range(2,min(8,18-R)+1):
            val=2*R+2*x+x*f(R+x);assert val>=12;labels.append(val)
    for q in range(14):
        for p in range(min(4,17-q)+1):
            for H in range(max(0,q-2),q+1):
                val=12+2*((H if H>2 else 0)-p)-2*H-H*f(q+p)
                assert val>=0;sources.append(val)
    assert 6*13>26+6*8
    report=dict(status='PASS',label_options=len(labels),source_options=len(sources),
        minimum_label_cost=min(labels),minimum_source_slack=min(sources),
        contradiction=dict(required_lower=78,allowed_upper=74),external_review='OPEN')
    (HERE/'hand_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
