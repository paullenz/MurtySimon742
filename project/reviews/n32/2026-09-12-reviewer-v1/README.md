# N32 reviewer-v1

12 September 2026.

**Candidate theorem:**

```text
e(G) <= 256 = floor(32^2/4),
with equality exactly K(16,16).
```

Independent mathematical review, novelty assessment and independent computational reproduction remain **OPEN**.

Reviewer order:

1. [`PROOF.md`](PROOF.md) — complete fixed-order assembly.
2. [`HOSTILE_AUDIT.md`](HOSTILE_AUDIT.md) — same-assistant hostile audit; no blocking flaw found, external review still required.
3. [`../../research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md`](../../research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md) — exact t=1 finite accounting.
4. [`../../research/n32/2026-09-12-equality-v1/HAND_EXCEPTION.md`](../../research/n32/2026-09-12-equality-v1/HAND_EXCEPTION.md) — hand contradiction for the sole full-RX equality survivor.
5. [`../../research/n32/2026-09-12-t2-frontier-v1/N32_T2_RECTANGLE_POTENTIAL.md`](../../research/n32/2026-09-12-t2-frontier-v1/N32_T2_RECTANGLE_POTENTIAL.md) — exact 257-edge closure.
6. [`../../research/n32/2026-09-11-hand-route-v1/`](../../research/n32/2026-09-11-hand-route-v1/) — 258-edge hand closure and fourteen-label theorem application.

Replay the equality layer from repository root with:

```sh
bash project/research/n32/2026-09-12-equality-v1/run_replay.sh
```

### Important dependency note

All `Delta=17` finite models use `d_i<=12`. This is justified uniformly for every positive `t` by the isolated-C lemma: with `(a,b)=(14,17)`, an isolated C-vertex would force `17<=13-t`, impossible for `t>=1`. Thus `delta(C)>=1` and `d_F(i)<=12`. The hostile audit records this explicitly because the main proof first spells the cap out in its zero-demand subsection.

### Review priorities

The highest-value mathematical review is not to rerun SciPy first. It is to attack:

- the universal selected/residual graph bridge;
- threshold capacity and its equality case;
- endpoint load / source-degree forcing;
- completeness of the t=1 monotone-tail expansion;
- the strengthened zero-demand `(d,R,x)` model.

The exact replay then addresses arithmetic/implementation risk conditional on those lemmas.
