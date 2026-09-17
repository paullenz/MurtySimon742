#!/usr/bin/env python3
"""Exact histogram census for the a=20,b=23,t=2, all-demand-4 h=5 band.
Standard library only. This is an auxiliary scalar/bridge census, not a graph census.
"""
A=20; B=23; R=76

def heavy_local_cost(h,T,H,p):
    ramp=max(0,T-max(h,H+p))
    return h*H+h*p+H*ramp-h*H*(H>h)

def restricted_C(h,T,P,c):
    return max(heavy_local_cost(h,T,H,p) for H in range(c+1) for p in range(P+1))

pre={}
for h in range(1,5):
    for T in range(h,61):
        arr=[]
        for rho in range(1,21):
            if rho<h:
                arr.append(0); continue
            P=rho+B-A-1
            count=20 if 4<=rho else 0
            c=min(A-rho,count)
            arr.append(restricted_C(h,T,P,c))
        pre[(h,T)]=arr

order=[]
for h in (4,3,2,1):
    center={4:16,3:12,2:8,1:5}[h]
    for T in sorted(range(h,61),key=lambda z:abs(z-center)):
        order.append((h,T))

profiles=0; survivors=[]

def hindex_five(c):
    return sum(c[4:])>=5 and sum(c[5:])<6

def passes(c):
    for h,T in order:
        lhs=h*20*max(T,4)
        rhs=h*R+sum(c[i]*pre[(h,T)][i] for i in range(20))
        if rhs<lhs: return False
    return True

def rec(rho,remn,remsum,c):
    global profiles
    if rho==21:
        if remn==0 and remsum==0 and hindex_five(c):
            profiles+=1
            if passes(c): survivors.append(tuple(c))
        return
    for n in range(remn+1):
        rs=remsum-rho*n
        if rs<0: break
        rem=remn-n
        if rem*(rho+1)<=rs<=rem*20:
            rec(rho+1,rem,rs,c+[n])

rec(1,23,76,[])
expected=(7,0,0,11,5)+(0,)*15
assert profiles==127885
assert survivors==[expected]
print({'status':'PASS','histograms':profiles,'finite_heavy_survivors':len(survivors),'survivor':survivors[0]})
