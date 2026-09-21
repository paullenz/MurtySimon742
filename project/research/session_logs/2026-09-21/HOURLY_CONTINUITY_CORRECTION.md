# Hourly continuity correction — 21 September 2026

Status: operational correction; historical timestamps and mathematical claims unchanged.

A scheduled trigger identifies one hourly accounting slot. Continuation, compaction and re-entry are segments of that slot, not independent hours. Preserve the earliest evidenced start, shared deadline, ledger and 50-minute target. If segment identity is uncertain, mark it UNVERIFIED. Do not infer historical timestamps or execution causes.

Continue useful bounded research until the preservation cutoff. The old eight-minute check was a guard, never permission to stop below eight minutes. After the cutoff, preserve briefly without overlapping the next invocation. A late zero-work segment does not establish that the whole hour had zero work; it also does not exempt that slot from the target.

Count the union of documented research intervals. Do not double-count overlapping segments or count undocumented gaps. Keep all scheduled slots in delivery accounting; missing duration remains UNVERIFIED. Distinguish delivery failures, early stopping, continuation and unknown cause. Preserve original records and append corrections.

## Concrete regression: 09:00:38 BST slot

The three existing logs were read directly:

- `2026-09-21T09-00-41+01-00.md`: start 09:00:41, eight timestamped units, but stop/preservation/final times remain PENDING. Its completed research duration is UNVERIFIED.
- `2026-09-21T09-28-15+01-00-a.md`: documented research interval 09:28:15–09:47:52, exactly 1177 seconds (19m37s). The stated permission to stop with 7m46s before cutoff was erroneous. Target exemption for this re-entry is superseded at slot level.
- `2026-09-21T09-57-59+01-00-a.md`: zero research in the late segment; this is not zero research in the full hour.

The completed documented research-interval union is 19m37s; additional earlier research is evidenced by the ledger but its closed duration is missing. Full-slot research duration and 50-minute compliance are UNVERIFIED; the premature stop explanation is NONCOMPLIANT. No missing duration has been reconstructed. The run did start near 09:00, so the 09:57 segment alone is not evidence of an hour-late scheduler start.

## Current run

The 14:00:38 slot began at measured 14:01:25 BST. One JSON ledger retains the slot identity through continuations. Mathematical direction follows the latest audit's graph-realizability priority using raw Q3 criticality. No historical log was edited.
