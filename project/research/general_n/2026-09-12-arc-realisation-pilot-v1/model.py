#!/usr/bin/env python3
"""Necessary binary routing models; every saved row has integer coefficients."""
from collections import defaultdict

def build(rec,mode):
    assert mode in ('degree_routing','label_compatible')
    a,b,s,rho=rec['a'],rec['b'],rec['s'],rec['rho']
    assert len(s)==a and len(rho)==b and min(s)>=0 and min(rho)>=0
    names=[];upper=[];index={};rows=[]
    def var(name,cap=1):
        key=tuple(name);index[key]=len(names);names.append(list(name));upper.append(cap)
        return index[key]
    x={(u,i):var(('x',u,i),int(s[i]<=rho[u])) for u in range(b) for i in range(a)}
    r={(u,i):var(('r',u,i)) for u in range(b) for i in range(a)}
    z={(u,i,v):var(('z',u,i,v)) for u in range(b) for i in range(a) if s[i]<=rho[u] for v in range(b) if v!=u}
    y={(u,v):var(('y',u,v)) for u in range(b) for v in range(b) if v!=u}
    q={u:var(('q',u),a) for u in range(b)};p={u:var(('p',u),b-1) for u in range(b)}
    thresholds=range(1,max(s,default=0)+1)
    e={(u,h):var(('e',u,h)) for u in range(b) for h in thresholds}
    def row(name,terms,lo=None,hi=None):
        d=defaultdict(int)
        for col,c in terms:d[col]+=c
        rows.append(dict(name=list(name),terms=[[col,c] for col,c in sorted(d.items()) if c],lower=lo,upper=hi))
    for u in range(b):
        row(('rho',u),[(r[u,i],1) for i in range(a)],rho[u],rho[u])
        row(('q',u),[(q[u],1)]+[(x[u,i],-1) for i in range(a)],0,0)
        row(('p',u),[(p[u],1)]+[(y[v,u],-1) for v in range(b) if v!=u],0,0)
        row(('source_capacity',u),[(q[u],1)],hi=a-rho[u])
        row(('receiving_capacity',u),[(p[u],1)],hi=rho[u]+b-a-1)
        for i in range(a):
            row(('disjoint',u,i),[(x[u,i],1),(r[u,i],1)],hi=1)
            row(('label_arc',u,i),[(x[u,i],1)]+[(z[u,i,v],-1) for v in range(b) if (u,i,v) in z],0,0)
            # If selected, label B-degree is at least the missing degree q+p.
            row(('endpoint_load',u,i),[(q[u],1),(p[u],1),(x[u,i],b-1)]+
                [(x[v,i],-1) for v in range(b)]+[(r[v,i],-1) for v in range(b)],hi=b-1)
        for h in thresholds:
            heavy=[(x[u,i],1) for i in range(a) if s[i]>=h]
            row(('high_upper',u,h),heavy+[(e[u,h],-a)],hi=h)
            row(('high_lower',u,h),heavy+[(e[u,h],-h-1)],lo=0)
    for i in range(a):row(('demand',i),[(x[u,i],1) for u in range(b)],lo=s[i])
    for u in range(b):
        for v in range(b):
            if u==v:continue
            row(('arc_label',u,v),[(y[u,v],1)]+[(z[u,i,v],-1) for i in range(a) if (u,i,v) in z],0,0)
            row(('destination_eligibility',u,v),[(q[u],1),(q[v],-1),(y[u,v],a)],hi=a+rho[v]+1)
            if u<v:row(('orientation',u,v),[(y[u,v],1),(y[v,u],1)],hi=1)
            for h in thresholds:
                if rho[v]<h:
                    for i in range(a):
                        if s[i]>=h and (u,i,v) in z:
                            row(('heavy_destination',u,v,h,i),[(z[u,i,v],1),(e[u,h],1)],hi=1)
            if mode=='label_compatible':
                for i in range(a):
                    if (u,i,v) in z:
                        row(('exception_absent',u,i,v),[(z[u,i,v],1),(x[v,i],1),(r[v,i],1)],hi=1)
                    terms=[(x[v,i],1),(r[v,i],1),(x[u,i],-1),(y[u,v],-1),(y[v,u],-1)]
                    if (u,i,v) in z:terms.append((z[u,i,v],1))
                    row(('other_missing_neighbour',u,i,v),terms,lo=-1)
    return dict(schema='arc-realisation-integer-model-v1',mode=mode,record=rec,variables=names,
                lower_bounds=[0]*len(names),upper_bounds=upper,integrality='all_integer',objective='zero',rows=rows)
