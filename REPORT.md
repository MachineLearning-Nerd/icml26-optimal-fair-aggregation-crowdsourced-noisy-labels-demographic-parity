# Audit report

## Decision

The local release bundle verifies all five registered claim contracts, the
independent cumulative checker passes, and all deliberate controls fail as
expected:

```text
ALL_FIVE_CLAIM_CONTRACTS_VERIFIED_SCOPED_C2_ASYMPTOTIC_RECONSTRUCTED_C5_GRID_COMPARATOR
```

This is a scoped finite reproduction archive, not a proof-assistant
formalization, current judge score, or author endorsement:

```text
publication_allowed=false
score_claim=false
official_author_endorsement=false
```

## Boundaries

C1, C3, and C4 use finite or historical Monte Carlo evidence. C2 provides an
exact heterogeneous enumeration through `R=16` and a reconstructed asymptotic
derivation audit. C5 uses a dense threshold grid rather than an exact LP
solver. The previous live judged score was 9/10; the proposed 10/10 remains a
forecast and is not claimed as a result.
