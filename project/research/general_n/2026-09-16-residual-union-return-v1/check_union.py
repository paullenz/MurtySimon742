#!/usr/bin/env python3
"""Direct finite premise checks for residual-set union forcing.
These are set/array models, not original edge-critical graphs.
"""
import itertools,json
from pathlib import Path

def run():
    valid=nonempty=overlap=0
    for n in range(1,6):
        for status in itertools.product(range(3),repeat=n):
            Su=sum(1<<i for i,x in enumerate(status) if x==1)
            Ru=sum(1<<i for i,x in enumerate(status) if x==2)
            for Rv in range(1<<n):
                for F in range(1<<n):
                    if F&~(Su|Ru) or (F&Su)&~Rv: continue
                    assert not F&~(Ru|Rv)
                    assert F.bit_count()<=(Ru|Rv).bit_count()
                    assert F.bit_count()<=Ru.bit_count()+Rv.bit_count()-(Ru&Rv).bit_count()
                    valid+=1
                    nonempty+=bool(F&Su)
                    overlap+=bool(Ru&Rv)
    core_tests=eligible=one_hole_controls=0
    for d in range(2,7):
        core=(1<<d)-1
        for Ru in range(1<<d):
            for Rv in range(1<<(d+3)):
                outside=(Rv&~core).bit_count()
                for s in range(1,4):
                    core_tests+=1
                    if (Ru|Rv).bit_count()>=d+s:
                        eligible+=1
                        assert outside>=s
                        assert outside>=d+s-((Ru|Rv)&core).bit_count()
                    # A low source selecting a one-hole core neighbour needs d-1 core labels.
                    if Rv.bit_count()<=d-1 and (Rv&core).bit_count()>=d-1:
                        one_hole_controls+=1
                        assert (Ru|Rv).bit_count()<d+s
    # Explicit nonvacuous strict improvement over endpoint degree sum.
    Ru={0,1,2,3}; Rv={0,1,2,4}; required_degree=7
    assert len(Ru)+len(Rv)==8 and len(Ru|Rv)==5<required_degree
    # Dropping exact source containment weakens the profile-defect threshold.
    core={0,1,2}; Ru={0,1,3}; Rv={2}; h0=3;s=1
    assert len(Ru|Rv)>=h0+s and not (Rv-core)
    return {'status':'PASS_RESIDUAL_UNION_PREMISE_TESTS_ONLY',
            'valid_set_premise_cases':valid,
            'cases_with_nonempty_forced_destination_residual':nonempty,
            'cases_with_source_destination_residual_overlap':overlap,
            'profile_threshold_arrays':core_tests,
            'arrays_passing_union_degree_threshold':eligible,
            'one_hole_selection_incompatibility_arrays':one_hole_controls,
            'controls':[{'kind':'degree_sum_can_pass_while_union_fails',
                         'source_residual':[0,1,2,3],'destination_residual':[0,1,2,4],
                         'required_degree':7,'sum_capacity':8,'union_capacity':5},
                        {'kind':'source_core_containment_is_required_for_full_receiver_penalty',
                         'core':[0,1,2],'source_residual':[0,1,3],
                         'receiver_residual':[2],'required_degree':4}],
            'scope':'Finite sets and parameter arrays assuming stated local premises; not validation of the canonical bridge'}
if __name__=='__main__':
    out=run();Path(__file__).with_name('UNION_CHECK_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
