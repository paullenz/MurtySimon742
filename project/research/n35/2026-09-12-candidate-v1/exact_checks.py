#!/usr/bin/env python3
"""N35 exact local formulas; no discovery or numerical imports.

Adapted from the separately implemented N34 formula verifier.
"""
from collections import Counter
from functools import lru_cache
A,B,DMAX,T=15,19,13,2
FIXED9=[('BC',2,18,4),('BC',2,11,2),('BC',2,9,1),('BC',2,7,1),
        ('BC',2,4,1),('BC',2,3,1),('BC',3,8,1),('BC',3,6,1),('BC',3,5,1)]
FIXED13=[('BC',1,9,7),('BC',1,6,11),('BC',1,4,5),('BC',1,3,21),
         ('BC',1,2,29),('BC',1,1,39),('BC',2,4,6),('BC',3,8,5),
         ('BC',3,7,8),('BC',3,5,11),('DIAG',-1,0,17),('DIAG',0,0,8),('SH',2,17,39)]


def feature(kind,k,H,s,d,h):
    if kind=='BC':return d>=k and h<=H
    if kind=='SH':return s>=k and h<=H
    assert kind=='DIAG'
    return d-h>=k


def envelope(rec):
    s,rho=rec['s'],rec['rho'];mode=rec['method']
    assert mode in ('fixed9','fixed13','adaptive')
    E=sum(s)-sum(rho)-2*T
    assert E>=0 and (E==0 or s.count(0)<=1)
    assert min(s)==0 or E==0
    den=rec['denominator'];assert type(den) is int and den>0
    names=[tuple(n) if isinstance(n,list) else n for n in rec['names']]
    nums=rec['numerators']
    assert len(names)==len(set(names))==len(nums) and all(type(v) is int for v in nums)
    X=dict(zip(names,nums))
    required={'lambda','c','mu'}|{('tau',j) for j in range(1,A+1)}
    required|={('ell',v) for v in s}|{('sig',v) for v in rho}
    weights=[]
    if mode=='adaptive':
        for name,w in X.items():
            if isinstance(name,tuple) and name[0]=='weight':
                assert len(name)==4 and w>=0
                _,kind,k,H=name
                assert type(k) is int and type(H) is int
                assert ((kind=='BC' and 1<=k<=DMAX and 0<=H<=B)
                        or (kind=='SH' and 1<=k<A and 0<=H<=B)
                        or (kind=='DIAG' and -B<=k<A and H==0))
                required.add(name);weights.append((kind,k,H,w))
    else:
        weights=[(kind,k,H,w*den) for kind,k,H,w in (FIXED9 if mode=='fixed9' else FIXED13)]
    assert set(X)==required
    assert all(X['tau',j]>=0 for j in range(1,A+1))

    @lru_cache(None)
    def phi(s0,d,h):
        return sum(w*feature(kind,k,H,s0,d,h) for kind,k,H,w in weights)

    checks=0
    for sv in sorted(set(s)):
        options=0
        for R in range(B+1):
            d=R+sv if sv else R-E
            if not 0<=d<=DMAX:continue
            xmax=min(B-R,sum(rv>=sv for rv in rho))
            for x in range(sv,xmax+1):
                assert X['ell',sv]<=X['lambda']*R+X['c']*x+x*phi(sv,d,R+x)
                checks+=1;options+=1
        assert options
    for rv in sorted(set(rho)):
        qmax=min(A-rv,sum(sv<=rv for sv in s))
        for q in range(qmax+1):
            for p in range(min(rv+B-A-1,B-1-q)+1):
                trans=sum(X['tau',j]*((q if q>=j+1 else 0)-(p if rv+q>=j else 0))
                          for j in range(1,A+1))
                assert X['sig',rv]<=X['mu']*(q-p)-X['c']*q+trans-q*phi(rv,rv+q-1,q+p)
                checks+=1
    gap=X['lambda']*sum(rho)
    gap-=sum(n*X['ell',v] for v,n in Counter(s).items())
    gap-=sum(n*X['sig',v] for v,n in Counter(rho).items())
    assert gap==rec['gap'] and gap<0
    return checks,gap


def hand(rec):
    s,rho=rec['s'],rec['rho'];method=rec['method']
    if method=='positive_degree_mass':
        assert min(s)>0 and sum(s)!=sum(rho)+2*T
        assert (rec['S'],rec['r'])==(sum(s),sum(rho));return
    h=rec['h'];assert type(h) is int and h>=1
    W=sum(v for v in s if v>=h);z=sum(rv>=h for rv in rho)
    assert (rec['W'],rec['z'])==(W,z)
    if method=='tight_subset_threshold':
        assert h>=2 and z>=h and 2*W==z*(z-1)+h*(h+1)
        lower=W-h*(h+1);upper=sum(rv-1 for rv in rho if rv>=h)
        assert (rec['incoming_lower'],rec['incoming_upper'])==(lower,upper)
        assert lower>upper;return
    assert method=='source_capped_threshold'
    caps=[min(A-rv,sum(h<=sv<=rv for sv in s)) for rv in rho if rv>=h]
    assert caps==rec['capacities'] and all(c>=0 for c in caps)
    high=sorted((c for c in caps if c>h),reverse=True)
    L=sum(min(h,c) for c in caps)
    bounds=[]
    for j in range(len(high)+1):
        pair_limit=j*(z-j)+j*(j-1)//2
        bounds.append(L-j*h+min(sum(high[:j]),pair_limit))
    assert bounds==rec['upper_bounds'] and W>max(bounds)
