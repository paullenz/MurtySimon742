# State 382 replay

Run from `project/research/general_n/2026-09-13-alternative-attacks-v1/` with a C++17 compiler.

```bash
g++ -O3 -std=c++17 verify_state382_low.cpp -o verify_state382_low
for E in $(seq 0 17); do
  ./verify_state382_low "$E"
done

g++ -O3 -std=c++17 verify_state382_tail.cpp -o verify_state382_tail
for E in $(seq 16 34); do
  ./verify_state382_tail "$E"
done
```

Every low-excess invocation asserts that all profiles at that E are strictly excluded and checks the preserved minimum gap. The tail executable asserts the preserved minimum `(h,gap,q2)` for each layer.

The refined tail reports a negative relaxed gap only at `E=16`; that layer is already strictly excluded by the exact low-excess replay with minimum gap 17. Every `E=17,...,34` tail layer is strict.

No separate hand-rigidity case is needed for state 382.
