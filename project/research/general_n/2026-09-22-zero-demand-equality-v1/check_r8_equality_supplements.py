#!/usr/bin/env python3
"""Enumerate source populations and apply necessary supplement forcing at r=8 equality."""
import itertools,json

cores=json.load(open('R8_EQUALITY_CORE_SCREEN.json'))
feas=json.load(open('R8_EQUALITY_SOURCE_FEASIBILITY.json'));out={}
for partition,entry in cores.items():
    R=tuple(int(x.strip()) for x in partition.strip('()').split(',') if x.strip());k=len(R)
    ok={x['orbit'] for x in feas.get(partition,{}).get('rows',[]) if x['source_feasible']}
    for q,orbit in enumerate(entry['orbit_representatives'],1):
        if q not in ok:continue
        rep=orbit['representative'];neighbors=[set() for _ in R]
        for i,j in rep['edges']:neighbors[i].add(j);neighbors[j].add(i)
        P=set(rep['P']);need=tuple(rep['selected_lower_bounds']);patterns=[];free=[]
        for state in itertools.product(range(3),repeat=k):
            L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
            if any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L):continue
            if not Z:assert not (L&P);free.append(state);continue
            patterns.append((tuple(int(i in Z) for i in range(k)),tuple(int(i in L) for i in range(k)),state))
        tested=[0];survivors=[]
        def forced(su,u,sw,w):
            Lu={i for i,s in enumerate(su) if s==1};Lw={i for i,s in enumerate(sw) if s==1}
            return {(u,i) for i in Lu if sw[i]==0}|{(w,j) for j in Lw if su[j]==0}
        def test(pop):
            for u,su in enumerate(pop):
                for i,s in enumerate(su):
                    if s!=1:continue
                    if any(w!=u and forced(su,u,sw,w)=={(u,i)} for w,sw in enumerate(pop)):continue
                    if any(forced(su,u,sw,('free',z))=={(u,i)} for z,sw in enumerate(free)):continue
                    return False
            return True
        def search(start,rem,x,chosen):
            if not any(rem):
                if all(x[i]>=need[i] for i in range(k)):
                    tested[0]+=1
                    if test(chosen) and len(survivors)<3:survivors.append(tuple(chosen))
                return
            for a in range(start,len(patterns)):
                z,l,state=patterns[a]
                if all(z[i]<=rem[i] for i in range(k)):
                    search(a,tuple(rem[i]-z[i] for i in range(k)),tuple(x[i]+l[i] for i in range(k)),chosen+[state])
        search(0,R,tuple(0 for _ in R),[])
        out[f'{partition}/orbit_{q}']={'source_multisets_tested':tested[0],'residual_free_types_available':len(free),
          'supplement_feasible':len(survivors),'first_survivors':survivors,
          'scope':'Necessary singleton supplement forcing; capped survivor storage at 3.'}
print(json.dumps(out,indent=2))
