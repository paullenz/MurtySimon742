# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph `X_3` is a mandatory hostile control. Murty-Simon / Erdos #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_CRITICALITY_COLLAPSE_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `760891ad5e3f6ab7f62d769187b5e72cc75b351a`

LATEST THEOREM PACKAGES:

- `project/research/post_ms/2026-09-19-two-omission-criticality-collapse-v1/OMITTED_PAIR_NONEDGE_FORCING.md`
- `project/research/post_ms/2026-09-19-two-omission-criticality-collapse-v1/OUTSIDE_U_EXACT_BALANCE.md`
- `project/research/post_ms/2026-09-19-two-omission-criticality-collapse-v1/OUTSIDE_U_SCORE_ELIMINATION.md`
- `project/research/post_ms/2026-09-19-common-buffer-criticality-v1/UNLOADED_COMMON_BUFFER_SOURCE_EDGE_DICHOTOMY.md`
- `project/research/post_ms/2026-09-19-common-buffer-criticality-v1/ANTICOMPLETE_BUFFER_X_EDGE_TRICHOTOMY.md`
- `project/research/post_ms/2026-09-19-common-buffer-criticality-v1/check_z1_criticality_collapse.py`

## Audit reconciliation

Before any forward mathematics this run, the current `CURRENT_STATE.md`, root `README.md`, recent commits, the 19 September daily adversarial/red-team audit and handoff, the independent source-tuple reproof, the source-premise graph audit/repair, and the independent actual-D2C Hall/pair-capacity regression were reread.

There is **no departure** from the latest audit priority order.

The trust boundary remains:

1. distinct physical-source identity and global selected `(source,coordinate)` uniqueness have been independently re-derived at the exact raw/selected interface used downstream;
2. the finite source-tuple capacity theorem remains described as conditional on those named premises rather than as unconditional graph-level closure;
3. the independent actual-D2C regression through rooted partition, criticality slots, A-codes, Hall objects, gamma codes and pair-local capacity remains mandatory, includes hostile `X_3`, and still records zero graph/formula mismatches;
4. the regression still has **no positive actual-graph fixture realizing a rigid complete Hall cut with `x>=3`**. The rigid one-code deductions below are therefore hand structural implications conditional on those rigid hypotheses, not empirical claims that such a cut occurs in a graph;
5. only the audit-authorized one-code rigid branch is being pushed. Exact `Ccap_P`, `(ONE)` and `(CROWD)` remain distinct from the rooted residual ledger; no collapse to total `C0` is being substituted for the local geometry.

The closed mixed `{4,5}` selected-excess ladder remains closed. The four-exception gate remains subordinate. First-proof priority on Erdos #742 remains inactive.

## Mandatory negative control

`X_3` remains explicit and untouched: `n=12`, `m=32>M(12)=31`, diameter two, every edge critical, canonical root `a=3,b=8,p=4,u=0`, `Q=12`, `r=f=delta=0`. Every theorem added this run uses a nonempty unmatched-U mechanism and is inactive on that canonical root. Nothing here repairs the false all-order 2019 conjecture by accidentally excluding its published counterexample.

## Full-support z=1: omitted pairs are forced nonedges

Retain the purified one-code `z=1`, `h=0`, full-support setup:

- `X--Y` is a complete rigid A-cut, `x=|X|>=3`, `y=|Y|`;
- every source in Y has code d, with `A_d=Y` and `A_{bar d}=emptyset`;
- `g=g_P`, `k=x-g>0`;
- `U_-=U_{bar d}`, `|U_-|=k+1`;
- `U_o=U\U_-`, `u_o=u-k-1`;
- source visibility gives `e(Y)=e(Y,U_d)=e(G[U_-])=0`;
- the full-support omission map has exactly two omitted vertices `o_1,o_2`, with every source omitting exactly one.

A hostile raw-criticality pass now eliminates **every possible certificate for an omitted pair that is an edge**.

The key definition-level facts are:

1. two tight-code vertices have no common matched-B neighbour iff their codes are complementary;
2. the old Orientation A is impossible for **every** source, not only for a non-singleton omission class: the witness would lie in X but complementarity would force code d, contradicting `A_d=Y`;
3. the ROOT alternative is impossible because every A-source has one matched B-neighbour in each of the p tight fibres; if its omitted unmatched vertex were also adjacent then `d_B(s)>=p+1>=2`, so `N_B(s)={o_i}` cannot occur;
4. the OUT alternative is impossible because singleton common neighbourhood with an unmatched head forces an outside witness to have code `bar d`, putting it back in `U_-` rather than `U_o`;
5. the MATCHED alternative is impossible because generalized matched-foot localization gives gamma code d, while in the `h=0` crossing classification every source already uses **all** g gamma-d matched feet as its crossing witnesses, with graph-fixed singleton X heads.

Therefore:

> `nu=y`.                                                  `(FS-NU)`

Every source is nonadjacent to its unique omitted `U_-` vertex. This supersedes the predecessor heuristic that near score equality might push `nu` toward zero: `nu=0` is not realizable in this branch.

The exact full-support ledger consequently simplifies to

> `Z=Z0+H_X+H_Y`,                                         `(FS-Z)`
>
> `L_Y=y(p-g+1)+H_Y`,                                     `(FS-LY)`
>
> `E_-=B+M`,                                               `(FS-E)`
>
> `2q+E_U=D0+H_X+H_Y`,                                    `(FS-R)`

where

`B=(k+1)(p+k-1)`,

`Z0=(k+1)(a-1)`,

`D0=Z0-u(p-lambda)`,

`M=(k+1)u_o-e(U_-,U_o)`.

In particular the apparent `-y` savings in both A--U holes and `U_-` slack disappear exactly.

The score floor is now

> `S>=B+M+max{phi(g),y(p-g+1)+H_Y}`.                      `(FS-S0)`

The exact pair-local crossing bill remains

> `2xy<=Ccap_P=R_code(S_P)[g+2S_P/L]`.                    `(FS-CAP)`

The old `(ONE-P)` substitution is weaker after the exact crossing count is known; `(CROWD)` remains independently useful. Do not replace `S_P` by total score before the local intersection is exhausted.

## Rooted triangle correction: q is the unmatched internal edge count

A second hostile correction was found while reconciling the full-support ledger with the foundational rooted-triangle identity.

Tight fibres force

> `e(G[P])=p(p-1)`,
>
> `e(P,U)=pu`.

Hence

> `Q=p(p+u-1)+e(G[U])`.

The preserved canonical identity is

> `Q=p(p+u-1)+q`.

Therefore:

> `q=e(G[U])`.                                             `(Q-U)`

This matters because the predecessor variable

`Q_rest=Q-e(U_-,U_o)`

contains the forced baseline `p(p-1)+pu`; it is **not** a small correction which can be set to zero. In the present branch

> `Q_rest=p(p-1)+pu+e(G[U_o])>0`.

Any earlier hypothetical state using `Q_rest=0` in this branch is invalid and must not be cited as an equality geometry.

Use instead the genuinely residual quantity

> `Q_o=e(G[U_o])`.

Since `e(G[U_-])=0`,

> `q=(k+1)u_o-M+Q_o`.                                     `(Q-O)`

## Exact outside-U degree balance

For each `z in U_o`, define

- `h_z=a-d_A(z)`;
- `m_z=(k+1)-d_{U_-}(z)`;
- `d_o(z)=d_{G[U_o]}(z)`.

A direct degree sum gives the exact vertexwise identity

> `h_z+m_z=(p+k+1-lambda)+d_o(z)+epsilon_z`.              `(OUT-1)`

Summing over `U_o`, with `H=H_X+H_Y` and `E_o=sum_{U_o}epsilon`, gives

> `H+M=u_o(p+k+1-lambda)+2Q_o+E_o`.                       `(OUT-2)`

Thus `H,M,Q_o,E_o` are one physical ledger, not independent correction knobs.

Two useful exact consequences are

> `q+E_U=B+(k+1)u_o+Q_o+E_o`,                             `(OUT-QE)`

and

> `Q+E_-=p(p+u-1)+B+(k+1)u_o+Q_o`.                       `(OUT-Q)`

The `U_- -- U_o` edge choice cancels exactly from these combinations.

Using only the physical capacity `H_X<=xu_o`, with `x=g+k`, gives

> `H_Y+M>=u_o(p-g+1-lambda)+2Q_o+E_o`.                    `(OUT-SPILL)`

Minimizing exactly over whether that forced spill is paid as Y-holes or missing `U_- -- U_o` edges yields the compact full-support score theorem

> `S >= B + max{ phi(g),`
> `               y(p-g+1)`
> `               +[u_o(p-g+1-lambda)+2Q_o]_+ }`.         `(FS-S1)`

In particular

> `S >= B + max{ phi(g),`
> `               y(p-g+1)`
> `               +u_o[p-g+1-lambda]_+ }`.                `(FS-S2)`

At `lambda=0` this becomes

> `S>=B+max{phi(g),(y+u_o)(p-g+1)}`.

Each internal `U_o` edge costs two units in the non-gamma branch until the gamma term dominates. Near-minimal full-support geometry is therefore pushed toward an independent `U_o` layer.

A bounded arithmetic diagnostic on the existing coarse grid records 59,028 full-support abstract parameter survivors under `(FS-S2)`, versus 59,500 after only the forced-`nu` base score floor. These are **not graph counts**.

## Unloaded common-buffer comparator: source-buffer edges are triangle-free

The other minimal `z=1` support type is the common-buffer branch. Write

`U_-=W_0 disjoint_union {b}`,

with `|W_0|=k`; every source uses all of `W_0`, while b is unused by crossing certificates.

The cheapest comparator has

> `e(Y)=e(Y,U_d)=e(G[U_-])=0`.                             `(CB-0)`

The preserved core floor is

> `E_core>=k(p+k-2)`.                                      `(CB-CORE)`

Let

`r=d_Y(b)`,

`d_o=d_{U_o}(b)`.

Raw criticality now proves:

> every source-buffer edge `s b` is triangle-free.        `(CB-DIR)`

The proof again eliminates both triangle-edge singleton orientations by pair purity, tight-code complementarity, rigid cut completeness, `U_-` independence and saturated gamma-d crossing use.

Consequences for `r>0`:

1. the buffer is anticomplete to X:
   > `d_X(b)=0`;                                           `(CB-X0)`
2. every buffer--`U_o` neighbour is nonadjacent to every source adjacent to b, so
   > `H_Y>=r d_o`;                                         `(CB-RECT)`
3. the buffer slack is exact:
   > `epsilon_b=p+k+u_o-r-d_o`;                            `(CB-EB)`
4. the Y-slack is exact:
   > `L_Y=y(p-g+1)-r+H_Y`.                                 `(CB-LY)`

Therefore for fixed `r>=1`, putting

`A0=phi(g)`, `P0=p+k+u_o`, `L_r=y(p-g+1)-r`,

one has

> `S>=E_core+P0-r-d_o+max{A0,L_r+r d_o}`,                 `(CB-R)`

with `0<=d_o<=min(u_o,P0-r)`. This is a one-dimensional integer profile whose minimum occurs at a clamped integer adjacent to `(A0-L_r)/r` (or on the flat boundary when `r=1`).

For `r=0`, b is anticomplete to Y and may use X. Direct degree counting gives

> `epsilon_b>=p-g`,                                        `(CB-E0)`
>
> `L_Y>=y(p-g+1)`,                                         `(CB-L0)`

hence

> `S>=E_core+(p-g)+max{phi(g),y(p-g+1)}`.                 `(CB-S0)`

Equality in `(CB-E0)` forces the buffer complete to X and complete to `U_o`; zero buffer slack additionally forces `g=p`.

The unified unloaded common-buffer score theorem is the minimum over `r=0,...,y` of these exact one-dimensional profiles.

A deterministic arithmetic replay of the same abstract parameter box reproduces the predecessor gates and records:

- old shared z=1 floor survivors: `86,820`;
- predecessor common-buffer survivors: `76,463`;
- predecessor full-support survivors: `77,310`;
- predecessor either-support survivors: `78,167`;
- criticality-sharpened common-buffer survivors: `64,892`;
- criticality-sharpened full-support survivors: `59,028`;
- criticality-sharpened either-support survivors: `64,892`;
- additional exclusions relative to the older shared z=1 floor: `21,928`.

Among new common-buffer survivors the cheapest branch is `r=0` in 40,589 abstract states and `r>0` in 24,303. These figures are diagnostic parameter counts only. On this grid every new full-support survivor is contained in the new common-buffer survivor set, so the **common-buffer branch is now the limiting minimal z=1 comparator**.

## Minimal r=0 equality geometry: buffer-X edges become matched-foot obligations

Because `r=0` is now frequently the cheapest surviving common-buffer model, the exact buffer-slack equality geometry was pushed one step further rather than moving to `z=2`.

Assume

> `epsilon_b=p-g`,                                        `(CB-EQ)`

so b is complete to X and complete to `U_o`.

Every edge `b x0`, `x0 in X`, lies in a triangle: `c(x0)` is neither d nor `bar d`, while `c(b)=bar d`, so the codes agree in at least one tight coordinate and share a matched neighbour.

Raw D2C criticality gives two possible singleton orientations. Under `(CB-EQ)` they collapse as follows.

### Orientation I

Source `x0`, matched foot z, singleton head b:

> `gamma(z)=c(x0)`.                                       `(CB-I)`

All root, A and unmatched-B locations are excluded; completeness of `b--U_o` removes the otherwise possible outside-unmatched channel.

### Orientation II

Source b, matched foot z, singleton head `x0`:

> `gamma(z)=bar d`.                                       `(CB-II)`

There are exactly g such matched endpoints. For a fixed matched endpoint z, the graph set `N(b) intersect N(z)` is fixed, so if it is a singleton it determines at most one X-head. Therefore at most g of the x buffer-X edges can use Orientation II.

Since `k=x-g`, at least

> `k`                                                      `(CB-K)`

vertices of X require Orientation-I matched feet whose gamma code equals their own tight code.

No injectivity among these Orientation-I feet is claimed. The safe conclusion is a **source/code demand**, not k distinct physical matched endpoints. The set of X-codes occurring among those at least k sources must occur in the matched gamma-code support.

This is the next load-bearing compatibility between the rigid Hall family and the signed tight-fibre core.

## Exact pair-local control remains active

Throughout both support types the audit-requested local pair tools remain live:

- exact `Ccap_P`;
- `(ONE)` where it adds information rather than merely restating the crossing count;
- `(CROWD)`;
- channel separation and gamma-collision pricing.

Do not replace local `S_P` by total `S`/`C0` as the primary next move. Previous global scalar relaxations were explicitly diagnosed as too generous.

## Next action

Stay on `z=1`; **do not move to `z=2` yet**.

The current priority is the unloaded common-buffer branch, especially the `r=0`, minimal-buffer-slack geometry.

1. Group the at least k Orientation-I X-sources by tight code. Do **not** assume their matched feet are distinct.
2. Couple their code multiplicities to the matched gamma support and the existing gamma-collision / switchable zero-signed-subcore penalty. Seek a compact dichotomy: code concentration must pay quadratic A-slack, while code dispersion must force many constrained gamma rows.
3. Intersect that dichotomy with the exact outside-pair `Ccap_P` and `(CROWD)` bill before any total-score collapse.
4. In parallel, classify the `r>0` branch further: triangle-free source-buffer edges plus the rectangular `H_Y>=r d_o` payment may force a stronger direct-edge/slack obstruction.
5. Retain the full-support branch as a sharpened comparator; revisit it only if a new local constraint makes it competitive with common-buffer.
6. Only after both common-buffer subbranches have been structurally exhausted should work move to `z=2`.

## Stop / pivot rules

- Any actual graph/formula mismatch is an immediate repair blocker.
- Keep the source-tuple theorem conditional on its two named premises.
- Retain the actual-graph regression and `X_3` as mandatory controls.
- Do not treat finite parameter counts as D2C graph counts.
- Do not credit ordinary A-layer triangles to rooted Q.
- Use `Q_o=e(G[U_o])`, not `Q_rest`, as the residual outside-unmatched triangle correction.
- Do not infer witness injectivity from per-source criticality; explicitly prove physical uniqueness before multiplying obligations.
- Do not return to mixed `{4,5}`, first-proof Erdős #742 optimization, or the four-exception gate unless the latter becomes genuinely load-bearing.

UNPRESERVED WORK: None. All completed theorem, correction, diagnostic and common-buffer criticality work from this run is committed. The next unfinished line is exactly the code-multiplicity/gamma-support attack described above.
<!-- CURRENT-STATUS:END -->
