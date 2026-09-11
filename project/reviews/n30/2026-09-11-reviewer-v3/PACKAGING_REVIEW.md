# Small-archive publication and checkout consistency

The initial reviewer-v3 publication and both of its CI checks passed at `fb9ed4167da09727ee01a5b5ba805137fb8820d3`. Exact Git object readback matched both PDFs and the ZIP. During final local alignment, the repository's blanket `*.zip filter=lfs` rule made the small ordinary-Git reviewer ZIP appear modified even though its local and remote SHA-256 hashes were identical.

Commit `762fafebafa3e1e68d803b517e20b44566548a54` adds one path-specific ordinary-Git exception for this reviewer ZIP. All historical archive settings remain unchanged. The exception is checked against the exact original `.gitattributes` plus the three appended lines; the small ZIP includes this configuration for provenance. The reviewed PDFs and all mathematical evidence remain unchanged.

The associated package CI run `34654753599` then exposed a separate portability defect in the publication-scope check: `git diff BASE` examined the filtered working tree, so Git LFS reported seven unchanged historical raw ZIP files as modified. The check failed before the portable mathematical replay ran. This was a checkout/filter mismatch, not an arithmetic failure or a change to any historical archive's committed bytes.

The corrected scope check compares the actual committed trees with `git diff BASE HEAD`. Exact source and release hashes continue to validate working-file bytes separately, and publication verifies every changed blob plus the preservation of all other blobs. This checks the intended repository invariant without mistaking LFS clean-filter output for a historical source edit. The final publication receipt records the corrected CI run and updated ZIP hash.
