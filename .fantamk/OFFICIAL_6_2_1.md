# Official ReVanced Patches 6.2.1 provenance

Authoritative metadata endpoint:
`https://api.revanced.app/v5/patches`

Observed on 2026-09-06:
- Version: `v6.2.1`
- Created at: `2026-06-02T18:30:00`
- RVP: `https://api.revanced.app/v5/patches.rvp`
- Signature: `https://api.revanced.app/v5/patches.rvp.asc`

Official RVP validation:
- Size: `5,697,683` bytes
- SHA-256: `50F41E4656B7374A1C8FE5579FD107F697F86D7F13FC6CD194CF3821761DC4B4`
- ZIP integrity: PASS
- ZIP entries: `1,821`
- ReVanced CLI 6 patch count: `294`

Official detached signature:
- Size: `588` bytes
- SHA-256: `F47593CD5C25512DC57657AC2CA15F47CC23F0532ED80F442250C6074EB97472`
- Signature verification: BLOCKED_BY_UPSTREAM_TLS (`https://api.revanced.app/keys` returned Cloudflare 526).

The API changelog links to concrete GitLab commits. Those commits remain retrievable even though tag `v6.2.1` is no longer advertised by the temporary GitLab mirror.
## Source equivalence

Recovered source snapshot: `09afcf3e44d6d8c98810b1cbf6f39477f9bcae66`.

Validation:
- All 9 commits referenced by the API changelog are ancestors of this snapshot: PASS.
- Private CI run `34032039996`: PASS.
- Source-built RVP patch count: `294`.
- Source-built ZIP entries: `1,821`.
- Normalized patch-list SHA-256: `D209665F773EC912AD0E098DB1D02BBE442EBCB9EE743C162F765C283E2E8E41`.
- Official RVP normalized patch-list SHA-256: same value.
- Patch-list exact match: PASS.

FantaMK candidate version is deliberately changed to `6.2.1-fantamk.1` so the private build is distinguishable in ReVanced Manager.

## Private candidate identity

The FantaMK candidate intentionally changes only project/distribution metadata outside patch implementation code:
- Version: `6.2.1-fantamk.1`.
- Bundle name: `FantaMK ReVanced Patches`.
- Source/website: private repository `plarika/revanced-patches-private`.
- Author field: `ReVanced / FantaMK` to preserve upstream attribution and identify private maintenance.
- GitHub Packages publishing target: the private repository.

No files under patch implementation or extension source trees are changed by this identity step.
