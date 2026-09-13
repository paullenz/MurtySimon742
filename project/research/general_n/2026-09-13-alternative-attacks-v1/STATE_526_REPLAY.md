# State 526 replay

Run from `project/research/general_n/2026-09-13-alternative-attacks-v1/` with a C++17 compiler.

```bash
g++ -O3 -std=c++17 verify_state526_low.cpp -o verify_state526_low
./verify_state526_low

g++ -O3 -std=c++17 verify_state526_tail.cpp -o verify_state526_tail
for E in $(seq 16 34); do
  ./verify_state526_tail "$E"
done
```

Expected final low-excess summary:

```text
PASS low layers E=0..16; unique coarse equality is E=7, e2=7, e3=0^14, q2=1^2, q3=1^2,5^7,6^2.
```

The tail executable asserts the preserved minimum `(h,gap,q2_total)` for the requested layer. It reports gap zero only at `E=16`; every `E=17,...,34` has positive gap. `E=16` is already strictly excluded by the exact low-excess replay with minimum gap 23.

The hand rigidity exclusion of the unique `E=7` equality profile is in `STATE_526_WHOLE_STATE.md` and is not replaced by a machine assertion.
