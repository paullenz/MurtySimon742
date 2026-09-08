# Exploratory multi-threshold relaxation — NOT A PROOF

8 September 2026.

To decide whether further work on demand tails is worthwhile, a continuous normalised relaxation was discretised on demand values x=s/a. It imposed simultaneously:

- total mass one and total demand y;
- the charging-defect dispersion budget;
- the residual lower cost sum x^2/(1-x);
- the residual upper budget r/a^2 <= y-2c+2epsilon;
- demand-tail capacity at many thresholds theta:

  W(theta) <= 1/2 [ (R/theta)^2 + theta^2 ].

On a 401-point x grid and thresholds spaced by 0.01, feasibility did not appear until epsilon was approximately 0.00903. If that relaxation could eventually be converted into a rigorous theorem, the corresponding degree coefficient would be around 0.6085.

**This numerical observation is not a theorem, certificate, or claimed bound.** Grid discretisation can create artefacts; the relaxation omits finite-a rounding; and the optimisation has not been converted into exact Farkas certificates or a hand inequality. The only proved candidate improvement in this checkpoint is the one-threshold epsilon=1/750 result giving the conservative 0.6126 coefficient.

The research value of the experiment is directional: it suggests that several demand thresholds may encode substantially more of the shared source-supplement competition than the current one-threshold proof.
