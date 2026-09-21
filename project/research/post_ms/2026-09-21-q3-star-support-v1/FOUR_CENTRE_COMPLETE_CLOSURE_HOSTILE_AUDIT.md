# Hostile audit of the exactly-four-centre density closure

21 September 2026. Independent re-derivation from the raw certificate calculus.

## Verdict

The proof in `FOUR_CENTRE_COMPLETE_DENSITY_CLOSURE.md` survives targeted hostile review at its stated Q3 antipodal-transversal scope. One written sign boundary at `q=0` was found and repaired by separating that case. No selected/Hall premise, matching-one assertion, finite-grid extrapolation or fourth-pair assumption is used.

## Load-bearing input 1: every star misses a P0 vertex

Take a star vertex `x` of even centre `c` and delete its centre spoke `xc`. Re-run the four exhaustive raw spoke-certificate cases.

1. The endpoint pair `(x,c)` retains length two through the three cube neighbours of `c` already in the star code.
2. There is no cube neighbour of `c` outside the star code.
3. A third A-vertex code meeting `S_c` exactly in `c` must be `P0`; the raw certificate also requires this physical vertex to be nonadjacent to `x`.
4. A reverse B-end target would require the code disjoint from `S_c`, namely the absent odd-centred star `S_bar(c)`.

Thus case 3 is forced. Every physical star has a physical `P0` nonneighbour, proving `e(R,S)<=s(r-1)`. This is a per-vertex statement and does not infer physical uniqueness between different stars.

## Load-bearing input 2: `L+k<=s`

A low-bridge `T--S` edge is incident with a star of total bridge degree one. Every `S--S` edge has a star endpoint of total bridge degree one by the star-forest proof. Assign each bucket edge to such a degree-one endpoint. No star can receive two assignments because its total bridge degree is one. No high-bridge star can receive any assignment. Hence the `L` bucket edges and the `k` high stars occupy disjoint physical star tokens, proving `L+k<=s`.

This is physical-token injection, not a centre-count argument.

## Algebra replay

For `q>=1`, exact partitioning gives

    B-rq-s=A+T_H+L-U-s.

Insert `A<=s(r-1)`, `T_H<=kq`, and `L+k<=s`:

    B-rq-s <= s(r-1)+k(q-1)-U
             <= s(r+q-2)-U.

Together with the independent ledger `epsilon<=U`, positive excess satisfies

    2 epsilon <= s(r+q-2).

For `q=0`, the intermediate comparison `k(q-1)<=s(q-1)` would reverse direction. The corrected proof instead observes `U=0`, whence `e(R,S)=0`, and uses the star forest to get `epsilon=0` directly.

The exact floor comparison was replayed over

    5<=t<=80, 1<=r<=80, 0<=q<=80, 4<=s<=40.

The minimum `D-floor(s(w-2)/2)` for `w>=2` is 11, attained first at `(t,r,q,s)=(5,1,1,4)`. The `q=0` boundary is already exact-closed. The scan audits arithmetic only; the displayed inequalities are the proof.

## Actual hostile controls

The saved `n=33` RTS graph has `U=4`, `B=21`, `epsilon=1`, and symmetric cap 24. The `n=34` fourth-pair-missing graph has `U=6`, `B=22`, `epsilon=0`, and cap 30. Both pass direct D2C replay. The first is particularly important because it falsifies exact cancellation while satisfying the repaired theorem.

## Scope boundary

The audit verifies the complete density closure only after the prior support theorem has reduced exactly four centres to a parity plane. It says nothing about five through eight star centres, nontransversal outside codes, or the global eventual theorem. External mathematical review remains required.
