# Residual-mass-six equality source-state screen

22 September 2026. Exact necessary physical-source enumeration over the 13 optimistic equality-core orbits. This is not a graph search and does not close equality at r=6.

For each core/slack orbit from R6_EQUALITY_CORE_SCREEN.json, screen_r6_equality_sources.py enumerates source states on C with exact residual column sums, core selected-demand lower bounds, the missing-neighbour rule, and selected-neighbour injection capacity. Repeated states represent distinct physical B-sources and are permitted.

Residual-free selected patterns require special care because they consume no finite residual budget. The script proves/asserts that none can select a P-label; they may select whole N-components, but cannot help meet the only positive lower bounds. They are therefore omitted without strengthening the necessary screen. Completely adjacent sources remain arbitrary and irrelevant.

Eight of the 13 core/slack orbits have zero source-multiset survivors. Five remain:
- (3,1,1,1): all three core orbits survive, with 6,1,1 source multisets;
- (2,2,1,1): its sole core orbit survives with 3 source multisets;
- (2,1,1,1,1): only orbit 4 survives, with 20 source multisets; the other eight die.

The screen therefore reduces r=6 product equality from 13 optimistic cores to five source-supported cores and 31 source multisets. Each saved survivor is only a necessary C-layer object. Zero-residual attachment identities, B-edges, unique supplements, selected B-edge injectivity, deletion criticality and maximum-root graph realizability remain unchecked.

Exact output: R6_EQUALITY_SOURCE_SCREEN.json. Next: apply supplement uniqueness and selected-B-edge injectivity to all 31 multisets. Any survivors must still be treated as abstract kernels, not actual D2C graphs.
