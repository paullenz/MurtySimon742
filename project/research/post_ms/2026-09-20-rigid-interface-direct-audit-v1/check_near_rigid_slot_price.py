#!/usr/bin/env python3
"""Audit-only arithmetic diagnostic for ONE_CODE_NEAR_RIGID_SLOT_PRICE.md.

This does not enumerate graphs. It compares the new near-equality slot-price
floor with the older gamma/U score floor over a broad abstract integer box.
The promoted mathematics is the hand theorem, not these counts.

The rigid cut is proper, so Y is nonempty. Since g0=p-y, the diagnostic uses
1<=g0<=p-1 rather than admitting the spurious y=0 boundary.
"""


def phi(g: int) -> int:
    return g * (g - 1) if g >= 3 else 0


def ell(p: int, x: int, g0: int, k: int) -> int:
    """Minimum integral L_X from L_X > x*g0-k(x-k)-p/2."""
    if k > x - 3:
        return 0
    n2 = 2 * x * g0 - 2 * k * (x - k) - p
    return max(0, n2 // 2 + 1)


def old_floor(p: int, x: int, gP: int) -> int:
    kP = max(0, x - gP)
    return phi(gP) + kP * (p - 1)


def new_floor(p: int, x: int, g0: int, gP: int):
    kP = max(0, x - gP)
    vals = []
    for k in range(kP, x + 1):
        u_price = k * (p - 1)
        if k <= x - 3:
            l_price = max(phi(gP), ell(p, x, g0, k))
        else:
            l_price = phi(gP)
        vals.append((u_price + l_price, k))
    return min(vals)


def main():
    checked = 0
    improved = 0
    max_gain = 0
    max_gain_row = None

    for p in range(3, 21):
        for x in range(3, 31):
            for g0 in range(1, p):  # y=p-g0 >= 1
                for gP in range(0, p + 1):
                    checked += 1
                    old = old_floor(p, x, gP)
                    new, k = new_floor(p, x, g0, gP)
                    if new < old:
                        raise AssertionError((p, x, g0, gP, old, new, k))
                    gain = new - old
                    if gain:
                        improved += 1
                    if gain > max_gain:
                        max_gain = gain
                        max_gain_row = (p, x, g0, gP, old, new, k)

    print("abstract states checked:", checked)
    print("new floor strictly stronger:", improved)
    print("maximum score-floor gain:", max_gain)
    print("max-gain row (p,x,g0,gP,old,new,minimizing_k):", max_gain_row)


if __name__ == "__main__":
    main()
