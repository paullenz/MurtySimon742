#!/usr/bin/env python3
"""Final exact pair-count cuts using the fixed labelled residual column.

For S_j={i:d_i>=j}, selected demand is at least sum(max(0,d_i-R_i)).
Every selected edge with such a label has a distinct unordered B-pair with
rho_b+rho_w>=j. Hence this demand cannot exceed the number of those pairs.
This refines the earlier pair threshold by using the actual column R.
"""
import argparse
from collections import Counter
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path

@lru_cache(None)
def pair_counts(rho, maximum):
    return tuple(sum(rho[b]+rho[w]>=j for b in range(len(rho)) for w in range(b))
                 for j in range(maximum+1))

def run(source, prefix):
    certificates=[]; survivors=[]; counts=Counter(); total=0
    with gzip.open(source,'rt') as stream:
        for line in stream:
            row=json.loads(line); state,k,r,d,rho,R,c=row
            pairs=pair_counts(tuple(rho),max(d)); witness=None
            for j in range(1,max(d)+1):
                indices=[i for i,di in enumerate(d) if di>=j]
                required=sum(max(0,d[i]-R[i]) for i in indices)
                if required>pairs[j]:
                    witness={'threshold':j,'subset':indices,'required':required,'available_pairs':pairs[j]}
                    break
            total+=1
            if witness:
                certificates.append({'row':row,'witness':witness});counts[j]+=1
            else:survivors.append(row)
    data={'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'checked':total,
          'eliminated':len(certificates),'surviving_columns':len(survivors),
          'threshold_counts':dict(sorted(counts.items())),
          'status':'ALL_REJECTED' if not survivors else 'SURVIVORS_RETAINED',
          'external_review':False}
    with gzip.open(str(prefix)+'_pair_certificates.json.gz','wt') as f:json.dump(certificates,f,separators=(',',':'))
    with gzip.open(str(prefix)+'_pair_survivors.jsonl.gz','wt') as f:
        for row in survivors:f.write(json.dumps(row,separators=(',',':'))+'\n')
    Path(str(prefix)+'_pair_summary.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('prefix',type=Path)
    a=p.parse_args();run(a.input,a.prefix)
