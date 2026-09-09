# Canonical reviewer-paper build

This directory builds the reviewer-facing paper layer requested on 9 September 2026.

## Scope

Every **current theorem-level candidate claim** in the top-level project status is required to have a standalone reviewer manuscript. Existing n=25 and n=28 reviewer packages are retained. This builder creates the missing packages for n=27, n=29, n=30, the general 293/500 maximum-degree candidate, and the retained 13/22 layer-sum candidate.

Historical failed, superseded or intermediate research checkpoints remain preserved in their original locations and are not silently promoted into theorem papers. The ongoing RX-Hall / residual-budget / R+Z programme remains research in progress until a theorem-level statement is frozen.

## Editorial rule

The canonical proof sources are not modified by this build. The manuscript copies the complete canonical proof verbatim after transparent reviewer front matter. The verification companion concatenates the principal replay/audit/bridge documents. Internal exact arithmetic is described as exact arithmetic; same-assistant reconstructions are not called external independent review.

## Output

Each new release contains:

- reviewer manuscript Markdown;
- reviewer manuscript PDF;
- verification companion Markdown;
- verification companion PDF;
- reviewer README;
- SHA-256 manifest.

`releases/REVIEW_READY_INDEX.md` is the governing reviewer-facing index after a successful build.
