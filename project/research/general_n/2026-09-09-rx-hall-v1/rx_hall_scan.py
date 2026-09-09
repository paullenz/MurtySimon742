#!/usr/bin/env python3
"""Parameterized positive-demand RX-Hall reconnaissance scanner.

This is a NECESSARY-CONDITION relaxation for the Murty-Simon complement
quasi-edge framework.  It deliberately omits unordered-pair capacity.

Numerical LP infeasibility from this script is reconnaissance only until an
exact certificate layer is added.
"""
from collections import defaultdict
from pathlib import Path
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def groups(vals):
    d={}
    for x in vals:d[x]=d.get(x,0)+1
    return sorted(d.items())


class LP:
    def __init__(self):
        self.names=[]; self.eq=[]; self.be=[]; self.ub=[]; self.bu=[]
    def var(self,name):
        self.names.append(name); return len(self.names)-1
    def equal(self,row,b=0):
        self.eq.append(row); self.be.append(b)
    def le(self,row,b):
        self.ub.append(row); self.bu.append(b)
    @staticmethod
    def _mat(rows,n):
        rr=[];cc=[];vv=[]
        for i,row in enumerate(rows):
            for j,c in row.items():
                if c:
                    rr.append(i);cc.append(j);vv.append(c)
        return coo_matrix((vv,(rr,cc)),shape=(len(rows),n)).tocsr()
    def solve(self):
        n=len(self.names)
        U=self._mat(self.ub,n) if self.ub else None
        E=self._mat(self.eq,n)
        return linprog(
            np.zeros(n),
            A_ub=U,b_ub=np.array(self.bu,float) if self.ub else None,
            A_eq=E,b_eq=np.array(self.be,float),
            bounds=(0,None),method='highs'
        )


def build_rx_hall(a,b,dmax,s,rho):
    """Build the weakened positive-demand RX-Hall relaxation.

    Source constraints:
      q+rho<=a
      p<=rho+(b-a-1)
      q+p<=b-1
      supplement transport u->w only if rho_w+q_w>=q_u-1

    Label types retain only (R,x), since positive demand gives d=R+s.
    Selected source-label incidence requires
      s<=rho,
      R+s<=rho+q-1,
      R+x>=q+p.

    No unordered-pair capacity is imposed.
    """
    assert len(s)==a and len(rho)==b and min(s)>0
    r=sum(rho)
    LG=groups(s); SG=groups(rho); m=LP()
    W={}; source_types=defaultdict(list)

    # Source-type distributions within equal-rho groups.
    for k,(rh,nk) in enumerate(SG):
        norm={}
        for q in range(a-rh+1):
            pmax=min(rh+b-a-1,b-1-q)
            for p in range(pmax+1):
                w=m.var(('W',k,q,p));W[k,q,p]=w
                source_types[k].append((q,p,w));norm[w]=1
        m.equal(norm,1)

    # Source -> supplement transportation.  This keeps self-exclusion in the
    # grouped flow equations but deliberately omits pair-capacity inequalities.
    Pout=defaultdict(list); Pin=defaultdict(list)
    for k,(rhk,nk) in enumerate(SG):
        qks=sorted({q for q,p,w in source_types[k] if q>0})
        for l,(rhl,nl) in enumerate(SG):
            if k==l and nk<2:
                continue
            qls=sorted({q for q,p,w in source_types[l]})
            for q in qks:
                for q2 in qls:
                    if rhl+q2 < q-1:
                        continue
                    z=m.var(('P',k,l,q,q2))
                    Pout[k,q].append((l,z));Pin[l,q2].append((k,z))

    for k,(rh,nk) in enumerate(SG):
        for q in sorted({qq for qq,p,w in source_types[k] if qq>0}):
            row={}
            for qq,p,w in source_types[k]:
                if qq==q: row[w]=row.get(w,0)-q
            for l,z in Pout[k,q]:
                row[z]=row.get(z,0)+SG[l][1]-(k==l)
            m.equal(row,0)

    for l,(rh,nl) in enumerate(SG):
        for q2 in sorted({qq for qq,p,w in source_types[l]}):
            row={}
            for qq,p,w in source_types[l]:
                if qq==q2: row[w]=row.get(w,0)-p
            for k,z in Pin[l,q2]:
                row[z]=row.get(z,0)+SG[k][1]-(k==l)
            m.equal(row,0)

    # Label (R,x) distributions. Positive demand fixes d=R+s.
    L={}; label_types=defaultdict(list)
    for g,(sg,ng) in enumerate(LG):
        norm={}
        for R in range(dmax-sg+1):
            for x in range(sg,b-R+1):
                z=m.var(('L',g,R,x));L[g,R,x]=z
                label_types[g].append((R,x,z));norm[z]=1
        m.equal(norm,1)

    # Exact residual-column budget.
    residual={}
    for g,(sg,ng) in enumerate(LG):
        for R,x,z in label_types[g]:
            residual[z]=residual.get(z,0)+ng*R
    m.equal(residual,r)

    # Selected source-label incidence.
    by_source=defaultdict(list); by_label=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        for g,(sg,ng) in enumerate(LG):
            if sg>rh:
                continue
            for q,p,w in source_types[k]:
                if q==0:
                    continue
                for R,x,lvar in label_types[g]:
                    if R+sg > rh+q-1:
                        continue
                    if R+x < q+p:
                        continue
                    z=m.var(('Z',k,g,q,p,R,x))
                    by_source[k,q,p,g].append(z)
                    by_label[g,R,x].append((k,z))

    for k,(rh,nk) in enumerate(SG):
        for q,p,w in source_types[k]:
            total={w:-q}
            for g,(sg,ng) in enumerate(LG):
                cap={w:-1}
                for z in by_source[k,q,p,g]:
                    cap[z]=cap.get(z,0)+1
                    total[z]=total.get(z,0)+ng
                # A source can use at most one actual label from this group per
                # source-label pair; group density is normalized per label.
                m.le(cap,0)
            m.equal(total,0)

    for g,(sg,ng) in enumerate(LG):
        for R,x,lvar in label_types[g]:
            row={lvar:-x}
            for k,z in by_label[g,R,x]:
                row[z]=row.get(z,0)+SG[k][1]
            m.equal(row,0)

    return m


def load_rows(demands_json,rows_path):
    demands=json.loads(Path(demands_json).read_text())
    rows=[]
    for line in Path(rows_path).read_text().splitlines():
        if not line.strip(): continue
        z=list(map(int,line.split()))
        rows.append((z[0],z[1],z[2:]))
    return demands,rows


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--demands-json',type=Path,required=True)
    ap.add_argument('--rows',type=Path,required=True)
    ap.add_argument('--a',type=int,required=True)
    ap.add_argument('--b',type=int,required=True)
    ap.add_argument('--dmax',type=int,required=True)
    ap.add_argument('--t',type=int,required=True)
    ap.add_argument('--shard',type=int,default=0)
    ap.add_argument('--shards',type=int,default=1)
    ap.add_argument('--output',type=Path,required=True)
    z=ap.parse_args()
    if not (0<=z.shard<z.shards): raise SystemExit('bad shard')

    demands,rows=load_rows(z.demands_json,z.rows)
    counts={
        'rows_total':len(rows),'positive_zero_slack_total':0,
        'positive_nonzero_slack':0,'zero_demand_rows':0,
        'rows_in_shard':0,'numerical_infeasible':0,'numerical_feasible':0,
        'numerical_other':0,
    }
    survivors=[]
    hard_position=0
    for position,(did,total,rho) in enumerate(rows):
        s=demands[did]['s']
        if min(s)<=0:
            counts['zero_demand_rows']+=1; continue
        if sum(s)!=sum(rho)+2*z.t:
            counts['positive_nonzero_slack']+=1; continue
        counts['positive_zero_slack_total']+=1
        local=hard_position; hard_position+=1
        if local%z.shards!=z.shard:
            continue
        counts['rows_in_shard']+=1
        model=build_rx_hall(z.a,z.b,z.dmax,s,rho)
        res=model.solve()
        if res.status==2:
            counts['numerical_infeasible']+=1
        elif res.success:
            counts['numerical_feasible']+=1
            survivors.append({
                'position':position,'hard_position':local,'demand_id':did,
                'total':total,'s':s,'rho':rho,
            })
        else:
            counts['numerical_other']+=1
            survivors.append({
                'position':position,'hard_position':local,'demand_id':did,
                'total':total,'s':s,'rho':rho,'solver_status':res.status,
            })

    report={
        'schema':'general-rx-hall-recon-v1','status':'RECONNAISSANCE',
        'scope':{'a':z.a,'b':z.b,'dmax':z.dmax,'t':z.t},
        'shard':z.shard,'shards':z.shards,'counts':counts,
        'survivors':survivors,
        'uses_unordered_pair_capacity':False,
        'uses_cumulative_tail_variables':False,
        'positive_demand_only':True,
        'numerical_infeasibility_is_proof':False,
    }
    z.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report,sort_keys=True))


if __name__=='__main__':
    main()
