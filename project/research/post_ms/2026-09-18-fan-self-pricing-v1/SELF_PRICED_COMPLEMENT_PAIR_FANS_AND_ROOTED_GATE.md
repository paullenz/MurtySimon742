# Self-priced complementary-pair fans and a rooted-transfer gate

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large second-extremal D2C programme. No global eventual theorem is claimed.

## 1. Why this move

The live fan-packing frontier left one explicit escape in the A/U branch: the supporting complementary Boolean-code pair could have a large population

`M_P=max(N_c,N_bar(c))`,

which weakens the pair fan floor

`d(2d-T-1) <= (1+2M_P/(lambda+1)) S_P`.                 `(PFC3)`

That escape had already been priced earlier by the same-code crowding theorem, but the two theorem packages had not been composed. This note performs that composition. The result is a pair-local fan cost with **no free code-population parameter**, and hence a distribution-free fan-packing theorem.

The published order-12, size-32 `X_3` graph remains a mandatory hostile control. At its canonical root `u=0` and `F_min=0`, so no positive rooted fan is forced.

## 2. Preserved input

Use the live notation

- `P=p+u`;
- `a=2p+u-lambda-1`;
- `V_0=a+u=2p+2u-lambda-1`;
- `T=P-lambda-1=a-p`;
- `L=lambda+1>0`;
- `S=E_U+L_A`.

For a Boolean code `c`, put

`N_c=|(A union U)_c|`,

`n_c=|A_c|`,

`w_c=N_c+n_c=2n_c+t_c`,

`S_c=sum_{z:c(z)=c} epsilon_z`.

For an unordered complementary pair `Pi={c,bar c}`, put

`S_Pi=S_c+S_bar(c)`,

`M_Pi=max(N_c,N_bar(c))`.

The preserved aligned-code self-pricing theorem says, with

> `D_0=T+2V_0+1=5p+5u-3lambda-2`,                        `(AC0)`

that every code satisfies

> `S_c >= [(w_c/2)(3w_c/2-D_0)]_+`.                      `(AC1)`

The preserved complementary-pair fan theorem says that an A/U fan of order `d` supported on `Pi` satisfies

> `d(2d-T-1) <= (1+2M_Pi/L) S_Pi`.                       `(PFC3)`

## 3. Local code concentration is paid by the same pair

For an integer slack budget `s>=0`, define

> `R_code(s)=floor((D_0+sqrt(D_0^2+12s))/3)`.             `(RC)`

When the right-hand expression is negative, replace it by `0`; in the live parameter range the nonnegative convention is harmless.

### Lemma 3.1 — pair-local aligned-code cap

If `S_Pi=s`, then

> `M_Pi <= R_code(s)`.                                    `(PLC)`

### Proof

Since `S_c<=S_Pi=s` and `S_bar(c)<=S_Pi=s`, `(AC1)` applies separately to both code classes. The positive root of

`(w/2)(3w/2-D_0)=s`

is exactly

`(D_0+sqrt(D_0^2+12s))/3`.

Thus

`w_c,w_bar(c)<=R_code(s)`.

Since `N_c<=w_c` and `N_bar(c)<=w_bar(c)`, `(PLC)` follows. square

The important point is locality: a pair cannot invoke code concentration to make its fan cheap without paying for that concentration from **the same pair slack `S_Pi`**.

## 4. Self-priced complementary-pair fan theorem

Define the nondecreasing integer function

> `Psi(s)=s(1+2R_code(s)/L)`.                             `(SP0)`

### Theorem 4.1 — self-priced fan inequality

Every A/U fan of order `d` supported on a complementary pair `Pi` satisfies

> `d(2d-T-1) <= Psi(S_Pi)`.                               `(SPF)`

### Proof

Apply `(PFC3)` and then Lemma 3.1:

`d(2d-T-1)`

`<= (1+2M_Pi/L)S_Pi`

`<= (1+2R_code(S_Pi)/L)S_Pi`

`=Psi(S_Pi)`.

square

This removes the previous structural alternative “or `M_Pi` is large”. Large `M_Pi` is not free; it is already part of the pair's own slack bill.

### Definition 4.2 — exact self-priced fan cost

For integer `d>=0`, put

> `C_pair(d)=min{s>=0 : d(2d-T-1)<=Psi(s)}`.              `(SPC)`

If `d(2d-T-1)<=0`, set `C_pair(d)=0`.

Then every A/U fan of order `d` satisfies

> `S_Pi>=C_pair(d)`.                                      `(SPC2)`

The definition is finite and monotone and is preferable in exact arithmetic. It has no optimization variable from the code distribution.

## 5. Continuous reviewer-facing form

Put

> `R_bar(s)=(D_0+sqrt(D_0^2+12s))/3`.                    `(RB)`

Since `R_code(s)<=R_bar(s)`, every fan necessarily satisfies the slightly weaker but floor-free inequality

> `d(2d-T-1)`
> ` <= s(1+2R_bar(s)/L)`,                                 `(SPF-real)`

with `s=S_Pi`.

Writing `y=R_bar(s)`, the relation between `s` and `y` is

> `s=y(3y-2D_0)/4`.                                      `(Y1)`

Thus the floor-free fan condition is equivalent to

> `4L d(2d-T-1)`
> ` <= y(3y-2D_0)(L+2y)`.                                `(Y2)`

This cubic normal form is useful for asymptotic analysis; the integer definition `(SPC)` is stronger and should be used for finite certification.

## 6. Distribution-free packing

Choose at most one A/U fan from each of distinct complementary pairs `Pi_j`, with fan orders `d_j`. The pair slacks are disjoint, so

`sum_j S_Pi_j<=S`.

### Theorem 6.1 — self-priced fan packing

> `sum_j C_pair(d_j) <= S`.                               `(SPP)`

### Proof

Apply `(SPC2)` pair by pair and sum. square

This strictly improves the *distribution-free* use of the earlier packing theorem. The old `(PFP)` is sharper if the actual `M_Pi` are retained, but once one wants to eliminate code-population variables, the correct cost is `(SPC)`, not the substitution of one global worst-case code cap into every pair.

### Corollary 6.2 — global one-fan cap above `M(n)`

Above `M(n)` put

> `D_M=b(n-b)-M(n)`,
>
> `C_0=2(D_M-1)+lambda(p+u)-p`.                           `(C0)`

Then `S<=C_0`. Define

> `R_0=R_code(C_0)`.                                      `(R0)`

Every A/U fan obeys

> `d(2d-T-1) <= C_0(1+2R_0/L)`.                          `(GF1)`

Hence

> `d <= floor((T+1+sqrt((T+1)^2+8C_0(1+2R_0/L)))/4)`.    `(GF2)`

The preserved coarse fan slack threshold

> `S>=2d(d-T)_+`                                         `(AUFS)`

may be intersected with `(GF2)`; the smaller cap should be used.

## 7. Rooted-transfer gate with the code escape removed

The rooted-triangle transfer theorem gives, for every above-`M(n)` candidate,

> `f>=F_min=(p-lambda)(p+u)+q-D_M+1`.                    `(FMIN)`

Matched-B traffic satisfies

> `P_B<=sigma_0 a`.

Put

> `H=(F_min-sigma_0 a)_+`.                               `(H)`

The preserved fan gate says that at least one of the following exists:

1. a direct fan of order at least `ceil(H/a)`;
2. an A/U fan of order at least `ceil(H/(2a))`.

The direct fan theorem gives

> `L_A>=d(d-T)_+`.                                       `(DFS)`

The A/U branch now has the self-priced cost `(SPC2)` in addition to `(AUFS)`.

### Theorem 7.1 — two-fan rooted closure criterion

Define

> `d_D=ceil(H/a)`,
>
> `d_C=ceil(H/(2a))`.                                    `(RG0)`

If simultaneously

> `d_D(d_D-T)_+ > L_A`                                   `(RG-D)`

and

> `max(2d_C(d_C-T)_+, C_pair(d_C)) > S`,                 `(RG-C)`

then the assumed above-`M(n)` candidate cannot exist.

Equivalently, every above-threshold candidate must leave at least one of the direct or A/U fan branches feasible under its **actual** slack distribution.

### Corollary 7.2 — parameter-only version

Using

> `sigma_0<=R_A(C_0)`,
>
> `R_A(C_0)=max(2,floor((1+sqrt(1+4C_0))/2))`,            `(RA)`

put

> `H_0=(F_min-aR_A(C_0))_+`.                             `(H0)`

Then the same contradiction follows if

> `ceil(H_0/a)(ceil(H_0/a)-T)_+ > C_0`                   `(PRG-D)`

and

> `max(2d_0(d_0-T)_+, C_pair(d_0)) > C_0`,               `(PRG-C)`

where `d_0=ceil(H_0/(2a))`.

This is deliberately a sufficient closure test, not a claim that it closes all parameters. Its value is conceptual: the current A/U “large code class” alternative has disappeared, so the rooted gate now ends in two explicit finite stability models only.

## 8. Rooted `q` ceiling

Let

`R_D(T,L_A)=floor((T+sqrt(T^2+4L_A))/2)`

be the direct-fan cap, and let

> `R_AU^*(S)=max{d>=0:max(2d(d-T)_+,C_pair(d))<=S}`.      `(RAU*)`

The fan gate implies

> `H <= max(aR_D(T,L_A), 2aR_AU^*(S))`.                  `(QG1)`

Substituting `(H)` and `(FMIN)` gives the exact necessary bound

> `q <= sigma_0 a`
> `     +max(aR_D(T,L_A),2aR_AU^*(S))`
> `     -(p-lambda)(p+u)+D_M-1`.                         `(QG2)`

This is a new fan-derived ceiling on the rooted internal unmatched-edge count `q=e(G[U])`. It should be intersected with the independent beta-sensitive cap

> `q<=au-B_beta+N_1`.                                    `(BQ)`

The significance is that rooted triangle transfer and code-pair fan stability now constrain the same `q` that appears in

`Q=p(p+u-1)+q`

and

`delta=E_U+Q-f-lambda(p+u)+p`.

## 9. Scope and negative control

- `(PLC)--(SPP)` are exact consequences of the preserved aligned-code self-pricing theorem and complementary-pair fan theorem.
- `(RG-D)/(RG-C)` are exact consequences of the preserved rooted fan gate.
- `(QG2)` is only a necessary ceiling under the above-`M(n)` assumption; it is not by itself a residual theorem.
- The parameter-only corollary may be substantially weaker than the actual-slack version and should not replace code-local information when that information is available.
- `X_3` remains untouched: its canonical root has `u=0`, `F_min=0`, hence `H=0`.
- No all-order strengthening is asserted.

## 10. Research consequence

The next A/U step is no longer “control a large code class”. That variable is now self-priced and eliminated. The live alternatives are:

1. **A/U:** use `(SPC)/(SPP)` together with the source-tuple/beta restrictions to force enough pair cost, or combine `(QG2)` with the beta-sensitive `q` ceiling and residual identities;
2. **direct:** attack the false-twin equality/stability model.

The second branch is treated in the companion note `FALSE_TWIN_PRIVATE_SUPPORT_AND_BIPARTITE_STABILITY.md`.
