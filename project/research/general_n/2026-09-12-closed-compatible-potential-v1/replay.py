#!/usr/bin/env python3
"""Full-pool exact replay using only closed local maxima."""
from collections import Counter
from functools import cache
from pathlib import Path
import json,platform,time
from closed import maxima
HERE=Path(__file__).resolve().parent
COUNTS=Counter()

@cache
def local(a,b,h,k,j,rho,hi,lo):
    answer=maxima(a,b,h,k,j,rho,hi,lo)
    COUNTS['source_contexts']+=1
    COUNTS['piece_evaluations']+=sum(r['pieces'] for r in answer)
    COUNTS['candidate_evaluations']+=sum(r['candidates'] for r in answer)
    COUNTS['maximum_candidates_per_class']=max(COUNTS['maximum_candidates_per_class'],*(r['candidates'] for r in answer))
    return tuple(r['value'] for r in answer)

def capacity(rec,h):
    caps=[min(rec['a']-r,sum(h<=s<=r for s in rec['s'])) for r in rec['rho'] if r>=h]
    large=sorted((v for v in caps if v>h),reverse=True);low=sum(min(v,h) for v in caps);z=len(caps)
    return [low-j*h+min(sum(large[:j]),j*(z-j)+j*(j-1)//2) for j in range(len(large)+1)]

def gaps(rec,h,j,ks):
    a,b,s,rho=rec['a'],rec['b'],rec['s'],rec['rho'];sizes=Counter(rho)
    W=sum(v for v in s if v>=h);G=sum(max(4*h,v) for v in s if v>=h);target=h*(G-sum(rho))+W
    answer=[]
    for k in ks:
        low=0;differences=[]
        for rv,n in sizes.items():
            hi=sum(h<=v<=rv for v in s);lo=sum(v<h and v<=rv for v in s)
            values=local(a,b,h,k,j,rv,hi,lo);assert values[0] is not None
            low+=n*values[0]
            if values[1] is not None:differences.extend([values[1]-values[0]]*n)
        assert len(differences)>=j
        answer.append(target-low-sum(sorted(differences,reverse=True)[:j]))
    return answer

def main():
    assert json.loads((HERE/'local_verification.json').read_text())['status']=='PASS'
    pool=[json.loads(line) for line in (HERE/'pool_inputs.jsonl').read_text().splitlines()]
    assert len(pool)==5578
    counts=Counter();start=time.monotonic()
    with (HERE/'frontier_results.jsonl').open('w') as out:
        for index,rec in enumerate(pool):
            row=dict(layer=rec['layer'],state_id=rec['state_id'],modes={})
            for mode,ks in [('fixed_k2',[2]),('all_k',list(range(rec['a']+2)))]:
                thresholds=[];witness=None
                for h in range(2,max(rec['s'])+1):
                    caps=capacity(rec,h);W=sum(s for s in rec['s'] if s>=h);attempts=[];blocked=False
                    for j,c in enumerate(caps):
                        if c<W:continue
                        values=gaps(rec,h,j,ks);attempts.append(dict(j=j,gaps=values))
                        if max(values)<=0:blocked=True;break
                    thresholds.append(dict(h=h,capacities=caps,attempts=attempts))
                    if not blocked:witness=h;break
                row['modes'][mode]=dict(thresholds=thresholds,witness_h=witness);counts[mode]+=witness is not None
            out.write(json.dumps(row,separators=(',',':'))+'\n')
            if (index+1)%500==0 or index+1==len(pool):
                out.flush();print('PROGRESS',index+1,'excluded',dict(counts),'contexts',local.cache_info().currsize,flush=True)
    elapsed=time.monotonic()-start
    report=dict(python=platform.python_version(),platform=platform.platform(),original_closed_replay_seconds=elapsed,
        exclusions=dict(counts),**COUNTS,integer_arithmetic='Python unbounded integers',solver_used=False,external_review='OPEN')
    (HERE/'environment.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
