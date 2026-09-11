#!/usr/bin/env python3
"""Discover small integer Hall weights; every accepted result is rechecked exactly."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import json
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix
from mine_scalar_excess import types,h

HERE=Path(__file__).resolve().parent

@lru_cache(None)
def minimum(r,qmax,c,w):
    # Analytic endpoint reduction in p; no LP participates in acceptance.
    Z=[sum(w[:i]) for i in range(13)]
    return min(q*(Z[max(0,q-1)]+w[12]-c)+min(0,-(r-1)*(Z[min(12,r+q)]+w[12]),3*q-(r+2)*(Z[min(12,r+q)]+w[12])) for q in range(qmax+1))

def gap(row,w):
    s=row['s'];c=max(s)+3
    return c*sum(s)+sum(n*minimum(r,min(13-r,sum(si<=r for si in s)),c,w) for r,n in Counter(row['rho']).items())

def compress(rows,ids,D):
    # Nonnegative integer z_k. The unrestricted equality multiplier nu is zero
    # in every discovered useful template, so omit it here.
    ng=12;keys=[];var={}
    for i in ids:
        for r in sorted(set(rows[i]['rho'])):var[i,r]=ng+len(keys);keys.append((i,r))
    N=ng+len(keys);rr=[];cc=[];vv=[];lo=[];hi=[]
    def add(d,l,u):
        j=len(lo);lo.append(l);hi.append(u)
        for k,v in d.items():
            if v:rr.append(j);cc.append(k);vv.append(v)
    for i,r in keys:
        s=rows[i]['s'];c=max(s)+3
        for q,p in types(s,r):
            d={k-1:-h(k,r,q,p) for k in range(1,13)};d[var[i,r]]=1
            add(d,-np.inf,D*q*(max(0,p-r+1)-c))
    for i in ids:
        s=rows[i]['s'];c=max(s)+3
        add({var[i,r]:n for r,n in Counter(rows[i]['rho']).items()},1-D*c*sum(s),np.inf)
    A=coo_matrix((vv,(rr,cc)),shape=(len(lo),N)).tocsc()
    sol=milp(np.array([1.0]*ng+[0.0]*len(keys)),integrality=np.ones(N),bounds=Bounds([0]*ng+[-10000]*len(keys),[1000]*ng+[10000]*len(keys)),constraints=LinearConstraint(A,lo,hi),options={'time_limit':8})
    if sol.x is None:return {'status':int(sol.status),'D':D}
    z=[int(round(x)) for x in sol.x[:ng]];w=tuple(F(x,D) for x in z)+(F(0),)
    gaps=[gap(rows[i],w) for i in ids]
    if min(gaps)<=0:return {'status':int(sol.status),'D':D,'exact_rejected':True}
    return {'status':int(sol.status),'D':D,'z':z,'min_gap':str(min(gaps)),'assigned':ids}

if __name__=='__main__':
    rows=json.loads((HERE/'SCALAR_EXCESS_DISCOVERY.json').read_text())['rows']
    ws=list(dict.fromkeys(tuple(map(F,r['weights'])) for r in rows if r.get('exact_positive')))
    covers=[{i for i,row in enumerate(rows) if gap(row,w)>0} for w in ws]
    rem=set().union(*covers);out=[]
    while rem:
        j=max(range(len(ws)),key=lambda j:len(covers[j]&rem));ids=sorted(covers[j]&rem);rem-=set(ids)
        attempts=[]
        for D in (2,3,4,6,12,24,60):
            rec=compress(rows,ids,D);attempts.append(rec)
            if 'z' in rec:break
        if 'z' not in rec:
            rec={'weights':list(map(str,ws[j])),'assigned':ids}
        out.append({'attempts':attempts,'certificate':rec})
        print('template',len(out),'assigned',len(ids),'certificate',rec,flush=True)
    (HERE/'SMALL_SCALAR_TEMPLATES.json').write_text(json.dumps(out,indent=2)+'\n')
    # Preserve the explicit acceptance input separately from optimizer diagnostics.
    certificates=[]
    for j,item in enumerate(out,1):
        c=item['certificate']
        if 'z' not in c:
            raise RuntimeError('Integer compression incomplete; diagnostics preserved')
        certificates.append({'name':f'T{j}','D':c['D'],
                             'weights':{str(k+1):v for k,v in enumerate(c['z']) if v},
                             'assigned_rows':[{'s':rows[i]['s'],'rho':rows[i]['rho']} for i in c['assigned']]})
    (HERE/'SCALAR_CERTIFICATES.json').write_text(json.dumps({'schema':'n30-m225-seven-scalar-certificates-v1','templates':certificates},indent=2)+'\n')
