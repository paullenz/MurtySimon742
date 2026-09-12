#!/usr/bin/env python3
"""Pure-integer grouped RX/Hall model with an explicit heavy-outdegree split.

No numerical imports. The graph-to-model implication is in HEAVY_SPLIT.md.
Variable order is deterministic for exact certificate reconstruction.
"""
from collections import Counter,defaultdict


class Model:
    def __init__(self):
        self.names=[];self.eq=[];self.be=[];self.ub=[];self.bu=[]
    def var(self,name):
        self.names.append(name);return len(self.names)-1
    def equal(self,row,rhs=0):
        self.eq.append(row);self.be.append(rhs)
    def le(self,row,rhs):
        self.ub.append(row);self.bu.append(rhs)


def build(s,rho,h=2):
    a,b,dmax,t=15,18,13,1
    assert len(s)==a and len(rho)==b and min(s)>0
    assert sum(s)==sum(rho)+2*t
    LG=sorted(Counter(s).items());SG=sorted(Counter(rho).items())
    m=Model();source_types=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        norm={}
        light=sum(v<h and v<=rh for v in s)
        heavy=sum(h<=v<=rh for v in s)
        for q in range(min(a-rh,light+heavy)+1):
            for p in range(min(rh+b-a-1,b-1-q)+1):
                for H in range(max(0,q-light),min(q,heavy)+1):
                    w=m.var(('W',k,q,p,H))
                    source_types[k].append((q,p,H,w));norm[w]=1
        m.equal(norm,1)
    # Supplement transport, aggregated over p,H but retaining source q.
    Pout=defaultdict(list);Pin=defaultdict(list)
    for k,(rhk,nk) in enumerate(SG):
        for l,(rhl,nl) in enumerate(SG):
            if k==l and nk<2:continue
            for q in sorted({q for q,p,H,w in source_types[k] if q>0}):
                for q2 in sorted({q for q,p,H,w in source_types[l]}):
                    if rhl+q2<q-1:continue
                    z=m.var(('P',k,l,q,q2))
                    Pout[k,q].append((l,z));Pin[l,q2].append((k,z))
    for k,(rh,nk) in enumerate(SG):
        for q in sorted({q for q,p,H,w in source_types[k] if q>0}):
            row={w:-q for qq,p,H,w in source_types[k] if qq==q}
            for l,z in Pout[k,q]:row[z]=SG[l][1]-(k==l)
            m.equal(row)
    for l,(rh,nl) in enumerate(SG):
        for q2 in sorted({q for q,p,H,w in source_types[l]}):
            row={w:-p for q,p,H,w in source_types[l] if q==q2}
            for k,z in Pin[l,q2]:row[z]=SG[k][1]-(k==l)
            m.equal(row)
    label_types=defaultdict(list)
    for g,(sv,ng) in enumerate(LG):
        norm={}
        for R in range(dmax-sv+1):
            for x in range(sv,min(b-R,sum(rv>=sv for rv in rho))+1):
                z=m.var(('L',g,R,x));norm[z]=1
                label_types[g].append((R,x,z))
        m.equal(norm,1)
    m.equal({z:ng*R for g,(sv,ng) in enumerate(LG)
             for R,x,z in label_types[g]},sum(rho))
    by_source=defaultdict(list);by_label=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        for g,(sv,ng) in enumerate(LG):
            if sv>rh:continue
            for q,p,H,w in source_types[k]:
                if q==0 or (sv>=h and H==0) or (sv<h and H==q):continue
                for R,x,lvar in label_types[g]:
                    if R+sv>rh+q-1 or R+x<q+p:continue
                    z=m.var(('Z',k,g,q,p,H,R,x))
                    by_source[k,q,p,H,g].append(z)
                    by_label[g,R,x].append((k,z))
    for k,(rh,nk) in enumerate(SG):
        for q,p,H,w in source_types[k]:
            total={w:-q};heavy={w:-H}
            for g,(sv,ng) in enumerate(LG):
                cap={w:-1}
                for z in by_source[k,q,p,H,g]:
                    cap[z]=1;total[z]=ng
                    if sv>=h:heavy[z]=ng
                m.le(cap,0)
            m.equal(total);m.equal(heavy)
    for g,(sv,ng) in enumerate(LG):
        for R,x,lvar in label_types[g]:
            row={lvar:-x}
            for k,z in by_label[g,R,x]:row[z]=SG[k][1]
            m.equal(row)
    # Every heavy arc from a source with H>h ends in Z_h.
    transport={}
    for k,(rh,nk) in enumerate(SG):
        for q,p,H,w in source_types[k]:
            c=nk*((H if H>h else 0)-(p if rh>=h else 0))
            if c:transport[w]=c
    m.le(transport,0)
    m.bound_start=len(m.ub)
    for j in range(len(m.names)):m.le({j:1},1)
    return m


def verify(m,cert):
    assert cert['variables']==len(m.names)
    assert cert['inequalities']==len(m.ub) and cert['equalities']==len(m.eq)
    coef=[0]*len(m.names);rhs=0
    for key,rows,right in [('ub',m.ub,m.bu),('eq',m.eq,m.be)]:
        seen=set()
        for i,w in cert[key]:
            assert type(i) is int and 0<=i<len(rows) and i not in seen
            assert type(w) is int and (key=='eq' or w>=0)
            seen.add(i);rhs+=w*right[i]
            for j,c in rows[i].items():coef[j]+=w*c
    assert min(coef)>=0 and rhs==cert['rhs'] and rhs<0
    return dict(integer_columns_checked=len(coef),rhs=rhs)
