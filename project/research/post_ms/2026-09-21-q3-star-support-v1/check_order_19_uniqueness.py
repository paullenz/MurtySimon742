import sys,itertools,collections
sys.path.insert(0,'project/research/post_ms/2026-09-21-q3-star-support-v1')
from check_star_support import graph,d2c,relation
allcoords=['C00','C01','C10','C11','C20','C21'];stars=['S0','S3','S5','S6']
r=relation((0,3,5,6));R=set(r['allowed_pairs']);R|={(b,a) for a,b in R}
rows=[]
for miss in allcoords:
 codes=[x for x in allcoords if x!=miss]+['P0']+stars
 poss=[(i,j) for i in range(10) for j in range(i+1,10) if (codes[i],codes[j]) in R]
 found=[]
 for mask in range(1<<len(poss)):
  ae=[e for k,e in enumerate(poss) if mask>>k&1]
  if d2c(graph(codes,ae)):found.append(ae)
 print(miss,'possible',len(poss),'found',len(found),'edgecounts',collections.Counter(map(len,found)))
 rows.append({'missing':miss,'possible_A_edges':len(poss),'D2C_models':len(found),'edge_counts':dict(collections.Counter(map(len,found))),'unique_A_edges':[[codes[i],codes[j]] for i,j in found[0]]})
from pathlib import Path
import json
Path(__file__).with_name('ORDER_19_UNIQUENESS_RESULTS.json').write_text(json.dumps({'rows':rows},indent=2)+'\n')
assert all(r['D2C_models']==1 and r['edge_counts']=={6:1} for r in rows)
print('PASS: one D2C A-edge set for each of six missing-coordinate orientations')
