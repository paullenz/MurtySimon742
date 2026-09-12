#!/usr/bin/env python3
"""Pin the N34-v2/N35-v1 publication after exact validation and final edits."""
from pathlib import Path
import hashlib
import json
import platform
import numpy
import scipy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
BASELINE='ef030cc4e3d1ecc1355c94b5b1fac6befe6ebb78'


def main():
    old=json.loads((ROOT/'releases/n34-reviewer-v1/MANIFEST.json').read_text())
    paths=set(old['artifacts'])
    for folder in ['project/reviews/n34/2026-09-12-heavy-independent-v1',
                   'project/research/n35/2026-09-12-candidate-v1',
                   'releases/n34-reviewer-v2','releases/n35-reviewer-v1']:
        paths.update(str(p.relative_to(ROOT)) for p in (ROOT/folder).rglob('*')
                     if p.is_file() and '__pycache__' not in p.parts
                     and p.name not in ('MANIFEST.json','PUBLICATION_RECEIPT.json'))
    for folder in ['2026-09-12-a14-high-b-v1','2026-09-11-fourteen-label-tail-v1',
                   '2026-09-09-profile-integral-7-12-v1']:
        base=ROOT/'project/research/general_n'/folder
        paths.update(str(p.relative_to(ROOT)) for p in base.rglob('*')
                     if p.is_file() and p.suffix in ('.md','.py') and '__pycache__' not in p.parts)
    artifacts={}
    for name in sorted(paths):
        data=(ROOT/name).read_bytes()
        artifacts[name]=dict(sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
    for package,n,bound,equality in [('n34-reviewer-v2',34,289,'K(17,17)'),('n35-reviewer-v1',35,306,'K(17,18)')]:
        scope=dict(n=n,candidate_upper_bound=bound,candidate_equality=equality+' only',
                   internal_certificate_status='PROJECT_CERTIFIED',external_review='OPEN',unrestricted_theorem=False)
        if n==34:
            scope.update(equality_states=13546,hand_accounting_exclusions=6709,integer_envelopes=6837,
                         envelope_local_integer_checks=3018781,proof_critical_heavy_farkas_certificates=0)
        else:
            scope.update(m307_states=19,m306_states=466,hand_accounting_exclusions=228,integer_envelopes=257,
                         local_integer_checks=92701,unresolved_states=0)
        report=dict(schema=package+'-manifest',date='2026-09-12',repository='paullenz/MurtySimon742',
            unchanged_dependency_baseline=BASELINE,scope=scope,
            environment=dict(python=platform.python_version(),numpy=numpy.__version__,scipy=scipy.__version__),
            artifacts=artifacts,notes=[
                'Both packages pin the common publication artifact set; each scope is stated separately.',
                'Unchanged transitive dependencies remain available at the pinned complete repository baseline.',
                'The two new manifests exclude themselves and publication receipts to avoid circular hashes.',
                'Historical manifests apply to their stated publication snapshots; current navigation hashes are pinned here.',
                'Exact proof replay uses Python standard library; NumPy/SciPy are optional discovery dependencies.',
                'Clean validation also rebuilt the complete C++ demand enumeration and matched original CSV bytes.'])
        (ROOT/'releases'/package/'MANIFEST.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PINNED',len(artifacts),'artifacts in each manifest')


if __name__=='__main__':main()
