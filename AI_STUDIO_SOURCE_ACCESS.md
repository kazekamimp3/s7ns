# AI Studio Source Retrieval Guide

Repository: https://github.com/kazekamimp3/s7ns

## Start here

Fetch these two files first:

- https://raw.githubusercontent.com/kazekamimp3/s7ns/main/S7NS_SOURCE_INDEX.md
- https://raw.githubusercontent.com/kazekamimp3/s7ns/main/SOURCE_MANIFEST.json

The index contains a direct `raw.githubusercontent.com` URL for every source document. The manifest contains each original filename, repository path, byte size and SHA-256 digest.

## Retrieval procedure

1. Read the source index and manifest.
2. Fetch the raw URLs for all required source owners. For a full project initialization, fetch the complete authority/current-state/routing sources, active Season 3 material, complete character owners, world/research sources, manifests and historical archives.
3. Preserve each source as an independent owner. Similar filenames and dated suffixes indicate distinct artifacts and must not be silently collapsed.
4. Verify fetched byte sizes and SHA-256 values against `SOURCE_MANIFEST.json` whenever the ingestion environment permits.
5. If a raw URL fails, report its exact path. Do not replace it with a summary or guessed version.
6. Use the raw URLs unchanged in Google AI Studio URL-context or source-ingestion workflows.

## Direct source-link list

All 38 source links are in `S7NS_SOURCE_INDEX.md`. This guide is intentionally a stable entry point for a fresh AI Studio session.
