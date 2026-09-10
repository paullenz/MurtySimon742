# Exact n=29,t=3 compression and falsification of the naive t-parametric extrapolation

Date: 2026-09-10

Status: **exact finite RX-Hall evidence for the stated t=3 frontier, conditional on the graph-to-RX-Hall bridge; t=2 extrapolation falsified at the floating feasibility level.**

## 1. n=29,t=3 exact result

For the regenerated 94-profile n=29, Delta=16, t=3 RX-Hall frontier, the global two-coordinate monotone potential can be taken to be the primitive three-rectangle function

\[
F_3(d,v)=6B(3,0)+4B(3,5)+3B(3,9),
\]

where \(B(D,V)=\mathbf 1[d\ge D,\ v\ge V]\).

A corrected integer exactification and independent standard-library replay succeeded in GitHub Actions run **34496485698**.  The compact scalar-template reduction was subsequently checked directly with Python `Fraction` arithmetic, without LP/MIP participation in acceptance.

The current exact four-template family is:

- `A0`: lambda=140/81, tau3=29/12, tau4=23/12;
- `A1`: lambda=9/5, c=16/3, tau2=23/3;
- `A38`: lambda=9/5, c=141/70, tau2=841/210, tau3=1682/1155;
- `A530`: lambda=9/5, c=103/144, tau2=1513/720, tau3=3101/1440, tau4=109/144.

Exact four-template replay: GitHub Actions run **34497612545**.

Artifact id: **10160459068**.

Artifact SHA-256: **ef3fc892ce47f54c18d3adbf1488cfe2a8fa4e270d02ba851e529ad0f3278db3**.

The four templates cover all 94 profiles.  Their exact unique coverage in this family is:

- A0: profile 0;
- A1: profile 1;
- A38: profiles 38 and 88;
- A530: profiles 5 and 30.

The A530 template has exact gap 1 on profiles 5 and 30 and minimum positive gap 139/480 over its covered profiles.

A test forcing profiles 1..93 to share a single scalar vector is infeasible (run **34497692889**), so the most obvious two-template partition (profile 0 alone, all others together) does not work.  This is not a proof that four templates are globally minimal.

## 2. Verifier bug found and repaired

An earlier t=3 exactification run **34459995976** reported `FAIL_EXACT` despite zero exact row and bound violations.  The cause was a hard-coded check `len(margins)==902` inherited from the t=2 frontier.  The t=3 frontier has 94 strict profile rows, so the helper could never return PASS.

The helper was repaired in commit **6ee4c336902ba6a12e5d6911cb3703cc9899de44** by deriving the expected strict-margin count from the matrix.  The unchanged three-rectangle certificate then replayed successfully in run **34484239567**.

This is recorded as a verifier-control bug, not a mathematical failure.

## 3. A tempting but false t-parametric formula

The t=3 primitive weights suggest the aesthetically simple formula

\[
F_t=2tB(t,0)+(t+1)B(t,2t-1)+tB(t,3t).
\]

At t=3 this is exactly \(6B(3,0)+4B(3,5)+3B(3,9)\).

The natural t=2 prediction is therefore

\[
F_2^{\rm naive}=4B(2,0)+3B(2,3)+2B(2,6).
\]

This extrapolation is **falsified** on the 902-profile n=29,t=2 frontier.

GitHub Actions run **34497116957** completed successfully at the workflow level because the reconnaissance script intentionally records infeasibility as data rather than exiting nonzero.  Its actual mathematical output is:

- profiles: 902;
- rows: 334,159;
- variables: 20,515;
- HiGHS status: 2;
- message: `The problem is infeasible`;
- `success: false`.

A later template-cover attempt, run **34498191793**, independently rebuilt the same fixed potential and again found the decoupled LP infeasible before any cross-testing.

Therefore **no claim should be made that the three-term t=3 formula extends to t=2**.  An earlier conversational interpretation of the green workflow as mathematical success was incorrect; the logs/JSON are unambiguous.

## 4. Structural interpretation

The t=3 case is genuinely simpler than t=2 in the current RX-Hall relaxation.  The old exact t=2 proof uses a richer monotone potential with D=2,3,4 layers and diagonal slack cuts.  The failure of the naive three-term D=2 potential means that some t=2 profiles require information not encoded by those three rectangles.

The next falsification task is to identify the exact t=2 obstruction profiles and determine the smallest geometrically meaningful augmentation: an additional d-layer, a diagonal-slack cut, or a retained first-coordinate (s/rho) threshold.  No augmentation should be promoted until it is tested against all 902 profiles and exactified.
