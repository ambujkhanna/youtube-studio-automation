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

## Current status (2026-11-21 13:04 IST)

- Analytics collection works in both repos with the analytics-only refresh token (`YT_ANALYTICS_REFRESH_TOKEN`); the upload token is separate and untouched.
- The daily workflow loads the latest brief into its run summary. The step is optional (`continue-on-error`, 5-minute limit): a GitHub API problem there never stops a video.
- Open check: one daily **Dry run** that shows the brief in its summary.
- Dated validation notes are kept in `docs/GROWTH_ENGINE_LOG.md`; status changes go to the channel handoff's change log.


## Editorial topic gate and playlist model (2026-11-25)

Search/radar output is a discovery input only. Before a topic enters a recommendation or episode backlog, it must clearly fit one of AInation's six AI pillars and suit the practical Dad–Teen explainer format. Reject unrelated finance/market stories (such as gold-price movements), general news, gossip and off-pillar trends; do not force an AI angle onto an unrelated topic. Search volume never overrides channel fit.

Playlist organisation is multi-dimensional: each upload can be in a topic playlist and its spoken-language playlist for languages the channel actually publishes, plus a series playlist where useful. One upload can appear in multiple playlists; do not duplicate uploads. Do not create empty language playlists for languages not published.

## Channel growth roadmap (2026-11-25)

The channel-specific approved plan is in [`docs/GROWTH_ROADMAP.md`](GROWTH_ROADMAP.md). It extends the existing analytics-led learning loop; it does not replace it.

AInation priorities: demonstration-first Dad–Teen hook; practical AI topic pillars; clear tool demos and verified limitations; Shorts-to-tutorial connections; playlists and Instagram profile alignment. Multilingual expansion is out of scope.

### Delivery sequence
1. Baseline and data quality (metadata coverage, metric availability, Shorts/long-form and publication-age cohorts).
2. Analytics gap investigation: impressions/CTR where eligible, Shorts Stayed to watch where accessible, audience-retention curve availability.
3. Advisory content intelligence: topic pillars, hook/first-frame/visual progression/payoff/factual checks, historical opportunities.
4. Channel-specific workstreams and owner-reviewed packaging/link recommendations.
5. Unit/sample-data tests, read-only analytics validation and explicit render-only dry-runs.

### Non-negotiable guardrails
- Analytics-only OAuth remains read-only; upload credentials are not touched.
- Growth recommendations never automatically edit scripts, titles, thumbnails, queues, schedules or published videos.
- No publishing workflow dispatch for validation. Use render-only dry-runs.
- CurioKids must respect Made for Kids restrictions; do not rely on comments, cards, end screens or viewer playlist-saving.
- Establish baselines before numerical targets. Missing API metrics are reported as unavailable, never fabricated.
