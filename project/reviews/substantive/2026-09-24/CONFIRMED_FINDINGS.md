# Confirmed substantive findings — first checkpoint

Baseline main 2ff383498ee08f607aa958181f6dbc4e36d136a1; source export at 90b5fd21a90f88aec1ba6445a5ab385559eea999, Actions run 36011981168, artifact 10812503619. PR #2 head bdd46c59365757d373bd359867d9fe47cde0d70f. This is manual internal review, not external acceptance or scheduled research.

## PR #2 is not acceptable as submitted

All four changed files were inspected. `universal_core_checked.py` is byte-identical to main's preserved `universal_core_impl.py`, Git blob 8b9124fc5bc384c4388a0f2d92c1f9be80425ff2. The proposed implementation does not contain the count/hash or pending-file hardening claimed in the PR body. Its parser test raises ImportError because `work_mode` is absent from main's parser; the old inline regular expression also accepts the prefix of invalid modes such as MATH2.

Fresh generation and C++ replay of the unchanged universal-core implementation PASS all 11,357 records, reproducing the committed input hash ab9ed63d9caa99b5fbd237fc6b238f77b69a8dc893ff17a764f96ff5cc9ab4bb and decision hash c4859538b56444860b26fdc46e40f68bf21b4c65b68dce2e394b531c621ba82a.

However, two executed hostile controls expose a real false-success hazard: replacing BOTH input and expected-decision streams with empty files, or with matching one-record prefixes, still exits zero and reports PASS_LOCAL_AND_INCIDENCE_CHECKS with replay_agreement_records=11357. Actual C++ output contains zero or one records. A matching pair of incomplete streams is not adequate integrity evidence. This does not show that the freshly regenerated complete replay is wrong.

## Solver-result handling can silently invalidate a closure

The active exact-star model labels a returned objective `minimum_deficit` without requiring optimal status. A controlled status-1 result with incumbent 17 and lower bound 16 is exported as minimum_deficit=17. The row driver then treats values over Dmax=16 as exclusions. Results with no incumbent are skipped without an unresolved-case count. These are demonstrated code hazards, not a claim that a particular historical timeout actually caused a false exclusion. Active and closely related legacy entry points need fail-closed handling; old full-row closure claims cannot be freshly certified from an uninstrumented FINAL summary alone.

## Historical gaps and exact index identities

Complete available path histories show that the R9 orbit-audit script's original committed bytes were only a timestamp, and the R11 support-six result originally contained only five progress lines. No complete older versions of those exact paths were found. Fresh reconstruction is therefore distinct from historical recovery.

Fresh scalar enumeration reproduces exactly 54,820 n18/Delta10 candidates. The (5,5,5)/(5,5,5) tuple is index 14,444, not 20,851. Index 20,851 is d=(5,4,2,1,1,1,1), x=(6,5,3,5,2,1,1), h=(7,6,4,9,3,1,1), agreeing with the preserved JSON. Index 50,740 is d=x=h=(8,8). Index 2 is d=(8,7), x=(8,8), and is another known abstract v4 survivor requiring its separate singleton-source exclusion. The old statement that v4 has only survivors 20,851 and 50,740 is not reliable.

## Positive mathematical replays

A fresh R9 C++ orbit enumeration reproduces 1,044 unit orbits, 79,264 rooted/coloured orbits and all 69 saved strict masks exactly. A separately written Burnside/group-action audit reproduces both orbit counts and verifies all 69 masks are pairwise inequivalent and satisfy the stated necessary inequalities.

Fresh R11 support-six enumeration completes all seven partitions: strict-orbit counts 18,72,15,39,13,27,5, total 189. Only the sixth partition has source-feasible cores (four), agreeing with the later prose; the original five-row artifact is not retroactively made complete.

A separate edge-first weighted-cover search reproduces star minima 4,8,14 on every labelled graph of orders 3,4,5, and minima 21,30 on all 156/1,044 Graph Atlas representatives of orders 6/7. Exact integer budget checks reproduce the n19 deficit contradictions 31,29,28 against allowance 27. Enumeration of all 3,072 relevant index2 core/outer skeletons (using symmetry for the omitted outer endpoint) has no uncovered case and leaves exactly the two symmetric hard patterns treated in the proof.

The 50,740 proof's initial prose uses a maximum as though it were a lower bound. Its deficit rigidity conclusion nevertheless follows from BOTH star inequalities: writing centre deficits p,q and noncentre deficit R, p+q+R<=16, 8p+R>=59, 8q+R>=59, 0<=p,q<=8 forces (p,q,R)=(8,8,0). A corrected argument and regression test are being preserved; no failed inference will be silently left in the proof.

Supported repairs, complete executable outputs and final review verdict will follow within this user-requested review. No old time or session credit is reconstructed.
