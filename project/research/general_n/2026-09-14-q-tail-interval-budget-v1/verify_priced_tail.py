#!/usr/bin/env python3
"""Independent tests of the selected-excess priced-tail inequality.
The universal upper bound needs an actual selected-incidence/endpoint bridge.
Relaxed profiles are not asserted graph-realizable.
"""
import itertools,json,collections
from pathlib import Path
from verify_interval_budget import check,target_caps
ROOT=Path(__file__).parent

def lower_bound(A,f,v,demand,theta):
    free=[min(a,r) for a,r in zip(A,f)]
    paid=[a-r for a,r in zip(A,free)]
    return theta*(demand-sum(free))-sum(max(0,theta-x)*p for x,p in zip(v,paid))

def test_receiver_dual():
    count=0;demands=0
    types=list(itertools.product(range(3),range(2),range(3)))
    for n in range(1,4):
        for pp in itertools.combinations_with_replacement(types,n):
            A,f,v=map(list,zip(*pp));best={}
            for x in itertools.product(*(range(a+1) for a in A)):
                D=sum(x);cost=sum(w*max(0,y-r) for w,y,r in zip(v,x,f))
                best[D]=min(best.get(D,10**9),cost)
            for D,value in best.items():
                dual=max(lower_bound(A,f,v,D,theta) for theta in {0,*v})
                assert dual==value
                demands+=1
            count+=1
    return dict(receiver_profiles=count,feasible_demand_values=demands)

def test_selected_charge():
    count=0
    for a in range(1,4):
        for b in range(1,4):
            for bits in itertools.product((0,1),repeat=a*b):
                M=[bits[u*a:(u+1)*a] for u in range(b)]
                q=[sum(row) for row in M]
                if any(x>=a for x in q):continue
                x=[sum(M[u][i] for u in range(b)) for i in range(a)]
                for rho in itertools.product(*(range(1,a-qu+1) for qu in q)):
                    lim=[min([x[i]]+[rho[u] for u in range(b) if M[u][i]]) for i in range(a)]
                    for s in itertools.product(*(range(l+1) for l in lim)):
                        e=[xx-ss for xx,ss in zip(x,s)];E=sum(e);z=s.count(0)
                        # Maximal endpoint-excess demand at each positive-label source.
                        d=[min([e[i] for i in range(a) if M[u][i] and s[i]>0],default=0) for u in range(b)]
                        charge=sum(max(0,q[u]-z)*d[u] for u in range(b))
                        exact=sum(ei*xi for ei,xi in zip(e,x));envelope=E*(E+max(s,default=0))
                        assert charge<=exact<=envelope
                        count+=1
    return dict(selected_incidence_configurations=count)

def remaining_fixture():
    q=[0,0,0,0,0,1,2,2,2,2,7,7,7,7,7,7,7,7]
    rho=[1,1,1,1,1,3]+[4]*12
    s=[2]+[4]*14
    P=[3]*5+[5]+[6]*4+[4]*8
    a=15;t=1;D0=0;E=sum(q)-sum(s);tau=3;theta=7;z=s.count(0)
    computed=target_caps(a,q,rho,E,z)
    for eta in sorted({0,*rho}):
        low=[si for si in s if si<=eta]
        C=E+sum(low)-sum(qu for qu,ru in zip(q,rho) if ru<=eta)
        assert C>=0
        for w in range(len(q)):
            k=min(len(low),q[w],C)
            if rho[w]>eta and q[w]>k:
                computed[w]=min(computed[w],rho[w]-1+(C-k)//(q[w]-k))
    assert computed==P
    c=[qu+ru for qu,ru in zip(q,rho)]
    A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 for u in range(len(q)))) for w in range(len(q))]
    demand=sum(qu for qu in q if qu>=tau);free=[ru-1 for ru in rho];v=[max(0,qu-z) for qu in q]
    lower=lower_bound(A,free,v,demand,theta);upper=E*(E+max(s))
    rows=check(q,rho,P,a,t,D0,E)['rows']
    assert max(row['deficiency'] for row in rows)==0
    assert demand==sum(A)==56 and lower==80 and upper==77
    return dict(state=4073,a=a,b=len(q),t=t,D0=D0,Esel=E,q=q,rho=rho,s=s,P_local=P,tau=tau,theta=theta,interval_slots=A,tail_demand=demand,tail_capacity=sum(A),forced_excess_cost_lower=lower,selected_excess_budget_upper=upper,strict_gap=lower-upper,maximum_Hall_tail_deficiency=0)

def main():
    result=dict(status='PASS',scope='Exact receiver dual and selected-incidence charge tests; graph bridge remains an explicit hypothesis',**test_receiver_dual(),**test_selected_charge(),remaining_fixture=remaining_fixture())
    (ROOT/'PRICED_TAIL_VERIFICATION.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
