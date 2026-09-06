from __future__ import annotations

import hashlib
import json
import sys
import urllib.request

API_URL = "https://api.revanced.app/v5/patches"
EXPECTED_VERSION = "v6.2.1"
EXPECTED_RVP_URL = "https://api.revanced.app/v5/patches.rvp"
EXPECTED_SIGNATURE_URL = "https://api.revanced.app/v5/patches.rvp.asc"
EXPECTED_RVP_SHA256 = "50F41E4656B7374A1C8FE5579FD107F697F86D7F13FC6CD194CF3821761DC4B4"


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "FantaMK-ReVanced-Maintenance/1"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "FantaMK-ReVanced-Maintenance/1"})
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()


def fail(message: str) -> None:
    print(f"OFFICIAL_API=FAIL: {message}")
    sys.exit(1)


def main() -> None:
    metadata = fetch_json(API_URL)
    if metadata.get("version") != EXPECTED_VERSION:
        fail(f"version changed: {metadata.get('version')} (expected {EXPECTED_VERSION})")
    if metadata.get("download_url") != EXPECTED_RVP_URL:
        fail("download_url changed")
    if metadata.get("signature_download_url") != EXPECTED_SIGNATURE_URL:
        fail("signature_download_url changed")

    rvp = fetch_bytes(EXPECTED_RVP_URL)
    digest = hashlib.sha256(rvp).hexdigest().upper()
    if digest != EXPECTED_RVP_SHA256:
        fail(f"RVP SHA-256 changed: {digest}")

    print("OFFICIAL_API=PASS")
    print(f"version={metadata['version']}")
    print(f"created_at={metadata.get('created_at')}")
    print(f"rvp_bytes={len(rvp)}")
    print(f"rvp_sha256={digest}")
    print(f"signature_url={metadata['signature_download_url']}")


if __name__ == "__main__":
    main()
