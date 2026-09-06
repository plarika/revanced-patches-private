# FantaMK maintenance policy

The private fork follows a conservative update path.

1. Fetch upstream into `upstream-patches`.
2. Never push to the upstream remote.
3. Review upstream changes before integration.
4. Merge/update only on `dev` or a maintenance branch.
5. Build the complete Android RVP.
6. Run CI on Linux/JDK 17.
7. Import the candidate RVP into ReVanced Manager.
8. Test representative patches before promotion.
9. Promote to `main` only after the gate is complete.

## Upstream rule

Do not automatically overwrite FantaMK changes with upstream changes. Resolve conflicts deliberately and preserve provenance.

## Release rule

Automatic semantic release, GPG signing, Crowdin pushes and scheduled dependency mutation are disabled until explicitly configured for this private fork.

## Existing FantaMK integration

The separate validated fixture repository remains the regression harness for the Manager/Patcher pipeline. This full repository supplies the maintained real patch collection.