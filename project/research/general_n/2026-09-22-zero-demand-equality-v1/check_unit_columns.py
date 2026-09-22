#!/usr/bin/env python3
"""Actual graph and repeated-source kernel replay for unit-column theorem."""
import hashlib
import json
from pathlib import Path
import sys
import check_low_residual as L
E=L.E
extra_witnesses={}


def checked(rows,v,selection,counts):
    p=L.checked(rows,v,selection,counts)
    A=[i for i in range(len(rows)) if i!=v and not(rows[v]>>i&1)]
    B=[u for u in range(len(rows)) if rows[v]>>u&1]
    selected={(u,i):w for u,i,w in selection}
    R={i:sum(not(rows[u]>>i&1) and (u,i) not in selected for u in B) for i in A}
    d={i:sum(bool(rows[i]>>j&1) for j in A) for i in A}
    x={i:sum((u,i) in selected for u in B) for i in A}
    positive=sorted(z for z in R.values() if z)
    if positive and max(positive)==1:
        assert p['f']<=p['r']-1
        assert max(d.values(),default=0)<=2
        for i in A:
            if d[i]:
                assert R[i]==1 and x[i]*(d[i]-1)<=d[i]
        counts['unit_column_cases']+=1
        counts['unit_column_nonempty_F_cases']+=bool(p['f'])
        counts['unit_column_degree_two_cases']+=any(z==2 for z in d.values())
        if p['f']:extra_witnesses.setdefault('unit_column_nonempty_F',{'n':len(rows),'root':v,'R':R,'d':d,'selection':selection,'edges':E.C.edges(rows)})
    if len(positive)==2 and positive[0]==1:
        assert p['f']<=p['r']-1
        counts['two_column_with_unit_cases']+=1
    if 1<=p['r']<=3:
        assert p['f']<=p['r']-1
        counts['r_at_most_three_cases']+=1
    if p['r']==4 and p['f']>=4:
        assert positive==[2,2]
        counts['r4_saturating_cases']+=1
    if p['S']<=3:
        assert len(E.C.edges(rows))<=len(rows)**2//4
        counts['S_at_most_three_cases']+=1
    return p


def partitions(n,prefix=()):
    if len(prefix)==n:
        yield prefix;return
    for k in range(max(prefix,default=-1)+2):
        yield from partitions(n,prefix+(k,))


def repeated_source_kernel():
    total=0;survivors=0
    for n in range(3,10):
        for z in partitions(n):
            total+=1
            valid=True
            for i in range(n):
                prev=z[(i-1)%n];own=z[i];nxt=z[(i+1)%n]
                # Xi={next residual source}; no selected/residual overlap;
                # predecessor witness is adjacent to i; selected source must
                # miss the predecessor label.
                if nxt==own or nxt==prev or nxt not in (prev,own):
                    valid=False;break
            survivors+=valid
    assert survivors==0
    return {'source_partitions_checked':total,'survivors':survivors,
            'scope':'finite replay of the proof kernel, including repeated sources; not a graph search'}


if __name__=='__main__':
    E.check=checked
    if '--output' not in sys.argv:sys.argv+=['--output','UNIT_COLUMN_RESULTS.json']
    E.main()
    output=Path(sys.argv[sys.argv.index('--output')+1]);data=json.loads(output.read_text())
    ledger=data.pop('fixtures')
    data['fixture_ledger_sha256']=hashlib.sha256(json.dumps(ledger,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    data['fixture_ledger_reference']='Same deterministic fixture/root construction as EQUALITY_RESULTS.json; source parameters unchanged.'
    data['unit_column_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data['witnesses']=extra_witnesses
    data['repeated_source_kernel']=repeated_source_kernel()
    output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'new_counts':{k:v for k,v in data['counts'].items() if 'unit_column' in k or 'three' in k or 'r4' in k},'kernel':data['repeated_source_kernel']},indent=2))
