# Residual-one k=2 ledger-scope correction

Date: 2026-09-20

Status: **same-session audit correction**. This note supersedes one overly compressed comparison in `ONE_CODE_R1_K2_PURE_F0_Y_EDGE_CERTIFICATE_OBSTRUCTION.md`; it does not weaken the raw certificate obstruction itself.

## Correction

The F0--Y certificate theorem proves, at the pure-F0 endpoint,

`(Z_X+Z_Y)/p^2 >= q^2-o(1)`

and on the exact q=1 ray this adds a coefficient-one located X/Y-hole block to the coefficient-one-half independent-U block in the unweighted physical functional

`D_phys=E_U+Z_X+Z_Y+M_U`.

It is therefore correct that the pure endpoint has an unweighted physical-defect lower contribution of order `3p^2/2` before further terms.

It is **not** correct to compare that `3/2` coefficient directly with the score ceiling

`E_U+L_A<=C0`,

because `Z_X,Z_Y,M_U` do not all live in that score inequality.

The correct preserved combined rooted/score ledger on the exact low-k ray is

`E_U+Z_X+Z_Y+2M_U+2L_A <= p(p+1)+2C0`,

whose right-hand side has leading coefficient **4**, not `3/2`.

Hence the phrase in the predecessor F0--Y note saying the physical defect was driven to the 'leading-order ceiling scale 3/2 p^2' is superseded. The valid conclusion is narrower and still strong:

> the coefficient-1/2 pure-F0 equality endpoint is impossible in every high-Y regime because it requires `Z_X+Z_Y=o(p^2)`, whereas raw F0--Y edge criticality forces `Z_X+Z_Y>=q^2p^2-o(p^2)`.

For the exact q=1 ray, the subsequent witness-split theorem now performs the comparison in the correct weighted ledger. It gives a golden endpoint with typical density `rho=(sqrt(5)-1)/2`; all exceptional witnesses are dual-role, the dual class has linear U-slack, and the certificate subsystem contributes weighted leading coefficient **2** against the legitimate coefficient-4 combined ceiling. That is a tightening, not a closure.

## Evidence status

No graph-theoretic premise is retracted by this correction. The forward/reverse witness exclusions, certificate-capacity inequality, golden-ratio population bound, and high-Y pure-endpoint elimination remain as stated. Only the cross-ledger comparison is corrected.

The global rigid-interface reachability caveat remains binding.