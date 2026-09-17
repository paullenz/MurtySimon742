# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 strengthening is not assumed. The published order-12, size-32 D2C obstruction remains a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `SECOND_POSITIVE_RESIDUAL_FULL_TIGHT_HAMMING_DEFECT_CLOSED_FOR_K_GE_17_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This unit continued the full tight-antipode Boolean branch after the predecessor `0a311bae71ee15045926dbbe4fa3e70737c88998`. It did not return to a broad scalar census. The key move was to combine the Boolean witness-cover theorem with the preserved F-separation rule. At the first surviving layer `a=k+1,r=2k`, all A-codes are forced distinct, so residual-coordinate counts become Hamming-ball degree bounds in `F=G[A]`. This is strong enough to put the entire layer strictly below `M(n)` for `k>=17`.

## Preserved entry point

For a non-bipartite D2C graph above `M(n)`, the preserved Q0 theorem forces every maximum-degree root to have rooted triangles. For `n>=14`, the all-private edge-witness theorem forces a disjoint-support antipode. Tight antipodes form a matching. If they cover `B=N(v)`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`; every A-vertex is a Boolean transversal; and

`Q=k(k-1)`,

`r=k(a-k+1)`,

`delta=r-e(F)`.

The residual-zero classification preserves only `k=2` (`H5`) and `k=4` (`X_3`). The Boolean witness-cover theorem then gives, for `k>=5`, at least `k+1` distinct A-codes and therefore excludes the algebraic layer `a=k,r=k`.

## New theorem — Hamming residual support bounds F-degree

Now impose the first surviving layer

`a=k+1`, `r=2k`.

The Boolean witness-cover theorem forces exactly `a=k+1` distinct codes: every A-label has a different code.

For a label `x`, let `D_x subseteq [k]` be its residual coordinate set and `R_x=|D_x|`. Every coordinate outside `D_x` is selected at `x`. The preserved selected-incidence F-separation rule says that every F-neighbour `y` agrees with `x` at each selected coordinate. Hence

`{j:c_j(x)!=c_j(y)} subseteq D_x`.

Because all A-codes are distinct, an F-neighbour must differ on a nonempty subset of `D_x`. Therefore

> `d_F(x) <= 2^{R_x}-1`.

Every A-vertex already has exactly `k` B-neighbours and maximum degree is `2k`, so also

> `d_F(x) <= k`.

Thus

> **HAMMING DEGREE BOUND**
>
> `d_F(x) <= g_k(R_x):=min(k,2^{R_x}-1)`.

The exact residual ledger is

`sum_x R_x = r = 2k`.

Full proof:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/SECOND_POSITIVE_RESIDUAL_HAMMING_DEFECT.md`.

## Global F-bound and second-extremal consequence

For every `k>=19` and every integer `R>=0`,

`g_k(R) <= (k/5) R`.

The only nontrivial checks are `R=1,2,3,4`; the strongest is `15 <= 4k/5`, valid from `k=19`. For `R>=5`, simply use `g_k(R)<=k<=kR/5`.

Therefore

`2e(F) <= (k/5) sum R_x = 2k^2/5`,

so

> `e(F) <= k^2/5`.

For `k=17,18`, the uniform majorant

`g_k(R) <= (15/4)R`

gives the integral bounds

`e(F)<=63` at `k=17`,

`e(F)<=67` at `k=18`.

At `a=k+1`,

`n=3k+2`,

`m=2k^2+2k+e(F)`.

For `k>=19`, the Hamming bound and the parity-independent lower estimate

`M(3k+2) >= (9k^2+6k+4)/4`

give

`m < M(3k+2)`.

The two boundary calculations are

- `k=17`: `m<=675 < M(53)=677`;
- `k=18`: `m<=751 < M(56)=757`.

Hence:

> **SECOND POSITIVE-RESIDUAL FULL-TIGHT DEFECT THEOREM — internal candidate.** In the full tight-antipode Boolean normal form, the layer
>
> `a=k+1`, `r=2k`
>
> lies strictly below the second-extremal comparison level for every `k>=17`.

Consequently an above-`M(n)` full-tight counterexample with `k>=17` must satisfy

> `a>=k+2`,
>
> `r=k(a-k+1)>=3k`.

This is a density closure inside the full-tight branch, not an eventual theorem for arbitrary antipode configurations.

## Verification

Files:

- `SECOND_POSITIVE_RESIDUAL_HAMMING_DEFECT.md`
- `check_second_positive_residual_hamming_defect.py`
- `SECOND_POSITIVE_RESIDUAL_HAMMING_CHECK_SUMMARY.json`

Executed arithmetic replay:

- every `k=17,...,5000`;
- 71,720 pointwise envelope records across all changing values of `g_k(R)`;
- zero failure;
- boundary values reproduced exactly: `(k,m_bound,M)=(17,675,677)` and `(18,751,757)`.

The finite arithmetic check is evidence only. The Hamming and comparison arguments above are the hand proof.

## Negative controls and trust boundary

- `k=2,r=0`: classical `H5` remains allowed.
- `k=4,r=0`: the independent `X_3` Boolean/cube construction remains allowed with `n=12,m=32>M(12)=31`.
- The present theorem starts at `k=17` and therefore does not suppress the hostile finite mechanism.
- External mathematical review and novelty assessment remain open.
- No all-order second-extremal statement is claimed.

## Strategic consequence

The full-tight Boolean obstruction now has three successive structural barriers:

1. `r=0`: only the finite `H5/X_3` switching mechanisms survive;
2. `r=k`: impossible for `k>=5` by the Boolean witness-code cover theorem;
3. `r=2k`: below `M(n)` for `k>=17` by the new Hamming-support defect theorem.

For sufficiently large fibre count, any above-threshold full-tight witness is therefore pushed to

`a>=k+2`, `r>=3k`.

**NEXT ACTION:** critically attack the next layer

`a=k+2`, `r=3k`.

The Boolean witness-cover theorem still guarantees at least `k+1` distinct codes, so there is at most one duplicated code class. Extend the Hamming-support degree bound to this bounded-multiplicity setting, carefully pricing the extra F-edges that one duplicate code can create. Determine whether the `r=3k` layer is also below `M(n)` for all sufficiently large `k`. If the duplicate class causes a genuine obstruction, preserve its exact structure rather than hiding it.

Use `(AMC)` only when returning to near-full/unmatched/errorful antipodes. Do not revisit Q0, the closed mixed `{4,5}` ladder, or first-proof optimization for Erdős #742.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
