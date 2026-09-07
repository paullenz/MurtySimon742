# Audit of the weak-core reduction's scope

7 September 2026. Same-assistant internal mathematical audit; independent review OPEN.

## Question and conclusion

Does the complete (a,b,t)=(12,15,1) numerical chain exclude the weaker active B-quasi-edge cores of PROOF.md Section 6, or only actual diameter-two-critical graphs?

**Candidate conclusion:** it excludes the weaker cores, provided positive minimum degree of H[A] is included as an input axiom. Full criticality is used only to put an original positive-surplus critical graph into that class. It is not used again after density reduction. This distinction is a mathematical proof obligation, not something certified by replaying arithmetic.

## Core identities and charging

The chosen cross edges and existing H[B]-edges account for all binom(b,2) B-pairs. Thus e(F)=r+t. The minimum H-degree gives D_i=R_i+x_i>=d_i, because d_H(i)=a-d_i+D_i. Hence x_i>=s_i=max(0,d_i-R_i). At B-vertex u, d_H(u)=b-1+rho_u-p_u, so p_u<=rho_u+ell. None uses criticality outside the chosen B-pairs.

For a selected ui with exception w, any F-neighbour j of i must neighbour u. If uj is residual, charge to that residual row edge. If uj is selected with exception z, z differs from w; ui must dominate z through iz. The edge iz is residual because i and z both miss j. The exceptions at a source are distinct, so these latter edges are distinct. This proves d_i<=rho_u+R_i.

For the pair version, a selected uj at an F-neighbour j must dominate w through jw, because uw is absent and w is not uj's exception. The edge jw is residual because j and w both miss i. This proves d_i<=rho_u+rho_w, again with distinct row charges.

The F-neighbours of a selected label are contained in the source's rho_u+q_u neighbours, excluding the label itself. This gives d_i<=rho_u+q_u-1. Distinct selected labels and distinct supplements also give rho_w+q_w>=q_u-1. If a source misses j, all its q selected labels must neighbour j in C, so d_j<=a-q_u-1. These all concern chosen B-quasi-edges only.

For the initial charging bound let g(s)=0 for s=0 and g(s)=(s-1)/(a-s) for 1<=s<a. Every selected positive-demand label satisfies s<=rho_u. If rho_u<a, monotonicity and q_u<=a-rho_u give sum_{selected at u} g(s_i)<=rho_u-1; if rho_u=a then q_u=0 and the assertion is automatic. A demand s_i>=a cannot occur: supplying its selected incidences would require a source of residual degree at least a and positive q. Each label receives at least s_i selected incidences. Thus

    r-b >= sum_i s_i(s_i-1)/(a-s_i),
    S >= r+2t.

Combining these gives exactly the initial demand-domain inequality. This argument requires activity and the chosen-edge charging facts, not other missing-pair quasi-edges.

## Stage-by-stage scope table

| Stage | Necessary ingredients | Criticality after reduction? |
|---|---|---|
| v4 initial demand domain, source counts, support and weighted dual cuts | Residual ledger, activity, selected charging, distinct source labels and supplements, one selected arc per unordered B-pair | No |
| v4 full residual enumeration and row caps | Same facts; rho in 1..a; sum rho=r; positive minimum C-degree gives r<=59 | No |
| v4 zero-slack and projected degree/pair cuts | Exact column identity z_i=R_i+s_i-d_i, d_i<=10, residual column totals, d_i<=rho_u+rho_w, pair injection | No |
| v5 column domains and forced labels | d_i<=10; exact sums of R and z; x_i>=s_i; safe source/supplement eligibility | No |
| v5 one-source joint program | Chosen-edge implications for selected/residual/missing status, global column sums, exact one-source totals | No |
| v5 activation networks and 807 certificates | Bounds on q and p; supplement degree inequality; unique source-label and ordered pair incidences | No |
| v6 shared F/column/pair model | An actual core has one simple F, one A-B adjacency matrix and one selected assignment; averaged indicator identities and chosen-edge domination | No |
| v6 source-degree types | The actual integer q at each source; row degrees, pair capacities and label restrictions conditional on q | No |
| v6 91 branching trees | Counts of vertices with a given column/type, F-edges or selected/residual incidences are integers; both sides of each split are covered | No |
| v7 joint events and (q,p,x) types | Facts in PROOF.md Sections 2–4; actual event indicators and their marginal sums | No |

The r<=59 bound is not an unexplained criticality prune: item 4 gives e(C)>=ceil(12/2)=6; since e(C)+r=binom(12,2)-1=65, r<=59. The initial 1,976 retained demand intervals have maximum r=63, so the compiled upstream row-domain bounds are respected before this cut. Unsupported dimensions are not being extrapolated.

The v4 label-tail stress-profile exclusion and the infinite families in v4/v5/v6 are not needed for the order-28 finite chain. Their additional statements are not silently imported into the core lemma. The n=25/n=27 legacy branches are likewise not dependencies of the order-28 finite enumeration beyond explicitly restated structural arguments.

## Where full criticality IS required

1. Published complement correspondence for the original non-bipartite critical G.
2. Existence of a chosen B-quasi-edge for each missing B-pair.
3. The original all-active argument: missing pairs in a subset of A may need quasi-edges to force residual edges.
4. The original positive-C-minimum-degree argument: if C has an isolated x, missing pairs in A minus {x} need quasi-edges.

Steps 3 and 4 are proved for the original positive-surplus critical graph before F-edges are removed. The properties they establish—activity and positive C-minimum degree—are invariant under the reduction. Reapplying criticality to the reduced complement would be invalid and is not done.

## Adversarial checks and limits

The reduction does not preserve d_i, s_i, e(C), minimum G-degree, diameter two, or edge-criticality. Only the specified core properties and unchanged cross/B structure are asserted. The target domain is re-enumerated over every possible resulting demand; we do not apply the old row certificate to an altered demand.

A saved five-vertex example has a valid all-active chosen system, but deleting its F-edge yields a complement of diameter greater than two while retaining the selected B-quasi-edges. The direct regression contains 672 nonempty deletions with the same behaviour. This rules out interpreting the argument as deletion-preserves-criticality.

No positive-surplus original graph occurred in those examples. No finite test proves universal core closure or confirms that an expert will accept this audit. The proof above, the original numerical-domain proofs and the model-to-core lifting arguments remain the mathematical trust boundary.
