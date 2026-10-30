# YouTube Studio Automation

**Last updated:** 2026-10-30T22:26:10+05:30 (2026-10-30T16:56:10Z)

A zero-additional-subscription-cost, AI-assisted system for researching, creating, reviewing, publishing, and improving YouTube Shorts across three planned English-language channels.

## Project status
- Repository: private
- Current phase: Phase 0 — foundation and workflow design
- First channel: AI in Action Lab (working name)
- Initial format: YouTube Shorts
- Public publishing requires human approval

## Core documents
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
- Public publishing requires human approval.
- Do not claim success for commits, tests, renders, uploads, or integrations without checking the result.

### New conversation / other agent

Use the copy/paste prompt in AGENT_HANDOVER.md. Resume from the exact Next actions in PROGRESS.md; do not ask the user to repeat documented decisions.
