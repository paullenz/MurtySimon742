#!/usr/bin/env python3
"""Actual-graph replay of residual-support and exact core ledger."""
import hashlib
import json
from pathlib import Path
import sys
import check_unit_columns as U
E=U.E
witnesses={}

def checked(rows,v,selection,counts):
    p=U.checked(rows,v,selection,counts)
    A=[i for i in range(len(rows)) if i!=v and not(rows[v]>>i&1)]
    B=[u for u in range(len(rows)) if rows[v]>>u&1]
    selected={(u,i):w for u,i,w in selection}
    R={i:sum(not(rows[u]>>i&1) and (u,i) not in selected for u in B) for i in A}
    d={i:sum(bool(rows[i]>>j&1) for j in A) for i in A}
    x={i:sum((u,i) in selected for u in B) for i in A}
    C=[i for i in A if R[i]];T=[i for i in A if not R[i]]
    core=sum(bool(rows[i]>>j&1) for i in C for j in C if i<j)
    for c in C:
        if any(rows[c]>>i&1 for i in T):
            assert x[c]==0 and d[c]<=R[c]
            counts['boundary_lemma_checks']+=1
    positive=sum(max(0,d[c]-R[c]) for c in C)
    slack=sum(max(0,R[c]-d[c]) for c in C)
    assert p['f']-p['r']==positive-slack-core
    counts['core_ledger_checks']+=1
    for key,cond in [('independent_support',bool(C) and core==0),('two_support',1<=len(C)<=2),('r_le_four',1<=p['r']<=4)]:
        if cond:
            assert p['f']<=p['r']-1
            counts[key+'_cases']+=1
            counts[key+'_nonempty_F']+=bool(p['f'])
            if p['f']:witnesses.setdefault(key,{'n':len(rows),'root':v,'R':R,'d':d,'core_edges':core,'selection':selection,'edges':E.C.edges(rows)})
    if len(C)>=3 and core==0 and p['f']:
        counts['independent_support_three_or_more_nonempty']+=1
        witnesses.setdefault('independent_support_three_or_more',{'n':len(rows),'root':v,'R':R,'d':d,'selection':selection,'edges':E.C.edges(rows)})
    if p['S']<=4:
        assert len(E.C.edges(rows))<=len(rows)**2//4
        counts['S_le_four_cases']+=1
    return p

if __name__=='__main__':
    E.check=checked
    if '--output' not in sys.argv:sys.argv+=['--output','SUPPORT_RESULTS.json']
    E.main()
    output=Path(sys.argv[sys.argv.index('--output')+1]);data=json.loads(output.read_text())
    ledger=data.pop('fixtures')
    data['fixture_ledger_sha256']=hashlib.sha256(json.dumps(ledger,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    data['fixture_ledger_reference']='EQUALITY_RESULTS.json deterministic fixture/root construction; unchanged parameters'
    data['support_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data['witnesses']=witnesses
    output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data['counts'],indent=2))
