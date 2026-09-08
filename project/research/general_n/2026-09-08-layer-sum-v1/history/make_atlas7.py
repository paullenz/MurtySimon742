# Regenerate the ten saved atlas inputs. Not needed for the standard-library replay.
import sys
from pathlib import Path
import networkx as nx
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import check_layers as m
out=[]
for atlas_id,g in enumerate(nx.graph_atlas_g()):
    if len(g)!=7:
        continue
    adj=[sum(1<<v for v in g.neighbors(u)) for u in g]
    x=m.witness_critical(adj)
    y=m.deletion_critical(adj)
    if x!=y:
        raise AssertionError('atlas disagreement')
    if x:
        out.append({'atlas_id':atlas_id,'n':7,'adjacency_bitmasks':adj})
assert out == m.ATLAS7
print(nx.__version__, len(out))
