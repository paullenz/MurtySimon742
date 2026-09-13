# State 588 replay

Run from `project/research/general_n/2026-09-13-alternative-attacks-v1/` with any C++17 compiler.

```bash
g++ -O3 -std=c++17 verify_state588_low.cpp -o verify_state588_low
./verify_state588_low

g++ -O3 -std=c++17 verify_state588_tail.cpp -o verify_state588_tail
./verify_state588_tail

g++ -O3 -std=c++17 verify_state588_exact_16_24.cpp -o verify_state588_exact_16_24
./verify_state588_exact_16_24
```

Expected terminal summaries:

```text
PASS low layers E=0..15; unique coarse equality is E=9, e=0^12,3^3, q=3^6,6^6.
PASS h2 relaxation: all E=17..23 and 25..34 strict; only E=16 and E=24 need exact-profile replay.
PASS E=16 and E=24: every excess profile is strictly excluded or source-infeasible.
```

The hand rigidity exclusion of the unique E=9 equality profile is in `STATE_588_WHOLE_STATE.md` and is not replaced by a machine assertion.
