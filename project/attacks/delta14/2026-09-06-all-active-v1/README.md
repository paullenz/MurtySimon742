# Delta=14 all-active candidate closure — 6 September 2026

## Status

PROPOSED COMPLETE DELTA14 CLOSURE, PENDING MATHEMATICAL PROOF REVIEW.

This is new attack work, not recovery or promotion of old SAT results. The historical theorem ledger and the parked Delta=15 checkpoint are unchanged. No completed n=25 theorem or equality characterization is claimed.

The candidate theorem excludes a 25-vertex diameter-2-critical graph with 157 edges and maximum degree 14. A new inactive-vertex inequality gives r >= e(F)+e(F[N_A(b)]) whenever b has no residual cross-edge. Since e(F)=r+3, every B vertex must instead be residual-active, so r>=14. Short quasi-edge counting arguments exclude k=0,1; r<=42-5k excludes k>=6. Two separately implemented exact arithmetic verifiers then exclude every degree/residual state for k=2,3,4,5.

## Checks completed in this session

| k | residual range | outer states | survivors |
|---|---|---:|---:|
| 5 | 14..17 | 21 | 0 |
| 4 | 14..22 | 572 | 0 |
| 3 | 14..27 | 6764 | 0 |
| 2 | 14..32 | 51907 | 0 |
| Total | 46 bands | 59264 | 0 |

Both programs agree on every state key, every band disposition, and all 1480 labelled residual-column vectors and their source capacities. The last 110 column cases are two r=22 equality patterns, each with ten residual-degree-one vertices and four residual-degree-three vertices. A hand contradiction requires seven distinct supplements where only three can qualify.

The programs use only exact integer arithmetic and the Python standard library, with no SAT solver, graph catalogue or isomorphism engine. Twelve unit/negative tests passed. Fresh extraction of the final ZIP reproduced both complete arithmetic runs. Both implementations were written by the same assistant: separate code is not external mathematical review or a formally verified kernel.

## Preserved actual package

Filename: N25_Delta14_AllActive_Candidate_2026-09-06_v1.zip
Bytes: 382174
SHA-256: aab329723a551eddf2fd7c2dd76c6b12653a135ad36850f2759ce3b332fcb98b
State-set SHA-256: 882a99e6e6df73fc23c6380ec19b4324fd59eb16bc384519cbe9aa9ea2f18462

The complete ZIP, proposed proof, status and verification record were uploaded to the user's Library at:
/N25_Checkpoints/Delta14/2026-09-06-all-active-v1/

The ZIP contains 23 manifested files plus the manifest: full proposed proof, both actual verifier sources, runner, tests, exact results and exclusion ledger, environment, and separately labelled exploration history. It is also available as a conversation download.

The attempted batch GitHub source upload was blocked because the tool could not determine the request's safety status. This receipt is NOT publication of the ZIP or of those source files. Actual source/proof publication to the repository remains outstanding unless separately recorded as successful.

## Next work

Audit the injections in the all-active lemma and new A-column residual lemma; audit the k=0,1 slack arguments; verify necessity and exhaustive coverage of all arithmetic bounds; then explicitly decide whether to promote the candidate and update the paper/ledger. Return to the parked Delta=15 proof-chain and global reductions before any full n=25 claim. Preserve this version unchanged when making corrections.
