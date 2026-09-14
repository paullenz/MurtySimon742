# Reproduce the conditioned-excess checkpoint

From the repository root, with Python 3 and no third-party packages:

```sh
python3 project/research/general_n/2026-09-14-conditioned-excess-v1/verify_conditioned_excess.py \
  --prior project/research/general_n/2026-09-14-capped-spill-v1/verify_capped_spill.py \
  --block project/research/general_n/2026-09-14-block-pressure-v1/verify_block_pressure.py \
  --remainder project/research/general_n/2026-09-14-block-pressure-v1/REMAINDER_12.json \
  > CONDITIONED_EXCESS_FULL.json
```

Do not run Python with `-O`; assertions are audit checks. The complete output includes every tested low-block budget, failed price attempt, all three new exclusions and the nine not-excluded profile IDs. It is not merely the successful certificates.

Validate the ENTIRE output, not only its headline totals:

```python
import hashlib, json
from pathlib import Path
root = Path('project/research/general_n/2026-09-14-conditioned-excess-v1')
frozen = json.loads((root/'FROZEN_RESULT.json').read_text())
actual = json.loads(Path('CONDITIONED_EXCESS_FULL.json').read_text())
canonical = json.dumps(actual, sort_keys=True, separators=(',', ':')).encode()
assert hashlib.sha256(canonical).hexdigest() == frozen['full_output_canonical_sha256']
```

The expected canonical hash is `7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e`. The compact frozen file explicitly says where unsuccessful-branch details are omitted from its displayed summary; none are omitted from the hash-bound full replay. It includes every branch needed to exclude rows 295, 365 and 570.

The verifier source Git blob is `412356d3585e2fda845434868e52653a58852aee`, independently checked against the locally executed file. It reuses prior cap and receiver routines but implements the conditioned cap and exact-budget DP separately, with brute-force comparisons. Thus it is not a wholly independent implementation of every earlier bridge consequence.

No live GitHub artifact is required to replay this NEW checkpoint: its twelve input profiles are already committed. Reconstructing the entire older 713-row corpus and historical exploratory outputs has separate provenance in the evidence-preservation package. No all-order or whole-state claim follows from the sample.
