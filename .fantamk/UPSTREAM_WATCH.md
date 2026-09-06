# FantaMK upstream update watcher

The private repository checks the official ReVanced Patches API every six hours.
The watcher is detection-only and never updates patch sources, tags, releases, `main`, `dev`, or the LKG automatically.

Baseline:
- Official version: `v6.2.1`
- Official patch count: `294`
- Private LKG: `fantamk-6.2.1-lkg.1`
- Baseline data: `.fantamk/upstream_baseline.json`

Statuses:
- `current`: official version and RVP SHA-256 match the recorded baseline.
- `update_available`: the official version changed; a private GitHub issue is created or updated.
- `same_version_hash_changed`: the version did not change but the RVP hash did; an issue is created and the workflow fails.
- `upstream_unavailable`: transient HTTP 5xx/526 or network failure; report only, no repository mutation.

A detected update must still pass the normal FantaMK maintenance pipeline before promotion.
