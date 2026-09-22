#!/usr/bin/env python3
"""Actual-graph replay for the local unit-cycle and r<=5 closure."""
import hashlib,json,sys
from pathlib import Path
import check_core as H
E=H.E

def checked(rows,v,selection,counts):
    p=H.checked(rows,v,selection,counts)
    A=[i for i in range(len(rows)) if i!=v and not(rows[v]>>i&1)]
    B=[u for u in range(len(rows)) if rows[v]>>u&1]
    selected={(u,i):w for u,i,w in selection}
    R={i:sum(not(rows[u]>>i&1) and (u,i) not in selected for u in B) for i in A}
    # Exact F-components.
    unseen=set(A);components=[]
    while unseen:
        stack=[unseen.pop()];comp=set(stack)
        while stack:
            i=stack.pop()
            for j in list(unseen):
                if rows[i]>>j&1:
                    unseen.remove(j);comp.add(j);stack.append(j)
        components.append(comp)
    f=sum(bool(rows[i]>>j&1) for x,i in enumerate(A) for j in A[x+1:])
    r=sum(R.values());t=f-r
    for q in components:
        if len(q)>=3 and all(R[i]==1 and sum(bool(rows[i]>>j&1) for j in q)==2 for i in q):
            counts['unit_cycle_components']+=1
            if t==0 and len(B)>len(q):
                counts['forbidden_local_cycle_premises']+=1
                raise AssertionError(('local unit cycle',len(rows),v,q,R,selection))
    if 1<=r<=5:
        assert f<=r-1
        counts['r_at_most_five_cases']+=1
        counts['r_at_most_five_nonempty_F']+=bool(f)
    if p['S']<=5:
        m=len(E.C.edges(rows));n=len(rows)
        assert m<=n*n//4
        counts['S_le_five_cases']+=1
        if m==n*n//4:
            fedges=[(i,j) for x,i in enumerate(A) for j in A[x+1:] if rows[i]>>j&1]
            assert not selection and not fedges and r==0
            assert all(rows[i]>>u&1 for i in A+[v] for u in B)
            counts['S_le_five_equality_cases']+=1
    return p

if __name__=='__main__':
    E.check=checked
    if '--output' not in sys.argv:sys.argv+=['--output','LOCAL_CYCLE_RESULTS.json']
    E.main()
    output=Path(sys.argv[sys.argv.index('--output')+1]);data=json.loads(output.read_text())
    ledger=data.pop('fixtures')
    data['fixture_ledger_sha256']=hashlib.sha256(json.dumps(ledger,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    data['fixture_ledger_reference']='EQUALITY_RESULTS.json deterministic construction'
    data['local_cycle_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data['counts'],indent=2))
