# S7NS CHARACTER BIBLE — TIER 1 FIDELITY REBUILD CHECKPOINT

**Checkpoint timestamp:** 2026-11-11, approximately 6:08 PM HST  
**Project:** S7NS  
**Branch:** `S7NS_SPACE_SAGA_ACTS_20261111`  
**Author authority:** Kaze / Tristan  
**Work state:** IN_PROGRESS — source-owner retrieval verified; Tier 1 rebuild not yet drafted or approved.

## 1. User correction and required action

Kaze identified that the first Tier 1 Character Bible was defective because it largely copied recent Act 42 handoff information about the Sins instead of retrieving and using their actual character-fidelity owners. The user explicitly rejected that deliverable. It must be treated as superseded / not accepted and must not be represented as a valid character-fidelity bible.

Required correction: rebuild Tier 1 from the full character-fidelity owner files and supporting source files. The recent Act 42 handoff may only be used as a present-state overlay where relevant; it is not the character source and must not replace the owners.

## 2. Exact resume position

The newest unfinished step is **rebuilding Tier 1 from the recovered source owners**. Do not restart Tier 2, do not rewrite Tier 2, do not begin Tier 3, and do not repeat completed source retrieval/hash validation.

Tier 2 — Antagonists, Rivals & Mercenaries — was completed and saved before this correction. Its six dossiers and connected records remain as-is unless Kaze later requests changes.

## 3. Source owners recovered and SHA-256 validated

All following owner excerpts were extracted by manifest byte offset/length from the attached physical bundles and their bytes matched the SHA-256 values in `MANIFEST.yaml`.

| Logical owner | Physical source | Role | Bytes | SHA-256 |
|---|---|---|---:|---|
| `canon/characters/kaze_current.md` | `04_KAZE_SINS.md` | inherited mechanics / full owner | 137,508 | `2cea37e9a9b1a38b145dbddaf91220db014d218b1bbbc251a7e437edd0740430` |
| `canon/characters/kaze_psychology.md` | `04_KAZE_SINS.md` | inherited mechanics / full owner | 156,498 | `b2d1d55282207224baac66d0cfe8de86676151489b04f6ed2e73da306ce9e48f` |
| `character_sources/Kaze_Character_Source.txt` | `04_KAZE_SINS.md` | current / full owner | 26,045 | `d21caa61d8a18a7e360dd7046dd269eab1d8a7769f6d7a2f6d791684a8cb70f8` |
| `character_sources/Sins_Group_and_Reputation_Source.txt` | `04_KAZE_SINS.md` | current / full owner | 19,485 | `34685f44e3b2d4076c3924081c2eb6bc0ac183bc482622592b5bcd4af45b35c8` |
| `canon/characters/chris_catfish_billy_current.md` | `05_CHRIS_BILLY(1).md` | inherited mechanics / full owner | 217,740 | `e6db765c6af1af9e18cb40b89419298b38014b2e6469da76e0cf9efb76c7dfe6` |
| `canon/characters/chris_catfish_billy_future.md` | `05_CHRIS_BILLY(1).md` | future progression / full owner | 71,193 | `b4fa4d0992942088bebb7b663daec50390ba2470039c96cad77d0a3b0eb829fb` |
| `character_sources/Chris_Character_Source.txt` | `05_CHRIS_BILLY(1).md` | current / full owner | 51,450 | `d49b99f639a175786ce4671aa06ab6f524128485cd83a9d46a8f0651f95694f4` |
| `character_sources/Billy_Character_Source.txt` | `05_CHRIS_BILLY(1).md` | current / full owner | 51,066 | `ccdb38258021d42375a278c61598656efce9e67d58fead2e4dfe37c9a728bc46` |
| `character_sources/Chris_Billy_BELLY_Source.txt` | `05_CHRIS_BILLY(1).md` | current / full owner | 35,861 | `f5b2234d799645c9c00b85721927ded0b3018dbb5029841d7bca6c41e18153cb` |
| `canon/characters/dana_mana.md` | `dana_mana.md` | current / full owner | 79,337 | `dea9374d91efe4a85d4e11482bb28e072fdf96ec6531b6c461db5d951835cfab` |
| `character_sources/Dana_Character_Source.txt` | `Dana_Character_Source_2.md` | current / full owner | 8,078 | `e3d7b5e377192c276c2e1ecce01440451392147360b72b84965d4c338968cc96` |
| `character_sources/Mana_Character_Source.txt` | `Mana_Character_Source_2.md` | current / full owner | 8,092 | `0ba41abaf0c3d571a63a694b353184eb02584df03a8327f3044785d3cf5ddfbc` |

The Dana/Mana physical filenames in the manifest use `.txt`; the mounted uploaded files use `_2.md`. The exact manifest byte slices were verified against the same SHA-256 values, so the content identity is established despite the upload filename difference.

## 4. Character coverage to rebuild

1. **Kaze** — integrate the full current Kaze owner, psychology owner, Kaze Character Source, and Sins group/reputation source. Do not reduce him to the 1,502-Brapple Act 42 bounty or the few traits in the current checkpoint.
2. **Chris** — integrate the full Chris current owner and Chris Character Source. Preserve his own voice, history, kit, psychology, mechanics, and exact constraints; do not reduce him to “Louisiana marksman / anti-sci-fi purist.”
3. **Daynah / Dana** — use the full Dana/Mana owner and Dana Character Source, plus the author correction source. Capture full baseline, earned progression, gamma forms, build/craft systems, Kahuhu equipment, limitations, and exact naming/spelling rules; do not reduce her to the Act 42 8'10" / 840 lb snapshot.
4. **Catfish Billy** — use Chris/Billy current and future owners, Billy Character Source, and Chris/Billy BELLY source. Preserve host/body rules, independent identity and agency, two-mind/one-body mechanics, voice, contradictions, and exact transformation/continuity boundaries. Future material must be marked as future, not current.
5. **Mahnah / Mana** — use the full Dana/Mana owner and Mana Character Source. Preserve actual canine biology, 1,400-lb baseline if supported by owner, abilities and limitations, reality-bite/spatial mechanics, temperament, voice, and ownership/relationship rules. Do not substitute generic “pit bull portal battery” shorthand.

## 5. Evidence and continuity rules

- The `MANIFEST.yaml` describes a prepared package whose installation was not performed. Its owner roles and byte/hash locators are retrieval metadata, not proof that every historical progression item is currently active.
- Source role and dated scope must be retained. Current owner, inherited mechanics, future progression, historical notes, and superseded material must not be collapsed into one present-tense canon layer.
- The current Acts 35–45 Space Saga handoff is a separate present-day overlay. Use it only for genuinely relevant current status, location, or crossover effects, and label that layer clearly.
- Preserve `[OPEN]` and `[KAZE: fill]` verbatim wherever the source leaves a field open.
- Do not infer powers, origin, personality, dialogue, relationships, or current availability from franchise familiarity or generic knowledge.
- Keep user-authored exact dialogue and signature phrases verbatim; do not invent quotes.
- Keep character sections complete and source-attributed internally; no handoff-only shorthand.

## 6. Existing deliverable disposition

- The first Tier 1 file `continuity/character_bible/TIER_1_CORE_SINS_20261111.md` exists in GitHub and was saved to Notion. It is defective for the requested purpose because it was based too heavily on the Act handoff. Do not cite it as the final fidelity bible. Replace it only after the full source-grounded rebuild is complete and verified.
- Tier 2 file `continuity/character_bible/TIER_2_ANTAGONISTS_20261111.md` remains completed and saved. Do not redo it.

## 7. Next production actions

1. Read and analyze the full extracted source owners listed above, including their internal dates, status labels, corrections, and explicit gaps.
2. Build the five Tier 1 dossiers using Kaze's exact ten-section schema, with substantial detail drawn from the actual owners.
3. Perform a source-by-source coverage audit. Confirm that no major owner mechanics, limitations, forms, voice rules, locked dialogue, or guardrails were omitted.
4. Generate a corrected Tier 1 artifact and replace the defective GitHub Tier 1 file using its latest blob SHA. Update the existing Tier 1 Notion page if it can be identified unambiguously; otherwise create a clearly titled corrected page and mark the old page superseded without deleting it.
5. Update Airtable only with clearly branch-scoped corrected character records; do not overwrite records from other branches.
6. Verify GitHub readback, Notion page readback, and Airtable record values before reporting completion.

**Resume instruction:** Continue directly with full owner analysis and Tier 1 reconstruction. Do not repeat manifest retrieval or hash verification unless a source changes.