# Rigid one-code cuts with at least two matched-selected heads: full boundary exposure

Date: 2026-09-21

Status: raw realizability theorem inside the rigid complete one-code interface. It generalizes the residual-one population obstruction to arbitrary residual matched-coordinate dimension and uses only the post-audit boundary trichotomy plus the global matched-leaf collapse.

## 1. Setup

Let `Y=A_d` be the one-code outside block of a rigid complete cut. Suppose at least two X-heads are supplied by distinct tight matched coordinates. Write the selected matched-head coordinates as S, `|S|=m>=2`.

For each `i in S`, the corresponding matched-selected head has code

`d xor e_i`.

Let `I(d,X)` and `C(d,X)` be the exposed and universal coordinate sets of the boundary trichotomy.

## 2. Full exposure

### Theorem 2.1

If `m>=2`, then

> **`I(d,X)=[p]`.**                                      `(2.1)`

### Proof

Fix a tight coordinate j.

- If `j notin S`, every matched-selected head `d xor e_i` with `i in S` agrees with d at j.
- If `j in S`, choose another selected coordinate `i in S`, `i!=j` (possible because m>=2). The head `d xor e_i` agrees with d at j.

Thus every coordinate has some X-head agreeing with d, so every coordinate is exposed. `square`

Moreover every selected coordinate is nonuniversal because its own head `d xor e_i` disagrees with d there. Therefore

> **`C(d,X) subseteq [p]\S`, so `|C|<=p-m`.**            `(2.2)`

## 3. Population consequence

The global matched-leaf theorem gives

`|L(d,X)|<=2`.

Let

`rho=max_c |X_c|`

be the largest X-code-class multiplicity.

At a coordinate with no matched-forward support, at most rho Y-heads can reverse-certify because the forced reverse witnesses all lie in one X-code class and fixed-source injectivity makes distinct Y-heads require distinct physical witnesses.

Hence if

> **`y>rho`,**                                            `(3.1)`

then every one of the `p-|L|` nonmatched coordinates requires a U-forward witness. Different coordinates require different one-match U-code classes `bar d xor e_i`. Therefore

> **`p-|L|<=u`.**                                        `(3.2)`

Using `|L|<=2`:

### Corollary 3.1 — full-exposure population obstruction

For every rigid complete one-code cut with `m>=2` and `y>rho`,

> **`p<=u+2`.**                                          `(3.3)`

If `C=empty`, matched-forward support vanishes and this sharpens to

> **`p<=u`.**                                            `(3.4)`

Thus any profile with `m>=2`, `p>u+2`, and no X-code class as large as the outside block is **literally unrealizable** before the Hall/score capacity machinery is consulted.

## 4. Reverse-gamma alternative when y<=rho

When `(3.1)` fails, large reverse classes are unavoidable rather than free. Since full exposure gives `|I|=p`, the exposed-coordinate master bound from `RIGID_CUT_REVERSE_GAMMA_MULTIPLICITY.md` yields

> **`p <= u+2+floor(x/y) G(C0)`.**                       `(4.1)`

More locally, every coordinate not using one of the at most u U-forward one-match classes or the at most two matched leaves is reverse-only and hence must be assigned to an X gamma class of size at least y. Repetition of those gamma classes incurs the preserved gamma-collision A-slack bill.

Consequently a one-code rigid cut with `m>=2` has only two physical boundary regimes:

1. **U-rich:** enough unmatched vertices exist to populate nearly all exposed one-match classes; or
2. **gamma-rich:** X contains code classes of multiplicity at least y and enough repeated gamma capacity to absorb the remaining coordinates, paying collision slack.

There is no third aggregate-capacity escape.

## 5. Relation to residual-one closure

Residual dimension one has `m=p-1>=2`, so full exposure is automatic. In that branch the residual X-code class is the only class with multiplicity above one. This specializes Corollary 3.1 exactly to the residual-one theorem `u<p => y<=k` and closes the intermediate half-ray because `rho=k=2<y=t` while `u=t+1<p=2t`.

## 6. Scope

This is a necessary condition conditional on the rigid complete one-code interface. It does not assert that the interface itself is reachable from an arbitrary D2C graph. Bounded actual-D2C regression still has zero positive rigid complete pair-family cuts with `x>=3`; X_3 remains the mandatory negative control.
