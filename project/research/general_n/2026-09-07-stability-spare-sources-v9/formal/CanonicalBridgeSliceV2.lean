import QuasiCore
import CanonicalBridgeSlice
import Std

/-
Second extension of the Murty-Simon local formalisation slice.

This file pins down the local graph-theoretic step used in the isolated-C
injection.  It still does NOT formalise finite-cardinality injections,
residual activity as a global count, threshold-capacity counting, or the
complete Murty-Simon theorem.

No sorry, axiom declaration, or native_decide.
-/
namespace MurtySimon
universe u
variable {V : Type u}

/-- Local isolated-C forcing step.

Suppose `i z -> j` is a quasi-edge whose exception `j` lies on the A side.
If another A-vertex `x` is not the exception and `i` misses `x`, then the
quasi-edge domination rule forces `z-x`.  Symmetry gives `x-z`.

If `x` also misses the exception `j`, then `x-z` cannot itself be a selected
quasi-edge with any distinct exception `b`: the endpoints `x,z` have the
common miss `j`, so uniqueness of a quasi-edge exception forces `b=j`.
This is precisely the local selected/residual separation used in the
isolated-C argument before the global injection/counting step.
-/
theorem isolated_C_forces_cross_edge_and_excludes_other_exception
    {adj : V → V → Prop}
    (symm : ∀ x y, adj x y → adj y x)
    {i z j x b : V}
    (q : Quasi adj i z j)
    (hxj : x ≠ j)
    (hix : ¬ adj i x)
    (hxMissJ : ¬ adj x j)
    (hjb : j ≠ b) :
    adj x z ∧ ¬ Quasi adj x z b := by
  have hzx : adj z x :=
    (q.dominates x hxj).resolve_left hix
  have hxz : adj x z := symm z x hzx
  refine ⟨hxz, ?_⟩
  intro qxz
  exact hjb (common_miss_is_exception qxz hxMissJ q.label_misses)

/-- A direct restatement of the second residual-injection local target.
If two labels `i,j` selected at the same source have distinct supplements
and `i-j` is an F-edge, then the first supplement `w` is adjacent to `j`,
while `j` and `w` have the common A-miss `i`.  Hence `j-w` cannot be selected
with any exception distinct from `i`.
-/
theorem second_residual_injection_local_separation
    {adj : V → V → Prop}
    (symm : ∀ x y, adj x y → adj y x)
    {u i j w z b : V}
    (qi : Quasi adj u i w)
    (qj : Quasi adj u j z)
    (hwz : w ≠ z)
    (hij : ¬ adj i j)
    (hib : i ≠ b) :
    adj j w ∧ ¬ Quasi adj j w b := by
  have forced := two_forced_cross_edges_from_same_source symm qi qj hwz hij
  have hjw : adj j w := forced.1.1
  have hji : ¬ adj j i := forced.1.2.1
  have hwi : ¬ adj w i := forced.1.2.2
  refine ⟨hjw, ?_⟩
  intro qjw
  exact hib (common_miss_is_exception qjw hji hwi)

#print axioms isolated_C_forces_cross_edge_and_excludes_other_exception
#print axioms second_residual_injection_local_separation

end MurtySimon
