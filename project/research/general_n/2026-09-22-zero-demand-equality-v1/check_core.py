#!/usr/bin/env python3
"""Regression of positive-core identity and bounded r=5 theorem."""
import hashlib,json,sys
from pathlib import Path
import check_support as H
E=H.E

def checked(rows,v,selection,counts):
    p=H.checked(rows,v,selection,counts)
    A=[i for i in range(len(rows)) if i!=v and not(rows[v]>>i&1)]
    B=[u for u in range(len(rows)) if rows[v]>>u&1]
    selected={(u,i):w for u,i,w in selection}
    R={i:sum(not(rows[u]>>i&1) and (u,i) not in selected for u in B) for i in A}
    d={i:sum(bool(rows[i]>>j&1) for j in A) for i in A}
    C=[i for i in A if R[i]];P=[i for i in C if d[i]>R[i]];N=[i for i in C if d[i]<=R[i]]
    ep=sum(bool(rows[i]>>j&1) for i in P for j in P if i<j)
    en=sum(bool(rows[i]>>j&1) for i in N for j in N if i<j)
    assert p['f']-p['r']==ep-en-sum(R[i] for i in P)-sum(R[i]-d[i] for i in N)
    counts['positive_core_identity_checks']+=1
    if 1<=len(C)<=3:
        assert p['f']<p['r']
        counts['support_le_three_cases']+=1
    if p['r']==5:
        assert p['f']<=p['r']
        counts['r_five_cases']+=1
        counts['r_five_equal_product_cases']+=p['f']==p['r']
    if p['S']<=7:
        assert len(E.C.edges(rows))<=len(rows)**2//4
        counts['S_le_seven_cases']+=1
    return p

if __name__=='__main__':
    E.check=checked
    if '--output' not in sys.argv:sys.argv+=['--output','CORE_RESULTS.json']
    E.main()
    output=Path(sys.argv[sys.argv.index('--output')+1]);data=json.loads(output.read_text())
    ledger=data.pop('fixtures')
    data['fixture_ledger_sha256']=hashlib.sha256(json.dumps(ledger,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    data['fixture_ledger_reference']='EQUALITY_RESULTS.json deterministic construction'
    data['core_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data['counts'],indent=2))
