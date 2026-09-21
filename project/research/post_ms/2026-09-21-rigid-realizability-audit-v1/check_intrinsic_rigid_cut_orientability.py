#!/usr/bin/env python3
"""Independent actual-D2C scan for intrinsically orientable rigid complete A-cuts.

Unlike the earlier regression this does not fix an A-edge certificate policy first.
For each oriented rooted code-pair cut X|Y it asks the graph-intrinsic existence
question: are all X-Y edges present, and does every crossing edge admit at
least one raw criticality certificate oriented from Y to X with witness in
B=N(v)?  Both orientations of every unordered partition are tested because
Y->X orientability is not symmetric.

A positive hit is therefore a candidate realizability witness for the rigid
Hall branch before any arbitrary certificate-policy choice.  A negative bounded
scan is only diagnostic, never a proof of non-realizability.
"""
import itertools, random, json
from collections import Counter, defaultdict
import networkx as nx


def is_d2c(G):
    if len(G)<3 or not nx.is_connected(G) or nx.diameter(G)!=2: return False
    for e in list(G.edges()):
        H=G.copy(); H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H)<=2: return False
    return True

def tight_pair(G,v,u,w):
    if not G.has_edge(v,u) or not G.has_edge(v,w) or G.has_edge(u,w): return False
    if set(nx.common_neighbors(G,u,w))!={v}: return False
    for z in G:
        if z in (v,u,w): continue
        if int(G.has_edge(z,u))+int(G.has_edge(z,w))!=1: return False
    return True

def rooted_partition(G,v):
    B=set(G.neighbors(v)); A=set(G)-B-{v}
    pairs=[]
    for u,w in itertools.combinations(sorted(B),2):
        if tight_pair(G,v,u,w): pairs.append((u,w))
    flat=[z for P in pairs for z in P]
    if len(flat)!=len(set(flat)): return None
    U=B-set(flat)
    return A,B,U,pairs

def complement(c): return tuple(1-b for b in c)
def pair_key(c): return min(tuple(c),complement(c))
def codes_for(G,v,A,U,pairs):
    codes={}
    for z in A|U:
        bits=[]
        for q0,q1 in pairs:
            b0=G.has_edge(z,q0); b1=G.has_edge(z,q1)
            if b0==b1: return None
            bits.append(0 if b0 else 1)
        codes[z]=tuple(bits)
    return codes

def y_to_x_witnesses(G,y,x,B):
    out=[]
    for w in B:
        if G.has_edge(y,w) or not G.has_edge(w,x): continue
        if set(nx.common_neighbors(G,y,w))=={x}: out.append(w)
    return out

def intrinsic_cuts(G,v,max_active=14):
    rp=rooted_partition(G,v)
    if rp is None: return []
    A,B,U,pairs=rp
    if not pairs: return []
    codes=codes_for(G,v,A,U,pairs)
    if codes is None: return []
    classes=defaultdict(set)
    for z in A: classes[pair_key(codes[z])].add(z)
    active=list(classes)
    if len(active)<2 or len(active)>max_active: return []
    out=[]
    # Do NOT quotient by set-complement: X|Y and Y|X have different required
    # certificate orientations, so both masks must be tested.
    for mask in range(1,(1<<len(active))-1):
        X=set().union(*(classes[active[i]] for i in range(len(active)) if mask>>i&1))
        Y=A-X
        if len(X)<3 or not Y: continue
        if any(not G.has_edge(x,y) for x in X for y in Y): continue
        witnesses={}; ok=True
        for y in Y:
            for x in X:
                ws=y_to_x_witnesses(G,y,x,B)
                if not ws:
                    ok=False; break
                witnesses[(y,x)]=ws
            if not ok: break
        if not ok: continue
        singleton_traffic=Counter(w for ws in witnesses.values() for w in ws if len(ws)==1)
        out.append({
            'x':len(X),'y':len(Y),'p':len(pairs),'u':len(U),
            'min_candidates':min(len(ws) for ws in witnesses.values()),
            'max_forced_singleton_reuse':max(singleton_traffic.values(),default=0),
            'forced_singleton_reuse_hist':dict(Counter(singleton_traffic.values())),
        })
    return out

def greedy_d2c(n,seed):
    rng=random.Random(seed); G=nx.complete_graph(n); es=list(G.edges()); rng.shuffle(es)
    for e in es:
        H=G.copy(); H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H)<=2: G=H
    assert is_d2c(G)
    return G

def cube_face(k):
    G=nx.Graph(); cube=[format(i,f'0{k}b') for i in range(2**k)]; faces=[f'a{j}' for j in range(k)]
    G.add_nodes_from(['r']+faces+cube)
    for s in cube:
        for j in range(k):
            t=s[:j]+('1' if s[j]=='0' else '0')+s[j+1:]
            G.add_edge(s,t)
    for s in cube: G.add_edge('r',s)
    for j,a in enumerate(faces):
        for s in cube:
            if s[j]=='0': G.add_edge(a,s)
    return G

def scan():
    stats=Counter(); hits=[]
    # Mandatory X3 negative control, all roots.
    G=cube_face(3)
    for v in G:
        stats['roots']+=1
        cs=intrinsic_cuts(G,v)
        if cs: hits.append(('X3',v,cs))
    # Entire unlabeled atlas through order 7, all maximum-degree roots.
    for G0 in nx.graph_atlas_g():
        if len(G0)<3: continue
        G=nx.convert_node_labels_to_integers(G0)
        if not is_d2c(G): continue
        stats['atlas_graphs']+=1
        md=max(dict(G.degree()).values())
        for v in G:
            if G.degree(v)!=md: continue
            stats['roots']+=1
            cs=intrinsic_cuts(G,v)
            if cs: hits.append((f'atlas_n{len(G)}',v,cs))
    # Deterministic randomized actual-D2C corpus, n=8..18.
    for n in range(8,19):
        for s in range(120):
            G=greedy_d2c(n,n*100000+s)
            stats['generated_graphs']+=1
            md=max(dict(G.degree()).values())
            for v in G:
                if G.degree(v)!=md: continue
                stats['roots']+=1
                cs=intrinsic_cuts(G,v)
                if cs:
                    hits.append((f'gen_n{n}_s{s}',v,cs))
                    if len(hits)>=20: return stats,hits
    return stats,hits

if __name__=='__main__':
    stats,hits=scan()
    print(json.dumps({'stats':dict(stats),'hits':hits},default=list,indent=2))
