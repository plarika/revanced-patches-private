# Full bundle Android validation

Candidate target: `fantamk-6.1.0-candidate.2`
Promoted code LKG: `fantamk-6.1.0-lkg.1`

Controlled target:
- Package: `com.fantamk.fullbundletest`
- Version: `1.0.0`
- Source: `.fantamk/fixtures/full-bundle-test-app`
- Runtime screen displays `getPackageName()` directly.

Patch under test:
- `Change package name`
- Universal patch from the full ReVanced 6.1.0 bundle.
- Default expected package: `com.fantamk.fullbundletest.revanced`.

PC reference result:
- Fixture build: PASS.
- ReVanced CLI 6 patch application: PASS without `--force`.
- Android SDK manifest verification: PASS.
- Original package: `com.fantamk.fullbundletest`.
- Patched package: `com.fantamk.fullbundletest.revanced`.

Android gate:
1. Import the Candidate 2 RVP in ReVanced Manager.
2. Select `fantamk-full-bundle-test-app-debug.apk` from storage.
3. Select only `Change package name`.
4. Patch and install.
5. Launch `FantaMK Full Bundle Test`.
6. Confirm `Runtime package:` shows `com.fantamk.fullbundletest.revanced`.

Physical Android result on 2026-09-06: **PASS**.
The installed app displayed runtime package `com.fantamk.fullbundletest.revanced`.
