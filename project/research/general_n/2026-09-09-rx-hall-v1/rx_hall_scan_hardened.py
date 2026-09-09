#!/usr/bin/env python3
"""Hardened runner for the RX-Hall reconnaissance scanner.

The original scanner deliberately treats every nonstandard HiGHS status as
unresolved.  GitHub Actions run 34295699108 exposed six status-4 cases where
SciPy/HiGHS reported model_status=Unknown with primal_status=Infeasible.

This runner preserves that conservative first pass.  Only when the original
`method='highs'` call returns status 4 does it rebuild exactly the same LP and
retry it with the distinct HiGHS interior-point route (`method='highs-ipm'`).
The final classification still comes from SciPy's public status code.  No
status-4 result is silently reclassified without the second solve.

This remains floating-point reconnaissance, not proof evidence.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import numpy as np


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "rx_hall_scan.py"
spec = spec_from_file_location("rx_hall_scan_original", SOURCE)
if spec is None or spec.loader is None:
    raise SystemExit(f"cannot load {SOURCE}")
rx = module_from_spec(spec)
spec.loader.exec_module(rx)

_original_solve = rx.LP.solve


def _ipm_retry(self, first):
    n = len(self.names)
    U = self._mat(self.ub, n) if self.ub else None
    E = self._mat(self.eq, n)
    retry = rx.linprog(
        np.zeros(n),
        A_ub=U,
        b_ub=np.array(self.bu, float) if self.ub else None,
        A_eq=E,
        b_eq=np.array(self.be, float),
        bounds=(0, None),
        method="highs-ipm",
    )
    retry["rx_primary_status"] = int(first.status)
    retry["rx_primary_message"] = str(first.message)
    retry["rx_solver_method"] = "highs-ipm-retry"
    return retry


def hardened_solve(self):
    first = _original_solve(self)
    if first.status == 4:
        return _ipm_retry(self, first)
    first["rx_primary_status"] = int(first.status)
    first["rx_primary_message"] = str(first.message)
    first["rx_solver_method"] = "highs"
    return first


rx.LP.solve = hardened_solve
rx.main()
