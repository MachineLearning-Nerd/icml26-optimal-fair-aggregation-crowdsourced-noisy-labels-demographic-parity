# Branch audit

The old `orx/` prefix identified evidence-development stages. All live branches are retained and renamed by purpose; `main` remains the aggregate publication branch.

| Clean branch | Previous branch | Evidence or purpose |
| --- | --- | --- |
| `main` | `main` | Aggregate release and current publication surface: README, report, Space overlay, manifests, exact C2 evidence, cumulative checker, and controls. |
| `audit/judged-monte-carlo-baseline` | `orx/judged-monte-carlo-baseline` | Freezes the historical judged evidence and the original C2 criticism: homogeneous skills made Bayes indistinguishable from Majority Vote. |
| `audit/exact-heterogeneous-bayes` | `orx/exact-heterogeneous-bayes-verifier` | Adds heterogeneous group-dependent skills, exact pattern enumeration, condition audits, and the reconstructed Theorem-3.4 derivation check. |
| `release/evaluator-visible-candidate` | `orx/evaluator-visible-release-candidate` | Packages the independent cumulative checker, claim controls, technical report, and notebook for evaluator visibility. |
| `audit/release-manifest-blind-audit` | `orx/release-manifest-and-blind-audit` | Seals manifests, upload allowlists, hash records, and two evaluator-blind traversal audits. |
| `release/publication-surface` | `orx/publication-surface` | Final publication-provenance pointer; it shares the pre-cleanup aggregate tip with `main` and is retained as a distinct release reference. |

## Branch guarantees

- No evidence-development branch was discarded during cleanup.
- The live GitHub repository uses only the clean names above; no `orx/*` or `master` branch remains.
- `main` is the default branch and contains the human-readable README and this audit.
- All reachable commit authors and committers are normalized to `MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>`; scientific artifact contents and historical identifiers remain unchanged.
