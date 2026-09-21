# Complete density closure for the exactly-four-centre branch

21 September 2026. Internally proved at Q3-antipodal-transversal scope; independent and external review open.

## Theorem

Every D2C graph in the Q3 antipodal-transversal branch with exactly four distinct star centres satisfies

    m <= M(n)=floor((n-1)^2/4)+1.

The support classification already proves that every realizable four-centre support is a parity plane. Thus this closes the complete exactly-four-centre branch, at every order, while leaving five through eight centres and nontransversal outside codes open.

## Setup

In the parity-plane normalization let

    r=|R=P0|, q=|T=P1|, s=|S|, t=|C|,
    w=r+q, u=t+w,
    U=M-I,
    B=e(G[R union T union S]),
    epsilon=max(0,B-rq-s).

At least five coordinate codes and all four star-centre classes occur, so `t>=5`, `s>=4`, and `r>=1`.

Let `A=e(R,S)`. Let `H` be the high-bridge star vertices incident with a high-bridge `T--S` edge, put `k=|H|`, let `T_H` count those edges, and let `L` count the low-bridge `T--S` edges plus `e(S)`.

## The `q=0` boundary

If `q=0`, then `M=I=U=0`. The missing-pair injection forces `e(R,S)=0`, there are no `T--S` edges, and the star-forest theorem gives `e(S)<=s-1`. Hence `B<=s-1<rq+s`, so `epsilon=0` and the density closure is immediate.

Assume henceforth that `q>=1`.

## Symmetric excess bound

Parity substitution gives `e(R union T)=rq-U`, hence

    B-rq-s=A+T_H+L-U-s.                    (1)

Every star vertex has a critical centre spoke. Its sole available singleton code is `P0`, so it requires a physical `P0` vertex nonadjacent to that star. Therefore

    A <= s(r-1).                            (2)

The star-token injection assigns every edge counted by `L` to a distinct low-bridge star vertex. The `k` high-bridge vertices are unavailable to that assignment, giving

    L+k <= s.                               (3)

Trivially `T_H<=kq`. Combining (1)--(3), and using `q-1>=0`,

    B-rq-s <= s(r-1)+k(q-1)-U
             <= s(r+q-2)-U
             = s(w-2)-U.                   (4)

The unconditional missing-pair ledger independently gives `epsilon<=U`. If `epsilon>0`, (4) also gives `epsilon<=s(w-2)-U`; adding yields

    2 epsilon <= s(w-2).

If `epsilon=0` the same final bound is automatic. Thus for `q>=1` (and hence `w>=2`),

    epsilon <= floor(s(w-2)/2).             (5)

This is the missing quantitative replacement for the false exact-cancellation inequality.

## Comparison with the density budget

The budgeted cancellation theorem closes the graph whenever `epsilon<=D(u,s)`, where

    D(u,s)=floor((u+s)^2/4)-floor(u^2/4)-s-3.

The floor-difference inequality gives

    D(u,s)-floor(s(w-2)/2)
      >= floor(st/2+s^2/4)-3.

Since `t>=5` and `s>=4`, the final expression is at least `11`. Together with the separately closed `q=0` boundary, this proves `epsilon<=D` in all cases and hence `m<=M(n)`.

## Hostile controls and dependency boundary

The actual `n=33,m=143` RTS control has `epsilon=1`, so exact cancellation is genuinely false; (5) correctly accommodates it. The proof uses only:

1. parity substitution and the unconditional missing-pair ledger;
2. the raw star-centre-spoke `P0` nonneighbour requirement;
3. the star-token injection for low-bridge and star edges;
4. the already proved five-coordinate minimum.

It does not use matching-one, one-tree-component, selected/Hall source-tuple capacity, the rigid one-code cut, or finite SAT extrapolation. The SAT controls are hostile tests, not premises.

## Remaining frontier

The eventual theorem is not proved. The next Q3 frontier is support with five through eight star centres; outside the Q3 antipodal-transversal setting, nontransversal codes also remain. The four-centre classification, however, is now both support-complete and density-closed at its stated scope.
