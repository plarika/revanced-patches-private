# FantaMK private maintenance state

## CURRENT_PHASE

`6.2.1-fantamk.1` candidate preparation from the source-equivalent ReVanced 6.2.1 snapshot.

## VALIDATED LKG

- Full-repository LKG: `fantamk-6.1.0-lkg.1`.
- Validated source commit: `0d61e0ab3ac25414fe421b646eaae2157e423b73`.
- Android Manager import / patch / install / runtime: PASS.
- Recovery LKG: `plarika/fantamk-revanced-patches` tag `v0.2.0-dev.2`.

## 6.2.1 PROVENANCE

- Official API version: `v6.2.1`.
- Official patch count: `294`.
- Official RVP SHA-256: `50F41E4656B7374A1C8FE5579FD107F697F86D7F13FC6CD194CF3821761DC4B4`.
- Source snapshot: `09afcf3e44d6d8c98810b1cbf6f39477f9bcae66`.
- All 9 API changelog commits are ancestors of the source snapshot: PASS.
- Private source-equivalence CI run `34032039996`: PASS.
- Source-built patch count: `294`.
- Normalized patch-list SHA-256: `D209665F773EC912AD0E098DB1D02BBE442EBCB9EE743C162F765C283E2E8E41`.
- Exact patch-list equivalence with official RVP: PASS.

## CURRENT GATES

- Candidate version field `6.2.1-fantamk.1`: SET / local validation PASS.
- Official API/hash verifier: PASS against `v6.2.1` and the recorded RVP SHA-256.
- Unbranded candidate CI run `34034052448`: PASS.
- Private bundle identity (`FantaMK ReVanced Patches`): SET / final CI pending.
- Controlled PC patch test before private identity change: PASS; final branded RVP test pending.
- Android Manager import: PENDING.
- Android patch/install/runtime: PENDING.
- Signature verification: BLOCKED_BY_UPSTREAM_TLS while the official keys endpoint returns Cloudflare 526.

## BRANCH MODEL

- `main`: promoted LKG only.
- `dev`: validated maintenance.
- `maintenance/6.2.1-source`: isolated 6.2.1 candidate work.
- `upstream-patches`: fetch only; push disabled locally.
