#!/usr/bin/env python3
"""Exactify the selected nine-feature BC min-hinge potential on n29 t=3.

Potential coordinates are d=R+s / alpha=rho+q-1 and v=b-h. Selected features
are H_{D,V}(d,v)=min((d-D)_+,(v-V)_+), with nonnegative common coefficients.
Floating LP is proposal only. Acceptance scales to rational integer numerators,
repairs free ell/sig envelopes downward, and checks every model row and bound
with Python integer arithmetic, using -scale for each profile-margin rhs -1.
"""
from pathlib import Path
from collections import Counter
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('ex',HERE/'n29_all_t23_exactify.py');ex=module_from_spec(sp);sp.loader.exec_module(ex)

def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
def hval(D,V,u,v):return min(max(0,u-D),max(0,v-V))
class LP:
    def __init__(self):self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0):
        if name in self.idx:return self.idx[name]
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs):self.rows.append(row);self.rhs.append(rhs)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items():A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')
def build(P,spec,a=12,b=16,dmax=10):
    M=LP();W=[M.var(('H',D,V),(0,None),1) for D,V in spec]
    def addpot(row,u,v,factor,sign):
        for w,(D,V) in zip(W,spec):
            z=hval(D,V,u,v)
            if z:row[w]=row.get(w,0)+sign*factor*z
    for pi,pf in enumerate(P):
        lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01);mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01);taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)};sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    d=R+s;v=b-(R+x);row={e:1,lam:-R,cc:-x};addpot(row,d,v,x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    alpha=rho+q-1;v=b-(q+pp);row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for jj in range(1,a+1):
                        tv=tterm(rho,q,pp,jj)
                        if tv:row[taus[jj]]=row.get(taus[jj],0)-tv
                    addpot(row,alpha,v,q,1);M.le(row,0)
        r=sum(pf['rho']);row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--boost',type=int,default=2);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();P=ex.load(z.demands,z.rows,3);J=json.loads(z.support_json.read_text());spec=[tuple(x['param']) for x in J['active_features'] if x['kind']=='min']
    M=build(P,spec);res=M.solve()
    if not res.success:raise SystemExit('selected nine-hinge support no longer numerically feasible')
    chosen=None;meta=None;attempts=[]
    for scale in (10**6,10**8,10**10):
        X,m=ex.exact_attempt(M,res,scale,z.boost,len(P));attempts.append(m)
        if X is not None:chosen=X;meta=m;break
    passed=chosen is not None
    out={'schema':'n29-t3-min-hinge-exact-v1','status':'PASS' if passed else 'FAIL','profiles':len(P),'feature_count':len(spec),'features':[list(x) for x in spec],'rows':len(M.rows),'variables':len(M.names),'integer_arithmetic_only_acceptance':True,'floating_point_proposal_only':True,'correct_scaled_rhs_rule':True,'attempts':attempts,'interpretation':'PASS gives one exact rational BC-only analytic min-hinge potential across all 94 regenerated n29 t=3 hard profiles. Finite evidence conditional on the RX-Hall bridge/frontier preparation.'}
    if passed:
        out.update(meta);out['integer_feature_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0]=='H'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('attempts','integer_feature_numerators')},indent=2,sort_keys=True))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
