# FantaMK private maintenance state

## CURRENT_PHASE

`V0.1-private-baseline` - complete ReVanced Patches snapshot under private maintenance.

Validation status:
- Linux/JDK 17 full RVP build: PASS (GitHub Actions run 34029292582 for Candidate 2).
- Candidate 2 RVP integrity: PASS; 5,648,273 bytes; 289 patches; SHA-256 `6352FC96358DCF955962CE4A3422016E0346AE068A68B297172E31055FAD68C0`.
- Android ReVanced Manager local import: PASS on 2026-09-06; displayed `ReVanced Patches 6.1.0 - 289 patches`.
- Application-level patching with the full bundle: PASS on PC using the controlled runtime fixture and `Change package name`, without `--force`.
- Physical Android patch/install/runtime validation: PASS on 2026-09-06; installed app displayed runtime package `com.fantamk.fullbundletest.revanced`.
- Promoted code LKG: `fantamk-6.1.0-lkg.1` -> `0d61e0ab3ac25414fe421b646eaae2157e423b73`.
- Manager official source observed alongside it: `ReVanced Patches v6.2.1 (Jun 02) - 294 patches`; upstream refresh remains pending.

## LAST_KNOWN_GOOD

Current full-repository LKG: `fantamk-6.1.0-lkg.1` at commit `0d61e0ab3ac25414fe421b646eaae2157e423b73`.

Previous recovery LKG remains available in the separate repository `plarika/fantamk-revanced-patches` at tag `v0.2.0-dev.2`.

## PRIVATE_REPOSITORY

`plarika/revanced-patches-private`

## BRANCH_MODEL
- `main`: promoted/private baseline only.
- `dev`: maintenance and validation.
- feature/maintenance branches: isolated changes before `dev`.

## UPSTREAM

`upstream-patches` fetches from the official temporary GitLab mirror. Push is disabled locally.
