#!/usr/bin/env python3
"""Replace unwieldy rational discovery weights by checked small integers."""
from pathlib import Path
import json
import shared_pair_cover as s
from endpoint_control import frozen_patterns
HERE=Path(__file__).resolve().parent

def main():
    inputs={(r['layer'],r['state_id']):(r,S) for r,S,_ in frozen_patterns()}
    source=json.loads((HERE/'SHARED_PAIR.json').read_text());out=[]
    for item in source['records']:
        for mode in ('placement_control','shared_pair'):
            old=item.get(mode,{})
            if not old.get('exact_pattern_exclusion'):continue
            rec,S=inputs[item['layer'],item['state_id']];D,edges,opts=s.options(rec,S);cert=old['certificate']
            ww={(i,k):s.F(v) for i,k,v in cert['pair_weights']};aa={(u,i):s.F(v) for u,i,v in cert['endpoint_weights']};vv=list(map(s.F,cert['residual_prices']));mm=s.F(cert['incoming_multiplier'])
            for scale in (10,100,1000,10000,1000000):
                w=[round(ww.get(e,0)*scale) for e in edges];alpha={e:round(v*scale) for e,v in aa.items()};prices=[round(v*scale) for v in vv];mu=round(mm*scale)
                gap,lhs,rhs,local=s.exact_check(rec,S,D,edges,opts,w,alpha,prices,mu)
                if gap>0:break
            assert gap>0
            out.append({'layer':rec['layer'],'state_id':rec['state_id'],'mode':mode,'scale':scale,'exact_gap':str(gap),'exact_lhs':str(lhs),'exact_rhs':str(rhs),'certificate':{'pair_weights':[[*e,str(w[k])] for k,e in enumerate(edges) if w[k]],'endpoint_weights':[[u,i,str(v)] for (u,i),v in alpha.items() if v],'residual_prices':list(map(str,prices)),'incoming_multiplier':str(mu),'local_maxima':list(map(str,local))}})
    (HERE/'COMPACT_CERTIFICATES.json').write_text(json.dumps({'schema':'shared-budget-integer-certificate-compression-v1','scope':'Integer-weight compression of the same 38 fixed-pattern certificates; zero additional exclusions.','records':out},separators=(',',':'))+'\n')
    print({'compressed':len(out),'max_scale':max(x['scale'] for x in out)})
if __name__=='__main__':main()
