# Unmatched-slack floor from maximum-degree balance and antipode branching

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not externally reviewed.** This note combines only already-preserved ingredients: the near-full partial Boolean normal form, the no-private-foot corollary, the antipode slack identity, and the antipode branching-error theorem. It does not assume the false all-order 2019 second-extremal conjecture. The order-12/32 `X_3` hostile control lies in `u=0` and is unaffected.

Use the near-full notation

`B=N(v)`, `b=|B|`, `A=V\N[v]`, `a=|A|`, `lambda=2b-n=b-a-1`,

with `p>=2` tight antipode pairs and unmatched set `U`, `|U|=u`. For `y in U`, let `epsilon_y=b-d(y)>=0`, and put

`E_U=sum_{y in U} epsilon_y`.

Every unmatched vertex has an errorful antipode.

---

## 1. Above M(n), a maximum-degree root always has lambda >= -1

This elementary balance fact is useful because it fixes the sign in every unmatched antipode slack equation.

Assume

`m > M(n)=floor((n-1)^2/4)+1`.

Since `m` is integral, `m>=M(n)+1`, and the maximum degree satisfies

`b=Delta(G)>=ceil(2m/n)`.

If `n=2t`, then

`M(n)=t^2-t+1`,

so

`2m/n = m/t >= t-1+2/t > t-1`,

and therefore `b>=t=n/2`.

If `n=2t+1`, then

`M(n)=t^2+1`,

and

`2m/n >= 2(t^2+2)/(2t+1) > t-1`,

so `b>=t=floor(n/2)`.

Hence:

> **MAX-DEGREE BALANCE LEMMA.** Every graph above `M(n)` satisfies, at a maximum-degree root,
>
> `b>=floor(n/2)` and therefore `lambda=2b-n>=-1`.       (1.1)
>
> If `n` is even, in fact `lambda>=0`.

No D2C property is needed for this lemma.

---

## 2. The branching theorem applies to any chosen subset of partners

The proof of the preserved antipode branching-error theorem is local to a fixed centre `w` and a set of its antipode partners. Nothing requires taking **all** partners.

Thus if `S` is any subset of antipode partners of `w`, `d=|S|`, and

`E(w,S)=sum_{y in S} eta(yw)`,

then the same nonedge-count plus critical-edge injection gives

> `3 E(w,S) >= d(d-1)`.                                (2.1)

This subset form is what is needed to price only zero-slack unmatched partners of one antipode hub.

---

## 3. Zero-slack unmatched vertices must be paid by positive-slack U hubs

Let

`Z={y in U:epsilon_y=0}`,

`R=U\Z`.

A vertex `y in Z` cannot have a matched antipode. Indeed, if `q in P` is antipodal to `y` and `q'` is the tight mate of `q`, the preserved exact formula says

`eta(yq)=epsilon_y-epsilon_q'<=0`,

contradicting the fact that every antipode incident with an unmatched vertex is errorful.

Therefore every `y in Z` has at least one antipode partner `z in U`. For such an edge the slack identity gives

`eta(yz)=epsilon_z-(lambda+1)`.                         (3.1)

Since `eta>=1` and `lambda>=-1`, the partner `z` necessarily lies in `R`.

Choose one such positive-slack partner for every zero-slack vertex. For a used hub `z in R`, let `d_z` be the number of zero-slack vertices assigned to it. Applying the subset branching inequality to precisely those assigned partners gives

`3 d_z (epsilon_z-lambda-1) >= d_z(d_z-1)`.

If `d_z>0`, then

> `d_z <= 3(epsilon_z-lambda-1)+1`.                    (3.2)

This is an explicit domination-capacity bound: one positive-slack antipode hub can cover only linearly many zero-slack unmatched vertices, and the coefficient is forced by D2C edge criticality.

---

## 4. A universal lower bound on total unmatched slack

### Odd-balance endpoint: lambda = -1

Equation (3.2) becomes

`d_z<=3 epsilon_z+1`.

Let `H subseteq R` be the used positive hubs. Summing over them,

`|Z| <= 3 sum_{z in H} epsilon_z + |H|`

and `|H|<=sum_{z in H}epsilon_z`. Hence

`|Z|<=4 sum_{z in H}epsilon_z<=4E_U`.

Also every vertex of `R` has positive integral slack, so

`|R|<=E_U`.

Therefore

> **UNMATCHED-SLACK FLOOR, lambda=-1.**
>
> `E_U >= ceil(u/5)`.                                  (4.1)

### Nonnegative balance: lambda >= 0

If `Z` is empty, every unmatched vertex has positive integral slack and simply

`E_U>=u`.

Suppose `Z` is nonempty. For a used hub, (3.2) is

`d_z<=3 epsilon_z-3lambda-2`.

Writing `H` for the used hubs and separating the unused positive vertices gives

`u=|Z|+|R|`

` <= 3 sum_{H}epsilon_z-(3lambda+2)|H| + |H| + |R\H|`

` <= 3E_U-(3lambda+1)|H|`.

Because `Z` is nonempty, `|H|>=1`. Thus

> **UNMATCHED-SLACK FLOOR, lambda>=0.** If at least one unmatched vertex has zero slack, then
>
> `E_U >= ceil((u+3lambda+1)/3)`.                       (4.2)
>
> If no unmatched vertex has zero slack, then `E_U>=u`.

In particular the coarse unconditional form is

> `E_U >= ceil(u/3)` for `lambda>=0`.                   (4.3)

The sharper dichotomy (4.2) should be retained when `lambda` itself is useful.

---

## 5. These constants are sharp for the currently used abstract ingredients

The bounds cannot be improved from only the antipode slack identity, errorfulness, and the branching theorem.

Take the abstract antipode graph `K_{1,4}` on five unmatched vertices, with four zero-slack leaves.

- For `lambda=-1`, give the centre slack `1`. Every star edge then has `eta=1`, and the centre satisfies branching equality

  `3*(4*1)=4*3`.

  Here `u=5`, `E_U=1`, attaining (4.1).

- For any `lambda>=0`, give the centre slack `lambda+2`. Again every star edge has `eta=1` and branching equality. Then

  `u=5`, `E_U=lambda+2`

  and

  `ceil((u+3lambda+1)/3)=lambda+2`,

  attaining (4.2).

This is the same abstract `K_{1,4}` obstruction already preserved in `ANTIPODE_WEIGHTED_MATCHING_OBSTRUCTION.md`. No such configuration was seen in the D2C graph-atlas scan through order seven. The new calculation shows exactly what extra structure is required to improve the constants: **the Boolean unmatched-row constraints must rule out or price these concentrated complementary-code hubs.**

---

## 6. Interaction with the exact near-full ledger

Let

`bar q=binom(u,2)-e(G[U])`

be the number of nonedges inside `U`. The exact unmatched-slack identity from the near-full normal form is

> `E_U = pu + 2 bar q - s`,                             (6.1)

where `s=e(A,U)`.

The companion row-capacity note proves

`E_U <= 2 bar q + W_alpha`,                            (6.2)

where

`W_alpha=sum_{q in P} n_{alpha(q)}`

is the selected/Hall alpha weight.

Thus every above-`M(n)` near-full candidate must simultaneously satisfy the branching lower floor

- `E_U>=ceil(u/5)` when `lambda=-1`,
- the sharper dichotomy (4.2) when `lambda>=0`,

and the row-capacity upper payment (6.2).

The remaining gap is now concrete. Concentrated antipode stars are the sharp obstruction to improving the branching floor, while the row-kernel theorem and beta-pool disjointness are precisely the additional structures available to price those stars.

The next structural target should therefore combine a **complementary-code antipode hub** with its row covers and per-source capacities, rather than seeking a stronger ABE-only matching lemma.
