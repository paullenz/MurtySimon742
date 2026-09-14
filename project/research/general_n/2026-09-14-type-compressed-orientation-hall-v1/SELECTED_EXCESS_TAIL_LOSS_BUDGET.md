# Selected-excess tail losses and the exact Hall slack budget

14 September 2026. **New hand derivation with local exact finite verification. External mathematical review and novelty assessment remain OPEN. No new whole-state exclusions are promoted.**

This continues `SUMMED_Q_TAIL_PRESSURE.md` and `BRIDGE_TWO_DEFECT_DECOMPOSITION.md`. It does not assume high-q tails suffice to detect all target-Hall failures. Instead it writes the capacity spent by the selected-excess cap as an exact short sum of high-q tail counts, then couples that expenditure to every Hall cut.

## 1. Hypotheses and notation

Use the current post-pair cap model and its canonical bridge notation. There are b B-vertices, a A-labels, and

```text
k = b-a-1 >= 0,
c_u = q_u + rho_u <= a,
r = sum_u rho_u,
Q = sum_u q_u,
E = Esel >= 0,
z = #{i:s_i=0}.
```

Here E denotes selected excess, NOT the zero-demand bridge deficit D0. The two-defect identity is

```text
Q-r = 2t+D0+E.
```

The cap calculation itself needs only the integer profile and E,z; applying the last identity to a graph inherits the canonical bridge hypotheses. The proof below treats only nonnegative target-cap branches when discussing Hall feasibility. A negative computed cap rejects the branch; it must not be silently rounded to zero.

Write d_K(u) for the degree in the potential-pair graph: an unordered pair is available precisely when at least one directed compatibility arc exists. The direct cap is

```text
P_u = min(rho_u+k, b-1-q_u, d_K(u)-q_u,
          rho_u+floor((E-h_u)/(q_u-h_u))-1 [when q_u>h_u]),
h_u = min(z,q_u,E).
```

There is no selected-excess term when q_u=h_u, including q_u=0. In particular, z is NOT restricted by z<=E.

Because c_u<=a, the simple-degree cap is redundant here:

```text
rho_u+k <= b-1-q_u.
```

This redundancy is conditional on the source-cap hypothesis c<=a.

## 2. Exact selected-excess loss as a short tail sum

For j=1,...,k+1 define

```text
h_j(E,z) = min(E,z) + floor(max(E-z,0)/j) + 1.
```

These h_j are demand thresholds and are distinct notation from the per-source h_u in the cap formula. Define

```text
ell_E(q) = sum_{j=1}^{k+1} 1_{q>=h_j(E,z)}.
```

**Selected-excess loss identity.** Before imposing the potential-pair cap, the effective receiver cap is exactly

```text
rho_u+k-ell_E(q_u).
```

### Proof

If q=0, all thresholds are positive and the selected-excess term is absent, so both losses are zero.

If q>E, then min(z,q,E)<=E<q, and

```text
0 <= E-min(z,q,E) < q-min(z,q,E).
```

The floor in the direct cap is zero. The cap is rho-1 and its loss from rho+k is k+1. Every h_j<=E+1<=q, so the tail-count formula gives k+1 too.

Now assume E>=q>0. If q<=z, the selected-excess cap is absent. If E<z then h_j=E+1>q; if E>=z then h_j>=z+1>q. Thus every indicator is zero.

The remaining case is E>=q>z. The direct loss is

```text
max(0,k+1-floor((E-z)/(q-z))).
```

This counts exactly the integers j in 1,...,k+1 satisfying

```text
j(q-z)>E-z,
```

or equivalently

```text
q >= z+floor((E-z)/j)+1 = h_j(E,z).
```

These cases exhaust the domain. No Hall or q-tail sufficiency claim is used.

An equivalent indicator, sometimes easier to charge directly, is

```text
ell_E(q) = sum_{j=1}^{k+1} 1_{q+(j-1)(q-z)_+ > E}.
```

## 3. Exact potential-pair loss and global budget

Define the additional, non-double-counted potential-pair loss

```text
eta_u = max(0,c_u+k-d_K(u)-ell_E(q_u)).
```

Taking the minimum with d_K(u)-q_u gives exactly

```text
P_u = rho_u+k-ell_E(q_u)-eta_u.
```

Let

```text
N(h) = #{u:q_u>=h},
L_E = sum_u ell_E(q_u) = sum_{j=1}^{k+1} N(h_j(E,z)),
L_K = sum_u eta_u.
```

Then

```text
sum_u P_u = r+bk-L_E-L_K.
```

Every feasible orientation needs Q incoming units in total, so Q<=sum P. Substituting the two-defect bridge identity yields the strengthened necessary budget

```text
2t+D0+E + sum_{j=1}^{k+1}N(h_j(E,z)) + L_K <= bk.   (A)
```

This is strictly more informative as a formula than the previous bare budget 2t+D0+E<=bk: it retains the receiver capacity removed by both extra cap families. It is NOT a new screen beyond the existing scanner's sum-P screen; it is that screen in explicit tail-loss coordinates. It cannot by itself newly reject a profile that already passed that same sum-P screen.

### All-positive-demand specialization

When z=0, D0=0 by the bridge and

```text
h_j(E,0)=floor(E/j)+1.
```

Thus

```text
2t+E + sum_{j=1}^{k+1} N(floor(E/j)+1) + L_K <= bk. (B)
```

For example, k=2 gives the three tails at E+1, floor(E/2)+1 and floor(E/3)+1. Increasing E cannot be treated as giving free incoming capacity: it consumes one unit in the bridge budget for every unit of E even while some threshold losses decrease.

## 4. Exact source-cut identity: aggregate spare capacity is not enough

For ANY source set A0, define

```text
y_w(A0) = #{u in A0 : u!=w, q_u<=c_w+1, q_w<=c_u},
D(A0) = sum_{u in A0}q_u,
H(A0) = sum_w min(P_w,y_w(A0)),
V(A0) = sum_w (P_w-y_w(A0))_+,
q_out(A0) = sum_{u notin A0}q_u.
```

Here V is target capacity unused by this source set, NOT the older crossing statistic C_q. Since min(P,y)=P-(P-y)_+,

```text
H(A0)-D(A0)
 = bk-(2t+D0+E)-L_E-L_K + q_out(A0)-V(A0).          (C)
```

Therefore every Hall cut is nondeficient exactly when

```text
V(A0)-q_out(A0) <= bk-(2t+D0+E)-L_E-L_K
```

for every A0. This explains precisely how a profile can pass the global cap budget (A) yet fail Hall: its unused capacity is too large to be offset by demand left outside the cut.

For a high-q tail A0={u:q_u>=tau},

```text
q_out = sum_{q_u<tau}q_u,
y_w = #{u:tau<=q_u<=c_w+1, c_u>=q_w}-1_{q_w>=tau}.
```

Thus (C) couples the bridge defects, short selected-excess tail sum, potential-pair loss, and exact threshold-rectangle vacancy. It is a natural adaptive-threshold proof target, without claiming that high-q tails suffice for arbitrary profiles.

## 5. Limits and next mathematical step

The identities expose the remaining obstruction; they do not automatically make it contradictory. A useful next theorem would lower-bound V(A0)-q_out(A0), for a structurally chosen A0, beyond the remaining budget on every branch one aims to exclude. The full q-layer minimum-cut/threshold normal form remains available if a high-q-tail reduction fails.

Do not reverse the logical direction: actual graph-derived orientations satisfy Hall. To exclude hypothetical counterexample branches, one must show that their OTHER bridge constraints force a negative margin somewhere. Establishing that every admissible relaxed profile satisfies Hall would not prove Murty-Simon.

The frozen 812 profiles already passed the scanner's global cap check. Accordingly (A) alone cannot newly explain them. Their exact failing cuts can instead be decomposed by (C) to distinguish cap loss from inaccessible residual receiver capacity.

## 6. Verification and provenance

See `EXCESS_TAIL_LOSS_AUDIT.md`, `verify_excess_tail_loss.py`, and `EXCESS_TAIL_LOSS_VERIFICATION.json`. The verifier compares the direct current scanner cap with a separately expressed threshold-loss formula and compares direct labelled Hall margins with (C).

The direct cap was read from `scan_post_pair_relational.cpp` at recovered repository head `81560e92698d07992df4a53976ee1ea8efaaeb4d`. The new formulas were tested locally in the resumed session. This is same-assistant internal derivation and verification, not third-party acceptance. No full-frontier promotion, all-order proof, or graph-realizability claim is made.
