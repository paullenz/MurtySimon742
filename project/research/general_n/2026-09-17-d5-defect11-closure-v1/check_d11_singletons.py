from pathlib import Path
import itertools, json, hashlib
verts=range(5)
edges=list(itertools.combinations(verts,2))
def threat(mask,S):
    S=set(S); adj=[set() for _ in verts]; Q=[]
    for b,(i,j) in enumerate(edges):
        if mask>>b&1:
            adj[i].add(j); adj[j].add(i); Q.append((i,j))
    out=set()
    for i,j in Q:
        for t,s in ((i,j),(j,i)):
            if t not in S and s in S and (adj[t]&S)=={s}:
                out.add((min(i,j),max(i,j))); break
    return out
def solve(mask):
    Q=[e for b,e in enumerate(edges) if mask>>b&1]
    if not Q: return (0,0)
    idx={e:i for i,e in enumerate(Q)}; full=(1<<len(Q))-1
    fam=[]
    for r in range(1,6):
        c=0 if r==5 else 4-r; sing=1 if r==1 else 0
        for S in itertools.combinations(verts,r):
            bm=0
            for e in threat(mask,S): bm |= 1<<idx[e]
            if bm: fam.append((bm,c,sing))
    INF=(99,99); dp=[INF]*(1<<len(Q)); dp[0]=(0,0)
    for st in range(1<<len(Q)):
        if dp[st]==INF: continue
        for bm,c,sing in fam:
            ns=st|bm; cand=(dp[st][0]+c,dp[st][1]+sing)
            if cand<dp[ns]: dp[ns]=cand
    return dp[full]
rows=[]; types={}
for mask in range(1<<10):
    tau,mins=solve(mask); mu=10-mask.bit_count(); total=2*mu+tau
    deg=[0]*5
    for b,(i,j) in enumerate(edges):
        if mask>>b&1: deg[i]+=1; deg[j]+=1
    row=(mask,mu,tau,mins,total,*sorted(deg)); rows.append(row)
    if total==11:
        k=str((mu,tau,mins,tuple(sorted(deg))))
        types[k]=types.get(k,0)+1
stream=''.join(' '.join(map(str,r))+'\n' for r in rows).encode()
summary={'status':'PASS_D11_OPTIMAL_COVER_SINGLETON_CLASSIFICATION','tight_graphs':1024,'d11_graphs':sum(r[4]==11 for r in rows),'minimum_types':types,'all_d11_require_singleton':all(r[3]>=1 for r in rows if r[4]==11),'row_sha256':hashlib.sha256(stream).hexdigest()}
Path(__file__).with_name('PYTHON_ROWS.txt').write_bytes(stream)
Path(__file__).with_name('CHECK_SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,indent=2,sort_keys=True))
