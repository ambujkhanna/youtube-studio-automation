# AInation Studio

**Last updated:** 2026-11-10T13:11:14+05:30 (2026-11-10T07:41:14Z)
**Status:** Live: YouTube @AI.nationstudio, Facebook Page and Instagram @ai.nationstudio. Daily Shorts and a weekly long video are made and published automatically by GitHub Actions.

## Channel role

Channel 1 in the YouTube Studio Automation project. This is the first channel to be developed and the proving ground for the shared Shorts production engine.

## Working positioning

A broad AI and technology channel covering AI tools, AI agents, automation, practical demonstrations, real-world use cases, experiments, productivity workflows, and emerging technology explained clearly for a global English-speaking audience.

**Positioning confirmed by the user:** this is a broad AI channel, not an AI-animation-only channel. Animation may be used as a visual technique, but the subject matter spans AI tools, agents, automation, practical demos, and technology.

## Publishing (current)

- Format: YouTube Shorts (daily) + one 16:9 long video (Sunday 10:00 IST)
- Language: English · Audience: global · Hosts: Dad and Teen
- Duration: typically 45–90 seconds with the expressive Chatterbox voices; QC accepts 20–180 s
- Publish window: 17:00–20:00 IST (repo variable `PUBLISH_WINDOW`); uploads stay Private until the YouTube API audit is approved, so the owner publishes or schedules each one in Studio
- Also posted to the Facebook Page and Instagram as Reels
- Full option list: `docs/CHANNELS_REFERENCE.md`

## Editorial principles

- Demonstrate or explain one useful idea per Short.
- Prefer real workflows and reproducible demonstrations over generic AI claims.
- Source-check factual claims and distinguish evidence from opinion.
- Avoid fabricated tool capabilities, screenshots, benchmarks, quotations, and results.
- Use original or properly licensed visuals, voice, music, and other assets.
- Keep on-screen text readable on a phone and captions accurate.

## Launch gates (done)

All original launch gates are complete: visual identity, channel and handle, first reviewed Short, and unattended daily publishing with QC fail-safes. (The early Metricool plan was replaced by direct YouTube/Meta API uploads.)

`channel.config.json` is kept as a reference summary only; the pipeline reads repo variables and `pipeline/*.py`.
