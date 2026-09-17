from fractions import Fraction as F


def u0(k):
    return 624 + 13*k + min(14*k, 76+k)


def legal(k, rho, p, q):
    if not (1 <= rho <= 20):
        return False
    if not (0 <= p <= min(rho+2, 22)):
        return False
    if not (0 <= q <= min(20-rho, 22-p)):
        return False
    if q > 0:
        if rho < 4:
            return False
        if rho == 4 and q > 20-k:
            return False
        g = max(0, p-rho+1)
        if g == 1 and q > 3:
            return False
        if g in (2, 3) and q > 1:
            return False
        if g >= 4:
            return False
    return True


def slack(k, rho, p, q):
    W = q*(p+q)
    H = 1 if rho >= 5 else 0
    I4 = 1 if rho == 4 else 0
    if k <= 2:
        return 3*W - (-42 - 42*rho + 28*p + 48*q + 32*H)
    if k <= 6:
        return W - (-19 - 14*rho + 11*p + 17*q + 3*H - q*I4)
    if k <= 13:
        return 7*W - (-133 - 98*rho + 77*p + 122*q - 10*q*I4)
    if k == 14:
        return 19*W - (-460 - 332*rho + 264*p + 361*q - 24*q*I4)
    if k == 15:
        return 48*W - (-1121 - 835*rho + 652*p + 912*q - 27*q*I4)
    if k <= 19:
        return 3*W - (-68 - 52*rho + 40*p + 57*q)
    return 4*W - (-109 - 71*rho + 60*p + 76*q)


def source_lower(k, x4=None):
    Q = 83+k
    r = 76+k
    if x4 is None:
        x4 = 83-4*k
    if k <= 2:
        return F(-14*23 - 14*r, 1) + F(28,3)*Q + F(16,1)*Q + F(32,3)*5
    if k <= 6:
        return F(-19*23 - 14*r + 11*Q + 17*Q + 3*5 - x4, 1)
    if k <= 13:
        return F(-19*23 - 14*r + 11*Q, 1) + F(122,7)*Q - F(10,7)*x4
    if k == 14:
        return F(-460*23 - 332*r + 264*Q + 361*Q - 24*x4, 19)
    if k == 15:
        return F(-1121*23 - 835*r + 652*Q + 912*Q - 27*x4, 48)
    if k <= 19:
        return F(-68*23 - 52*r + 40*Q + 57*Q, 3)
    return F(-109*23 - 71*r + 60*Q + 76*Q, 4)


checked = 0
for k in range(21):
    for rho in range(1, 21):
        for p in range(23):
            for q in range(21):
                if not legal(k, rho, p, q):
                    continue
                checked += 1
                s = slack(k, rho, p, q)
                assert s >= 0, (k, rho, p, q, s)

rows = []
for k in range(21):
    B = source_lower(k)
    U = F(u0(k)+81, 1)
    gap = B-U
    rows.append((k, B, U, gap))
    if k != 6:
        assert gap > 0, (k, B, U, gap)
assert rows[6][3] == -2

assert source_lower(6) == 863
assert u0(6)+77 == 861
assert source_lower(6) > u0(6)+77
assert u0(6)+78 == 862
assert source_lower(6) > u0(6)+78

B_special = source_lower(6, x4=56)
assert B_special == 866
assert u0(6)+81 == 865
assert B_special > u0(6)+81

print('PASS_E3_ROW_PACKING_BARRIER')
print('local_states_checked', checked)
for k, B, U, gap in rows:
    print(k, str(B), str(U), str(gap))
print('k6_special_source_lower', B_special)
