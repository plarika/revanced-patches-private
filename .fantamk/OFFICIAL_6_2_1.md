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