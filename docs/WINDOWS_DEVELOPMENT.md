# Windows Development Environment

**Last updated:** 2026-10-30T22:37:39+05:30 (2026-10-30T17:07:39Z)
**Status:** Windows selected; exact device specifications pending.

## Confirmed target

The user has selected **Windows** as the development platform for YouTube Studio Automation.

Do not assume a particular Windows release, CPU architecture, GPU, RAM, or available disk space. Confirm these before choosing local AI models, GPU acceleration, or hardware-intensive video workflows.

## Intended initial toolchain

Evaluate a Windows-compatible local-first stack:

- Git for source control.
- Python for orchestration, content manifests, and QC scripts.
- FFmpeg for video assembly, audio mixing, subtitle rendering, and media inspection.
- PowerShell for Windows setup and repeatable developer commands.
- A local or zero-recurring-cost TTS option, selected only after voice quality, licensing, and Windows compatibility checks.
- Optional image/video generation only after confirming hardware requirements, licensing, and whether it stays within the ₹0 additional monthly budget.

No specific package versions are pinned yet. Do not install tools or commit generated binaries until compatibility and licensing are checked.

## Information needed before hardware-dependent choices

Record these in the local environment notes (do not commit personal identifiers or secrets):

- Windows version and build.
- CPU model and architecture.
- Installed RAM.
- GPU model and dedicated VRAM, if any.
- Free disk space available for source assets and rendered videos.
- Whether the user can install software and run PowerShell scripts.

## Security and repository rules

- Keep API keys, OAuth credentials, cookies, and tokens out of Git.
- Use local environment variables or a secure secret store.
- Keep generated media and large model weights outside Git by default.
- Do not run untrusted setup scripts from candidate skill repositories without inspecting their contents.
- Disclose paid services, usage limits, privacy implications, and asset/voice licensing before adoption.

## First implementation milestone

Create a deterministic Windows-compatible video renderer that can turn an approved scene manifest, text overlays, narration track, and licensed/original assets into a vertical MP4. Add automated checks for output dimensions, duration, audio presence, subtitle timing, and file integrity. This first renderer should not depend on paid AI APIs.
