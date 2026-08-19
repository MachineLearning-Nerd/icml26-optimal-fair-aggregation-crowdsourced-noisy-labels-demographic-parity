#!/usr/bin/env python3
"""Verify the published FairCrowd audit surface, branches, and claim boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPOSITORY = "MachineLearning-Nerd/icml26-optimal-fair-aggregation-crowdsourced-noisy-labels-demographic-parity"
EXPECTED_URL = f"https://github.com/{REPOSITORY}"
EXPECTED_IDENTITY = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
OVERALL = "ALL_FIVE_CLAIM_CONTRACTS_VERIFIED_SCOPED_C2_ASYMPTOTIC_RECONSTRUCTED_C5_GRID_COMPARATOR"
BOUNDARY = "C1_C3_C4_HISTORICAL_MONTE_CARLO_C2_FINITE_R16_AND_RECONSTRUCTED_LIMIT_C5_GRID_NOT_EXACT_LP_NO_PROOF_ASSISTANT"
EXPECTED_BRANCHES = {
    "main",
    "audit/exact-heterogeneous-bayes",
    "audit/judged-monte-carlo-baseline",
    "audit/release-manifest-blind-audit",
    "release/evaluator-visible-candidate",
    "release/publication-surface",
}
CLAIM_STATUSES = {
    "C1": "verified_scoped_historical_monte_carlo",
    "C2": "verified_scoped_finite_r16_asymptotic_reconstruction",
    "C3": "verified_scoped_finite_fairness_bound",
    "C4": "verified_scoped_sufficient_condition",
    "C5": "verified_scoped_grid_comparator",
}


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def fail(message: str) -> None:
    print(f"FINAL_AUDIT=FAILED reason={message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: str) -> dict | list:
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid_json_{path.replace('/', '_')}_{type(exc).__name__}")
        raise AssertionError


def ref_for_branch(branch: str) -> str:
    for ref in (f"refs/heads/{branch}", f"refs/remotes/origin/{branch}"):
        result = subprocess.run(["git", "show-ref", "--verify", "--quiet", ref], cwd=ROOT)
        if result.returncode == 0:
            return ref
    fail(f"missing_branch_ref_{branch.replace('/', '_')}")
    raise AssertionError


def main() -> None:
    output = git("ls-remote", "--heads", "origin")
    remote_map = {
        line.split("\t", 1)[1].removeprefix("refs/heads/"): line.split("\t", 1)[0]
        for line in output.splitlines()
        if line.strip()
    }
    if set(remote_map) != EXPECTED_BRANCHES:
        fail(f"remote_branches_expected_6_observed_{len(remote_map)}")
    local = set(git("for-each-ref", "--format=%(refname:strip=2)", "refs/heads").splitlines())
    if local - EXPECTED_BRANCHES or "main" not in local:
        fail("local_branch_refs_are_not_a_subset_with_main")
    for branch, remote_sha in remote_map.items():
        if git("rev-parse", ref_for_branch(branch)) != remote_sha:
            fail(f"remote_tip_mismatch_{branch.replace('/', '_')}")
    if "refs/heads/main\tHEAD" not in git("ls-remote", "--symref", "origin", "HEAD"):
        fail("remote_default_branch_is_not_main")
    if git("remote", "get-url", "origin").removesuffix(".git") != EXPECTED_URL:
        fail("origin_url_mismatch")
    if git("status", "--porcelain"):
        fail("working_tree_not_clean")
    if git("for-each-ref", "--format=%(refname)", "refs/original"):
        fail("rewrite_backup_refs_present")

    identities = set(git("log", "--all", "--format=%an <%ae> | %cn <%ce>").splitlines())
    if identities != {EXPECTED_IDENTITY + " | " + EXPECTED_IDENTITY}:
        fail("non_canonical_commit_identity_present")
    if "Co-authored-by:" in git("log", "--all", "--format=%B"):
        fail("coauthor_trailer_present")
    commit_count = int(git("rev-list", "--all", "--count"))

    required = [
        "README.md",
        "branch-audit.md",
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "CITATION.cff",
        "AUTHOR_THANK_YOU.md",
        "STATUS.md",
        "claims.json",
        "reproduction_verdicts.json",
        "AUTONOMOUS_STATE.json",
        "EVIDENCE_MANIFEST.json",
        "verify_final.py",
        "space_overlay/artifacts/cumulative_results.json",
        "space_overlay/artifacts/cumulative_controls.json",
        "space_overlay/artifacts/claim2_checker.json",
        "space_overlay/pages/current-verification/page.md",
        "repro/run_all.py",
        "repro/check_cumulative.py",
        "repro/cumulative_controls.py",
        "release/blind-audit-round1.json",
        "release/blind-audit-round2.json",
    ]
    for path in required:
        if not (ROOT / path).is_file():
            fail(f"missing_required_file_{path.replace('/', '_')}")

    state = load_json("AUTONOMOUS_STATE.json")
    assert isinstance(state, dict)
    if state["repository"] != REPOSITORY or state["branch_layout"]["expected_count"] != 6:
        fail("autonomous_state_repository_or_branch_count_mismatch")
    if set(state["branch_layout"]["branches"]) != EXPECTED_BRANCHES:
        fail("autonomous_state_branch_list_mismatch")
    if state["audit"]["overall_verdict"] != OVERALL or state["audit"]["publication_boundary"] != BOUNDARY:
        fail("autonomous_state_boundary_mismatch")
    if state["audit"]["publication_allowed"] or state["audit"]["score_claim"] or state["audit"]["official_author_endorsement"]:
        fail("autonomous_state_publication_flags_must_be_false")
    if state["history"]["expected_reachable_commits"] != commit_count:
        fail("autonomous_state_commit_count_mismatch")
    if state["history"]["published_main_parent"] != git("rev-parse", "main^"):
        fail("autonomous_state_main_parent_mismatch")
    if state["attribution"]["canonical_identity"] != EXPECTED_IDENTITY:
        fail("autonomous_state_attribution_mismatch")

    claims = load_json("claims.json")
    assert isinstance(claims, dict)
    if claims["overall_verdict"] != OVERALL or claims["publication_boundary"] != BOUNDARY:
        fail("machine_readable_claim_boundary_mismatch")
    if claims["publication_allowed"] or claims["score_claim"] or claims["official_author_endorsement"]:
        fail("machine_readable_publication_flags_must_be_false")
    if {item["id"]: item["status"] for item in claims["claims"]} != CLAIM_STATUSES:
        fail("machine_readable_claim_status_mismatch")

    verdicts = load_json("reproduction_verdicts.json")
    assert isinstance(verdicts, dict)
    if verdicts["overall_verdict"] != OVERALL or verdicts["publication_boundary"] != BOUNDARY:
        fail("machine_readable_verdict_boundary_mismatch")
    if {key: value["status"] for key, value in verdicts["claims"].items()} != CLAIM_STATUSES:
        fail("machine_readable_verdict_status_mismatch")
    historical = verdicts["historical_judge"]
    if historical["points"] != 9 or historical["total"] != 10 or not historical["current_score_not_claimed"]:
        fail("historical_score_boundary_mismatch")
    if verdicts["upstream"]["cumulative_verdict"] != "PASS" or verdicts["upstream"]["controls_verdict"] != "FAIL_AS_EXPECTED":
        fail("upstream_verdict_boundary_mismatch")

    cumulative = load_json("space_overlay/artifacts/cumulative_results.json")
    if not cumulative["all_regressions_pass"] or not cumulative["claim_2_verified"] or {item["status"] for item in cumulative["claims"]} != {"VERIFIED"}:
        fail("cumulative_claim_gate_failed")
    controls = load_json("space_overlay/artifacts/cumulative_controls.json")
    if controls["status"] != "FAIL_AS_EXPECTED" or not all(item["failed_as_expected"] for item in controls["controls"].values() if "failed_as_expected" in item):
        fail("control_gate_failed")
    checker = load_json("space_overlay/artifacts/claim2_checker.json")
    if checker["status"] != "PASS" or checker["failures"]:
        fail("claim2_checker_failed")
    page = (ROOT / "space_overlay/pages/current-verification/page.md").read_text(encoding="utf-8")
    if "f6a147f01856d20e54047311773d98e90123be014ee8372b2fdac3c9f9c44835" not in page:
        fail("source_hash_record_missing")

    manifest = load_json("EVIDENCE_MANIFEST.json")
    if manifest["repository"] != REPOSITORY or manifest["overall_verdict"] != OVERALL:
        fail("evidence_manifest_header_mismatch")

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(remote_map)} commits={commit_count} claims=C1:C5_verified "
        "cumulative=PASS controls=FAIL_AS_EXPECTED historical_score=9/10 "
        "current_score_claim=false publication_allowed=false"
    )


if __name__ == "__main__":
    main()
