# Current structural review — 17 September 2026

The project now has four complementary structural layers. The latest was chosen after a deliberate step-back review: instead of inventing a new h/h-1 routing theorem from scratch, the existing canonical threshold-capacity theorem was rewritten in tail coordinates and found to already contain the required multi-level coupling.

## 1. Five-label exact block

[Five-label defect eleven is impossible](project/research/general_n/2026-09-17-d5-defect11-closure-v1/THEOREM.md) proves, under the whole-level exact-block hypothesis |T|=|H|=5,

    D >= 12,
    W >= 37,
    extras => W >= 57.

The preceding exact support-cover and pair-coverage packages supply the critical-edge machinery and independent finite checks. D=12 attainability, sharpness and external acceptance remain open.

The parameter-wide exact-block predecessor also supplies pair coverage, critical-edge support charging and the hand lower bound `D>=ceil(d(d-1)/4)` for general block size d.

## 2. Scope bridge via h-index saturation

[Residual h-index saturation and the exact-block equality face](project/research/general_n/2026-09-17-hindex-saturation-v1/HINDEX_SATURATION.md) revisits the general residual h-index argument. If h is the residual h-index, `|{rho>=h}|=h+u`, and k labels have demand h, then

    b+2t <= (a-h-u)(h-1)+k.

Equivalently, the older h-index upper bound loses the explicit stability term `a-k+u(h-1)`. When u=0, receiver containment forces `k<=h`; `k=h` is precisely the square exact block. This identifies the exact-block theory as a saturation face rather than an isolated hypothesis.

## 3. Destination bridge via receiver inflation

[Receiver inflation beyond h-index saturation](project/research/general_n/2026-09-17-receiver-inflation-v1/RECEIVER_INFLATION.md) adds a penalty that the scalar h-index theorem does not see. For a threshold q<h, omission counting bounds how many high sources can select at most q maximum-demand labels. The remaining selected mass cannot all use destinations inside the h+u high sources because selected representatives consume distinct B-pairs. Overflow to low destinations forces those receivers to carry at least q maximum-demand labels residually.

With `N=h+u`,

    ell_q=min(N,floor(ku/(k-q))),
    Y_q=max(0,kh-q ell_q-C(N,2)),
    z_q=ceil(Y_q/N),

one obtains

    r >= b+h(h-1)+u(h-1)+(q-1)z_q,

and hence

    b+2t <= (a-h-u)(h-1)+k-(q-1)z_q.

The accompanying exact dynamic programme checks the row-load relaxation for 6,090 parameter/threshold combinations. The graph implication remains a hand theorem by the same assistant, so external mathematical review is still required.

## 4. Coupled staircase / first peeling theorem

[Coupled demand/residual staircases and the first peeling inequality](project/research/general_n/2026-09-17-staircase-peeling-v1/STAIRCASE.md) rewrites the canonical threshold-capacity theorem in terms of demand-tail counts

    K_d=#{i:s_i>=d}

and residual-tail counts

    N_d=#{u:rho_u>=d}.

Positive surplus gives exact layer-cake identities

    S=sum_d K_d,
    r=sum_d N_d,

so the ledger becomes

    2t <= sum_d (K_d-N_d).

At every threshold d the existing pair-capacity theorem becomes the pure multi-level inequality

    d K_d + sum_{j>d} K_j
      <= d N_d + C(N_d-d,2).

For the top two levels, writing `k=K_h`, `K=K_{h-1}`, `N=N_h`, `M=N_{h-1}`, a non-square top level `k<=h-1` satisfies

    b+2t <= a(h-2)-1+K_*(M)-(h-2)M,

where

    K_*(M)=min(a, M-1+floor(C(M-h+1,2)/(h-1))).

If the residual staircase is flat across the top two levels, `N_h=N_{h-1}=h`, this collapses to

    b+2t <= (h-2)(a-h+1).

Hence, once `N_h=h`, a dense configuration above that threshold must either enter the exact square block or grow its residual tail immediately below h. At h=5,

    N_5=5 and b+2t>3a-12
      => K_5=5 or N_4>=6.

This is a direct structural narrowing of the exact-block coverage problem. The arithmetic elimination was brute-checked over 50,076 parameter triples; the inherited threshold-capacity graph theorem remains subject to external review.

## Strategic consequence

The scope problem is now better viewed as a staircase rather than a single equality face. There are three principal escape mechanisms:

1. excess top sources, penalized by h-index saturation and receiver inflation;
2. the exact square block, handled by the current critical-edge theory;
3. lower-level residual-tail growth, forced when demand migrates below the top level.

The next priority is to make the third branch recursive: combine the full staircase inequalities with receiver inflation and the 12 September heavy-load/routing family, and test whether repeated peeling must eventually reach a square block or accumulate too much residual-tail area for the layer-cake ledger.

**Status:** internal candidate mathematics. Exact-block coverage is narrowed but not solved. Canonical counts remain 4626 exclusions / 952 survivors / 3632 whole-state closures; no unrestricted Murty-Simon proof or catalogue promotion is claimed.

Use [CURRENT_STATE.md](CURRENT_STATE.md) for the live operational handoff. All earlier proofs, verifiers, failed routes and review material remain preserved.
