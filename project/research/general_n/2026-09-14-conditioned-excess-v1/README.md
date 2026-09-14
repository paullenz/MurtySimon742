# Conditioned spill slack and the row-295 equality obstruction

14 September 2026. **Candidate universal consequences of the canonical selected/residual bridge. Exact internal hand derivation and separately structured finite checks; external review OPEN. No whole-state promotion, graph realization or unrestricted proof.**

This follows the [block-pressure package](../2026-09-14-block-pressure-v1/README.md) and [all-source spill](../2026-09-14-capped-spill-v1/README.md). The earlier twelve-profile remainder is retained unchanged. The new calculation rejects three specific sampled profiles, rows 295, 365 and 570. It does not close three canonical scalar states.

## 1. Why condition on a budget rather than optimize it independently?

Previous caps and charge envelopes separately allowed every distribution of selected excess. A cap could effectively use one distribution while the charge bound used another. Both bounds were safe, but that independent relaxation could lose the obstruction.

Here we fix the actual excess in one label block, use that SAME value in the incoming caps and the charge envelope, and exhaust all possible integer values. This is a legitimate case split, not an extra graph hypothesis or an empirical choice of a favourable budget.

Keep Q=r+2t+D0+Esel, x_i=s_i+e_i, e_i>=0, rho_u>=1 and c_u=q_u+rho_u<=a. Structural surplus is t; the q-threshold is tau; eta indexes label-demand blocks. The graph application inherits the canonical selected-label forcing s_i<=rho_u and positive-label endpoint consequence

    d_u=(p_u-rho_u+1)_+ <= e_i

at every selected incidence ui with s_i>0. Retain all earlier legitimate target caps P_u and D_u=(P_u-rho_u+1)_+.

## 2. A general block lemma

Let L be ANY label set containing every zero-demand label. Let A_u be the eligible labels of source u; in the present projection A_u={i:s_i<=rho_u}. Define

    S_L=sum_{i in L}s_i,
    f_u=(q_u-|A_u\L|)_+,
    M=sum_u f_u,
    m_u=|A_u intersect L|.

Actual selections place at least f_u incidences from u into L. Fix the actual value

    e_L=sum_{i in L}e_i,
    J=S_L+e_L-M,
    E_H=Esel-e_L.

Necessarily J>=0 and 0<=e_L<=Esel. If k_u is the actual number of u's selected labels in L, then

    sum_u k_u=S_L+e_L=M+J,
    k_u>=f_u.

Thus, source by source,

> **Spill-slack selection bound**
>
>     k_u <= kmax_u := min(q_u,m_u,f_u+J).

Every selected label outside L has positive demand and consumes at least d_u units of excess. Its label is distinct at the source. Therefore, when q_u>kmax_u,

> **Conditioned pressure cap**
>
>     d_u <= floor(E_H/(q_u-kmax_u)),
>     p_u <= rho_u-1+floor(E_H/(q_u-kmax_u)).                 (1)

Take the minimum with EVERY earlier cap, including exact potential-pair degrees. A zero denominator supplies no additional cap. A negative J or impossible block total rejects that branch; it is never rounded to zero.

The source's forced selections are not counted twice: J is the TOTAL slack above all sources' lower bounds. This proof explicitly retains the same disjoint counting that motivated the +f_w correction in the preceding all-source-spill theorem.

The computation below uses L={i:s_i<=eta}. The lemma itself is more general. No q-tail sufficiency, equality of Hall minima, or fixed-q monotonicity is needed for (1).

## 3. Couple the same branch to the integer charge envelope

For each eta, enumerate every integer

    max(0,M-S_L) <= e_L <= Esel.

The empty block has e_L=0; the whole label set has e_L=Esel. These boundary conditions are explicitly tested.

Compute P^(eta,e_L) using (1). The earlier top-source charge envelope is then maximized with the ADDITIONAL EXACT condition

    sum_{s_i<=eta} e_i=e_L.

It still enforces total excess, per-label selected-incidence upper bounds, and complete equal-demand-prefix spill lower bounds. For a charge threshold xi>=0 and nonnegative source coefficients alpha, its per-label score is the sum of the largest s_i+e_i values

    alpha_u min(e_i,(P_u^(eta,e_L)-rho_u+1)_+)

among sources with q_u>0 and rho_u>=s_i, and is zero for s_i<=xi. This is a SAFE UPPER envelope for the explicitly stated necessary projection, not exact joint selected-incidence or graph realization.

Combine it with the previously proved priced-receiver lower bound at some tau,theta. Every branch must pass both bounds using that SAME e_L. If every branch is rejected, the profile is excluded. A branch with no strict contradiction is retained, not reported as a graph.

Our frozen search tests xi in {0,eta}, alpha identically one and the earlier coefficients alpha=1 for q<=2 / alpha=3 for q>2. It tests all finite q-thresholds and price breakpoints used by the existing receiver certificate. It makes no claim that this finite coefficient family is complete for every obstruction.

## 4. Row 295 has a short hand contradiction, without an optimizer

Its complete arrays remain in ../2026-09-14-block-pressure-v1/REMAINDER_12.json. The relevant facts are

    a=24, b=28, t=1, D0=0,
    Q=109, r=79, Esel=28,
    demands: 1 twice, 2 three times, 3 three times, 4 sixteen times.

There are twelve sources with (q,rho)=(2,1). Each MUST select both demand-one labels. Thus these labels have total excess e_L>=22, leaving at most six excess units elsewhere.

Using all preceding caps, the pressure ceilings D=(P-rho+1)_+ are

    [4,4,0,0,1,4,0,4,4,1,1,1,4,1,0,1,4,4,4,2,4,4,1,4,4,4,4,4].

For each label of demand 2, 3 or 4, its top-source charge at excess e=0,...,6 is bounded by the following explicit table:

| demand | e=0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0 | 3 | 8 | 14 | 19 | 20 | 21 |
| 3 | 0 | 4 | 10 | 15 | 20 | 21 | 22 |
| 4 | 0 | 5 | 9 | 13 | 17 | 18 | 18 |

Every entry is at most 5e. The two demand-one labels contribute at most 4(2+e_L). Since every label is positive-demand, the actual selected-incidence charge C=sum_u q_u d_u consequently satisfies

    C <= 4(2+e_L)+5(28-e_L)=148-e_L <=126.                (2)

On the receiver side sum_u p_u=109 and sum_u(rho_u-1)=51, so sum d_u>=58. All q are at least two; exactly twelve have q=2, and their pressure is at most four. Therefore

    C = 3 sum d_u - sum_{q=2}d_u + sum_{q>3}(q_u-3)d_u
      >= 3*58-12*4=126.                                  (3)

Feasibility forces equality THROUGHOUT (2)-(3). Hence e_L=22; both low labels have selected degree exactly twelve and are used exclusively by the twelve forced sources. Also every q>3 source has d_u=0, every q=2 source has d_u=4, and the four q=3 sources must carry total pressure 58-48=10.

None of those q=3 sources may select a low label: both columns are already full. Each selects three distinct other labels. Each such label must have excess at least that source's pressure, but total excess outside the low block is only six. Consequently every q=3 source has d_u<=floor(6/3)=2. Their total pressure is at most eight, contradicting ten.

> **The equality case would require 10<=8.**

This is the new structural obstruction. It is not an assertion that equality in an arbitrary safe upper bound is automatically impossible; all intermediate equalities and forced incidences are identified explicitly.

## 5. Complete finite branch certificates

The independently executed conditional calculation excludes:

| Original synthetic row | Conditioning threshold eta | Every tested excess total | Result |
|---|---:|---|---|
| 295 | 1 | 22,...,28 | every branch rejected |
| 365 | 1 | 22,...,38 | every branch rejected |
| 570 | 2 | 43,...,49 | every branch rejected |

For row 295 at e_L=22, the conditioned price certificate is already strict: lower 129 > upper 126. This is a second explanation of the same profile, separate from the hand equality proof above. Row 365 includes a one-unit strict branch, 206>205. Row 570 includes a one-unit strict branch, 242>241. They are exact integer comparisons, not numerical tolerances.

The cumulative sampled-corpus result is 704/713 rejected, with nine not rejected:

    108,160,240,258,338,342,347,471,586.

The earlier 701 rejections are retained through their preceding proof scopes; this new replay directly examines the twelve-record remainder. It is not a new independent generation of all 713 profiles or a complete enumeration of any canonical scalar state. The canonical 3,607-survivor frontier is unchanged.

## 6. Verification and preserved limitations

The new standard-library verifier completed 9,293 selected-incidence configurations, 42,649 conditioned inequalities and 2,000 independently structured brute-force upper-envelope comparisons (143 nonempty projections). It checks empty and whole conditioning blocks, zero demands, all three standing hostile examples and all twelve remainder profiles. A hand-arithmetic verifier checks the row-295 table and every integer used in its 10-versus-8 contradiction.

The complete deterministic output preserves every branch of the stated search, including branches that remain unrejected. It must be compared as parsed JSON; no numerical solver, floating infeasibility status or timeout certifies any exclusion.

Historical exploration is retained as data, including unsuccessful searches and local-path assumptions. The new theorem does not turn old numerical exploration into proof. Any future closure must continue to keep whole-state coverage, synthetic profile rejection, internally replayed arithmetic and external mathematical acceptance separate.

Next structural target: enforce common excess totals across several demand blocks, or the joint selected-incidence constraints lost by taking each label's best sources independently. The nine remaining profiles are explicit boundary evidence, not graph constructions. Exact q-layer, crossing-wall and independent maximum-cut/stability routes remain preserved.
