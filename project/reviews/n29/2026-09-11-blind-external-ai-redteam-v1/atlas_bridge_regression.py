#!/usr/bin/env python3
"""Independent small-graph regression of the n=29 base bridge semantics.

Requires NetworkX. Uses graph_atlas_g(), exhaustively finds all unlabeled
simple diameter-two-edge-critical graphs through order 7, roots each at every
maximum-degree vertex, enumerates every admissible choice of one selected
quasi-edge per missing unordered B-pair, and checks the base bridge identities
and selected-edge inequalities.

This intentionally does NOT test the positive-surplus lemmas: all atlas cases
found here have t<=0.

Expected summary:
    critical_types = 21
    rooted_cases = 50
    selection_configurations = 58
    failures = 0
"""
import itertools
import networkx as nx


def is_diameter_two_critical(G):
    if len(G)<2 or not nx.is_connected(G):
        return False
    if nx.diameter(G)!=2:
        return False
    for x,y in list(G.edges()):
        J=G.copy()
        J.remove_edge(x,y)
        if nx.is_connected(J) and nx.diameter(J)<=2:
            return False
    return True


def admissible_choices(H,A,B,u,w):
    out=[]
    V=set(H.nodes())
    for source,exception in ((u,w),(w,u)):
        for label in A:
            if not H.has_edge(source,label):
                continue
            if set(H.neighbors(source))|set(H.neighbors(label))==V-{exception}:
                out.append((source,label,exception))
    return out


def check_configuration(G,v,selection):
    H=nx.complement(G)
    n=len(G)
    Delta=G.degree(v)
    A=set(H.neighbors(v))
    B=set(H.nodes())-{v}-A
    a=len(A)
    b=len(B)
    assert a==n-1-Delta and b==Delta

    F=nx.Graph()
    F.add_nodes_from(A)
    for i,j in itertools.combinations(A,2):
        if not H.has_edge(i,j):
            F.add_edge(i,j)
    d={i:F.degree(i) for i in A}

    selected={(u,i) for u,i,w in selection}
    assert len(selected)==len(selection)
    cross={(u,i) for u in B for i in A if H.has_edge(u,i)}
    residual=cross-selected

    rho={u:sum((u,i) in residual for i in A) for u in B}
    R={i:sum((u,i) in residual for u in B) for i in A}
    q={u:0 for u in B}
    p={u:0 for u in B}
    x={i:0 for i in A}
    for u,i,w in selection:
        q[u]+=1
        p[w]+=1
        x[i]+=1

    r=sum(rho.values())
    t=G.number_of_edges()-b*(n-b)
    assert F.number_of_edges()==r+t
    assert sum(d.values())==2*(r+t)

    s={i:max(0,d[i]-R[i]) for i in A}
    S=sum(s.values())
    assert all(x[i]>=s[i] for i in A)
    assert S>=r+2*t

    for u,i,w in selection:
        assert d[i]<=rho[u]+R[i]
        assert d[i]<=rho[u]+rho[w]
        assert d[i]<=rho[u]+q[u]-1
        assert rho[w]+q[w]>=q[u]-1
        assert R[i]+x[i]>=q[u]+p[u]
        assert s[i]<=rho[u]

    for u in B:
        assert q[u]+rho[u]<=a
        assert p[u]<=rho[u]+(b-a-1)
        assert q[u]+p[u]<=b-1

    return t


def main():
    critical=[G.copy() for G in nx.graph_atlas_g()
              if len(G)<=7 and is_diameter_two_critical(G)]
    rooted=0
    configs=0
    t_values=[]

    for G in critical:
        Delta=max(dict(G.degree()).values())
        for v,dv in G.degree():
            if dv!=Delta:
                continue
            rooted+=1
            H=nx.complement(G)
            A=set(H.neighbors(v))
            B=set(H.nodes())-{v}-A
            missing=[(u,w) for u,w in itertools.combinations(sorted(B),2)
                     if not H.has_edge(u,w)]
            option_lists=[]
            for u,w in missing:
                choices=admissible_choices(H,A,B,u,w)
                assert choices,(len(G),v,u,w)
                option_lists.append(choices)
            products=itertools.product(*option_lists) if option_lists else [()]
            for selection in products:
                configs+=1
                t_values.append(check_configuration(G,v,selection))

    print({
        'critical_types':len(critical),
        'rooted_cases':rooted,
        'selection_configurations':configs,
        't_values':sorted(set(t_values)),
        'failures':0,
    })
    assert len(critical)==21
    assert rooted==50
    assert configs==58
    assert sorted(set(t_values))==[-3,-2,-1,0]
    print('PASS')


if __name__=='__main__':
    main()
