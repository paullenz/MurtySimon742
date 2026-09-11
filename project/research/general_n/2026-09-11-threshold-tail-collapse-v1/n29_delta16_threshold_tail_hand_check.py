#!/usr/bin/env python3
"""Exact regression audit for N29 Delta16 threshold-tail hand proof.

This does NOT re-run the 1,352,078-multiset search.  It checks only the finite
local obligations used in N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md:
  * high-tail nonpositivity h>=7;
  * the exceptional clipping cases 6->5, 5->4, 4->3;
  * the final two-level inequality for all 0<=y<=x<=12.
All arithmetic is integer exact; no solver or floating point is used.
"""
from __future__ import annotations
from argparse import ArgumentParser
from pathlib import Path
import json

A=12
B=16


def cap(h:int,z:int)->int:
    """Twice C_h(z): z(z-1)+h(h+1)."""
    return z*(z-1)+h*(h+1)


def g(h:int,W:int)->int:
    if W==0:
        return 0
    for z in range(h,B+1):
        if 2*W<=cap(h,z):
            return z
    raise AssertionError(('threshold_incompatible',h,W))


def D_constant(m:int)->int:
    return sum(12-g(h,12*m) for h in range(2,m+1))


def main():
    ap=ArgumentParser();ap.add_argument('--output',type=Path);z=ap.parse_args()
    checks={}

    # Section 2: h>=7 gives d_h<=0 already from W_h>=h N_h.
    high=[]
    for h in range(7,12):
        for N in range(13):
            W=h*N
            gh=0 if N==0 else g(h,W)
            high.append((h,N,gh,N-gh))
            assert N-gh<=0,(h,N,gh)
    checks['high_tail_nonpositive']=True

    # Section 4: clip 6->5.
    for k in range(0,11):
        gh=0 if k==0 else g(6,6*k)
        assert k-gh<=0,('six_nonexceptional',k,gh)
    six=[]
    for k in (11,12):
        d6=k-g(6,6*k)
        ls=range(0,2) if k==11 else range(0,1)
        for l in ls:
            before=6*k+5*l
            after=5*(k+l)
            drop=g(5,before)-g(5,after)
            six.append((k,l,d6,drop))
            assert drop>=d6,('six_exception',k,l,d6,drop)
    checks['clip_6_to_5']=six

    # Section 5: clip 5->4.
    for k in range(0,10):
        gh=0 if k==0 else g(5,5*k)
        assert k-gh<=0,('five_nonexceptional',k,gh)
    five=[]
    for k in (10,11):
        d5=k-g(5,5*k)
        for l in range(0,13-k):
            before=5*k+4*l
            after=4*(k+l)
            drop=g(4,before)-g(4,after)
            five.append((k,l,d5,drop))
            assert drop>=d5,('five_exception',k,l,d5,drop)
    assert D_constant(5)==4
    checks['clip_5_to_4']=five
    checks['D_5_pow_12']=4

    # Section 6: clip 4->3.
    for k in range(0,9):
        gh=0 if k==0 else g(4,4*k)
        assert k-gh<=0,('four_nonexceptional',k,gh)
    four=[]
    for k in (9,10):
        d4=k-g(4,4*k)
        for l in range(0,13-k):
            before=4*k+3*l
            after=3*(k+l)
            drop=g(3,before)-g(3,after)
            four.append((k,l,d4,drop))
            assert drop>=d4,('four_exception_9_10',k,l,d4,drop)
    # k=11: l=0 uses g3 alone; l=1 uses g3+g2.
    k=11;d4=k-g(4,4*k)
    drop0=g(3,4*k)-g(3,3*k)
    assert drop0>=d4,('four_exception_11_0',d4,drop0)
    old3=4*k+3;new3=3*12
    old2=4*k+3;new2=3*12
    drop1=(g(3,old3)-g(3,new3))+(g(2,old2)-g(2,new2))
    assert drop1>=d4,('four_exception_11_1',d4,drop1)
    # k=12: all fours; g3+g2 drops pay d4.
    k=12;d4=k-g(4,4*k)
    drop12=(g(3,48)-g(3,36))+(g(2,48)-g(2,36))
    assert drop12>=d4,('four_exception_12',d4,drop12)
    checks['clip_4_to_3']=four+[(11,0,d4,drop0),(11,1,d4,drop1),(12,0,d4,drop12)]

    # Section 7: final max-demand-three problem.  This is only 91 integer pairs,
    # and each row is exactly the displayed hand inequality, not a demand-vector
    # enumeration.
    rows=[];mx=-10**9;eq=[]
    for y in range(13):
        for x in range(y,13):
            W2=2*x+y;W3=3*y
            g2=0 if W2==0 else g(2,W2)
            g3=0 if W3==0 else g(3,W3)
            D=x+y-g2-g3
            if y<=6:
                assert x-g2<=5,(x,y,g2,g3,D)
                assert y-g3<=0,(x,y,g2,g3,D)
            elif y<=10:
                assert x-g2<=4,(x,y,g2,g3,D)
                assert y-g3<=2,(x,y,g2,g3,D)
            else:
                assert x-g2<=3,(x,y,g2,g3,D)
                assert y-g3<=3,(x,y,g2,g3,D)
            assert D<=6,(x,y,g2,g3,D)
            rows.append((x,y,g2,g3,D))
            if D>mx:mx=D;eq=[(x,y)]
            elif D==mx:eq.append((x,y))
    assert mx==6
    assert eq==[(12,11),(12,12)]
    checks['final_two_level_pairs']=len(rows)
    checks['max_D_after_reduction']=mx
    checks['max_D_pairs']=eq

    out={
        'schema':'n29-delta16-threshold-tail-hand-check-v1',
        'status':'PASS',
        'checks':checks,
        'solver_used':False,
        'floating_point_used':False,
        'arithmetic':'integer exact',
        'logical_conclusion':'The local case obligations in the hand reduction D(s)<=6 all pass. Together with Q=p+D and p<=12, this yields Q<=18 without the 1,352,078-multiset search.'
    }
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if z.output:
        z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
