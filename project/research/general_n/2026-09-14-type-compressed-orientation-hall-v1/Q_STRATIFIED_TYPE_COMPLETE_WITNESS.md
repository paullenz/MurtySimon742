# Type-complete crossing-free q-stratified minimum witness

14 September 2026. **Candidate exact corollary of q-stratified minimum-cut exactness and the whole-type symmetry/compression framework. External mathematical review remains OPEN.**

[`Q_STRATIFIED_MINCUT_EXACTNESS.md`](Q_STRATIFIED_MINCUT_EXACTNESS.md) proves that some labelled minimum Hall witness is crossing-free and therefore q-stratified exact. The present corollary strengthens that conclusion in the direction needed by the type-compressed programme:

> **A crossing-free minimum witness can be chosen as a union of complete `(q,c,P)` types.**

Consequently

```text
min over labelled source sets [U_q(S)-D(S)]
=
min over complete-type source sets [U_q(S)-D(S)]
=
min over labelled source sets [H(S)-D(S)].             (1)
```

So the q-stratified exact reduction does **not** force a return to arbitrary labelled subsets.

## 1. Why the maximal minimizer is type-complete

Copies with the same triple

```text
(q,c,P)                                                (2)
```

are interchangeable automorphisms of the labelled target-Hall relaxation. If one copy of a type belongs to some minimum witness, permuting identical copies gives a minimum witness containing any other copy of that type.

Therefore the union `M+` of all minimum witnesses contains either every copy of a type or none of them. Thus

```text
M+ is a union of complete types.                       (3)
```

This also follows from the exact type-quotient construction.

## 2. Whole-type neutral deletion

Suppose the current minimum witness `S` is type-complete and has a positive q-crossing. Choose a crossing pair

```text
x notin S,
y in S,
q_x=q_y,
c_x<c_y,
P_x<m<=P_y.                                           (4)
```

Let `Y` be the complete type of `y`.

The iterative argument in [`Q_STRATIFIED_MINCUT_EXACTNESS.md`](Q_STRATIFIED_MINCUT_EXACTNESS.md) guarantees that the low endpoint `x` lies outside the original maximal minimizer `M+`; previously removed endpoints cannot later become low crossing endpoints because preincoming counts only decrease.

For the first copy `y_1` of `Y`, the neutral deletion lemma gives

```text
F(S\{y_1})=F(S)=delta.                                (5)
```

Now consider another still-selected copy `y_2` of the same type. Before any deletion, every selected copy of `Y` has the same actual incoming count

```text
m-1<P_Y.                                              (6)
```

Deleting another copy of `Y` can only decrease the incoming count at `y_2`: distinct identical copies are numerically compatible, so each deleted `Y` source removes at most one such incidence. Hence throughout the sequential deletion of the type,

```text
y_{y_j}<P_Y.                                          (7)
```

The exterior witness `x` remains outside `M+`, has the same demand as every copy of `Y`, and has smaller `c`. Therefore the neutral deletion lemma applies to every remaining copy in turn.

Thus the **entire selected type `Y` may be deleted copy-by-copy without changing the minimum Hall margin**.

After the last copy is removed, the source set is type-complete again.

## 3. Type-level crossing-removal algorithm

Start with

```text
S_0=M+.                                                (8)
```

While `C_q(S_t)>0`:

1. choose any crossing pair `(x,y)`;
2. let `Y` be the complete selected type of `y`;
3. delete every copy of `Y` sequentially.

Section 2 proves that every intermediate labelled deletion preserves the minimum Hall margin, and every completed stage returns to a union of complete types.

A removed type cannot later supply a low crossing endpoint. At the moment the type is selected high,

```text
P_Y>=m_Y(S_t).                                        (9)
```

Future source sets are nested subsets, so its preincoming count never increases. Therefore after removal

```text
P_Y>=m_Y(S_j)                                         (10)
```

for all later stages, whereas a low endpoint would require the strict reverse inequality.

Each stage removes at least one whole type, so the process terminates at a type-complete minimum witness `S*` with

```text
C_q(S*)=0.                                            (11)
```

Hence

```text
U_q(S*)=H(S*)
       =D(S*)+delta.                                  (12)
```

This proves (1).

## 4. Computational check

A separate deterministic test of the whole-type deletion algorithm was run on 10,000 random fixed-q-monotone profiles with up to eight labelled copies. For every profile it:

- enumerated all labelled source subsets and recovered the exact minimum margin;
- formed the union `M+` of all exact minimizers;
- checked that `M+` was type-complete;
- whenever a crossing occurred, deleted the entire selected high type copy-by-copy;
- required every individual deletion to preserve the exact minimum margin;
- required type-completeness after every completed type deletion;
- required the final witness to have `C_q=0` and q-stratified margin equal to the exact minimum.

All 10,000 profiles passed. This is finite support for the proof, not a substitute for external review.

## 5. Research consequence

The q-stratified all-order problem may now remain entirely in the type quotient. A candidate counterexample to target Hall can be sought as a complete-type set with exact q-layer capacity

```text
U_q(S)
 = sum_q sum_{k>=1} min(alpha_{q,k},beta_{q,k}(S)),    (13)
```

rather than as an arbitrary labelled max-flow cut.

This preserves the main compression gain of the current programme while removing the target-by-target correlation that motivated the q-crossing analysis.

## Trust boundary

The corollary uses the neutral deletion theorem, fixed-q target-cap monotonicity, identical-copy symmetry, and the fact that `M+` is the union of all labelled minimizers. It is exact for the current target-Hall relaxation under those hypotheses. Its Murty-Simon application inherits the canonical bridge and target-cap trust boundary. It does not prove unrestricted Murty-Simon.
