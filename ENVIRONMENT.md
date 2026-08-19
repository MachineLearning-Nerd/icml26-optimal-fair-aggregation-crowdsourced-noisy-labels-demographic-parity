# Reproduction environment

## Fixed command

```bash
uv sync --frozen
uv run --frozen python repro/run_all.py
```

The collection-surface verifier is:

```bash
python3 verify_final.py
```

## Recorded run

- Python: `3.12.11`
- Platform: macOS arm64
- Seeds: `1, 2, 3, 5`
- Compute: one CPU core, no GPU
- Visible logical CPUs: `8`
- Scientific run SHA: `10451115e7ef0ba33a07b7b1ea20a5aaca959e8f`
- Recorded cumulative runtime: `41.007319` seconds
- Cumulative checker: `PASS`
- Controls: every deliberately broken control `FAIL_AS_EXPECTED`

The exact C2 enumeration is finite and ends at `R=16` because it evaluates
`2^R` patterns. The pinned `uv.lock`, upload allowlists, blind audits, and
raw artifacts are retained in the repository.
