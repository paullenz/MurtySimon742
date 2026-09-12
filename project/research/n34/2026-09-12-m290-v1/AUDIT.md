# N34 bound: focused internal audit

12 September 2026. Same-assistant audit by ChatGPT/Geeps.
**No blocking flaw found in this internal pass. External review OPEN.**

## Findings and proof obligations checked

1. **Coverage.** The original frontier is conservative. The new verifier
   regenerates all 1,614 states, matches each saved state ID to its exact
   vectors, rejects duplicates and omissions, and requires each stage's
   inputs to equal the preceding stage's unresolved set. All states close.

2. **Exact degree mass.** The identity uses actual d, R and
   `s=max(0,d-R)`, not an inequality substituted as equality. With positive
   demands the exact relation is `r=S-4`. The 463 removed states were safe
   extra states in the earlier expansion, not an error in its coverage.

3. **Zero demands.** Every zero-demand state in this branch has exactly one
   zero label. Its residual excess is `E=S-r-4`, so d=R-E is forced.
   Both discovery and verification check the one-zero hypothesis. The four
   fixed and 14 adaptive zero-state certificates use that domain; 11 other
   zero states close by the subset hand lemma. Multiple-zero profiles
   require a different allocation of E and are not covered by this shortcut.

4. **Subset equality.** The generalized hand proof counts actual heavy
   incidences ell_u, with J defined by ell_u>h. Tight capacity forces each
   heavy label to have x=s and every source in Z to have a heavy incidence.
   It does not force q_u=ell_u. Total q_u cancels in endpoint load/source
   forcing anyway, giving p_u<=rho_u-1. All heavy arcs from J enter Z by the
   canonical supplement argument. This establishes both incoming bounds
   without assuming that light labels disappear.

5. **Envelope signs.** The new residual balance is exact, so free lambda
   is valid. c and mu multiply exact selected-incidence balances. Only
   transport and adaptive potential weights must be nonnegative. The older
   baseline certificates retain their stronger nonnegative restrictions.
   The verifier checks all relevant signs and permits no unknown weights.

6. **Monotonicity and local domains.** BC, SH and diagonal indicators are
   monotone in s,d,-h. Source bounds dominate each selected label's s and d
   while their load is at most the label's load. The added label cap
   `x<=#{rho>=s}` uses distinct selected sources. Every integer local option
   in the stated safe domain is checked; no numerical feasible set is
   trusted as a characterization of graphs.

7. **Exact acceptance.** Numerical coefficients are rounded and repaired
   only by lowering ell/sigma envelopes, followed by exact sign, local-row
   and strict-gap checks. Adaptive weights omitted from storage are exactly
   zero integers. The separate verifier checks all 431,338 local rows and
   all 952 negative gaps from their saved integer values. An infeasible LP,
   failed proposal or stopped discovery process never counts as a proof.

8. **Dependencies and scope.** The existing N34 higher-degree and 291/292
   reductions remain necessary, together with the canonical bridge and its
   fixed-label bounds. Their prior source/dependency audit is preserved.
   The new argument concludes m<=289 only; it does not exclude the 13,546
   equality states, establish uniqueness of K(17,17), or prove an all-order
   theorem. Published status denotes repository availability, not external
   mathematical acceptance.

## Reproduction boundary

The standard-library verifier was run on the complete saved certificate
set. A clean staged-tree replay also checks this verifier and the existing
upper-layer verifier; its receipt belongs in the reviewer release.
The complete 77,558,760-profile frontier had already been regenerated
byte-for-byte in the preceding publication. It was reused unchanged here.
The package manifest pins its direct replay inputs and the unchanged
dependency baseline.

Separate program structure is internal implementation evidence. A specialist
should review the bridge and the heavy-subset equality proof first, then
reproduce the saved certificates and the original frontier independently.
