# Independent replay of the r=9 support-eight closure

> **Substantive review — 24 September 2026:** A substantive review on 24 September found that the historically committed Python audit file contained only a timestamp. The present audit_r9_support8_orbits.py is a fresh reconstruction, not recovered historical code. Fresh C++ enumeration and a separate Burnside/group-action check reproduce 1,044 / 79,264 / 69 and all saved masks. The new explicit decimal-line checksum is recorded in the substantive review; the old checksum above did not state its serialization and is not used as the new integrity pin.


22 September 2026. Internal replay; no external review.

A separate Python group-action audit reproduces the generator's two global counts by Burnside's lemma: 1044 unlabelled graphs on seven unit labels and 79,264 rooted/coloured graphs when the residual-2 label is distinguished. It independently verifies that the 69 saved strict masks are distinct, pairwise inequivalent under all 5040 allowed permutations, and satisfy the recorded optimistic strict conditions. Of them, 60 have t_upper=1 and 9 have t_upper=2. Sorted-mask SHA-256 is `5bf755609d1c8f7ea7b513aaec15a224a442e45c11516e63e462be8f15f57297`.

A second implementation formulates physical-source feasibility as an integer linear program, independently of the memoized DP. SciPy/HiGHS reports all 69 systems infeasible (status 2), with 640–946 allowed source-pattern variables per orbit. This agrees with the zero-survivor DP.

These checks materially strengthen the internal r=9 closure but do not constitute external proof review. They audit the finite quotient and source-feasibility layers; the inherited graph-to-profile bridge retains its existing internal-candidate trust boundary.
