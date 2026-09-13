#!/usr/bin/env python3
"""Exact arithmetic replay of the hand case split in MARGIN_CLASS_EXAMPLE.md.

This is deliberately not an optimizer.  It checks the frozen numerical identities
and the four exhaustive locations/types for the unique one-unit incoming deficit.
The mathematical reason each case contradicts realization is documented in the
companion hand proof.
"""
import json

s = [2]*4 + [3]*11
rho = [1]*7 + [2] + [3]*10
q = [0]*7 + [4,3,3,4,4,4,4,4,4,3,4]

assert len(s)==15 and len(rho)==len(q)==18
Q=sum(s); r=sum(rho)
assert Q==41 and r==39 and sum(q)==Q

# Active exact-demand p maxima are rho-1.  The seven inactive rho=1 sources
# retain the ordinary canonical p cap rho+b-a-1=3.
pmax=[3]*7+[1]+[2]*10
assert sum(pmax)==42
assert sum(pmax)-Q==1

# Unique rho=2 source must use all four demand-two labels.
assert q[7]==4 and rho[7]==2 and s.count(2)==4

# Three q=3,rho=3 sources: nine incidences total.  In the first three
# deficit classes four go to demand-two labels, leaving 5, not divisible by 3.
q3_sources=[u for u in range(18) if rho[u]==3 and q[u]==3]
q4_rho3=[u for u in range(18) if rho[u]==3 and q[u]==4]
assert len(q3_sources)==3 and len(q4_rho3)==7
left_q3=3*3-4
assert left_q3==5 and left_q3%3!=0

# In the remaining deficit class, k cancels: at most nine C=5-capable
# incidences remain on demand-three labels.
for k in range(5):
    capable=(9-(4-k))+(4-k)
    assert capable==9

# Raw cross-degree total forces six of the eleven demand-three labels to C=5.
C_total=r+Q
C_demand2=4*5
C_demand3=C_total-C_demand2
h=C_demand3-5*11
assert C_total==80 and C_demand3==60 and h==5
num_C5=11-h
needed_C5_inc=3*num_C5
assert num_C5==6 and needed_C5_inc==18 and 18>9

out={
    "schema":"margin-class-example-arithmetic-v1",
    "state":{"layer":"n34-m289","state_id":227},
    "Q":Q,"r":r,
    "incoming_max_total":sum(pmax),
    "incoming_required_total":Q,
    "unique_deficit_units":1,
    "q3_demand3_left_in_first_three_cases":left_q3,
    "q4_deficit_case_C5_capable_incidences":9,
    "q4_deficit_case_C5_labels_required":num_C5,
    "q4_deficit_case_C5_incidences_required":needed_C5_inc,
    "status":"PASS",
    "scope":"Arithmetic replay of the hand proof; margin-class exclusion only, not whole-state exclusion."
}
print(json.dumps(out,indent=2))
with open("MARGIN_CLASS_VERIFICATION.json","w",encoding="utf-8") as f:
    json.dump(out,f,indent=2); f.write("\n")
