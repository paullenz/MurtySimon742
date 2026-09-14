#!/usr/bin/env python3
"""Regenerate the fixed fresh seed without external artifact downloads."""
import argparse,hashlib,json,subprocess,tempfile
from pathlib import Path
SEED=74220260919
EXPECTED={'seed':SEED,'trials':100000,'domain':44451,'cap_pass':5539,'incidence_pass':1496,'pair_flow_pass':715,'zero_demand_profiles':53,'Hall_failures':484,'tail_detection_misses':0,'interval_detection_misses':0}
def gitblob(data):
 return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--generator',required=True,type=Path);ap.add_argument('--scanner',required=True,type=Path);ap.add_argument('--outdir',required=True,type=Path);args=ap.parse_args()
 source=args.generator.read_bytes();scanner=args.scanner.read_bytes()
 assert gitblob(source)=='72b1b0374cba1b865ad778c6ad123d9353c13de6'
 assert hashlib.sha256(scanner).hexdigest()=='7b07649c355028818ba2153dedf461eb001b92541a5d994a83967cf366757906'
 assert source.count(b'74220260914')==2
 text=source.replace(b'74220260914',str(SEED).encode())
 out=args.outdir.resolve();out.mkdir(parents=True,exist_ok=True)
 with tempfile.TemporaryDirectory(prefix='shared-slack-fresh-') as tmp:
  root=Path(tmp);inc=root/'project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1';inc.mkdir(parents=True)
  (inc/'scan_q_crossing_stats.cpp').write_bytes(scanner);(root/'fresh.cpp').write_bytes(text)
  subprocess.run(['g++','-O3','-std=c++17','-I',str(root),str(root/'fresh.cpp'),'-o',str(root/'generate')],check=True)
  with (out/'GENERATOR.json').open('w') as h:subprocess.run([str(root/'generate'),'100000'],cwd=out,stdout=h,check=True)
 assert json.loads((out/'GENERATOR.json').read_text())==EXPECTED
 assert hashlib.sha256((out/'SYNTHETIC_INTERVAL_PROFILES.tsv').read_bytes()).hexdigest()=='f0e32e99a66d51027d1ad89d9f3874a8d50b3d4d215e8e1dd0d816786504dc2e'
 print(json.dumps(EXPECTED,sort_keys=True,indent=2))
if __name__=='__main__':main()
