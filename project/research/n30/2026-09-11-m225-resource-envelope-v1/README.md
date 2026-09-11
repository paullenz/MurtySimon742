# N30 equality endpoint: four joint-envelope certificates

11 September 2026. Continuation of the research checkpoint at `34763cb17ce554a27e57643cfb8e74882e66fc86` in `paullenz/MurtySimon742`.

**Candidate analytic/certificate reduction; exact arithmetic REPRODUCED. Independent mathematical review OPEN. No governed theorem-ledger promotion or new reviewer edition.**

The [four-envelope reduction](FOUR_ENVELOPE_REDUCTION.md) excludes **all 211 ledger-tight rows** at `n=30,Delta=16,m=225`. The four shared integer certificates cover `195+13+2+1` rows, with minimum assigned exact gap one. This includes all 207 positive-demand rows and the four zero-demand rows.

The new route keeps the joint source/label constraints, the exact residual budget, supplement Hall tails, and the individual selected-label cap `x_i<=#{u:rho_u>=s_i}`. It uses only the elementary degree bound `d_F<=12`, rather than the stronger isolated-C bound `d_F<=11` used in some historical endpoint models.

The earlier 61 positive-ledger-slack rows are already excluded by a short identity. Thus, **conditional on the complete 100-profile demand input**, the whole historical 272-row endpoint frontier can be excluded without its final LP/Farkas models. The current reviewer-v2 remains frozen and available with those original certificates.

**Later continuation:** the [hand classification of all 100 profiles](../2026-09-11-m225-hand-classification-v1/HAND_CLASSIFICATION.md) now supplies a candidate completeness argument with bounded arithmetic tables. It derives 70 cap-four profiles and 30 containing fives, rules out all higher preimages, and feeds its independently generated list into this checker with the same 211/211 result. The original files here retain their historical input boundary. The combined N30 route still needs envelope/assembly review and the separate Delta=17 work.

## Review and replay

- [Written reduction and all four formulas](FOUR_ENVELOPE_REDUCTION.md).
- [Small integer certificate file](JOINT_CERTIFICATES.json).
- [Full 211-row arithmetic appendix](EXACT_APPENDIX.md).
- [Independent standard-library checker](verify_joint_certificates.py) and [exact audit](EXACT_AUDIT.json).
- [Failure and boundary audit](ACCEPTANCE_BOUNDARY_AUDIT.json).
- [Provenance, unsuccessful attempts and next steps](HANDOVER.md).

From the repository root:

```sh
python -I -B project/research/n30/2026-09-11-m225-resource-envelope-v1/verify_joint_certificates.py
```

Acceptance imports no solver or discovery program. It reconstructs the tail-slack rows, checks all four templates on all 211 tight rows, and independently compares full integer-domain minima with piecewise-linear endpoint evaluations. The saved run records 12,772 direct state checks, 8,069 endpoint checks and 37,128 product-order comparisons. An incomplete cover exits with failure unless explicitly requested as exploratory output using `--allow-partial`.

The scripts prefixed `mine_`, `compress_` or `simplify_` are optional SciPy 1.17.0 discovery tools. Their output, including unsuccessful first attempts and a preliminary 210-row cover, is preserved with explicit provenance. Optimizer termination and optimality are not acceptance conditions; only the independently replayed integer certificate matters.

The original next target, the 100-profile hand classification, is now addressed by that candidate continuation. The next target is an audit of the full supplementary Delta=16 assembly and the separate Delta=17 dependencies before any new reviewer PDF edition is prepared.
