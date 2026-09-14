"""Numerical discovery of joint incidence/orientation witnesses, not a proof of infeasibility."""
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix
HERE=Path(__file__).resolve().parent
p=json.loads((HERE/'inputs.json').read_text())['rows'][int(sys.argv[1])]
s,q,rho,P=(p[k] for k in ('s','q','rho','P'))
a,b=len(s),len(q)
ix=lambda u,i:u*a+i
iy=lambda u,v:b*a+u*b+v
ie=lambda i:b*a+b*b+i
ip=lambda u:b*a+b*b+a+u
idp=lambda u:b*a+b*b+a+b+u
N=b*a+b*b+a+2*b
lo=np.zeros(N);hi=np.ones(N)
D=[max(0,P[u]-rho[u]+1) for u in range(b)]
for u in range(b):
 for i in range(a): hi[ix(u,i)]=int(s[i]<=rho[u])
 for v in range(b): hi[iy(u,v)]=int(u!=v and q[u]<=q[v]+rho[v]+1 and q[v]<=q[u]+rho[u])
 hi[ip(u)]=P[u];hi[idp(u)]=D[u]
for i in range(a): hi[ie(i)]=b-s[i]
r=[];c=[];v=[];lb=[];ub=[]
def add(terms,l,h):
 j=len(lb)
 for k,val in terms:
  r.append(j);c.append(k);v.append(val)
 lb.append(l);ub.append(h)
for u in range(b):
 add([(ix(u,i),1) for i in range(a)],q[u],q[u])
 add([(iy(u,z),1) for z in range(b)],q[u],q[u])
 add([(iy(z,u),1) for z in range(b)]+[(ip(u),-1)],0,0)
 add([(ip(u),1),(idp(u),-1)],-np.inf,rho[u]-1)
 for i in range(a):
  if s[i]>0:
   add([(idp(u),1),(ie(i),-1),(ix(u,i),D[u])],-np.inf,D[u])
for i in range(a):
 add([(ix(u,i),1) for u in range(b)]+[(ie(i),-1)],s[i],s[i])
for i in range(a-1):
 if s[i]==s[i+1]: add([(ie(i),1),(ie(i+1),-1)],0,np.inf)
for u in range(b):
 for z in range(u+1,b): add([(iy(u,z),1),(iy(z,u),1)],-np.inf,1)
add([(ie(i),1) for i in range(a)],p['Esel'],p['Esel'])
A=coo_matrix((v,(r,c)),shape=(len(lb),N)).tocsc()
res=milp(np.zeros(N),integrality=np.ones(N),bounds=Bounds(lo,hi),
 constraints=LinearConstraint(A,np.array(lb),np.array(ub)),options={'time_limit':8.0})
out={'row':p['row'],'solver_status':int(res.status),'solver_message':res.message,
     'scope':'Joint selected incidence, endpoint pressure and compatible simple orientation; NOT a graph or scalar-state closure.'}
if res.x is not None:
 z=[int(round(x)) for x in res.x]
 out['selected_labels']=[[i for i in range(a) if z[ix(u,i)]] for u in range(b)]
 out['arcs']=[[u,w] for u in range(b) for w in range(b) if z[iy(u,w)]]
 out['excess']=[z[ie(i)] for i in range(a)]
 out['incoming']=[z[ip(u)] for u in range(b)]
 out['pressure']=[max(0,z[ip(u)]-rho[u]+1) for u in range(b)]
 # This is only an early exact screening; a separate checker is required.
 out['rounded_linear_constraints_pass']=bool(np.all(A@np.array(z)>=np.array(lb)) and np.all(A@np.array(z)<=np.array(ub)))
(HERE/('joint_'+str(p['row'])+'.json')).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(p['row'],res.status,'witness',res.x is not None,out.get('rounded_linear_constraints_pass'),flush=True)
