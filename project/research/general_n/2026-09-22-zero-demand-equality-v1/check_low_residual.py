#!/usr/bin/env python3
"""Hostile actual-graph regression of the residual support theorems."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import check_equality_boundary as E

base_check=E.check
witnesses={}


def checked(rows,v,selection,counts):
    p=base_check(rows,v,selection,counts)
    A=[i for i in range(len(rows)) if i!=v and not(rows[v]>>i&1)]
    B=[u for u in range(len(rows)) if rows[v]>>u&1]
    selected={(u,i):w for u,i,w in selection}
    X={i:{u for u in B if (u,i) in selected} for i in A}
    Z={i:{u for u in B if not(rows[u]>>i&1) and (u,i) not in selected} for i in A}
    R={i:len(Z[i]) for i in A}
    support=[i for i in A if R[i]]
    fedges=[(i,j) for i,j in E.C.combinations(A,2) if rows[i]>>j&1]
    for i,j in fedges:
        assert R[i]+R[j]>=2, ('residual edge charge',v,i,j,R,selection)
        counts['residual_edge_charge_checks']+=1
        for x,y in ((i,j),(j,i)):
            if R[x]==0:
                assert X[x]<=Z[y] and len(X[x])>=sum(bool(rows[x]>>z&1) for z in A)
                assert R[y]>=2
                counts['zero_residual_endpoint_checks']+=1
                witnesses.setdefault('zero_residual_endpoint',{'root':v,'edge':[x,y],'R':R,'selection':selection,'graph_edges':E.C.edges(rows),'n':len(rows)})
    if len(support)==1:
        assert p['f']<=p['r']-1
        counts['single_residual_label_checks']+=1
        if p['f']:
            counts['nonempty_single_residual_label_checks']+=1
            witnesses.setdefault('nonempty_single_residual_label',{'root':v,'R':R,'profile':p,'selection':selection,'graph_edges':E.C.edges(rows),'n':len(rows)})
    if 1<=p['r']<=2:
        assert p['f']<=p['r']-1
        counts['low_residual_checks']+=1
    if p['r']==2 and p['f']==1:
        witnesses.setdefault('sharp_r2_f1',{'root':v,'R':R,'profile':p,'selection':selection,'graph_edges':E.C.edges(rows),'n':len(rows)})
    n=len(rows); m=len(E.C.edges(rows)); b=len(B)
    if p['S']<=2:
        assert m<=n*n//4
        counts['S_at_most_2_bound_checks']+=1
        if m==n*n//4:
            assert not selection and not fedges and p['r']==0
            assert all(rows[i]>>u&1 for i in A+[v] for u in B)
            counts['S_at_most_2_equality_checks']+=1
    if m>=n*n//4 and (selection or fedges):
        D=n*n//4-b*(n-b); epsilon=m-n*n//4
        assert p['r']>=3 and p['S']>=3+2*D+2*epsilon
        counts['nonbipartite_target_density_checks']+=1
    return p


if __name__=='__main__':
    E.check=checked
    if '--output' not in sys.argv:sys.argv+=['--output','LOW_RESIDUAL_RESULTS.json']
    E.main()
    output=Path(sys.argv[sys.argv.index('--output')+1])
    result=json.loads(output.read_text())
    result['low_residual_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['low_residual_witnesses']=witnesses
    result['nonvacuity_warning']='No nonbipartite target-density fixture is asserted; tested branch counts are explicit.'
    output.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps({'witness_kinds':list(witnesses),'new_source_sha256':result['low_residual_source_sha256']},indent=2))
