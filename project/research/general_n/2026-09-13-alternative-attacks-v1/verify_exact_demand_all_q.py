#!/usr/bin/env python3
"""Exact integer replay of the all-q exact-demand exclusion for N34 state 227."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def F(m,Q,P):
    """Minimum sum q(q+p) over m active rho=3 sources."""
    dp={(0,0):0}
    for _ in range(m):
        nd={}
        for (q0,p0),cost in dp.items():
            for q in range(1,8):
                for p in range(3):
                    nq,np_=q0+q,p0+p
                    if nq>Q or np_>P:
                        continue
                    key=(nq,np_)
                    value=cost+q*(q+p)
                    if value<nd.get(key,10**9):
                        nd[key]=value
        dp=nd
    return dp.get((Q,P))

def main():
    z0=[]
    for k in range(6,11):
        P=max(0,5*k-34)
        value=F(k,41,P)
        assert value is not None
        z0.append({
            'active_sources':k,
            'rho2_active':False,
            'minimum_active_incoming':P,
            'minimum_A_lower_bound':value,
        })

    z1=[]
    for k in range(7,12):
        P=max(0,5*k-35)
        best=None; arg=None
        for q2 in range(1,5):
            for p2 in range(2):
                if p2>P:
                    continue
                tail=F(k-1,41-q2,P-p2)
                if tail is None:
                    continue
                r2=q2*max(0,q2+p2-2)
                value=q2*(q2+p2)+r2+tail
                if best is None or value<best:
                    best=value
                    arg={'q2':q2,'p2':p2,'rho3_cost':tail,'rho2_R2_lower':r2}
        assert best is not None
        z1.append({
            'active_sources':k,
            'rho2_active':True,
            'minimum_active_incoming':P,
            'minimum_A_lower_bound':best,
            'minimizer':arg,
        })

    assert [x['minimum_A_lower_bound'] for x in z0]==[281,246,241,236,233]
    assert [x['minimum_A_lower_bound'] for x in z1]==[253,245,240,235,234]
    global_min=min(x['minimum_A_lower_bound'] for x in z0+z1)
    assert global_min==233
    assert global_min>232

    out={
        'schema':'state-227-exact-demand-all-q-v1',
        'state':{
            'layer':'n34-m289','state_id':227,
            'a':15,'b':18,'t':1,
            's':'2^4,3^11','rho':'1^7,2,3^10','S':41,'r':39,
        },
        'necessary_upper_bound':{
            'quantity':'sum_u q_u(q_u+p_u)+R_2','upper':232,
        },
        'rho2_inactive_table':z0,
        'rho2_active_table':z1,
        'global_minimum_lower_bound':global_min,
        'status':'PASS',
        'conclusion':'No exact-demand x=s selected geometry exists for state 227 for any q-vector.',
        'scope':'Closes G2 for state 227 only. Does not exclude x>s or the whole scalar state.',
    }
    (HERE/'EXACT_DEMAND_ALL_Q_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','upper':232,'minimum_lower':global_min},indent=2))

if __name__=='__main__':
    main()
