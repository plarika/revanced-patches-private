# Full bundle Android validation

Validated candidate: `fantamk-6.2.1-candidate.1` (`6.2.1-fantamk.1`).
Promoted LKG tag: `fantamk-6.2.1-lkg.1`.
Previous LKG: `fantamk-6.1.0-lkg.1`.

Controlled target:
- Package: `com.fantamk.fullbundletest`
- Version: `1.0.0`
- Source: `.fantamk/fixtures/full-bundle-test-app`
- Runtime screen displays `getPackageName()` directly.

Patch under test:
- `Change package name`
- Universal patch from the full 6.2.1-equivalent bundle.
- Expected package: `com.fantamk.fullbundletest.revanced`.

Reference PC result: PASS on final CI artifacts from run `34034682653`.
- RVP: 294 patches; ZIP integrity PASS; metadata exact-match with official v6.2.1.
- `Change package name`: PASS without `--force`.
- Manifest changed to `com.fantamk.fullbundletest.revanced`.

## Physical Android result

Physical validation on 2026-09-06: **PASS**.

Observed on the installed app:
- Runtime package: `com.fantamk.fullbundletest.revanced`.
- Original package shown by the fixture: `com.fantamk.fullbundletest`.
- Patched package shown by the fixture: `com.fantamk.fullbundletest.revanced`.
- Version: `1.0.0`.

Closed gates:
- Android Manager import: PASS.
- Android patch application: PASS.
- Android installation: PASS.
- Android runtime verification: PASS.

The candidate is eligible for LKG promotion. The LKG artifact remains the exact Candidate 1 RVP built from commit `8b6bae8048a28f507b9cd9e6f53f038e54a4d6eb`.
