# Residual-mass-seven equality source-state screen

22 September 2026. Exact necessary physical-source enumeration over 51 optimistic equality-core orbits. No graph realization is claimed.

screen_r7_equality_sources.py imposes exact residual column sums, P-label selected-demand lower bounds, the selected-source missing-neighbour rule and selected-neighbour injection capacity. Repeated physical-source states are allowed. Residual-free states are asserted not to select P and cannot meet the positive lower bounds.

Of 51 core/slack orbits, 39 have zero source-multiset survivors. Twelve remain, carrying 211 exact necessary source multisets:
- (4,1,1,1): all 3 core orbits, 8 multisets total;
- (3,1,1,1,1): zero surviving core orbits;
- (2,2,1,1,1): 6 of 19 core orbits, 154 multisets total;
- (2,1,1,1,1,1): 3 of 23 core orbits, 49 multisets total.

The saved JSON names every surviving orbit and gives its exact count plus a representative multiset. These are C-layer kernels only. Unique supplements, selected B-edge injectivity, zero-label attachments, deletion criticality and actual maximum-root D2C realization remain untested.

The source script regenerates from R7_EQUALITY_CORE_SCREEN.json written by the same deterministic core program. The core program now supports an explicit --output path, avoiding shell-capture/source mismatch.

Next: regenerate all 211 populations and apply the supplement forcing rule. Equality at r=7 remains open until that screen and an independent replay succeed.
