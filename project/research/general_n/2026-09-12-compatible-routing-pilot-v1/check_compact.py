#!/usr/bin/env python3
"""Corroborate the hand source bounds and the worked state's arithmetic."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def main():
    checks=0;best={}
    for j in (5,6):
        for H in range(41):
            for q in range(H,H+41):
                for p in range(8):
                    e=int(H>4)
                    v=5*H+H*sum(q+p<=k for k in range(4,16))-2*H*e+2*min(p,j-e)+4*p-4*q*int(q>2)
                    assert v<=(56 if e else 64);checks+=1
                    best[j,e]=max(best.get((j,e),v),v)
    capacities=[4*(10-j)+j*(10-j)+j*(j-1)//2 for j in range(11)]
    allowed=[j for j,c in enumerate(capacities) if c>=55];assert allowed==[5,6]
    assert 4*(208-57)+55==659
    bounds={j:36+64*(10-j)+56*j for j in allowed}
    assert bounds=={5:636,6:628}
    report=dict(status='PASS',local_options_checked=checks,local_maxima={str(k):v for k,v in best.items()},
        allowed_j=allowed,required=659,source_upper_bounds=bounds,gaps={j:659-v for j,v in bounds.items()},
        scope='H=0..40, q=H..H+40, p=0..7, j=5 or 6; hand proof establishes unbounded local scope',external_review='OPEN')
    (HERE/'compact_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
