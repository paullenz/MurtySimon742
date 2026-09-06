# Reviewer-wrapper validation

6 September 2026, Python 3.12.13, same assistant environment as the earlier runs.

The new wrapper checked every manifest and all 1,959 equality certificates. Its partial replay reproduced the original Delta14/e157 primary and second outputs byte for byte, passed the original 12 tests, and exactly reproduced both Delta15 scopes (108 and 211 outer states). Logs and the machine-readable report are in `validation/`.

The large Delta14/e156 scopes were not rerun merely for this packaging change; their earlier full primary/second replay records remain in the unchanged frozen evidence ZIP. This wrapper-validation run is explicitly PARTIAL. No external machine or independent researcher participated. Mathematical and independent computational review remain OPEN.

All nine manuscript pages were rendered and visually inspected. XeLaTeX reported no missing glyphs or overfull boxes in the final build. The TeX, Markdown and builder are supplied; `FROZEN_PROOF.md` preserves the exact input for rebuilding.
