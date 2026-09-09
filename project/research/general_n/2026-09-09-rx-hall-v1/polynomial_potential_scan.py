#!/usr/bin/env python3
"""Search for low-degree monotone polynomial pairwise potentials.

For BC coordinates use u=d (or alpha) and v=b-h (or b-beta); for SH use
u=s (or rho) and the same v. On the finite domains u,v>=0 and both coordinates
increase in the relevant product order, so every monomial u^i v^j with
nonnegative coefficient is a valid monotone potential. Search

  F(d,h)=sum A_ij d^i (b-h)^j,
  G(s,h)=sum B_ij s^i (b-h)^j,

for 1<=i+j<=degree, A_ij,B_ij>=0. Profile-specific scalar residual/threshold
dual multipliers are allowed. Tests n30 alone, n29 residual corner alone, and
both orders together. Floating reconnaissance only; success requires later
exactification.
"""
from pathlib import Path
from collections import Counter
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
class LP:
    def __init__(self):self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0):
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs):self.rows.append(row);self.rhs.append(rhs)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items():A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')

def terms(deg):return [(i,j) for i in range(deg+1) for j in range(deg+1-i) if i+j>=1]
def build(P,deg):
    M=LP();T=terms(deg);A={ij:M.var(('F',)+ij,(0,None),1) for ij in T};B={ij:M.var(('G',)+ij,(0,None),1) for ij in T}
    def addpot(row,vars,u,v,factor,sign):
        for (i,j),w in vars.items():
            val=(u**i)*(v**j)
            if val:row[w]=row.get(w,0)+sign*factor*val
    for pi,pf in enumerate(P):
        a,b,dmax=pf['a'],pf['b'],pf['dmax'];lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01);mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01);taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)};sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    d=R+s;h=R+x;v=b-h;row={e:1,lam:-R,cc:-x};addpot(row,A,d,v,x,-1);addpot(row,B,s,v,x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    alpha=rho+q-1;beta=q+pp;v=b-beta;row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for jj in range(1,a+1):
                        tv=tterm(rho,q,pp,jj)
                        if tv:row[taus[jj]]=row.get(taus[jj],0)-tv
                    addpot(row,A,alpha,v,q,1);addpot(row,B,rho,v,q,1);M.le(row,0)
        r=sum(pf['rho']);row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M,T

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n30-json',type=Path,required=True);ap.add_argument('--n29-json',type=Path,required=True);ap.add_argument('--max-degree',type=int,default=5);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();N30=json.loads(z.n30_json.read_text());N29=json.loads(z.n29_json.read_text());p30=[{'order':'n30','s':r['s'],'rho':r['rho'],'a':13,'b':16,'dmax':11} for r in N30['records']];p29=[{'order':'n29','s':r['s'],'rho':r['rho'],'a':12,'b':16,'dmax':10} for r in N29['trimmed_survivor_records']]
    scopes={'n30':p30,'n29':p29,'both':p30+p29};results={}
    for scope,P in scopes.items():
        rr=[]
        for deg in range(1,z.max_degree+1):
            M,T=build(P,deg);res=M.solve();q={'degree':deg,'success':bool(res.success),'objective':float(res.fun) if res.success else None,'monomials_per_family':len(T)}
            if res.success:
                q['active_F']=[{'term':list(ij),'weight':float(res.x[M.idx[('F',)+ij]])} for ij in T if res.x[M.idx[('F',)+ij]]>1e-9];q['active_G']=[{'term':list(ij),'weight':float(res.x[M.idx[('G',)+ij]])} for ij in T if res.x[M.idx[('G',)+ij]]>1e-9];q['active_threshold_union']=sorted({j for pi,p in enumerate(P) for j in range(1,p['a']+1) if res.x[M.idx[('tau',pi,j)]]>1e-9})
            rr.append(q)
            if res.success:break
        results[scope]=rr
    out={'schema':'pairwise-monotone-polynomial-potential-scan-v1','floating_point_reconnaissance_only':True,'results':results,'interpretation':'Nonnegative monomial coefficients make F and G coordinatewise monotone on the finite pairwise order. Degree-1 is the scalar/first-moment class; higher degree tests smooth analytic alternatives to staircase lists.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({s:[{k:v for k,v in r.items() if k not in ('active_F','active_G')} for r in q] for s,q in results.items()},indent=2,sort_keys=True))
if __name__=='__main__':main()
