#!/usr/bin/env python3
"""Verify the portable package, regenerate regressions, replay endpoint audit."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import tempfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
ASSEMBLY=ROOT/'project/research/n30/2026-09-11-assembled-hand-route-v1'
RELEASE=ROOT/'releases/n30-reviewer-v3'


def main():
    records=json.loads((RELEASE/'BUNDLE_CONTENTS.json').read_text())['files']
    for row in records:
        data=(ROOT/row['path']).read_bytes()
        assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256'],row['path']
    with tempfile.TemporaryDirectory(prefix='n30-reviewer-v3-') as tmp:
        temp=Path(tmp)
        binary=temp/'profile-regression'
        subprocess.run(['g++','-O2','-std=c++17',str(ASSEMBLY/'profile_regression.cpp'),'-o',str(binary)],check=True)
        regenerated=temp/'PROFILE_REGRESSION.json'
        subprocess.run([str(binary),str(regenerated)],check=True,stdout=subprocess.DEVNULL)
        assert regenerated.read_bytes()==(ASSEMBLY/'PROFILE_REGRESSION.json').read_bytes(),'Profile regression differs'
        output=temp/'ASSEMBLY_AUDIT.json'
        envelopes=temp/'INDEPENDENT_ENVELOPES.json'
        subprocess.run(['python3','-I','-B',str(ASSEMBLY/'audit_assembly.py'),'--output',str(output),'--envelopes-output',str(envelopes)],check=True,stdout=subprocess.DEVNULL)
        expected=json.loads((ASSEMBLY/'ASSEMBLY_AUDIT.json').read_text())
        actual=json.loads(output.read_text())
        assert actual==expected,'Assembly audit differs'
        assert json.loads(envelopes.read_text())==json.loads((ASSEMBLY/'INDEPENDENT_ENVELOPES.json').read_text()),'Envelope output differs'
        subprocess.run(['python3','-I','-B',str(ASSEMBLY/'check_publication.py'),'--tables-only'],check=True,stdout=subprocess.DEVNULL)
    print(json.dumps({'status':'PASS','bundled_files_verified':len(records),
        'profile_regression_exact_bytes_match':True,'assembly_audit_matches':True,
        'all_envelope_outputs_match':True,'written_transfer_tables_pass':True,
        'external_validation':False},indent=2))


if __name__=='__main__':
    main()
