# Reproduce this checkpoint

From this directory, using Python 3.10+ and its standard library:

```sh
python verify_source_prices.py > /tmp/source-prices-actual.json
python verify_joint_witnesses.py > /tmp/source-joint-actual.json
python - <<'PY'
import json
for actual, expected in [('/tmp/source-prices-actual.json','VERIFIED_RESULT.json'),('/tmp/source-joint-actual.json','JOINT_VERIFIED.json')]:
    with open(actual) as f: a=json.load(f)
    with open(expected) as f: e=json.load(f)
    assert a==e, (actual,expected)
print('Both complete result objects match exactly.')
PY
```

`BEST_PRICES.json` supplies rational prices with common integer scales. It is not trusted as proof: the verifier recomputes every bound. `JOINT_WITNESSES.json` supplies integer witnesses that are checked directly, without importing the numerical model.

The extracted `inputs.json` points to the canonical original `REMAINDER_12.json`, blob `70b6fb160c82179c52ef8d88be673a4a729016a4`. Row IDs are ORIGINAL, not fresh-seed IDs. Numerical exploration uses SciPy1.17.0 and NumPy, but neither is required for either exact replay. The readable initial script retains its original local-path assumptions as historical exploration. The current scripts use paths relative to their own directory.

To repeat optional discovery, run `python explore_prices.py INDEX` or `python explore_joint_incidence.py INDEX`, with INDEX0,...,5 selecting the input row. Discovery outputs may vary by numerical solver version. The latter's time limit is deliberately not treated as infeasibility; its infeasibility status likewise is not an accepted proof. Use a copied directory for new experiments to avoid replacing preserved raw outputs.

The portable bundle contains the full numerical traces and particular-witness diagnostics. Committed exact prices, witnesses, source, complete exact result objects and discovery index suffice to audit the claims without those auxiliary traces. Source and output integrity hashes are listed in MANIFEST.json.
