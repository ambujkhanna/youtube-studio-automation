# Agent Handover — YouTube Studio Automation

**Last updated:** 2026-10-30T22:26:10+05:30 (2026-10-30T16:56:10Z)
**Repository:** https://github.com/ambujkhanna/youtube-studio-automation
**Default branch:** main
**Visibility:** Private

## Read this first

This is the portable onboarding guide for a new ChatGPT conversation, another AI agent, or a human contributor. Read these files before changing the project:
1. [OVERALL_OBJECTIVE.md](OVERALL_OBJECTIVE.md) — background, objectives, scope, exclusions, constraints, success criteria.
2. [PLAN.md](PLAN.md) — target architecture, pipeline, phases, quality gates, future scope.
3. [PROGRESS.md](PROGRESS.md) — verified status, blockers, exact next actions.
4. [CONVERSATION.md](CONVERSATION.md) — chronological requirements, decisions, and rationale.
5. [README.md](README.md) — repository overview and operating rules.

The repository is the durable source of truth. The original ChatGPT thread may be unavailable or truncated. Do not require access to it to continue.

## Project in one paragraph

The user is building three separate English-language YouTube channels for a global audience, launched sequentially. Start with Shorts (initial target approximately 30–60 seconds). The user wants a highly automated content studio using skills, agents, and workflows so their main involvement is reviewing and approving work rather than repetitive production. They can spend about 5–7 hours/week and want to avoid additional monthly subscriptions/API spend (₹0/month initially). Channel 1 covers practical AI and technology demonstrations/explanations; Channel 2 covers mystery, history, and untold stories; Channel 3 is original animated storytelling. Prove a reusable production engine with Channel 1 before scaling.

## Channel strategy

| Order | Working name | Editorial promise |
|---|---|---|
| 1 | AI in Action Lab | Practical AI/technology explained through experiments, demonstrations, and useful workflows |
| 2 | The Hidden Archive | Interesting history, mysteries, and untold stories with evidence-led narration |
| 3 | StorySprout Studio | Original animated short stories and characters |

These are working names only. Do not treat names, logos, handles, or trademarks as finalized.

## Non-negotiable constraints

- English narration and on-screen text; global audience.
- Shorts-first; do not begin with 5–15 minute videos.
- 5–7 hours/week user time.
- ₹0 additional monthly subscription/API budget initially.
- Prefer free/open-source/local tools; disclose quotas, trials, usage caps, costs, privacy, and limitations.
- Do not incur paid usage or subscribe without explicit approval.
- Keep human approval before public publishing.
- No fabricated facts, sources, statistics, demonstrations, analytics, or completion claims.
- Respect copyright, asset/music licenses, privacy, and platform rules.
- Never commit secrets or credentials.
- Timestamp every Markdown file whenever created or updated.
- Update CONVERSATION.md and PROGRESS.md after every meaningful work session.

## Current state snapshot

The private repository exists at the URL above; default branch is main. GitHub access was verified to have push/admin permissions during documentation setup. README.md and the four core documents were created and read back from GitHub. Detailed portable documentation is being expanded.

**No production code, installed/adapted skills, agents, workflows, rendered Short, upload, OAuth integration, or analytics integration has been implemented/tested yet.** Verify the live repository before editing; this snapshot may become stale.

## Intended production pipeline

`Research → Idea scoring → Script/hook → Fact check → Storyboard → Visuals/narration → Video assembly → QC → Metadata → Human approval → Publish → Analytics`

Suggested content lifecycle:
`IDEA → RESEARCHED → SELECTED → SCRIPT_DRAFT → FACT_CHECKED → STORYBOARDED → ASSETS_READY → RENDERED → QC_PASSED → HUMAN_APPROVED → PUBLISH_READY → PUBLISHED → ANALYZED`

Add failure/rework states. Failed or unapproved content must not reach publishing.

Each Short should have traceable artifacts as appropriate: idea brief, research/source record, script, storyboard, asset provenance, narration, captions, render settings, QC report, metadata, approval status, publication record, and analytics review.

## Candidate skills supplied by the user

Evaluate, do not assume adoption:
- https://github.com/agricidaniel/claude-youtube
- https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill
- https://github.com/ZeroPointRepo/youtube-skills

Inspect each LICENSE, supported runtime, scripts/dependencies, external APIs/MCP servers, credentials, free-tier limits, privacy, and maintenance. A skill for Claude Code/Codex/another Agent Skills runtime is not automatically executable in ordinary ChatGPT chat. Adapt useful patterns only after license and compatibility review.

## Technical direction — hypotheses only

Potential low-cost components include Python for orchestration, FFmpeg for video assembly/QC, local TTS if voice quality and rights are acceptable, and original or properly licensed visuals. YouTube Data API/OAuth is optional future integration, not a prerequisite for the first pilot.

Do not assume ChatGPT subscription includes API access. Do not assume interactive image generation can be invoked by local scripts. Check current prices, quotas, privacy, rights, and terms before adopting hosted services. Confirm the actual development machine and OS before selecting a toolchain; earlier context mentions Mac M2 but must not be assumed to be the current target.

## Exact next actions

Follow the latest PROGRESS.md. Current intended order:
1. Finish and verify the detailed documentation/handover pack.
2. Add starter channel directories and configuration templates.
3. Inspect the three candidate skill repositories and their licenses/requirements.
4. Confirm target development machine/OS.
5. Choose the smallest viable local toolchain.
6. Build Channel 1 playbook, idea backlog, and pilot brief.
7. Produce one Short end-to-end and record time, manual steps, cost, and defects.

Do not jump to channels 2/3, dashboards, cloud infrastructure, or paid APIs before the Channel 1 pilot demonstrates a need.

## How to work with the user

- The user has authorized project-level repository changes. Be proactive, but verify before editing.
- Ask only for essential missing information; do not ask the user to repeat documented decisions.
- Work in small, verifiable phases and report what changed versus what remains pending.
- Prefer a working minimal implementation over speculative architecture.
- Never claim a commit, test, render, deployment, upload, or integration succeeded without checking it.
- Explain cost, quotas, privacy, and rights before adopting external tools.
- Keep user-facing status concise while repository documentation remains detailed.

## Documentation maintenance procedure

After each meaningful work session:
1. Fetch the latest versions of relevant Markdown files.
2. Preserve existing content and historical decisions.
3. Append the new dated decision/work summary to CONVERSATION.md.
4. Update PROGRESS.md with verified completed work, current phase, blockers, and next actions.
5. Update PLAN.md or OVERALL_OBJECTIVE.md only when they materially change.
6. Update README.md or this file if onboarding rules change.
7. Add a timezone-aware ISO 8601 timestamp to every modified Markdown file.
8. Commit and read the files back from GitHub to verify.

Do not promise background updates between conversations; updates happen while an agent is actively working in the repository.

## Copy/paste prompt for a new ChatGPT conversation or another agent

> Continue the YouTube Studio Automation project from https://github.com/ambujkhanna/youtube-studio-automation. First read AGENT_HANDOVER.md, OVERALL_OBJECTIVE.md, PLAN.md, PROGRESS.md, and CONVERSATION.md from the repository. Treat the repository as the source of truth and verify its current state before editing. Do not ask me to repeat decisions already documented. Resume from the exact Next actions in PROGRESS.md. Work in small, verifiable phases; do not claim unverified completion. Preserve the ₹0 additional monthly budget, Shorts-first approach, sequential channel launch, English/global audience, and human approval before public publishing. After meaningful work, update CONVERSATION.md and PROGRESS.md, timestamp every modified Markdown file, and verify the commits.

## Future scope — not initial commitments

Long-form videos, localization, scheduled trend monitoring, dashboards, deeper analytics/experiments, thumbnail testing, multi-platform repurposing, cloud rendering, and richer multi-agent orchestration may be considered only after the Channel 1 workflow is proven and an observed need justifies the added complexity or cost.
