"""Corrected v2 cumulative-threshold model for the n=29 Delta=16 red team.

This file exists because the v1 builder double-counted the label-group multiplicity
in the label-side Z/T equations.  It reuses only the generic Model/certificate
machinery from v1; the graph-derived build() is reconstructed here.
"""
from collections import defaultdict
from independent_threshold_model import Model,add,groups,exact_certificate,verify_certificate

def build(s,rho,t):
    a=12;b=16;r=sum(rho);LG=groups(s);SG=groups(rho);m=Model()
    Y={};T={};label_opts=defaultdict(list)
    W={};source_types=defaultdict(list)

    # Y and T are fractions within one demand group g.  T_h is therefore
    # already a per-label-group fraction and must not be multiplied by n_g
    # again on the label side of the incidence equations.
    for g,(sg,ng) in enumerate(LG):
        norm={}
        for d in range(11):
            for R in range(17):
                if sg>0 and d-R!=sg: continue
                if sg==0 and d>R: continue
                U=16-R
                if U<sg or d>R+U: continue
                y=m.var(('Y',g,d,R));Y[g,d,R]=y;label_opts[g].append((d,R,y,U));norm[y]=1
                prev=y
                for h in range(1,U+1):
                    th=m.var(('T',g,d,R,h));T[g,d,R,h]=th
                    m.le({th:1,prev:-1},0)
                    if h<=sg:m.equal({th:1,y:-1},0)
                    prev=th
        m.equal(norm,1)

    ed={};er={}
    for (g,d,R),y in Y.items():
        ng=LG[g][1];add(ed,y,ng*d);add(er,y,ng*R)
    m.equal(ed,2*(r+t));m.equal(er,r)

    # Source type fractions (q,p) within each residual-degree group.
    for k,(rh,nk) in enumerate(SG):
        norm={}
        for q in range(13-rh):
            for p in range(min(rh+3,15-q)+1):
                w=m.var(('W',k,q,p));W[k,q,p]=w;source_types[k].append((q,p,w));norm[w]=1
        m.equal(norm,1)

    # Oriented missing-B-pair flow.  P is density among ordered source/target
    # vertex pairs.  Every actual graph maps to these equations by averaging.
    P_out=defaultdict(list);P_in=defaultdict(list);P_pair=defaultdict(list)
    for k,(rhk,nk) in enumerate(SG):
        qks=sorted({q for q,p,w in source_types[k] if q>0})
        for l,(rhl,nl) in enumerate(SG):
            if k==l and nk<2: continue
            qls=sorted({q for q,p,w in source_types[l]})
            for q in qks:
                for q2 in qls:
                    if rhl+q2<q-1: continue
                    z=m.var(('P',k,l,q,q2))
                    P_out[k,q].append((l,z));P_in[l,q2].append((k,z));P_pair[min(k,l),max(k,l)].append((k,l,z))
    for k,(rh,nk) in enumerate(SG):
        for q in sorted({qq for qq,p,w in source_types[k] if qq>0}):
            e={}
            for qq,p,w in source_types[k]:
                if qq==q:add(e,w,-q)
            for l,z in P_out[k,q]:add(e,z,SG[l][1]-(k==l))
            m.equal(e,0)
    for l,(rh,nl) in enumerate(SG):
        for q2 in sorted({qq for qq,p,w in source_types[l]}):
            e={}
            for qq,p,w in source_types[l]:
                if qq==q2:add(e,w,-p)
            for k,z in P_in[l,q2]:add(e,z,SG[k][1]-(k==l))
            m.equal(e,0)
    for (k,l),items in P_pair.items():
        e={}
        for kk,ll,z in items:add(e,z,1)
        # For k=l, <=1 is weaker than the exact <=1/2 and is therefore safe.
        m.le(e,1)

    # Selected source-label incidence density Z.  If z is the density among
    # source vertices in group k and labels in group g, then z*n_g is selected
    # incidence count per source, while z*n_k is selected incidence count per
    # label.  This dimensional identity is the normalization checkpoint that
    # v1 violated.
    by_source=defaultdict(list);by_label=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        for g,(sg,ng) in enumerate(LG):
            for q,p,w in source_types[k]:
                if q==0: continue
                for d,R,y,U in label_opts[g]:
                    req=max(1,q+p-R)
                    if sg>rh or d>rh+R or d>rh+q-1 or req>U: continue
                    z=m.var(('Z',k,g,q,p,d,R))
                    by_source[k,q,p,g].append((d,R,z));by_label[g,d,R].append((k,q,p,z))

    for k,(rh,nk) in enumerate(SG):
        for q,p,w in source_types[k]:
            e={w:-q}
            for g,(sg,ng) in enumerate(LG):
                cap={w:-1}
                for d,R,z in by_source[k,q,p,g]:
                    add(cap,z,1);add(e,z,ng)
                m.le(cap,0)
            m.equal(e,0)

    for g,(sg,ng) in enumerate(LG):
        for d,R,y,U in label_opts[g]:
            items=by_label[g,d,R]
            total={}
            for k,q,p,z in items:add(total,z,SG[k][1])
            e=dict(total)
            # Correct per-label selected-degree identity:
            #   sum_k n_k Z = E[x] = sum_h T_h.
            for h in range(1,U+1):add(e,T[g,d,R,h],-1)
            m.equal(e,0)

            # Correct per-label nested Hall capacity:
            # E[x 1{x>=h}] = (h-1)T_h + sum_{j=h}^U T_j.
            for h in range(1,U+1):
                e={}
                for k,q,p,z in items:
                    if max(1,q+p-R)>=h:add(e,z,SG[k][1])
                add(e,T[g,d,R,h],-(h-1))
                for hh in range(h,U+1):add(e,T[g,d,R,hh],-1)
                m.le(e,0)

    m.bound_start=len(m.ub)
    for j in range(len(m.names)):m.le({j:1},1)
    return m
