# One-code near-rigid cut — zero/unit rooted-gap finite-order closure

Date: 2026-09-20

Status: **same-session analytic consequence** of `ONE_CODE_NEAR_RIGID_WITNESS_CLASS_CROWDING.md` and the previously audited one-code rigid machinery. This is conditional on reaching the exact rigid Hall interface. It is not a graph-level reachability theorem; the bounded graph regression still has no positive rigid fixture with `x>=3`.

This note records two useful consequences of keeping the rooted gap

`c=lambda+1-g0`, `g0=p-y`,

physical. The c=0 case collapses to six tiny score-feasible parameter tuples. The c=1 case has only two possible matched/U splits for a minimum source, and an elementary averaged form of the new witness-class slack bound proves finite order without a scan.

## 1. c=0 recap

The companion witness-class theorem proves, for p>=3 and c=0,

- `u=x-p`;
- a minimum source uses every U vertex as a complementary singleton X-witness;
- `Y` is independent and anticomplete to U;
- `G[U]` is independent by same-code criticality;
- `E_U=u(p+u-2)`;
- all p matched singleton resources are used, so `g_P=p` and `L_A>=p(p-1)`.

Comparing

`u(p+u-2)+p(p-1)`

with the exact above-M score ceiling C0 leaves only

`lambda=p-2`,

`(p,u) in {(3,0),(3,1),(3,2),(4,0),(4,1),(4,2)}`,

hence `n<=18`.

The rest of this note treats c=1.

## 2. c=1 leaves exactly two minimum-source witness splits

Assume

> `c=1`.

Then

`lambda=g0`, `y=p-lambda>=1`,

and the rooted size identity gives

> `u=x-p+1`.                                              `(SG1)`

For a source with minimum U-witness count k, the distinct-head theorem gives

`k>=x-p=u-1`,

while trivially `k<=u`. Thus exactly two values are possible:

### Branch A — one escaping U vertex

`k=u-1`,

`m=x-k=p` matched-covered heads.                         `(SG-A)`

### Branch B — no escaping U vertex

`k=u`,

`m=x-k=p-1` matched-covered heads.                       `(SG-B)`

This is already a strong structural normalization: the minimum source uses either all U vertices or all but one.

## 3. Branch score floors

Write

`E_base(k)=k(p-1)`

for the preserved all-source witness-incidence U-slack floor, and

`E_same(k)=k(g0+k-1)-2(y-1)(k-1)`

for the new same-code witness-class degree/certificate floor. Then

> `E_U>=max{E_base(k),E_same(k)}`.                         `(SG-E)`

The matched-covered heads force the gamma collision floor `phi(m)=m(m-1)` when `m>=3`. We deliberately do **not** use the additional Hamming-slot floor in the analytic estimates below, so the conclusions remain true a fortiori when it is restored.

For p>=4, both branch collision prices are in their quadratic regime. Hence

### Branch A

> `S:=E_U+L_A`
> ` >= max{(u-1)(p-1),`
> `         (u-1)(lambda+u-2)-2(y-1)(u-2)}`
> `    +p(p-1)`.                                         `(SG-SA)`

### Branch B

> `S`
> ` >= max{u(p-1),`
> `         u(lambda+u-1)-2(y-1)(u-1)}`
> `    +(p-1)(p-2)`.                                     `(SG-SB)`

The only input beyond the predecessor one-code interface is the new W-class crowding floor.

## 4. Average the two U-slack mechanisms

For real numbers A,B, `max(A,B)>=(A+B)/2`. Apply this only to the two U-slack terms in `(SG-SA)/(SG-SB)`.

The exact above-M score ceiling can be written

> `C0=(lambda+3)p+(lambda+2)u-A_lambda`,                  `(SG-C0)`

where

> `A_lambda=floor(lambda^2/2)+lambda+4+(lambda mod 2)`.   `(SG-AL)`

In particular

> `2A_lambda>=lambda^2+2lambda+8`.                        `(SG-AL2)`

Put `y=p-lambda`. Twice the difference between the averaged branch floor and C0 is:

### Branch B

> `D_B`
> `=2A_lambda+2lambda y-12lambda`
> `  +u^2-u y-4u+2y^2-10y+2`.                            `(SG-DB)`

### Branch A

> `D_A`
> `=2A_lambda+2lambda y-10lambda`
> `  +u^2-u y-6u+2y^2-5y-1`.                             `(SG-DA)`

Any survivor in the corresponding branch requires `D_A<=0` or `D_B<=0` respectively.

## 5. Analytic exclusion for p>=10

Using `(SG-AL2)` and minimizing the quadratic in u over the reals gives

> `D_B >= [4p(p-10)+3y^2-8y+24]/4`,                      `(SG-B10)`

and

> `D_A >= [4p(p-8)+3y^2-8]/4`.                           `(SG-A10)`

For every `p>=10`, `y>=1`, both right sides are strictly positive:

- `3y^2-8y+24>0` for all real y;
- `4p(p-8)>=80`, while `3y^2-8>=-5` for y>=1.

Therefore:

> **`c=1` and `p>=10` are impossible above M(n) in the one-code rigid near-rigid branch.** `(SG-P)`

This is an analytic exclusion, not a bounded search.

## 6. For 4<=p<=9, u>=8 is impossible

For `u>=8` and `1<=y<=p-1<=8`, the u-derivatives of the lower quadratic forms are positive:

`2u-y-4>0` in Branch B,

`2u-y-6>0` in Branch A.

So it suffices to evaluate the lower bounds at u=8. Using `(SG-AL2)` gives

> `D_B(8) >= p^2-10p+y^2-8y+42`,                         `(SG-B8)`

> `D_A(8) >= p^2-8p+y^2-5y+23`.                          `(SG-A8)`

For integer y,

`y^2-8y>=(y-4)^2-16>=-16`,

so

`D_B(8)>=p^2-10p+26>0`

for every `4<=p<=9`.

Likewise `y^2-5y>=-6` for integer y, so

`D_A(8)>=p^2-8p+17>0`

for every `4<=p<=9`.

Therefore

> **if `4<=p<=9` and c=1, then `u<=7`.**                  `(SG-U)`

## 7. The p=3 tail

Here `lambda in {1,2}`. The Branch-B matched collision term has `m=2` and hence phi=0, so it is safer to check the two exact lambda values directly rather than reuse the p>=4 formula.

### lambda=1, y=2

`C0=6+3u`.

Branch A has

`S>=u^2-4u+11`,

and Branch B has

`S>=u^2-2u+2`.

Both exceed C0 for `u>=7`.

### lambda=2, y=1

`C0=7+4u`.

Branch A has

`S>=u^2-u+6`,

and Branch B has

`S>=u(u+1)`.

Again both exceed C0 for `u>=7`.

Thus p=3 also satisfies `u<=6`, in particular `u<=7`.

## 8. Unit-gap finite-order theorem

Combining the preceding sections:

> **Unit-gap theorem.** For p>=3, any above-M(n) graph reaching the one-code rigid near-rigid interface with
>
> `c=lambda+1-g0=1`
>
> must satisfy
>
> **`p<=9`, `u<=7`.**                                     `(SG-FIN)`

Since `lambda=g0>=1` and `n=4p+2u-lambda`,

> **`n<=49`.**                                            `(SG-N)`

The bound 49 is deliberately analytic and conservative. A bounded arithmetic diagnostic using the full max/slot floor is smaller, but that diagnostic is not used as proof.

Together with the c=0 theorem:

> **every one-code rigid near-rigid survivor with c<=1 has order at most 49.** `(SG-01)`

## 9. Trust boundary and next step

This note assumes the exact rigid Hall interface and the independently audited one-code singleton-witness localization. The new proof uses only:

- the witness-class same-code crowding theorem;
- the preserved all-source U-slack floor;
- the preserved gamma-collision floor;
- the exact above-M score ceiling.

No finite scan enters `(SG-P)`, `(SG-U)` or `(SG-N)`.

The natural continuation is `c>=2`. The minimum source still uses all but at most c U vertices, so the same W-class theorem gives a quadratic U-slack price. Rather than attack each c separately, the next objective should be an analytic **gap-versus-order dichotomy**: either c is small relative to the witness class and the quadratic W bill closes the branch, or c itself is large enough to be charged through exact pair-local `Ccap_P/(ONE-P)/(CROWD)` and the rooted residual identity.

`X_3` remains a mandatory negative control and is not in these c=0 or c=1 rigid one-code regimes.