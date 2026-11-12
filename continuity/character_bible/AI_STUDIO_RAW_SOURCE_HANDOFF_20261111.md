# S7NS — Complete Raw-Source Handoff for Google AI Studio

Prepared: 2026-11-11
Purpose: portable, self-contained source retrieval and continuity bootstrap for a fresh Google AI Studio session.

CRITICAL RAW-URL REQUIREMENT:
Every source reference intended for retrieval must be a complete, literal, plain-text URL beginning with https://raw.githubusercontent.com/. Do not use Markdown links, GitHub blob URLs, GitHub repository-page URLs, shortened links, relative paths, or filename-only references as retrieval targets. A filename may appear only as descriptive metadata beside its complete raw URL. If a raw URL is unavailable or fails, report that exact raw URL and the failure; never substitute a normal GitHub page URL.
Mode: WORK. This document does not authorize PLAY, episode prose, fictional time advancement, or canon changes.
Creative Director and final authority: Kaze.

## 1. Mandatory first-read order

1. Read this entire handoff.
2. Read the current Space Saga checkpoint and approved Character Bible tier files (Section 2).
3. Read the Space Saga authority/current-state/routing bundles and the Space manifest/index (Section 3).
4. Retrieve the remaining Space physical bundles (Section 3) and the supporting source-owner material (Section 4).
5. Read the older Runeterra index/manifest and source bundles only as branch-separated reference (Section 5).
6. Build a retrieval ledger listing every URL, fetched byte length, computed SHA-256, manifest-declared byte length/hash, status, and any truncation/failure. Do not claim a source was read unless its full body was retrieved and verified.

## 2. Current controlling Space Saga state and author-approved Character Bible

These files are current controlling state or approved author-reviewed references. Retrieve the full body of each.

### Current act checkpoint
- Act 42 → Act 43 checkpoint
  https://raw.githubusercontent.com/kazekamimp3/s7ns/main/continuity/acts/ACT_42_TO_43_CHECKPOINT_20261111.md
  Purpose: current Space Saga cursor, completed Acts 35–42, exact Act 43 setup, ledger, TTS constraints.

### Approved Character Bible — five tiers and audit
- Tier 1 — Core Sins & Ship Crew: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/continuity/character_bible/TIER_1_CORE_SINS_20261111.md
- Tier 2 — Antagonists, Rivals & Mercenaries: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/continuity/character_bible/TIER_2_ANTAGONISTS_20261111.md
- Tier 3 — Lānaʻi & Outer Rim Lore Anchors: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/continuity/character_bible/TIER_3_LANAI_OUTER_RIM_20261111.md
- Tier 4 — Red Dead & Historical Ledger: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/continuity/character_bible/TIER_4_RED_DEAD_HISTORICAL_LEDGER_20261111.md
- Tier 5 — Household Residents & Missing Persons: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/continuity/character_bible/TIER_5_HOUSEHOLD_RESIDENTS_MISSING_PERSONS_20261111.md
- Cross-tier audit: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/continuity/character_bible/CROSS_TIER_AUDIT_20261111.md

Author approval status: Kaze explicitly approved all five tiers and the cross-tier audit. Approval does NOT close [OPEN] fields, resolve unknowns, authorize PLAY, or convert future plans into occurred events.

### Previous progress checkpoint
- https://raw.githubusercontent.com/kazekamimp3/s7ns/main/continuity/character_bible/AI_STUDIO_RAW_SOURCE_HANDOFF_CHECKPOINT_20261111.md
  Purpose: prior work state and this handoff's exact continuation checkpoint. Do not redo its completed steps.

## 3. Space Saga source repository — complete physical-bundle inventory

Repository identifier: kazekamimp3/s7ns
Branch: main
All URLs below are raw text URLs. The path is from SOURCE_MANIFEST.json and was checked against the repository tree. The manifest-declared byte length and SHA-256 are metadata, not a claim that this session independently downloaded and hashed each complete bundle.

Space routing/manifest files:
- SOURCE_MANIFEST.json: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/SOURCE_MANIFEST.json
- Space manifest with logical module routes and byte offsets: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/06_manifests/MANIFEST_SPACE_20261024.yaml
- General source manifest: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/06_manifests/MANIFEST.yaml

### 3A. Authority and routing
- `01_BOOT_AUTHORITY.md` — 0 logical modules; declared 474268 bytes; SHA-256 `4841a244fc829e949c2b8f816eb345b4558dae195618cb48456f2d901c8e8c12`; tree bytes 474268. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/00_authority/01_BOOT_AUTHORITY.md
- `01_BOOT_AUTHORITY_SPACE_20261024.md` — 19 logical modules; declared 524545 bytes; SHA-256 `9a92bb8e4d32ca4b208b4912ee316966df2f4c2b44132e6e19a688703b12b98e`; tree bytes 524545. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/00_authority/01_BOOT_AUTHORITY_SPACE_20261024.md
- `02_CURRENT_STATE(1).md` — 0 logical modules; declared 1035651 bytes; SHA-256 `6da42e7579fb40edac3f49565ccd0c9f3ec079139c8e5839556aa884c8dd6eca`; tree bytes 1035651. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/00_authority/02_CURRENT_STATE(1).md
- `02_CURRENT_STATE_SPACE_20261024.md` — 23 logical modules; declared 2058342 bytes; SHA-256 `f8877526acfd122f66e0025d5e23f61ea2eb3fb537c6bf7feffcb57200b0d9a1`; tree bytes 2058342. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/00_authority/02_CURRENT_STATE_SPACE_20261024.md
- `03_INDEX_ROUTING.md` — 0 logical modules; declared 3015276 bytes; SHA-256 `6e629d7a35c6f74367918a6c36b57d83666dfabee57d901a2fe32993e958b7d1`; tree bytes 3015276. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/00_authority/03_INDEX_ROUTING.md
- `03_INDEX_ROUTING_SPACE_20261024.md` — 160 logical modules; declared 3614995 bytes; SHA-256 `c4dbf24318e8db9b519c1489522c237f19a5a38ea042ab55a9da2e960e0ce033`; tree bytes 3614995. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/00_authority/03_INDEX_ROUTING_SPACE_20261024.md

### 3B. Character owner bundles
- `04_KAZE_SINS.md` — 6 logical modules; declared 390851 bytes; SHA-256 `85f7312f574af2a1950aa4f80ed1a6bc9ebfab0c071e75700c0fdb7e04869db8`; tree bytes 390851. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/04_KAZE_SINS.md
- `05_CHRIS_BILLY(1).md` — 13 logical modules; declared 606164 bytes; SHA-256 `4ce1d1f2945b15b8ee1b47fadc6568511f80fa95081a09025148e04e15f85800`; tree bytes 606164. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/05_CHRIS_BILLY(1).md
- `06_OTHER_MAIN_CAST(1).md` — 22 logical modules; declared 377983 bytes; SHA-256 `7208666d9f886c6554fbb7435cdaee56e873c87f0f6178011963ba2bfcdbd2ce`; tree bytes 378329 [SIZE MISMATCH]. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/06_OTHER_MAIN_CAST(1).md
- `07_CROSSOVER_CAST(3).md` — 18 logical modules; declared 92997 bytes; SHA-256 `b7a8d9eeb70a551d043a937c5988f8a9d39b539bca61b9e2026c5abc4607cd59`; tree bytes 92997. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/07_CROSSOVER_CAST(3).md
- `08_CROSSOVER_EXTENDED(4)(1).md` — 19 logical modules; declared 206809 bytes; SHA-256 `20bb53a3e30ceb72f1fab924ded78cf0ad06b61fdf5467b76809f619c0242538`; tree bytes 206809. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/08_CROSSOVER_EXTENDED(4)(1).md
- `14_BILLY_SPECIALS(3).md` — 12 logical modules; declared 308529 bytes; SHA-256 `d4bd7dead6c89bfcb8b6b8cf48eed7e0c58439b2f307e06258e30d34108732fb`; tree bytes 308529. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/14_BILLY_SPECIALS(3).md
- `Dana_Character_Source_2.md` — 1 logical modules; declared 8078 bytes; SHA-256 `e3d7b5e377192c276c2e1ecce01440451392147360b72b84965d4c338968cc96`; tree bytes 8078. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/Dana_Character_Source_2.md
- `Mana_Character_Source_2.md` — 0 logical modules; declared 8092 bytes; SHA-256 `0ba41abaf0c3d571a63a694b353184eb02584df03a8327f3044785d3cf5ddfbc`; tree bytes 9195 [SIZE MISMATCH]. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/Mana_Character_Source_2.md
- `dana_mana.md` — 1 logical modules; declared 79337 bytes; SHA-256 `dea9374d91efe4a85d4e11482bb28e072fdf96ec6531b6c461db5d951835cfab`; tree bytes 79337. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/dana_mana.md

### 3C. Runeterra and Season 3 source bundles in the Space package
- `09_RUNETERRA_APPENDIX.md` — 1 logical modules; declared 2354712 bytes; SHA-256 `3a1f521feff8c62421b80bc6ee4e2ea16264747edb3476ea7af09eb9a053bd37`; tree bytes 2354712. Branch-sensitive historical/season material; determine scope from authority files before use. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/02_runeterra/09_RUNETERRA_APPENDIX.md
- `10_RUNETERRA_CORE.md` — 2 logical modules; declared 1038839 bytes; SHA-256 `58559fb3571364fcea85d9388a69d2bc770e91921377499fe24fae4d2a4efb04`; tree bytes 1038839. Branch-sensitive historical/season material; determine scope from authority files before use. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/02_runeterra/10_RUNETERRA_CORE.md
- `11_RUNETERRA_A_M.md` — 28 logical modules; declared 74307 bytes; SHA-256 `e344e9baf81065f25198aac35c3cb563f218a1b01aac24597a8f294968ee14b9`; tree bytes 74307. Branch-sensitive historical/season material; determine scope from authority files before use. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/02_runeterra/11_RUNETERRA_A_M.md
- `12_RUNETERRA_N_Z.md` — 31 logical modules; declared 80084 bytes; SHA-256 `c86a95b278811724448fa5a35e1900eeae38faeecbdbfa3d0e1b76f729db4ada`; tree bytes 80084. Branch-sensitive historical/season material; determine scope from authority files before use. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/02_runeterra/12_RUNETERRA_N_Z.md
- `13_SEASON3_CURRENT.md` — 39 logical modules; declared 1089992 bytes; SHA-256 `63ecf60e2b686facdde9a526898c93d58786ab744f6c8320a3d4e03c95485422`; tree bytes 1089992. Branch-sensitive historical/season material; determine scope from authority files before use. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/03_season3/13_SEASON3_CURRENT.md
- `15_SEASON3_PLOTS.md` — 0 logical modules; declared 1233572 bytes; SHA-256 `b1bb68395c2f92a6b34192c8d29abc6fcdede31bbbc66e6b51dfe63d363b4c5d`; tree bytes 1233572. Branch-sensitive historical/season material; determine scope from authority files before use. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/03_season3/15_SEASON3_PLOTS.md
- `15_SEASON3_PLOTS_SPACE_20261024.md` — 61 logical modules; declared 2673388 bytes; SHA-256 `a3ad4eba9c7c74d4160ab82b16f627d2325fd683357b9e45592eb64576b8a7c6`; tree bytes 2673388. Branch-sensitive historical/season material; determine scope from authority files before use. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/03_season3/15_SEASON3_PLOTS_SPACE_20261024.md
- `16_ROSTER_DUELS_TRAVEL.md` — 13 logical modules; declared 1007570 bytes; SHA-256 `4d211b1e8eedcf6d580224a308ae1e9db10127d72ae18957af7c71afb51e3d9a`; tree bytes 1007570. Branch-sensitive historical/season material; determine scope from authority files before use. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/03_season3/16_ROSTER_DUELS_TRAVEL.md
- `17_BELLY_COMBAT.md` — 3 logical modules; declared 22703 bytes; SHA-256 `02e08b8555bb8a9527819c14ee490f699e52c832bf2e0eccccd1746020c8f1bc`; tree bytes 22703. Branch-sensitive historical/season material; determine scope from authority files before use. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/03_season3/17_BELLY_COMBAT.md

### 3D. World presentation and research bundles
- `18_WORLD_PRESENTATION(1).md` — 0 logical modules; declared 578436 bytes; SHA-256 `b41b291990c44c0be9a0a2c35225edd9e1cea79bbb865eb82ed86bdea12dabc9`; tree bytes 578436. Research/world presentation evidence; separate source evidence from current canon. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/04_world_research/18_WORLD_PRESENTATION(1).md
- `18_WORLD_PRESENTATION(1)_R21_20261024.md` — 38 logical modules; declared 687264 bytes; SHA-256 `f6b8553af56dcb5d0cd3aa4384741c9d36597e393bff811708fedd4a864acb7a`; tree bytes 687264. Research/world presentation evidence; separate source evidence from current canon. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/04_world_research/18_WORLD_PRESENTATION(1)_R21_20261024.md
- `19_RESEARCH(1).md` — 0 logical modules; declared 311336 bytes; SHA-256 `8b2a459ba2d6a21adcc4cdec0b0c213d0e4e29f6ba79a3f4570db7b61e680b18`; tree bytes 311336. Research/world presentation evidence; separate source evidence from current canon. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/04_world_research/19_RESEARCH(1).md
- `19_RESEARCH(1)_R20_20261024.md` — 28 logical modules; declared 344823 bytes; SHA-256 `2601ffdaff592b4919d5fa272b4d8930060625964ab52fd46bbeed4d8aeb3cac`; tree bytes 344823. Research/world presentation evidence; separate source evidence from current canon. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/04_world_research/19_RESEARCH(1)_R20_20261024.md
- `20_RESEARCH_SUPPORT.md` — 11 logical modules; declared 201818 bytes; SHA-256 `a93e28e3a036da0cea8ba357b9b2d6c89b88ea5a30e2397495d3f1c9f71a93a9`; tree bytes 201818. Research/world presentation evidence; separate source evidence from current canon. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/04_world_research/20_RESEARCH_SUPPORT.md

### 3E. Historical-state and archive bundles
- `21_HISTORICAL_STATE.md` — 3 logical modules; declared 1176940 bytes; SHA-256 `140f1aa336f1a577f4d4248d7f2e2773a7d7962777ebd4ad1bf0f8f12efc48ee`; tree bytes 1176940. Historical archive; do not treat archive chronology as current state without current-state confirmation. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/05_history/21_HISTORICAL_STATE.md
- `22_HISTORY_ARCHIVE_PART_01.md` — 1 logical modules; declared 1474897 bytes; SHA-256 `13d4c498bd37def3f2dcecb749a3929c8a3841dd2830d50def4642df703d6790`; tree bytes 1474897. Historical archive; do not treat archive chronology as current state without current-state confirmation. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/05_history/22_HISTORY_ARCHIVE_PART_01.md
- `23_HISTORY_ARCHIVE_PART_02.md` — 1 logical modules; declared 1798617 bytes; SHA-256 `60cd1cb622239a725601d20932816d737596d707636c7ac6ac21e96a4379dfb7`; tree bytes 1798617. Historical archive; do not treat archive chronology as current state without current-state confirmation. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/05_history/23_HISTORY_ARCHIVE_PART_02.md
- `24_HISTORY_ARCHIVE_PART_03.md` — 1 logical modules; declared 1478327 bytes; SHA-256 `2fbd86926ed8f41d02ba3f11b3a60afbc25f4e60cf1424d7a0b6ae73ab996620`; tree bytes 1478327. Historical archive; do not treat archive chronology as current state without current-state confirmation. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/05_history/24_HISTORY_ARCHIVE_PART_03.md
- `25_HISTORY_ARCHIVE_PART_04.md` — 1 logical modules; declared 1471780 bytes; SHA-256 `96f43d656becb4b8a64d336ba6108d908ccbad2bdaa7d883c1cfcb32adf5ae2b`; tree bytes 1471780. Historical archive; do not treat archive chronology as current state without current-state confirmation. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/05_history/25_HISTORY_ARCHIVE_PART_04.md
- `26_HISTORY_ARCHIVE_PART_05.md` — 1 logical modules; declared 1470359 bytes; SHA-256 `c172b13162af3dbb8f3fd7836a4f3d7587d214d7f94e646bfb90e1cb0dba9367`; tree bytes 1470359. Historical archive; do not treat archive chronology as current state without current-state confirmation. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/05_history/26_HISTORY_ARCHIVE_PART_05.md
- `27_HISTORY_ARCHIVE_PART_06.md` — 1 logical modules; declared 1139900 bytes; SHA-256 `f194ca8f9d40228be12d89d8f3615d0bd0454859394c0a943875b33c91a769d6`; tree bytes 1139900. Historical archive; do not treat archive chronology as current state without current-state confirmation. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/05_history/27_HISTORY_ARCHIVE_PART_06.md

### 3F. Manifests and standalone Dana/Mana owner material
- `Dana_Character_Source_2.md` — declared 8078 bytes; SHA-256 `e3d7b5e377192c276c2e1ecce01440451392147360b72b84965d4c338968cc96`; tree bytes 8078. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/Dana_Character_Source_2.md
- `MANIFEST.yaml` — declared 337244 bytes; SHA-256 `4d4ec12142131ea9858a20bf6844fff018312db4e633d68d0e360bac3a18dd50`; tree bytes 337244. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/06_manifests/MANIFEST.yaml
- `MANIFEST_SPACE_20261024.yaml` — declared 231335 bytes; SHA-256 `49acfad805f76d73bc56957b16797c85c06f43342956c55abe80973825263228`; tree bytes 231335. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/06_manifests/MANIFEST_SPACE_20261024.yaml
- `Mana_Character_Source_2.md` — declared 8092 bytes; SHA-256 `0ba41abaf0c3d571a63a694b353184eb02584df03a8327f3044785d3cf5ddfbc`; tree bytes 9195 [SIZE MISMATCH]. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/Mana_Character_Source_2.md
- `dana_mana.md` — declared 79337 bytes; SHA-256 `dea9374d91efe4a85d4e11482bb28e072fdf96ec6531b6c461db5d951835cfab`; tree bytes 79337. Raw: https://raw.githubusercontent.com/kazekamimp3/s7ns/main/source/01_character_owners/dana_mana.md

## 4. Older repository — standalone character owners, author directions, and research

Repository identifier: kazekamimp3/kaze808
Branch: main
These are source-owner references and author directions. They are not a replacement for the current Space Saga checkpoint. The separate branch identified by the older repository's CURRENT.json/DELIVERY_LEDGER.json is `S3_RESET_CAMPFIRE_CANON_CHRIS_RETOLD_20261017`; its Episode 73/74 cursor must not be imported into Space Saga.

### 4A. Standalone character and canon sources
- Current Chris/Catfish Billy character owner: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/canon/characters/chris_catfish_billy_current.md
- Chris/Catfish Billy future branch; do not treat as current events: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/canon/characters/chris_catfish_billy_future.md
- Dana/Mana character source: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/canon/characters/dana_mana.md
- S37 kit/character application source: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/canon/characters/s37_kit_application.md
- Billy character fidelity owner: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/character_sources/Billy_Character_Source.txt
- Chris character fidelity owner: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/character_sources/Chris_Character_Source.txt
- Dana character fidelity owner: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/character_sources/Dana_Character_Source.txt
- K.K./Keke character fidelity owner: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/character_sources/KK_Keke_Complete_Character_Source_20261019.md
- Mana character fidelity owner: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/character_sources/Mana_Character_Source.txt
- Dana/Mana reinstatement author direction: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/Dana_Mana_Reinstated_After_E32_20261018.json
- K.K./Zid scoped author direction: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/KK_Keke_and_Zid_Scoped_Esketit_20261019.json
- Cast-focus author direction: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_Cast_Focus_R8_20261023.md
- Mahnah/Dana/Chris trust-exchange author direction: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_Mahnah_Crucifix_Daynah_Trust_Chris_Exchange_20261021.md
- Mana Season 3 integration author direction; older branch reference: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_Mana_Shoplifting_Season3_Integration_20261021.md
- Kaze/Starkiller/cast mobility author direction; older branch reference: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_Post_E50_Approvals_Kaze_Starkiller_Cast_Mobility_20261021.md
- TTS/faction/Brian balance author direction; older branch reference: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_Post_E50_TTS_Faction_Beef_Brian_Rebalance_20261021.md
- K.K./Billy/Clifford fidelity corrections: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_R10_KK_Billy_Clifford_Fidelity_Corrections_20261020.md
- Daynah/Brian consequences author direction; older branch reference: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_Restaurant_Consequences_Daynah_Anger_Brian_Reversal_20261022.md
- Space Saga director's outline; future planning, status caveats inside source: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_SPACE_SAGA_DIRECTORS_HANDOFF_OUTLINE_20261105.md
- New-member cast/source fidelity research: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/research/TPP_New_Members_WTF_Cast_Source_Fidelity_20261019.md
- Tracy Morgan speech-fidelity research: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/research_sources/Tracy_Morgan_Speech_Fidelity_After_E32_20261018.md

### 4B. Older author and research references
Use only where relevant to the Space Saga and only after checking whether a newer Space-specific direction supersedes it. These sources are older-branch references unless their content explicitly scopes into Space Saga:
- Current older-branch state: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/CURRENT.json
- Older-branch delivery ledger: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/DELIVERY_LEDGER.json
- Older-branch first-read authority: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/KAZE_READ_FIRST.txt
- Space E82–E100 selected future-development handoff (NOT occurred, NOT current cursor, NOT PLAY authorization): https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_SPACE_ARC_E82_E100_AI_STUDIO_HANDOFF_20261027.md
- Space Saga director's outline dated 2026-11-05 (future planning; inspect its internal status/approval caveats; not a current episode cursor): https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/author/S7NS_SPACE_SAGA_DIRECTORS_HANDOFF_OUTLINE_20261105.md

## 5. Older Runeterra/Season 3 source bundles — separate branch only

Repository identifier: kazekamimp3/kaze808
Branch: main
Routing/manifest/access files:
- MASTER_SOURCE_INDEX.json: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/routing/MASTER_SOURCE_INDEX.json
- MANIFEST.yaml: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/MANIFEST.yaml
- ACCESS_INDEX.json: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/complete_sources/ACCESS_INDEX.json
- KAZE_READ_FIRST.txt: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/KAZE_READ_FIRST.txt
- CURRENT.json: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/CURRENT.json
- DELIVERY_LEDGER.json: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/continuity/DELIVERY_LEDGER.json

### 5A. Full physical source-bundle inventory
- `11_RUNETERRA_A_M.md` — 28 logical modules; manifest declares 74307 bytes and SHA-256 `e344e9baf81065f25198aac35c3cb563f218a1b01aac24597a8f294968ee14b9`; current tree bytes 74307; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/11_RUNETERRA_A_M.md
- `12_RUNETERRA_N_Z.md` — 31 logical modules; manifest declares 80084 bytes and SHA-256 `c86a95b278811724448fa5a35e1900eeae38faeecbdbfa3d0e1b76f729db4ada`; current tree bytes 80084; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/12_RUNETERRA_N_Z.md
- `20_RESEARCH_SUPPORT.md` — 11 logical modules; manifest declares 201818 bytes and SHA-256 `a93e28e3a036da0cea8ba357b9b2d6c89b88ea5a30e2397495d3f1c9f71a93a9`; current tree bytes 201818; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/20_RESEARCH_SUPPORT.md
- `10_RUNETERRA_CORE.md` — 2 logical modules; manifest declares 1038839 bytes and SHA-256 `58559fb3571364fcea85d9388a69d2bc770e91921377499fe24fae4d2a4efb04`; current tree bytes 1038839; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/10_RUNETERRA_CORE.md
- `24_HISTORY_ARCHIVE_PART_03.md` — 1 logical modules; manifest declares 1478327 bytes and SHA-256 `2fbd86926ed8f41d02ba3f11b3a60afbc25f4e60cf1424d7a0b6ae73ab996620`; current tree bytes 1478327; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/24_HISTORY_ARCHIVE_PART_03.md
- `09_RUNETERRA_APPENDIX.md` — 1 logical modules; manifest declares 2354712 bytes and SHA-256 `3a1f521feff8c62421b80bc6ee4e2ea16264747edb3476ea7af09eb9a053bd37`; current tree bytes 2354712; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/09_RUNETERRA_APPENDIX.md
- `26_HISTORY_ARCHIVE_PART_05.md` — 1 logical modules; manifest declares 1470359 bytes and SHA-256 `c172b13162af3dbb8f3fd7836a4f3d7587d214d7f94e646bfb90e1cb0dba9367`; current tree bytes 1470359; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/26_HISTORY_ARCHIVE_PART_05.md
- `21_HISTORICAL_STATE.md` — 3 logical modules; manifest declares 1176940 bytes and SHA-256 `140f1aa336f1a577f4d4248d7f2e2773a7d7962777ebd4ad1bf0f8f12efc48ee`; current tree bytes 1176940; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/21_HISTORICAL_STATE.md
- `22_HISTORY_ARCHIVE_PART_01.md` — 1 logical modules; manifest declares 1474897 bytes and SHA-256 `13d4c498bd37def3f2dcecb749a3929c8a3841dd2830d50def4642df703d6790`; current tree bytes 1474897; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/22_HISTORY_ARCHIVE_PART_01.md
- `27_HISTORY_ARCHIVE_PART_06.md` — 1 logical modules; manifest declares 1139900 bytes and SHA-256 `f194ca8f9d40228be12d89d8f3615d0bd0454859394c0a943875b33c91a769d6`; current tree bytes 1139900; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/27_HISTORY_ARCHIVE_PART_06.md
- `23_HISTORY_ARCHIVE_PART_02.md` — 1 logical modules; manifest declares 1798617 bytes and SHA-256 `60cd1cb622239a725601d20932816d737596d707636c7ac6ac21e96a4379dfb7`; current tree bytes 1798617; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/23_HISTORY_ARCHIVE_PART_02.md
- `25_HISTORY_ARCHIVE_PART_04.md` — 1 logical modules; manifest declares 1471780 bytes and SHA-256 `96f43d656becb4b8a64d336ba6108d908ccbad2bdaa7d883c1cfcb32adf5ae2b`; current tree bytes 1471780; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/25_HISTORY_ARCHIVE_PART_04.md
- `14_BILLY_SPECIALS(3).md` — 12 logical modules; manifest declares 305799 bytes and SHA-256 `22bab809e53c67a0db9f29572ab519305e476a31122c58efe65e31a52d5d9e94`; current tree bytes 305799; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/14_BILLY_SPECIALS(3).md
- `07_CROSSOVER_CAST(3).md` — 20 logical modules; manifest declares 86893 bytes and SHA-256 `e3d7ab1fbcb89903b3c9fe2a759a66cb5842096cd433fdee961c0292bb9f35c7`; current tree bytes 86410 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/07_CROSSOVER_CAST(3).md
- `08_CROSSOVER_EXTENDED(4).md` — 21 logical modules; manifest declares 189400 bytes and SHA-256 `7b6b6e6354e391c173f0297f028bdbf3adf6cdc81566a2c4fcb8b677216c7200`; current tree bytes 183031 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/08_CROSSOVER_EXTENDED(4).md
- `17_BELLY_COMBAT.md` — 3 logical modules; manifest declares 19276 bytes and SHA-256 `a43900fb6748039afde45af43a9ad9f0a283ada60176ce4e2ced95b09d39f802`; current tree bytes 19276; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/17_BELLY_COMBAT.md
- `18_WORLD_PRESENTATION.md` — 29 logical modules; manifest declares 575679 bytes and SHA-256 `3eec2f45ed0930211a132ac6cd16f3c41ea32b4448db5cc8f0dc958242b0b84d`; current tree bytes 569592 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/18_WORLD_PRESENTATION.md
- `ACTIVE_AUTHOR_UPDATE_20261017_BRIAR_KAZE_RICK_MORTY.txt` — 0 logical modules; manifest declares 7904 bytes and SHA-256 `334aa56408c9a151fba01d602addcadcd37dcc455b7984db090ade0914921e26`; current tree bytes 7904; role `author_overlay`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/ACTIVE_AUTHOR_UPDATE_20261017_BRIAR_KAZE_RICK_MORTY.txt
- `16_ROSTER_DUELS_TRAVEL.md` — 14 logical modules; manifest declares 1003299 bytes and SHA-256 `1b74e6ad122a1eb3752f8d4b30060cc88bdaec22cfb76a5c5e1f23acb7d98221`; current tree bytes 1002500 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/16_ROSTER_DUELS_TRAVEL.md
- `01_BOOT_AUTHORITY.md` — 17 logical modules; manifest declares 470182 bytes and SHA-256 `c4c5be51a70b1aac74ac6cdecdc533109600d65b3437ad0a53169b6738d03d5d`; current tree bytes 470182; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/01_BOOT_AUTHORITY.md
- `02_CURRENT_STATE.md` — 21 logical modules; manifest declares 843309 bytes and SHA-256 `f3dcc53ff4126e1f5dd63efc2dac2ea52ba5c696180e1ad870e2d1586550f948`; current tree bytes 836157 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/02_CURRENT_STATE.md
- `03_INDEX_ROUTING.md` — 160 logical modules; manifest declares 3312921 bytes and SHA-256 `67e69850d16c19245230f41315132d586ba021bb67e8e5a887b7b3298e23be3a`; current tree bytes 3294578 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/03_INDEX_ROUTING.md
- `04_KAZE_SINS.md` — 6 logical modules; manifest declares 382680 bytes and SHA-256 `e18ef6a28b4290175297fbf8e3f78955b7f04cfb666372ae1bf4f56d369e0f72`; current tree bytes 380763 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/04_KAZE_SINS.md
- `05_CHRIS_BILLY.md` — 15 logical modules; manifest declares 587536 bytes and SHA-256 `f2eecc033c994e039d31ce490a89974873f6e04f577b157c2f2dc5d7fa85da68`; current tree bytes 580610 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/05_CHRIS_BILLY.md
- `06_OTHER_MAIN_CAST.md` — 23 logical modules; manifest declares 359408 bytes and SHA-256 `4a1f3ede0c15da583086c597f37d23b65699116f56c683df70e07414507757af`; current tree bytes 356414 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/06_OTHER_MAIN_CAST.md
- `13_SEASON3_CURRENT.md` — 10 logical modules; manifest declares 683276 bytes and SHA-256 `57af52984b79515c409564032ef7267ca57b7ad2d0c187938551ec044a973f10`; current tree bytes 682111 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/13_SEASON3_CURRENT.md
- `15_SEASON3_PLOTS.md` — 23 logical modules; manifest declares 795805 bytes and SHA-256 `8a02394465f44602ea7ff37fd0edc2ef51adc9c62d42b330d3c44e56a3e4a030`; current tree bytes 791558 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/15_SEASON3_PLOTS.md
- `19_RESEARCH.md` — 21 logical modules; manifest declares 269029 bytes and SHA-256 `dd373b021f2e12149106f3735018bdf54dc6d88bc4269eea260096440e2c1893`; current tree bytes 266185 [SIZE MISMATCH]; role `controlling_bundle`. Raw: https://raw.githubusercontent.com/kazekamimp3/kaze808/main/19_RESEARCH.md

The older master index contains 477 parsed logical routes; the older MANIFEST.yaml declares 476. Eight indexed byte ranges exceed the manifest-declared physical bundle length (three in `03_INDEX_ROUTING.md`, five in `15_SEASON3_PLOTS.md`). Twelve older physical bundles have manifest byte lengths that differ from current tree byte lengths. Do not silently repair or ignore these differences. For extraction, use the actual fetched bytes, record offsets/ranges, and report invalid/out-of-bounds ranges.

## 6. Verification protocol — mandatory

For every raw URL:
1. Fetch the complete body. A browser preview, snippet, search result, or partial response is not a successful full fetch.
2. For large bodies, retrieve in deterministic chunks. Record each chunk's byte range and continue until EOF. Verify that the assembled UTF-8 byte length matches the actual downloaded body length. Do not assume character count equals byte count.
3. Compute SHA-256 over the exact complete UTF-8 bytes. Compare it with the manifest value where the file has one. Preserve both computed and declared values.
4. Record HTTP status, final URL, fetched bytes, computed SHA-256, declared bytes/hash, match/mismatch, truncation status, and any error.
5. If a tool cannot retrieve a large file, do not pretend it succeeded. Use another supported retrieval method or report failure with the exact URL and needed chunk strategy.
6. For embedded logical sources, use the matching manifest/index mapping: physical bundle, byte_offset, byte_length, expected logical SHA-256, role, and retrieval role. Extract exact byte slices, not approximate character slices. Verify each logical extraction against its own expected SHA-256. Preserve module names and offsets.
7. Never fabricate missing files, fill gaps from general knowledge, or silently substitute another version.

## 7. Known source-index and manifest discrepancies

Keep the following visible in the retrieval report:
- Space manifest: 558 logical-module blocks were parsed from the logical section, while its declared count is 564 (6 discrepancy).
- The Space SOURCE_MANIFEST.json currently enumerates 38 physical files. Its tree sizes match except `06_OTHER_MAIN_CAST(1).md` (manifest 377,983 bytes; tree 378,329 bytes) and `Mana_Character_Source_2.md` (manifest 8,092 bytes; tree 9,195 bytes). The corresponding Space manifest also contains an author-update path/extension discrepancy. Preserve both source metadata and actual tree metadata.
- Older Runeterra index: 477 parsed routes vs manifest declaration 476.
- Eight older index ranges are beyond declared bundle lengths: 3 in `03_INDEX_ROUTING.md`, 5 in `15_SEASON3_PLOTS.md`.
- Twelve older manifest physical-file byte lengths differ from current tree sizes.
- Do not conflate a metadata mismatch with a missing file or a successful hash check. The older Git tree and manifest may represent different snapshots.

## 8. Continuity, authority, and branch separation

### Current Space Saga cursor
- Acts 35–42 are completed.
- Last complete Act: 42, “Fifteen Hundred and Two.”
- Next unfinished Act: 43, “Whose Falcon.”
- Do not replay or redraft Acts 35–42.
- Act 43 prose has not been generated in the current checkpoint.
- Do not PLAY Act 43 unless Kaze explicitly requests PLAY.
- The Act 43 premise includes the interstellar custody hearing for the Millennium Falcon between Han, Lando, and Kaze; Dirk represents both sides; Chris repairs the hyperdrive with possum grease and a hammer. Preserve the exact checkpoint for full detail.

### Older Runeterra/Season 3 cursor — not the Space cursor
- Branch ID: `S3_RESET_CAMPFIRE_CANON_CHRIS_RETOLD_20261017`.
- Older CURRENT.json/DELIVERY_LEDGER.json: Episode 73 delivered provisionally; next Episode 74; acceptance NOT_ASSERTED.
- Do not import E73/E74 into Space Saga.
- Do not treat older branch status as current Space state.

### Future-only planning
- E82–E100 handoff is selected future-development planning only; no manuscript, no PLAY authorization, and no fictional time advanced.
- The 2026-11-05 director's outline is planning material with its own status caveats. Do not assume every item in it is approved/current.
- Do not treat any future plan as an occurred event unless a current checkpoint or explicit author decision confirms it.

### Character Bible approval
- Kaze approved all five tiers and the cross-tier audit.
- Approval does not close any `[OPEN]` field.
- Keep OPEN unknowns open. Do not infer missing ages, heights, histories, powers, motivations, relationships, or outcomes.
- Do not merge distinct people, bodies, branches, or character identities based on superficial similarity.

## 9. Output required from the new AI Studio session

Before doing any creative work, return:
1. A source retrieval ledger for every URL in this document, including full/partial/failure status, bytes, SHA-256, manifest values, and any mismatch.
2. A logical-module extraction ledger from both routing indexes. List all routes, exact bundle, offsets, lengths, hashes, and roles; separately flag count discrepancies and invalid ranges.
3. A branch-separated continuity summary with the Space Saga cursor first and older Runeterra cursor in a clearly separate section.
4. A list of every unresolved `[OPEN]` item, preserving its original wording and source.
5. A concise statement of what is author-approved, what is only selected/planned, what is historical, and what is not authorized.
6. A list of source retrieval failures and exactly what is needed to complete them.

Do not generate an episode, rewrite source files, alter canon, or advance fictional time as part of this retrieval task.

---

# COPY-PASTE BOOTSTRAP PROMPT FOR A FRESH GOOGLE AI STUDIO SESSION

You are taking over the S7NS project from a self-contained source handoff. You have no access to the prior ChatGPT conversation or its memory. Treat the raw URLs in the handoff document as the source inventory, not as optional reading.

FIRST ACTION:
Fetch and read this complete handoff. CRITICAL: every source retrieval target must be the literal plain-text raw.githubusercontent.com URL. Do not use Markdown links, GitHub blob pages, repository pages, shortened links, relative paths, or filenames as substitutes. If a raw URL fails, report it; do not fall back to a normal GitHub URL.

Fetch this complete handoff from:
https://raw.githubusercontent.com/kazekamimp3/s7ns/main/continuity/character_bible/AI_STUDIO_RAW_SOURCE_HANDOFF_20261111.md

Then fetch every raw URL listed in it. Retrieve full bodies, not snippets. For large files, use deterministic chunking to EOF, assemble the exact byte stream, compute UTF-8 byte length and SHA-256, and report all successes, mismatches, truncations, and failures. Use the manifests and routing indexes to extract every embedded logical module by exact byte_offset and byte_length and verify its expected SHA-256. Do not silently omit a URL or logical module.

AUTHORITY AND CONTINUITY:
- The current controlling story branch is S7NS Space Saga. Its checkpoint says Acts 35–42 are complete, Act 42 “Fifteen Hundred and Two” is the last completed act, and Act 43 “Whose Falcon” is next but unfinished.
- Never replay or redraft Acts 35–42. Do not write Act 43 unless Kaze explicitly says PLAY.
- The older Runeterra/Season 3 branch `S3_RESET_CAMPFIRE_CANON_CHRIS_RETOLD_20261017` is separate. Its older ledger says Episode 73 delivered provisionally and Episode 74 next, acceptance NOT_ASSERTED. This is not the Space Saga cursor.
- The E82–E100 handoff and 2026-11-05 director outline are future-planning sources, not proof that those events occurred and not PLAY authorization.
- The five Character Bible tiers and cross-tier audit are author-approved. Preserve every [OPEN] field exactly; approval does not fill gaps.
- Kaze is the final creative authority. Suggestions are not canon until explicitly accepted.

RETRIEVAL AND REASONING RULES:
- Preserve source terminology, organization, chronology, exact names, and branch boundaries.
- Distinguish direct source facts, reasonable inferences, and unresolved gaps.
- Never invent, normalize, silently reconcile, or replace contradictory source content. Report conflicts with exact source locations.
- The Space manifest's 558 parsed logical modules vs 564 declared count, older index's 477 routes vs 476 declared count, eight older out-of-bounds ranges, twelve older manifest/tree size mismatches, and Space bundle metadata discrepancies must be explicitly reported.
- A raw URL existing does not mean its body was fetched. Do not claim full retrieval without a complete body and a recorded byte/hash verification.
- Do not change files, update canon, draft episodes, PLAY, or advance fictional time during the initial source retrieval.

YOUR FIRST DELIVERABLE:
Produce the complete retrieval ledger, all logical-module extraction statuses, branch-separated continuity summary, author-approval/planning status, complete OPEN-field register, and unresolved retrieval failures. Stop there and wait for Kaze's next instruction.
