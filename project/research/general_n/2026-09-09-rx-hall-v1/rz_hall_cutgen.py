#!/usr/bin/env python3
"""Project the stripped Z transport exactly by iterative Hall-cut separation.

Builds the W/L master with exact residual budget and no Z variables.  The total
source/label incidence equality H0 is explicit.  A floating feasible master
point is separated by a max-flow/min-cut calculation on the ABC compatibility
graph.  Each violated Hall cut has integer coefficients and is appended to the
master.  Final infeasibility is accepted only through the existing exact
integer-Farkas checker.

Research diagnostic only; graph-to-model validity is inherited from the
candidate selected/residual framework.
"""
from collections import Counter,defaultdict,deque
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json,math
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('rx_hall_exact',HERE/'rx_hall_exact.py'); ex=module_from_spec(spec); spec.loader.exec_module(ex); rx=ex.rx

def groups(v): return sorted(Counter(v).items())

class Dinic:
    def __init__(self,n): self.n=n; self.g=[[] for _ in range(n)]
    def add(self,u,v,c):
        a=[v,float(c),None]; b=[u,0.0,a]; a[2]=b; self.g[u].append(a); self.g[v].append(b)
    def flow(self,s,t):
        ans=0.0
        while True:
            lev=[-1]*self.n; lev[s]=0; q=deque([s])
            while q:
                u=q.popleft()
                for e in self.g[u]:
                    if e[1]>1e-10 and lev[e[0]]<0: lev[e[0]]=lev[u]+1; q.append(e[0])
            if lev[t]<0: break
            it=[0]*self.n
            def dfs(u,f):
                if u==t: return f
                while it[u]<len(self.g[u]):
                    e=self.g[u][it[u]]
                    if e[1]>1e-10 and lev[e[0]]==lev[u]+1:
                        z=dfs(e[0],min(f,e[1]))
                        if z>1e-10: e[1]-=z; e[2][1]+=z; return z
                    it[u]+=1
                return 0.0
            while True:
                z=dfs(s,1e100)
                if z<=1e-10: break
                ans+=z
        seen=[False]*self.n; seen[s]=True; q=deque([s])
        while q:
            u=q.popleft()
            for e in self.g[u]:
                if e[1]>1e-9 and not seen[e[0]]: seen[e[0]]=True; q.append(e[0])
        return ans,seen

def build_master(a,b,dmax,s,rho):
    SG=groups(rho); LG=groups(s); r=sum(rho); m=rx.LP(); sources=[]; labels=[]; ST=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        qmax=min(a-rh,sum(si<=rh for si in s)); norm={}
        for q in range(qmax+1):
            for p in range(min(rh+b-a-1,b-1-q)+1):
                w=m.var(('W',k,q,p)); ST[k].append((q,p,w)); norm[w]=1; sources.append({'k':k,'rho':rh,'n':nk,'q':q,'p':p,'var':w})
        m.equal(norm,1)
    m.equal({w:nk*(q-p) for k,(rh,nk) in enumerate(SG) for q,p,w in ST[k]},0)
    for th in range(1,a+1):
        row={}
        for k,(rh,nk) in enumerate(SG):
            for q,p,w in ST[k]:
                c=(nk*q if q>=th+1 else 0)-(nk*p if rh+q>=th else 0)
                if c: row[w]=c
        m.le(row,0)
    LT=defaultdict(list)
    for g,(sg,ng) in enumerate(LG):
        norm={}
        for R in range(dmax-sg+1):
            for x in range(sg,b-R+1):
                z=m.var(('L',g,R,x)); LT[g].append((R,x,z)); norm[z]=1; labels.append({'g':g,'s':sg,'n':ng,'R':R,'x':x,'var':z})
        m.equal(norm,1)
    m.equal({z:ng*R for g,(sg,ng) in enumerate(LG) for R,x,z in LT[g]},r)
    # H0: total source incidence mass equals total label incidence mass.
    h0={}
    for u in sources:
        if u['q']: h0[u['var']]=h0.get(u['var'],0)+u['n']*u['q']
    for v in labels:
        if v['x']: h0[v['var']]=h0.get(v['var'],0)-v['n']*v['x']
    m.equal(h0,0)
    return m,sources,labels

def compat(u,v):
    return v['s']<=u['rho'] and v['R']+v['s']<=u['rho']+u['q']-1 and v['R']+v['x']>=u['q']+u['p']

def separate(sol,sources,labels):
    # S -> label (demand), label -> compatible source (INF), source -> T (capacity).
    activeL=[v for v in labels if v['n']*v['x']*sol[v['var']]>1e-9]
    activeS=[u for u in sources if u['n']*u['q']*sol[u['var']]>1e-9]
    nl,ns=len(activeL),len(activeS); S=0; lo=1; so=lo+nl; T=so+ns; D=Dinic(T+1)
    total=0.0
    for i,v in enumerate(activeL):
        d=v['n']*v['x']*sol[v['var']]; total+=d; D.add(S,lo+i,d)
    for j,u in enumerate(activeS): D.add(so+j,T,u['n']*u['q']*sol[u['var']])
    INF=max(1.0,total+1.0)
    for i,v in enumerate(activeL):
        for j,u in enumerate(activeS):
            if compat(u,v): D.add(lo+i,so+j,INF)
    val,seen=D.flow(S,T)
    if total-val<=1e-7: return None
    U=[v for i,v in enumerate(activeL) if seen[lo+i]]
    # Exact Hall row uses all source states compatible with at least one v in U,
    # not merely source states active at this numerical solution.
    N=[u for u in sources if u['q'] and any(compat(u,v) for v in U)]
    row={}
    for v in U: row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for u in N: row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    lhs=sum(c*sol[j] for j,c in row.items())
    if lhs<=1e-7: raise RuntimeError(f'mincut failed to yield violated exact Hall row: {lhs}')
    signature=(tuple(sorted((v['g'],v['R'],v['x']) for v in U)),tuple(sorted((u['k'],u['q'],u['p']) for u in N)))
    return row,lhs,signature,U,N

def load(dp,rp,t):
    D=json.loads(Path(dp).read_text()); out=[]
    for line in Path(rp).read_text().splitlines():
        if not line.strip(): continue
        z=list(map(int,line.split())); did,total,rho=z[0],z[1],z[2:]; s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t: out.append((did,total,s,rho))
    return out

def main():
    p=argparse.ArgumentParser(); p.add_argument('--demands-json',type=Path,required=True); p.add_argument('--rows',type=Path,required=True); p.add_argument('--a',type=int,required=True); p.add_argument('--b',type=int,required=True); p.add_argument('--dmax',type=int,required=True); p.add_argument('--t',type=int,required=True); p.add_argument('--output',type=Path,required=True); p.add_argument('--max-cuts',type=int,default=200); a=p.parse_args()
    records=[]
    for hp,(did,total,s,rho) in enumerate(load(a.demands_json,a.rows,a.t)):
        m,sources,labels=build_master(a.a,a.b,a.dmax,s,rho); cuts=[]; sigs=set(); numerical_status=None
        for it in range(a.max_cuts+1):
            res=m.solve(); numerical_status=res.status
            if not res.success: break
            sep=separate(res.x,sources,labels)
            if sep is None: break
            row,lhs,sig,U,N=sep
            if sig in sigs: raise RuntimeError('duplicate Hall cut at feasible point')
            sigs.add(sig); m.le(row,0)
            cuts.append({'iteration':it,'violation':lhs,'label_states':[{'g':v['g'],'s':v['s'],'R':v['R'],'x':v['x']} for v in U],'source_states':[{'k':u['k'],'rho':u['rho'],'q':u['q'],'p':u['p']} for u in N]})
        # Only exact certificate establishes rejection.
        ex.add_unit_density_bounds(m); cert=ex.exact_certificate(m)
        records.append({'hard_position':hp,'demand_id':did,'s':s,'rho':rho,'hall_cuts_added':len(cuts),'cuts':cuts,'numerical_status_before_exact':numerical_status,'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']})
    out={'schema':'rz-hall-cut-generation-v1','scope':{'a':a.a,'b':a.b,'dmax':a.dmax,'t':a.t},'hard_rows':len(records),'exact_rejections':sum(r['rejected_exactly'] for r in records),'survivors':sum(not r['rejected_exactly'] for r in records),'cut_counts':[r['hall_cuts_added'] for r in records],'records':records,'interpretation':'Z-free exact Hall projection. Numerical max-flow/LP proposes integer Hall rows; final rejection requires independently checked integer Farkas certificate.'}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({'exact_rejections':out['exact_rejections'],'survivors':out['survivors'],'cut_counts':out['cut_counts']},indent=2))
if __name__=='__main__': main()
