# Full bundle Android validation

Candidate: `fantamk-6.1.0-candidate.1`

Controlled target:
- Package: `com.fantamk.patchtest`
- Version: `1.0.0`
- Source: FantaMK fixture app from the validated companion repository.

Patch under test:
- `Change package name`
- Universal patch from the full ReVanced 6.1.0 bundle.
- Default expected package: `com.fantamk.patchtest.revanced`.

PC reference result:
- Fixture build: PASS.
- ReVanced CLI 6 patch application: PASS without `--force`.
- Android SDK manifest verification: PASS.
- Original package: `com.fantamk.patchtest`.
- Patched package: `com.fantamk.patchtest.revanced`.

Android gate:
1. Import the 6.1.0 / 289-patch RVP in ReVanced Manager.
2. Select `fantamk-patch-test-app-debug.apk` from storage.
3. Select only `Change package name`.
4. Patch and install.
5. Launch the app and confirm it runs.
6. Record Android patch/install/runtime as PASS only after physical verification.
