# Claim evidence ledger

This ledger records how the five paper claims are produced, checked, and
bounded. The original contracts and raw evidence remain under
`space_overlay/artifacts/` and `repro/`; the current public status is also
machine-readable in `claims.json`.

Overall status: `ALL_FIVE_CLAIM_CONTRACTS_VERIFIED_SCOPED_C2_ASYMPTOTIC_RECONSTRUCTED_C5_GRID_COMPARATOR`.

Publication boundary:
`C1_C3_C4_HISTORICAL_MONTE_CARLO_C2_FINITE_R16_AND_RECONSTRUCTED_LIMIT_C5_GRID_NOT_EXACT_LP_NO_PROOF_ASSISTANT`.

| Claim | Paper anchor | Producer and primary evidence | Independent checks and controls | Scoped result and boundary |
| --- | --- | --- | --- | --- |
| C1 | Proposition 3.2 | `repro/run_all.py`; cumulative regression in `space_overlay/artifacts/cumulative_results.json` | Error/DP-gap trajectories, exponential-rate mutation, deterministic seeds | `VERIFIED_SCOPED`; tail is Monte Carlo sampling-noise limited. |
| C2 | Theorem 3.4 | `repro/claim2_exact.py`; `space_overlay/artifacts/claim2_exact.json`, `.csv`, and checker | Exhaustive `2^R` vote patterns through `R=16`, heterogeneous skills, Conditions 8–9, six proof steps, homogeneous/no-signal controls | `VERIFIED_SCOPED_ASYMPTOTIC_RECONSTRUCTED`; finite enumeration does not prove the limit, and the dominated-convergence chain is not proof-assistant formalized. |
| C3 | Proposition 3.6 | `repro/check_cumulative.py`; cumulative result artifact | Four observed/bound rows at `R=6,10,20,40`, zero-influence mutation | `VERIFIED_SCOPED`; historical Monte Carlo regression. |
| C4 | Condition 8 and Lemma 3.3 | `repro/cumulative_controls.py`; cumulative result artifact | Competent/weak-competent convergence and random/adversarial non-convergence controls | `VERIFIED_SCOPED_SUFFICIENT_CONDITION`; this does not claim the condition is necessary. |
| C5 | Theorem 4.1 | Cumulative checker and `space_overlay/artifacts/cumulative_results.json` | Four epsilon values, DP tolerance, accuracy gap against exhaustive `121×121` threshold grid, unconstrained-control mutation | `VERIFIED_SCOPED_GRID_COMPARATOR`; the comparator is not an exact LP solver. |

The evidence path is:

```text
paper anchor → contract → deterministic producer → raw artifact
             → independent checker → negative control → scoped verdict
```

The historical 9/10 score and the possible 10/10 forecast are separate
publication records; the forecast is never used as a current score claim.
