#!/usr/bin/env python3
"""N=29, Delta=16 direct finite adaptation of the n=28 direct197 machinery.
The inherited source is extracted from its hash-pinned archive; this file changes
only the scope parameters and provides fresh exact checks. Candidate arithmetic,
not a formal proof of the graph lemmas.
"""
from pathlib import Path
import argparse,sys,json,itertools,collections,time

def paths(base):
 sys.path[:0]=[str(base/'exploration'),str(base/'src'),str(base/'dependencies')]

def prepare(base,t,out):
 paths(base);import v3_discover as D,v3_check as C
 b=16;records=[];kept=[];cnt=collections.Counter();start=time.monotonic()
 for s in D.demands(12,b,t):
  lo,hi=D.bounds(s,b,t);rec={'s':s,'rmin':lo,'rmax':hi}
  cert={'kind':'bounds'} if lo>hi else (D.support_certificate(s,b,hi) or D.dual_certificate(s,b,hi))
  if cert is None:cert={'kind':'OPEN'};kept.append(rec.copy())
  else:C.verify_record(dict(rec,certificate=cert),12,b,t)
  rec['certificate']=cert;records.append(rec);cnt[cert['kind']]+=1
 assert len(records)==C.domain_count(12,b,t)
 out.mkdir(parents=True,exist_ok=True)
 (out/'demands.json').write_text(json.dumps(kept,separators=(',',':'))+'\n')
 (out/'demands.txt').write_text(str(len(kept))+'\n'+''.join(' '.join(map(str,r['s']+[r['rmin'],r['rmax']]))+'\n' for r in kept))
 rep={'scope':{'n':29,'Delta':16,'m':208+t,'a':12,'b':16,'t':t},'demand_domain':len(records),'counts':dict(cnt),'retained_demands':len(kept),'max_r':max(r['rmax'] for r in kept),'domain_count_independently_recomputed':True,'all_saved_demand_cuts_exactly_rechecked':True,'seconds':time.monotonic()-start}
 (out/'PREPARE_REPORT.json').write_text(json.dumps(rep,indent=2)+'\n');print(json.dumps(rep))

def projected(t,root):
 demands=json.loads((root/'demands.json').read_text());cnt=collections.Counter();kept=[]
 def reject(s,rho,r):
  slack=sum(s)-r-2*t
  if slack and not any(x==0 for x in s):return 'zero_slack'
  D=2*r+2*t
  for j in range(2,11):
   pairs=sum(u+v>=j for u,v in itertools.combinations(rho,2));forced=[v for v in s if v>=j];optional=sorted(v for v in s if v<j);bounds=[]
   for h in range(len(forced),13):
    if 10*h+(12-h)*(j-1)<D or j*h>D:continue
    q=sum(forced)+sum(optional[:h-len(forced)]);high=max(h*j,D-(12-h)*(j-1));q=max(q,high-sum(min(x,h) for x in rho));bounds.append(q)
   if not bounds or min(bounds)>pairs:return 'projected_pair'
 for line in (root/'row_survivors.txt').read_text().splitlines():
  row=list(map(int,line.split()));kind=reject(demands[row[0]]['s'],row[2:],row[1]);cnt['rows']+=1
  if kind is None:cnt['survivors']+=1;kept.append(row)
  else:cnt[kind]+=1
 (root/'projected_survivors.json').write_text(json.dumps(kept,separators=(',',':'))+'\n');(root/'PROJECTED_REPORT.json').write_text(json.dumps(dict(cnt),indent=2)+'\n');print(dict(cnt))

def final_shard(base,t,root,shard,shards,out):
 paths(base);import joint,check_joint
 from common_lp import build,certificate,verify
 from degree_types import build_types
 from total_degree import build_total
 from check_total import rebuild_total
 from check_constraints import rebuild,rebuild_types,translate,verify_named,signature
 rows=json.loads((root/'projected_survivors.json').read_text());demands=json.loads((root/'demands.json').read_text());todo=[(i,r) for i,r in enumerate(rows) if i%shards==shard];jcnt=collections.Counter();lpcnt=collections.Counter();start=time.monotonic();final=[]
 stages=[('shared',build,rebuild),('typed',build_types,rebuild_types),('endpoint',build_total,rebuild_total)]
 for pos,row in todo:
  s=demands[row[0]]['s'];state=joint.propagate(s,row[2:],t=t,dmax=10);chk=check_joint.verify_row(s,row[2:],t=t,maxd=10);assert (chk is not None)==(state['kind']=='survivor');jcnt[state['kind']]+=1
  if chk is None:continue
  for key,value in chk.items():assert json.loads(json.dumps(state[key]))==value
  for phase,builder,checker in stages:
   m=builder(s,row[2:],state,t=t);ans=m.solve()
   if ans.status!=2:continue
   c=certificate(m)
   if c is None:continue
   verify(m,c);named=translate(m,c);other=checker(s,row[2:],state,t=t);assert set(m.names)==other.variables
   assert {signature({m.names[j]:v for j,v in e.items()},b) for e,b in m.eq}==set(other.equalities)
   assert {signature({m.names[j]:v for j,v in e.items()},b) for e,b in m.ub}==set(other.inequalities);verify_named(other,named);lpcnt[phase]+=1;break
  else:lpcnt['OPEN']+=1;final.append({'position':pos,'row':row})
 rep={'scope':{'n':29,'Delta':16,'m':208+t,'t':t},'shard':shard,'shards':shards,'positions':[x[0] for x in todo],'input_rows':len(todo),'joint_counts':dict(jcnt),'joint_survivors':sum(lpcnt.values()),'lp_counts':dict(lpcnt),'final_survivors':final,'all_joint_survivor_states_independently_recomputed':True,'all_exact_lp_rejections_independently_rebuilt_and_verified':True,'seconds':time.monotonic()-start}
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(rep,indent=2)+'\n');print(json.dumps({k:v for k,v in rep.items() if k not in ('positions','final_survivors')}));assert not final

def aggregate(root,reports,out):
 summary={}
 for t in (3,2):
  p=root/f't{t}';scan=json.loads((p/'SCAN_REPORT.json').read_text());check=json.loads((p/'CHECK_ROWS_REPORT.json').read_text());assert scan==check
  proj=json.loads((p/'PROJECTED_REPORT.json').read_text());parts=[]
  for q in reports.rglob(f't{t}-*.json'):parts.append(json.loads(q.read_text()))
  expected=proj['survivors'];positions=sorted(x for r in parts for x in r['positions']);assert positions==list(range(expected));assert all(not r['final_survivors'] for r in parts)
  lp=collections.Counter();joint=collections.Counter()
  for r in parts:lp.update(r['lp_counts']);joint.update(r['joint_counts'])
  summary[str(208+t)]={'demand_domain':json.loads((p/'PREPARE_REPORT.json').read_text())['demand_domain'],'residual_rows':scan['states'],'row_survivors':scan['survivors'],'projected_survivors':expected,'joint_counts':dict(joint),'lp_counts':dict(lp),'final_survivors':0}
 assert summary['211']['lp_counts']=={'shared':13,'typed':23}
 assert summary['210']['lp_counts']=={'shared':213,'typed':378,'endpoint':2}
 result={'status':'PASS','scope':'n=29 Delta=16 at m=211 and m=210','results':summary,'all_partition_positions_exactly_covered':True,'independent_row_scanner_agreement':True,'final_survivors':0,'mathematical_status':'CANDIDATE; graph lemmas remain hand proofs; independent review OPEN'}
 out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

if __name__=='__main__':
 p=argparse.ArgumentParser();sp=p.add_subparsers(dest='mode',required=True)
 q=sp.add_parser('prepare');q.add_argument('--base',type=Path,required=True);q.add_argument('--t',type=int,choices=[2,3],required=True);q.add_argument('--output',type=Path,required=True)
 q=sp.add_parser('projected');q.add_argument('--t',type=int,choices=[2,3],required=True);q.add_argument('--root',type=Path,required=True)
 q=sp.add_parser('final');q.add_argument('--base',type=Path,required=True);q.add_argument('--t',type=int,choices=[2,3],required=True);q.add_argument('--root',type=Path,required=True);q.add_argument('--shard',type=int,required=True);q.add_argument('--shards',type=int,required=True);q.add_argument('--output',type=Path,required=True)
 q=sp.add_parser('aggregate');q.add_argument('--root',type=Path,required=True);q.add_argument('--reports',type=Path,required=True);q.add_argument('--output',type=Path,required=True)
 a=p.parse_args()
 if a.mode=='prepare':prepare(a.base,a.t,a.output)
 elif a.mode=='projected':projected(a.t,a.root)
 elif a.mode=='final':final_shard(a.base,a.t,a.root,a.shard,a.shards,a.output)
 else:aggregate(a.root,a.reports,a.output)
