#!/usr/bin/env python3
from fractions import Fraction
from math import comb, ceil


def check_threshold_algebra():
    # Integer identity used in the threshold-capacity proof:
    # target - rhs = (q-j)(q-j-1)/2, q=z-h.
    for h in range(1, 25):
        for z in range(h, 40):
            q = z - h
            for j in range(0, 40):
                rhs = (z-j)*h + j*z - j*(j+1)//2
                target = h*z + (q*(q-1))//2
                diff = target - rhs
                want = ((q-j)*(q-j-1))//2
                assert diff == want, (h,z,j,diff,want)
                assert want >= 0, (h,z,j,want)


def charge_term(a, s):
    assert 0 <= s <= a-1
    return Fraction(s*(a+1-2*s), a-s)


def lower_charge_term(a, s):
    assert 0 <= s <= a-1
    return Fraction(s*(s-1), a-s)


def check_charging_elimination():
    # Exact pointwise identity behind eliminating r:
    # s - s(s-1)/(a-s) = s(a+1-2s)/(a-s).
    for a in range(2, 30):
        for s in range(0, a):
            lhs = Fraction(s,1) - lower_charge_term(a,s)
            rhs = charge_term(a,s)
            assert lhs == rhs, (a,s,lhs,rhs)

    # Exhaustive small synthetic profiles confirm the summed implication.
    # If r-b >= L and S>=r+2t, then charge_sum >= b+2t.
    for a in range(2, 9):
        vals = list(range(a))
        # constant profiles and two-level profiles are enough to exercise signs exactly.
        profiles = []
        for s in vals:
            profiles.append([s]*a)
        for s in vals:
            for u in vals:
                profiles.append([s]*(a//2) + [u]*(a-a//2))
        for prof in profiles:
            S = sum(prof)
            L = sum(lower_charge_term(a,s) for s in prof)
            C = sum(charge_term(a,s) for s in prof)
            assert C == Fraction(S,1)-L
            for b in range(1, 12):
                for t in range(1, 8):
                    # There exists an r meeting both hypotheses only if b+L <= S-2t.
                    if Fraction(b,1)+L <= S-2*t:
                        assert C >= b+2*t, (a,b,t,prof,C)


def pointwise_max(a):
    vals=[charge_term(a,s) for s in range(a)]
    return max(vals), [s for s,v in enumerate(vals) if v==max(vals)]


def check_fixed_order_caps():
    # a=12 cap used at n=28/n=29/n=30.
    mx, where = pointwise_max(12)
    assert mx == Fraction(5,2)
    assert where == [4]

    # a=13 cap used at n=30, Delta=16.
    mx, where = pointwise_max(13)
    assert mx == Fraction(8,3)
    assert where == [4]

    # N29, Delta=16: a=12,b=16. Total charging <=30 => t<=7.
    assert 12*Fraction(5,2) == 30
    assert (30-16)//2 == 7

    # Boundary t=7: all 12 demands must be 4, S=48, r=34.
    S=12*4
    L=12*lower_charge_term(12,4)
    assert S == 48
    assert L == 18
    rmin=16+L
    rmax=S-14
    assert rmin == rmax == 34
    z4max=(34-16)//3
    assert z4max == 6
    threshold_rhs=z4max*z4max-z4max+4*5
    assert 2*S == 96
    assert threshold_rhs == 50
    assert 96 > 50

    # N30 Delta=17: a=12,b=17 => t<=6 => m=221+t<=227.
    assert (30-17)//2 == 6

    # N28 Delta=15: a=12,b=15 => t<=7 => m=195+t<=202.
    assert (30-15)//2 == 7

    # N30 Delta=16: a=13,b=16, total <=104/3 gives integer t<=9.
    total=13*Fraction(8,3)
    assert total == Fraction(104,3)
    feasible=[t for t in range(0,30) if Fraction(16+2*t,1) <= total]
    assert max(feasible)==9


def check_isolated_c_specialisations():
    # General upper bound r <= C(a,2)-t-ceil(a/2), when isolated-C is excluded.
    def rmax(a,t):
        return comb(a,2)-t-ceil(a/2)
    assert rmax(12,2)==58
    assert rmax(12,3)==57
    # Equivalent to 60-t for a=12.
    for t in range(1,12):
        assert rmax(12,t)==60-t
    # a=13 gives 71-t.
    for t in range(1,12):
        assert rmax(13,t)==71-t
    assert rmax(13,1)==70
    assert rmax(13,2)==69


def main():
    check_threshold_algebra()
    check_charging_elimination()
    check_fixed_order_caps()
    check_isolated_c_specialisations()
    print('UNIVERSAL_BRIDGE_EXACT_ARITHMETIC_AUDIT: PASS')


if __name__=='__main__':
    main()
