#!/usr/bin/env python3
"""Third audit of all frozen states/columns using threshold min-cut bounds.

Imports neither scanner nor the certificate checker. Domain cardinalities use
generating-function coefficients. Matching uses the min-cut formula for nested
threshold neighbourhoods, not either scanner's matching algorithm.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import gzip
import hashlib
import json
import math
import time

ROOT=Path(__file__).resolve().parent.parent
OUT=Path(__file__).resolve().parent
COUNTS=Counter()


def need(ok,label):
    if not ok:raise AssertionError(label)
    COUNTS[label]+=1


@lru_cache(None)
def coefficient(slots,total,lo,hi):
    if total<0 or hi<lo:return 0
    dp=[[0]*(total+1) for _ in range(slots+1)];dp[0][0]=1
    for value in range(lo,hi+1):
        for number in range(1,slots+1):
            for weight in range(value,total+1):
                dp[number][weight]+=dp[number-1][weight-value]
    return dp[slots][total]


def columns_coefficient(lower,total,upper):
    dp=[0]*(total+1);dp[0]=1
    for low in lower:
        following=[0]*(total+1)
        for weight,count in enumerate(dp):
            if count:
                for value in range(low,min(upper,total-weight)+1):following[weight+value]+=count
        dp=following
    return dp[total]


class ThresholdCut:
    def __init__(self,ds,rs):
        self.ds=ds;self.rs=rs;self.a=len(ds);self.b=len(rs);self.full=(1<<self.a)-1
        self.cuts={};self.q_masks={};self.cache={rb:{} for rb in set(rs)}
        for rb in set(rs):
            supplies=[rb+rw for rw in rs];supplies.remove(2*rb)
            self.cuts[rb]=[(sum(1<<i for i,d in enumerate(ds) if d<t),sum(c>=t for c in supplies)) for t in set(ds)]
            self.q_masks[rb]=[(q,sum(1<<i for i,d in enumerate(ds) if d<=rb+q-1)) for q in range(min(self.a-rb,self.b-1),0,-1)]

    def matching(self,rb,mask):
        return min([mask.bit_count()]+[(mask&below).bit_count()+supplies for below,supplies in self.cuts[rb]])

    def cap(self,rb,mask):
        cache=self.cache[rb]
        if mask not in cache:
            cache[mask]=next((q for q,closure in self.q_masks[rb] if self.matching(rb,mask&closure)>=q),0)
        return cache[mask]

    def caps(self,R=None):
        by_type={}
        for rb in self.cache:
            mask=self.full if R is None else sum(1<<i for i,d in enumerate(self.ds) if d-R[i]<=rb)
            by_type[rb]=self.cap(rb,mask)
        return [by_type[rb] for rb in self.rs]

    def refine(self,caps):
        by_type={}
        for rb in self.cache:
            index=self.rs.index(rb);other=[r+c for i,(r,c) in enumerate(zip(self.rs,caps)) if i!=index]
            by_type[rb]=next(q for q in range(caps[index],-1,-1) if sum(x>=q-1 for x in other)>=q)
        return [by_type[rb] for rb in self.rs]


def exhaustive_matching_check():
    # Direct injection search validates the min-cut identity on small instances.
    def brute(labels,supplies):
        if not labels:return 0
        best=brute(labels[1:],supplies)
        for i,c in enumerate(supplies):
            if labels[0]<=c:best=max(best,1+brute(labels[1:],supplies[:i]+supplies[i+1:]))
        return best
    for count_l in range(5):
        for count_s in range(5):
            for labels in combinations_with_repetition(range(4),count_l):
                for supplies in combinations_with_repetition(range(4),count_s):
                    formula=min([len(labels)]+[sum(d<t for d in labels)+sum(c>=t for c in supplies) for t in set(labels)])
                    need(formula==brute(labels,supplies),'min_cut_vs_exhaustive_injections')


def combinations_with_repetition(values,length):
    from itertools import combinations_with_replacement
    return combinations_with_replacement(values,length)


def inspect_scope(name,folder,a,b,L,t):
    started=time.monotonic();summary=json.loads((folder/'primary_summary.json').read_text())
    by_band={(row['k'],row['r']):row for row in summary['rows']}
    observed=Counter();kinds={kr:Counter() for kr in by_band};keys=set();columns_total=0;survivors={}
    for (k,r),row in by_band.items():
        D=a-1-k
        expected=(coefficient(a,2*(r+t),0,D)-coefficient(a,2*(r+t),0,D-1))*coefficient(b,r,1,a)
        need(expected==row['states'],'independent_outer_cardinality')
    with gzip.open(folder/'primary_ledger.jsonl.gz','rt',encoding='ascii') as stream:
        for line in stream:
            row=json.loads(line);key=row['key'];k,r,ds,rs=json.loads(key);kind=row['kind'];w=row['witness']
            need(key not in keys,'unique_outer_key');keys.add(key)
            need((k,r) in by_band and b<=r<=L-(a*k+1)//2,'outer_band_membership')
            need(len(ds)==a and ds==sorted(ds) and 0<=min(ds) and max(ds)==a-1-k and sum(ds)==2*(r+t),'degree_domain_membership')
            need(len(rs)==b and rs==sorted(rs) and min(rs)>=1 and max(rs)<=a and sum(rs)==r,'residual_domain_membership')
            observed[k,r]+=1;kinds[k,r][kind]+=1
            if kind=='pair_threshold':
                cut=w['threshold'];labels=[d for d in ds if d>=cut]
                required=sum(labels)-sum(min(rb,len(labels)) for rb in rs)
                available=sum(x+y>=cut for x,y in combinations(rs,2))
                need(1<=cut<=max(ds) and required==w['lower'] and available==w['upper'] and required>available,'pair_prune_recomputed')
                continue
            model=ThresholdCut(ds,rs);caps=model.caps()
            if kind=='source_total':
                need(caps==w['caps'] and sum(caps)==w['upper'] and w['lower']==r+2*t and sum(caps)<r+2*t,'source_total_prune_recomputed')
                continue
            if kind=='source_threshold':
                cut=w['threshold'];mask=sum(1<<i for i,d in enumerate(ds) if d>=cut)
                required=sum(d for d in ds if d>=cut)-sum(min(rb,mask.bit_count()) for rb in rs)
                bound=[]
                for rb,c in zip(rs,caps):
                    eligible=mask&sum(1<<i for i,d in enumerate(ds) if d<rb+c)
                    bound.append(min(c,model.matching(rb,eligible)))
                need(bound==w['source_caps'] and sum(bound)==w['upper'] and required==w['lower'] and required>sum(bound),'source_threshold_prune_recomputed')
                continue
            h=max([0]+[j for j in range(1,b+1) if sum(rb>=j for rb in rs)>=j]);lower=[max(0,d-h) for d in ds]
            need(h==w['h'] and lower==w['lower_columns'],'column_lower_vector_recomputed')
            if kind=='column_lower_bound':
                need(sum(lower)>r and sum(lower)==w['lower'] and w['budget']==r,'column_lower_prune_recomputed')
                continue
            need(kind in ('all_columns','survives'),'recognized_final_kind')
            expected_columns=columns_coefficient(lower,r,b)
            need(expected_columns==w['column_count']==len(w['columns']),'independent_labelled_column_cardinality')
            seen_columns=set();actual_survivors=[]
            for col in w['columns']:
                R=col['columns'];rr=tuple(R)
                need(rr not in seen_columns,'unique_labelled_column');seen_columns.add(rr)
                need(len(R)==a and sum(R)==r and all(low<=x<=b for low,x in zip(lower,R)),'column_domain_membership')
                demand=sum(max(0,d-x) for d,x in zip(ds,R))
                cc=model.caps(R);refined=cc if sum(cc)<demand else model.refine(cc)
                need(cc==col['caps'] and refined==col['refined_caps'],'every_column_cap_recomputed_by_min_cut')
                need(demand==col['required'] and sum(refined)==col['upper'],'every_column_margin_recomputed')
                if sum(refined)>=demand:
                    actual_survivors.append(col);survivors[(key,rr)]=(ds,rs,refined)
                columns_total+=1
            need(actual_survivors==w['survivors'] and bool(actual_survivors)==(kind=='survives'),'surviving_column_list_recomputed')
            if COUNTS['independent_labelled_column_cardinality']%200==0:
                print(json.dumps(dict(scope=name,outer=len(keys),columns=columns_total,elapsed=round(time.monotonic()-started,1))),flush=True)
    need(len(keys)==summary['state_count'],'total_outer_count')
    fingerprint=hashlib.sha256(('\n'.join(sorted(keys))+'\n').encode()).hexdigest()
    need(fingerprint==summary['state_key_sha256'],'outer_key_fingerprint')
    for band,row in by_band.items():
        need(observed[band]==row['states'] and dict(kinds[band])==row['dispositions'],'complete_band_coverage')
    need(columns_total==summary['column_vectors'],'total_column_count')
    cert_path=folder/'hall_certificates.json'
    if cert_path.is_file():
        certificate=json.loads(cert_path.read_text())
        need(certificate['input_sha256']==hashlib.sha256((folder/'primary_ledger.jsonl.gz').read_bytes()).hexdigest(),'certificate_input_hash')
        covered=set()
        for item in certificate['certificates']:
            lookup=(item['key'],tuple(item['columns']))
            need(lookup in survivors and lookup not in covered,'certificate_unique_coverage')
            covered.add(lookup);ds,rs,caps=survivors[lookup]
            need(caps==item['caps'],'certificate_caps_rederived')
            R=item['columns'];subset=item['witness']['subset']
            need(subset and len(set(subset))==len(subset) and all(0<=i<a for i in subset),'certificate_subset_valid')
            demand=sum(max(0,ds[i]-R[i]) for i in subset)
            bounds=[min(c,sum(ds[i]<=rb+c-1 and ds[i]<=rb+R[i] for i in subset)) for rb,c in zip(rs,caps)]
            need(demand>sum(bounds) and demand==item['witness']['required'] and bounds==item['witness']['by_source'] and sum(bounds)==item['witness']['available'],'certificate_strict_contradiction_recomputed')
        need(covered==set(survivors) and not certificate['survivors'] and certificate['surviving_columns']==0,'zero_uncertified_survivors')
        need(certificate['checked']==certificate['eliminated']==len(covered),'certificate_totals')
    else:need(not survivors,'scope_needs_no_additional_certificates')
    result=dict(scope=name,outer_states=len(keys),columns=columns_total,final_certificates=len(survivors),elapsed_seconds=round(time.monotonic()-started,2))
    print(json.dumps(result),flush=True)
    return result


def main():
    exhaustive_matching_check()
    need(Fraction(25**2,4)+(Fraction(25**2)-Fraction(162,10)*25+56)/320==Fraction(12569,80),'Fan_exact_arithmetic')
    tables={str(T):[math.comb(h,2)+h*(25-h)+2*math.comb(T-2*h,2) for h in range(T//2+1)] for T in [11,13]}
    need(tables['11']==[110,96,89,89,96,110] and tables['13']==[156,134,119,111,110,116,129],'witness_table_exact')
    base=ROOT/'N25_Full_Chain_Candidate_2026-09-06_v1'
    configs=[('d14_157',ROOT/'review_evidence/results',10,14,42,3),('d15_157',base/'d15_157',9,15,29,7),('d15_156',base/'d15_156',9,15,30,6),('d14_156',base/'d14_156',10,14,43,2),('d14_156_k1',base/'d14_156_k1',10,14,43,2)]
    scopes=[inspect_scope(*cfg) for cfg in configs]
    domains=[]
    for edges in [156,157]:
        for a in [8,9,10]:
            b=24-a;L=300-edges-a-math.comb(b,2);t=math.comb(a,2)-L
            bands=set();exclusions=[]
            for k in range(a):
                small_limit=L-math.comb(a-1,2) if k==0 else L-1-math.comb(a-2,2) if k==1 else None
                if small_limit is not None and b>small_limit:
                    exclusions.append(dict(k=k,reason='low_k',upper=small_limit));continue
                bands.update((k,r) for r in range(b,L-(a*k+1)//2+1))
            recorded=set()
            for name,folder,aa,bb,LL,tt in configs:
                if (aa,bb,LL,tt)==(a,b,L,t):recorded.update((row['k'],row['r']) for row in json.loads((folder/'primary_summary.json').read_text())['rows'])
            need(bands==recorded,'all_k_r_bands_covered')
            domains.append(dict(edges=edges,a=a,b=b,L=L,t=t,retained_bands=sorted(bands),low_k_exclusions=exclusions))
    result=dict(status='PASS',scope='Third arithmetic audit; graph-theoretic lemmas remain external premises',imports_existing_verifiers=False,counts=dict(COUNTS),scopes=scopes,domains=domains,witness_tables=tables)
    (OUT/'arithmetic_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status='PASS',counts=dict(COUNTS),scopes=scopes)),flush=True)


if __name__=='__main__':main()
