# Combined complementary-pair A-edge channel capacity

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

The published order-12, size-32 graph `X_3` remains a mandatory negative control. No all-order or eventual second-extremal theorem is claimed.

## 1. Reassessment

The current rooted-transfer gate prices the three possible criticality channels for an internal A-edge separately:

1. direct edges;
2. matched-B witnesses;
3. A/U unique-common-neighbour witnesses.

The direct and A/U branches were recently converted into fan stability statements. For the next global synthesis, however, there is a more compact object: an unordered complementary Boolean-code pair. The weighted direct-edge inequality and the weighted A/U capacity have the same slack variables, and adding them before taking maxima removes the need for a free direct-fan radius or a free A/U traffic split.

This note records that composition.

## 2. Notation and preserved inputs

Work in the live partial-Boolean branch. Put

`L=lambda+1`.

For a Boolean code `c`, write

- `n_c=|A_c|`;
- `N_c=|(A union U)_c|`;
- `w_c=N_c+n_c=2n_c+t_c`;
- `L_c=sum_{x in A_c} epsilon_x`;
- `S_c=sum_{z in (A union U)_c} epsilon_z`.

For an unordered complementary pair

`Pi={c,bar(c)}`

put

`L_Pi=L_c+L_bar(c)`,

`S_Pi=S_c+S_bar(c)`.

The preserved aligned-code self-pricing theorem is

> `S_c >= [(w_c/2)(3w_c/2-D_0)]_+`,                      `(AC1)`

where

> `D_0=5p+5u-3lambda-2`.

Consequently, if a complementary pair has total slack `s=S_Pi`, then

> `w_c,w_bar(c) <= R_code(s)`,                            `(AC2)`

where

> `R_code(s)=max(0,floor((D_0+sqrt(D_0^2+12s))/3))`.      `(AC3)`

The preserved weighted A/U capacity is

> `L C_c <= N_bar(c)L_c+n_c S_bar(c)`,                    `(AUC)`

where `C_c` is the chosen A/U certificate traffic whose A-source has code `c`.

Every direct A-edge joins complementary code classes and obeys

> `epsilon_x+epsilon_y >= L`.                             `(DIR0)`

## 3. Direct traffic on one complementary pair

Let `D_Pi` be the number of direct A-edges between `A_c` and `A_bar(c)`.

Summing `(DIR0)` over those edges gives

> `L D_Pi <= n_bar(c)L_c+n_cL_bar(c)`.                    `(DIR1)`

Indeed, each vertex of `A_c` occurs in at most `n_bar(c)` such edges and each vertex of `A_bar(c)` in at most `n_c`.

This is the weighted pair analogue of the local direct-fan slack inequality.

## 4. Combined direct plus A/U pair capacity

Put

`C_Pi=C_c+C_bar(c)`.

Adding `(DIR1)` to `(AUC)` in both directions gives

`L(D_Pi+C_Pi)`

` <= (N_bar(c)+n_bar(c))L_c`

`    +(N_c+n_c)L_bar(c)`

`    +n_c S_bar(c)+n_bar(c)S_c`

and therefore

> `L(D_Pi+C_Pi)`
> ` <= w_bar(c)L_c+w_cL_bar(c)`
> `    +n_cS_bar(c)+n_bar(c)S_c`.                         `(PAIR1)`

Now let

`R=R_code(S_Pi)`.

By `(AC2)`, `w_c,w_bar(c)<=R`. Since

`w_c=2n_c+t_c`,

one also has the useful half-factor

> `n_c,n_bar(c) <= R/2`.                                  `(HALF)`

Substituting these bounds into `(PAIR1)` gives the main pair theorem.

### Theorem 4.1 — combined complementary-pair channel capacity

For every unordered complementary code pair `Pi`,

> `2L(D_Pi+C_Pi)`
> ` <= R_code(S_Pi)(2L_Pi+S_Pi)`.                         `(CCP)`

Equivalently,

> `D_Pi+C_Pi`
> ` <= R_code(S_Pi)(L_Pi+S_Pi/2)/L`.                     `(CCP')`

No direct-fan radius, A/U fan radius, or independent code-population variable appears.

### Structural interpretation

The two non-matched-B channels share the same local resource. A pair can support many direct edges, many A/U certificates, or a mixture of the two only by paying either A-slack `L_Pi` or total pair slack `S_Pi`, and code concentration itself is already priced into `R_code(S_Pi)`.

Thus direct and A/U traffic cannot independently spend the same complementary-code population.

## 5. Global combined channel theorem

Let

`D=sum_Pi D_Pi`,

`C=sum_Pi C_Pi`.

The complementary pairs partition the code space, so

`sum_Pi L_Pi=L_A`,

`sum_Pi S_Pi=S`.

Since `R_code` is nondecreasing and `S_Pi<=S`, summing `(CCP)` gives

### Corollary 5.1 — global direct+A/U capacity

> `2L(D+C) <= R_code(S)(2L_A+S)`.                         `(GCC)`

Equivalently,

> `D+C <= [R_code(S)/L](L_A+S/2)`.                       `(GCC')`

This should replace the old distribution-free practice of separately inserting a direct radius and an A/U radius when only total slack information is retained.

## 6. Add the matched-B channel

The exact A-edge channel decomposition is

> `f=D+C+P_B`.                                             `(CH)`

The preserved matched-B theorem gives

> `P_B<=sigma_0 a`,                                       `(MB1)`

while a switchable zero-signed core of order `sigma_0>=3` gives

> `L_A>=sigma_0(sigma_0-1)`.                              `(MB2)`

Define

> `R_A(L_A)=max(2,floor((1+sqrt(1+4L_A))/2))`.            `(RA)`

Then `sigma_0<=R_A(L_A)` in all cases. Combining this with `(GCC)` yields the complete channel envelope.

### Theorem 6.1 — slack-priced complete A-edge capacity

> `f`
> ` <= a R_A(L_A)`
> `    +[R_code(S)/(2L)](2L_A+S)`.                        `(ACE)`

All three A-edge witness channels are now paid from the actual slack variables. The theorem contains no free channel split.

## 7. Rooted-triangle form

The exact rooted transfer identity is

> `delta+Q=L_A+f`,                                        `(RQ2)`

with

> `Q=p(p+u-1)+q`.

Substituting `(ACE)` gives

### Corollary 7.1 — rooted-triangle capacity

> `delta+Q`
> ` <= L_A+aR_A(L_A)`
> `    +[R_code(S)/(2L)](2L_A+S)`.                        `(RTC)`

Equivalently,

> `q`
> ` <= L_A+aR_A(L_A)`
> `    +[R_code(S)/(2L)](2L_A+S)`
> `    -delta-p(p+u-1)`.                                  `(QCC)`

This is a direct bridge from criticality-channel capacity to the rooted triangle variable.

## 8. Source/Hall-conditioned parameter-only bridge

Above `M(n)`, put

`C_0=2(D_M-1)+lambda(p+u)-p`,

so `S<=C_0`.

Let

> `B_*=max(0,p(lambda+1-2p),pu-R_hat a)`                  `(B*)`

be the preserved beta-load floor, and let `N_sup(B)` be the integrated source-tuple support floor. The preserved support theorem gives

> `E_U`
> ` >= u(p+u-1)-3au+B_*+uN_sup(B_*)-2a`.                 `(SE)`

Define the nonnegative lower bound

> `E_*=max(0,u(p+u-1)-3au+B_*+uN_sup(B_*)-2a)`.           `(E*)`

If `E_*>C_0`, the parameter tuple is already impossible. Otherwise

> `L_A<=L_*:=C_0-E_*`.                                    `(L*)`

Monotonicity in `(ACE)` then gives the finite parameter-only necessary condition

> `f`
> ` <= aR_A(L_*)`
> `   +[R_code(C_0)/(2L)](2L_*+C_0)`.                    `(PACE)`

Combining this with the exact rooted lower bound

> `f>=F_min=(p-lambda)(p+u)+q-D_M+1`                     `(FMIN)`

yields

> `q`
> ` <= aR_A(L_*)`
> `   +[R_code(C_0)/(2L)](2L_*+C_0)`
> `   -(p-lambda)(p+u)+D_M-1`.                            `(PQCC)`

Thus the preserved chain

`source/Hall beta load -> beta support -> E_U floor`

now continues directly as

`-> A-slack ceiling -> complete A-edge channel capacity -> rooted q ceiling`.

This is the compact synthesis that was missing from the previous fan-by-fan frontier.

## 9. Trust boundary and diagnostic outcome

- `(CCP)--(QCC)` are exact consequences of the preserved weighted direct, weighted A/U, aligned-code, matched-B and rooted-transfer theorems.
- `(PACE)/(PQCC)` are deliberately coarser parameter-only consequences; actual `E_U,L_A,S` should be retained whenever possible.
- A diagnostic finite scan shows that this coarse parameter-only collapse does **not** by itself close the generic above-threshold parameter region. That is useful negative information: the structural gain is the shared pair/slack accounting, not a magic one-line numerical contradiction.
- The correct next use is to retain actual slack or combine `(QCC)` with the independent beta-sensitive `q` ceiling.

## 10. Negative control

For the published `X_3` graph, `u=0`, `f=0`, and no positive rooted A-edge demand is forced. The theorem is compatible with `n=12,m=32>M(12)=31`; nothing here asserts an all-order bound.
