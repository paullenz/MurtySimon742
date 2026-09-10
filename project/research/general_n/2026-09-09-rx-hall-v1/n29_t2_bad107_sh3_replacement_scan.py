#!/usr/bin/env python3
"""Can the natural first-coordinate Hall threshold S=3 replace a 2-D family?

Scope: the 107 n=29,t=2 profiles isolated as obstructions to the naive
three-rectangle potential.  The full 2-D family D2+D3+D4+J0+J2 is feasible,
and each of its five families is individually indispensable within that 2-D
basis.  Here we restore one coordinate discarded by the projection:

    H_3(s) = 1[s >= 3],  H_3(rho) = 1[rho >= 3].

The exact incidence coupling has s<=rho, hence

    sum_i x_i H_3(s_i) <= sum_u q_u H_3(rho_u).

We add one nonnegative common SH3 weight and retest each one-family deletion.
Floating reconnaissance only.  Success means the 3-D coordinate can replace
that deleted family on bad107; it must then be tested on all 902 profiles and
exactified before proof use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from collections import Counter
import argparse,json,time

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)

BAD=[0,1,2,3,4,5,6,7,8,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,38,39,40,77,78,79,82,84,87,91,92,93,94,107,112,113,121,126,127,128,129,134,135,136,145,173,178,180,181,192,193,194,195,196,197,208,209,210,211,212,231,232,256,257,258,259,260,368,381,382,385,403,404,410,411,412,415,435,436,437,438,439,440,441,442,483,498,499,501,502,503,505,566,567,570,681,683]
S=3
CASES=[
 ('drop_D2_plus_SH3',(3,4),(14,16)),
 ('drop_D3_plus_SH3',(2,4),(14,16)),
 ('drop_D4_plus_SH3',(2,3),(14,16)),
 ('drop_J0_plus_SH3',(2,3,4),(14,)),
 ('drop_J2_plus_SH3',(2,3,4),(16,)),
 ('full_plus_SH3',(2,3,4),(14,16)),
]

def build(P,layers,steps,a=12,b=16,dmax=10):
    M=rd.LP();rect=[]
    for D in layers:
        for V in range(b+1):rect.append((D,V,M.var(('BCrect',D,V),(0,None),1.0)))
    diag=[(K,M.var(('J',K),(0,None),1.0)) for K in steps]
    sh=M.var(('SH',S),(0,None),1.0)
    def add2d(row,d,h,factor,sign):
        v=b-h
        for D,V,w in rect:
            if d>=D and v>=V:row[w]=row.get(w,0)+sign*factor
        for K,w in diag:
            if d+v>=K:row[w]=row.get(w,0)+sign*factor
    for pi,pf in enumerate(P):
        lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01)
        mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01)
        taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)}
        sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    row={e:1,lam:-R,cc:-x};add2d(row,R+s,R+x,x,-1)
                    if s>=S:row[sh]=row.get(sh,0)-x
                    M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg
            qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for j in range(1,a+1):
                        tv=rd.tterm(rho,q,pp,j)
                        if tv:row[taus[j]]=row.get(taus[j],0)-tv
                    add2d(row,rho+q-1,q+pp,q,1)
                    if rho>=S:row[sh]=row.get(sh,0)+q
                    M.le(row,0)
        row={lam:sum(pf['rho'])}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M,rect,diag,sh

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,2);P0=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P0)!=902:raise SystemExit(f'expected 902 profiles, got {len(P0)}')
    P=[P0[i] for i in BAD];results=[]
    for name,layers,steps in CASES:
        st=time.time();M,rect,diag,sh=build(P,layers,steps);res=M.solve()
        r={'case':name,'layers':list(layers),'diagonal_K':list(steps),'SH_threshold':S,'success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st}
        if res.success:
            ar=[{'D':D,'V':V,'weight':float(res.x[w])} for D,V,w in rect if res.x[w]>1e-8]
            ad=[{'K':K,'c':16-K,'weight':float(res.x[w])} for K,w in diag if res.x[w]>1e-8]
            r.update(objective=float(res.fun),SH_weight=float(res.x[sh]),active_rectangles=ar,active_diagonals=ad,active_generator_count=len(ar)+len(ad)+(1 if res.x[sh]>1e-8 else 0))
        results.append(r);print(json.dumps(r,sort_keys=True),flush=True)
    out={'schema':'n29-t2-bad107-SH3-replacement-scan-v1','bad_profile_count':len(P),'bad_indices':BAD,'SH_threshold':S,'floating_point_reconnaissance_only':True,'results':results,'prior_2d_irreducibility_run':34500408371,'interpretation':'Tests whether the single universally valid first-coordinate threshold s>=3/rho>=3 can replace any one of D2,D3,D4,J0,J2 on bad107. Positive cases require full-902 testing and exactification. Negative cases strengthen only this restricted replacement statement.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
