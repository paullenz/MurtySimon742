# Matched-foot collision capacity in repeated beta cylinders

**Status:** internal structural theorem, 18 September 2026.

This note continues the scope repair in `CYLINDER_REPEATED_CLASS_WITNESS_LOCALISATION.md`. A repeated beta-cylinder class may use matched-B endpoints as incoming critical feet, but only in deficit coordinates. The results below show that these exceptional feet have a **globally bounded reuse capacity**: each matched endpoint accepts sources of one uniquely determined Boolean code, and collisions of those source codes are themselves switchable zero-signed subcores.

Thus the matched-foot escape is not merely bounded by `k_x` locally; its total multiplicity across all low-deficit centres is controlled by the already-priced switching-stability parameter.

The order-12 `X_3` hostile control has `u=0` and is unaffected.

## 1. Sign convention and the source code of a matched foot

Write the tight fibres as

`P_i={q_i^0,q_i^1}`, `i=1,...,p`.

For `i!=j`, let `sigma_ij in {0,1}` be the 2-lift sign, so

`q_i^s q_j^{s xor sigma_ij}`

is a physical B-edge.

Fix a matched endpoint

`w=q_i^s`.

Define its **row-complement source code** `gamma(w) in {0,1}^p` by

`gamma(w)_i=1-s`,

and, for `j!=i`,

`gamma(w)_j=1-s-sigma_ij  (mod 2)`.

Equivalently, `gamma(w)` chooses the endpoint opposite every matched-B neighbour of `w`, and chooses the mate of `w` in its own fibre.

### Lemma 1.1 (unique source code of a matched incoming foot)

Suppose `z in A` and a matched endpoint `w=q_i^s` satisfy

> `N(z) cap N(w)={x}`

for some `x in A`.

Then

> `c(z)=gamma(w)`.                                        `(MF1)`

### Proof

The source `z` is nonadjacent to `w`, so in fibre `i` it chooses `q_i^{1-s}`. For every `j!=i`, if `z` chose the same endpoint of `P_j` as the matched-B neighbour of `w`, that endpoint would be a second common neighbour of `z` and `w`. Hence `z` chooses the opposite endpoint in every other fibre. This is exactly `gamma(w)`.

### Lemma 1.2 (one source gives at most one centre for a fixed foot)

Fix `z` and `w`. If `N(z) cap N(w)` is a singleton, its member is uniquely determined. Therefore a fixed matched foot `w` can certify at most one incoming cylinder edge for any given source `z`.

Consequently, if `t_w` is the total number of incoming repeated-cylinder certifications using `w`, then

> `t_w<=n_{gamma(w)}`,                                    `(MF2)`

where `n_c` is the number of A-vertices of Boolean code `c`.

---

## 2. Colliding foot-source codes are a zero-signed subcore

The map `w -> gamma(w)` can collide across fibres, but such collisions are highly structured.

### Lemma 2.1 (collision equation)

Let

`w_i=q_i^{s_i}` and `w_j=q_j^{s_j}`

lie in distinct fibres. Then

> `gamma(w_i)=gamma(w_j)`

implies

> `sigma_ij=s_i xor s_j`,                                 `(MF3)`

and, for every `k` distinct from `i,j`,

> `sigma_ik xor sigma_jk=sigma_ij`.                       `(MF4)`

### Proof

Compare the two codes in coordinate `i`:

`1-s_i = 1-s_j-sigma_ji (mod 2)`,

which is `(MF3)`. Comparison in every third coordinate gives `(MF4)`.

### Theorem 2.2 (gamma-collision classes are switchable zero-signed subcores)

Suppose matched endpoints

`w_i=q_i^{s_i}`, `i in I`,

all have one common code `gamma`. Then switching fibre `i` by `s_i` makes every edge among the fibres in `I` parallel. Equivalently, the induced sign graph on `I` becomes zero-signed.

### Proof

For each pair `i,j in I`, `(MF3)` gives

`sigma_ij=s_i xor s_j`.

After switching by the bit vector `(s_i)`, the new sign is

`sigma'_ij=sigma_ij xor s_i xor s_j=0`.

### Corollary 2.3 (collision multiplicity cap)

Let

`mu_gamma=max_c |{w:gamma(w)=c}|`.

If `sigma_0` is the largest switchable zero-signed tight-fibre subcore from the live switching-stability theorem, then

> `mu_gamma<=sigma_0<=R_*`.                               `(MF5)`

The last inequality is the preserved scorecard consequence of `(ZS)/(SD)`.

There is also a useful fibre symmetry:

### Lemma 2.4 (opposite endpoints give complementary source codes)

For every tight fibre,

> `gamma(q_i^1)=bar gamma(q_i^0)`.                        `(MF6)`

This follows immediately from the definition.

---

## 3. Global capacity of all exceptional matched feet

Let `M_P` be the total number of incoming cylinder-edge certifications that use a matched-B foot, counted with multiplicity over all centres and all repeated classes. Then by `(MF2)` and `(MF5)`,

`M_P=sum_w t_w`

`<=sum_w n_{gamma(w)}`

`=sum_c n_c |{w:gamma(w)=c}|`

`<=mu_gamma sum_c n_c`.

Since `sum_c n_c=a`, we obtain:

### Theorem 3.1 (global matched-foot capacity)

> `M_P<=sigma_0 a<=R_* a`.                               `(MFC)`

This is the desired aggregate complement to the local bound `|I_P|<=k_x` from the repaired cylinder theorem.

In the common near-full regime where the scorecard gives `R_*=O(sqrt p)` and `a=O(p)`, all exceptional matched-foot certifications together are only

> `M_P=O(p^{3/2})`.

Thus a genuinely quadratic population of repeated-cylinder critical edges cannot hide in matched-B feet.

---

## 4. Slack-weighted matched-foot capacity

The unique-common-neighbour slack inequality also prices matched-foot reuse whenever the foot itself does not carry all endpoint slack.

For one use `(z,w)`,

> `epsilon_z+epsilon_w>=lambda+1`.                        `(MF7)`

Hence

> `epsilon_z >= (lambda+1-epsilon_w)_+`.

Summing over all uses of `w`, and then over all matched feet, counts any A-source `z` at most `mu_gamma` times because all feet using it must have `gamma(w)=c(z)`. Therefore:

### Theorem 4.1 (weighted foot-slack payment)

> `sum_w t_w (lambda+1-epsilon_w)_+`
>
> `<=mu_gamma L_A<=sigma_0 L_A`.                          `(MFS)`

For a tight fibre `P_i={q_i^0,q_i^1}`, the preserved endpoint-slack identity is

`epsilon_{q_i^0}+epsilon_{q_i^1}=lambda+1`.

Thus `(MFS)` has the especially clean paired form

> `sum_i [t_i^0 epsilon_i^1+t_i^1 epsilon_i^0]`
>
> `<=sigma_0 L_A`,                                        `(MFSP)`

where `t_i^s=t_{q_i^s}` and `epsilon_i^s=epsilon_{q_i^s}`.

This is structurally the same cross-slack form that appears in the preserved alpha--beta endpoint payment `T_i`.

### Corollary 4.2 (cheap feet have small total load)

For any `0<=eta<lambda+1`, let

`W_eta={w:epsilon_w<=eta}`.

Then

> `sum_{w in W_eta} t_w`
>
> `<=sigma_0 L_A/(lambda+1-eta)`.                         `(MFCHEAP)`

So large matched-foot reuse can occur only on endpoints carrying correspondingly large matched slack; by the fibre sum identity, their mates then have small slack and are expensive if used in the opposite direction.

---

## 5. Combined repeated-cylinder consequence

For a low-deficit centre `x`, the repaired decomposition is

`R_x=O_x dotcup I_{AU,x} dotcup I_{P,x}`,

with

`|I_{P,x}|` locally supported on at most `k_x` matched-foot types.

Summing over any family `X` of centres and choosing one repeated cylinder class `R_x` per centre gives

> `sum_{x in X}|I_{P,x}|<=M_P<=sigma_0 a`.                `(MFFAM)`

Therefore

> `sum_{x in X} (|R_x|-|O_x|-|I_{AU,x}|)`
>
> `<=sigma_0 a`.                                          `(MFFAM2)`

The matched-B escape is now globally capped. Any attempt to produce many large repeated cylinder classes must therefore move a comparable number of critical edges into `O_x` or `I_{AU,x}`, where the A/U complementary-witness scorecard and same-code/common-foot machinery applies.

This is the first aggregate cylinder-capacity theorem that remains valid after correcting the `c_R=c(x)` scope error.

---

## 6. Strategic consequence

The local cylinder obstruction has now been reduced to a quantitative competition between three resources:

1. **matched-foot escape:** globally at most `sigma_0 a`, and more sharply controlled by `(MFS)`;
2. **outgoing A/U witnesses:** pairwise distinct within each repeated class and complementary to the centre code;
3. **incoming A/U witnesses:** complementary to the repeated-class code, with reuse forcing dense same-code source blocks and the common-foot hole/clique payments.

The next useful theorem should combine `(MFFAM)` with the beta-cylinder multiplicity

`|R_x|>=ceil((p-epsilon_x)_+/2^{k_x})`

on the low-deficit population forced by the source-tuple staircase. If the total repeated-class mass exceeds `sigma_0 a`, a definite excess must enter the A/U witness channels. That excess should be convertible into `L_A` through distinct-witness or common-foot capacity.

Unlike the pre-repair cylinder heuristic, this target is now fully compatible with arbitrary repeated class code `c_R`.

## 7. Trust boundary

- `(MF1)--(MF6)` are exact Boolean/2-lift statements.
- `(MFC)` uses only source uniqueness and the preserved zero-signed-subcore scorecard theorem.
- `(MFS)` uses the exact unique-common-neighbour slack inequality and the collision multiplicity cap.
- No assumption is made that a repeated cylinder class has the centre's code.
- No global near-full closure is claimed.
- `X_3` has `u=0` and remains untouched.
