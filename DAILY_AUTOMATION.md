# Daily Shorts Automation — Requirements and Runbook

**Last updated:** 2026-10-30T22:37:39+05:30 (2026-10-30T17:07:39Z)
**Status:** Requirements recorded; implementation and authorization pending.

## Goal

Generate and publish one original YouTube Short per day for Channel 1 (AI in Action Lab, working title), with a suitable title, description, hashtags, and metadata. Later, the same shared engine may serve the other channels after their launch gates.

## Daily run outline

1. Read channel configuration and publishing rules.
2. Check the content backlog and recent publication history to avoid duplicates.
3. Research a suitable topic and collect reliable sources.
4. Score the idea and draft a hook/script.
5. Verify claims and flag uncertainty.
6. Create storyboard and scene/asset plan.
7. Prepare visuals, narration, captions, and licensed audio.
8. Render a vertical Short.
9. Run technical and editorial QC.
10. Generate title, description, relevant hashtags, and metadata.
11. Upload only through an authorized YouTube publishing integration/API.
12. Verify upload status and store the resulting URL and run record.
13. Update analytics/performance record when data becomes available.

## Fail-safe behavior

Do not publish if the script contains unverified factual claims, assets have unclear rights, the render fails QC, subtitles/audio are defective, the video is a duplicate, metadata is misleading, or upload authorization is missing. Save the failed run details and notify the user instead.

## Prerequisites

- User-selected daily run/publish time and timezone.
- Target YouTube channel identity and OAuth authorization or verified publishing connector.
- Persistent execution host/scheduler.
- Working topic research, script, fact-check, narration, visual, render, and QC components.
- Cost-free/approved media-generation and TTS strategy.
- First end-to-end pilot reviewed and validated.
- Secure secret storage outside Git.

## Important limitations

A recurring ChatGPT task does not itself run arbitrary local code or guarantee YouTube upload. A GitHub repository is source control, not a continuously running renderer. GitHub Actions or another execution host must be explicitly configured, tested, and assessed for runner limits, storage, secrets, and cost. ChatGPT subscription does not imply free API usage. Do not promise unattended generation or publishing until all components have been tested.

## User-approved publishing scope

The user has explicitly requested daily automatic publishing. Implement toward that goal. The first end-to-end pilot remains a validation gate; once successful, configure recurring unattended publishing only after the user has authorized the target channel and the schedule is confirmed.

## Current state

No renderer, scheduler, OAuth integration, or successful upload exists yet. The preferred daily run time is not yet specified.


## Latest decision — initial publishing time

**Recorded:** 2026-10-30T22:33:57+05:30 (2026-10-30T17:03:57Z)

- Initial target: **daily at 7:00 PM IST**.
- Timezone: Asia/Kolkata / Asia/Calcutta.
- Review actual audience reach, views, retention, and engagement before changing the time.
- Metricool is connected and one YouTube destination is visible. Verify that destination is AI in Action Lab before first public publishing.
- Metricool accepts an actual video file or accessible media URL; it does not generate the video. No renderer, media delivery path, daily scheduler, or successful upload exists yet.
- Do not activate recurring unattended publishing until the first end-to-end pilot passes QC and the target channel is verified.


## Development environment decision — 2026-10-30T22:37:39+05:30 (2026-10-30T17:07:39Z)

Windows is the confirmed development platform. Exact Windows version and hardware remain to be confirmed. Build the initial implementation to be Windows-compatible; do not assume GPU acceleration or a particular device configuration.
