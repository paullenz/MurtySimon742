#!/usr/bin/env python3
"""Actual new star fixtures passed through the prior independent Hall checker."""
import sys,json
from pathlib import Path
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'2026-09-19-rigid-graph-regression-v1'))
import networkx as nx
import check_rigid_graph_level as hall
from check_five_coordinate_family import build as five
from check_star_forest_family import build as six

def main():
    totals=Counter(); rows=[]
    fixtures=[('X3',hall.cube_face_graph(3))]
    for name,build in [('five',five),('six',six)]:
        for r,q in [(1,0),(1,1),(2,2),(4,4),(8,8)]:
            adj,_,_=build(r,q)
            G=nx.Graph();G.add_nodes_from(range(len(adj)))
            G.add_edges_from((x,y) for x,ns in enumerate(adj) for y in ns if x<y)
            fixtures.append((f'{name}_{r}_{q}',G))
    for name,G in fixtures:
        assert hall.is_d2c(G)
        degree=max(dict(G.degree()).values()); roots=[v for v in G if G.degree(v)==degree]
        root_rows=[]
        for v in roots:
            D=hall.root_data(G,v)
            stats=Counter()
            for policy in ('lex','matched_first','au_first'):
                stats.update(hall.verify_root(G,v,policy,True))
            totals.update(stats)
            root_rows.append({'root':v,'a':D['a'],'b':D['b'],'p':D['p'],'u':D['u'],'lambda':D['lambda'],'Q':G.subgraph(D['B']).number_of_edges(),'stats':dict(stats)})
        row={'fixture':name,'n':len(G),'m':G.number_of_edges(),'M':hall.M(len(G)),'maximum_degree':degree,'roots':root_rows}
        rows.append(row)
        print(name,len(G),G.number_of_edges(),'roots',len(roots),'parameters',[(x['p'],x['u'],x['lambda']) for x in root_rows],flush=True)
    assert rows[0]['n']==12 and rows[0]['m']==32 and rows[0]['M']==31
    result={'fixtures':rows,'totals':dict(totals),'scope':'Maximum-degree roots only; three certificate policies; all Hall cuts where <=12 active code-pairs. Zero rigid cuts is absence of coverage, not verification of the rigid branch.'}
    Path(__file__).with_name('NEW_FAMILIES_HALL_INTERFACE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(dict(totals))
if __name__=='__main__':main()
