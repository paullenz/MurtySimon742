#!/usr/bin/env python3
"""Sparse inverse scan for the n=29,t=2 rectangle + one diagonal-step potential.

Every monotone supermodular BC potential has the exact finite decomposition

  G(d,v) = sum_{D<=d,V<=v} r[D,V],  r[D,V] >= 0,

so the generators are all orthant rectangles 1[d>=D,v>=V]. We add the single
non-supermodular diagonal generator

  J_b(d,v)=1[d+v>=b],

which is exactly the c=0 slack-threshold inequality from DIAGONAL_SLACK_THRESHOLD.md.

This script solves the common hard-profile LP directly in generator coordinates,
reports the active support, then optionally greedily deletes generators while
retaining floating feasibility. Positive results are reconnaissance until exactified.
"""
from pathlib import Path
from collections import Counter
import argparse,json,time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
class LP:
    def __init__(self):self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0.0):
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs):self.rows.append(row);self.rhs.append(rhs)
    def solve(self,bounds_override=None):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items():A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=(bounds_override or self.bounds),method='highs')

def build(P,a,b,dmax,with_diag=True):
    M=LP();dtop=max(dmax,a-1)
    rect=[]
    for D in range(dtop+1):
        for V in range(b+1):rect.append((D,V,M.var(('BCrect',D,V),(0,None),1.0)))
    diag=M.var(('Jb',),(0,None),1.0) if with_diag else None
    def addpot(row,d,h,factor,sign):
        v=b-h
        for D,V,w in rect:
            if d>=D and v>=V:row[w]=row.get(w,0)+sign*factor
        if diag is not None and d+v>=b:row[diag]=row.get(diag,0)+sign*factor
    for pi,pf in enumerate(P):
        lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01);mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01);taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)}
        sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    row={e:1,lam:-R,cc:-x};addpot(row,R+s,R+x,x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for j in range(1,a+1):
                        tv=tterm(rho,q,pp,j)
                        if tv:row[taus[j]]=row.get(taus[j],0)-tv
                    addpot(row,rho+q-1,q+pp,q,1);M.le(row,0)
        r=sum(pf['rho']);row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M,rect,diag

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--mode',choices=['demand45','hard38'],default='hard38');ap.add_argument('--no-diag',action='store_true');ap.add_argument('--greedy',action='store_true');ap.add_argument('--a',type=int,default=12);ap.add_argument('--b',type=int,default=16);ap.add_argument('--dmax',type=int,default=10);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());R=B['trimmed_survivor_records']
    if z.mode=='demand45':R=[r for r in R if r['demand_id']==45][:1]
    P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in R]
    st=time.time();M,rect,diag=build(P,z.a,z.b,z.dmax,not z.no_diag);res=M.solve();
    out={'schema':'n29-t2-rectdiag-sparse-v1','mode':z.mode,'profiles':len(P),'with_diag':not z.no_diag,'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
    if not res.success:
        z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return
    eps=1e-8
    active=[{'D':D,'V':V,'weight':float(res.x[w]),'var':w} for D,V,w in rect if res.x[w]>eps]
    out['diag_weight']=float(res.x[diag]) if diag is not None else None;out['active_rectangles_initial']=[{k:v for k,v in q.items() if k!='var'} for q in active];out['active_rectangle_count_initial']=len(active)
    if z.greedy:
        fixed=set(w for D,V,w in rect if res.x[w]<=eps)
        # Try deleting currently active generators in ascending fitted weight; repeat passes.
        changed=True;attempts=[]
        while changed:
            changed=False
            current=[q for q in active if q['var'] not in fixed]
            current.sort(key=lambda q:q['weight'])
            for q in current:
                trial=set(fixed);trial.add(q['var']);bd=list(M.bounds)
                for w in trial:bd[w]=(0,0)
                rr=M.solve(bd);attempts.append({'D':q['D'],'V':q['V'],'success':bool(rr.success)})
                if rr.success:
                    fixed=trial;res=rr;changed=True
                    # refresh weights/order after successful deletion
                    for qq in active:qq['weight']=float(res.x[qq['var']])
                    break
        afinal=[{'D':D,'V':V,'weight':float(res.x[w])} for D,V,w in rect if w not in fixed and res.x[w]>eps]
        out['greedy_attempts']=attempts;out['active_rectangles_greedy']=afinal;out['active_rectangle_count_greedy']=len(afinal);out['diag_weight_greedy']=float(res.x[diag]) if diag is not None else None;out['objective_greedy']=float(res.fun)
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('active_rectangles_initial','active_rectangles_greedy','greedy_attempts')},indent=2,sort_keys=True));print('initial rectangles',[(q['D'],q['V'],round(q['weight'],6)) for q in active]);print('greedy rectangles',[(q['D'],q['V'],round(q['weight'],6)) for q in out.get('active_rectangles_greedy',[])])
if __name__=='__main__':main()
