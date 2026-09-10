# n=29, t=2 all-902 three-layer exact compression — 10 September 2026

Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status:** exact finite evidence inside the candidate RX-Hall framework. This is not an unrestricted Murty–Simon theorem, does not replace the fixed-order n=29 proof, and remains conditional on the universal graph-to-demand / BC compatibility bridge. Independent mathematical review remains open.

## 1. Pinned finite frontier

All runs regenerate the committed n=29, t=2 frontier from `minimal_prepare.py` and `minimal_rows.cpp`. The resulting positive-demand frontier contains **902 profiles**. Each common-potential model below has **334,159 finite inequalities**.

The independent replay is standard-library Python only. It imports neither SciPy/NumPy nor the exactifier/LP builder: it independently reconstructs deterministic variable order, label/source envelope inequalities, margin inequalities and bounds, then checks the stored integer numerator vector.

## 2. First exactification: three consecutive d-layers + J0,J1,J2

Workflow `General RX-Hall n29 t2 three-layer exact`, run **34455724749**, exactified both compact overnight candidates.

### Layers D={1,2,3}

- 902 profiles; 334,159 rows; 20,552 variables.
- Allowed support: 19 rectangles + 3 diagonal slack thresholds `J_2,J_1,J_0` (K=14,15,16).
- Exact acceptance: denominator scale `10^6`, whole-point boost `2`.
- Homogeneous-row maximum LHS: `0`.
- Worst profile margin numerator: `-1,999,868`, versus required `-1,000,000`.
- Row violations: `0`; bound violations: `0`.
- Independent replay: **PASS**.
- Artifact: `10143482769`, archive digest `sha256:908446759d22429711b56133348395ba94676e6ba45eb8be4000752c8ebb89f5`.
- Exact JSON SHA256: `2f24d484a41221372d6c136653e9ea57b67958350672adb2bcdf148b7a9996a9`.
- Replay JSON SHA256: `378bb3257944b104557bcf3985889246e9e097b53186b238899283b181ad471f`.

### Layers D={2,3,4}

- 902 profiles; 334,159 rows; 20,552 variables.
- Allowed support: 17 rectangles + 3 diagonal slack thresholds `J_2,J_1,J_0`.
- Exact acceptance: denominator scale `10^6`, whole-point boost `2`.
- Homogeneous-row maximum LHS: `0`.
- Worst profile margin numerator: `-1,999,828`, versus required `-1,000,000`.
- Row violations: `0`; bound violations: `0`.
- Independent replay: **PASS**.
- Artifact: `10143513705`, archive digest `sha256:ddd18ffda7002856254eebb209295a56ac29924d7edf7348ba2591162602c660`.
- Exact JSON SHA256: `88d194d624a0504e7fee1fd6c073f8cf7dd72f0afe55caa303b84ec6a1aa41aa`.
- Replay JSON SHA256: `2f3c6dbd3fb229e48eac175323743408e0b736433e454c44126df8222d12797a`.

This upgrades the two overnight three-layer candidates from floating reconnaissance to exact finite rational evidence.

## 3. Diagonal ablation

Workflow `General RX-Hall n29 t2 three-layer diagonal ablation`, run **34455927836**, tested which second diagonal threshold can accompany `J_0` while retaining all rectangle thresholds on each selected three-layer family.

| d-layers | J0+J1 | J0+J2 |
|---|---:|---:|
| `{1,2,3}` | **infeasible** | **feasible** |
| `{2,3,4}` | **infeasible** | **feasible** |

Separately, the earlier unrestricted-rectangle ablation found `J0+J1` and `J0+J2` feasible but `J1+J2` infeasible, while `J0` alone was already known to fail all 902. Thus within the three-layer compression, the useful two-step slack language is specifically **J0 + J2**.

The two positive diagonal-pair results in this section are floating support discovery only; their exactification is the next section.

## 4. Stronger exactification: J0 + J2 only

Workflow `General RX-Hall n29 t2 three-layer c02 exact`, run **34456420686**, exactified the successful two-diagonal candidates and replayed them independently.

### D={1,2,3}, J0+J2

- 902 profiles; 334,159 rows; 20,551 variables.
- Allowed support from the ablation: 20 rectangles + 2 diagonals = 22 generators.
- The accepted exact point actually has **20 nonzero generators** (18 rectangles + `J_2,J_0`); two allowed rectangle coordinates vanish exactly.
- Exact acceptance: scale `10^6`, boost `2`.
- Homogeneous-row maximum LHS: `0`.
- Worst profile margin numerator: `-1,999,887`, versus required `-1,000,000`.
- Row violations: `0`; bound violations: `0`.
- Independent replay: **PASS**; variable-order hash matches.
- Artifact: `10143762203`, archive digest `sha256:3beeb24261aa7542500e6f9553648feb3a9b316a447d20b6b8676e90ef2e4abd`.
- Exact JSON SHA256: `4577f3d48a52ecdeeaff428bfad7022d5d3cfddc271ace10f21ea9a4fd005be9`.
- Replay JSON SHA256: `e9d7ed043533e159289bc6a59f73d4686ba8690ca3b548291de9c1225a0a2d1d`.

### D={2,3,4}, J0+J2 — current cleanest candidate

- 902 profiles; 334,159 rows; 20,551 variables.
- Allowed support from the ablation: 17 rectangles + 2 diagonals = 19 generators.
- The accepted exact point actually has **18 nonzero generators** (16 rectangles + `J_2,J_0`); the allowed `B_(4,1)` coordinate vanishes exactly.
- Exact acceptance: scale `10^6`, boost `2`.
- Homogeneous-row maximum LHS: `0`.
- Worst profile margin numerator: `-1,999,819`, versus required `-1,000,000`.
- Row violations: `0`; bound violations: `0`.
- Independent replay: **PASS**; variable-order hash matches.
- Artifact: `10143779359`, archive digest `sha256:7dbb9a85412891145ab5a72b94735a7a14c1480b5d5902938e7d55a462944ed4`.
- Exact JSON SHA256: `aaed0dedbab29839d3b244e380a2568df5ac185e4ecbc3ddf284e75bcb3ed339`.
- Replay JSON SHA256: `f1f3bde3098056675410af96f85bc670d762c19b5dd0a0819aae093035a69c7d`.

The 18 nonzero global generator numerators at denominator `10^6` are:

```text
B(2,11)  2,086,417
B(2,12)  2,174,611
B(2,13)  5,513,698
B(2,14)  1,493,936

B(3,0)   7,839,514
B(3,2)      44,359
B(3,4)     715,789
B(3,5)     812,953
B(3,7)   1,564,813
B(3,8)   1,564,813
B(3,10)  2,086,417
B(3,12)  1,034,719

B(4,2)     826,698
B(4,3)   1,088,821
B(4,6)   1,069,862
B(4,9)   1,564,813

J2        2,973,384
J0        2,755,434
```

These integers describe the common global potential in the accepted scaled exact certificate. Profile-specific scalar/envelope coefficients are retained in the Actions exact payload and are reproducibly regenerated by the pinned exactifier.

## 5. What is and is not established

Established exactly at the finite-model level:

> Every one of the 902 regenerated n=29,t=2 profiles is contradicted by one common BC potential using only the three d-threshold layers D=2,3,4 and the two exact cumulative slack thresholds c=0,2; the accepted certificate and an independently coded integer replay have zero violations.

Not established:

- support minimality of the 18 nonzero generators;
- a parameter rule for the rectangle thresholds/weights;
- extension to arbitrary `(n,b,t)`;
- independent external validation of the graph-to-incidence/BC bridge.

## 6. Next attack

Priority order after this checkpoint:

1. treat the **18-nonzero D={2,3,4}, J0+J2** potential as the principal t=2 compression;
2. perform generator-removal ablations, beginning with the tiny `B(3,2)` coefficient and other low-weight rectangles, to identify indispensable shape;
3. re-exactify any smaller common support immediately;
4. rewrite surviving rectangle layers as monotone step functions in original `(d,h)` coordinates and search for a short parameter rule;
5. only after that use n=30/n=31 as falsification laboratories for the symbolic rule.
