#!/usr/bin/env python3
"""MILP reconnaissance for a minimum-support staircase potential shared by all seven n30 profiles.

Uses the same envelope model as shared_sparse_staircase_scan.py, but introduces
binary selectors for all candidate BC and SH staircase weights and minimizes
support cardinality. This is floating/MILP reconnaissance only. Any nominated
support must be rebuilt and exactified separately before it becomes evidence.
"""
from collections import Counter
from pathlib import Path
import argparse,json
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

def leq(a,b): return all(x<=y for x,y in zip(a,b))
def min_gens(points):
    pts=sorted(set(tuple(p) for p in points))
    return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))
def inside(pt,gens): return any(leq(g,pt) for g in gens)
def tterm(rho,q,p,j): return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)

class MILP:
    def __init__(self): self.names=[];self.idx={};self.rows=[];self.lo=[];self.hi=[];self.lb=[];self.ub=[];self.integrality=[];self.c=[]
    def var(self,name,lb=-np.inf,ub=np.inf,integer=False,cost=0.0):
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.lb.append(lb);self.ub.append(ub);self.integrality.append(1 if integer else 0);self.c.append(cost);return i
    def le(self,row,rhs): self.rows.append(row);self.lo.append(-np.inf);self.hi.append(rhs)
    def solve(self,limit):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items(): A[i,j]=v
        cons=LinearConstraint(A.tocsr(),np.array(self.lo),np.array(self.hi))
        return milp(np.array(self.c),integrality=np.array(self.integrality),bounds=Bounds(np.array(self.lb),np.array(self.ub)),constraints=cons,options={'time_limit':limit,'mip_rel_gap':0.0})

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bc-json',type=Path,required=True);ap.add_argument('--sh-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--big-m',type=float,default=100.0);ap.add_argument('--time-limit',type=float,default=900.0);z=ap.parse_args()
    B=json.loads(z.bc_json.read_text());S=json.loads(z.sh_json.read_text())
    bcset=set()
    for rec in B['records']:
        for cut in rec['cuts']:
            pts=[(x['R']+x['s'],-(x['R']+x['x'])) for x in cut['label_states']]
            g=min_gens(pts)
            if g: bcset.add(g)
    bcshapes=sorted(bcset);shshapes=[tuple(tuple(x) for x in c['generators']) for c in S['sh_cuts']]
    P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['records']]
    M=MILP(); lam=M.var(('coef','lambda'),0,z.big_m);cc=M.var(('coef','c'),0,z.big_m);mp=M.var(('coef','mu+'),0,z.big_m);mm=M.var(('coef','mu-'),0,z.big_m);t2=M.var(('coef','tau2'),0,z.big_m);t3=M.var(('coef','tau3'),0,z.big_m)
    bw=[];by=[]
    for i in range(len(bcshapes)):
        w=M.var(('BC',i),0,z.big_m);y=M.var(('YBC',i),0,1,integer=True,cost=1);M.le({w:1,y:-z.big_m},0);bw.append(w);by.append(y)
    sw=[];sy=[]
    for i in range(len(shshapes)):
        w=M.var(('SH',i),0,z.big_m);y=M.var(('YSH',i),0,1,integer=True,cost=1);M.le({w:1,y:-z.big_m},0);sw.append(w);sy.append(y)
    def addpot(row,coord_bc,coord_sh,factor,sign):
        for i,g in enumerate(bcshapes):
            if inside(coord_bc,g): row[bw[i]]=row.get(bw[i],0)+sign*factor
        for i,g in enumerate(shshapes):
            if inside(coord_sh,g): row[sw[i]]=row.get(sw[i],0)+sign*factor
    meta=[]
    for pi,p in enumerate(P):
        sc=Counter(p['s']);rc=Counter(p['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s));ells[s]=e
            for R in range(z.dmax-s+1):
                for x in range(s,z.b-R+1):
                    d=R+s;h=R+x;row={e:1,lam:-R,cc:-x};addpot(row,(d,-h),(s,-h),x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho));sigs[rho]=sg;qmax=min(z.a-rho,sum(si<=rho for si in p['s']))
            for q in range(qmax+1):
                pmax=min(rho+z.b-z.a-1,z.b-1-q)
                for pp in range(pmax+1):
                    alpha=rho+q-1;beta=q+pp;row={sg:1,mp:-(q-pp),mm:(q-pp),t2:-tterm(rho,q,pp,2),t3:-tterm(rho,q,pp,3),cc:q};addpot(row,(alpha,-beta),(rho,-beta),q,1);M.le(row,0)
        r=sum(p['rho']);row={lam:r}
        for s,n in sc.items(): row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items(): row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1);meta.append({'profile':pi,'demand_id':p['demand_id'],'r':r})
    res=M.solve(z.time_limit)
    out={'schema':'n30-shared-min-support-milp-v1','success':bool(res.success),'status':int(res.status),'message':res.message,'BC_candidate_shapes':len(bcshapes),'SH_candidate_shapes':len(shshapes),'big_m':z.big_m,'time_limit':z.time_limit,'floating_point_reconnaissance_only':True,'profiles':meta}
    if res.x is not None:
        x=res.x;actbc=[{'index':i,'weight':float(x[w]),'generators':[list(p) for p in bcshapes[i]]} for i,w in enumerate(bw) if x[w]>1e-7];actsh=[{'index':i,'weight':float(x[w]),'generators':[list(p) for p in shshapes[i]]} for i,w in enumerate(sw) if x[w]>1e-7]
        out.update({'objective':float(res.fun) if res.fun is not None else None,'active_BC':actbc,'active_SH':actsh,'active_BC_count':len(actbc),'active_SH_count':len(actsh),'support_count':len(actbc)+len(actsh),'mip_gap':getattr(res,'mip_gap',None),'mip_node_count':getattr(res,'mip_node_count',None)})
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('active_BC','active_SH','profiles')},indent=2,sort_keys=True))
if __name__=='__main__': main()
