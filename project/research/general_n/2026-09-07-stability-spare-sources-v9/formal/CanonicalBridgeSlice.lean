import QuasiCore
import Std

/-
Extension of the existing Murty-Simon local formalisation slice.

Scope is deliberately explicit.  This file formalises additional *local*
quasi-edge consequences used by the canonical selected/residual bridge and
kernel-checks finite arithmetic consequences relevant to the current fixed
orders.  It does NOT formalise the global finite-cardinality injections,
residual-activity count, threshold-capacity count, isolated-C count, or a
complete Murty-Simon theorem.

No sorry, axiom declaration, or native_decide.
-/
namespace MurtySimon
universe u
variable {V : Type u}

/-- Endpoint-load local fact for an incoming selected orientation.
If `ui -> w` is selected and another selected pair is oriented `y -> u`,
then, provided `y` is not the exception `w`, label `i` must neighbour `y`.
The symmetry premise converts the incoming source's missing edge `y-u`
into the missing edge `u-y` required by the quasi-edge domination rule. -/
theorem incoming_source_neighbours_selected_label
    {adj : V → V → Prop}
    (symm : ∀ x y, adj x y → adj y x)
    {u i w y j : V}
    (qi : Quasi adj u i w)
    (qy : Quasi adj y j u)
    (hyw : y ≠ w) :
    adj i y := by
  have huy : ¬ adj u y := by
    intro huyEdge
    exact qy.source_misses (symm u y huyEdge)
  exact (qi.dominates y hyw).resolve_left huy

/-- The two local residual targets forced by an F-edge `ij` whose two
endpoints are selected from the same source `u` with distinct exceptions.
Each forced cross-edge comes equipped with an explicit common A-miss,
which is the local reason it cannot itself be a selected representative
with a different B-exception. -/
theorem two_forced_cross_edges_from_same_source
    {adj : V → V → Prop}
    (symm : ∀ x y, adj x y → adj y x)
    {u i j w z : V}
    (qi : Quasi adj u i w)
    (qj : Quasi adj u j z)
    (hwz : w ≠ z)
    (hij : ¬ adj i j) :
    (adj j w ∧ ¬ adj j i ∧ ¬ adj w i) ∧
    (adj i z ∧ ¬ adj i j ∧ ¬ adj z j) := by
  have hji : ¬ adj j i := by
    intro hjiEdge
    exact hij (symm j i hjiEdge)
  have left :=
    cross_forcing_with_common_miss symm qj qi (Ne.symm hwz) hji
  have right :=
    cross_forcing_with_common_miss symm qi qj hwz hij
  exact ⟨left, right⟩

/-- A forced cross-edge with an A-vertex common miss cannot be another
selected quasi-edge whose exception is a distinct vertex.  This is the
exact local selected/residual separation used repeatedly in the bridge. -/
theorem common_A_miss_excludes_distinct_exception
    {adj : V → V → Prop}
    {x y a b : V}
    (qab : Quasi adj x y b)
    (hxa : ¬ adj x a)
    (hya : ¬ adj y a)
    (hab : a ≠ b) : False := by
  exact hab (common_miss_is_exception qab hxa hya)

/-! ## Kernel-checked finite arithmetic used by current fixed orders

The propositions are written over `Int` after coercing a finite index,
so negative charging numerators are represented faithfully rather than
being truncated by natural-number subtraction.
-/

/-- n=29, Delta=16 pointwise charging cap:
    2*s*(13-2*s) <= 5*(12-s) for every integer s=0,...,11. -/
theorem n29_delta16_pointwise_charging_cap :
    ∀ s : Fin 12,
      (2 : Int) * (s.val : Int) * (13 - 2 * (s.val : Int)) ≤
        5 * (12 - (s.val : Int)) := by
  decide

/-- n=30, Delta=16 pointwise charging cap:
    3*s*(14-2*s) <= 8*(13-s) for every integer s=0,...,12. -/
theorem n30_delta16_pointwise_charging_cap :
    ∀ s : Fin 13,
      (3 : Int) * (s.val : Int) * (14 - 2 * (s.val : Int)) ≤
        8 * (13 - (s.val : Int)) := by
  decide

/-- Exact threshold-capacity gap comparison on the full residual/source
range needed at n=28,29,30 (all have b<=16).  This checks the potentially
counterintuitive case `z-h-j < 0` as well: the target expression still
majorises the pre-compression counting bound. -/
theorem threshold_capacity_gap_b16 :
    ∀ z h j : Fin 17,
      (2 : Int) * ((z.val : Int) - (j.val : Int)) * (h.val : Int)
        + 2 * (j.val : Int) * (z.val : Int)
        - (j.val : Int) * ((j.val : Int) + 1)
      ≤
      (z.val : Int) * (z.val : Int) - (z.val : Int)
        + (h.val : Int) * ((h.val : Int) + 1) := by
  decide

/-- Fixed-order residual h-index parabola bound in a range containing all
current a,h values.  Multiplying by four avoids floor/division issues:
4*((a+1)h-h^2) <= (a+1)^2. -/
theorem residual_hindex_parabola_fixed_range :
    ∀ a h : Fin 17,
      (4 : Int) * (((a.val : Int) + 1) * (h.val : Int)
        - (h.val : Int) * (h.val : Int))
      ≤ ((a.val : Int) + 1) * ((a.val : Int) + 1) := by
  decide

#print axioms incoming_source_neighbours_selected_label
#print axioms two_forced_cross_edges_from_same_source
#print axioms common_A_miss_excludes_distinct_exception
#print axioms n29_delta16_pointwise_charging_cap
#print axioms n30_delta16_pointwise_charging_cap
#print axioms threshold_capacity_gap_b16
#print axioms residual_hindex_parabola_fixed_range

end MurtySimon
