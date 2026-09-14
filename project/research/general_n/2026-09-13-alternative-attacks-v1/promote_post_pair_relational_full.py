#!/usr/bin/env python3
"""Thin entry point for the hash-gated full relational ledger promotion."""
from pathlib import Path
import importlib.util

HERE = Path(__file__).resolve().parent
IMPL = HERE / "_promote_post_pair_relational_full_impl.py"
spec = importlib.util.spec_from_file_location("relational_full_promotion_impl", IMPL)
if spec is None or spec.loader is None:
    raise SystemExit(f"cannot load {IMPL}")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# The implementation lives four directory components below the repository root;
# Path.parents is zero-indexed, so parents[3] is the checkout root.
mod.ROOT = HERE.parents[3]
mod.EVIDENCE = mod.ROOT / "RESEARCH_EVIDENCE_INDEX.md"
mod.README = mod.ROOT / "README.md"
mod.CURRENT = mod.ROOT / "CURRENT_STATE.md"
mod.main()
