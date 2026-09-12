#!/usr/bin/env python3
"""N34 m290 discovery; numerical proposals require repaired integer acceptance."""
import sys
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRONTIER = HERE.parent / '2026-09-12-frontier-v1'
sys.path.insert(0, str(FRONTIER))
from check_frontier import expand
from certify_upper_layers import e, integer_certificate


def hand_reason(s, rho):
    if min(s) > 0 and sum(s) != sum(rho) + 4:
        return dict(method='positive_degree_mass', S=sum(s), r=sum(rho))
    for h in range(2, min(s) + 1):
        z = sum(v >= h for v in rho)
        if z >= h and 2*sum(s) == z*(z-1)+h*(h+1) and 22 > h*(h+1):
            return dict(method='tight_total_threshold', h=h, z=z)
    return None


def main():
    states, stats = expand(2)
    result = dict(schema='n34-m290-baseline-v1', frontier=stats,
                  hand=[], certificates=[], unresolved=[])
    for idx, (s, rho) in enumerate(states):
        rec = dict(state_id=idx, s=s, rho=rho)
        reason = hand_reason(s, rho)
        if reason:
            result['hand'].append(dict(**rec, **reason))
        elif min(s) == 0:
            result['unresolved'].append(dict(**rec, reason='zero_demand_separate_model'))
        else:
            model = e.build_envelope(s, rho)
            cert = integer_certificate(model)
            if cert:
                result['certificates'].append(dict(**rec, **cert))
            else:
                result['unresolved'].append(dict(**rec, reason='no_exact_baseline_certificate', solver_status=int(model[-1].status)))
        if (idx+1) % 100 == 0 or idx+1 == len(states):
            print(idx+1, {k:len(result[k]) for k in ('hand','certificates','unresolved')}, flush=True)
            (HERE/'baseline.json').write_text(json.dumps(result, separators=(',', ':'))+'\n')


if __name__ == '__main__':
    main()
