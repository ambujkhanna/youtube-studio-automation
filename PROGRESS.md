# Project Progress

**Last updated:** 2026-11-10T09:20:00+05:30
**Current phase:** Existing production pipelines operational; analytics foundation on feature branch, pending OAuth authorization and CI verification.
**Overall status:** AInation Studio has daily Shorts and weekly long-form automation. A read-only YouTube Analytics collector, report workflow, tests and setup guide have been added to `feat/youtube-growth-engine`; no analytics token has been configured and no live collection has yet been verified.

## Current snapshot (verified 2026-11-10)
- `pipeline/daily.py`, upload/render/QC modules, episode state, and daily/weekly GitHub Actions workflows are present on `main`.
- `pipeline/analytics.py`, `tests/test_analytics.py`, `docs/ANALYTICS.md`, and `.github/workflows/youtube-analytics.yml` are present on `feat/youtube-growth-engine`.
- The analytics workflow is read-only and does not change publishing, upload credentials, or episode state.
- GitHub Actions scheduled workflows only execute from the default branch; the analytics schedule will become active after the feature branch is merged. A manual workflow run can be selected from the branch once GitHub exposes the workflow there.
- Four analytics unit tests passed in GitHub Actions for both repositories on 2026-11-10, including SQLite persistence and CSV/Markdown export coverage. The live API call was intentionally skipped because `YT_ANALYTICS_REFRESH_TOKEN` is not configured. The first live report remains blocked until that secret is configured with `https://www.googleapis.com/auth/youtube.readonly` and YouTube Analytics API is enabled.

## Completed
- [x] Agreed on three channel themes and sequential launch.
- [x] Agreed to start with Shorts rather than 5–15 minute videos.
- [x] Agreed English narration and global audience.
- [x] Agreed on screen recordings, animation, and AI visuals as presentation modes.
- [x] Agreed to minimize manual work using skills, agents, and workflows.
- [x] Agreed on 5–7 hours/week and ₹0 additional monthly subscription budget.
- [x] Identified three candidate YouTube skill repositories for evaluation.
- [x] Agreed GitHub documents will preserve continuity across ChatGPT conversations.
- [x] Created private repository: https://github.com/ambujkhanna/youtube-studio-automation
- [x] Initialized core project documentation.

## In progress
- [x] Add the AImation Studio starter folder, channel configuration, and Windows development guide.
- [ ] Review candidate skills, licenses, and runtime compatibility.
- [x] Select Windows as the development platform.
- [ ] Confirm Windows version and hardware specifications.

## Current blockers and open decisions
- Create a separate read-only OAuth refresh token for AInation Studio using `https://www.googleapis.com/auth/youtube.readonly`; do not replace the upload token.
- Confirm the YouTube Analytics API is enabled in the Google Cloud project.
- Decide whether the SQLite database should remain an Actions cache/artifact or move to a durable private store. The cache is best-effort; each run's artifact is retained for 90 days.
- The new workflow and unit tests have run successfully on the feature branch. The daily schedule will only activate after the feature branch is merged into the default branch.

## Current next actions
1. Configure `YT_ANALYTICS_REFRESH_TOKEN` in repository Actions secrets using the correct AInation Studio Brand Account.
2. Review and run the analytics unit tests on the feature branch or after merging.
3. Run a manual analytics collection for a completed date range and inspect the CSV, Markdown report and SQLite output.
4. Decide on durable analytics retention before relying on long-term trend comparisons.
5. Use the first verified report to establish channel baselines before making content/thumbnail experiments.


## AI concepts script batch — 2026-11-15T18:54:12.898Z
- [x] Added 20 individual AInation Studio custom-script files under `scripts/ai-concepts-*` covering the 20 concepts from the user's Instagram reference image.
- [x] Each file uses the documented custom-script header and DAD/TEEN dialogue format, with title, cover, hashtags, description, tags, title board and picture cues.
- [ ] Dry-run each script through the Daily AInation Short workflow and review the rendered videos before publishing.
- Note: Topics 18 and 20 were partly obscured in the screenshot and were interpreted as Evaluation and AI Agents respectively.

## Update protocol
At the end of every meaningful work session:
- Append a timestamped entry to CONVERSATION.md with new requirements, decisions, outcomes, and rationale.
- Update this file's Last updated, phase, completed/in-progress items, blockers, and next actions.
- Update PLAN.md or OVERALL_OBJECTIVE.md only if their content materially changes; timestamp each updated file.
- Never mark a task complete until repository state or output has been verified.
- Use ISO 8601 timestamps with timezone, e.g. 2026-10-30T22:20:45+05:30.


## Repository update — 2026-10-30T22:22:27+05:30 (2026-10-30T16:52:27Z)
- [x] Updated README.md with the project overview and links to the core documents.
- [x] Created OVERALL_OBJECTIVE.md, PLAN.md, PROGRESS.md, and CONVERSATION.md.
- [x] Read back all five Markdown files from GitHub to verify that the commits are present.
- [ ] Starter channel folders and production implementation remain pending.


## Documentation depth and portability requirement

The user explicitly requires detailed, self-explanatory Markdown documentation so that a fresh ChatGPT conversation or a different AI agent can understand the project's background, scope, constraints, channel strategy, implementation approach, current status, decisions, future scope, and next actions without access to the original conversation. A dedicated AGENT_HANDOVER.md is being added as the entry point.

## Verified vs unverified implementation

**Verified:** private repository exists; GitHub integration has read/write/admin access; README and four core Markdown files were previously committed and read back successfully.

**Not implemented or tested:** production code; agent runtime; installed/adapted skills; Python/FFmpeg pipeline; local TTS; image/video automation; QC scripts; YouTube OAuth/API; first Short; publishing; analytics integration.

Do not mark these items complete based on plans or discussion alone.

## Next actions (ordered)

1. Complete and read back the detailed documentation and AGENT_HANDOVER.md.
2. Add starter channel directories and configuration templates.
3. Inspect candidate skill repositories, licenses, dependencies, runtimes, external services, and cost limits.
4. Confirm the actual target development machine/OS (earlier context mentions Mac M2 but must not be assumed current).
5. Select the smallest viable local toolchain.
6. Create Channel 1 playbook, backlog, and pilot brief.
7. Produce one Short end-to-end; record time, manual interventions, cost, and defects.

## New agent operating requirement

A new agent must read AGENT_HANDOVER.md, OVERALL_OBJECTIVE.md, PLAN.md, PROGRESS.md, and CONVERSATION.md before making changes. It must verify the live repository, avoid asking for already documented details, follow the exact next action in this file, and update timestamped project records after meaningful work.

## New user request — daily end-to-end video automation

**Recorded:** 2026-10-30T22:28:47.380+05:30 (2026-10-30T16:58:47.380Z)

The user explicitly requested that the project now move from planning into implementation, configure an automated daily workflow, generate a video each day, and publish it to YouTube with an appropriate title, description, and hashtags.

This is a new scope requirement. It supersedes the earlier default of requiring approval for every future upload, but does not remove the need to validate the first end-to-end run, authorize the target YouTube channel, and prevent publishing when factual, rights, or technical checks fail.

### Current capability assessment
- No YouTube publishing connector is currently connected/verified in this conversation.
- Plugin discovery surfaced vidIQ (research/idea/analytics assistance), Metricool (social scheduling and supported publishing actions; YouTube write support must be verified before relying on it), Windsor.ai (analytics/data connectors), and Runway (media generation; may involve a separate paid account/credits).
- No tool has yet been authorized to upload to the user's YouTube channel.
- No daily video-rendering workflow, scheduler, OAuth integration, or media-generation pipeline has been implemented.
- A daily schedule cannot be responsibly configured until its execution time is known and a real publishing path is established.

### Immediate prerequisites
1. User to specify daily publishing/run time in India Standard Time (IST).
2. Verify target YouTube channel and obtain authorization through YouTube OAuth or a verified publishing connector.
3. Confirm execution environment and persistent scheduler.
4. Select a zero-cost media generation/narration/rendering path, with limitations recorded.
5. Build and test the first Short end-to-end; only then enable unattended daily publication.

### Next action
Ask the user for the preferred daily run/publish time in IST. In parallel, continue designing the local-first pipeline and verify the safest available YouTube publishing route. Do not claim automatic publishing is configured until an authorized upload test succeeds.


## New user decision — initial daily publishing time

**Recorded:** 2026-10-30T22:33:57+05:30 (2026-10-30T17:03:57Z)

The user selected **7:00 PM IST daily** as the initial publishing target, with a later adjustment based on audience reach. Metricool is connected and reports one YouTube destination; its scheduling interface supports YouTube Shorts metadata. The destination identity still needs to be matched to AImation Studio.

**Verified:** Metricool connection and YouTube destination availability.

**Not implemented:** video generation, renderer, media delivery, persistent daily scheduler, successful upload, and analytics feedback loop. No video has been generated, uploaded, or scheduled. Do not create a recurring task that only wakes ChatGPT but cannot produce and deliver the media.

**Next actions:** verify the destination identity; create Channel 1 configuration; confirm development environment; implement and validate a pilot Short; then activate the 7:00 PM IST daily schedule.


## Channel 1 naming decision — 2026-10-30T22:36:37+05:30 (2026-10-30T17:06:37Z)

- [x] Working name selected: **AImation Studio**.
- [ ] Check YouTube name/handle availability and relevant trademark conflicts before final brand lock.
- [x] Confirm broad AI/technology positioning: AI tools, agents, automation, practical demos, and technology.


## Development environment decision — 2026-10-30T22:37:39+05:30

The user confirmed Windows as the development platform. Exact Windows version and hardware specifications remain unknown and must be checked before selecting local models or GPU-dependent tools. Next: add the AImation Studio channel configuration and a Windows setup guide, then begin the first production-engine phase.


## Starter configuration created — 2026-10-30T22:37:39+05:30 (2026-10-30T17:07:39Z)

Verified on GitHub: `channels/aimation-studio/README.md`, `channels/aimation-studio/channel.config.json`, and `docs/WINDOWS_DEVELOPMENT.md` have been created. These are setup/configuration artifacts only; no renderer or production code exists yet. The channel config intentionally keeps publishing disabled and initial privacy private until the destination and pilot are validated.


## Channel positioning confirmed — 2026-10-30T22:42:04+05:30 (2026-10-30T17:12:04Z)

The user selected option 1: **Broad AI channel**. AImation Studio will cover AI tools, AI agents, automation, practical demonstrations, and technology. It is not an AI-animation-only channel; animation may be used as a visual style. The machine-readable channel configuration and channel brief have been updated to reflect this decision. Name/handle/trademark checks remain pending.


## Current channel strategy

AImation Studio's broad AI/technology positioning is confirmed: AI tools, AI agents, automation, practical demonstrations, real-world use cases, productivity workflows, experiments, and emerging technology explained clearly. It is not an AI-animation-only channel. Animation may be used as a visual technique.


## 2026-10-31T00:20:51+05:30 (2026-10-30T18:50:51Z) — Animation reference accepted; production engine remains blocked

**User decision:** The uploaded 10-second reference is the quality benchmark for AImation Studio. The user explicitly approved the polished 3D CGI character-animation style. Reference properties measured: 720×1280, 24 FPS, 10 seconds. Sampled frames show a detailed classroom, expressive silver robot, school-age boy, teacher/adult characters, scene changes, and character pose changes.

**Acceptance criteria added:**
- Real continuous character and environment movement; expressive gestures/reactions and facial animation.
- Convincing dialogue, separate natural voices, and synchronized lip movement when characters speak.
- Consistent character appearance across shots and episodes.
- Detailed animated environments, purposeful camera/shot changes, and transitions.
- Final target 1080×1920 vertical Shorts.
- Static storyboards, sprite-sheet crops, slideshow cuts, and motion-graphics-only output do not pass.

**Skills status verified:** The three user-shared repositories were fetched and their README/LICENSE files inspected. All three fetched LICENSE files declare MIT. They are external GitHub repositories, not installed skills in this ChatGPT runtime and are not currently executing in the project. Their roles and setup/cost implications are recorded in CONVERSATION.md. No skill installation or adaptation has been completed.

**Current blocker:** No genuine video-generation or rigged-character/lip-sync renderer is available in this ChatGPT session. The requested new sample video has NOT been generated. Do not substitute a static montage. Evaluate a real Windows-compatible animation pipeline and disclose all costs/rights/API constraints before adoption. Preserve ₹0 additional recurring budget unless the user approves a paid option.

**Next actions:**
1. Evaluate the three shared skill repos in detail for useful reusable creator workflow components; keep content strategy/SEO skills separate from the actual animation renderer.
2. Research real 3D/2D character animation and video-generation options that can deliver the approved quality, including consistency, lip-sync, commercial rights, automation, Windows hardware fit, and price.
3. Verify the user's GPU model/VRAM before recommending local rendering/generation.
4. Build a genuine short pilot only after selecting a feasible engine; require user review before public publishing.
5. Continue timestamped CONVERSATION.md and PROGRESS.md updates after each meaningful prompt/work session.

**Verified not done:** no new sample video, no renderer, no automated daily generation, no upload/scheduling, and no change to publishing enablement.


## 2026-10-31T00:40:00+05:30 (2026-10-30T19:10:00Z) — Skills installer prepared; skill-guided pilot script drafted; video render blocked

**User instruction:** Every user conversation turn, including casual or non-productive messages, must be recorded in CONVERSATION.md with a timestamp. Continue this rule without exception while actively maintaining the repository.

### Added to repository
- `scripts/install-youtube-skills.ps1` — Windows installer for the three user-selected GitHub skill repositories.
- `docs/YOUTUBE_SKILLS.md` — installation and usage guide, API/cost notes, verification checklist, and animation quality gate.
- `samples/aimation-studio-pilot-script.md` — skill-guided 40–44 second Alex/Mia Short script about AI agents vs chatbots, with shot plan, metadata, and quality checklist.

### Skill status
- Source directory listings and core skill instructions have been fetched and reviewed.
- Skill workflows were applied to the sample script/metadata package.
- Installer clones the three repositories under `vendor/youtube-skills/`, copies Claude YouTube into `%USERPROFILE%\.claude\skills\youtube`, and copies the other skill folders into project-local `.codex\skills\`.
- **Not yet installed on user's Windows machine:** PowerShell has not been executed from this chat. The installer and instructions are committed, but installation verification requires the user to run it and confirm the expected files / skill discovery.
- ChatGPT hosted runtime cannot load these external skills as native runtime extensions. It can consult their skill instructions when available. Do not misrepresent this.

### Actual video status
No actual sample video has been rendered. No genuine video-generation / rigged-character / lip-sync engine is available in this chat. The pilot script is not a video. Do not generate a static montage and label it animation. Need a real animation renderer and confirmed local GPU/VRAM or a reviewed cloud option. Preserve ₹0 recurring spend unless user approves a paid service.

### Next actions
1. User runs `scripts/install-youtube-skills.ps1` from Windows project root and shares output or errors.
2. Verify the installed folders and agent discovery; then use the installed creator skills for research, script, hooks, packaging, and QC.
3. Confirm GPU model/VRAM.
4. Evaluate real character-animation/video-generation options with commercial rights, lip-sync, API/batch automation, output quality, and cost.
5. Generate and review an actual moving pilot only after the renderer is available; no public publishing before user approval.


## 2026-10-31T01:05:00+05:30 (2026-10-30T19:35:00Z) — Animation engine research complete; no MP4 render yet

### Recommended first test
Autodesk Flow Studio Free, with Blender as a finishing/lip-sync fallback. Research is documented in `docs/ANIMATION_ENGINE_EVALUATION.md`.

- Flow Studio Free: $0, 300 credits/month, one performer at a time, 720p export with watermark.
- Flow Studio Lite: $10/month or $7/month annual billing, two mocap performers and 1080p export without watermark. Do not subscribe without user approval.
- Critical caveat: automatic lip-sync for arbitrary custom 3D characters in Flow Studio's 3D Editor is not explicitly guaranteed by the docs reviewed. Must be demonstrated in a proof before committing.
- Blender Lip Sync extension provides phoneme-based shape-key animation; iClone/AccuLIPS is a higher-cost dedicated fallback; NVIDIA Audio2Face is unsuitable for the current known 8 GB RAM PC unless hardware is upgraded/confirmed.

### Sample render status
**Not generated.** This ChatGPT session has no Flow Studio connector, browser/computer-use control, or video generation tool; cannot sign into the user's Flow Studio account or export an MP4. No static montage will be passed off as animation.

### Next actions
1. User opens https://app.flowstudio.com and uses the free tier to test two characters and an 8–12 second dialogue exchange.
2. Share the exported proof clip here; inspect movement, facial acting, voices, lip-sync, character consistency and export quality.
3. If the free-tier proof passes, user can explicitly approve Lite for 1080p/two-person mocap.
4. If lip-sync fails, test a Blender shape-key workflow or iClone/AccuLIPS before selecting the production stack.
5. No publishing or scheduling until the user approves the actual pilot.


## 2026-10-30T19:18:39.753Z — First no-credit ChatGPT-rendered animation prototype

Rendered a 10-second vertical 720×1280, 24 fps MP4 directly in the hosted execution environment using procedural Python/Pillow animation and FFmpeg. It contains two original stylized 2D characters (Alex and Mia), continuous body movement, blinking, simple arm gestures, alternating mouth motion, animated background accents, and timed captions. No Hansora/Higgsfield/external video-generation credits or user-side installation were used.

**Status: technical prototype only.** It is not 3D animation, has no generated voice audio, and mouth motion is not phoneme-synchronized lip-sync. User review is pending. Do not treat it as approval of production quality. Next: collect user feedback and improve the free procedural approach only if acceptable; paid generation remains disabled without explicit approval.

## 2026-11-01T14:13:11+05:30 (2026-11-01T08:43:11Z) — Claude Code session: zero-cost 3D animation pipeline (in progress)

### Verified in this session
- [x] Free toolchain runs headless on CPU: Blender 5.2.3 (`bpy`), Kokoro-82M text-to-speech, FFmpeg with libass.
- [x] Exact phoneme timings extracted from the Kokoro model for lip-sync.
- [x] 30-second "AI Agents vs Chatbots" dialogue generated with two distinct natural voices.
- [x] Procedural Blender scene built:
  - rigged stylised characters Alex and Mia with lip-sync, blinks, gaze, brows and gestures;
  - an animated lab set and a hologram panel synced to the spoken words;
  - a drone and multi-camera cuts.
- [x] Test frames reviewed. Cycles with denoising chosen over EEVEE.
- [x] Finishing script written: captions, original music and sound effects, 1080×1920 export.
- [x] Low-resolution full-length preview rendered.

### In progress
- [ ] Final full render (more than 2 hours of CPU time, no GPU).
- [ ] Deliver the MP4 for user review.

### Blockers
- The pipeline code exists only in the Claude Code session. It is not committed yet because the session has no push access.
- The reference Short could not be viewed because youtube.com is blocked in the session.
- CPU render time is about 20 s per frame at 720×1280. Daily automation needs a GPU host, a lower resolution or simpler shading.

### Next actions
1. Finish the final render and send the MP4 for review.
2. User decides whether the stylised look is acceptable, or whether better character assets are needed. Licensed rigged models would drop into the same pipeline.
3. Grant write access so the pipeline code (`tts.py`, `scene.py`, `render.py`, `finish.py`) can be committed.
4. Turn the pipeline into a script-in, MP4-out tool for the daily workflow.


## 2026-11-02T23:16:25+05:30 (2026-11-02T17:46:25Z) — Daily automation built (Claude Code session)

- [x] Episode-as-data format (`episodes/<id>/episode.json`) + generic renderer (`pipeline/episode_engine.py`): automatic acting, 8 board-scene templates, automatic camera.
- [x] First backlog written with the public YouTube skills applied: EP002–EP008 (61–68 s each, 1–2 min target): prompts, hallucinations, how ChatGPT works, AI privacy, deepfakes, AI images, everyday AI.
- [x] `pipeline/daily.py`: validate → render → QC (1080×1920, 45–180 s, audio level, captions, metadata) → upload scheduled 19:00 IST → `episodes/state.json`. Fail-closed.
- [x] GitHub Actions workflow `.github/workflows/daily-short.yml` (daily 14:45 IST + manual run; dry-run option; MP4 kept as artifact 14 days).
- [x] Tested end-to-end here in dry-run (EP003 rendered + QC passed). YouTube upload code not testable from the build session (no API access) — first real run will confirm.
- Fixed: `kit2d.py` no longer requires the legacy `char2d` module; `tts.py` writes timing next to itself (`pipeline/build`).

### Next actions
1. Push this update; run the workflow once with **dry_run** and watch the artifact.
2. Do the one-time YouTube OAuth + GitHub secrets (`docs/AUTOMATION_SETUP.md`).
3. First real run; then apply for the YouTube API audit so uploads can go public automatically.
4. Keep ≥7 ready episodes in the backlog (top up weekly).


## 2026-11-03T00:36:22+05:30 (2026-11-02T19:06:22Z) — Backlog: 30 more episodes (EP009–EP038)

- [x] 30 episode files added under `episodes/` (60–70 s each), validated; list in `episodes/BATCH_EP009-EP038.md`.
- Backlog now covers EP002–EP038 = 37 daily Shorts (~5 weeks).
- Next top-up due when ~7 ready episodes remain.


## 2026-11-18T22:04:00+05:30 — Analytics-led growth loop status

- [x] Read-only YouTube Analytics collection verified; latest run #19 completed successfully (GitHub Actions run 44341681018).
- [x] Latest artifact generated (artifact 14443188651); includes CSV, Markdown, SQLite and generated growth brief files.
- [x] Channel-specific growth brief generator and unit tests committed on `feat/youtube-growth-engine`.
- [x] Daily Short workflow updated to retrieve the latest successful analytics artifact and surface the brief in the run summary; advisory only.
- [x] Pull request opened: https://github.com/ambujkhanna/youtube-studio-automation/pull/1
- [ ] Merge blocked: GitHub currently reports PR mergeability as `dirty`; branch is 10 commits ahead and 56 behind `main`. Do not force-merge or overwrite newer main changes.
- [ ] Rebase/sync feature work with current main, resolve conflicts, rerun tests and daily-workflow dry run, then merge only after clean validation.
- Data-quality issue: latest report metadata coverage was 52.6%; repair unknown video/episode mappings before topic-level conclusions.
- Guardrails: no upload credentials, episode queue, publishing settings, schedule, or upload behavior changed. Growth brief does not auto-edit scripts or publish.


## 2026-11-18T22:12:00+05:30 — Latest PR readiness check

- [x] Confirmed `PROGRESS.md`, `CONVERSATION.md`, and `docs/GROWTH_ENGINE.md` are pushed to `feat/youtube-growth-engine`.
- [x] Rechecked PR #1 and branch comparison against `main`.
- [ ] Not ready to merge: PR is open but GitHub reports `mergeable=false`, `mergeable_state=dirty`; branch diverged (13 commits ahead, 56 behind main).
- [ ] Latest analytics workflow run #22 failed at token exchange with Google OAuth `invalid_grant: Token has been expired or revoked`. Artifact upload still ran, but it is not a fresh successful analytics collection.
- Next: user must rotate/reauthorize the AInation analytics refresh token and update only `YT_ANALYTICS_REFRESH_TOKEN` in this repo; do not change upload token. Then sync branch with main, resolve conflicts, run tests and daily-workflow validation, and merge only when clean.


## 2026-11-19 19:18 IST — Post-merge verification

- [x] PR #1 merged into `main` on 2026-11-18; merge commit `97c68a27362c54d0f46b9ca05c24a4a560b9b183`.
- [ ] Latest inspected daily Short workflow run #40 failed before Python dependencies, growth brief loading or rendering: system-package installation timed out after 15 minutes while installing ffmpeg/fonts. Retry/adjust apt installation and validate on a fresh runner.
- [ ] Latest observed analytics workflow run #25 failed with Google OAuth `invalid_grant: Token has been expired or revoked`. Rotate only this repo's `YT_ANALYTICS_REFRESH_TOKEN`; do not change upload token.
- [ ] Growth brief loader has a path bug: downloaded artifact files are nested under an artifact-named directory, but loader checks only `out/analytics/growth_brief.md` at root. Fix with recursive discovery/copy and test.
- [ ] Metadata coverage in last valid analytics report was 52.6%; repair unknown video/episode mappings.
- [ ] After token rotation, run analytics workflow manually and verify fresh CSV/MD/SQLite/growth brief artifact; then run a daily dry-run and confirm brief appears in the Actions summary.
- [ ] Recommendations remain advisory; no automatic script rewrite, upload or publishing changes.


## 2026-11-19 19:35 IST — Retry and integration fixes

- [x] Clarified prior token history: analytics worked in earlier successful feature-branch runs (#19). Subsequent runs #22–#27 repeatedly failed at Google OAuth refresh with `invalid_grant`; this is a new observed failure, not evidence original setup was wrong. Exact cause is not established by logs alone.
- [x] Fixed daily growth-brief loader to search recursively inside downloaded artifact subfolders, then copy Markdown/JSON to a stable path. Commit on main: `33731bfc73b673b463f04338133e589f58ee7e2f`.
- [x] Analytics workflow now triggers on main changes as well as legacy feature branch. Commit: `ffe548e5749322fa380adb95df99426ef7ca2d74`.
- [x] Increased system package installation timeout from 15 to 30 minutes. Commit: `1ca14e41fa03c14e598bca1233fed72fa6b62125`.
- [ ] Retry analytics run #26 still failed with `invalid_grant`; run #27 is still in progress at last check. A fresh analytics-only refresh token is needed if it also fails. Do not change `YT_REFRESH_TOKEN`.
- [ ] Validate loader end-to-end after a fresh successful analytics artifact exists. Daily production workflow was not manually dispatched; no video was published as part of this retry.
- Previous report metadata coverage: 52.6%; repair unmapped episode/video IDs.


## 2026-11-19 Analytics token recovery

- The user replaced the `YT_ANALYTICS_REFRESH_TOKEN` GitHub Actions secret in this repository. The upload secret `YT_REFRESH_TOKEN` was not changed.
- Retried the failed YouTube Analytics workflow (run attempt 2). Google OAuth refresh succeeded; analytics collection, channel-specific growth brief generation, and artifact upload all succeeded.
- Verified 7 analytics/growth unit tests passed in the workflow.
- Successful run: https://github.com/ambujkhanna/youtube-studio-automation/actions/runs/44546163486 (artifact youtube-analytics-30).
- Remaining validation: confirm the next scheduled daily video workflow downloads the analytics artifact and displays the growth brief in its Actions summary. No daily video workflow was manually dispatched and no video was published as part of this recovery.


## 2026-11-19 21:30 IST — Current-main audit

- Re-fetched current `main` files rather than relying on earlier feature-branch or conversation copies.
- Confirmed `.github/workflows/daily-short.yml` includes recursive analytics-artifact discovery/copy and the manual `Dry run (render only, nothing uploaded)` action.
- Confirmed the current Short state file contains 18 distinct video IDs; historical analytics metadata coverage remains 52.6%. Do not guess mappings for older/untracked video IDs.
- Analytics token recovery remains successful (run `44546163486`); the analytics-only token is separate from upload credentials.
- No daily workflow was dispatched in this audit; post-fix end-to-end brief display remains unverified. No upload/publishing settings or episode state were changed.

## 2026-11-19 — Growth report unmapped-video review

- Downloaded and inspected the latest successful analytics artifact. AInation report: 20 rows, 18 mapped (90.0%); two unknown IDs remain: `uhSn_4CVPHQ` (138 views) and `ToSaTHNDoEg` (46 views).
- Added an explicit unmapped-video review list to the growth brief JSON and Markdown. Unknown IDs are linked for manual inspection and are never assigned to episodes automatically.
- Added regression test coverage and a lightweight pull-request unit-test workflow.
- PR #2: https://github.com/ambujkhanna/youtube-studio-automation/pull/2
- Validation/merge: waiting for GitHub Actions PR checks. Daily render-only dry-run remains unverified; no video was uploaded or published.


## 2026-11-19 — Growth review PR #2 merged

- [x] Inspected the latest analytics artifact: 20 rows, 18 mapped (90.0%); unknown IDs `uhSn_4CVPHQ` (138 views) and `ToSaTHNDoEg` (46 views).
- [x] Growth brief now exports unmapped video IDs/views in JSON and a linked Markdown review table; no speculative episode mapping is performed.
- [x] Added regression test and PR-only unit-test workflow. PR #2 merged: https://github.com/ambujkhanna/youtube-studio-automation/pull/2 (merge commit `3ee1e23adf1a66f5661af0a0ee7016e9fe3d58a1`); all PR test runs succeeded.
- [ ] Fresh analytics collection is blocked again: main push run `44561570026` failed with Google OAuth `invalid_grant`. Analytics tests passed; collection failed before growth brief generation. Upload token was not changed.
- [ ] AInation daily workflow has not yet had a post-timeout scheduled run observed; its latest known daily run `44364802528` predates the 30-minute timeout fix.
- [ ] Daily dry-run validation remains pending; no production workflow was dispatched as part of this work.


## 2026-11-19 — Analytics trigger noise reduction

- [x] Merged PR #3: https://github.com/ambujkhanna/youtube-studio-automation/pull/3 (merge commit `50f9031454c08c3ef8024697e9feec000cece90c`).
- Analytics push collection now runs only for analytics code/dependencies/tests, episode metadata state and the analytics workflow itself; documentation-only commits no longer trigger an OAuth refresh.
- Scheduled and manual analytics triggers remain enabled. Daily publishing workflows are unchanged.


## 2026-11-19 — Follow-up audit: current workflow status

- [x] Re-fetched current main versions of all three tracking documents and the Daily Short / analytics workflows before this update.
- [x] Confirmed PR #3's path filter is active; documentation-only commits will not trigger analytics collection. The latest analytics push runs after the merge still failed (CurioKids run 44562221268; AInation run 44562248765) and the earlier OAuth failure pattern remains unresolved. Do not change YT_REFRESH_TOKEN.
- [ ] AInation Daily Short workflow dispatch 44562499073 is currently in progress. GitHub's run summary does not expose the selected action input, so this audit cannot safely classify it as dry-run versus publish. Its job is still at the bounded system-package installation step; analytics brief loading and render/upload have not yet run. Do not infer that it is a safe dry-run.
- [ ] CurioKids daily post-fix dry-run remains unverified; no new CurioKids daily workflow dispatch was found in the latest 10 runs.
- [ ] Need a fresh valid YT_ANALYTICS_REFRESH_TOKEN in each repository, then a successful analytics collection followed by safe daily dry-run(s) to prove the growth brief appears in the Actions summary.
- Guardrails unchanged: no assistant-initiated video upload, publish, schedule change, episode-state edit or upload-token change.


## 2026-11-20 — Current operational status and episode-ID fix

- [x] Investigated Daily Short run 44562499073. It ran with action `Next video (scheduled)`, destination YouTube + Facebook + Instagram, and forced episode input `EP020`. Growth-brief loading succeeded, but rendering stopped before upload because `pick()` compared the uppercase workflow input to lowercase metadata ID `ep020` and raised `StopIteration`. No video was uploaded by this failed run; episode state reported “nothing changed”.
- [x] Fixed forced episode lookup to be case-insensitive and to report a useful error for unknown/ambiguous IDs. Added regression tests in `tests/test_daily.py`. PR #4 merged after CI passed: https://github.com/ambujkhanna/youtube-studio-automation/pull/4; merge commit `5505732787e5148bd9db0fcf4eab9d4aa338cf4b`.
- [x] The Daily Short growth-brief loader completed successfully in run 44562499073. It loaded the latest successful analytics artifact, but that report is stale until a new analytics collection succeeds.
- [ ] Latest scheduled analytics run 44603311245 failed with Google OAuth `invalid_grant` (“Token has been expired or revoked”). Reauthorize and replace only `YT_ANALYTICS_REFRESH_TOKEN`; leave `YT_REFRESH_TOKEN` unchanged.
- [ ] A safe post-fix daily dry-run is still pending. The available GitHub integration does not expose workflow dispatch; use Actions → Daily AInation Short → Run workflow → action `Dry run (render only, nothing uploaded)` and select `EP020` if validating the formerly failing path.
- No publishing behavior, tokens, schedule, or episode-state data was modified by PR #4.


## 2026-11-20 — Analytics refresh-token validation

- [x] User clarified that yesterday's update may have replaced the short-lived access token rather than the refresh token. User has now updated `YT_ANALYTICS_REFRESH_TOKEN` in both repositories.
- [x] Retried the previously failed analytics workflow jobs using the current repository secrets. CurioKids run 44606697918 completed successfully; AInation run 44603311245 completed successfully.
- [x] In both runs, OAuth collection, channel-specific growth brief generation, and report/database artifact upload succeeded. Analytics unit tests also passed. This validates the current analytics refresh tokens in both repositories.
- [ ] Safe Daily Short dry-run remains a separate pending validation; do not use the default scheduled/publish action.
- Upload credential `YT_REFRESH_TOKEN` was not changed. No video was uploaded or published by these analytics retries.


## 2026-11-20 — Follow-up analytics retry

- [x] Rechecked latest analytics runs. AInation push-triggered run 44724594920 had failed with OAuth `invalid_grant` before the user's refresh-token correction.
- [x] Re-ran that workflow (attempt 2) using the current repository secret; OAuth refresh, read-only analytics collection, growth brief generation, tests and artifact upload all completed successfully.
- [x] Together with successful retry 44603311245, this confirms the current AInation analytics refresh token is working. The upload secret `YT_REFRESH_TOKEN` was not changed.
- [ ] Safe Daily Short dry-run remains pending; select only `Dry run (render only, nothing uploaded)`, and for the previous episode-ID regression use `EP020`.


## 2026-11-25 — Shared channel growth audit

- [x] Compared the previous roadmap branch with current `main`: it was diverged and behind (CurioKids by 5 commits; AInation by 3). Created fresh branch `feat/shared-growth-audit-2026-11` from each current `main`; did not force-update the old branch.
- [x] Retrieved the latest available successful analytics artifacts (runs 44739181837 and 44724594920; collected 2026-11-20; report window 2026-10-21 to 2026-11-17). Historical baseline: CurioKids 18 rows / 88.9% metadata coverage / 3,004 views / 1,465 engaged views; AInation 21 rows / 90.5% / 919 views / 376 engaged views.
- [x] Audited current published episode-state inventory: 33 video IDs per channel. Current playlist rules preview: CurioKids 66 assignment rows with 2 manual-topic-review videos; AInation 79 rows with 1 manual-topic-review video.
- [x] Identified and improved narrow planner vocabulary; added regression tests for common on-pillar topics. See `docs/GROWTH_AUDIT_2026-11-25.md`.
- [x] Audited API support: country reports are supported; thumbnail impressions/CTR are available through Reporting API Reach reports; retention curves are available through single-video Analytics API queries; Stayed-to-watch is not a standalone targeted API metric and must not be inferred from engaged views.
- [x] Recorded the owner-supplied top-10 country/language opportunity shortlist as a market reference; the top 3–4 opportunities must be ranked separately per channel from actual YouTube analytics. AInation multilingual production remains out of scope.
- [ ] Obtain fresh analytics artifacts including country/language report and playlist plan; manual workflow dispatch is required.
- [x] Improve planner taxonomy and add regression tests; remaining manual review is 2 CurioKids videos and 1 AInation video.
- [ ] Fix country report language grouping/share denominator and add supported country metrics.
- [ ] Prototype Reporting API Reach Basic and bounded retention collection; preserve publication timestamps for age-matched cohorts.
- [ ] Run PR CI and explicit render-only Daily Short dry-runs in both repositories (AInation EP020). No scheduled/publishing action.

**Safety:** no upload token was touched; no live playlist, video metadata, queue, schedule or publishing behaviour changed. Historical analytics are not presented as current. Work is scoped to shared analytics and recommendations.


## 2026-11-25 — Shared growth CI validation update

- [x] CurioKids growth-engine PR unit tests passed: run 45653482421.
- [x] AInation growth-engine PR unit tests passed after normalizing topic-filter input case: run 45653499001.
- [x] Expanded playlist planner vocabulary and added regression tests for on-pillar topic titles. Current preview leaves 2 CurioKids items and 1 AInation item for manual review.
- [ ] Fresh analytics collection and artifact inspection remain pending.
- [ ] Explicit render-only Daily Short dry-run remains pending in both repos; AInation regression path should use EP020.
- No PR merged. No publishing workflow dispatched. No upload credential or live channel state changed.


## 2026-11-25 — Country report enrichment implemented

- [x] Extended the read-only country report with engaged views, engaged views/views, subscribers gained/lost, subscribers gained per 1,000 views, average view duration and average viewed percentage.
- [x] Added the `script` and `en` language groups so custom English/script uploads are not omitted from the language report.
- [x] Increased country result retrieval to 200 rows and labelled the percentage as share of reported country views; anonymized/unavailable rows may still affect full-global coverage.
- [x] Added unit tests for country aggregation and the custom-script language group. CI rerun pending.
- No OAuth scope or secret changed. No YouTube write API used.


## 2026-11-25 — Country report tests passed

- [x] CurioKids country-report and growth-engine unit tests passed: run 45654199219.
- [x] AInation country-report and growth-engine unit tests passed: run 45654217704.
- [ ] Live analytics artifact verification remains pending; country reporting still requires a manual analytics workflow run on this feature branch.


## 2026-11-25 — Primary-language market focus clarified

- Owner direction: target one primary language per country; do not produce secondary/regional-language variants by default.
- India: Hindi only. Explicitly do not create Tamil, Telugu or Bengali videos.
- United States: English; Indonesia: Indonesian; Brazil: Portuguese; Mexico: Spanish; Japan: Japanese; Germany: German; Vietnam: Vietnamese; Philippines: Filipino/Tagalog; Turkey: Turkish.
- CurioKids retains its existing English/Hindi/Spanish library; any additional language requires owner approval and channel analytics evidence.
- AInation remains English-only; multilingual production is outside current scope.
- Updated growth roadmap, country/language audit, TODO and progress tracking. Analytics can still report audiences in other languages; reporting does not imply production approval.
