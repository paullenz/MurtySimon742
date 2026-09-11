#!/usr/bin/env python3
"""Independent standard-library census for n=29, Delta=16 charging profiles.

Enumerates every nondecreasing length-12 integer tuple 0<=s_i<=11 and counts
those satisfying

    sum s_i(13-2s_i)/(12-s_i) >= 16+2t.

Expected counts for t=2..8:
    9251, 4867, 2032, 586, 79, 1, 0
"""
from fractions import Fraction

A=12
B=16
VAL=[Fraction(s*(A+1-2*s),A-s) for s in range(A)]


def count_for_t(t):
    need=Fraction(B+2*t)
    count=0
    unique=None
    cur=[]
    tail=[max(VAL[i:]) for i in range(A)]

    def rec(left,lo,total):
        nonlocal count,unique
        if left==0:
            if total>=need:
                count+=1
                if count==1:
                    unique=tuple(cur)
                else:
                    unique=None
            return
        if total+left*tail[lo] < need:
            return
        for s in range(lo,A):
            if total+VAL[s]+(left-1)*tail[s] < need:
                continue
            cur.append(s)
            rec(left-1,s,total+VAL[s])
            cur.pop()

    rec(A,0,Fraction())
    return count,unique


def main():
    expected={2:9251,3:4867,4:2032,5:586,6:79,7:1,8:0}
    got={}
    for t in range(2,9):
        count,unique=count_for_t(t)
        got[t]=count
        print(f"t={t}: {count}" + (f" unique={unique}" if unique else ""))
    assert got==expected,(got,expected)
    print("PASS")


if __name__=="__main__":
    main()
