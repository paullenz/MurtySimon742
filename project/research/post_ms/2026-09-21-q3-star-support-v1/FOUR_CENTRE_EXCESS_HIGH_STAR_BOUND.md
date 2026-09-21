# A quantitative parity-star excess bound and the P1-dominance gate

21 September 2026. Unconditional at the exactly-four-centre Q3 parity-plane scope.

Write `R=P0`, `T=P1`, `U=M-I`, `s=|S|`, and

    B=e(G[R union T union S]),
    epsilon=max(0,B-rq-s).

Let `H` be the set of physical star vertices of bridge degree at least two and put `k=|H|`.

## Excess theorem

Every graph in the branch satisfies

    epsilon <= min(U, k(q-1)) <= min(U, s(q-1)).       (1)

## Proof

Partition parity--star and star edges as in the corrected cancellation ledger:

- `A=e(R,S)` consists of hard obligations;
- `T_H` is the number of `T--S` edges incident with a high-bridge star;
- `L` is the number of low-bridge `T--S` edges plus `e(S)`.

Parity substitution gives `e(R union T)=rq-U`. Therefore

    B-rq-s = A+T_H+L-U-s.                              (2)

The raw missing-pair injection gives `A<=U`. The star-token injection assigns every edge counted by `L` to a distinct low-bridge star token; every high-bridge star remains unused by that assignment. Hence

    L+k<=s.

Using these two inequalities in (2) gives

    B-rq-s <= T_H-k.

Each of the `k` high stars has at most `q` neighbours in `T`, so `T_H<=kq`; this proves `epsilon<=k(q-1)<=s(q-1)`. The old unconditional ledger gives `epsilon<=U`, completing (1).

The actual `n=33` RTS control has `epsilon=1`, showing that zero cannot replace the left side. It has `k>0`, so it is consistent with (1).

## Density consequence

Put `u=t+r+q` and retain

    D(u,s)=floor((u+s)^2/4)-floor(u^2/4)-s-3.

The budgeted cancellation theorem closes the branch whenever `epsilon<=D`. Thus (1) closes it whenever

    s(q-1) <= D(u,s).                                  (3)

There is a simple explicit gate. Since

    D-s(q-1)
      >= floor(s(2(t+r-q)+s)/4)-3,

(3) holds whenever

    s(2(t+r-q)+s) >= 12.                               (4)

Equivalently, writing `c_s=ceil(12/s)`, every survivor must satisfy

    q > t+r+floor((s-c_s)/2).                          (5)

In particular, the branch closes throughout `q<=t+r`. The only surviving parameter wedge is strongly `P1`-dominant: roughly `q>t+r+s/2`, in addition to the earlier conditions `s<ceil((r+q)/2)`, `U>D`, and `r,q>s/2`.

## Significance and trust boundary

This replaces false exact cancellation by a proved error term that is already sufficient outside a narrow one-sided population regime. It uses only the raw parity substitution, missing-pair injection and star-token injection; no selected/Hall source-tuple premise enters. It does not close the remaining P1-dominant wedge, where `s(q-1)` can exceed `D`.
