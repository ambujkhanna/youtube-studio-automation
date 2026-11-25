# AInation Studio — channel growth roadmap

**Status:** implemented on the shared feature branch; analytics artifacts and CI validated. Reach API enablement and render-only visual checks remain pending.  
**Updated:** 2026-11-25  
**Scope:** AInation Studio only. Multilingual expansion is not part of this plan.

## Channel promise

Practical, understandable AI explained through the established Dad–Teen format. Prioritise useful demonstrations, honest limitations, safety/privacy and workflows viewers can verify. Preserve the existing no-intro-on-Shorts decision: show the topic/problem from frame 0.

## Priority workstreams

### 1. First seconds and retention — highest priority
- Start with the concrete problem, surprising output or before/after result; avoid generic AI hype and greetings.
- Show the AI result early, then explain how it was produced and what needs human verification.
- Use screen recordings, readable captions, practical demonstrations and purposeful visual changes. Do not add cuts solely to satisfy a fixed seconds-per-shot rule.
- Keep the Dad–Teen dialogue natural and globally understandable; test concise openings and the previously discussed 40–55-second experiment as an experiment, not a permanent duration rule.
- Test a natural callback/loop only when it fits the explanation. Never sacrifice clarity for replay manipulation.

### 2. Topic pillars and search demand
- Core pillars: AI Explained; AI Tools & Practical Workflows; AI Coding/Building; AI Creativity; AI in Everyday Life; AI Safety, Privacy & Verification.
- Cover current models/tools when there is a practical audience problem or meaningful capability change.
- Prioritise evergreen questions alongside timely developments; verify current product claims, pricing, availability and limitations before scripting.
- Search trends are discovery signals, not automatic episode ideas. Every candidate must pass a strict AInation channel-fit gate: it must clearly serve one of the six AI pillars and suit the practical, understandable Dad–Teen explainer format.
- Reject unrelated finance/market news (for example, why gold prices are dropping), celebrity gossip, generic politics, unrelated gadgets and broad news stories. Do not force an AI angle onto a topic that does not naturally belong.
- Generic phone launches and gadgets are off-pillar unless there is a meaningful AI-specific capability or workflow to demonstrate.
- Use search/radar and channel performance only after channel fit is established; high search volume alone never overrides the channel promise. Label untested topic clusters as hypotheses.

### 3. Shorts-to-long-form and playlists
- Identify Shorts with matching full tutorials, demos or projects and recommend a Related Video link where eligible.
- Use two complementary playlist dimensions: **topic playlists** (AI basics, tools/workflows, coding/building, creativity, everyday AI, safety/privacy) and **language playlists** for each language actually published.
- A single video may belong to multiple playlists. Add it to its relevant topic playlist and its language playlist; use a focused series playlist as a third dimension when it helps viewers follow a learning path.
- Do not create empty language playlists for languages the channel does not publish. Keep playlist names and descriptions clear about the language of the videos.
- Build connected learning paths (beginner → practical example → deeper tutorial) where the library supports them.

### 4. Instagram discovery bridge
- Align the Instagram bio with the actual Dad–Teen AI-explainer show and practical AI content.
- Put the direct AInation YouTube channel link in the bio and use a clear link-in-bio CTA.
- Use specific links to matching tutorials or series when available; avoid vague manual-search instructions.

### 5. Historical optimisation
- Identify videos with strong retention/engaged views but weak discovery; investigate topic packaging and distribution.
- Review title/thumbnail for eligible long-form videos with meaningful impressions and weak CTR. Do not apply classic thumbnail CTR logic to Shorts-feed views.
- Identify strong search performers and create useful follow-ups rather than duplicating the same explanation.
- Review high-view/low-retention videos for weak hooks, overlong setup, unclear demos or unsupported promises.
- Require owner approval before changing published metadata; no automatic repackaging.

### 6. Trust and demonstration quality
- Show the actual tool/output where possible and disclose the model/tool/version when relevant.
- Verify claims, dates, prices, availability and privacy/security implications before publishing.
- Include limitations, failure cases and human verification; never imply AI is infallible.
- Maintain consistent Dad–Teen character presentation, readable screen content and clear before/after storytelling.

### 7. Language policy
- Keep AInation English-only. Do not introduce multilingual production or new language tracks as part of this roadmap.
- If the owner later approves a market expansion, target one primary language per country (for example, Hindi for India, English for the United States and Indonesian for Indonesia); do not create secondary/regional-language variants by default.
- Revisit only if the owner requests it and audience evidence supports a separate decision.

## Experiments and measures

- Opening: compare Stayed to watch / Viewed vs. swiped away and early retention where available.
- Demonstration-first format: compare engaged views, average duration and average percentage viewed across similar topics and durations.
- Duration: test the 40–55-second format against comparable episodes; do not assume shorter is always better.
- Topic pillars: compare topic-level engagement and subscriber conversion only after metadata coverage is sufficient.
- Long-form packaging: use impressions CTR and watch-time context where available; avoid judging by CTR alone.

## Measurement rules (both channels)

- Establish a fresh baseline from the latest successful YouTube Analytics report before setting numerical targets.
- Compare Shorts with Shorts and long-form with long-form; compare videos at similar publication ages and report windows.
- Keep public views, engaged views, average view duration and average percentage viewed distinct. For Shorts, use **Stayed to watch / Viewed vs. swiped away** when the relevant report is available.
- Use impressions and impressions CTR for eligible long-form/discovery surfaces where YouTube reports them; do not treat CTR as a Shorts-feed metric.
- Segment by language, format, topic pillar and episode age only when the source data supports that segmentation.
- Label small samples and missing metrics. No causal claims from simple correlations; no guessed video-to-episode mappings.
- Track subscribers gained per 1,000 views, returning viewers, search traffic and (where available) traffic from Shorts to related long-form videos.
- A recommendation is advisory until a human reviews it. Never auto-rewrite scripts, titles, thumbnails, queues, schedules or publishing state.

## Shared execution phases

1. **Baseline and data quality:** refresh analytics, map videos to episodes, report coverage, identify missing dimensions and API limitations.
2. **Content intelligence:** topic pillars, search demand, channel-fit checks, historical opportunities and format/age-aware comparisons.
3. **Creative quality:** first-frame, opening hook, visual progression, explanation/payoff, ending and factual/editorial checks.
4. **Packaging and connections:** title/thumbnail review where applicable, playlists, related-video candidates and Instagram profile/link review.
5. **Validation:** unit tests, sample-data tests, read-only analytics run, report inspection and safe render-only dry-run.
6. **Measured experiments:** change one creative variable at a time where practical; compare a suitable baseline and record the result before making it a standing rule.

## Safety and scope

- Analytics remains read-only and uses the analytics-only OAuth credential. Do not touch upload credentials.
- No publishing, visibility, schedule, queue or live metadata changes are part of this roadmap.
- Do not dispatch a publishing workflow to validate growth work. Use explicitly labelled render-only/dry-run actions.
- Respect Made for Kids restrictions. Do not depend on comments, cards, end screens, notifications or viewer playlist-saving features where YouTube disables them. Channel-owned playlists may still be curated and measured where reporting permits.
- Prefer free/open tooling already in the repositories. No paid SEO service is required for this roadmap.


## Acceptance gates

- No multilingual expansion in this workstream.
- No unsupported AI claims or unverified tool/pricing statements.
- No automatic changes to published videos, episode queues, publishing schedules or channel settings.
- First deliverable is a data-quality-aware growth report; later implementation can add metrics and checks incrementally.


## Analytics implementation update — 2026-11-25

- Country reports include supported engaged-view and subscriber metrics and are grouped by published language version. The market-opportunity report ranks target countries by actual returned views and distinguishes localized-language evidence from all-language country totals.
- The owner language policy is enforced in recommendations: India = Hindi only (no Tamil, Telugu or Bengali); CurioKids retains existing English/Hindi/Spanish; AInation remains English-only.
- The analytics collector now preserves publish timestamps from episode state (scheduled publish time preferred; upload time is a fallback), produces complete 7/14/28-day age-matched cohorts for the top 20 videos, and requests audience-retention curves for the top 10 videos.
- A YouTube Reporting API Reach Basic collector captures thumbnail impressions and CTR. The workflow ensures a daily Reach Basic job exists; reports may take up to 24 hours after job creation to appear.
- CI has passed for the analytics, market-opportunity and Reach API parsing tests. Fresh artifact/runtime verification is tracked separately; render-only video checks remain owner validation tasks.


## Fresh data checkpoint — 2026-11-25

The first live feature-branch analytics artifacts were generated for 2026-10-26 to 2026-11-22. CurioKids returned 25 per-video rows (3,247 views; 1,559 engaged views); AInation returned 28 rows (1,100 views; 443 engaged views). Country reports, review-only playlist plans, retention curves and age cohorts were generated. Country metrics cover returned rows only and may be anonymized; they are not a full-global denominator. The Reach Basic Reporting API is currently disabled in the shared Google Cloud project 702229494667, so thumbnail impressions/CTR remain blocked until the owner enables that API. See the audit for the data observations and exact run links.


## Topic-level performance implementation — 2026-11-25

Growth briefs now group analytics by the channel-specific topic taxonomy and format (Shorts vs long-form), including video count, views, engaged views, engaged-view rate, weighted average viewed percentage and subscribers per 1,000 views. A video may match more than one topic; unmatched titles remain manual review and are not guessed. If Reach Basic is available, the same brief adds long-form thumbnail impressions and CTR for packaging review; Shorts-feed swipe behaviour is never inferred from CTR.
