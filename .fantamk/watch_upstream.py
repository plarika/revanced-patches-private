from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

API_URL = "https://api.revanced.app/v5/patches"
BASELINE_PATH = Path(__file__).with_name("upstream_baseline.json")
USER_AGENT = "FantaMK-ReVanced-Upstream-Watch/1"


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()


def load_baseline() -> dict:
    return json.loads(BASELINE_PATH.read_text(encoding="utf-8"))


def emit_outputs(values: dict[str, str], output_path: str | None) -> None:
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as handle:
        for key, value in values.items():
            safe = str(value).replace("\n", " ").replace("\r", " ")
            handle.write(f"{key}={safe}\n")


def write_report(path: str | None, lines: list[str]) -> None:
    text = "\n".join(lines) + "\n"
    if path:
        Path(path).write_text(text, encoding="utf-8")
    print(text, end="")


def is_transient(exc: BaseException) -> bool:
    if isinstance(exc, urllib.error.HTTPError):
        return 500 <= exc.code <= 599
    return isinstance(exc, urllib.error.URLError)


def require_metadata(metadata: dict) -> None:
    for key in ("version", "created_at", "download_url", "signature_download_url"):
        if not metadata.get(key):
            raise ValueError(f"official API response missing {key}")


def evaluate(metadata: dict, rvp: bytes, baseline: dict) -> tuple[str, dict[str, str]]:
    digest = hashlib.sha256(rvp).hexdigest().upper()
    current_version = str(metadata["version"])
    baseline_version = str(baseline["official_version"])
    baseline_digest = str(baseline["official_rvp_sha256"]).upper()

    if current_version == baseline_version and digest != baseline_digest:
        status = "same_version_hash_changed"
    elif current_version != baseline_version:
        status = "update_available"
    else:
        status = "current"

    values = {
        "status": status,
        "version": current_version,
        "created_at": str(metadata["created_at"]),
        "rvp_sha256": digest,
        "download_url": str(metadata["download_url"]),
        "signature_url": str(metadata["signature_download_url"]),
        "baseline_version": baseline_version,
        "baseline_sha256": baseline_digest,
        "lkg_tag": str(baseline["lkg_tag"]),
    }
    return status, values


def make_report(values: dict[str, str]) -> list[str]:
    status = values["status"]
    title = {
        "current": "No upstream update detected",
        "update_available": "Upstream ReVanced Patches update detected",
        "same_version_hash_changed": "Upstream integrity anomaly detected",
        "upstream_unavailable": "Upstream temporarily unavailable",
    }[status]
    return [
        f"# {title}",
        "",
        f"- Status: `{status}`",
        f"- Current LKG: `{values['lkg_tag']}`",
        f"- Baseline official version: `{values['baseline_version']}`",
        f"- Observed official version: `{values.get('version', 'unavailable')}`",
        f"- Created at: `{values.get('created_at', 'unavailable')}`",
        f"- Observed RVP SHA-256: `{values.get('rvp_sha256', 'unavailable')}`",
        f"- Baseline RVP SHA-256: `{values['baseline_sha256']}`",
        "",
        "No patch source, release, tag, main branch, or LKG is modified by this watcher.",
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-unavailable", action="store_true")
    parser.add_argument("--report")
    parser.add_argument("--github-output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    baseline = load_baseline()
    try:
        metadata = fetch_json(API_URL)
        require_metadata(metadata)
        rvp = fetch_bytes(str(metadata["download_url"]))
        _, values = evaluate(metadata, rvp, baseline)
    except Exception as exc:
        if args.allow_unavailable and is_transient(exc):
            values = {
                "status": "upstream_unavailable",
                "version": "unavailable",
                "created_at": "unavailable",
                "rvp_sha256": "unavailable",
                "download_url": "unavailable",
                "signature_url": "unavailable",
                "baseline_version": str(baseline["official_version"]),
                "baseline_sha256": str(baseline["official_rvp_sha256"]).upper(),
                "lkg_tag": str(baseline["lkg_tag"]),
            }
            print(f"UPSTREAM_WATCH_WARNING={type(exc).__name__}: {exc}")
        else:
            raise

    emit_outputs(values, args.github_output)
    write_report(args.report, make_report(values))
    print(f"UPSTREAM_WATCH={values['status'].upper()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
