# Selection-free candidate capacity and selected-excess bounds

13 September 2026. **Candidate general hand lemmas. External mathematical review and novelty assessment remain OPEN.** These statements use the canonical bridge but are designed to retain information before, or with less dependence on, a particular global choice of selected quasi-edge representatives.

## 1. Raw cross data

Use the canonical bridge notation. Thus `H` is the complement of a diameter-two edge-critical graph, `v` is a minimum-degree vertex of `H`, `A=N_H(v)`, `B=V(H)\\N_H[v]`, and `F` is the complement of `H[A]` on `A`.

For `u in B`, define the **raw A-cross degree**

```text
c_u = |N_H(u) cap A|
```

and the **raw missing-B degree**

```text
mu_u = |{w in B\\{u}: uw notin E(H)}|.
```

For `i in A`, define the raw B-cross degree

```text
C_i = |N_H(i) cap B|,
```

and as usual let `d_i=d_F(i)`.

These quantities exist in `H` before any global selected/residual representative system is fixed.

A cross-edge `ui in E(H)` is called a **candidate label at source u for exception w** when `uw` is missing in `H[B]` and

```text
N_H(u) union N_H(i) = V(H)\\{w}.
```

The complement form of diameter-two edge-criticality guarantees at least one such candidate orientation/label for every missing unordered B-pair.

## 2. Selection-free pointwise restrictions on a candidate label

Suppose `ui -> w` is a candidate quasi-edge in the preceding raw sense.

### Lemma 2.1: F-degree capacity

```text
d_i <= c_u - 1.                                      (2.1)
```

**Proof.** If `j` is an F-neighbour of `i`, then `ij` is absent from `H`. The unique exception `w` lies in `B`, so the pair `{u,i}` must dominate `j in A`. Since `i` misses `j`, `u` must be adjacent to `j` in `H`. Thus every one of the `d_i` F-neighbours of `i`, together with `i` itself, is a distinct A-neighbour of `u`. Hence `c_u>=d_i+1`. QED.

### Lemma 2.2: missing-degree capacity

```text
C_i >= mu_u.                                          (2.2)
```

**Proof.** Source `u` has `mu_u` missing neighbours inside `B`, one of which is the exception `w`. For every other missing B-neighbour `z != w`, domination by `{u,i}` forces `iz in E(H)`. These `mu_u-1` B-neighbours of `i`, together with `u` itself through the cross-edge `ui`, give `C_i>=mu_u`. QED.

Both inequalities are properties of the raw graph and the single candidate quasi-edge. They do not require a global choice of representatives.

## 3. Candidate-capacity sets and a subset inequality

For `u in B`, define

```text
K_u = { i in A : ui in E(H), d_i<=c_u-1, C_i>=mu_u }.
```

Every label that can occur as the selected representative of a missing B-pair oriented out of `u` lies in `K_u` by Lemmas 2.1-2.2.

Now fix any legal global representative system from the canonical bridge and let `q_u` be its outgoing selected count. Distinct missing pairs oriented out of the same source use distinct selected cross-edges, hence distinct A-labels. Therefore

```text
q_u <= |K_u|.                                         (3.1)
```

When `t>0`, the canonical residual-activity lemma gives `rho_u>=1`. Since `c_u=q_u+rho_u`, also

```text
q_u <= c_u-1.                                         (3.2)
```

Define

```text
kappa_u = min(c_u-1, |K_u|).                         (3.3)
```

Let `J=overline{H[B]}` be the graph of missing B-pairs. For **every** subset `U subset B`, each edge of `J[U]` is oriented out of exactly one of its endpoints in any legal representative system. Consequently, without any surplus assumption,

```text
e(J[U]) <= sum_(u in U) q_u <= sum_(u in U) |K_u|.   (3.4a)
```

When `t>0`, residual activity additionally gives the sharpened form

```text
e(J[U]) <= sum_(u in U) q_u <= sum_(u in U) kappa_u.  (3.4b)
```

These are representative-selection-independent necessary conditions on the raw graph: the left and final right sides do not depend on which legal representatives are chosen.

Since

```text
sum_(u in U) mu_u
 = 2 e(J[U]) + e_J(U,B\\U)
 <= 2 e(J[U]) + |U|(b-|U|),
```

the sharpened (3.4b) gives the purely degree/capacity corollary

```text
sum_(u in U) mu_u - |U|(b-|U|)
 <= 2 sum_(u in U) kappa_u.                            (3.5)
```

The case `U=B` with only the `c_u-1` part of `kappa` collapses to the already known aggregate residual-activity accounting. The possible new strength is the **candidate-label restriction** `|K_u|` and proper subsets `U`.

No finite-domain exclusion from (3.4) or (3.5) is claimed in this checkpoint.

## 4. Selected-degree excess pays for incoming load

Return to any legal selected/residual representative system. For `i in A`, put

```text
e_i = x_i-s_i >= 0
```

and suppose `ui` is selected with `s_i>0`.

The canonical source selected-degree forcing gives

```text
d_i <= rho_u+q_u-1.                                  (4.1)
```

The endpoint-load lemma gives

```text
q_u+p_u <= R_i+x_i.                                  (4.2)
```

Because `s_i>0`, its definition is exact: `s_i=d_i-R_i`, so

```text
R_i+x_i = d_i + (x_i-s_i) = d_i+e_i.
```

Combining with (4.1)-(4.2) yields

```text
p_u-rho_u+1 <= e_i = x_i-s_i.                        (4.3)
```

Thus excess selected degree is not free: every positive-demand label selected at a source with incoming load above `rho_u-1` must carry at least the corresponding excess.

Let

```text
q_u^+ = |{i in S_u : s_i>0}|,
L_u   = max(0,p_u-rho_u+1).
```

Summing (4.3) over all selected positive-demand incidences gives the global necessary inequality

```text
sum_u q_u^+ L_u
 <= sum_(i:s_i>0) x_i(x_i-s_i).                       (4.4)
```

The right side is exactly the selected-incidence-weighted excess because label `i` appears in `x_i` selected incidences.

### Exact-demand corollary

If

```text
x_i=s_i for every i,
```

then no zero-demand label is selected and every active source satisfies

```text
p_u <= rho_u-1.                                       (4.5)
```

This can be dramatically sharper than the basic incoming-capacity bound. It is valid only for active sources; a source with `q_u=0` need not satisfy (4.5).

## 5. Exact-demand interval formulation

Still assume `x=s`. Every selected label has positive demand. Put

```text
C_i=R_i+x_i,
```

the raw B-cross degree of label `i`. Since `s_i=d_i-R_i` and `x_i=s_i`,

```text
C_i=d_i.                                              (5.1)
```

For every selected incidence `ui`, endpoint load and (4.1) therefore give

```text
q_u+p_u <= C_i <= rho_u+q_u-1.                        (5.2)
```

So an active source `u` may select only labels whose raw B-cross degree lies in the integer interval

```text
I_u=[q_u+p_u, rho_u+q_u-1].                           (5.3)
```

Sources with disjoint intervals cannot share a selected label. This turns exact-demand selected-geometry feasibility into a margin/interval incidence problem and is the basis of the state-227 worked exclusion in `MARGIN_CLASS_EXAMPLE.md`.

## 6. Scope and trust boundary

- Lemmas 2.1-2.2 and (3.4)-(3.5) constrain the raw graph before a representative system is fixed, but they still depend on the candidate sets `K_u`, which themselves are graph data not present in the current scalar frontier.
- Inequalities (4.3)-(4.5) and the interval formulation are consequences of the selected/residual canonical bridge and therefore inherit its trust boundary.
- A fixed `(q,x)` margin class can be excluded without fixing the actual selected sets. That is still weaker than excluding the underlying scalar state when alternative `q` or `x>s` choices remain possible.
- No unrestricted Murty-Simon theorem, whole-state frontier reduction, or fixed-order ledger change is claimed here.
