# Murty–Simon / Erdős #742 — current state handoff

**14 September 2026. Latest research: capped positive-excess charge and all-source spill. Proof `f1f9ea055233bf5bff4499f3f7981591a2f20765`, verifier `ea77b7372cf19b0dce74fbca9bcc8649757600c6`, frozen evidence `18cafdf20c5ab0d31c4c79f767f721b2064efa88`, reproducible CI `552fd57e9160467e0a70e9150c7ed8491c213ab8`. Inspect newer commits and live CI before resuming.**

Canonical repository: `paullenz/MurtySimon742`, ID `1359206057`. The full preceding priced-tail handoff is permanently preserved [at commit 0b8ba460](https://github.com/paullenz/MurtySimon742/blob/0b8ba460064f7441a8f92cc6f7434193039b7db5/CURRENT_STATE.md). `CURRENT_STATE_PRE_PRICED_2026-09-14.md` and earlier archives retain the localized, interval, selected-loss, q-layer and recovery chronology. No proof files or failed approaches were removed. No unrestricted proof, graph realization or whole-state promotion is claimed.

## Canonical promoted frontier — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — UNPROMOTED
```

The fixed-order candidates n=25 and n=27 through n=35, and the general 7/12 candidate theorem, are unchanged. External mathematical review and novelty assessment remain OPEN. These candidate packages are separate from the scalar generalisation frontier; scalar survivors are not graphs. Preserve both reviewer navigation surfaces.

## GitHub queue intervention and actual audit progress

The user requested a GitHub kick. Commit `6a66d18654b501abe02002e0d2a4d178c8657207` added `.github/workflows/kick-short-verifiers.yml`: a bounded, read-only fresh replay of the localized and priced verifiers on `ubuntu-24.04-arm`, with complete frozen-value checks and fully paginated audit-job diagnostics. It does NOT cancel or duplicate the 256-shard audit. An alternate architecture is a fresh allocation request, not scheduling priority or a bypass of account concurrency limits.

Direct observations:

| Run | Latest observation in this synchronization |
|---|---|
| `34883538561`, short-verifier kick | Queued; job `104108421139` has not started. |
| `34885163695`, new capped-spill CI | Created from `552fd57e`; queued. |
| `34880833888`, original localized verifier | Rechecked; queued, no steps. |
| `34854911792`, 2,655-candidate audit | Incomplete but making progress: new shard evidence downloaded; final indexed shard 255 still queued and no accepted aggregate. |

The audit artifact listing had 87 artifacts at one observation; that is NOT a claim of 87 successful shards. Its newest artifact was `10364625816`, `post-pair-relational-final-audit-shard-90`, uploaded at 2026-09-14 18:55:54 UTC. Its downloaded `AUDIT_STATUS.json` was checked: `finished=true`, `states_expected=11`, `states_audited=11`, `unresolved=[]`. Audited keys were (0,1694), (0,3190), (0,5194), (0,6144), (0,7129), (0,7841), (0,8475), (0,9191), (0,10002), (0,11002), (1,436). The archive SHA256 is `a842b781ddf9f27777d8085b08da44dbab1884c295636a0d70fdd417a5934db1`.

Do not diagnose the whole audit as stalled merely from its run-level queued label. Do not restart successful shards or the whole audit to try to accelerate allocation. Promotion requires ALL 2,655 inputs, both implementations agreeing state by state, zero unresolved, successful aggregate, then a separate ledger commit. Candidate discovery SHA256 remains `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`.

Earlier directly checked successes remain: frozen ledger `34875592126`, threshold `34871045562`, corrected mincut `34878019517`. Original mincut `34868771056` passed its mathematics but failed a raw JSON-format comparison; the repair retained all frozen values. These green gates do not complete the relational audit. No current platform-wide outage or quota diagnosis has been established.

## New main hand inequality

Read [`project/research/general_n/2026-09-14-capped-spill-v1/README.md`](project/research/general_n/2026-09-14-capped-spill-v1/README.md).

Keep notation exact:

```text
Q=r+2t+D0+Esel, delta=b-a,
x_i=s_i+e_i, z=#{i:s_i=0},
v_u=(q_u-z)_+, d_u=(p_u-rho_u+1)_+.
```

`t` is structural surplus, `tau` a q threshold, `eta` a label-demand threshold. Never constrain z by z<=Esel. At selected positive-demand labels, canonical endpoint forcing gives d_u<=e_i. The incoming cap also gives d_u<=delta. Hence

```text
sum_u v_u d_u
 <= sum_{i:s_i>0}(s_i+e_i)min(e_i,delta).
```

Let

```text
M0=sum_u(q_u-#{i:0<s_i<=rho_u})_+,
B=Esel-M0>=0, smax=max_i s_i.
```

M0 is excess forced onto zero-demand labels, which cannot fund the positive-label charge. The strongest new closed-form bound is

```text
sum_u(q_u-z)_+(p_u-rho_u+1)_+
 <= B[smax+min(B,delta)].
```

When B>=delta, this is LINEAR in B, replacing the older quadratic envelope Esel(Esel+smax). Its bridge use depends on the incoming cap and positive-label endpoint forcing; these hypotheses cannot be silently omitted.

For the priced tail with A_w=min(P_w,J_w(tau)), f_w=min(A_w,rho_w-1), g_w=A_w-f_w, substitute the new right side into

```text
theta(Q_tau-sum f_w)-sum_w(theta-v_w)_+g_w <= charge envelope.
```

A tail can have enough capacity but still be too expensive. No universal high-q-tail sufficiency theorem is assumed.

## All-source spill and the integer envelope

For L_eta={i:s_i<=eta}, let

```text
f_u(eta)=(q_u-#{i:eta<s_i<=rho_u})_+,
M_eta=sum_u f_u(eta), S_eta=sum_{i in L_eta}s_i,
C_{eta,w}=Esel+S_eta-M_eta+f_w(eta).
```

Removing w's own forced spill before counting its actual k low-block selections avoids double counting. The exact necessary inequality is

```text
C_{eta,w}>=k+(q_w-k)d_w when d_w>=1.
```

With m=#{i:s_i<=min(eta,rho_w)} and kstar=min(m,q_w,C), q_w>kstar gives

```text
p_w<=rho_w-1+floor((C-kstar)/(q_w-kstar)).
```

Take the minimum with EVERY prior cap, particularly exact potential-pair degrees. Negative caps reject a branch. Unlike the preceding localized theorem, this counts unavoidable low-label selections from all sources. The +f_w term is essential; a counterexample to omitting it is preserved in the proof note.

A prefix dynamic programme further maximizes the capped positive-label charge over INTEGER excess vectors with total Esel, per-label selected-incidence upper bounds, and all equal-demand-prefix spill lower bounds. The actual excess vector belongs to this projection. Its optimum is therefore a safe upper bound, but exactness is only for that explicitly relaxed budget problem, NOT for selectable matrices or graph realization. Constraints on an equal-demand block are imposed after the whole block.

## Completed local verification and finite reach

`verify_capped_spill.py` was executed locally and its committed blob checked against the executed file. It imports no production scanner. `CAPPED_SPILL_VERIFICATION.json` freezes every value.

```text
exhaustive selected-incidence configurations: 133,586
pressure/cap/envelope checks (delta=1,2,4):    400,758
independent brute-force DP comparisons:        3,000
  feasible / empty projections:          1,179 / 1,821
standing hostile q-tail examples:                  3
frozen difficult profiles replayed:              812
```

On the 812, spill tightens one further cap vector (row 811, state 6085): full-capacity contradictions increase from 630 to 631; uniform interval detections stay 773; adaptive interval detections remain 812. These profiles were already excluded by other tails. No new whole-state closure follows.

The original fixed-seed 100,000-trial synthetic generator was regenerated locally from its committed source and frozen scanner. It reproduces all previous totals and the 713-row corpus. Shared generation is NOT an independent generator. TSV SHA256: `157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572`.

```text
prior localized/priced rejections:               652 / 713
all-source spill with old quadratic envelope:     654 / 713
spill with new closed-form capped envelope:       672 / 713
spill with exact integer prefix envelope:         694 / 713
not rejected:                                     19 / 713
```

Thus 42 of the former 61 sampled survivors are newly rejected. This is NOT a 42-state frontier reduction. All new/remainder row IDs and the explicit arrays are preserved in frozen outputs and the reproducible corpus.

The old published unrejected witness, zero-based row 4, now has a short certificate. It has Esel=34, M0=26, B=8, delta=smax=3. The closed-form upper cost is 8(3+3)=48. At tau=1, theta=4, previous localized caps already force cost at least 4(96-31)-203=57. Therefore **57>48**. The integer-envelope upper bound is 46 but is not needed. No interval tail is deficient on this profile with the new caps; the price genuinely adds a constraint beyond interval-tail deficiency.

The remaining synthetic row IDs are 39,76,108,119,160,240,258,295,338,342,347,365,406,471,570,586,664,682,688. Passing remains no graph-realizability evidence. Do not assert all-order closure from this sample.

## Retained previous achievements and next research target

The priced-tail package retains its fixed tau=3 detection of all 812 localized difficult profiles and its Hall-or-price explanation of all 205,931 OLD exported rows, including the 80>77 state-4073 fixture. Those larger exports were NOT regenerated in this capped-spill session. Eliminating old early-stopping witnesses still requires exploring omitted source-state continuations before a whole-state claim.

The old-cap fixed-weight obstruction remains valid for OLD caps; it does not transfer automatically to new caps. Preserve all hostile examples, 32 frozen interval strict gaps, zero-demand corrections and incomplete wider scans. Exact q-layer/minimum-cut and crossing-wall routes remain fallbacks; check fixed-q monotonicity before transferring witness theorems to modified caps. The independent maximum-cut/stability route remains preserved.

Next: attack the 19 explicit synthetic survivors using joint residual/selected realization, sharper column constraints or source-specific pressure, rather than merely fitting another empirical threshold. Continue bounded source-state scans separately, with complete coverage and independent replay. The main hand target is a structurally forced priced-tail violation with the new capped budget.

Local proof checks, same-assistant independent implementation, remote CI, external mathematical review and third-party reproduction are distinct. No timeout, missing output, failed search or floating infeasibility is proof. The canonical graph-to-selected/residual bridge remains the principal correlated external-review dependency.
