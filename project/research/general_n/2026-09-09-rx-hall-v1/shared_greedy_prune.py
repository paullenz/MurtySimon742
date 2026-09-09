#!/usr/bin/env python3
"""Greedy support pruning for the shared n30 staircase-potential LP.

Starts from a supplied BC/SH support (normally the active support from the
L1 shared scan), repeatedly tries deleting one shape, and keeps any deletion
for which the shared envelope LP remains feasible with margin >=1 on all seven
profiles. Floating-point reconnaissance only; final support must be exactified.
"""
from collections import Counter
from pathlib import Path
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def inside(pt,gens):return any(leq(g,pt) for g in gens)
def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)

class LP:
    def __init__(self):self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0.0):i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs):self.rows.append(row);self.rhs.append(rhs)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items():A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')

def build(P,bcshapes,shshapes,a,b,dmax):
    M=LP();lam=M.var(('coef','lambda'),(0,None),1);cc=M.var(('coef','c'),(0,None),1);mp=M.var(('coef','mu+'),(0,None),1);mm=M.var(('coef','mu-'),(0,None),1);t2=M.var(('coef','tau2'),(0,None),1);t3=M.var(('coef','tau3'),(0,None),1)
    bw=[M.var(('BC',i),(0,None),1) for i in range(len(bcshapes))];sw=[M.var(('SH',i),(0,None),1) for i in range(len(shshapes))]
    def addpot(row,coord_bc,coord_sh,factor,sign):
        for i,g in enumerate(bcshapes):
            if inside(coord_bc,g):row[bw[i]]=row.get(bw[i],0)+sign*factor
        for i,g in enumerate(shshapes):
            if inside(coord_sh,g):row[sw[i]]=row.get(sw[i],0)+sign*factor
    for pi,p in enumerate(P):
        sc=Counter(p['s']);rc=Counter(p['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    d=R+s;h=R+x;row={e:1,lam:-R,cc:-x};addpot(row,(d,-h),(s,-h),x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in p['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    alpha=rho+q-1;beta=q+pp;row={sg:1,mp:-(q-pp),mm:(q-pp),t2:-tterm(rho,q,pp,2),t3:-tterm(rho,q,pp,3),cc:q};addpot(row,(alpha,-beta),(rho,-beta),q,1);M.le(row,0)
        r=sum(p['rho']);row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M

def solve(P,bcshapes,shshapes,a,b,dmax):
    M=build(P,bcshapes,shshapes,a,b,dmax);return M,M.solve()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bc-json',type=Path,required=True);ap.add_argument('--shared-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.bc_json.read_text());J=json.loads(z.shared_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['records']]
    bc=[tuple(tuple(p) for p in x['generators']) for x in J['active_BC']];sh=[tuple(tuple(p) for p in x['generators']) for x in J['active_SH']]
    history=[];changed=True
    while changed:
        changed=False
        candidates=[('BC',i) for i in range(len(bc))]+[('SH',i) for i in range(len(sh))]
        for fam,i in candidates:
            bc2=bc[:i]+bc[i+1:] if fam=='BC' else list(bc);sh2=sh[:i]+sh[i+1:] if fam=='SH' else list(sh)
            _,res=solve(P,bc2,sh2,z.a,z.b,z.dmax)
            if res.success:
                history.append({'deleted_family':fam,'deleted_index':i,'remaining_BC':len(bc2),'remaining_SH':len(sh2),'objective':float(res.fun)})
                bc,sh=bc2,sh2;changed=True;break
    M,final=solve(P,bc,sh,z.a,z.b,z.dmax)
    vals={str(name):float(final.x[i]) for i,name in enumerate(M.names)} if final.success else {}
    out={'schema':'n30-shared-greedy-prune-v2','success':bool(final.success),'floating_point_reconnaissance_only':True,'initial_BC':len(J['active_BC']),'initial_SH':len(J['active_SH']),'final_BC_count':len(bc),'final_SH_count':len(sh),'support_count':len(bc)+len(sh),'BC_shapes':[[list(p) for p in g] for g in bc],'SH_shapes':[[list(p) for p in g] for g in sh],'history':history,'final_objective':float(final.fun) if final.success else None,'variables':vals}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_shapes','SH_shapes','history','variables')},indent=2,sort_keys=True))
if __name__=='__main__':main()
