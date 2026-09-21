#!/usr/bin/env python3
"""Independent bitset replay of the two physical nonparity-plane proofs."""
from itertools import permutations
from pathlib import Path
import json
from check_star_support import CODES,Q
ALL=set(range(8))
def singleton(h,s):return [k for k,K in CODES.items() if CODES[h]&K=={s}]
def reverse(s):return [k for k,K in CODES.items() if not(K&({s}|Q[s]))]
def image(S,p,t):return frozenset(t^sum(((c>>j)&1)<<p[j] for j in range(3)) for c in S)
def orbit(rep):return {image(rep,p,t) for p in permutations(range(3)) for t in range(8)}

def main():
 # Opposite-edge representative: missing C01 matches S0--S6.
 opp={'C00','C10','C11','C20','C21','P0','P1','S0','S1','S6','S7'}
 assert singleton('C10',1)==['S3'] and reverse(1)==['S6']
 assert singleton('C10',0)==['S2'] and reverse(0)==['S7']
 assert 'S3' not in opp and 'S2' not in opp
 assert 1 in CODES['C10'] # forbids C10--S6 by S6 physical matching uniqueness
 assert 3 in CODES['S7']  # second spoke reverse killed by first spoke restriction
 avoid23=sorted(k for k in opp if 2 not in CODES[k] and 3 not in CODES[k])
 assert avoid23==['C10','C21']
 assert {2,3}<=CODES['C11']

 # Coordinate-face representative: missing C20 matches S0--S3 and S1--S2.
 face={'C00','C01','C10','C11','C21','P0','P1','S0','S1','S2','S3'}
 assert singleton('C10',4)==['S6'] and reverse(4)==['S3']
 assert singleton('C10',5)==['S7'] and reverse(5)==['S2']
 assert 'S6' not in face and 'S7' not in face
 assert 4 in CODES['C10'] and 5 in CODES['C10']
 avoid67=sorted(k for k in face if 6 not in CODES[k] and 7 not in CODES[k])
 assert avoid67==['C10','S0','S1']
 assert 7 in CODES['C11'] and 6 in CODES['C11']
 # Hence S0/S1 cannot meet C11 without duplicating their matched antipode bridge.

 oo=orbit({0,1,6,7});fo=orbit({0,1,2,3});po=orbit({0,3,5,6})
 assert (len(oo),len(fo),len(po))==(6,6,2)
 assert not(oo&fo or oo&po or fo&po)
 affine={frozenset(s) for s in __import__('itertools').combinations(range(8),4) if __import__('functools').reduce(int.__xor__,s)==0}
 assert oo|fo|po==affine
 out={'opposite_edge':{'available_codes':sorted(opp),'C10_neighbor_codes_after_spokes_1_0':avoid23},'coordinate_face':{'available_codes':sorted(face),'C10_neighbor_codes_after_spokes_4_5':avoid67},'orbit_counts':{'opposite_edge':6,'coordinate_face':6,'parity_plane':2},'result':'all primitive singleton/reverse tables, antipode-membership exclusions and 14-plane orbit coverage pass'}
 Path(__file__).with_name('FOUR_CENTRE_ORBIT_EXCLUSION_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
 print('PASS:',out['result'])
if __name__=='__main__':main()
