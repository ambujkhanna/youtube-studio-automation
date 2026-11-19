# Analytics-led growth loop

**Last updated:** 2026-11-18T21:50:00+05:30

## What the automation does

1. The read-only analytics workflow fetches per-video views, engaged views, watch time, average view duration, average viewed percentage, likes, comments, shares, and subscriber gains/losses.
2. It exports CSV, Markdown and SQLite, then runs `pipeline/growth.py` to create `growth_brief.md` and `growth_brief.json`.
3. The analytics artifact retains those files for 90 days.
4. The daily Short workflow downloads the latest successful analytics artifact, if one exists, and places the growth brief in that run's GitHub Actions summary for editorial use.

## Editorial use

Use the latest growth brief when selecting and drafting the next episodes. Treat its ranked videos and guidance as directional evidence, not causal proof. Compare like formats and similar publication ages. Repair unknown episode mappings before making topic-level decisions.

Channel-specific guidance is embedded in `pipeline/growth.py`:
- CurioKids: curiosity-led child-friendly questions, immediate visual/verbal hooks, one clear concept, accessible vocabulary and a satisfying answer.
- AInation: practical AI use and safety, concrete problem/outcome openings, demonstrations, and explicit limitations/verification.

## Guardrails and limitations

- Analytics uses a separate read-only refresh token; upload credentials and publishing behavior are unchanged.
- The growth brief is advisory. It does not rewrite queued episode JSON, change titles, alter schedules, upload videos, or publish automatically.
- Current reports do not include impressions, CTR or audience-retention curves.
- Unknown metadata remains visible and lowers the metadata-coverage score; no titles or episode IDs are guessed.
- Keep analytics reports in Actions artifacts; do not commit private performance snapshots to the public repository.

## Validation

Run locally:
```bash
PYTHONPATH=pipeline python -m unittest discover -s tests -v
python pipeline/growth.py --csv out/analytics/<report>.csv --channel-key CHANNEL_KEY
```


## Live validation snapshot — 2026-11-18 22:04 IST

- Latest analytics collection on this feature branch completed successfully and uploaded its report artifact.
- Latest observed episode/video metadata coverage: **52.6%**. The growth brief flags unknown mappings; resolve these before relying on topic-level rankings.
- The PR to `main` remains open and currently has merge conflicts (`mergeable_state=dirty`). Synchronize with current `main`, resolve conflicts and revalidate before merging. No force merge.
- Daily-workflow integration has been committed, but it is advisory: it surfaces the brief in the Actions summary and does not alter scripts or publishing.


## Post-merge audit — 2026-11-19 19:18 IST

PR #1 is merged to `main`. Latest inspected daily workflow run #40 failed before growth-brief loading or rendering because the apt package installation step timed out after 15 minutes. This is an environment/package-install blocker, not yet evidence of a growth-brief code failure. Retry with more resilient installation or runner preinstalled dependencies.

Latest observed analytics run #25 failed with Google OAuth `invalid_grant`; refresh the analytics-only token. The daily loader also needs recursive discovery because artifact downloads are nested under an artifact-named directory, while the current check expects the file at the output root. After fixes, manually validate fresh analytics collection and daily dry-run. Previous valid report metadata coverage: 52.6%. Recommendations remain advisory.


## Retry fixes — 2026-11-19 19:35 IST

The analytics token worked in earlier successful runs, but later retries fail with OAuth `invalid_grant`. Root cause is not conclusively identifiable from logs. A new analytics-only refresh token may be required to restore collection; upload token is separate and must remain untouched.

Daily workflow artifact loader now recursively locates the growth brief in the downloaded artifact directory tree and copies the MD/JSON pair into `out/analytics`. Analytics workflow push trigger includes main. Daily system package installation timeout increased to 30 minutes. End-to-end loader validation remains pending until a fresh successful analytics artifact is produced.


## 2026-11-19 Analytics token recovery

- The user replaced the `YT_ANALYTICS_REFRESH_TOKEN` GitHub Actions secret in this repository. The upload secret `YT_REFRESH_TOKEN` was not changed.
- Retried the failed YouTube Analytics workflow (run attempt 2). Google OAuth refresh succeeded; analytics collection, channel-specific growth brief generation, and artifact upload all succeeded.
- Verified 7 analytics/growth unit tests passed in the workflow.
- Successful run: https://github.com/ambujkhanna/youtube-studio-automation/actions/runs/44546163486 (artifact youtube-analytics-30).
- Remaining validation: confirm the next scheduled daily video workflow downloads the analytics artifact and displays the growth brief in its Actions summary. No daily video workflow was manually dispatched and no video was published as part of this recovery.


## Current-main audit — 2026-11-19 21:30 IST

- The current Daily Short workflow contains recursive discovery of `growth_brief.md` in the downloaded analytics artifact and copies the Markdown/JSON pair to the stable output path.
- The workflow offers a manual `Dry run (render only, nothing uploaded)` action. End-to-end confirmation that the brief appears in the Actions summary is still pending.
- The latest known metadata coverage is 52.6%; the current Short state file contains 18 distinct video IDs. Do not invent mappings for videos absent from state.
- Analytics token recovery succeeded in run `44546163486`; upload credentials remain separate and unchanged.
- No production workflow was dispatched and no video was uploaded or published during this audit.

## 2026-11-19 — Unmapped-video audit

The latest inspected analytics artifact contains 20 rows, 18 mapped (90.0%). Unknown IDs: `uhSn_4CVPHQ` (138 views) and `ToSaTHNDoEg` (46 views). These are surfaced in the growth brief for manual review; the system deliberately does not guess episode IDs. PR #2 adds this output and regression coverage: https://github.com/ambujkhanna/youtube-studio-automation/pull/2.


## 2026-11-19 — Unmapped review and validation status

PR #2 is merged to main (`3ee1e23adf1a66f5661af0a0ee7016e9fe3d58a1`). Growth briefs now list unknown video IDs and views in JSON and Markdown, linking to the video for manual verification. Latest artifact: 20 rows, 18 mapped (90.0%); unresolved: `uhSn_4CVPHQ` (138 views), `ToSaTHNDoEg` (46 views).

PR unit tests passed. A subsequent main analytics collection failed with `invalid_grant` (run `44561570026`), so no fresh growth brief was generated. The AInation daily workflow still needs a post-timeout validation run. Do not infer mappings or modify upload credentials.


## 2026-11-19 — Trigger scope

PR #3 merged (`50f9031454c08c3ef8024697e9feec000cece90c`). Push-triggered analytics collection is limited to analytics source/dependencies/tests, episode metadata state and the analytics workflow. Documentation-only commits no longer consume refresh-token attempts. Scheduled and manual analytics runs remain enabled.
