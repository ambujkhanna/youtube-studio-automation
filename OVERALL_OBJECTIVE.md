# Overall Objective — YouTube Studio Automation

**Last updated:** 2026-10-30T22:37:39+05:30 (2026-10-30T17:07:39Z)
**Status:** Initial baseline; strategy agreed, implementation not yet started.

## Vision
Build a repeatable, low-cost, AI-assisted YouTube content studio for three distinct English-language channels serving a global audience. Automate as much of the lifecycle as practical—from research and ideation through scripting, narration, video assembly, quality checks, metadata, publishing support, and analytics—while retaining human editorial review for the pilot and automated fail-closed quality gates for routine publishing.

The goal is not to mass-produce generic AI content. Each Short should provide original explanation, useful demonstration, meaningful storytelling, or a distinct editorial point of view.

## Planned channels
Launch sequentially, proving the workflow with the first channel before expanding.

| Order | Working name | Theme | Editorial direction |
|---|---|---|---|
| 1 | AImation Studio | AI and technology explained | Practical demonstrations, experiments, workflows, clear explanations |
| 2 | The Hidden Archive | Mystery, history, untold stories | Evidence-led storytelling; distinguish fact, theory, and speculation |
| 3 | StorySprout Studio | Animated storytelling | Original short-form stories, characters, and narratives |

Names are working titles; handle, name, and trademark availability have not been checked.

## Audience and format
- Language: English narration and on-screen text.
- Audience: global from day one.
- Initial format: vertical YouTube Shorts, not 5–15 minute videos.
- Creative mix: screen recordings, animation, and AI-generated visuals where suitable.
- Initial target duration: approximately 30–60 seconds, adapted to the story and platform requirements.
- Launch Channel 1 first; validate the workflow before Channels 2 and 3.

## Time and budget
- Available time: approximately 5–7 hours per week.
- Additional monthly subscription/API budget: ₹0 initially.
- Prefer free, open-source, and local tools.
- Clearly identify paid usage, API credits, subscriptions, usage caps, and trade-offs.
- Do not silently introduce recurring costs.

## Automation objective
Preferred lifecycle:
1. Research topics and trends.
2. Score ideas against channel strategy.
3. Generate hooks, scripts, and storyboards.
4. Verify factual claims and collect sources.
5. Prepare visuals and narration.
6. Assemble vertical video, subtitles, and audio.
7. Run technical and editorial quality checks.
8. Prepare metadata and upload package.
9. Obtain first-pilot approval before enabling unattended publishing.
10. Review analytics and feed learning into future content.

Human involvement should primarily be editorial review, approval, and exceptional decisions—not repetitive editing or copying between tools.

## Success criteria
- A documented, repeatable Shorts production pipeline.
- Minimal manual work while preserving editorial control.
- Initial pilot stays within the zero-additional-subscription-cost constraint, or clearly documents unavoidable costs.
- No fabricated claims, unlicensed media, misleading metadata, or repetitive low-value content.
- Each Short is tracked from idea through publication and performance review.
- Work can resume across ChatGPT conversations using repository documents.
- Channel 1 workflow is reliable before expansion.

## Guardrails
- Do not enable unattended public publishing until the first pilot passes review, the correct destination is verified, and all automated safety/quality gates are working.
- No fabricated sources, quotes, statistics, demonstrations, or analytics.
- Verify factual claims and distinguish facts from theories.
- Respect copyright, music licensing, privacy, platform policies, and applicable AI disclosure requirements.
- Do not optimize views at the expense of accuracy, originality, or viewer value.
- Keep secrets out of the repository.

## Current state
Strategy and broad direction are agreed. Repository documentation is being initialized. Tool selection, skill adaptation, local production setup, and the first end-to-end Short remain to be implemented and tested.


## Background and continuity requirement

This project is a long-running effort to create a sustainable content operation, not a one-off video. The user wants to minimize repetitive manual work through skills, agents, and workflows. A previous long ChatGPT thread reached a conversation-size limit, so the repository must act as the durable source of truth. A new ChatGPT conversation or another AI agent must be able to understand the project without access to the original thread.

## Scope boundaries

**In scope:** channel strategy; topic and trend research; competitor/content-gap analysis; idea scoring; scripts/hooks/storyboards; source collection and fact checking; visual and narration preparation; subtitles; video assembly; technical/editorial QC; metadata; human approval; optional upload/scheduling; analytics; reusable skills, agents, scripts, workflows, and handover documentation.

**Not in the initial scope:** simultaneous launch of all channels; 5–15 minute videos; unattended public publishing; paid subscriptions/API usage without consent; custom video-editor SaaS; copying creators' content; guaranteeing views, subscribers, revenue, virality, or monetization.

## Operating constraints

- User time: approximately 5–7 hours/week.
- Additional recurring budget: ₹0/month initially.
- English narration and on-screen text; global audience.
- Shorts-first, initially around 30–60 seconds.
- Launch Channel 1 and validate the workflow before Channels 2 and 3.
- Human review is mandatory for the first pilot; routine daily publishing is intended to run unattended after validation, with automated fail-closed quality gates.
- The user is technically comfortable with GitHub and software automation. Windows is the selected development platform; exact version and hardware must be confirmed before tool selection.

## Target system principles

Use a shared, channel-agnostic production engine with separate channel configuration for audience, tone, content pillars, voice, visual identity, and editorial rules. Make each stage observable and reproducible. Keep provider-specific integrations replaceable. Record costs, quotas, rights, and limitations. Store source, templates, and documentation in Git; keep secrets and large generated media outside Git.

## Definition of success

A new agent can resume from repository documentation; a complete Short can be produced repeatably; the workflow fits the user's time and budget constraints; factual and copyright checks are recorded; first-pilot editorial approval and automated publishing gates are retained; each Short can be traced from idea to analytics; Channel 1 is reliable before expansion.


**Channel 1 working name update (2026-10-30T22:36:37+05:30 (2026-10-30T17:06:37Z)):** AImation Studio. Treat this as a working name until YouTube name/handle availability and trademark checks are completed. Existing content scope remains practical AI/technology unless the user changes it.


## Latest user decisions — 2026-10-30T22:37:39+05:30 (2026-10-30T17:07:39Z)

- Channel 1 working name is **AImation Studio**. Treat as provisional until YouTube name/handle and trademark checks are completed.
- Development machine/platform is **Windows**. Exact OS version and hardware specifications are still unknown.
- Initial daily publishing target is **7:00 PM IST**, with timing to be optimized later using audience reach and engagement data.
- The user wants routine daily publishing automated after the first end-to-end pilot is validated. The pilot must pass factual, rights, editorial, and technical checks; failed runs must not publish.
- Existing Channel 1 content direction remains practical AI/technology demonstrations and workflows unless the user confirms a narrower AI-animation focus.
