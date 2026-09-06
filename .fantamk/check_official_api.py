from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request

API_URL = "https://api.revanced.app/v5/patches"
EXPECTED_VERSION = "v6.2.1"
EXPECTED_RVP_URL = "https://api.revanced.app/v5/patches.rvp"
EXPECTED_SIGNATURE_URL = "https://api.revanced.app/v5/patches.rvp.asc"
EXPECTED_RVP_SHA256 = "50F41E4656B7374A1C8FE5579FD107F697F86D7F13FC6CD194CF3821761DC4B4"


def request(url: str, timeout: int):
    req = urllib.request.Request(url, headers={"User-Agent": "FantaMK-ReVanced-Maintenance/1"})
    return urllib.request.urlopen(req, timeout=timeout)


def fail(message: str) -> None:
    print(f"OFFICIAL_API=FAIL: {message}")
    sys.exit(1)


def unavailable(exc: BaseException, allow: bool) -> None:
    if not allow:
        raise exc
    print("OFFICIAL_API=BLOCKED_BY_UPSTREAM_TLS")
    print(f"reason={type(exc).__name__}: {exc}")
    print(f"pinned_version={EXPECTED_VERSION}")
    print(f"pinned_rvp_sha256={EXPECTED_RVP_SHA256}")
    sys.exit(0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-unavailable", action="store_true")
    args = parser.parse_args()
    try:
        with request(API_URL, 30) as response:
            metadata = json.load(response)
        if metadata.get("version") != EXPECTED_VERSION:
            fail(f"version changed: {metadata.get('version')} (expected {EXPECTED_VERSION})")
        if metadata.get("download_url") != EXPECTED_RVP_URL:
            fail("download_url changed")
        if metadata.get("signature_download_url") != EXPECTED_SIGNATURE_URL:
            fail("signature_download_url changed")
        with request(EXPECTED_RVP_URL, 60) as response:
            rvp = response.read()
    except urllib.error.HTTPError as exc:
        if exc.code >= 500:
            unavailable(exc, args.allow_unavailable)
        raise
    except (urllib.error.URLError, TimeoutError) as exc:
        unavailable(exc, args.allow_unavailable)

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
