import Std

/-
Local formalisation slice only. No numerical or graph-wide theorem is
claimed formalised here. No sorry, axiom declaration, or native_decide.
The relation, actual quasi-edge premises, symmetry, and the local
edge-insertion bridge used below are explicit.
-/
namespace MurtySimon
universe u
variable {V : Type u}

structure Quasi (adj : V → V → Prop) (u i w : V) : Prop where
  edge : adj u i
  source_misses : ¬ adj u w
  label_misses : ¬ adj i w
  dominates : ∀ j, j ≠ w → adj u j ∨ adj i j

theorem common_miss_is_exception {adj : V → V → Prop} {u i w j : V}
    (q : Quasi adj u i w) (hu : ¬ adj u j) (hi : ¬ adj i j) : j = w := by
  apply Classical.byContradiction
  intro hne
  exact (q.dominates j hne).elim hu hi

theorem exception_unique {adj : V → V → Prop} {u i w z : V}
    (q : Quasi adj u i w) (q' : Quasi adj u i z) : w = z := by
  exact common_miss_is_exception q' q.source_misses q.label_misses

theorem missing_source_forces_label_neighbour {adj : V → V → Prop}
    {u i w j : V} (q : Quasi adj u i w) (hj : j ≠ w)
    (hmiss : ¬ adj u j) : adj i j := by
  exact (q.dominates j hj).resolve_left hmiss

/-- If two selected quasi-edges have the same source and different
exceptions, the exception of either one is adjacent to the other label.
This is the local supplement-forcing fact used in the demand-tail proof. -/
theorem supplement_neighbours_other_label {adj : V → V → Prop}
    {u i j w z : V} (qi : Quasi adj u i w) (qj : Quasi adj u j z)
    (hwz : w ≠ z) : adj j w := by
  exact (qj.dominates w hwz).resolve_left qi.source_misses

theorem cross_forcing_with_common_miss {adj : V → V → Prop}
    (symm : ∀ x y, adj x y → adj y x) {u i j w z : V}
    (qi : Quasi adj u i w) (qj : Quasi adj u j z)
    (hwz : w ≠ z) (hij : ¬ adj i j) :
    adj i z ∧ ¬ adj i j ∧ ¬ adj z j := by
  have hiz : adj i z :=
    missing_source_forces_label_neighbour qi (Ne.symm hwz) qj.source_misses
  refine ⟨hiz, hij, ?_⟩
  intro hzj
  exact qj.label_misses (symm z j hzj)

theorem forced_cross_edge_cannot_have_other_exception {adj : V → V → Prop}
    (symm : ∀ x y, adj x y → adj y x) {u i j w z b : V}
    (qi : Quasi adj u i w) (qj : Quasi adj u j z)
    (hwz : w ≠ z) (hij : ¬ adj i j) (hjb : j ≠ b) :
    ¬ Quasi adj i z b := by
  intro qb
  have h := cross_forcing_with_common_miss symm qi qj hwz hij
  exact hjb (common_miss_is_exception qb h.2.1 h.2.2)

/- The following definitions formalise the local bridge from adding one
missing complement edge to obtaining a quasi-edge. They do not encode
finite graphs, edge-criticality, minimum degree, or any counting theorem. -/
def addEdge (adj : V → V → Prop) (u w : V) : V → V → Prop :=
  fun x y => adj x y ∨ (x = u ∧ y = w) ∨ (x = w ∧ y = u)

structure AdjTotalDominates (adj : V → V → Prop) (x y : V) : Prop where
  edge : adj x y
  dominates : ∀ z, adj x z ∨ adj y z

theorem added_edge_is_old_if_left_avoids_endpoints
    {adj : V → V → Prop} {u w x y : V}
    (hxu : x ≠ u) (hxw : x ≠ w) (h : addEdge adj u w x y) : adj x y := by
  rcases h with h | h | h
  · exact h
  · exact False.elim (hxu h.1)
  · exact False.elim (hxw h.1)

theorem new_adj_total_pair_is_incident_to_added_edge
    {adj : V → V → Prop} {u w x y : V}
    (noOld : ∀ p q, ¬ AdjTotalDominates adj p q)
    (q : AdjTotalDominates (addEdge adj u w) x y) :
    x = u ∨ x = w ∨ y = u ∨ y = w := by
  by_cases hxu : x = u
  · exact Or.inl hxu
  by_cases hxw : x = w
  · exact Or.inr (Or.inl hxw)
  by_cases hyu : y = u
  · exact Or.inr (Or.inr (Or.inl hyu))
  by_cases hyw : y = w
  · exact Or.inr (Or.inr (Or.inr hyw))
  have old : AdjTotalDominates adj x y := by
    refine ⟨added_edge_is_old_if_left_avoids_endpoints hxu hxw q.edge, ?_⟩
    intro z
    rcases q.dominates z with hx | hy
    · exact Or.inl (added_edge_is_old_if_left_avoids_endpoints hxu hxw hx)
    · exact Or.inr (added_edge_is_old_if_left_avoids_endpoints hyu hyw hy)
  exact False.elim (noOld x y old)

theorem added_endpoint_pair_fails_with_common_miss
    {adj : V → V → Prop} {u w v : V}
    (huv : u ≠ v) (hwv : w ≠ v)
    (hu : ¬ adj u v) (hw : ¬ adj w v) :
    ¬ AdjTotalDominates (addEdge adj u w) u w := by
  intro q
  rcases q.dominates v with h | h
  · rcases h with h | h | h
    · exact hu h
    · exact hwv h.2.symm
    · exact huv h.2.symm
  · rcases h with h | h | h
    · exact hw h
    · exact hwv h.2.symm
    · exact huv h.2.symm

theorem quasi_from_added_total_pair
    {adj : V → V → Prop} {u i w : V}
    (noOld : ∀ p q, ¬ AdjTotalDominates adj p q)
    (huw : u ≠ w) (hiu : i ≠ u) (hiw : i ≠ w)
    (hmiss : ¬ adj u w)
    (q : AdjTotalDominates (addEdge adj u w) u i) :
    Quasi adj u i w := by
  have hui : adj u i := by
    rcases q.edge with h | h | h
    · exact h
    · exact False.elim (hiw h.2)
    · exact False.elim (hiu h.2)
  have oldDomAway : ∀ z, z ≠ w → adj u z ∨ adj i z := by
    intro z hzw
    rcases q.dominates z with hu | hi
    · rcases hu with h | h | h
      · exact Or.inl h
      · exact False.elim (hzw h.2)
      · exact False.elim (huw h.1)
    · exact Or.inr (added_edge_is_old_if_left_avoids_endpoints hiu hiw hi)
  have hiMiss : ¬ adj i w := by
    intro hiwEdge
    have old : AdjTotalDominates adj u i := by
      refine ⟨hui, ?_⟩
      intro z
      by_cases hzw : z = w
      · subst z
        exact Or.inr hiwEdge
      · exact oldDomAway z hzw
    exact noOld u i old
  exact ⟨hui, hmiss, hiMiss, oldDomAway⟩

#print axioms common_miss_is_exception
#print axioms exception_unique
#print axioms missing_source_forces_label_neighbour
#print axioms supplement_neighbours_other_label
#print axioms cross_forcing_with_common_miss
#print axioms forced_cross_edge_cannot_have_other_exception
#print axioms added_edge_is_old_if_left_avoids_endpoints
#print axioms new_adj_total_pair_is_incident_to_added_edge
#print axioms added_endpoint_pair_fails_with_common_miss
#print axioms quasi_from_added_total_pair
end MurtySimon
