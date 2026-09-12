#!/usr/bin/env python3
"""Separate whole-count formulation of the N34 exceptional graph image.

All variables count objects, rather than fractions. No original model import.
"""
from itertools import product
from collections import defaultdict


def build():
    source_sizes={1:10,2:8};label_sizes={1:2,2:13}
    sources=[];labels=[];arcs=[];incidences=[];scales={}
    for r in source_sizes:
        for q,p,H in product(range(16),range(18),range(16)):
            if q+r>15 or q+p>17 or p>r+2:continue
            if H>q or q-H>2 or H>13:continue
            if r==1 and H:continue
            name=('source',r,q,p,H);sources.append(name);scales[name]=source_sizes[r]
    for s in label_sizes:
        for R,x in product(range(19),range(19)):
            if R+s>13 or x<s or R+x>18:continue
            if x>sum(n for r,n in source_sizes.items() if r>=s):continue
            name=('label',s,R,x);labels.append(name);scales[name]=label_sizes[s]
    qsets={r:sorted({n[2] for n in sources if n[1]==r}) for r in source_sizes}
    for r,r2 in product(source_sizes,repeat=2):
        for q,q2 in product(qsets[r],qsets[r2]):
            if not q or r2+q2<q-1:continue
            name=('arc',r,r2,q,q2);arcs.append(name)
            scales[name]=source_sizes[r]*(source_sizes[r2]-(r==r2))
    for w,l in product(sources,labels):
        _,r,q,p,H=w;_,s,R,x=l
        if not q or s>r or R+s>r+q-1 or R+x<q+p:continue
        if (s==2 and not H) or (s==1 and q==H):continue
        name=('incidence',r,s,q,p,H,R,x);incidences.append(name)
        scales[name]=source_sizes[r]*label_sizes[s]
    rows={'eq':[],'ub':[]}
    def add(kind,name,co,rhs=0):
        rows[kind].append(dict(name=name,coefficients={k:v for k,v in co.items() if v},rhs=rhs))
    for r,n in source_sizes.items():
        add('eq',('source_count',r),{w:1 for w in sources if w[1]==r},n)
    for s,n in label_sizes.items():
        add('eq',('label_count',s),{l:1 for l in labels if l[1]==s},n)
    add('eq',('residual_count',),{l:l[2] for l in labels},26)
    for r,qs in qsets.items():
        for q in qs:
            if q:
                co={p:1 for p in arcs if p[1]==r and p[3]==q}
                co.update({w:-q for w in sources if w[1]==r and w[2]==q})
                add('eq',('arc_out',r,q),co)
            co={p:1 for p in arcs if p[2]==r and p[4]==q}
            co.update({w:-w[3] for w in sources if w[1]==r and w[2]==q})
            add('eq',('arc_in',r,q),co)
    incident_source=defaultdict(list);incident_label=defaultdict(list)
    for z in incidences:
        _,r,s,q,p,H,R,x=z
        incident_source['source',r,q,p,H].append(z)
        incident_label['label',s,R,x].append(z)
    for w in sources:
        _,r,q,p,H=w
        for s,ng in label_sizes.items():
            co={z:1 for z in incident_source[w] if z[2]==s};co[w]=-ng
            add('ub',('source_label_cap',r,q,p,H,s),co)
        co={z:1 for z in incident_source[w]};co[w]=-q
        add('eq',('selected_out',r,q,p,H),co)
        co={z:1 for z in incident_source[w] if z[2]==2};co[w]=-H
        add('eq',('heavy_out',r,q,p,H),co)
    for l in labels:
        co={z:1 for z in incident_label[l]};co[l]=-l[3]
        add('eq',('selected_in',)+l[1:],co)
    add('ub',('heavy_routing',),{w:(w[4] if w[4]>2 else 0)-(w[3] if w[1]>=2 else 0) for w in sources})
    for name,scale in sorted(scales.items()):
        add('ub',('count_cap',)+name,{name:1},scale)
    return dict(scales=scales,rows=rows)


def verify(model,cert):
    totals=dict.fromkeys(model['scales'],0);rhs=0
    for kind in ('eq','ub'):
        seen=set()
        for i,w in cert[kind]:
            assert type(i) is int and 0<=i<len(model['rows'][kind]) and i not in seen
            assert type(w) is int and (kind=='eq' or w>=0)
            seen.add(i);row=model['rows'][kind][i];rhs+=w*row['rhs']
            for name,c in row['coefficients'].items():totals[name]+=w*c
    assert min(totals.values())>=0 and rhs==cert['rhs'] and rhs<0
    return dict(columns=len(totals),integer_rhs=rhs)
