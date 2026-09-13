# State 279 replay commands

13 September 2026. Run from this directory with a C++17 compiler.

```bash
g++ -O3 -std=c++17 verify_state279_low.cpp -o verify_state279_low
./verify_state279_low

g++ -O3 -std=c++17 verify_state279_tail.cpp -o verify_state279_tail
./verify_state279_tail
```

The first executable reproduces the complete `E=0,...,15` coarse-envelope table and the unique q-vectors for the three non-strict profiles. Those three profiles require the hand rigidity arguments in `STATE_279_WHOLE_STATE.md`.

The second executable checks the relaxed `h_2` tail minima for `E=16,...,34` and the `E>=35` incoming-capacity ceiling.

Both programs use integer arithmetic only. No LP/MILP solver status is used as proof.
