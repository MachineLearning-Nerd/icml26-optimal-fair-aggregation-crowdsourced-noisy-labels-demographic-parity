# Source audit

## Paper identity

The audited paper is *Optimal Fair Aggregation of Crowdsourced Noisy Labels
using Demographic Parity Constraints*, by Gabriel Singer, Samuel Gruffaz,
Olivier Vo Van, Nicolas Vayatis, and Argyris Kalogeratos.

- [arXiv:2601.23221](https://arxiv.org/abs/2601.23221)
- [OpenReview niQUth28zn](https://openreview.net/forum?id=niQUth28zn)
- [Current repository](https://github.com/MachineLearning-Nerd/icml26-optimal-fair-aggregation-crowdsourced-noisy-labels-demographic-parity)

This repository is an independent reproduction and audit, not the authors'
implementation and not an author endorsement.

## Pinned source and assumptions

The current verification page records the ar5iv HTML source retrieved on
2026-07-30 with SHA-256:

```text
f6a147f01856d20e54047311773d98e90123be014ee8372b2fdac3c9f9c44835
```

The C2 audit uses heterogeneous group-dependent skill sequences and a nonzero
target `DeltaDP(Y)=0.2`, unlike the homogeneous `p=0.75` historical judged
setup. This distinction is why the old baseline is preserved separately from
the current exact enumeration.

## Interpretation boundary

- C2 enumerates finite cases through `R=16` and audits the reconstructed
  Theorem 3.4 derivation; it does not replace the asymptotic proof.
- C5 compares against a dense `121x121` threshold grid, not an exact LP solver.
- C1, C3, and C4 are historical or finite Monte Carlo checks with the limits
  recorded in their artifacts.

The evaluator-facing source and raw artifacts are under `space_overlay/`.
