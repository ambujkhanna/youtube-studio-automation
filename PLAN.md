# Project Plan — YouTube Studio Automation

**Last updated:** 2026-10-30T22:28:47.380+05:30 (2026-10-30T16:58:47.380Z)
**Plan status:** Baseline agreed; detailed implementation decisions remain open.

## Guiding approach
Build one end-to-end Shorts pipeline for AI in Action Lab before scaling. Use modular skills and scripts that can be reused with channel-specific configuration. Keep the first version local and low-cost; add external services only to solve a demonstrated capability gap.

## Phase 0 — Foundation and decisions
- [x] Confirm three-channel concept and sequential launch.
- [x] Confirm Shorts-first approach.
- [x] Confirm English narration and global audience.
- [x] Confirm 5–7 hours/week and ₹0 additional monthly subscription budget.
- [x] Create repository and core project documentation.
- [ ] Add channel configuration and brand guideline templates.
- [ ] Confirm development machine and operating environment.
- [ ] Review candidate YouTube skills and licenses before adapting material.

**Exit criteria:** Decisions and repository conventions documented; implementation environment known.

## Phase 1 — Channel 1 strategy and content system
- [ ] Finalize positioning, audience promise, tone, and visual identity.
- [ ] Define content pillars and repeatable Short formats.
- [ ] Define idea scoring: relevance, hook, originality, evidence, production effort, series potential.
- [ ] Build a prioritized initial idea backlog.
- [ ] Define 30–60 second script and storyboard templates.
- [ ] Select and approve the first pilot topic.

**Exit criteria:** Channel playbook and approved pilot brief.

## Phase 2 — Skills and agent workflow
Design composable capabilities: trend/topic researcher; competitor and content-gap researcher; idea evaluator; Short-form script and hook writer; fact checker/source collector; visual director/storyboard writer; narration and subtitle preparer; video assembly orchestrator; quality-control reviewer; metadata and analytics assistant.

For each skill, define inputs, outputs, constraints, tools, and human approval points. Evaluate the user-provided candidate repositories:
- https://github.com/agricidaniel/claude-youtube
- https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill
- https://github.com/ZeroPointRepo/youtube-skills

These are candidates, not approved dependencies. Inspect licenses, runtime compatibility, dependencies, external services, API keys, free-tier limits, and maintenance. Do not assume a skill for Claude Code, Codex, or another Agent Skills runtime executes natively inside an ordinary ChatGPT conversation.

**Exit criteria:** Minimal tested skill set that takes a topic brief to a review-ready production package.

## Phase 3 — Local production engine
Evaluate a low-cost/local toolchain:
- Python for orchestration and file management.
- FFmpeg for vertical assembly, audio mixing, transitions, and subtitles.
- Local text-to-speech where quality and licensing are acceptable.
- Reusable visual templates, screen recordings, and approved assets.
- Automated checks for dimensions, duration, audio, subtitle timing, blank frames, and output integrity.

ChatGPT subscription access does not automatically provide API access or free API credits to local scripts. Automated image/video generation may require paid APIs or local models/hardware. Treat interactive ChatGPT asset creation as assisted, not unattended, until a supported route is tested.

**Exit criteria:** A repeatable workflow produces a playable, technically validated Short from approved inputs.

## Phase 4 — Pilot Short and quality review
- [ ] Generate pilot brief, script, sources, storyboard, and asset plan.
- [ ] Produce narration and visual assets.
- [ ] Render the Short in vertical format.
- [ ] Review accuracy, originality, pacing, audio, subtitles, accessibility, and rights.
- [ ] Revise and approve final render.
- [ ] Record production time and manual intervention points.

**Exit criteria:** One publish-ready pilot and documented production run.

## Phase 5 — Publishing and analytics
- [ ] Decide whether YouTube Data API upload is needed.
- [ ] If used, implement OAuth securely and keep credentials outside Git.
- [ ] Prepare title, description, hashtags, cover strategy, and metadata.
- [ ] Require human confirmation before public upload/scheduling.
- [ ] Record publication URL and performance metrics.
- [ ] Feed analytics and qualitative review into future ideas.

**Exit criteria:** Safe publishing workflow and basic feedback loop.

## Phase 6 — Consistent Channel 1 operation
- [ ] Establish a sustainable cadence, initially aiming for about 2–3 Shorts/week once the pilot workflow is stable.
- [ ] Batch research and production to fit 5–7 hours/week.
- [ ] Review quality and analytics regularly.
- [ ] Automate stable, repeatable steps and remove bottlenecks.

**Exit criteria:** Manageable production rhythm with documented quality standards.

## Phase 7 — Expand to Channels 2 and 3
- [ ] Create channel-specific configurations and editorial guardrails.
- [ ] Adapt research/fact-checking for history and mystery.
- [ ] Design original character/story workflows for animation.
- [ ] Reuse shared production engine while keeping brands and assets distinct.
- [ ] Launch each channel after its workflow passes a pilot.

**Exit criteria:** Three distinct channel workflows on a maintainable shared foundation.

## Proposed repository structure
```text
youtube-studio-automation/
├── README.md
├── OVERALL_OBJECTIVE.md
├── PLAN.md
├── PROGRESS.md
├── CONVERSATION.md
├── channels/
│   ├── ai-in-action-lab/
│   ├── hidden-archive/
│   └── storysprout-studio/
├── skills/
│   ├── research/ ├── ideation/ ├── scripting/
│   ├── fact-check/ ├── visuals/ ├── voice/
│   ├── production/ ├── publishing/ └── analytics/
├── agents/
├── workflows/
├── scripts/
├── templates/
└── production/  # generated media should generally stay out of Git
```

## Definition of done for each Short
A video file alone is not completion. Record the topic and intended audience; approved hook and script; source references for factual claims; storyboard and asset provenance/rights; narration and subtitles; rendered video and technical QC result; human editorial approval; metadata and publishing status; and performance review when analytics are available.

## Risks and mitigations
| Risk | Mitigation |
|---|---|
| API or tool introduces recurring cost | Maintain cost/limits register; default to local/free options |
| ChatGPT thread reaches context limit | Use repository as source of truth; resume in a new chat from project docs |
| Skills are runtime-specific | Verify compatibility and adapt rather than assuming portability |
| AI output is repetitive or low-value | Require original insight, demonstrations, evidence, and review |
| Factual or copyright issues | Fact-check claims and document asset provenance |
| Automation publishes an error | Human approval gate before public publishing |
| Scope expands too early | Prove Channel 1 before reusing pipeline for others |

## Change control
Update this plan when scope, architecture, phase order, or milestones materially change. Add a timestamp whenever this file changes. Record decisions and rationale in CONVERSATION.md and reflect resulting work in PROGRESS.md.


## Target architecture and content lifecycle

The intended shared pipeline is:

`Research → Idea scoring → Script/hook → Fact check → Storyboard → Visuals/narration → Video assembly → QC → Metadata → Human approval → Publish → Analytics`

Suggested content states:
`IDEA → RESEARCHED → SELECTED → SCRIPT_DRAFT → FACT_CHECKED → STORYBOARDED → ASSETS_READY → RENDERED → QC_PASSED → HUMAN_APPROVED → PUBLISH_READY → PUBLISHED → ANALYZED`

Include explicit rework/failure states such as `NEEDS_RESEARCH`, `FACT_CHECK_FAILED`, `QC_FAILED`, and `REJECTED`. Failed or unapproved content must never advance to publishing.

### Component responsibilities

- **Channel configuration:** audience, promise, tone, language, content pillars, visual identity, voice, editorial constraints.
- **Orchestrator:** advances a content item through explicit states; records inputs, outputs, errors, and approvals.
- **Research/ideation skills:** collect sources, identify trends and gaps, score ideas without copying competitors.
- **Script/fact-check skills:** draft hooks and narration; map factual claims to sources; flag uncertainty.
- **Visual/voice skills:** scene plan, asset instructions, narration, subtitles, rights/provenance.
- **Production engine:** local assembly, captions, audio mixing, deterministic technical QC.
- **Publishing/analytics:** metadata and upload preparation; human confirmation; verified publication status and observed metrics.

### Per-Short artifact contract

Create artifacts as the item advances:
- `idea.json`: channel, topic, audience, rationale, score, status.
- `research.md`: source URLs, dates, evidence, claim/source mapping, uncertainty.
- `script.md`: hook, narration, on-screen text, target timing.
- `storyboard.md`: scenes, durations, visuals, narration, overlays, asset needs.
- `assets/`: assets and provenance/rights notes; large media local/ignored by default.
- `voice/`: narration and voice/license settings.
- `captions/`: timed subtitle files.
- `render/`: final output and render settings, normally local/ignored.
- `qc-report.md`: automated checks, editorial review, failures and fixes.
- `metadata.md`: title, description, hashtags, cover guidance, publishing state.
- `performance.md`: publication date, metric source, observation window, learnings.

### Quality and safety gates

Editorial: strong but honest hook; one clear takeaway; reliable source support; fact/theory/speculation distinguished; original work; no fabricated demonstrations, quotes, or statistics.

Production: correct vertical format; mobile-readable text; intelligible narration; accurate captions; no clipping or accidental silence; licensed music/assets; visuals support the story.

Publishing: accurate metadata; correct channel; human approval recorded; actual publication result verified.

### Future scope (not initial commitments)

Long-form videos, localization, scheduled trend monitoring, channel dashboards, deeper analytics/experiments, thumbnail testing, multi-platform repurposing, cloud rendering, and richer multi-agent orchestration. Add these only after the Channel 1 workflow works and an observed need justifies the complexity/cost.

### Candidate skill repositories

User supplied these for evaluation, not automatic adoption:
- https://github.com/agricidaniel/claude-youtube
- https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill
- https://github.com/ZeroPointRepo/youtube-skills

Inspect LICENSE, runtime compatibility, scripts/dependencies, external APIs/MCP servers, credentials, free-tier limits, privacy, and maintenance. Do not assume skills for Claude Code/Codex/other runtimes run natively in ordinary ChatGPT chat.

## Daily Shorts automation — user-requested scope extension

**Requirement recorded:** 2026-10-30T22:28:47.380+05:30 (2026-10-30T16:58:47.380Z)

The user has now explicitly requested a daily automated workflow that generates a Short, prepares its title/description/hashtags, and publishes it to YouTube. This supersedes the earlier default assumption that publishing would always require per-video manual approval. However, first-run validation and secure account authorization remain necessary.

### Target daily run
1. Select one eligible idea for Channel 1; avoid duplicate/recently used topics.
2. Research and source-check material.
3. Draft a concise original Short script and hook.
4. Fact-check claims and flag unsupported statements.
5. Create storyboard, visuals, English narration, and captions.
6. Render a vertical Short and run QC.
7. Generate title, description, relevant hashtags, and publishing metadata.
8. Publish through an authorized YouTube integration/API only if all gates pass.
9. Record the video URL, publication result, and run artifacts.
10. If any gate fails, do not publish; save the failure and notify the user.

### Automation gates and prerequisites
- Confirm daily execution time and timezone.
- Confirm which YouTube channel/account is the publishing destination and authorize it through a supported OAuth workflow.
- Select an execution host that can run persistently each day. A GitHub repository alone does not render videos; GitHub Actions or another scheduler must be configured and tested, including storage and runner constraints.
- Choose an image/video/narration path that works within the ₹0 additional recurring budget or obtain explicit approval for any cost.
- Establish a first-pilot validation run before enabling unattended daily public publishing.
- Store OAuth credentials securely, never in Git.
- Treat YouTube upload API quotas, channel permissions, Shorts classification, and current platform rules as implementation requirements to verify.

**Important capability boundary:** A scheduled ChatGPT task can trigger a recurring ChatGPT workflow, but it does not by itself guarantee that a local video renderer runs or that a YouTube upload succeeds. End-to-end daily publishing requires a working execution host, media-generation/assembly tools, and authorized YouTube upload capability.

