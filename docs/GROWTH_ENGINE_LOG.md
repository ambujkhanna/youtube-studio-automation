# Growth engine: validation log

Moved verbatim from `docs/GROWTH_ENGINE.md` on 2026-11-21 13:04 IST (07:34 UTC) so the design doc stays short. Newest last.

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


## Follow-up operational validation — 2026-11-19

- PR #3's analytics push path filter is merged in both repositories, preventing documentation-only edits from triggering token refreshes.
- Fresh analytics collection is still blocked: the latest post-merge push runs failed in CurioKids (44562221268) and AInation (44562248765). The known OAuth invalid_grant issue remains unresolved. Restore the analytics-only refresh token before treating any report as current; do not modify upload token YT_REFRESH_TOKEN.
- AInation daily run 44562499073 is in progress, but its selected workflow-dispatch inputs are not exposed in the run summary. At the latest check, the run had not reached the read-only growth-brief loader or render/upload step. Because the workflow's default action is Next video (scheduled), do not count this as a safe dry-run without confirming the selected action in GitHub Actions.
- CurioKids post-fix daily dry-run and both channels' post-fix growth-brief summary checks remain outstanding.
- No automatic script rewriting or publishing was introduced. No assistant-initiated video upload or publishing occurred during this audit.


## 2026-11-20 — Current operational status and episode-ID fix

- [x] Investigated Daily Short run 44562499073. It ran with action `Next video (scheduled)`, destination YouTube + Facebook + Instagram, and forced episode input `EP020`. Growth-brief loading succeeded, but rendering stopped before upload because `pick()` compared the uppercase workflow input to lowercase metadata ID `ep020` and raised `StopIteration`. No video was uploaded by this failed run; episode state reported “nothing changed”.
- [x] Fixed forced episode lookup to be case-insensitive and to report a useful error for unknown/ambiguous IDs. Added regression tests in `tests/test_daily.py`. PR #4 merged after CI passed: https://github.com/ambujkhanna/youtube-studio-automation/pull/4; merge commit `5505732787e5148bd9db0fcf4eab9d4aa338cf4b`.
- [x] The Daily Short growth-brief loader completed successfully in run 44562499073. It loaded the latest successful analytics artifact, but that report is stale until a new analytics collection succeeds.
- [ ] Latest scheduled analytics run 44603311245 failed with Google OAuth `invalid_grant` (“Token has been expired or revoked”). Reauthorize and replace only `YT_ANALYTICS_REFRESH_TOKEN`; leave `YT_REFRESH_TOKEN` unchanged.
- [ ] A safe post-fix daily dry-run is still pending. The available GitHub integration does not expose workflow dispatch; use Actions → Daily AInation Short → Run workflow → action `Dry run (render only, nothing uploaded)` and select `EP020` if validating the formerly failing path.
- No publishing behavior, tokens, schedule, or episode-state data was modified by PR #4.


## Analytics token recovery — 2026-11-20

- User clarified that the prior day's update may have replaced the short-lived access token rather than the refresh token. The user then updated `YT_ANALYTICS_REFRESH_TOKEN` in both repositories.
- Re-ran the failed analytics jobs using the current repository secrets. CurioKids run 44606697918 and AInation run 44603311245 both completed successfully.
- Both runs passed analytics unit tests, Google OAuth refresh, read-only collection, channel-specific growth brief generation, and report/database artifact upload. This validates the current analytics refresh-token configuration in both repositories.
- The upload secret `YT_REFRESH_TOKEN` was not changed. Analytics collection is read-only with respect to YouTube publishing; no video was uploaded or published by these retries.
- Remaining separate validation: run each Daily Short workflow with the explicit `Dry run (render only, nothing uploaded)` action and confirm the latest growth brief appears in the Actions summary. Do not select the scheduled/publish default for this check.


## Follow-up validation — 2026-11-20

The newer AInation push-triggered analytics run 44724594920 initially failed with OAuth `invalid_grant` before the user's refresh-token correction. Retry attempt 2 succeeded, including token refresh, analytics collection, growth brief generation, tests and artifact upload. Current analytics refresh-token configuration is validated. The remaining integration check is a safe Daily Short dry-run with `Dry run (render only, nothing uploaded)`; use `EP020` to exercise the recently fixed case-insensitive forced-episode selection. No production publishing action is needed for this validation.


## 2026-11-25 — Shared growth baseline and API metric-gap audit

- Latest retrievable successful artifacts: CurioKids run 44739181837 and AInation run 44724594920, collected 2026-11-20 for 2026-10-21 through 2026-11-17. These are historical, not a fresh baseline.
- CurioKids: 18 video rows, 13 Shorts, 16 mapped (88.9%), 3,004 views and 1,465 engaged views. AInation: 21 rows, 17 Shorts, 19 mapped (90.5%), 919 views and 376 engaged views.
- Current state inventory preview: 33 video IDs per channel. Planner preview: 66 CurioKids assignment rows (11 videos need manual topic review) and 77 AInation rows (5 need manual review). Improve keyword/phrase coverage before treating this as the final owner-facing playlist plan.
- Country-report code exists in the targeted Analytics collector, but retrieved artifacts predate it. Country report needs the English custom-script cohort, supported engaged/subscriber metrics and a correct denominator for country shares.
- Official API audit: thumbnail impressions/CTR are in YouTube Reporting API Reach Basic/Reach Combined; audience-retention curves are supported through single-video Analytics API queries; Shorts Stayed-to-watch is not a standalone targeted API metric and must not be derived from engagedViews.
- Publication-age cohorts require normalized publication timestamps from state plus daily video reports. Per-video subscribersGained must be labelled as watch-page-attributed, not total channel subscriber conversion.
- Fresh analytics collection, CI and render-only workflow checks remain pending. No upload token or publishing behaviour was changed.


## 2026-11-25 — CI validation

- CurioKids growth-engine tests passed in GitHub Actions run 45653482421.
- AInation growth-engine tests passed in run 45653499001 after normalizing topic-filter inputs in `_ok()`.
- Playlist planner taxonomy refinements and regression tests are included in both branches. Current state preview leaves 2 CurioKids and 1 AInation item for manual review.
- Fresh analytics artifact and explicit render-only daily workflow checks remain pending. No PR merged or publishing action dispatched.


## 2026-11-25 — Country report enrichment

The country report now includes engaged views, engaged views/views (not Shorts Stayed to watch), subscribers gained/lost, subscribers gained per 1,000 views, average duration and average viewed percentage. Added custom `script` and explicit `en` language groups. Country share is labelled as a share of returned country rows (up to 200), not asserted to be a perfect global denominator. Unit tests added; CI rerun and live artifact verification pending.


## 2026-11-25 — Country report CI result

The enriched country-report tests passed in CurioKids run 45654199219 and AInation run 45654217704. Live API output still needs verification by manually running the YouTube Analytics workflow on `feat/shared-growth-audit-2026-11`.
