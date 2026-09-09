#!/usr/bin/env python3
"""Test a common staircase potential with profile-specific scalar dual multipliers.

A single nonnegative BC/SH staircase-weight vector (hence one common F+G) is
shared by all 38 n29 t=2 survivors. For each profile separately, allow its own
lambda,c,mu and tau_h multipliers for the residual/q-p/threshold identities, plus
its own label/source envelope variables. This distinguishes universality of the
combinatorial potential from universality of algebraic dual bookkeeping.

Tests the specialised n30 base 6+3 dictionary and the full generated n29 pairwise
cut dictionary. Floating reconnaissance only; any compact success is exactified
later.
"""
from pathlib import Path
from collections import Counter
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('gp',HERE/'shared_greedy_prune.py');gp=module_from_spec(sp);sp.loader.exec_module(gp)

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def min_gens(g):
    pts=sorted(set(tuple(p) for p in g));return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))
def trim(g,dmax):return min_gens(p for p in g if p[0]<=dmax)
def inside(pt,g):return any(leq(q,pt) for q in g)
def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)

class LP:
    def __init__(self):self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0.0):
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs):self.rows.append(row);self.rhs.append(rhs)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items():A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')

def build(P,bc,sh,a,b,dmax):
    M=LP();bw=[M.var(('BC',i),(0,None),1) for i in range(len(bc))];sw=[M.var(('SH',i),(0,None),1) for i in range(len(sh))]
    for pi,pf in enumerate(P):
        lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01);mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01);taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)}
        sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        def addpot(row,cb,cs,factor,sign):
            for i,g in enumerate(bc):
                if inside(cb,g):row[bw[i]]=row.get(bw[i],0)+sign*factor
            for i,g in enumerate(sh):
                if inside(cs,g):row[sw[i]]=row.get(sw[i],0)+sign*factor
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    row={e:1,lam:-R,cc:-x};addpot(row,(R+s,-(R+x)),(s,-(R+x)),x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for j in range(1,a+1):
                        tv=tterm(rho,q,pp,j)
                        if tv:row[taus[j]]=row.get(taus[j],0)-tv
                    addpot(row,(rho+q-1,-(q+pp)),(rho,-(q+pp)),q,1);M.le(row,0)
        r=sum(pf['rho']);row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());S=json.loads(z.support_json.read_text());C=json.loads(z.correction_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    basebc={trim(tuple(tuple(p) for p in x['generators']),z.dmax) for x in S['active_BC']};basesh={tuple(tuple(p) for p in x['generators']) for x in S['active_SH']};fullbc=set(basebc);fullsh=set(basesh)
    for r in C['records']:
        for x in r['cuts']:
            g=tuple(tuple(p) for p in x['generators']);(fullbc if x['family']=='BC' else fullsh).add(g)
    modes={'base':(sorted(basebc),sorted(basesh)),'full':(sorted(fullbc),sorted(fullsh))};outm={}
    for name,(bc,sh) in modes.items():
        M=build(P,bc,sh,z.a,z.b,z.dmax);res=M.solve();q={'success':bool(res.success),'BC_shapes':len(bc),'SH_shapes':len(sh),'objective':float(res.fun) if res.success else None}
        if res.success:
            actbc=[i for i in range(len(bc)) if res.x[M.idx[('BC',i)]]>1e-8];actsh=[i for i in range(len(sh)) if res.x[M.idx[('SH',i)]]>1e-8]
            q.update({'active_BC':len(actbc),'active_SH':len(actsh),'active_BC_shapes':[[list(p) for p in bc[i]] for i in actbc],'active_SH_shapes':[[list(p) for p in sh[i]] for i in actsh],'BC_weights':[float(res.x[M.idx[('BC',i)]]) for i in actbc],'SH_weights':[float(res.x[M.idx[('SH',i)]]) for i in actsh],'threshold_union':sorted({j for pi in range(len(P)) for j in range(1,z.a+1) if res.x[M.idx[('tau',pi,j)]]>1e-8})})
        outm[name]=q
    out={'schema':'n29-common-potential-profile-scalars-v1','profiles':len(P),'floating_point_reconnaissance_only':True,'modes':outm,'interpretation':'BC/SH staircase weights are common across all 38 profiles; lambda,c,mu,tau_h and envelopes are profile-specific. Success isolates universality of F+G from scalar dual bookkeeping.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:{kk:vv for kk,vv in v.items() if kk not in ('active_BC_shapes','active_SH_shapes','BC_weights','SH_weights')} for k,v in outm.items()},indent=2,sort_keys=True))
if __name__=='__main__':main()
