# Full bundle Android validation

Candidate target: `fantamk-6.2.1-candidate.1` (`6.2.1-fantamk.1`).
Previous validated LKG: `fantamk-6.1.0-lkg.1`.

Controlled target:
- Package: `com.fantamk.fullbundletest`
- Version: `1.0.0`
- Source: `.fantamk/fixtures/full-bundle-test-app`
- Runtime screen displays `getPackageName()` directly.

Patch under test:
- `Change package name`
- Universal patch from the full 6.2.1-equivalent bundle.
- Default expected package: `com.fantamk.fullbundletest.revanced`.

Reference PC result: PASS on final CI artifacts from run `34034682653`.
- RVP: 294 patches; ZIP integrity PASS; metadata exact-match with official v6.2.1.
- `Change package name`: PASS without `--force`.
- Manifest changed to `com.fantamk.fullbundletest.revanced`.

Reference method:
- Build the controlled fixture.
- Apply only `Change package name`.
- Do not use `--force`.
- Verify the output manifest package with Android SDK tools.
- Install only after PC/CI reference gates pass.

Expected runtime:
`com.fantamk.fullbundletest.revanced`

Android gate:
1. Import the private 6.2.1 candidate RVP in ReVanced Manager.
2. Select `fantamk-full-bundle-test-app-debug.apk`.
3. Select only `Change package name`.
4. Patch and install.
5. Launch `FantaMK Full Bundle Test`.
6. Confirm the runtime package equals the expected value above.

Candidate Android result: PENDING.
Do not promote over `fantamk-6.1.0-lkg.1` until this physical gate passes.
