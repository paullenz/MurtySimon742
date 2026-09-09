#!/usr/bin/env python3
"""Reconnaissance for one common F+G across the n29 and n30 hard frontiers.

Profiles:
  * all seven n30 equality-frontier residual-budget hard profiles, a=13,b=16,dmax=11;
  * the 38 n29 t=2 profiles surviving n30-dictionary boundary specialisation,
    a=12,b=16,dmax=10.

Candidate dictionary is the union of every generated n30 BC staircase, the four
n30 SH corrections, and every generated n29 BC/SH correction shape. Staircase
weights are common across all 45 profiles. Each profile has its own lambda,c,mu,
tau_h and envelope variables. Floating reconnaissance only.
"""
from pathlib import Path
from collections import Counter
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def min_gens(points):
    pts=sorted(set(tuple(p) for p in points));return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))
def inside(pt,g):return any(leq(q,pt) for q in g)
def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
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

def build(profiles,bc,sh):
    M=LP();bw=[M.var(('BC',i),(0,None),1) for i in range(len(bc))];sw=[M.var(('SH',i),(0,None),1) for i in range(len(sh))]
    for pi,pf in enumerate(profiles):
        a,b,dmax=pf['a'],pf['b'],pf['dmax'];lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01);mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01);taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)}
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
    ap=argparse.ArgumentParser();ap.add_argument('--n30-bc-json',type=Path,required=True);ap.add_argument('--n30-sh-json',type=Path,required=True);ap.add_argument('--n29-boundary-json',type=Path,required=True);ap.add_argument('--n29-correction-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B30=json.loads(z.n30_bc_json.read_text());S30=json.loads(z.n30_sh_json.read_text());B29=json.loads(z.n29_boundary_json.read_text());C29=json.loads(z.n29_correction_json.read_text())
    bc=set();sh=set()
    # n30 BC generated shapes: derive generators from stored label-state upper sets.
    for r in B30['records']:
        for c in r['cuts']:
            g=min_gens((x['R']+x['s'],-(x['R']+x['x'])) for x in c['label_states'])
            if g:bc.add(g)
    # n30 generated SH corrections.
    for c in S30['sh_cuts']:
        sh.add(tuple(tuple(p) for p in c['generators']))
    # n29 all generated pairwise corrections (plus their specialised base support).
    for g in C29['base_support']['BC']:bc.add(tuple(tuple(p) for p in g))
    for g in C29['base_support']['SH']:sh.add(tuple(tuple(p) for p in g))
    for r in C29['records']:
        for c in r['cuts']:
            g=tuple(tuple(p) for p in c['generators']);(bc if c['family']=='BC' else sh).add(g)
    bc=sorted(bc);sh=sorted(sh);profiles=[]
    for i,r in enumerate(B30['records']):profiles.append({'order':'n30','id':i,'s':r['s'],'rho':r['rho'],'a':13,'b':16,'dmax':11})
    for r in B29['trimmed_survivor_records']:profiles.append({'order':'n29','id':r['hard_position'],'s':r['s'],'rho':r['rho'],'a':12,'b':16,'dmax':10})
    M=build(profiles,bc,sh);res=M.solve();out={'schema':'cross-order-common-potential-v1','profiles':len(profiles),'n30_profiles':7,'n29_profiles':38,'candidate_BC':len(bc),'candidate_SH':len(sh),'success':bool(res.success),'objective':float(res.fun) if res.success else None,'floating_point_reconnaissance_only':True}
    if res.success:
        ab=[i for i in range(len(bc)) if res.x[M.idx[('BC',i)]]>1e-8];ash=[i for i in range(len(sh)) if res.x[M.idx[('SH',i)]]>1e-8]
        out.update({'active_BC':len(ab),'active_SH':len(ash),'support_count':len(ab)+len(ash),'BC_shapes':[[list(p) for p in bc[i]] for i in ab],'SH_shapes':[[list(p) for p in sh[i]] for i in ash],'BC_weights':[float(res.x[M.idx[('BC',i)]]) for i in ab],'SH_weights':[float(res.x[M.idx[('SH',i)]]) for i in ash],'threshold_union_by_order':{order:sorted({j for pi,p in enumerate(profiles) if p['order']==order for j in range(1,p['a']+1) if res.x[M.idx[('tau',pi,j)]]>1e-8}) for order in ('n29','n30')}})
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_shapes','SH_shapes','BC_weights','SH_weights')},indent=2,sort_keys=True))
if __name__=='__main__':main()
