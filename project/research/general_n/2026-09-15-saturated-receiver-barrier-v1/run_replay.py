#!/usr/bin/env python3
"""Replay frozen mathematical evidence without overwriting it."""
from pathlib import Path
import csv, json, shutil, subprocess, sys, tempfile
HERE=Path(__file__).resolve().parent

def main():
    expected=json.loads((HERE/'JOINT_CORE_RESULTS.json').read_text())
    with tempfile.TemporaryDirectory(prefix='ms742-saturated-receiver-') as tmp:
        tmp=Path(tmp)
        for name in ['scan_joint_cores.py','RESCUE_PROFILES.json','replay_barrier.cpp','REPLAY_INPUT.txt']:
            shutil.copy2(HERE/name,tmp/name)
        subprocess.run([sys.executable,str(tmp/'scan_joint_cores.py')],check=True,capture_output=True,text=True)
        actual=json.loads((tmp/'JOINT_CORE_RESULTS.json').read_text())
        assert actual==expected
        subprocess.run(['g++','-O2','-std=c++17',str(tmp/'replay_barrier.cpp'),'-o',str(tmp/'replay')],check=True,capture_output=True,text=True)
        output=subprocess.check_output([str(tmp/'replay'),str(tmp/'REPLAY_INPUT.txt')],text=True)
        assert output==(HERE/'INDEPENDENT_REPLAY.tsv').read_text()
        rows=list(csv.DictReader(output.splitlines(),delimiter='\t'))
        assert len(rows)==124 and all(r['old_pass']=='1' for r in rows)
        rejected=sorted(int(r['state_id']) for r in rows if r['barrier_pass']=='0')
        assert rejected==sorted(expected['labelled_joint_rejected']) and len(rejected)==24
    print(json.dumps({'status':'PASS','old_witnesses_passed':124,'new_fixed_witness_rejections':24,'python_cpp_exact_agreement':True,'whole_state_exclusions_claimed':0,'external_review':'OPEN'},sort_keys=True))
if __name__=='__main__':main()

