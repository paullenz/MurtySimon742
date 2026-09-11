#!/usr/bin/env python3
"""Reconstruct the earlier interactive structural probes; not proof premises."""
import json
from pathlib import Path
import runpy
from collections import Counter
import sys

HERE=Path(__file__).resolve().parent
m=runpy.run_path(str(HERE/'verify_hand_classification.py'),run_name='probe_definitions')
g=m['threshold'];d=m['deficit4'];q5=m['score5'];q6=m['score6']
profiles=[]
for line in (HERE/'HAND_CLASSIFIED_PROFILES.txt').read_text().splitlines():
    if line and not line.startswith('#'):
        profiles.append(tuple(map(int,line.split('|')[0].split())))
out={
    'status':'RECONSTRUCTED EXPLORATION; NOT A PROOF PREMISE',
    'provenance':'Recreated from the interactive integer probes in this continuation; the new profile list is equivalent to the historical list used in the first histogram.',
    'profile_counts_by_p_N2_max':{str(k):v for k,v in Counter((sum(v>0 for v in s),sum(v>=2 for v in s),max(s)) for s in profiles).items()},
    'cap4_max_D_by_N2':{str(x):max(d(x,y,z) for y in range(x+1) for z in range(y+1)) for x in range(14)},
    'cap5_max_Q_by_N4_at_p_N2_13':{str(z):max(q5(13,13,y,z,k) for y in range(z,14) for k in range(1,z+1)) for z in range(1,14)},
    'cap5_max_Q_at_p13_N2_12':max(q5(13,12,y,z,k) for y in range(13) for z in range(1,y+1) for k in range(1,z+1)),
    'unused_larger_six_lift_box_max_Q_by_j':{str(j):max(q6(y,z,k,j) for y in (12,13) for z in range(10,y+1) for k in range(max(3,j),z+1)) for j in range(1,14)},
}
text=json.dumps(out,indent=2)+'\n'
if len(sys.argv)>1:
    Path(sys.argv[1]).write_text(text)
print(text)
