#!/usr/bin/env python3
"""Cross-check recursive residual domains against the earlier breadth expansion."""
import hashlib
import json
import sys
from frontier import HERE,CSV,expand

sys.path.insert(0,str(CSV.parent))
import check_frontier as legacy


def main():
    assert hashlib.sha256(CSV.read_bytes()).hexdigest()=='35f4569b93d80015e91f995ac0b905955496e57e276f0aad67cdd12b6d6530c4'
    legacy.B=19
    layers={}
    for t in (3,2):
        new,stats=expand(t);old,oldstats=legacy.expand(t)
        assert set(new)==set(old) and stats==oldstats
        zeros=[]
        for s,rho in new:
            if not min(s):
                E=sum(s)-sum(rho)-2*t
                assert E>=0 and (E==0 or s.count(0)<=1)
                zeros.append(dict(s=s,rho=rho,zero_labels=s.count(0),deficit=E))
        layers[str(t)]=dict(states=len(new),profiles=stats['profiles'],exact_state_set_agreement=True,zero_states=zeros)
    assert 2*306>35*17 and 21*12>=35*7 and 20*15<306
    assert 19+2*3<=26<19+2*4
    report=dict(status='PASS',csv_sha256=hashlib.sha256(CSV.read_bytes()).hexdigest(),
        layers=layers,independence='separate internal implementations; shared complete demand CSV',external_review='OPEN')
    (HERE/'frontier_audit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
