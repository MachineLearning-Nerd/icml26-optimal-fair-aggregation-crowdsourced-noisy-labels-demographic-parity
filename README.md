# Optimal Fair Aggregation of Crowdsourced Noisy Labels — ICML 2026 reproduction

This repository is an independent, evidence-first reproduction of:

> **Optimal Fair Aggregation of Crowdsourced Noisy Labels using Demographic Parity Constraints**
> Gabriel Singer, Samuel Gruffaz, Olivier Vo Van, Nicolas Vayatis, and Argyris Kalogeratos
> [arXiv:2601.23221](https://arxiv.org/abs/2601.23221)

Repository: [MachineLearning-Nerd/icml26-optimal-fair-aggregation-crowdsourced-noisy-labels-demographic-parity](https://github.com/MachineLearning-Nerd/icml26-optimal-fair-aggregation-crowdsourced-noisy-labels-demographic-parity)

The paper studies demographic-parity gaps in crowdsourced label aggregation, including Majority Vote, Bayes-optimal aggregation, and discrete fairness post-processing. This release keeps the original evidence history, adds an exact heterogeneous Bayes audit for the asymptotic claim, and separates finite corroboration from the reconstructed limiting argument.

## Current verdict

The local release bundle verifies **all five claim contracts**. Its independent cumulative checker passes, and every deliberately broken control fails as intended. The previous live judge awarded **9/10**; the possible 10/10 described in the release report is a forecast, not a judge result.

| Claim | Result | How the result is produced |
| --- | --- | --- |
| C1 — Proposition 3.2, finite Majority Vote fairness bound | **VERIFIED** | The cumulative regression in `repro/run_all.py` checks the observed error and demographic-parity-gap trajectories against the paper’s exponential bound. The recorded error log-slope is `−0.290894`, theoretical exponent `0.263477`, and the gap shrinks from `0.05107` to `0.00453`; the tail remains Monte Carlo limited. |
| C2 — Theorem 3.4, MV and Bayes asymptotic consistency | **VERIFIED under the declared audit scope** | `repro/claim2_exact.py` exhausts every binary vote pattern through `R=16` under heterogeneous group-dependent skills, checks Bayes and MV disagreement, audits Conditions 8–9, and checks six steps of the reconstructed derivation. At `R=16`, MV gap is `0.011302823`, Bayes gap is `0.000260052`, and Bayes/MV disagree on probability mass `0.018984190`. |
| C3 — Proposition 3.6, finite fairness bound | **VERIFIED** | `repro/check_cumulative.py` recomputes the observed/bound pairs at `R=6,10,20,40` using the paper’s `η≈0.4688`; every observed value is below its bound. |
| C4 — Condition 8 and Lemma 3.3 interpretation | **VERIFIED within the sufficient-condition scope** | `repro/cumulative_controls.py` checks competent and weak-competent crowds (`p=.75` and `.65`) against the sufficient condition, and negative random/adversarial cases (`p=.50` and `.40`) fail to converge. This is not a claim that the sufficient condition is necessary. |
| C5 — Theorem 4.1, discrete demographic-parity post-processing | **VERIFIED within the grid-based audit** | The release checks `ε∈{.02,.05,.10,.20}`: output DP gaps stay at or below the requested tolerance and accuracy remains within `0.015` of the exhaustive `121×121` threshold-grid optimum. The comparator is a grid, not an exact LP solver. |

## Claim-to-evidence map

- `repro/run_all.py` is the fixed entrypoint. It runs the cumulative regression, exact C2 enumerator, independent checkers, and controls.
- `repro/claim2_exact.py` computes every `2^R` vote pattern for `R=3,5,8,12,16`, using group priors, annotator-specific likelihood weights, and the paper’s `posterior >= 1/2` tie rule.
- `repro/check_claim2.py` independently reads the exact CSV and proof certificate; it reports `PASS`, zero failures, five rows checked, and six proof steps checked.
- `repro/check_cumulative.py` independently checks C1–C5 from the released JSON artifacts.
- `repro/cumulative_controls.py` mutates each contract: too-small exponential rate, homogeneous equal skills, no-signal Bayes, zero influence constant, false random convergence, and unconstrained fairness post-processing. Each control fails as expected.
- `space_overlay/artifacts/` is the evaluator-visible raw evidence bundle. `reports/faircrowd/report.md` explains the heterogeneous C2 audit; `reports/faircrowd/release_report.md` records provenance, gates, and the publication forecast.

## Reproduce the release

```bash
uv sync --frozen
uv run --frozen python repro/run_all.py
```

Optional notebook workflow:

```bash
marimo edit notebooks/faircrowd_claim2.py
```

The release used the pinned `uv.lock`, Python 3.12.11, deterministic seeds `1, 2, 3, 5`, one CPU core, and no GPU. The exact C2 enumeration is finite and ends at `R=16` because it evaluates `2^R` patterns. The asymptotic conclusion relies on the audited mathematical chain from Theorem 3.1, Lemma 3.3, and dominated convergence; it is not presented as a Lean/Coq proof.

## Repository map

- `repro/` — canonical cumulative checks, exact C2 verifier, fairness controls, and shared model code.
- `reports/faircrowd/` — technical report, figures, release forecast, and limitation record.
- `notebooks/faircrowd_claim2.py` — self-contained interactive explanation of the exact heterogeneous audit.
- `space_overlay/` — additive evaluator-facing Space files, including the current verification page and raw artifacts.
- `release/` — upload allowlist, hashes, candidate-tree records, and blind-audit records.
- `.openresearch/artifacts/` — internal claim contracts, source audits, cumulative outputs, and execution metadata.
- `branch-audit.md` — purpose and migration map for every retained branch.

## Historical versus current evidence

The historical judged setup used homogeneous `p=0.75` skills and a prior of `0.5`, making Bayes effectively identical to Majority Vote. The current C2 audit uses heterogeneous group-dependent skill sequences, a nonzero target `ΔDP(Y)=0.2`, exact enumeration, and explicit controls. The old judged Space revision `eee6b5ec719b769b952bd978850bffba2ba590c3` remains preserved as a baseline record; current release artifacts are not silently substituted for that historical state.

The strongest remaining limitation is mathematical rather than computational: the symbolic audit checks the derivation graph and named inequalities, but does not constitute proof-assistant formalization. C5 also compares against a dense threshold grid rather than an exact linear-programming solver.

## Citation

```bibtex
@article{singer2026optimal,
  title         = {Optimal Fair Aggregation of Crowdsourced Noisy Labels using Demographic Parity Constraints},
  author        = {Singer, Gabriel and Gruffaz, Samuel and Vo Van, Olivier and Vayatis, Nicolas and Kalogeratos, Argyris},
  journal       = {arXiv preprint arXiv:2601.23221},
  year          = {2026},
  doi           = {10.48550/arXiv.2601.23221}
}
```

## Thank you

Thank you to Gabriel Singer, Samuel Gruffaz, Olivier Vo Van, Nicolas Vayatis, and Argyris Kalogeratos for making the fairness definitions, aggregation rules, convergence claims, and post-processing method available for independent examination. This repository is an independent reproduction and audit; it is not an official implementation or an endorsement by the authors.

## Attribution

The cleanup documentation and approved repository-history normalization are maintained under the **MachineLearning-Nerd** GitHub identity. Historical evidence contents, hashes, timestamps, and external Space identifiers are preserved wherever changing them would alter the audit record.
