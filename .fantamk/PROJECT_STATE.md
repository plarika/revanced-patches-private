# FantaMK private maintenance state

## CURRENT_PHASE

`6.2.1-fantamk.1` - Android-validated private maintenance release.

## LAST_KNOWN_GOOD

- Current full-repository LKG: `fantamk-6.2.1-lkg.1`.
- Validated source/artifact commit: `8b6bae8048a28f507b9cd9e6f53f038e54a4d6eb`.
- Candidate tag used for the physical test: `fantamk-6.2.1-candidate.1`.
- Android Manager import / patch / install / runtime: PASS on 2026-09-06.
- Runtime package observed: `com.fantamk.fullbundletest.revanced`.
- Previous full-repository recovery LKG: `fantamk-6.1.0-lkg.1`.
- Separate recovery repository remains `plarika/fantamk-revanced-patches` tag `v0.2.0-dev.2`.

## 6.2.1 PROVENANCE

- Official API version: `v6.2.1`.
- Official patch count: `294`.
- Official RVP SHA-256: `50F41E4656B7374A1C8FE5579FD107F697F86D7F13FC6CD194CF3821761DC4B4`.
- Source snapshot: `09afcf3e44d6d8c98810b1cbf6f39477f9bcae66`.
- All 9 API changelog commits are ancestors of the source snapshot: PASS.
- Exact normalized patch metadata equivalence with the official RVP: PASS.

## VALIDATION GATES

- Official API/hash verifier: PASS.
- Final private CI run `34034682653`: PASS.
- Final branded bundle identity: PASS (`FantaMK ReVanced Patches`, `6.2.1-fantamk.1`).
- RVP ZIP integrity: PASS; `294` patches; `1,821` entries.
- Candidate RVP SHA-256: `D12097EB14E18495C50EBFB607750F031957441C8E2E9B55EFC041310652B7BA`.
- Controlled PC patch test: PASS without `--force`.
- Android Manager import: PASS.
- Android patch/install/runtime: PASS.
- Signature verification of the official detached signature remains `BLOCKED_BY_UPSTREAM_TLS` while the official keys endpoint returns Cloudflare 526.

## UPSTREAM WATCH

- Automatic detection workflow: `.github/workflows/watch_upstream.yml`.
- Schedule: every 6 hours at minute 17 UTC, plus manual dispatch.
- Baseline: `.fantamk/upstream_baseline.json`.
- Current baseline status: `v6.2.1` / `fantamk-6.2.1-lkg.1`.
- Update detection creates or updates a private GitHub issue; it never updates patch sources, releases, tags, `main`, `dev`, or the LKG automatically.
- Same-version RVP hash changes are treated as integrity anomalies and fail the watcher.
- Transient upstream 5xx/526/network failures are reported without mutating the repository.
- Full repository validation for watcher integration: PASS (run 34038458276).
- Manual watcher validation on main: PASS (run 34038934705, status CURRENT).
- Open upstream maintenance issues after current-baseline test: 0.

## BRANCH MODEL

- `main`: promoted LKG only.
- `dev`: validated maintenance.
- `maintenance/6.2.1-source`: provenance and candidate history.
- `maintenance/upstream-watch`: watcher integration history.
- `upstream-patches`: fetch only; push disabled locally.
