# FantaMK private maintenance state

## CURRENT_PHASE

`maintenance/6.2.1-source` - source-equivalence validation against the official ReVanced Patches 6.2.1 artifact.

## VALIDATED LKG

- Full-repository LKG: `fantamk-6.1.0-lkg.1`
- Validated source commit: `0d61e0ab3ac25414fe421b646eaae2157e423b73`
- Android Manager import / patch / install / runtime: PASS.
- Recovery LKG remains `plarika/fantamk-revanced-patches` tag `v0.2.0-dev.2`.

## 6.2.1 TARGET

- Official API version: `v6.2.1`
- Official patch count: `294`
- Official RVP SHA-256: `50F41E4656B7374A1C8FE5579FD107F697F86D7F13FC6CD194CF3821761DC4B4`
- Source snapshot under validation: `09afcf3e44d6d8c98810b1cbf6f39477f9bcae66`
- Source snapshot version field remains `6.1.1-dev.4` during equivalence testing.
- Signature verification: BLOCKED_BY_UPSTREAM_TLS until the official keys endpoint is available.

## GATES

- Official API metadata: PASS.
- Official RVP download/integrity: PASS.
- Official CLI patch count = 294: PASS.
- Source snapshot build in private CI: PENDING.
- Patch-list equivalence with official RVP: PENDING.
- Android Manager candidate validation: PENDING.