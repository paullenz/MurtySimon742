# Hostile audit of the universal selected/residual bridge

11 September 2026. Internal hostile audit by ChatGPT/Geeps. **Not external peer review.**

Target: `UNIVERSAL_BRIDGE.md` in this directory.

## Verdict

**No blocking defect found in this pass.** The parameterised bridge reproduces the fixed-order specialisations used at n=29 and n=30 and agrees with the independently reconstructed N29/N30 late-LP embeddings at the interface they share.

This verdict is deliberately narrower than a proof of Murty-Simon: it covers the universal hand bridge only. Downstream finite relaxations and exact certificate systems have separate trust boundaries.

## Audit method

The audit was performed adversarially. For every injection or counting step, the questions were:

1. can two nominally distinct source objects map to the same counted edge?
2. can an edge claimed residual secretly be selected?
3. is a source/supplement orientation being counted twice?
4. is an inequality used in the wrong direction?
5. is a denominator or monotonicity argument valid at the boundary?
6. does the claimed parameterised statement actually specialise to the existing fixed-order bounds?

Exact scalar identities are independently checked by `exact_arithmetic_audit.py`.

## 1. Complement/quasi-edge construction

For a missing pair `{u,w}` of H[B], adding `uw` to H corresponds to deleting the critical G-edge `uw`. A newly adjacent total-dominating pair in `H+uw` must use u or w because no other adjacency changed. It cannot be `{u,w}` because neither dominates v. Therefore an existing cross-edge `ui` with `i in A` exists, after orientation, and has unique exception w.

**Disposition: PASS.**

## 2. One representative per missing unordered B-pair

The selection is indexed by missing **unordered** B-pairs. A selected cross-edge `ui->w` recovers source u and the unique uncovered vertex w, hence recovers its indexing pair `{u,w}`. Two different indexing pairs cannot use the same selected edge. The reverse orientation of the same pair is not a second indexing object.

**Disposition: PASS.** This convention is essential and is now explicit.

## 3. First residual injection: `d_i <= rho_u+R_i`

For F-neighbour j of i, domination by selected `ui->w` forces `uj` to be an H-edge. If `uj` is selected, say `uj->z`, then domination by `ui->w` forces `iz` to be an H-edge. The potentially dangerous point is whether `iz` could itself be selected.

It cannot: `ij` is absent in H and `jz` is absent because j is the selected label in `uj->z` and z is its unique exception. Thus i and z jointly miss the A-vertex j. Any selected A-B edge has its unique exception in B and hence must dominate every A-vertex. Therefore `iz` is residual.

Different selected j at source u have different supplements z, so these residual edges are distinct.

**Disposition: PASS.**

## 4. Second residual injection: `d_i <= rho_u+rho_w`

Again take F-neighbour j. If `uj` is selected, `{u,j}` must dominate w, forcing `jw` to be an H-edge. It cannot be selected from w because `ij` and `iw` are both absent, so j and w jointly miss the A-vertex i. Distinct j give distinct residual edges at w.

**Disposition: PASS.**

## 5. Source and supplement forcing

`d_i<=rho_u+q_u-1` is a direct cross-neighbour count at u. For supplement forcing, every other selected label j at u must be adjacent to w because u misses w. The `q_u-1` labels are distinct, and their w-incidences are partitioned into residual plus selected incidences from w, giving `rho_w+q_w>=q_u-1`.

**Disposition: PASS.**

## 6. B-side missing-degree identity and endpoint load

Each missing unordered B-pair incident with u is oriented exactly once, outward or inward, giving `q_u+p_u` equal to the missing H[B]-degree. The minimum-degree inequality in H then gives `p_u<=rho_u+(b-a-1)`.

For endpoint load at selected `ui->w`, the families consisting of u, other outward supplements of u, and inward sources to u are pairwise distinct. A collision between an outward supplement z and an inward source z would orient the same unordered pair `{u,z}` both ways, impossible under the one-representative convention.

**Disposition: PASS.**

## 7. Residual activity

Assume `rho_u=0` and put `U=N_A(u)`, `T=A\U`.

There is no F-edge U-T because a selected edge from u to the U-endpoint would have to dominate the T-endpoint, contradicting its nonadjacency to u.

For an F-edge inside U, the two endpoint representatives at source u have distinct supplements and force two residual cross-edges. Their residual status follows from the same 'jointly miss an A-vertex' test as above.

For an F-edge inside T, the auxiliary of its quasi-edge cannot be u or v. If it lay in A, domination of u forces it into U; the quasi-edge exception in T then forces a missing U-T edge, contradicting the preceding separation. Hence the auxiliary lies in B. Because this cross quasi-edge has exception in A, it cannot be one of the selected representatives, whose exceptions lie in B.

The U and T residual families are disjoint by their A-endpoints. The T-family is injective because the cross quasi-edge plus its unique exception recovers the original missing A-pair.

Thus `r>=e(F)=r+t`, contradiction when `t>0`.

**Disposition: PASS.** This remains a highest-priority target for independent human review because many downstream bounds use `rho_u>=1`.

## 8. Charging

For each label choose `s_i` actual selected incidences. At each chosen incidence, the first residual injection gives `s_i<=rho_u`. Since a chosen source has q_u>=1, `q_u+rho_u<=a` implies `rho_u<=a-1`, so the denominator `a-rho_u` is strictly positive.

The charge `(rho_u-1)/(a-rho_u)` is increasing on `1<=rho<a`. Source u participates in at most `q_u<=a-rho_u` chosen incidences, so source charge is at most `rho_u-1`. Summing gives (7.1). Eliminating r with `S>=r+2t` produces (7.2); this algebra is checked exactly by the audit script.

**Disposition: PASS.**

## 9. Threshold capacity

Every chosen heavy incidence at level h has source residual degree at least h. For a high-load source u (`ell_u>h`), each supplement w of a heavy selected arc must itself have `rho_w>=h`: either the `ell_u-1` forced heavy-label incidences at w are all residual, or one is selected from w and its heavy label gives `rho_w>=s_k>=h`.

Therefore heavy arcs from high-load sources use unordered B-pairs within Z_h incident with J. Selected-pair injectivity gives the pair count

`j(z_h-j)+C(j,2)`.

The remaining sources contribute at most h each. The final comparison with `h z_h+C(z_h-h,2)` has the exact difference

`(q-j)(q-j-1)/2`, q=z_h-h,

which is nonnegative for every integer q-j, including negative values.

**Disposition: PASS.** The earlier historical sign/order typo was expositional only and is not present here.

## 10. Isolated-C lemma

Let x be isolated in C and X=A\{x}. A missing X-pair produces a cross quasi-edge with auxiliary in B and exception in A. Hence it is residual, and different X-pairs give distinct residual edges.

Let Z be the used B-endpoints. For z in Z, a representative `iz->j` forces xz because `{i,z}` must dominate x and i misses x. The edge xz cannot be selected: x and z jointly miss j (`xj` absent because x is C-isolated, `zj` absent because j is the exception). Thus xz is residual and is outside the first family because its A-endpoint is x.

Every unused B-endpoint has some residual incident edge by residual activity. These b additional edges are distinct by their B-endpoints and lie outside the first family. Therefore `r>=|P|+b`, yielding `b<=a-1-t`.

**Disposition: PASS.** This is another high-priority independent-review target because the proof uses two disjoint residual injections.

## 11. Parameterised consequences

When isolated-C is impossible, minimum degree one in C gives `e(C)>=ceil(a/2)`, hence

`r<=C(a,2)-t-ceil(a/2)`.

Specialisations:

- a=12 gives `r<=60-t`, exactly the N29 Delta=16 bound;
- a=13 gives `r<=71-t`, hence r<=70 at t=1 and r<=69 at t=2, exactly the N30 Delta=16 bounds.

**Disposition: PASS.** Exact arithmetic checked separately.

## 12. Interface with the corrected late LP

The universal bridge intentionally stops before the averaged LP. A separate N29 audit reconstructed the Y/T/W/P/Z normalization from an actual selected/residual configuration and found the corrected v2 dimensions sound. A separately written N30 parameterisation passed its own exact synthetic microstate audit. Those results reduce, but do not eliminate, the correlated-error risk of the downstream finite model.

**Disposition: PASS at current internal-audit level; independent reconstruction remains desirable.**

## Final status

No blocking defect was found. The bridge should be treated as the canonical **candidate** universal hand reduction for subsequent internal work, while fixed-order reviewer packages remain the official claim surfaces sent for external scrutiny.
