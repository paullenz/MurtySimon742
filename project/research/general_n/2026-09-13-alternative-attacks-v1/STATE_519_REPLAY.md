# State 519 replay

13 September 2026. Exact integer replay for the N34 state-519 whole-state candidate exclusion.

Run from

```text
project/research/general_n/2026-09-13-alternative-attacks-v1/
```

with a C++17 compiler.

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_state519_low.cpp -o verify_state519_low
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_state519_exceptions.cpp -o verify_state519_exceptions
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_state519_tail.cpp -o verify_state519_tail

./verify_state519_low
./verify_state519_exceptions
./verify_state519_tail
```

Expected terminal summaries include

```text
PASS state 519 low/profile sweep E=0..24. Only coarse nonpositive profiles occur at E=6,8,9; dedicated availability replay must close those three layers.

PASS E=6 profiles=30 minimum_gap=2
PASS E=8 profiles=67 minimum_gap=4
PASS E=9 profiles=97 minimum_gap=2
PASS state 519 source-availability replay: all three coarse exceptional layers E=6,8,9 are strictly excluded.

PASS state 519 refined tail E=25..34 strict; E>=35 impossible by incoming capacity.
```

The tail minimum gaps are

```text
E=25  4
E=26  5
E=27 12
E=28  2
E=29  1
E=30  2
E=31  5
E=32 10
E=33 21
E=34 20
```

The canonical GitHub Actions replay is

```text
workflow: .github/workflows/verify-state519-whole-state.yml
run:      34773463128
job:      103767168163
commit:   99da77421870283eb8c276825097a637951ae799
runner:   Ubuntu 24.04
result:   SUCCESS
```

All proof-critical stages completed green. The run used exact integer arithmetic only; no floating solver infeasibility or timeout is used as proof.

External mathematical review and independent computational reproduction remain open.
