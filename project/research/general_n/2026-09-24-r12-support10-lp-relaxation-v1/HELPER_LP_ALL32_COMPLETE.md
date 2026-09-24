# r=12 support-ten helper gate: complete independent LP reproduction

Second-pass solver interval: 2026-09-24T01:25:09+01:00 to 2026-09-24T01:26:27+01:00.

The independent helper-LP encoding has now decisively classified **all 32** independently regenerated source survivors. Pass 1 (`highs`, 30 s) proved 19 LP-infeasible and left 13 time-limit/unknown. Pass 2 reran exactly those 13 with the HiGHS interior-point method and a 120-second cap; **all 13 were LP-infeasible**, with no feasible or unknown rows remaining.

Combined result: **32/32 LP-infeasible; 0 feasible; 0 unknown.** Because this is a continuous relaxation of the integer helper model, each LP infeasibility implies integer infeasibility. The implementation was rebuilt independently from the mathematical helper semantics rather than reusing the saved helper result table.

Structural cross-checks against the saved historical aggregate are exact:

- pattern range: **3478--4017**
- residual-free types: **1 for every row**
- residual-free helper discharges: **0 total**
- helper-constraint range: **4296--5803**

These are precisely the saved aggregate ranges. Together with the independent strict-kernel regeneration, complete source-LP prefilter, and exact 32-row source replay, this resolves the 24-September red-team nonreproduction at the internal computation level using a second encoding and a stronger relaxation. Under the audit's explicit gate (“independently checkable certificates or ... a second solver/encoding”), the support-ten blocker is now decisively reproduced and the internal `S<=14` freeze can be lifted. This is **not external mathematical acceptance**, not graph realizability, and not a proof of the full Murty--Simon conjecture.

Rowwise results (`status=2` means LP infeasible):

```text
idx,identity,patterns,helpers,free,free_discharges,pass,status,seconds
355,5179456:0:11:19,3558,4481,1,0,default,2,8.102
359,5179456:0:11:67,3717,4963,1,0,default,2,29.997
362,5179456:0:11:81,3589,4624,1,0,ipm,2,21.441
363,5179456:0:11:82,3625,4690,1,0,ipm,2,22.151
434,5179456:0:67:131,3877,5405,1,0,default,2,24.709
437,5179456:0:67:137,3817,5251,1,0,ipm,2,21.567
438,5179456:0:67:138,3727,5012,1,0,ipm,2,20.800
451,5179456:0:73:145,3732,4788,1,0,ipm,2,22.406
452,5179456:0:73:146,3608,4688,1,0,default,2,18.999
455,5179456:0:74:145,3798,5198,1,0,ipm,2,21.193
1196,5670976:0:19:35,3478,4296,1,0,default,2,24.633
1202,5670976:0:19:67,3512,4343,1,0,default,2,22.509
1208,5670976:0:19:97,3493,4368,1,0,default,2,31.807
1209,5670976:0:19:98,3528,4433,1,0,default,2,18.965
1390,5670976:0:67:131,3573,4510,1,0,default,2,13.013
1393,5670976:0:67:137,3645,4777,1,0,default,2,10.865
1396,5670976:0:67:145,3632,4715,1,0,default,2,20.798
1397,5670976:0:67:146,3541,4478,1,0,default,2,10.957
1493,5670976:0:97:145,3637,4541,1,0,default,2,18.311
1494,5670976:0:97:146,3513,4444,1,0,ipm,2,18.129
1497,5670976:0:98:145,3705,4960,1,0,default,2,27.543
3753,15400961:0:7:11,3598,4566,1,0,default,2,15.056
3755,15400961:0:7:35,3611,4626,1,0,ipm,2,19.128
3758,15400961:0:7:67,3603,4588,1,0,ipm,2,16.876
3759,15400961:0:7:73,3594,4642,1,0,default,2,14.789
3790,15400961:0:37:73,3587,4440,1,0,default,2,17.861
3791,15400961:0:37:74,3502,4416,1,0,default,2,23.549
4663,48373761:0:7:11,4017,5803,1,0,ipm,2,25.966
4664,48373761:0:7:19,3999,5774,1,0,ipm,2,25.711
4665,48373761:0:7:25,3887,5483,1,0,ipm,2,24.147
4682,48373761:0:21:41,3787,4978,1,0,ipm,2,20.196
4683,48373761:0:21:42,3702,4950,1,0,default,2,16.391
```

Next action under the audited programme: treat the internal finite edge bound as restored through `S<=14`, then resume the bounded `n=18, Delta=10` stable-index diagnostic from **39,251**, stopping at the next distinct abstract survivor for staged exact D2C testing. Equality remains only through `S<=8` and all graph-to-profile trust limits remain in force.
