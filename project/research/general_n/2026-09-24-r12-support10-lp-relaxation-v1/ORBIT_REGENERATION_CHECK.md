# r=12 support-ten strict-kernel regeneration checkpoint

Timestamped research interval: 2026-09-24T01:14:30+01:00 to 2026-09-24T01:14:42+01:00.

The committed support-ten orbit generator was independently reconstructed in the local research runtime from the repository source, compiled with `g++ -O3 -std=c++20`, and executed from scratch. It produced exactly **6,386** strict mask rows. Its stderr summary was:

`unlabelled8=12346 maxdeg2_unit_cores=46 coloured=104981 strict=6386`

This exactly matches the repository's audited strict-kernel count for the `r=12`, support-ten partition `(2,2,1^8)`. It is a regeneration check of the finite kernel universe, not graph realizability and not a proof of `S<=14`.

Next action: regenerate the 32 source survivors from these 6,386 rows and test an independently encoded **continuous LP relaxation** of the helper system on every survivor. The first survivor's helper LP relaxation is already independently observed infeasible; `S<=14` remains frozen until the load-bearing 32-row claim is decisively reproduced or certified.
