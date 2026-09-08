from math import isqrt, comb

def zmin(W,h,H):
    z=H
    while z*z-z+h*(h+1) < 2*W:
        z+=1
    return z
survive=[]
for H in range(1,11):
  for S in range(H,11*H+1):
    if S-H*H<12:continue
    W=[]
    for h in range(1,H+1):
      k=max(1,(S-11*(h-1)+H-h)//(H-h+1))
      wh=max(k*h,S-(11-k)*(h-1),H)
      W.append(wh)
    zs=[zmin(w,h,H) for h,w in enumerate(W,1)]
    for j in range(H-2,-1,-1):zs[j]=max(zs[j],zs[j+1])
    if S-sum(zs)>=12:
      survive.append((H,S,sum(zs),zs))
print('envelope survivors',survive)
# extremum via full profile independent exact enumeration
from itertools import combinations_with_replacement
count=0; mx=-100000; witnesses=[]
for s in combinations_with_replacement(range(11),11):
  count+=1
  H=s[-1]; S=sum(s)
  z=[zmin(sum(x for x in s if x>=h),h,H) for h in range(1,H+1)]
  R=sum(z)
  gap=S-R
  if gap>mx:mx=gap;witnesses=[(s,z,S,R)]
  elif gap==mx: witnesses.append((s,z,S,R))
print('profiles',count,'max S-R',mx,'witness count',len(witnesses),'first',witnesses[:5])
