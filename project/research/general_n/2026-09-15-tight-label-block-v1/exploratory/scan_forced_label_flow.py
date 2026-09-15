#!/usr/bin/env python3
"""Necessary directed-pair/receiver flow with forced selected labels."""
from collections import deque
from pathlib import Path
import json

class Flow:
    def __init__(self): self.g=[]
    def node(self): self.g.append([]);return len(self.g)-1
    def edge(self,u,v,c):
        a=[v,c,len(self.g[v])];b=[u,0,len(self.g[u])]
        self.g[u].append(a);self.g[v].append(b)
    def run(self,s,t):
        ans=0
        while True:
            level=[-1]*len(self.g);level[s]=0;q=deque([s])
            while q:
                u=q.popleft()
                for v,c,_ in self.g[u]:
                    if c and level[v]<0:level[v]=level[u]+1;q.append(v)
            if level[t]<0:break
            pos=[0]*len(self.g)
            def dfs(u,f):
                if u==t:return f
                while pos[u]<len(self.g[u]):
                    e=self.g[u][pos[u]];v,c,j=e
                    if c and level[v]==level[u]+1:
                        sent=dfs(v,min(c,f))
                        if sent:e[1]-=sent;self.g[v][j][1]+=sent;return sent
                    pos[u]+=1
                return 0
            while True:
                f=dfs(s,10**9)
                if not f:break
                ans+=f
        seen={s};todo=[s]
        for u in todo:
            for v,c,_ in self.g[u]:
                if c and v not in seen:seen.add(v);todo.append(v)
        return ans,seen

def analyze(p,use_tight_columns=True):
    s,q,rho,a,b=p['s'],p['q'],p['rho'],p['a'],p['b']
    eligible=[{i for i,d in enumerate(s) if d<=r} for r in rho]
    tight={i for i,d in enumerate(s) if sum(r>=d for r in rho)==d}
    forced=[(set(eligible[v]) if q[v]==len(eligible[v]) else set()) | (eligible[v]&tight if use_tight_columns else set()) for v in range(b)]
    assert all(len(forced[v])<=q[v] for v in range(b))
    f=Flow();src=f.node();sink=f.node();receivers=[f.node() for _ in range(b)]
    for v in range(b):f.edge(receivers[v],sink,max(0,rho[v]+b-a-1))
    slots=[];pairs={}
    for u in range(b):
        for i in sorted(forced[u]):
            x=f.node();f.edge(src,x,1);slots.append((x,u,i,1))
        count=q[u]-len(forced[u])
        if count:
            x=f.node();f.edge(src,x,count);slots.append((x,u,None,count))
        for v in range(b):
            if u==v or not(q[u]<=q[v]+rho[v]+1 and q[v]<=q[u]+rho[u]):continue
            x=f.node();pairs[u,v]=x;f.edge(x,receivers[v],1)
    for x,u,i,count in slots:
        for v in range(b):
            if (u,v) not in pairs:continue
            if i is not None:
                if i in forced[v]:continue
                # Known selected labels must fit both required neighbourhood containments.
                if len((forced[u]-{i})|forced[v])>q[v]+rho[v]:continue
                if len(forced[u]|forced[v])>q[u]+rho[u]:continue
                if len(forced[v]-eligible[u])>rho[u]:continue
                if len((forced[u]-{i})-eligible[v])>rho[v]:continue
            f.edge(x,pairs[u,v],count)
    value,cut=f.run(src,sink);need=sum(q)
    return {'flow':value,'demand':need,'rejected':value<need,'forced_labels':[sorted(x) for x in forced],'tight_labels':sorted(tight),'cut_slots':[{'source':u,'label':i,'multiplicity':count} for x,u,i,count in slots if x in cut],'cut_receivers':[v for v,x in enumerate(receivers) if x in cut]}

def main():
    root=Path(__file__).parent;ps=json.loads((root/'RESCUE_PROFILES.json').read_text())
    rows=[{'layer':p['layer'],'state_id':p['state_id'],'saturation_only':analyze(p,False),'with_tight_columns':analyze(p,True)} for p in ps]
    result={'scope':'124 preserved fixed-q witnesses; not whole-state exclusions','profiles':len(rows),'saturation_flow_rejected':[r['state_id'] for r in rows if r['saturation_only']['rejected']],'tight_column_flow_rejected':[r['state_id'] for r in rows if r['with_tight_columns']['rejected']],'rows':rows}
    (root/'FORCED_LABEL_FLOW_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
