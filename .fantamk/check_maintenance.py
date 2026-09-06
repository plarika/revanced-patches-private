from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_UPSTREAM = "https://gitlab.com/ReVanced/revanced-patches.git"
EXPECTED_BASE = "015fe10a23ea5b919a3fda6e7da2c176517ae75d"


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout.strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}")
        sys.exit(1)


required = [
    ROOT / ".fantamk" / "UPSTREAM_BASE.md",
    ROOT / ".fantamk" / "PROJECT_STATE.md",
    ROOT / ".fantamk" / "MAINTENANCE_POLICY.md",
    ROOT / ".fantamk" / "fixtures" / "full-bundle-test-app" / "settings.gradle.kts",
    ROOT / ".fantamk" / "fixtures" / "full-bundle-test-app" / "build.gradle.kts",
    ROOT / ".fantamk" / "fixtures" / "full-bundle-test-app" / "src" / "main" / "AndroidManifest.xml",
    ROOT / ".fantamk" / "fixtures" / "full-bundle-test-app" / "src" / "main" / "java" / "com" / "fantamk" / "fullbundletest" / "MainActivity.java",
]
for path in required:
    require(path.is_file(), f"missing {path.relative_to(ROOT)}")
origin_url = git("remote", "get-url", "origin")
require("plarika/revanced-patches-private" in origin_url, "unexpected private origin")

baseline_exists = subprocess.run(
    ["git", "cat-file", "-e", f"{EXPECTED_BASE}^{{commit}}"], cwd=ROOT
).returncode == 0
require(baseline_exists, "recorded upstream baseline commit is missing")

remotes = set(git("remote").splitlines())
ci = os.environ.get("GITHUB_ACTIONS") == "true"
upstream_head = "NOT_FETCHED"

if "upstream-patches" in remotes:
    upstream_url = git("remote", "get-url", "upstream-patches")
    require(upstream_url == EXPECTED_UPSTREAM, "unexpected upstream-patches fetch URL")
    push_url = git("remote", "get-url", "--push", "upstream-patches")
    require(push_url == "DISABLED", "upstream-patches push must be disabled")
    upstream_head = git("rev-parse", "upstream-patches/main")
else:
    require(ci, "upstream-patches remote is missing outside GitHub Actions")

branch = git("branch", "--show-current")
head = git("rev-parse", "HEAD")

print("FANTAMK_MAINTENANCE=PASS")
print(f"branch={branch}")
print(f"head={head}")
print(f"upstream_main={upstream_head}")
print(f"baseline={EXPECTED_BASE}")
if upstream_head == "NOT_FETCHED":
    print("state=CI_VALIDATED_PRIVATE_FORK")
elif head != upstream_head:
    print("state=FANTAMK_DIVERGED_FROM_UPSTREAM")
else:
    print("state=UPSTREAM_EXACT")
