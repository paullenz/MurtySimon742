def relaxed(d,z,h,L):
    k=1+z*(d-1)+h; q=d*h-(d-1)*L
    if q<0: return None
    f=max(0,d-1-z-L)
    best=None
    for n0 in range(k+1):
        n1=max(0,2*(k-n0)-q)
        if n1>k-n0: continue
        val=d*h+(d-2)*L+(d-1)*n0+f*n1
        item=(val,h,L,n0,n1,k-n0-n1)
        if best is None or item<best: best=item
    return best

def minimize(d,z):
    ub=d*(2*z+4)
    best=None
    for h in range(ub//d+1):
        for L in range(d*h//(d-1)+1):
            r=relaxed(d,z,h,L)
            if r is not None and (best is None or r<best): best=r
    return best
for d in range(3,16):
    print(d,[(z,minimize(d,z),d*(z+1)-1) for z in range(1,min(d,4)+1)])
print('thresholds')
for d in range(3,13):
    for z in (1,2):
        B=minimize(d,z)[0]
        a=(z*d*(2*d-3)+B-d+4+(d-3))//(d-2)
        old=2*z*(d+1)+(-(-(4*z+3)//(d-2)))
        print(d,z,B,old,a,minimize(d,z))
