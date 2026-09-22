#!/usr/bin/env python3
"""Independent group-action/count audit of the saved r=9 support-eight cores."""
import hashlib,itertools,json
R=(2,1,1,1,1,1,1,1);pairs=list(itertools.combinations(range(8),2))
idx={e:q for q,e in enumerate(pairs)}
perms=[]
for q in itertools.permutations(range(1,8)):
    perms.append((0,)+q)
def edge_action(p):
    a=[]
    for i,j in pairs:
        x,y=sorted((p[i],p[j]));a.append(idx[(x,y)])
    return a
def cycles(action):
    seen=set();c=0
    for x in range(len(action)):
        if x not in seen:
            c+=1
            while x not in seen:seen.add(x);x=action[x]
    return c
actions=[edge_action(p) for p in perms]
coloured_burnside=sum(1<<cycles(a) for a in actions)//len(actions)
unit_actions=[[x-7 for x in a[7:]] for a in actions] # pairs order: 7 root edges, then 21 unit edges
unit_burnside=sum(1<<cycles(a) for a in unit_actions)//len(actions)
def image(mask,a):
    out=0
    for q in range(28):
        if mask>>q&1:out|=1<<a[q]
    return out
def check(mask):
    deg=[0]*8;neigh=[set() for _ in R];edges=[]
    for q,(i,j) in enumerate(pairs):
        if mask>>q&1:edges.append((i,j));deg[i]+=1;deg[j]+=1;neigh[i].add(j);neigh[j].add(i)
    P={i for i in range(8) if deg[i]>R[i]};N=set(range(8))-P
    assert all((deg[i]-R[i])**2<=sum(R[j] for j in neigh[i]) for i in P)
    eP=sum(i in P and j in P for i,j in edges);eN=sum(i in N and j in N for i,j in edges)
    slack=sum(i>0 and deg[i]==0 for i in N)
    t=eP-eN-sum(R[i] for i in P)-slack
    assert t>0
    return t,tuple(deg),tuple(sorted(P))
rows=[list(map(int,line.split())) for line in open("r9_support8_masks.txt")]
masks=[r[0] for r in rows]
assert len(masks)==69==len(set(masks))
canon=[min(image(m,a) for a in actions) for m in masks]
assert len(set(canon))==69
checks=[check(m) for m in masks]
assert all(t==row[1] for (t,d,p),row in zip(checks,rows))
payload={'unit_graph_orbits_burnside':unit_burnside,
         'rooted_coloured_graph_orbits_burnside':coloured_burnside,
         'saved_strict_orbits':len(masks),'pairwise_colour_inequivalent':len(set(canon)),
         't_upper_counts':{str(t):sum(x[0]==t for x in checks) for t in sorted(set(x[0] for x in checks))},
         'mask_sha256':hashlib.sha256((' '.join(map(str,sorted(masks)))+'\n').encode()).hexdigest(),
         'scope':'Independent Burnside/group-action and saved-mask invariant audit; source DP audited separately.'}
print(json.dumps(payload,indent=2))
#!/usr/bin/env python3
"""Independent MILP replay of physical-source infeasibility on 69 r=9 cores."""
import itertools,json,numpy as np
from scipy.optimize import milp,LinearConstraint,Bounds
from scipy.sparse import csc_matrix
R=np.array((2,1,1,1,1,1,1,1),dtype=float);k=8
pairs=list(itertools.combinations(range(k),2));results=[]
for line in open("r9_support8_masks.txt"):
    mask=int(line.split()[0]);neigh=[set() for _ in range(k)];deg=[0]*k
    for q,(i,j) in enumerate(pairs):
        if mask>>q&1:neigh[i].add(j);neigh[j].add(i);deg[i]+=1;deg[j]+=1
    need=np.array([max(0,deg[i]-int(R[i])) for i in range(k)],dtype=float)
    cols=[]
    for state in itertools.product(range(3),repeat=k):
        L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
        if not Z:continue
        if any(not neigh[i]<=L|Z or len(neigh[i]&L)>R[i] for i in L):continue
        cols.append([int(i in Z) for i in range(k)]+[int(i in L) for i in range(k)])
    A=np.array(cols,dtype=float).T
    lc=np.concatenate((R,need));uc=np.concatenate((R,np.full(k,np.inf)))
    ans=milp(np.zeros(len(cols)),integrality=np.ones(len(cols)),
             bounds=Bounds(np.zeros(len(cols)),np.full(len(cols),np.inf)),
             constraints=LinearConstraint(csc_matrix(A),lc,uc),
             options={'time_limit':30})
    results.append({'mask':mask,'patterns':len(cols),'status':int(ans.status),
                    'feasible':bool(ans.success)})
assert all(not r['feasible'] and r['status']==2 for r in results)
print(json.dumps({'orbits_tested':len(results),'milp_feasible':0,
 'all_status_infeasible':all(r['status']==2 for r in results),
 'pattern_range':[min(r['patterns'] for r in results),max(r['patterns'] for r in results)],
 'solver':'scipy.optimize.milp / HiGHS','scope':'Independent integer-linear feasibility replay.'},indent=2))
