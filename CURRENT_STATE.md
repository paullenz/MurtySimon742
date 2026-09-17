# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published order-12, size-32 D2C obstruction remains a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `COMPLETE_THREE_DEFECT_AUDITED_GENERAL_LEAF_PACKAGE_AND_FOUR_DEFECT_LOPSIDED_ISOLATED_PAIR_CLOSED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This extended unit first audited the previously unmerged complete three-defect theorem, then extracted a defect-count-independent leaf-package lemma, and used it to make two substantive advances at four defects: the unbounded no-pair lopsided ray is eventually closed, and every four-defect state with an isolated leaf-pair is support-impossible eventually. The remaining four-defect frontier is now a finite-width no-pair strip with at least two nonempty pendant groups.

## Preserved full-tight entry point

For a non-bipartite D2C graph above `M(n)`, the preserved Q0 theorem forces rooted triangles at a maximum-degree root. For `n>=14`, the all-private edge-witness theorem forces a disjoint-support antipode. Tight antipodes form a matching. If they cover `B=N(v)`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`; every A-vertex is a Boolean transversal; and

`Q=k(k-1)`,

`r=k(a-k+1)`,

`delta=r-e(F)`.

The orientation-code graph `Omega_sigma` has one Boolean-code vertex per possible witness code and one edge per physical rooted B-edge. The actual set of distinct A-codes is a vertex cover of `Omega_sigma`.

The above-threshold density window remains

> if `m>M(n)` in the full-tight branch, then `a<=2k`.

The mandatory order-12/32 hostile control is exactly the `k=4,r=0` Boolean/cube perfect-matching mechanism and remains untouched.

---

# Preserved hierarchy before this unit

- `r=0`: only `k=2` (`H5`) and `k=4` (`X_3`) survive the full-tight switching/factorization classification.
- `r=k`: impossible for `k>=5` by the Boolean witness-code cover theorem.
- `a=k+1,r=2k`: below `M(n)` for every `k>=17` by the Hamming-support defect theorem.
- perfect-matching switched state: excluded above `M(n)` for even `k>=8`.
- complete one-defect switching regime: eventually closed.
- complete two-defect switching regime: eventually closed from `k>=14`.
- the triangle-star three-defect state: eventually closed from `k>=15`.

---

# New result I — complete three-defect theorem audited

The previous unmerged note

`project/research/post_ms/2026-09-17-stronger-pivot-v1/THREE_DEFECT_COMPLETE_SWITCHING_CLASSIFICATION.md`

combines the exact three-defect leaf-package reduction, isolated-pair exclusion, a finite exceptional-core increment table, and the already proved F-separation closures of the empty-core star and triangle-star rays.

Its conclusion is:

> **COMPLETE THREE-DEFECT SWITCHING EXCLUSION — internal candidate.** If a full-tight switching class contains a state with exactly three non-leaf coordinates and `k>=15`, then `m<=M(n)`.

The key support facts are:

- every three-defect state with an isolated leaf-pair has `tau(Omega)>2k` from `k>=10`;
- every no-pair state with at least two nonempty pendant groups has `tau(Omega)>2k` from `k>=7`;
- the only low-cover no-pair rays are the empty-core star (`tau=2k`) and triangle-star (`tau=2k-1`), already excluded by F-separation from `k>=14` and `k>=15`.

### New independent exact audit

Files:

- `check_three_defect_complete_switching_classification.py`
- `THREE_DEFECT_COMPLETE_SWITCHING_CHECK_SUMMARY.json`

The exact physical orientation-code graph was independently reconstructed and exact minimum vertex covers were recomputed for every valid labelled no-pair parameter instance at `k=7,...,12`:

- 916 valid labelled instances;
- zero disagreement with the claimed `B+C_H` table;
- the only `tau<=2k` types were the two lopsided rays: 18 empty-core `g=1` instances and 18 `K_3`-core `g=1` instances.

This is audit evidence only; the universal theorem remains the hand argument.

---

# New result II — general leaf-package theorem

The three-defect leaf-only calculation generalizes to every switched state with `d>=3` non-leaf exceptional coordinates.

Full note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/GENERAL_LEAF_PACKAGE_REDUCTION.md`.

Let the pendant-group sizes be `p_1,...,p_d`, let `t` be the number of isolated leaf-leaf `K_2` components, let `S=sum p_i`, and let `g` be the number of nonempty pendant groups. Then

`k=d+S+2t`.

For a leaf source `x` with unique neighbour `p(x)`, the forced projective witness code is

`{p(x),q}`

for target coordinate `q`. Consequently the leaf-leaf orientation-code subgraph has exact cover

`B_d = 2 sum_i (p_i-1)_+ + 2 sum_{i<j} min(p_i,p_j)`.

If `t>=1`, the isolated-pair packages add exactly

`4tg + 2t(t-1) + 1`.

Thus

> `L_d = B_d` for `t=0`,
>
> `L_d = B_d+4tg+2t(t-1)+1` for `t>=1`,
>
> and universally `tau(Omega_sigma)>=L_d`.

If the attachment counts are sorted `p_(1)<=...<=p_(d)`, then

`B_d = 2S-2g + 2 sum_{i=1}^d (d-i)p_(i)`.

Since an above-`M(n)` full-tight graph needs `tau<=a<=2k`, this gives the general necessary inequalities

`t=0:`

`sum_{i=1}^d (d-i)p_(i) <= d+g`,

and for `t>=1`:

`2 sum_{i=1}^d (d-i)p_(i) +(4t-2)g+2t^2-6t+1-2d <=0`.

So for every fixed defect count `d`, all attachment counts except the largest are bounded independently of `k`. This is a reusable finite-width reduction rather than a four-defect-only observation.

### Regression

`check_general_leaf_package_reduction.py` and `GENERAL_LEAF_PACKAGE_CHECK_SUMMARY.json` independently replay the exact leaf-leaf subgraph for 1,766 configurations with `d=3,...,6`, attachment values `0,1,2`, isolated-pair counts `0,1,2`, and `k<=13`. There were zero failures. Small `d=1,2` is deliberately outside the theorem because accidental code collisions occur there.

---

# New result III — four-defect finite-width reduction

For four defects, write the sorted attachment counts

`w<=x<=y<=z`.

The general theorem gives

`B_4=2S-2g+6w+4x+2y`.

At `t=0`, the necessary support condition becomes

`3w+2x+y <= 4+g`.

Hence only the following no-pair rays survive the leaf package:

- `g=1`: `(0,0,0,z)`;
- `g=2`: `(0,0,y,z)`, `1<=y<=6`;
- `g=3`: `(0,x,y,z)` with `(x,y)` in
  `{(1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3)}`;
- `g=4`: `(w,x,y,z)` with `(w,x,y)` in
  `{(1,1,1),(1,1,2),(1,1,3)}`.

With isolated leaf-pairs, the only eventual possibilities left by the leaf package are

- `t=1,g=1`;
- `t=1,g=2` with smaller pendant size `1,2,3`;
- `t=2,g=1`.

All other `t>=1` states are already support-impossible, apart from fixed smaller orders.

---

# New result IV — lopsided no-pair four-defect ray closed

Full note:

`FOUR_DEFECT_LOPSIDED_SWITCHING_CLASSIFICATION.md`.

Take the no-pair lopsided ray `(0,0,0,k-4)` and root the exceptional four-vertex core at the attachment coordinate. Up to permutations of the three non-root exceptions there are exactly eight valid rooted core types. Direct projective-code grouping gives:

| rooted core | `tau(Omega)` |
|---|---:|
| empty | `2k+4` |
| root-containing `K_3` + isolated | `2k+3` |
| `C_4` | `2k+4` |
| `K_4-e`, missing edge away from root | `2k` |
| non-root `K_3` + isolated root | `2k+4` |
| paw with root pendant | `2k+1` |
| `K_4-e`, missing root edge | `2k+4` |
| `K_4` | `2k-2` |

Thus only two rooted cores can occur above threshold.

### `K_4-e`, missing edge away from root

Exact decomposition:

`Omega ~= 2 K_{k-3} + 2 K_{1,k-3} + 2 K_2 + 2 K_{2,k-2}`,

so `tau=2k`, forcing `a=2k`, `lambda=-1`. F-separation closes this state from `k>=16`.

### Complete core `K_4`

Exact decomposition:

`Omega ~= 2 K_{k-3} + 3 T_{k-3}`,

where `T_m` is the balanced double-star with a doubled physical centre edge. Hence `tau=2k-2`, leaving only `lambda in {1,0,-1}`.

The two clique code layers are

`C+={emptyset} union {{r,d}:d in D}`

and their complements. After explicitly accounting for code multiplicities, unique clean same-layer labels are F-independent, while every clean cross-layer F-edge forces residual degree at least `k-1` at both endpoints.

A conservative uniqueness count gives at most `10-2lambda` exceptional A-vertices. Therefore

`e(F) <= floor(h^2/4)+(10-2lambda)k`,

`h(k-1)<=r`.

This closes the three near-balanced layers from `k>=15,17,19` respectively.

Hence:

> **LOPSIDED NO-PAIR FOUR-DEFECT EXCLUSION — internal candidate.** If a full-tight switching class contains a no-pair four-defect state with all ordinary leaves attached to one exceptional coordinate and `k>=19`, then `m<=M(n)`.

Regression files:

- `check_four_defect_lopsided_switching_classification.py`
- `FOUR_DEFECT_LOPSIDED_SWITCHING_CHECK_SUMMARY.json`

They replay 90 valid labelled rooted-core instances at `k=8,...,12`, all eight exact cover formulas, and the defect arithmetic through `k=5000`.

---

# New result V — all isolated-pair four-defect states closed eventually

Full note:

`FOUR_DEFECT_ISOLATED_PAIR_EXCLUSION.md`.

The finite-width isolated-pair rays from the general leaf package were completed by exceptional-core code accounting.

For `t=1,g=1`, every valid rooted core has

`tau(Omega)>=2k+8`.

For `t=2,g=1`, every valid rooted core has

`tau(Omega)>=2k+16`.

For `t=1,g=2`, the only possible smaller pendant sizes are `y=1,2,3`; the minimum exact excesses over all valid exceptional cores are respectively

`14,18,20`.

Therefore:

> **FOUR-DEFECT ISOLATED-PAIR EXCLUSION — internal candidate.** If a full-tight switching class contains a four-defect state with at least one isolated leaf-pair and `k>=13`, then `tau(Omega)>2k`; hence it cannot occur above `M(n)`.

Regression files:

- `check_four_defect_isolated_pair_exclusion.py`
- `FOUR_DEFECT_ISOLATED_PAIR_CHECK_SUMMARY.json`.

The exact audit covers 180 one-group and 380 two-group instances across consecutive values of the unbounded pendant parameter.

---

# Remaining four-defect frontier

For sufficiently large `k`, a four-defect state in an above-threshold full-tight graph must now satisfy **all** of:

1. `t=0` — no isolated leaf-pairs;
2. at least two nonempty pendant groups;
3. one of the bounded-width attachment patterns listed above.

Only the largest attachment `z` remains unbounded.

An exact diagnostic has been preserved in

`FOUR_DEFECT_NO_PAIR_STRIP_DIAGNOSTIC.json`.

It is **not promoted as a theorem**, but across consecutive values of `z` every remaining strip tested has `tau(Omega)>2k`. The observed minimum excesses are:

- `g=2`, smaller size `y=1,...,6`: `2,6,8,10,12,14`;
- `g=3`: `12,14,16,18,20,18,20` on the seven surviving `(x,y)` pairs;
- `g=4`: `14,16,18` on the three surviving triples.

Equivalently, the observed exceptional-core increments above the exact leaf package stabilize at

- `12` for `g=2,y=1`;
- `14` for `g=2,y>=2`;
- `20` for the surviving `g=3` rays;
- `18` for the surviving `g=4` rays.

These constants would immediately imply `tau>2k` on every remaining nonlopsided strip if proved structurally.

**NEXT ACTION:** prove the **four-defect no-pair exceptional-core increment lemma** behind those four constants, using the forced projective code formula rather than promoting the diagnostic scan. The best compact target is:

- for `g=2`, core increment at least `12` (and at least `14` once the smaller attachment is at least two);
- for the surviving `g=3` rays, increment at least `20`;
- for the surviving `g=4` rays, increment at least `18`.

A hand proof of these finite core bounds would complete the entire four-defect switching regime, with uniform eventual threshold `k>=19` coming from the already closed lopsided `K_4` state. Do not replace this finite structural proof with a raw `z` scan.

After four defects are genuinely closed, reassess whether the general leaf-package inequality plus a defect-count-independent exceptional-core lower bound can close all fixed defect counts at once. Use `(AMC)` only when returning to near-full/unmatched/errorful antipodes.

---

## Mandatory negative control and trust boundary

- `k=2,r=0`: classical `H5` remains allowed.
- `k=4,r=0`: independent twelve-vertex `X_3` Boolean/cube mechanism remains allowed with `n=12,m=32>M(12)=31`.
- Nothing in the three-/four-defect work suppresses the `k=4` hostile control.
- Direct primary-source adjacency certification of the published 2024 Figure-1 graph against the project's `X_3` reconstruction remains open; no stronger identification is claimed.
- The new three- and four-defect claims are internal hand mathematics with exact regression, not externally reviewed theorems.
- External novelty assessment remains open.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
