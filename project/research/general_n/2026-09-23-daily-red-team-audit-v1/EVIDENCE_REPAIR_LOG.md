# Evidence repair log

Audited predecessor: `320ff91c4b3b1c64e98349788f9f971f65a9ef01`.

Two purported evidence files contained tool-output truncation markers and were not replayable:

- `../2026-09-22-zero-demand-equality-v1/R8_EQUALITY_CORE_SCREEN.json`
- `../2026-09-22-r11-quotient-v1/r11_support9_masks.txt`

The exact corrupt bytes are preserved as `R8_EQUALITY_CORE_SCREEN.corrupted-at-320ff91.json` and `r11_support9_masks.corrupted-at-320ff91.txt`.

Repairs were source regenerations, not manual editing:

1. `python screen_r8_equality.py > R8_EQUALITY_CORE_SCREEN.json`
2. `python verify_r8_pipeline.py` -> PASS: strict labelled 11,350; strict orbits 68; equality labelled 26,838; equality orbits 203; equality source-feasible 39; source populations 2,103; supplement survivors 0.
3. `g++ -O3 -std=c++17 r11_support9_orbits.cpp` followed by direct file output -> 3,273 strict support-nine rows.
4. `python audit_r11_pipeline.py` -> PASS: strict rows 2,496 / 3,273 / 280; source survivors 16 / 8 / 3; supplement survivors 0 / 0 / 0.

This repair restores internal reproducibility. It is not external verification and does not independently reimplement the algorithms.
