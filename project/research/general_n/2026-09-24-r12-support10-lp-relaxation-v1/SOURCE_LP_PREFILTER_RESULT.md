# r=12 support-ten: independent source-LP regeneration

Observed solver interval: 2026-09-24T01:19:17+01:00 to 2026-09-24T01:20:51+01:00.

Starting from the independently regenerated 6,386 strict support-ten kernels, I rebuilt the source-cover system independently and replaced source integrality by a continuous LP relaxation. Because every integer-feasible source population is LP-feasible, this is a safe superset prefilter.

Across the four survivor-bearing shards 0,1,4,5, the LP relaxation left **exactly 32** kernels, with shard counts **10, 11, 6, 5**. These match the audited saved source-survivor counts; the zero-survivor shards 2,3,6 were already freshly replayed as zero in the existing audit, and shard 7 is saved zero. The independently regenerated LP-survivor identities are:

```
355  [5179456,0,11,19]
359  [5179456,0,11,67]
362  [5179456,0,11,81]
363  [5179456,0,11,82]
434  [5179456,0,67,131]
437  [5179456,0,67,137]
438  [5179456,0,67,138]
451  [5179456,0,73,145]
452  [5179456,0,73,146]
455  [5179456,0,74,145]
1196 [5670976,0,19,35]
1202 [5670976,0,19,67]
1208 [5670976,0,19,97]
1209 [5670976,0,19,98]
1390 [5670976,0,67,131]
1393 [5670976,0,67,137]
1396 [5670976,0,67,145]
1397 [5670976,0,67,146]
1493 [5670976,0,97,145]
1494 [5670976,0,97,146]
1497 [5670976,0,98,145]
3753 [15400961,0,7,11]
3755 [15400961,0,7,35]
3758 [15400961,0,7,67]
3759 [15400961,0,7,73]
3790 [15400961,0,37,73]
3791 [15400961,0,37,74]
4663 [48373761,0,7,11]
4664 [48373761,0,7,19]
4665 [48373761,0,7,25]
4682 [48373761,0,21,41]
4683 [48373761,0,21,42]
```

The first coordinate is the regenerated strict-row index; the identity is `[unit_graph, heavy_edge, a_mask, b_mask]`.

This checkpoint does not use abstract profile feasibility as graph realizability and does not thaw `S<=14`. A fresh exact-integer source solve is being run only on these 32 LP survivors; if all 32 are integer-feasible, then the combination `LP prefilter + exact solve on its complete survivor set` independently reproduces the 32-row source stage while avoiding thousands of unnecessary branch-and-bound solves.
