#!/usr/bin/env python3
"""Inverse scan of analytic BC potential cones on the n=29 t=2 frontier.

Instead of choosing a generated staircase dictionary, put one shared value F(d,v)
on every finite BC state, where

    label : d=R+s,       v=b-(R+x)
    source: d=rho+q-1,   v=b-(q+p).

Every actual selected incidence satisfies coordinatewise domination, so every
coordinatewise nondecreasing F gives the valid transport inequality

    sum_i x_i F(d_i,v_i) <= sum_u q_u F(alpha_u,w_u).

Two cones are tested:

  monotone     : arbitrary nonnegative coordinatewise-nondecreasing F;
  supermodular : monotone F plus nonnegative discrete mixed differences.

On a rectangular finite grid the latter is exactly the nonnegative cone generated
by single orthant indicators (rectangles), including axis/base terms. Thus a
supermodular failure but monotone success is direct evidence that the obstruction
needs genuinely non-supermodular staircase unions, not merely more diagonal
min-hinges or different slopes.

Optional SH correction uses all canonical n=29 SH staircase shapes. Floating LP
reconnaissance only; every positive compact result must be exactified before proof
use.
"""
from pathlib import Path
from collections import Counter
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py')
allx=module_from_spec(sp);sp.loader.exec_module(allx)

def leq(a,b): return all(x<=y for x,y in zip(a,b))
def inside(pt,g): return any(leq(q,pt) for q in g)
def tup(g): return tuple(tuple(p) for p in g)
def tterm(rho,q,p,j): return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)

class LP:
    def __init__(self):
        self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0.0):
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs): self.rows.append(row);self.rhs.append(rhs)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items(): A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')

def build(P,a,b,dmax,shapes,cone):
    M=LP()
    # Source d=rho+q-1 is at most a-1; label d is at most dmax.
    dtop=max(dmax,a-1)
    fv={(d,v):M.var(('F',d,v),(0,None),1.0) for d in range(dtop+1) for v in range(b+1)}
    sw=[M.var(('SH',i),(0,None),1.0) for i in range(len(shapes))]

    # Monotonicity in both BC coordinates.
    for d in range(dtop):
        for v in range(b+1): M.le({fv[d,v]:1,fv[d+1,v]:-1},0)
    for d in range(dtop+1):
        for v in range(b): M.le({fv[d,v]:1,fv[d,v+1]:-1},0)

    # Nonnegative mixed differences: F11-F10-F01+F00 >= 0.
    if cone=='supermodular':
        for d in range(dtop):
            for v in range(b):
                M.le({fv[d+1,v+1]:-1,fv[d+1,v]:1,fv[d,v+1]:1,fv[d,v]:-1},0)
    elif cone!='monotone':
        raise ValueError(cone)

    def addpot(row,d,h,shpt,factor,sign):
        v=b-h
        row[fv[d,v]]=row.get(fv[d,v],0)+sign*factor
        for i,g in enumerate(shapes):
            if inside(shpt,g): row[sw[i]]=row.get(sw[i],0)+sign*factor

    for pi,pf in enumerate(P):
        lam=M.var(('lambda',pi),(0,None),0.01)
        cc=M.var(('c',pi),(0,None),0.01)
        mp=M.var(('mu+',pi),(0,None),0.01)
        mm=M.var(('mu-',pi),(0,None),0.01)
        taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)}
        sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    d=R+s;h=R+x
                    row={e:1,lam:-R,cc:-x}
                    addpot(row,d,h,(s,-h),x,-1)
                    M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg
            qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    d=rho+q-1;h=q+pp
                    row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for j in range(1,a+1):
                        tv=tterm(rho,q,pp,j)
                        if tv: row[taus[j]]=row.get(taus[j],0)-tv
                    addpot(row,d,h,(rho,-h),q,1)
                    M.le(row,0)
        r=sum(pf['rho']);row={lam:r}
        for s,n in sc.items(): row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items(): row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M,fv

def load_profiles(z):
    if z.mode in ('hard38','demand45'):
        B=json.loads(z.boundary_json.read_text())
        R=B['trimmed_survivor_records']
        if z.mode=='demand45': R=[r for r in R if r['demand_id']==45][:1]
        return [{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in R]
    P=allx.load29(z.demands_json,z.rows,2)
    return [{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in P]

def analyse_surface(res,M,fv,a,b,dmax):
    dtop=max(dmax,a-1)
    vals={(d,v):float(res.x[i]) for (d,v),i in fv.items()}
    mx=max(vals.values()) if vals else 0.0
    eps=max(1e-9,mx*1e-9)
    active=[{'d':d,'v':v,'value':x} for (d,v),x in sorted(vals.items()) if x>eps]
    neg=[];pos=[]
    for d in range(dtop):
        for v in range(b):
            dd=vals[d+1,v+1]-vals[d+1,v]-vals[d,v+1]+vals[d,v]
            if dd < -eps: neg.append({'d':d,'v':v,'mixed_difference':dd})
            elif dd > eps: pos.append({'d':d,'v':v,'mixed_difference':dd})
    neg.sort(key=lambda q:q['mixed_difference'])
    pos.sort(key=lambda q:-q['mixed_difference'])
    # Level-set frontiers of the numerical surface, useful for inverse pattern mining.
    levels=sorted({round(x,10) for x in vals.values() if x>eps})
    level_frontiers=[]
    if len(levels)<=80:
        for L in levels:
            pts={(d,v) for (d,v),x in vals.items() if x>=L-1e-8}
            gens=[]
            for p in sorted(pts):
                if not any(q!=p and q[0]<=p[0] and q[1]<=p[1] for q in pts): gens.append(p)
            level_frontiers.append({'level':L,'generators':[list(p) for p in gens],'generator_count':len(gens)})
    return {'max_F':mx,'active_grid_count':len(active),'active_grid':active,
            'negative_mixed_count':len(neg),'negative_mixed_top':neg[:30],
            'positive_mixed_count':len(pos),'positive_mixed_top':pos[:30],
            'distinct_positive_levels':len(levels),'level_frontiers':level_frontiers}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['demand45','hard38','t2'],required=True)
    ap.add_argument('--cone',choices=['monotone','supermodular'],required=True)
    ap.add_argument('--sh-mode',choices=['none','full'],default='none')
    ap.add_argument('--a',type=int,default=12);ap.add_argument('--b',type=int,default=16);ap.add_argument('--dmax',type=int,default=10)
    ap.add_argument('--boundary-json',type=Path);ap.add_argument('--demands-json',type=Path);ap.add_argument('--rows',type=Path)
    ap.add_argument('--dictionary-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    z=ap.parse_args()
    if z.mode in ('hard38','demand45') and not z.boundary_json: raise SystemExit('--boundary-json required')
    if z.mode=='t2' and (not z.demands_json or not z.rows): raise SystemExit('--demands-json/--rows required')
    D=json.loads(z.dictionary_json.read_text());sh=[] if z.sh_mode=='none' else [tup(x['generators']) for x in D['SH']]
    P=load_profiles(z);st=time.time();M,fv=build(P,z.a,z.b,z.dmax,sh,z.cone);res=M.solve()
    out={'schema':'n29-t2-bc-function-cone-v1','mode':z.mode,'cone':z.cone,'SH_mode':z.sh_mode,'SH_count':len(sh),'profiles':len(P),
         'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,
         'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
    if res.success:
        out['surface']=analyse_surface(res,M,fv,z.a,z.b,z.dmax)
        ash=[]
        for i in range(len(sh)):
            w=float(res.x[M.idx[('SH',i)]])
            if w>1e-8: ash.append({'index':i,'weight':w,'generators':[list(p) for p in sh[i]]})
        out['active_SH']=ash;out['active_SH_count']=len(ash)
    out['interpretation']='Monotone F is the full finite cone of nonnegative BC-monotone potentials. Supermodular F is the single-rectangle cone. A supermodular failure with monotone success diagnoses a genuine staircase-union/non-supermodular requirement.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    brief={k:v for k,v in out.items() if k not in ('surface','active_SH')}
    if res.success: brief.update({'negative_mixed_count':out['surface']['negative_mixed_count'],'distinct_positive_levels':out['surface']['distinct_positive_levels'],'active_SH_count':out['active_SH_count']})
    print(json.dumps(brief,indent=2,sort_keys=True))
if __name__=='__main__': main()
