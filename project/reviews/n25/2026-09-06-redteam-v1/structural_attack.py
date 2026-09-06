#!/usr/bin/env python3
"""Falsification tests from actual graphs; no imports from the proof verifiers.

Exhaustive labelled graphs through n=6, then seeded generated examples through
n=25. Small representatives use every base vertex and every selected-edge
assignment; larger examples use every minimum-degree base and sampled choices.
Passing is finite evidence, never a proof of the universal lemmas.
"""
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import math
import random

OUT=Path(__file__).resolve().parent
RNG=random.Random(250906)
COUNTS=Counter()
PROFILE=Counter()
NEGATIVE={}
CURRENT={}


def ensure(ok,label,details=None):
    if not ok:
        failure=dict(status='FAIL',label=label,details=details,context=CURRENT)
        (OUT/'structural_failure.json').write_text(json.dumps(failure,indent=2)+'\n')
        raise AssertionError(failure)
    COUNTS[label]+=1


def vertices(mask):
    return [i for i in range(mask.bit_length()) if mask>>i&1]


def graph(n,edges):
    adj=[0]*n
    for x,y in edges:adj[x]|=1<<y;adj[y]|=1<<x
    return tuple(adj)


def edge_list(adj):
    return [(x,y) for x,y in combinations(range(len(adj)),2) if adj[x]>>y&1]


def diameter_at_most_two(adj):
    return all(adj[x]>>y&1 or adj[x]&adj[y] for x,y in combinations(range(len(adj)),2))


def critical(adj):
    n=len(adj)
    if len(edge_list(adj))==n*(n-1)//2 or not diameter_at_most_two(adj):return False
    for x,y in edge_list(adj):
        changed=list(adj);changed[x]^=1<<y;changed[y]^=1<<x
        if diameter_at_most_two(changed):return False
    return True


def bipartite(adj):
    colour={}
    for start in range(len(adj)):
        if start in colour:continue
        colour[start]=0;todo=[start]
        while todo:
            x=todo.pop()
            for y in vertices(adj[x]):
                if y in colour:
                    if colour[y]==colour[x]:return False
                else:colour[y]=1-colour[x];todo.append(y)
    return True


def canonical(adj):
    groups={}
    for x,row in enumerate(adj):groups.setdefault(row.bit_count(),[]).append(x)
    best=None
    for blocks in product(*(permutations(groups[d]) for d in sorted(groups))):
        order=sum((tuple(b) for b in blocks),())
        code=tuple(int(bool(adj[x]>>y&1)) for x,y in combinations(order,2))
        if best is None or code<best:best=code
    return (len(adj),best)


def witness_checks(g):
    n=len(g);edges=set(edge_list(g));degrees=[row.bit_count() for row in g]
    direct=[];two=[];covered=set()
    for x,y in combinations(range(n),2):
        common=vertices(g[x]&g[y])
        if (x,y) in edges and not common:direct.append((x,y));covered.add((x,y))
        if (x,y) not in edges and len(common)==1:
            two.append((x,y));z=common[0]
            covered.update([tuple(sorted((x,z))),tuple(sorted((y,z)))])
    ensure(covered==edges,'witness_edge_coverage')
    dom=any((g[x]|g[y])==(1<<n)-1 for x,y in edges)
    if dom:return
    ensure(all(degrees[x]+degrees[y]<=n-1 for x,y in direct+two),'witness_degree_sum')
    D=max(degrees)
    if 2*D!=n+1:return
    low={x for x,d in enumerate(degrees) if D-d>=2}
    one={x for x,d in enumerate(degrees) if D-d==1}
    rest=set(range(n))-low;h=len(low);o=len(one)
    c=sum(x in rest and y in rest for x,y in edges)
    cross=sum((x in low)!=(y in low) for x,y in edges)
    ensure(c<=2*math.comb(o,2)+h*(n-h)-cross,'section3_partition_bound')
    ensure(len(edges)<=math.comb(h,2)+h*(n-h)+2*math.comb(o,2),'section3_total_bound')


def study(g,tag,small=False):
    global CURRENT
    n=len(g);CURRENT=dict(graph=tag,n=n,edges=edge_list(g))
    ensure(critical(g),'input_criticality')
    witness_checks(g)
    if bipartite(g):COUNTS['bipartite_inputs']+=1;return
    h=tuple(((1<<n)-1)^row^(1<<i) for i,row in enumerate(g))
    full=(1<<n)-1;V=set(range(n));hn=[set(vertices(row)) for row in h]
    hedges=edge_list(h)
    ensure(all((h[x]|h[y])!=full for x,y in hedges),'no_total_dominating_pair')
    ensure(any(h[x]|h[y]|h[z]==full for x,y,z in combinations(range(n),3)),'total_dominating_triple')
    for x,y in combinations(range(n),2):
        if h[x]>>y&1:continue
        hh=list(h);hh[x]|=1<<y;hh[y]|=1<<x
        ensure(any(hh[u]|hh[w]==full for u,w in hedges+[(x,y)]),'edge_addition_total_domination')
    exception={}
    for x,y in hedges:
        missing=full^(h[x]|h[y])
        if missing and missing&(missing-1)==0:
            exception[x,y]=exception[y,x]=missing.bit_length()-1
    minimum=min(row.bit_count() for row in h)
    bases=range(n) if small else [x for x in range(n) if h[x].bit_count()==minimum]
    for v in bases:
        A=sorted(hn[v]);B=sorted(V-hn[v]-{v});a=len(A);b=len(B)
        if not A or not B:continue
        is_min=a==minimum
        F={(i,j) for i,j in combinations(A,2) if j not in hn[i]}
        fn={i:{j for j in A if j!=i and j not in hn[i]} for i in A}
        ds={i:len(fn[i]) for i in A}
        cross={(i,z) for i in A for z in B if z in hn[i]}
        pairs=[(z,w) for z,w in combinations(B,2) if w not in hn[z]]
        options=[]
        for z,w in pairs:
            opts=[(i,src,dst) for src,dst in [(z,w),(w,z)] for i in A
                  if (i,src) in cross and exception.get((i,src))==dst]
            ensure(bool(opts),'selected_edge_exists')
            options.append(opts)
        ways=math.prod(map(len,options))
        if small:
            ensure(ways<=100000,'small_assignment_exhaustiveness_budget')
            assignments=product(*options)
            COUNTS['exhaustive_bases']+=1
        else:
            assignments=[tuple(opts[0] for opts in options)]+[tuple(RNG.choice(opts) for opts in options) for _ in range(7)]
            COUNTS['sampled_bases']+=1
        for choice in assignments:
            CURRENT=dict(graph=tag,n=n,edges=edge_list(g),base=v,selected=choice)
            selected={(i,z):w for i,z,w in choice}
            ensure(len(selected)==len(pairs),'selected_pair_injection')
            residual=cross-set(selected);r=len(residual)
            rho={z:sum(w==z for i,w in residual) for z in B}
            R={i:sum(j==i for j,w in residual) for i in A}
            q={z:sum(w==z for i,w in selected) for z in B}
            PROFILE['largest_selected_source_degree']=max(PROFILE['largest_selected_source_degree'],max(q.values()))
            ec=sum(j in hn[i] for i,j in combinations(A,2))
            L=len(hedges)-a-math.comb(b,2);t=math.comb(a,2)-L
            ensure(ec+r==L and len(F)==r+t,'residual_ledger')
            if not is_min and any(len(hn[i]&set(B))<ds[i] for i in A):
                NEGATIVE.setdefault('minimum_base_is_necessary',dict(context=CURRENT,degrees_F=ds,cross_degrees={i:len(hn[i]&set(B)) for i in A}))
            if is_min:
                ensure(all(len(hn[i]&set(B))>=ds[i] for i in A),'minimum_degree_column_demand')
                ensure(len(selected)>=r+2*t,'selected_total_demand')
            for (i,z),w in selected.items():
                ensure(ds[i]<=rho[z]+rho[w],'pair_residual_bound')
                ensure(ds[i]<=rho[z]+R[i],'column_residual_bound')
                ensure(ds[i]<=rho[z]+q[z]-1 and q[z]+rho[z]<=a,'source_closure_bound')
                other=[j for j,s in selected if s==z and j!=i]
                ensure(all(j in hn[w] for j in other),'supplement_other_labels')
                ensure(len(hn[w]&set(A))>=q[z]-1,'supplement_degree_bound')
            for z in B:
                if rho[z]:continue
                S=hn[z]&set(A);T=set(A)-S
                ensure(not any((i in S)!=(j in S) for i,j in F),'inactive_no_F_crossing')
                FS=[(i,j) for i,j in F if i in S];FT=[(i,j) for i,j in F if i in T]
                PROFILE['inactive_seen_forced_edges']+=2*len(FS)
                PROFILE['inactive_missed_forced_edges']+=len(FT)
                forcedS=[e for i,j in FS for e in [(j,selected[i,z]),(i,selected[j,z])]]
                ensure(len(set(forcedS))==2*len(FS) and set(forcedS)<=residual,'inactive_seen_injection')
                forcedT=[]
                for i,j in FT:
                    opts=[(u,w) for u,dst in [(i,j),(j,i)] for w in hn[u] if exception.get((u,w))==dst]
                    ensure(opts and all(w in B for u,w in opts),'inactive_missed_auxiliary_location')
                    forcedT.append(opts[0])
                ensure(len(set(forcedT))==len(FT) and set(forcedT)<=residual and not set(forcedT)&set(forcedS),'inactive_missed_injection')
                ensure(r>=len(F)+len(FS),'inactive_inequality')
                NEGATIVE.setdefault('positive_surplus_is_necessary',dict(context=CURRENT,inactive=z,r=r,F_edges=len(F),t=t))
            if t>0:
                PROFILE['positive_surplus_assignments']+=1
                ensure(all(rho.values()),'positive_surplus_all_active')
            k=min(len(hn[i]&set(A)) for i in A)
            for x in A:
                if len(hn[x]&set(A))!=k or k>1:continue
                Y=hn[x]&set(A);X=set(A)-Y-{x};missing=[(i,j) for i,j in combinations(sorted(X),2) if j not in hn[i]]
                P=[];y_edges=[]
                for i,j in missing:
                    opts=[(u,z) for u,w in [(i,j),(j,i)] for z in hn[u] if exception.get((u,z))==w]
                    ensure(opts and all(z in Y or z in B for u,z in opts),'low_k_auxiliary_location')
                    u,z=opts[0]
                    (P if z in B else y_edges).append((u,z))
                ensure(len(set(P))==len(P) and set(P)<=residual,'low_k_P_injection')
                used={z for u,z in P}
                ensure(all((x,z) in residual and (x,z) not in P for z in used),'low_k_extra_x_edges')
                if all(rho.values()):
                    extra=[(x,z) for z in used]+[next(e for e in residual if e[1]==z) for z in B if z not in used]
                    ensure(len(set(extra))==b and not set(extra)&set(P),'low_k_extra_edge_injection')
                    ensure(b<=r-len(P),'low_k_residual_budget')
                    ensure(b<=L-math.comb(a-1,2) if k==0 else b<=L-1-math.comb(a-2,2),'low_k_final_inequality')
                elif b>r-len(P):
                    NEGATIVE.setdefault('low_k_needs_all_active',dict(context=CURRENT,k=k,r=r,m=len(P),B=b))
            if is_min:
                hh=max([0]+[j for j in range(1,b+1) if sum(rho[z]>=j for z in B)>=j])
                ensure(all(R[i]>=max(0,ds[i]-hh) for i in A),'h_index_column_bound')
                for cut in range(1,max(ds.values())+1):
                    S=[i for i in A if ds[i]>=cut]
                    lower=sum(ds[i] for i in S)-sum(min(rho[z],len(S)) for z in B)
                    upper=sum(rho[z]+rho[w]>=cut for z,w in combinations(B,2))
                    ensure(lower<=upper,'selected_pair_threshold')
                subsets=list(range(1,1<<a)) if a<=6 else [RNG.randrange(1,1<<a) for _ in range(24)]
                for mask in subsets:
                    S=[i for j,i in enumerate(A) if mask>>j&1]
                    demand=sum(max(0,ds[i]-R[i]) for i in S)
                    available=sum(min(q[z],sum(ds[i]<=rho[z]+q[z]-1 and ds[i]<=rho[z]+R[i] for i in S)) for z in B)
                    ensure(demand<=available,'subset_capacity_with_actual_q')
            COUNTS['selected_assignments']+=1


def main():
    seen=set();catalogue=[];labelled={}
    for n in range(3,7):
        pairs=list(combinations(range(n),2));total=0;d2c=0
        for mask in range(1<<len(pairs)):
            g=graph(n,[e for j,e in enumerate(pairs) if mask>>j&1]);total+=1
            if not critical(g):continue
            d2c+=1;key=canonical(g)
            if key in seen:continue
            seen.add(key);catalogue.append(g)
            study(g,f'exhaustive_n{n}_mask{mask}',small=True)
        labelled[str(n)]=dict(graphs=total,diameter2critical=d2c)
        print(json.dumps(dict(stage='exhaustive',n=n,counts=labelled[str(n)])),flush=True)
    generated=[]
    for n in [7,8,9,10,12,14,16,20,25]:
        for trial in range(20):
            p=[0.35,0.5,0.75,1.0][trial%4]
            while True:
                g=graph(n,[e for e in combinations(range(n),2) if RNG.random()<p])
                if diameter_at_most_two(g):break
            g=list(g);order=edge_list(g);RNG.shuffle(order)
            for x,y in order:
                g[x]^=1<<y;g[y]^=1<<x
                if not diameter_at_most_two(g):g[x]^=1<<y;g[y]^=1<<x
            generated.append(tuple(g));study(tuple(g),f'generated_n{n}_{trial}')
        print(json.dumps(dict(stage='generated',n=n,selected_assignments=COUNTS['selected_assignments'])),flush=True)
    for sizes in [(1,1,1,1,1),(1,1,1,1,2),(2,2,2,2,2),(1,1,1,10,12),(5,5,5,5,5)]:
        groups=[];offset=0
        for size in sizes:groups.append(list(range(offset,offset+size)));offset+=size
        g=graph(offset,[(x,y) for j in range(5) for x in groups[j] for y in groups[(j+1)%5]])
        generated.append(g);study(g,'C5_blowup_'+str(sizes))
    k=graph(25,[(x,y) for x in range(12) for y in range(12,25)])
    NEGATIVE['no_dominating_edge_premise_is_necessary']=dict(graph='K12,13',critical=critical(k),edges=156,direct_witness_degree_sum=25,claimed_without_premise_upper=24)
    result=dict(status='PASS',scope='Finite falsification only, not proof or independent external review',seed=250906,
                labelled_search=labelled,nonisomorphic_small_representatives=len(catalogue),generated_graphs=len(generated),
                counts=dict(COUNTS),profile=dict(PROFILE),negative_controls=NEGATIVE)
    (OUT/'structural_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    (OUT/'tested_graphs.json').write_text(json.dumps(dict(small=[edge_list(g) for g in catalogue],generated=[dict(n=len(g),edges=edge_list(g)) for g in generated]),separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='negative_controls'},sort_keys=True),flush=True)


if __name__=='__main__':main()
