import itertools, json, hashlib
D=5
verts=range(D)
edges=list(itertools.combinations(verts,2))

def B(mask,S):
    S=set(S); adj=[set() for _ in verts]; Q=[]
    for b,(i,j) in enumerate(edges):
        if mask>>b&1:
            adj[i].add(j);adj[j].add(i);Q.append((i,j))
    out=set()
    for i,j in Q:
        for t,s in ((i,j),(j,i)):
            if t not in S and s in S and (adj[t]&S)=={s}:
                out.add((min(i,j),max(i,j)))
    return out

def mincost(mask):
    Q=[e for b,e in enumerate(edges) if mask>>b&1]
    if not Q: return 0
    idx={e:i for i,e in enumerate(Q)}; full=(1<<len(Q))-1
    fam=[]
    for r in range(1,6):
        cost=0 if r==5 else 4-r
        for S in itertools.combinations(verts,r):
            bm=0
            for e in B(mask,S): bm |= 1<<idx[e]
            if bm: fam.append((bm,cost,S))
    INF=99; dp=[INF]*(1<<len(Q));dp[0]=0
    for s in range(1<<len(Q)):
        if dp[s]>=INF: continue
        for bm,c,_ in fam:
            ns=s|bm
            if dp[s]+c<dp[ns]:dp[ns]=dp[s]+c
    return dp[full]

rows=[]; hist={}; types={}; best=99
for mask in range(1<<10):
    mu=10-mask.bit_count(); c=mincost(mask); total=2*mu+c
    deg=[0]*5
    for b,(i,j) in enumerate(edges):
        if mask>>b&1:deg[i]+=1;deg[j]+=1
    rows.append((mask,mu,c,total,*sorted(deg)))
    hist.setdefault(mu,{}); hist[mu][c]=hist[mu].get(c,0)+1
    best=min(best,total)
for row in rows:
    if row[3]==best:
        key=(row[1],row[2],tuple(row[4:]));types[str(key)]=types.get(str(key),0)+1
text=''.join(' '.join(map(str,r))+'\n' for r in rows).encode()
summary={'status':'PASS_EXHAUSTIVE_D5_SUPPORT_COVER','tight_graphs':1024,'minimum_total_defect':best,'histogram_by_mu_and_cover_cost':hist,'minimum_types':types,'sha256':hashlib.sha256(text).hexdigest()}
print(json.dumps(summary,indent=2,sort_keys=True))
