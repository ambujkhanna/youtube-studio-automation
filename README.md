# YouTube Studio Automation

**Last updated:** 2026-10-30T22:37:39+05:30 (2026-10-30T17:07:39Z)

A zero-additional-subscription-cost, AI-assisted system for researching, creating, reviewing, publishing, and improving YouTube Shorts across three planned English-language channels.

## Follow AInation Studio

| Platform | Link |
|---|---|
| ▶️ YouTube | https://www.youtube.com/@AI.nationstudio |
| 📘 Facebook | https://www.facebook.com/profile.php?id=61596527993377 |
| 📸 Instagram | https://www.instagram.com/ai.nationstudio/ |

Hashtag: **#AInationstudio**

## Project status (updated 2026-11-10T13:11:14+05:30 (2026-11-10T07:41:14Z))
- Repository: **public** at the moment (keeps GitHub Actions minutes free); never commit secrets
- Phase: **in production**. Daily AInation Studio Shorts (publish 17:00–20:00 IST) and a weekly 16:9 long video (Sunday 10:00 IST), rendered and uploaded by GitHub Actions; also posted to the Facebook Page and Instagram
- Voices: Chatterbox (Dad/Teen cloned) + Turbo for laughs, with Kokoro as automatic backup; typical Short 45–90 s (QC 20–180 s)
- Uploads stay Private until the YouTube API audit is approved; the owner publishes or schedules them in Studio
- Day-to-day reference: [docs/CHANNELS_REFERENCE.md](docs/CHANNELS_REFERENCE.md) (all workflow options, secrets, variables) and [docs/AUTOMATION_SETUP.md](docs/AUTOMATION_SETUP.md)
- Older planning documents below (OVERALL_OBJECTIVE, PLAN, PROGRESS, CONVERSATION) describe the early ChatGPT-era design phase and may be out of date

## Core documents
- [Windows development setup](docs/WINDOWS_DEVELOPMENT.md) — selected Windows platform and planned local toolchain.
- [AInation Studio channel setup](channels/aination-studio/README.md) — Channel 1 positioning, editorial guardrails, and launch gates.
- [AInation Studio configuration](channels/aination-studio/channel.config.json) — machine-readable channel defaults.
- [Overall objective](OVERALL_OBJECTIVE.md) — vision, goals, constraints, success criteria.
- [Plan](PLAN.md) — phases, architecture, workflows, milestones.
- [Progress](PROGRESS.md) — status, completed work, blockers, next actions.
- [Conversation log](CONVERSATION.md) — requirements, decisions, reasoning, and changes.

## Working principles
1. Automate repeatable work; retain human review for quality, accuracy, rights, and publishing.
2. Prefer free and local tools before paid APIs or subscriptions.
3. Never invent facts, sources, analytics, or publishing outcomes.
4. Keep credentials, OAuth tokens, and API secrets out of Git.
5. Update CONVERSATION.md and PROGRESS.md after every meaningful project interaction/work session.
6. Add a timestamp with timezone to every Markdown file whenever it is created or updated.
7. Update PLAN.md and OVERALL_OBJECTIVE.md only when their contents materially change.

## Resuming in a new ChatGPT conversation
Read OVERALL_OBJECTIVE.md, PLAN.md, PROGRESS.md, and CONVERSATION.md. Verify repository state, continue from the Next actions in PROGRESS.md, and do not repeat completed work.

## Repository safety
Do not commit credentials, private channel login details, personal data, copyrighted source media, or generated assets without a clear need and rights to store them. Use environment variables or local secret stores for credentials.

## Portable project context and agent onboarding

This repository must be sufficient to onboard a new human contributor, a fresh ChatGPT conversation, or a different AI agent without access to prior chats.

**Read in this order:**
1. [AGENT_HANDOVER.md](AGENT_HANDOVER.md) — complete handover brief and copy/paste resume prompt.
2. [OVERALL_OBJECTIVE.md](OVERALL_OBJECTIVE.md) — background, objectives, scope, constraints, exclusions, and success criteria.
3. [PLAN.md](PLAN.md) — target architecture, production workflow, phases, quality gates, and future scope.
4. [PROGRESS.md](PROGRESS.md) — verified implementation status, blockers, and exact next actions.
5. [CONVERSATION.md](CONVERSATION.md) — chronological decisions and rationale.

**Source-of-truth rules:** latest explicit user instruction wins; otherwise use the latest dated decision in CONVERSATION.md. PROGRESS.md describes verified reality; PLAN.md describes intended work. Never treat a planned item as implemented without verification.

## Detailed operating rules

- Verify the live repository before changing files.
- Preserve historical decisions; append a new decision when one changes.
- Update CONVERSATION.md and PROGRESS.md after each meaningful work session.
- Timestamp every Markdown file whenever created or updated, including timezone.
- Keep generated media, credentials, OAuth tokens, and private account details out of Git by default.
- Prefer free/local/open-source components; disclose quotas, cost, privacy, and licensing before adoption.
- First pilot requires review; routine publishing is intended to be unattended after validation.
- Do not claim success for commits, tests, renders, uploads, or integrations without checking the result.

### New conversation / other agent

Use the copy/paste prompt in AGENT_HANDOVER.md. Resume from the exact Next actions in PROGRESS.md; do not ask the user to repeat documented decisions.

**Channel 1 working name:** AInation Studio. Name availability and trademark status are not yet verified.

## Latest channel and development decisions

- Channel 1 working name: **AInation Studio**. Name/handle/trademark availability is not yet verified.
- Development target: **Windows**. Exact Windows version, CPU/GPU/RAM, and available disk space remain to be confirmed before selecting hardware-dependent tools.
- Initial publishing target: daily at 7:00 PM IST, after the first end-to-end pilot passes and the connected YouTube destination is verified.
- The current editorial direction remains practical AI and technology demonstrations, experiments, workflows, and explanations; confirm whether the brand should instead focus specifically on AI-generated animation.
