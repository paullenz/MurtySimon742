#!/usr/bin/env python3
"""Extract complete physical graph witnesses for the delicate supplement step."""
from itertools import product
from pathlib import Path
import json
import check_raw_profile as C


def graph_from_fixture(f):
    name=f['name']
    if name.startswith('greedy_'):
        parts=name.split('_')
        n=int(parts[1][1:]); seed=int(parts[2][4:])
        return C.greedy_critical(n,20260922+1000*n+seed)
    if name.startswith('exhaustive_'):
        parts=name.split('_'); n=int(parts[1][1:]); mask=int(parts[2][4:])
        return C.from_edges(n,[e for k,e in enumerate(C.combinations(range(n),2)) if mask>>k&1])
    if name.startswith('X_'): return C.cube_face(int(name[2:]))
    if name.startswith('star_'):
        n=int(name.split('n')[-1]); return C.from_edges(n,[(0,i) for i in range(1,n)])
    parts=name.split('_'); a=int(parts[-2]); b=int(parts[-1])
    return C.from_edges(a+b,[(i,j) for i in range(a) for j in range(a,a+b)])


def cases(rows,v):
    A,B,H,pairs,options=C.legal_choices(rows,v)
    for selection in product(*options):
        sel={(u,i):w for u,i,w in selection}
        Rset={(u,i) for u in B for i in A if H[u]>>i&1 and (u,i) not in sel}
        rho={u:sum((u,i) in Rset for i in A) for u in B}
        R={i:sum((u,i) in Rset for u in B) for i in A}
        d={i:sum(rows[i]>>j&1 for j in A) for i in A}
        s={i:max(0,d[i]-R[i]) for i in A}
        for h in range(1,max(s.values(),default=0)+1):
            I=[i for i in A if s[i]>=h]
            for u in B:
                load=[i for i in I if (u,i) in sel]
                if len(load)<=h: continue
                for i in load:
                    w=sel[u,i]
                    selected_others=[j for j in load if j!=i and (w,j) in sel]
                    yield {'root':v,'A':A,'B':B,'h':h,'source':u,'label':i,'supplement':w,'heavy_labels':I,'source_heavy_labels':load,'selected_other_labels':selected_others,'supplement_branch':'SELECTED' if selected_others else 'RESIDUAL','rho':rho,'R':R,'d':d,'s':s,'selected_triples':selection,'residual_cross_edges':sorted(Rset),'n':len(rows),'m':len(C.edges(rows)),'graph_edges':C.edges(rows),'W_h':sum(s[i] for i in I),'Z_h':[u for u in B if rho[u]>=h]}


def main():
    results=json.loads(Path('RESULTS.json').read_text())
    out=[]
    for f in results['fixtures']:
        relevant=[r for r in f['roots'] if r['positive_demand_assignments']]
        if not relevant: continue
        rows=graph_from_fixture(f)
        for r in relevant:
            for record in cases(rows,r['root']):
                record['fixture']=f['name']
                C.certify_d2c_bfs(rows)
                assert record['supplement'] in record['Z_h']
                out.append(record)
    Path('SUPPLEMENT_WITNESSES.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{'fixture':x['fixture'],'n':x['n'],'m':x['m'],'root':x['root'],'h':x['h'],'source':x['source'],'label':x['label'],'supplement':x['supplement'],'selected_other_labels':x['selected_other_labels'],'branch':x['supplement_branch']} for x in out],indent=2))


if __name__=='__main__': main()
