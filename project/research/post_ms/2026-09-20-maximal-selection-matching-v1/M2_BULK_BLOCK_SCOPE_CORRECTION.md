# Scope correction for the m=2 bulk-block argument

Date: 2026-09-20

Status: **mandatory correction** to Section 11 of `MAXIMAL_SELECTION_MATCHING_AND_M1_CLOSURE.md`. The original Section 11 omitted the radius-one exception when excluding the common buffer/core as a criticality witness. The large-X F/R normal-form conclusion survives, but its proof needs the two-case argument below. Future work must cite this correction rather than the unqualified statement in Section 11.

## 1. The missing exception

For a bulk code class `C`, the matched-edge obstruction at a differing coordinate `j` eliminates the buffer and common-core `bar d` witnesses by pointing to **another** `bar d` endpoint shared with the source. That requires

`d_H(C,d)>=2`.

If `d_H(C,d)=1`, there is no second differing coordinate, so the original proof does not force the other code block to contain that unique coordinate. Thus the unqualified statement

`[p]\I_C subseteq I_D`

was too broad.

## 2. Corrected bulk-block lemma

Let `m=2`, `p>=3`, and let `C,D` be the two X'-code classes with disjoint nonempty agreement blocks. If `C` has multiplicity at least two **and**

`d_H(C,d)>=2`,

then the original criticality exhaustion is valid and gives

> `[p]\I_C subseteq I_D`.

Since the blocks are disjoint, this yields

> `I_D=[p]\I_C`.                                        `(BLOCK-PARTITION+)`

## 3. Radius-one bulk class gives the same final normal form directly

Now suppose the bulk class instead has

`d_H(C,d)=1`.

Then `|I_C|=p-1>=2`, so for `p>=3` this class cannot be Type F (a Type-F agreement block is a singleton). It is Type R. Hence

`I_C subseteq I_0`.

But `I_C` already has size `p-1`, while `S_0` is nonempty. Therefore

> `|S_0|=1`, `I_C=I_0`.

The other class has a nonempty agreement block disjoint from `I_C`, so it must be exactly the remaining singleton `S_0`. Such a block is Type F. Thus again

> `I_F=S_0`, `I_R=I_0`, `|S_0|=1`.

The two X'-codes are complementary.

## 4. Corrected large-X theorem

If `x>=4`, the two code classes contain at least three heads in total, so at least one class is bulk.

- If the bulk class has Hamming radius at least two from `d`, apply `(BLOCK-PARTITION+)` and the F/R block-location rules; FF cannot partition `[p]` for `p>=3`, RR cannot cover nonempty `S_0`, so the classes are complementary F/R with `|S_0|=1`.
- If the bulk class has radius one, Section 3 gives the same conclusion directly.

Therefore the companion note's final large-X normal form is **still valid**:

> for maximal `m=2`, `p>=3`, `x>=4`, the two X'-classes are one F and one R, `|S_0|=1`, `I_F=S_0`, `I_R=I_0`, and their codes are complementary. `(M2-FR-NORMAL-CORRECTED)`

Only the intermediate unqualified bulk-block lemma was overstated.

## 5. Consequences retained

All later consequences that use only `(M2-FR-NORMAL-CORRECTED)` remain live, including `M2_FR_RESERVOIR.md`: the R class has one physical graph-fixed witness; `omega>2` forces the F class to be a singleton head with an F-witness star; and the code-swap / physical reservoir pricing remains unchanged.
