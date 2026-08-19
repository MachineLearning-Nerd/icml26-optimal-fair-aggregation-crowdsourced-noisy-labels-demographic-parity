# Status

- **Collection status:** `ALL_FIVE_CLAIM_CONTRACTS_VERIFIED_SCOPED_C2_ASYMPTOTIC_RECONSTRUCTED_C5_GRID_COMPARATOR`
- **Paper:** *Optimal Fair Aggregation of Crowdsourced Noisy Labels using Demographic Parity Constraints*.
- **Authors:** Gabriel Singer, Samuel Gruffaz, Olivier Vo Van, Nicolas Vayatis, and Argyris Kalogeratos.
- **Claims:** C1–C5 pass the registered contracts; C2 is finite through `R=16` with a reconstructed asymptotic derivation, and C5 uses a threshold grid comparator.
- **Cumulative checker:** `PASS`; all deliberate controls fail as expected.
- **Historical judge:** 9/10 at the preserved baseline; no current score claim. The possible 10/10 is forecast only.
- **Publication flags:** `publication_allowed=false`, `score_claim=false`, `official_author_endorsement=false`.
- **Audit author:** `MachineLearning-Nerd`.

The detailed production paths are in [`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md),
and the public six-branch state is checked by [`verify_final.py`](verify_final.py).
