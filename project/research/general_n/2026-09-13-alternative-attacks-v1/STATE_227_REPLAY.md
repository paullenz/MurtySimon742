# State 227 replay commands

13 September 2026. Run from this directory with a C++17 compiler.

```bash
g++ -O3 -std=c++17 verify_state227_exact_to20_replay.cpp -o verify_state227_exact_to20
./verify_state227_exact_to20

g++ -O3 -std=c++17 verify_state227_tail.cpp -o verify_state227_tail
./verify_state227_tail
```

The first executable checks the complete excess-profile table for `E=0,...,20`. Its only non-strict cases are the preserved `E=6` and `E=7` equality profiles, which require the hand rigidity arguments in `EXCESS_SWEEP_TO_8.md`.

The second executable checks the relaxed `h_2` tail minima for `E=21,...,34` and the `E>=35` incoming-capacity ceiling.

Both programs use integer arithmetic only. No LP/MILP solver status is used as proof.
