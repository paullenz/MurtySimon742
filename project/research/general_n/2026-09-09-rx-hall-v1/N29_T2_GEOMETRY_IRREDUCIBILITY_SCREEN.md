# n=29, t=2 RX-Hall geometry irreducibility screen

10 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status:** floating-point structural reconnaissance inside the candidate RX-Hall relaxation. This note does **not** upgrade the fixed-order n=29 theorem claim, does not prove global support minimality, and remains conditional on the graph-to-RX-Hall bridge. The already-preserved 16-generator t=2 potential remains the exact proof-grade finite certificate.

## 1. Motivation

The exact t=3 frontier admits the very small potential

\[
6B(3,0)+4B(3,5)+3B(3,9).
\]

A tempting t=2 analogue

\[
4B(2,0)+3B(2,3)+2B(2,6)
\]

was falsified on the 902-profile n=29,t=2 frontier. The question was whether only the coefficients were wrong, or whether t=2 genuinely needs richer Hall geometry.

## 2. Fixed-weight obstruction set

Workflow run **34498572156** recursively isolated **107 of the 902 profiles** that are individually infeasible with the fixed potential `4 B(2,0)+3 B(2,3)+2 B(2,6)`.

Artifact id: **10160906457**

Artifact SHA-256: **38081b8a2bf8d8f0ecd822e28b376b16506d089304487ebd2f3a540f1de0e72b**

These 107 profiles are not a single narrow exceptional type: `min(s)` is 1 in 33 cases, 2 in 44, and 3 in 30; 95 have `max(s)=4` and 12 have `max(s)=5`.

## 3. The three-rectangle support itself fails

The same support

```text
B(2,0), B(2,3), B(2,6)
```

was retested with **arbitrary free nonnegative common weights** over all 902 profiles.

Workflow run: **34499750831**

Artifact id: **10161347827**

Artifact SHA-256: **8e5f8c153a9a2156eee2dedeb84f0f1cbf353fe6a569b8f75dee89447cecebf2**

Result: HiGHS infeasible on 334,159 inequalities in 20,515 variables.

Thus the failure is geometric, not merely a poor `4:3:2` coefficient choice.

## 4. A whole single d-layer is still insufficient

Allowing **every** rectangle `B(2,V)`, `V=0,...,16`, with arbitrary common weights is also infeasible on all 902 profiles.

Workflow run: **34499903858**

Artifact id: **10161441824**

Artifact SHA-256: **ecc4446eb2b0a60be38b7b16048524d830cfcfbc4370d21f575cf1c82a244e63**

Result: HiGHS infeasible on 334,159 inequalities in 20,515 variables.

## 5. Full-902 hierarchy tests

Workflow run **34499397811** tested successively richer common potential families on all 902 profiles. Artifact id **10161380087**, SHA-256 **0feb16a8e0428dd60fae0e506c2f0c87a110ba9c58183c91ed3ae8af581e94b6**.

| potential family | floating result |
|---|---|
| three free rectangles `B(2,0),B(2,3),B(2,6)` | infeasible |
| all `D=2` rectangles | infeasible |
| all `D=2` rectangles + `J_0,J_2` | infeasible |
| all `D=2,D=3` rectangles | infeasible |

So neither the natural diagonal slack cuts by themselves nor simply adding the next d-layer is sufficient.

## 6. Fast 107-obstruction family screen

Workflow run **34500036709** then tested broader families on the 107 obstruction profiles only.

Artifact id: **10161476255**

Artifact SHA-256: **d7799260fa215c1be7377b5f41e1cf0d2f088068eebe2e6d7fb328e4d60c1f27**

Results:

| family | result on bad107 |
|---|---|
| D2 | infeasible |
| D2 + J0 | infeasible |
| D2 + J2 | infeasible |
| D2 + J0 + J2 | infeasible |
| D2 + D3 | infeasible |
| D2 + D4 | infeasible |
| D2 + D3 + J0 + J2 | infeasible |
| D2 + D4 + J0 + J2 | infeasible |
| D2 + D3 + D4 | infeasible |
| **D2 + D3 + D4 + J0 + J2** | **feasible** |

Here `Dk` means the complete rectangle layer `B(k,V)` over `V=0,...,16`; `J_c=1[d+v>=16-c]`.

The sole feasible family had 21 active generators in the returned optimum. The active support included all three d-layers and both diagonals.

## 7. Structural interpretation

Within this tested two-coordinate BC/diagonal basis, the t=2 obstruction profiles strongly distinguish the full family

\[
D=\{2,3,4\},\qquad c=\{0,2\}
\]

from the natural simpler alternatives. This is exactly the **family language** used by the trusted exact primitive 16-generator potential:

\[
F=A_2(v)1[d\ge2]+A_3(v)1[d\ge3]+A_4(v)1[d\ge4]+15J_2+14J_0.
\]

This alignment is more meaningful than the falsified simple coefficient formula. It suggests the parameter-derived architectural language

\[
D=\{t,t+1,t+2\},\qquad c=\{0,t\}
\]

may be the reusable object, with some layers/cuts allowed to receive zero weight in easier frontiers.

For comparison:

- t=1, n=30: exact solution uses D={1,2,3}, c={0,1}, plus one retained first-coordinate threshold `s>=2`;
- t=2, n=29: exact solution uses D={2,3,4}, c={0,2};
- t=3, n=29: exact solution collapses further to three rectangles on D=3 and needs neither diagonal nor first-coordinate correction.

## 8. What is not yet proved

The screen does **not** prove that each of the five families `D2,D3,D4,J0,J2` is individually indispensable. The tested ablations already establish necessity of D3 and D4 within several broad combinations, and establish that some diagonal information is necessary when all three d-layers are present. The next targeted tests are:

1. `D2+D3+D4+J0` (drop J2);
2. `D2+D3+D4+J2` (drop J0);
3. `D3+D4+J0+J2` (drop D2);
4. full family as a control.

If the first three are infeasible already on the bad107 set, then all five family components are irreducible within this BC/DST basis on that obstruction set. That still would not imply individual-generator minimality or a universal graph theorem.
