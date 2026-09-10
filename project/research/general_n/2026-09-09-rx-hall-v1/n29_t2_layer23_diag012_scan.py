#!/usr/bin/env python3
"""Test the compact n=29,t=2 potential family:

  - BC rectangle thresholds only on d-layers D=2 and D=3;
  - diagonal slack thresholds K=b,b-1,b-2 (c=0,1,2);
  - no SH corrections.

Thus

  F(d,v)=1[d>=2] A(v)+1[d>=3] B(v)
         + gamma0 1[d+v>=b]
         + gamma1 1[d+v>=b-1]
         + gamma2 1[d+v>=b-2],

with A,B nondecreasing step functions represented by nonnegative increments.
This is a sharply reduced, still universally valid monotone BC potential family.

Floating reconnaissance only.  A successful finite result must be exactified
before proof use.
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

def tterm(rho,q,p,j): return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)

class LP:
    def __init__(self): self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0.0):
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs): self.rows.append(row);self.rhs.append(rhs)
    def solve(self,bounds_override=None):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items(): A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=(bounds_override or self.bounds),method='highs')

def build(P,a=12,b=16,dmax=10,layers=(2,3),steps=(14,15,16)):
    M=LP(); rect=[]
    for D in layers:
        for V in range(b+1): rect.append((D,V,M.var(('BCrect',D,V),(0,None),1.0)))
    diag=[(K,M.var(('J',K),(0,None),1.0)) for K in steps]
    def addpot(row,d,h,factor,sign):
        v=b-h
        for D,V,w in rect:
            if d>=D and v>=V: row[w]=row.get(w,0)+sign*factor
        for K,w in diag:
            if d+v>=K: row[w]=row.get(w,0)+sign*factor
    for pi,pf in enumerate(P):
        lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01)
        mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01)
        taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)}
        sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    row={e:1,lam:-R,cc:-x};addpot(row,R+s,R+x,x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg
            qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for j in range(1,a+1):
                        tv=tterm(rho,q,pp,j)
                        if tv: row[taus[j]]=row.get(taus[j],0)-tv
                    addpot(row,rho+q-1,q+pp,q,1);M.le(row,0)
        row={lam:sum(pf['rho'])}
        for s,n in sc.items(): row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items(): row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M,rect,diag

def load_profiles(z):
    if z.mode=='hard38':
        B=json.loads(z.boundary_json.read_text())
        return [{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    P=allx.load29(z.demands_json,z.rows,2)
    return [{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in P]

def extract(res,rect,diag,eps=1e-8):
    return ([{'D':D,'V':V,'weight':float(res.x[w]),'var':w} for D,V,w in rect if res.x[w]>eps],
            [{'K':K,'c':16-K,'weight':float(res.x[w]),'var':w} for K,w in diag if res.x[w]>eps])

def greedy_prune(M,res,rect,diag):
    gen=[w for D,V,w in rect]+[w for K,w in diag]; fixed={w for w in gen if res.x[w]<=1e-8}; attempts=[]
    changed=True
    while changed:
        changed=False
        current=[w for w in gen if w not in fixed and res.x[w]>1e-8]
        current.sort(key=lambda w:float(res.x[w]))
        for w in current:
            bd=list(M.bounds);trial=set(fixed);trial.add(w)
            for q in trial: bd[q]=(0,0)
            rr=M.solve(bd);attempts.append({'generator':str(M.names[w]),'success':bool(rr.success)})
            if rr.success:
                fixed=trial;res=rr;changed=True;break
    ar,ad=extract(res,rect,diag)
    return res,ar,ad,attempts

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['hard38','t2'],required=True)
    ap.add_argument('--boundary-json',type=Path);ap.add_argument('--demands-json',type=Path);ap.add_argument('--rows',type=Path)
    ap.add_argument('--greedy',action='store_true');ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    if z.mode=='hard38' and not z.boundary_json: raise SystemExit('--boundary-json required')
    if z.mode=='t2' and (not z.demands_json or not z.rows): raise SystemExit('--demands-json and --rows required')
    P=load_profiles(z);st=time.time();M,rect,diag=build(P);res=M.solve()
    out={'schema':'n29-t2-layer23-diag012-v1','mode':z.mode,'profiles':len(P),'layers':[2,3],'diagonal_K':[14,15,16],'diagonal_c':[2,1,0],
         'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,
         'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
    if res.success:
        ar,ad=extract(res,rect,diag);out['active_rectangles_initial']=[{k:v for k,v in q.items() if k!='var'} for q in ar];out['active_diagonals_initial']=[{k:v for k,v in q.items() if k!='var'} for q in ad];out['active_generator_count_initial']=len(ar)+len(ad)
        if z.greedy:
            res2,ar2,ad2,att=greedy_prune(M,res,rect,diag);out['active_rectangles_greedy']=[{k:v for k,v in q.items() if k!='var'} for q in ar2];out['active_diagonals_greedy']=[{k:v for k,v in q.items() if k!='var'} for q in ad2];out['active_generator_count_greedy']=len(ar2)+len(ad2);out['greedy_attempts']=att;out['objective_greedy']=float(res2.fun)
    out['interpretation']='Tests the two d-layer BC family 1[d>=2]A(v)+1[d>=3]B(v) plus the three exact slack thresholds c=0,1,2. No SH. Positive results remain floating until exactified.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('active_rectangles_initial','active_diagonals_initial','active_rectangles_greedy','active_diagonals_greedy','greedy_attempts')},indent=2,sort_keys=True))
    if res.success:
        print('initial rect',[(q['D'],q['V'],round(q['weight'],6)) for q in out['active_rectangles_initial']]);print('initial diag',[(q['K'],round(q['weight'],6)) for q in out['active_diagonals_initial']])
        if z.greedy:
            print('greedy rect',[(q['D'],q['V'],round(q['weight'],6)) for q in out['active_rectangles_greedy']]);print('greedy diag',[(q['K'],round(q['weight'],6)) for q in out['active_diagonals_greedy']])
if __name__=='__main__': main()
