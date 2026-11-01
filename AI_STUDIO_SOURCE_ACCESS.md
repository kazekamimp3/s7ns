# AI Studio Source Retrieval Guide

Repository: https://github.com/kazekamimp3/s7ns

## Important: use GitHub browser pages, not raw URLs

Some AI Studio browsing environments block `raw.githubusercontent.com`. If that happens, do not retry raw URLs. Use the normal GitHub web interface on `github.com` instead.

Start with:
- https://github.com/kazekamimp3/s7ns/blob/main/AI_STUDIO_START_HERE.md
- https://github.com/kazekamimp3/s7ns/blob/main/S7NS_SOURCE_INDEX.md
- https://github.com/kazekamimp3/s7ns/blob/main/SOURCE_MANIFEST.json

For each source file, construct/open its GitHub browser page using:
`https://github.com/kazekamimp3/s7ns/blob/main/<repository-path>`

Example:
https://github.com/kazekamimp3/s7ns/blob/main/source/00_authority/01_BOOT_AUTHORITY.md

Directory listings:
- https://github.com/kazekamimp3/s7ns/tree/main/source/00_authority
- https://github.com/kazekamimp3/s7ns/tree/main/source/01_character_owners
- https://github.com/kazekamimp3/s7ns/tree/main/source/02_runeterra
- https://github.com/kazekamimp3/s7ns/tree/main/source/03_season3
- https://github.com/kazekamimp3/s7ns/tree/main/source/04_world_research
- https://github.com/kazekamimp3/s7ns/tree/main/source/05_history
- https://github.com/kazekamimp3/s7ns/tree/main/source/06_manifests

## Ingestion requirements

1. Read the complete source index and manifest.
2. Open source files through GitHub browser pages (`github.com/.../blob/main/...`), not raw URLs.
3. Read files in manageable batches. Large files may require multiple page/line-range reads if the browsing environment truncates them.
4. Keep every original file independent. Dated/revision variants are separate artifacts.
5. Preserve source authority and state distinctions. Do not silently reconcile conflicts.
6. Record exact files fully read, partially read, inaccessible, or truncated.
7. Do not claim full ingestion based on filenames, directory listings, manifests, or summaries alone.
8. Remain in WORK mode. No scene execution, fictional time advancement, or source modification.

## Integrity

The GitHub Actions import completed successfully at commit:
`20a46268020de3939fbf408ee221a4f32e864ec2`

The import job reported:
`SUCCESS: all 38 source raw links verified.`

This proves the GitHub-hosted raw files were reachable during the import verification. It does not prove a separate AI Studio session can access them. AI Studio must report its own retrieval results honestly.
