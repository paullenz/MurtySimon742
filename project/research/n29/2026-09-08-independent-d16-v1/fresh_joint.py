#!/usr/bin/env python3
"""Independent pure-Python N=29 Delta=16 joint-state verifier.
No imports from the inherited Murty-Simon verifier. Standard library only.
"""
from collections import defaultdict

def column_filter(dom,r,slack):
    a=len(dom); pref=[{(0,0)}]
    for opts in dom:
        pref.append({(x+R,y+z) for x,y in pref[-1] for _,R,z in opts if x+R<=r and y+z<=slack})
    if (r,slack) not in pref[-1]: return None
    suff=[None]*(a+1);suff[a]={(0,0)}
    for i in range(a-1,-1,-1):
        suff[i]={(x+R,y+z) for x,y in suff[i+1] for _,R,z in dom[i] if x+R<=r and y+z<=slack}
    out=[]
    for i,opts in enumerate(dom):
        keep=[]
        for op in opts:
            _,R,z=op
            if any((r-x-R,slack-y-z) in suff[i+1] for x,y in pref[i]): keep.append(op)
        if not keep:return None
        out.append(tuple(keep))
    return out

def matching(adj,mandatory,q):
    M={}
    def aug(i,seen):
        mask=adj[i]
        while mask:
            bit=mask&-mask; w=bit.bit_length()-1; mask-=bit
            if w in seen:continue
            seen.add(w)
            if w not in M or aug(M[w],seen):M[w]=i;return True
        return False
    for i in mandatory:
        if not aug(i,set()):return False
    if len(M)>=q:return True
    mand=set(mandatory)
    for i in sorted((i for i in range(len(adj)) if i not in mand),key=lambda x:adj[x].bit_count()):
        if aug(i,set()) and len(M)>=q:return True
    return len(M)>=q

class Dinic:
    def __init__(self,n):self.g=[[] for _ in range(n)]
    def add(self,u,v,c):self.g[u].append([v,c,len(self.g[v])]);self.g[v].append([u,0,len(self.g[u])-1])
    def flow(self,s,t):
        ans=0
        while True:
            lev=[-1]*len(self.g);lev[s]=0;q=[s]
            for u in q:
                for v,c,_ in self.g[u]:
                    if c and lev[v]<0:lev[v]=lev[u]+1;q.append(v)
            if lev[t]<0:return ans
            it=[0]*len(self.g)
            def dfs(u,f):
                if u==t:return f
                while it[u]<len(self.g[u]):
                    e=self.g[u][it[u]];v,c,rev=e
                    if c and lev[v]==lev[u]+1:
                        z=dfs(v,min(f,c))
                        if z:e[1]-=z;self.g[v][rev][1]+=z;return z
                    it[u]+=1
                return 0
            while True:
                z=dfs(s,10**9)
                if not z:break
                ans+=z

def source_hall(s,E,c):
    a=len(s);b=len(c);T=1+a+b;D=Dinic(T+1)
    for i,x in enumerate(s):
        D.add(0,1+i,x)
        for u in range(b):
            if E[i]>>u&1:D.add(1+i,1+a+u,1)
    for u,x in enumerate(c):D.add(1+a+u,T,x)
    return D.flow(0,T)>=sum(s)

def pair_hall(s,P):
    a=len(s)
    for mask in range(1,1<<a):
        q=0;U=0
        for i in range(a):
            if mask>>i&1:q+=s[i];U|=P[i]
        if q>U.bit_count():return mask
    return None

def allowed(i,d,s,rho,c,forced,u,q=None):
    if s[i]>rho[u]:return 0
    f=sum(x>>u&1 for x in forced); need=max(1,f,d-rho[u]+1)
    q=need if q is None else q
    if q<need or q>c[u]:return 0
    out=0
    for w in range(len(rho)):
        if w!=u and not(forced[i]>>w&1) and d<=rho[u]+rho[w] and rho[w]+c[w]>=q-1:out|=1<<w
    return out

def row_feasible(s,rho,t,dom,c,forced,u,q,pin=-1,choice=-1):
    a=len(s);b=len(rho);r=sum(rho);sl=sum(s)-r-2*t;rr=rho[u];missing=a-rr-q
    if missing<0:return False
    nr=rr+1;nz=sl+1;size=(q+1)*nr*nz;limit=(1<<(r+1))-1
    def at(x,y,z):return (x*nr+y)*nz+z
    dp=[0]*size;dp[0]=1
    for i in range(a):
        nx=[0]*size; mandated=forced[i]>>u&1
        for oi,(d,R,z) in enumerate(dom[i]):
            if i==pin and oi!=choice:continue
            if R>r or z>sl:continue
            supp=any(w!=u and not(forced[i]>>w&1) and rho[w]+c[w]>=q-1 and rr+rho[w]>=d for w in range(b))
            S=q>0 and s[i]<=rr and d<=rr+q-1 and supp and R<=b-max(1,s[i])
            Re=not mandated and R>=1; N=not mandated and d<=a-q-1 and R<=b-s[i]-1
            for x in range(min(q,i)+1):
                for y in range(min(rr,i-x)+1):
                    gone=i-x-y
                    if gone>missing:continue
                    for z0 in range(sl-z+1):
                        v=dp[at(x,y,z0)]
                        if not v:continue
                        v=(v<<R)&limit
                        if not v:continue
                        zz=z0+z
                        if S and x<q:n=at(x+1,y,zz);nx[n]|=v
                        if Re and y<rr:n=at(x,y+1,zz);nx[n]|=v
                        if N and gone<missing:n=at(x,y,zz);nx[n]|=v
        dp=nx
        if not any(dp):return False
    return bool(dp[at(q,rr,sl)]>>r&1)

def row_refine(s,rho,t,dom,c,forced):
    a=len(s);b=len(rho);reps=[];masks=[0]*b
    for u in range(b):
        twin=next((v for v in reps if rho[v]==rho[u] and c[v]==c[u] and all((f>>u&1)==(f>>v&1) for f in forced)),None)
        if twin is not None:masks[u]=masks[twin];continue
        reps.append(u)
        for q in range(c[u]+1):
            if row_feasible(s,rho,t,dom,c,forced,u,q):masks[u]|=1<<q
    flags=[[True]*len(x) for x in dom]
    if any(x==0 for x in masks):return masks,flags
    lreps=[]
    for i in range(a):
        twin=next((j for j in lreps if s[i]==s[j] and forced[i]==forced[j] and tuple(dom[i])==tuple(dom[j])),None)
        if twin is not None:flags[i]=flags[twin].copy();continue
        lreps.append(i)
        for oi in range(len(dom[i])):
            for u in reps:
                if not any((masks[u]>>q&1) and row_feasible(s,rho,t,dom,c,forced,u,q,i,oi) for q in range(c[u]+1)):
                    flags[i][oi]=False;break
    return masks,flags

def propagate(s,rho,t,dmax=10):
    a=len(s);b=len(rho);r=sum(rho);S=sum(s);sl=S-r-2*t
    if sl<0:return {'kind':'negative_slack'}
    dom=[]
    for x in s:
        dom.append(tuple((d,d-x,0) for d in range(x,dmax+1)) if x else tuple((d,d+z,z) for d in range(dmax+1) for z in range(min(sl,b-d)+1)))
    c=tuple(min(a-x,b-1) for x in rho);forced=[0]*a;rounds=0
    while True:
        rounds+=1;old=(tuple(dom),c,tuple(forced));f=[sum(x>>u&1 for x in forced) for u in range(b)]
        if any(f[u]>c[u] for u in range(b)):return {'kind':'forced_cap','round':rounds}
        nd=[]
        for i,opts in enumerate(dom):
            keep=[]
            for op in opts:
                d,R,_=op;E=sum(1<<u for u in range(b) if allowed(i,d,s,rho,c,forced,u))
                if E.bit_count()>=s[i] and forced[i]&E==forced[i] and R<=b-forced[i].bit_count():keep.append(op)
            if not keep:return {'kind':'label_domain','label':i,'round':rounds}
            nd.append(tuple(keep))
        dom=column_filter(nd,r,sl)
        if dom is None:return {'kind':'column_sum','round':rounds}
        E=[0]*a
        for i,opts in enumerate(dom):
            for d in {x[0] for x in opts}:
                E[i]|=sum(1<<u for u in range(b) if allowed(i,d,s,rho,c,forced,u))
            if s[i] and E[i].bit_count()==s[i]:forced[i]|=E[i]
        f=[sum(x>>u&1 for x in forced) for u in range(b)];nc=[]
        for u in range(b):
            mandatory=[i for i in range(a) if forced[i]>>u&1];cap=None
            for q in range(c[u],f[u]-1,-1):
                if q==0:cap=0;break
                adj=[allowed(i,min(x[0] for x in dom[i]),s,rho,c,forced,u,q) for i in range(a)]
                if matching(adj,mandatory,q):cap=q;break
            if cap is None:return {'kind':'source_matching','source':u,'round':rounds}
            nc.append(cap)
        c=tuple(nc)
        if sum(c)<S:return {'kind':'total_source','round':rounds}
        masks,flags=row_refine(s,rho,t,dom,c,forced)
        if not all(masks):return {'kind':'joint_empty_row','round':rounds}
        c=tuple(x.bit_length()-1 for x in masks)
        if sum(c)<S:return {'kind':'joint_total_source','round':rounds}
        dom=[tuple(op for op,k in zip(opts,flags[i]) if k) for i,opts in enumerate(dom)]
        if not all(dom):return {'kind':'joint_empty_column','round':rounds}
        if (tuple(dom),c,tuple(forced))==old:break
        if rounds>100:raise RuntimeError('nonconvergence')
    E=[0]*a;P=[];pair={};k=0
    for u in range(b):
        for w in range(u+1,b):pair[u,w]=k;k+=1
    for i in range(a):
        d=min(x[0] for x in dom[i]);pm=0
        for u in range(b):
            W=allowed(i,d,s,rho,c,forced,u)
            if W:E[i]|=1<<u
            while W:
                bit=W&-W;w=bit.bit_length()-1;W-=bit;pm|=1<<pair[min(u,w),max(u,w)]
        P.append(pm)
    if not source_hall(s,E,c):return {'kind':'source_hall','round':rounds}
    bad=pair_hall(s,P)
    if bad is not None:return {'kind':'pair_hall','mask':bad,'round':rounds}
    return {'kind':'survivor','round':rounds,'domains':dom,'c':c,'forced':forced}
