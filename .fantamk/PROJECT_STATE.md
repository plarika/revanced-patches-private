# FantaMK private maintenance state

## CURRENT_PHASE

`V0.1-private-baseline` - complete ReVanced Patches snapshot under private maintenance.

Validation status:
- Linux/JDK 17 full RVP build: PASS (GitHub Actions run 34027071494).
- RVP integrity: PASS; 5,648,269 bytes; 289 patches; SHA-256 `2525DA5EC347FA9C8C27052F3155BFE0CAB351BB26572CB77CD4BF3454B0F6E1`.
- Android ReVanced Manager local import: PASS on 2026-09-06; displayed `ReVanced Patches 6.1.0 - 289 patches`.
- Application-level patching with this full bundle: NOT_EXECUTED.
- Manager official source observed alongside it: `ReVanced Patches v6.2.1 (Jun 02) - 294 patches`; upstream refresh is therefore pending.

## LAST_KNOWN_GOOD

The validated Android LKG remains in the separate repository `plarika/fantamk-revanced-patches` at tag `v0.2.0-dev.2`.

This full repository is not promoted as a replacement until its own RVP build and ReVanced Manager tests pass.

## PRIVATE_REPOSITORY

`plarika/revanced-patches-private`

## BRANCH_MODEL

- `main`: promoted/private baseline only.
- `dev`: maintenance and validation.
- feature/maintenance branches: isolated changes before `dev`.

## UPSTREAM

`upstream-patches` fetches from the official temporary GitLab mirror. Push is disabled locally.