S7NS-P0-RFC-001

Implementation-Ready Engineering Contract & Acceptance Matrix

Document type: Production Engineering Contract
Phase: Phase 0, Export Verification and Strict Lossless Reconstruction
Status: PROPOSED ACCEPTANCE STANDARD
Implementation acceptance: NOT GRANTED
Source modifications: NOT AUTHORIZED
Scope: Exporter, verifier, compliance suite, and export package

⸻

1. Purpose

This contract establishes the formal acceptance requirements for the S7NS Phase 0 export and reconstruction system.

The system must establish four distinct properties:

1. Inventory presence: Every relevant source entry is accounted for.
2. Local availability: The system distinguishes locally available content from unavailable external dependencies.
3. Export completion: Every exportable payload is assigned to a package and reconstructed.
4. Integrity verification: Reconstructed bytes, package assignments, checksums, and reconciliation ledgers agree exactly.

A source being present in an inventory does not establish that its contents are locally available.

A source being locally available does not establish that it was successfully exported.

An export being completed does not establish that its reconstructed contents are byte-exact.

These conditions must remain independently verifiable.

2. Authority and implementation boundaries

The supplied exporter, verifier, and compliance suite are implementation evidence. They are not, by themselves, proof of compliance.

The normative RFC text must control wherever it specifies behavior not established by the supplied scripts.

This contract does not authorize:

* Changing source files.
* Rewriting the exporter or verifier.
* Modifying the existing test suite.
* Changing the archive format.
* Reclassifying intentional exclusions.
* Treating unresolved dependencies as successful exports.
* Treating a test-suite pass as production certification.

Any behavior not established by the available source material must be recorded as an unresolved specification item rather than silently invented.

3. Four-stage lifecycle contract

Stage 1: Inventory Presence

The exporter must discover and account for all applicable source records.

Required distinctions:

* Committed records.
* Staged records.
* Unstaged records.
* Untracked records.
* Ignored records.
* Intentional deletion tombstones.
* External dependency references.

Each record must have an unambiguous identity.

Path identity must preserve original path bytes, including non-UTF-8 paths.

Stage 2: Local Availability

The exporter must determine whether the content required by an inventory record is actually accessible.

Required dependency distinctions include:

* Valid locally available Git LFS content.
* Missing LFS content.
* Corrupt LFS local-cache content.
* Cloned submodules.
* Uninitialized or unavailable submodules.
* Missing Git objects.
* Inaccessible content.

A missing or corrupt external dependency must not be represented as an ordinary successful export.

Stage 3: Export Completion

Every exportable record must:

* Have its original bytes reconstructed.
* Have a verified SHA-256 digest.
* Have a verified byte length.
* Be assigned to exactly one package.
* Have matching manifest and package assignment metadata.

Intentional terminal states must not be assigned fabricated payloads.

Stage 4: Integrity Verification

The verifier must independently establish:

* Package integrity.
* Checksum registry parity.
* Payload reconstruction integrity.
* Manifest-to-package parity.
* Record uniqueness.
* Status breakdown reconciliation.
* Closed-ledger balance.
* Dependency classification.
* Correct exit-code precedence.

The verifier must not rely on the exporter having correctly described its own output.

⸻

4. Mandatory exit-code contract

Exit code	Meaning	Required condition
0	PASS	Every exportable payload is byte-exact, accounting balances, and unresolved dependencies equal zero.
1	INCOMPLETE	All exported payloads are byte-exact and accounting is valid, but unresolved dependencies remain explicitly cataloged.
2	FAIL	Integrity, uniqueness, path safety, package assignment, required data, or accounting validation fails.

Precedence

FAIL always takes precedence over INCOMPLETE.

A package hash mismatch cannot be downgraded to INCOMPLETE merely because an unrelated LFS dependency is unresolved.

Malformed or unrecognized records must not silently disappear from accounting.

The verifier must never return PASS when an unresolved dependency remains.

⸻

5. Status classification contract

The supplied verifier currently declares the following classifications.

Intentional terminal states

* staged_deleted
* working_tree_deleted
* inventory_only_ignored

These are not unresolved dependencies.

They must be accounted for without requiring fabricated payload content.

Unresolved dependency states

* unresolved_lfs
* corrupt_lfs_local_cache
* submodule_reference_only
* missing_object
* inaccessible

These states prevent exit code 0.

Exported state

* exported

An exported record must correspond to exactly one reconstructed payload with matching identity, digest, size, and package assignment.

Unknown states

Unknown terminal states must cause exit code 2.

The implementation must not silently reinterpret an unknown state as intentional, unresolved, or exported.

⸻

6. Engineering requirements and acceptance matrix

The following matrix establishes the acceptance gate.

ID	Requirement	Responsible component	Required evidence
P0-001	Inventory completeness	Exporter	Every applicable record appears in the correct inventory domain.
P0-002	Availability classification	Exporter	Missing, corrupt, valid, and accessible dependency fixtures are distinguished.
P0-003	Intentional exclusions	Exporter / Verifier	Tombstones and ignored entries remain accounted for without fabricated payloads.
P0-004	Non-UTF-8 path preservation	Exporter / Verifier	Original path bytes survive roundtrip exactly.
P0-005	Symlink target preservation	Exporter / Verifier	Raw target bytes survive roundtrip exactly.
P0-006	LFS integrity	Exporter	Valid objects are extracted; missing and corrupt objects are distinguished.
P0-007	Submodule accounting	Exporter	Cloned and uninitialized references are inventoried correctly.
P0-008	Package partitioning	Exporter	Package types and source states remain segregated.
P0-009	Oversized file isolation	Exporter	Oversized single-file packages preserve complete payload identity.
P0-010	Package integrity	Verifier	Declared package size and SHA-256 match disk bytes.
P0-011	Checksum registry parity	Verifier	No missing, extra, or duplicate registry targets.
P0-012	Path traversal protection	Verifier	Every referenced path remains inside its authorized root.
P0-013	Manifest uniqueness	Verifier	Duplicate logical records are rejected.
P0-014	Payload uniqueness	Verifier	Duplicate payload identities are rejected.
P0-015	Package assignment parity	Verifier	Manifest and reconstructed package IDs agree.
P0-016	Payload reconstruction	Verifier	Reconstructed bytes match declared digest and size.
P0-017	Encoding validation	Verifier	Only explicitly supported encodings are accepted.
P0-018	Strict Base64 validation	Verifier	Invalid Base64 is rejected rather than silently normalized.
P0-019	Status breakdown reconciliation	Verifier	Every status key and count agrees independently with the manifest.
P0-020	Ignored-record validation	Verifier	Count, status, size, and uniqueness are checked.
P0-021	Closed-ledger reconciliation	Exporter / Verifier	All inventory domains balance to their declared totals.
P0-022	Dependency diagnostics	Exporter / Verifier	Unresolved entries have sufficient diagnostic information for independent review.
P0-023	Unknown status rejection	Verifier	Unrecognized status codes fail closed.
P0-024	Exit-code determinism	Verifier	PASS, INCOMPLETE, and FAIL produce the specified codes.
P0-025	Failure precedence	Verifier	Any integrity failure overrides unresolved-dependency status.
P0-026	Historical commit isolation	Exporter	Historical exports do not accidentally incorporate current working-tree state.
P0-027	Worktree support	Exporter	Worktree exports are independently verified, not merely executed.
P0-028	Reference inventory	Exporter	Annotated tag objects and peeled commit identities remain distinct.

⸻

7. Required adversarial test cases

The existing 28-assertion suite provides useful positive and negative coverage. The following additional tests are required before acceptance.

A. Path and filesystem security

A-01: Package ID traversal

Inject a package ID containing a parent-directory traversal component.

Expected: exit 2. No file outside the authorized package root may be read.

A-02: Checksum registry traversal

Inject a checksum target pointing outside the export root.

Expected: exit 2.

A-03: Symlink escape

Create a referenced package path or parent directory that resolves outside the authorized root through a symlink.

Expected: exit 2.

A-04: Unexpected package contents

Place unregistered files and nested directories in the package directory.

Expected: behavior must match the formally defined package inventory policy. If the package directory is a closed inventory, reject the extras.

B. Identity and duplicate detection

B-01: Duplicate checksum target

Insert the same registry target twice.

Expected: exit 2.

B-02: Duplicate manifest identity

Insert two manifest entries with the same logical identity.

Expected: exit 2.

B-03: Status-code variation

Insert duplicate path and source-state records with different status codes.

Expected: exit 2 if path plus source state is the defined identity.

B-04: Duplicate ignored entry

Duplicate an ignored record.

Expected: exit 2.

B-05: Duplicate package assignment

Place one exported record in two different packages.

Expected: exit 2.

C. Payload reconstruction

C-01: Invalid Base64

Inject invalid Base64 characters.

Expected: exit 2.

C-02: Truncated Base64

Remove required encoded payload characters.

Expected: exit 2.

C-03: Unknown encoding

Declare an unsupported encoding.

Expected: exit 2.

C-04: Invalid UTF-8 package JSON

Provide invalid package-file encoding.

Expected: exit 2 with a controlled diagnostic.

C-05: Correct package hash, incorrect payload hash

Update package and registry hashes after modifying reconstructed payload content, while leaving the payload’s declared original digest unchanged.

Expected: exit 2.

D. Reconciliation and accounting

D-01: Missing breakdown key

Remove a declared status key.

Expected: exit 2.

D-02: Unexpected breakdown key

Add a status not present in the records.

Expected: exit 2.

D-03: Incorrect breakdown count

Change a status count while keeping the total unchanged.

Expected: exit 2.

D-04: Incorrect domain total

Change one domain total.

Expected: exit 2.

D-05: Ignored-record size corruption

Use a negative size, invalid type, or inconsistent ignored-record metadata.

Expected: exit 2.

D-06: Unhandled terminal state

Inject an unknown state.

Expected: exit 2.

E. Dependency classification

E-01: Unresolved LFS with valid unrelated payloads

Expected: exit 1 if all exported content is intact.

E-02: Unresolved dependency plus tampered payload

Expected: exit 2.

E-03: Intentional tombstones only

Expected: exit 0 if all other requirements are satisfied and no unresolved dependencies remain.

E-04: Unresolved record without diagnostic detail

Expected: reject if the normative dependency schema requires diagnostic fields. Exact required fields must be established from the RFC.

⸻

8. Test-suite execution requirements

The compliance suite must not depend on Python assert statements for acceptance decisions.

Every test must remain active under:

* Standard Python execution.
* Optimized Python execution using python -O.

The suite must maintain explicit test accounting:

* Passed.
* Failed.
* Skipped.
* Not executed.
* Blocked by environment.

A skipped test must never be counted as passed.

A test blocked by the host filesystem must be reported as a limitation, not silently treated as proof of compatibility.

Required test result record

Every test must report:

1. Test ID.
2. Requirement ID.
3. Fixture description.
4. Mutation or input.
5. Expected behavior.
6. Actual behavior.
7. Expected exit code.
8. Actual exit code.
9. PASS / FAIL / SKIP / BLOCKED.
10. Diagnostic evidence.

The final suite must return a nonzero result if any mandatory test fails or remains unexecuted without an explicitly authorized exception.

⸻

9. Existing 28-test suite: acceptance mapping

Existing test	Subject	Contract mapping
01	Missing LFS	P0-002, P0-022
02	Corrupt LFS	P0-002, P0-006
03	Valid LFS	P0-006, P0-016
04	Cloned submodule	P0-007
05	Uninitialized submodule	P0-007, P0-022
06	Staged deletion	P0-003
07	Unstaged deletion	P0-003
08	Ignored files	P0-020
09	Non-UTF-8 path	P0-004
10	Non-UTF-8 symlink target	P0-005
11	Committed symlink	P0-005
12	Working-tree symlink	P0-005
13	Git worktree	P0-027
14	Output boundary	P0-012, exporter boundary
15	Unique output directory	Exporter collision policy
16	Historical commit isolation	P0-026
17	Oversized file	P0-009
18	Package type separation	P0-008
19	INCOMPLETE exit code	P0-024
20	PASS exit code	P0-024
21	Payload tampering	P0-016
22	Duplicate payload	P0-014
23	Missing checksum target	P0-011
24	Extra checksum target	P0-011
25	Package file-count mismatch	P0-010
26	FAIL precedence	P0-025
27	Closed-ledger balance	P0-021
28	Annotated tag identity	P0-028

The 28 tests are retained as the existing baseline. The adversarial tests supplement them; they do not silently replace or renumber them.

⸻

10. Verifier implementation requirements

The verifier must:

1. Validate required top-level files before proceeding.
2. Validate manifest structure and required fields.
3. Reject duplicate registry targets.
4. Reject duplicate package IDs.
5. Validate every referenced path before accessing it.
6. Verify checksum registry parity.
7. Verify package count and package inventory.
8. Verify package size and SHA-256.
9. Verify package identity and type.
10. Verify package file count.
11. Validate payload identity.
12. Reject duplicate payload identities.
13. Strictly decode supported encodings.
14. Verify reconstructed payload SHA-256.
15. Verify reconstructed payload size.
16. Reconcile every manifest record against reconstructed payloads.
17. Verify package assignment.
18. Verify each reconciliation domain independently.
19. Verify ignored records independently.
20. Reject unknown terminal states.
21. Reject dangling payloads.
22. Enforce exit-code precedence.

All validation failures must produce controlled diagnostics and exit code 2 rather than an uncontrolled traceback.

The verifier must contain no Python assert statements.

⸻

11. Formal closed-ledger equations

Define:

* C = committed records.
* S = staged records.
* U = unstaged records.
* N = untracked records.
* I = ignored records.
* E = exported payloads.
* T = intentional terminal records.
* D = unresolved dependency records.

The total discovered record count is:

DISCOVERED = C + S + U + N + I

The exported and terminal classifications must reconcile against the relevant discovered records without duplication or omission.

The exported payload accounting requirement is:

E = UNIQUE_EXPORTED_MANIFEST_IDENTITIES = UNIQUE_RECONSTRUCTED_PAYLOAD_IDENTITIES

The dependency condition is:

D = 0 for PASS.

D > 0 permits INCOMPLETE only when every other mandatory integrity and accounting condition passes.

These equations must be checked independently. A calculated value that is never compared to an expected value is not a valid reconciliation test.

⸻

12. Failure classification

Exit 0: PASS

Requirements:

* No checksum mismatch.
* No missing payload.
* No unexpected payload.
* No duplicate logical identity.
* No package assignment mismatch.
* No breakdown mismatch.
* No ledger imbalance.
* No unresolved dependency.
* No unauthorized path access.

Exit 1: INCOMPLETE

Requirements:

* All exported payloads are byte-exact.
* All package hashes and sizes are correct.
* All package assignments are correct.
* All reconciliation equations balance.
* All unresolved dependencies are identified and cataloged.
* No integrity failure exists.

Exit 2: FAIL

Any one of the following is sufficient:

* Missing required package or manifest.
* Invalid checksum.
* Invalid package hash.
* Payload hash mismatch.
* Duplicate identity.
* Path traversal.
* Package assignment mismatch.
* Missing exported payload.
* Dangling payload.
* Invalid status.
* Breakdown mismatch.
* Ledger imbalance.
* Invalid payload encoding.
* Malformed or structurally invalid data.

⸻

13. Acceptance gate

Acceptance requires all gates below to pass.

Gate	Requirement	Status
G-01	Normative RFC requirements reconciled against this contract	PENDING
G-02	Exporter source audit completed	PENDING
G-03	Verifier defects resolved and reviewed	PENDING
G-04	Original 28 tests pass without optimization dependence	PENDING
G-05	Required adversarial tests pass	PENDING
G-06	Closed-ledger accounting independently verified	PENDING
G-07	Exit-code precedence verified	PENDING
G-08	Non-UTF-8 path and symlink roundtrips verified	PENDING
G-09	Full export package independently reconstructed	PENDING
G-10	Final evidence and execution logs retained	PENDING

Acceptance decision

The implementation is accepted only when all mandatory gates are satisfied.

A successful exporter execution alone is insufficient.

A successful verifier execution alone is insufficient.

A successful 28-test run alone is insufficient.

A PASS result must be supported by independent evidence that the complete export is byte-exact and has zero unresolved dependencies.

⸻

14. Required evidence package

The final acceptance package must contain:

1. Exact exporter source.
2. Exact verifier source.
3. Exact compliance suite.
4. Normative RFC source.
5. Test execution environment details.
6. Full test results.
7. Adversarial test results.
8. Export manifest.
9. Checksum registry.
10. Package inventory.
11. Verifier output.
12. Exit code.
13. SHA-256 values for the delivered implementation and evidence artifacts.
14. A final acceptance decision.

No evidence may be represented as executed if it was only statically reviewed.

⸻

15. Current audit disposition

Exporter: Not independently certified.
Verifier: Static audit identified implementation risks.
Compliance suite: Static audit identified coverage and test reliability gaps.
Production export: Not certified.
Acceptance: NOT GRANTED.

This document establishes the proposed engineering acceptance gate. It does not authorize implementation changes or certify any existing export.

Next authorized activity: Reconcile this contract against the complete S7NS-P0-RFC-001 normative specification and the exact exporter source, then finalize the acceptance matrix before implementation changes begin.
