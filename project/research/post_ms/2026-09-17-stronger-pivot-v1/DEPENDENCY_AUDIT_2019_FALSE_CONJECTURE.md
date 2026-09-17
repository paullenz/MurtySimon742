# Dependency audit: false 2019 second-extremal conjecture

17 September 2026. Audit requested after discovery that Dailly–Foucaud–Hansberg Conjecture 3 (2019) is false as an all-order statement.

**Status:** dependency audit and literature correction. Mathematical status of the existing project proofs is unchanged by this audit. External mathematical review remains open.

## Question

Does the failure of the 2019 all-order bound

`e(G) <= floor((n-1)^2/4)+1`

for non-bipartite D2C graphs (apart from the originally listed exceptions) invalidate any of the Murty–Simon / residual / Hall proofs in this repository?

## Finding

**No load-bearing proof dependency on Conjecture 3 was found in the proof chain inspected for the fixed-order results, the canonical selected/residual bridge, the residual h-index programme, or the post-pivot signed-surplus/zero-residual results.**

The 2019 paper contains both a conjecture and separate proved results. The distinction matters:

1. **False input:** its Conjecture 3 is now known to be false in all orders because a published 12-vertex D2C graph has 32 edges, while `floor(11^2/4)+1=31`.
2. **Valid published input:** the paper proves results for D2C graphs with a dominating edge, including an upper bound strictly below the Murty–Simon threshold. Those proved results do not become false because Conjecture 3 is false.
3. **Earlier valid input:** the complement/total-domination correspondence used by the canonical construction predates the 2019 paper. Hanson and Wang (2003) established the key relation between D2C graphs and total-domination edge-critical complements. The repository previously cited the 2019 paper too loosely at this point; that attribution is corrected by the same checkpoint as this audit.

## Proof-chain accounting

### Fixed-order Murty–Simon candidates

The fixed-order proofs target the original Murty–Simon inequality/equality statement. Their graph-to-residual constructions, finite certificate domains, Fan-free upper-range reductions, Hall/capacity arguments and hostile audits do **not** assume the 2019 second-extremal conjecture.

The discovery that a separate August 2026 repository appears to contain a complete Lean-formalised Murty–Simon solution changes priority/novelty, not the internal truth value of these fixed-order arguments.

### Canonical selected/residual bridge

The bridge uses edge criticality, the complement/total-domination correspondence, quasi-edge witnesses, selected representatives, residual incidences and exact counting identities. It does not infer any inequality from Conjecture 3.

### General residual h-index programme

`project/research/general_n/2026-09-07-residual-hindex-v1/README.md` derives its inequalities from the canonical bridge and, where stated, the hypothesis `t>0`. Its high-degree theorem is an internal derivation. The only relevant literature dependencies are proved structural results/correspondences. The attribution section is corrected to distinguish Hanson–Wang (2003) from the separate proved dominating-edge theorem in Dailly–Foucaud–Hansberg (2019).

### Post-pivot signed-surplus work

`SIGNED_SURPLUS_PIVOT.md` originally described Conjecture 3 as the new live all-order target. That **strategic framing was wrong** and is corrected. Its mathematical statements do not require Conjecture 3 to be true: they are identities and conditional implications inside the canonical bridge.

In particular, defining

`M(n)=floor((n-1)^2/4)+1`

is merely choosing a comparison threshold. Statements of the form "if `m>=M(n)` and the canonical boundary hypotheses hold, then ..." remain valid even though `m<=M(n)` is not universally true.

### Zero-residual order cutoff

The theorem in `ZERO_RESIDUAL_BOUNDARY.md` has the explicit hypothesis

`m>=M(n)`

and concludes that a non-bipartite D2C graph in the exact boundary `t=0, F=empty, r=0` must have `n<=294`. It does **not** assume that all D2C graphs satisfy `m<=M(n)`. The 12-vertex counterexample is inside the intended hostile-control regime rather than a contradiction to the theorem.

## What is changed by the false conjecture

The false 2019 statement changes:

- the **quantifier** of the active research goal: all-order is replaced by a sufficiently-large/eventual problem;
- the interpretation of the 12-vertex graph: it is a mandatory negative control;
- prose that previously called `M(n)` a valid universal stronger bound;
- any equality classification that was tied to the false all-order statement.

It does **not**, on the dependency audit performed here, require demotion of the existing Murty–Simon fixed-order candidates, the canonical bridge, the residual h-index inequalities, Hall majorization results, signed-surplus identities, or the zero-residual cutoff.

## Corrections made with this audit

The same repository checkpoint:

- corrects the attribution in the 7 September residual-h-index note to Hanson–Wang (2003) for the complement/total-domination correspondence;
- explicitly labels the Dailly–Foucaud–Hansberg 2019 dominating-edge result as a proved theorem distinct from their false Conjecture 3;
- marks `SIGNED_SURPLUS_PIVOT.md` as a historically corrected pivot and rephrases `M(n)` as an eventual-problem comparison threshold;
- corrects the wording in `DEFECT_TRIANGLE_ROOT.md` so it no longer presents the all-order second-extremal statement as valid;
- updates the root README and live handoff to expose the August 2026 proof collision, the 2024 counterexample, the dependency audit, the eventual target and the bounded three-day automated research window.

## Remaining audit boundary

This is a targeted dependency audit, not a fresh line-by-line external re-verification of every proof in the repository. The principal existing trust boundaries remain: external specialist review of the canonical bridge and structural lemmas, independent recompilation of the external `Erdos742/Erdos742` Lean development, and novelty review of the post-pivot Boolean-flow results.
