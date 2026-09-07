import Std

/-
First formalisation slice only. No numerical or graph-wide theorem is
claimed formalised here. No sorry, axiom declaration, or native_decide.
The relation, actual quasi-edge premises, and symmetry are explicit.
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

#print axioms common_miss_is_exception
#print axioms exception_unique
#print axioms missing_source_forces_label_neighbour
#print axioms cross_forcing_with_common_miss
#print axioms forced_cross_edge_cannot_have_other_exception
end MurtySimon
