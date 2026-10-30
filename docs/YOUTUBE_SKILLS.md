# YouTube creator skills — installation and usage

**Updated:** 2026-10-31T00:32:00+05:30 (2026-10-30T19:02:00Z)

## Scope and honest installation status

The three repositories selected by the user are external Agent Skills projects. Their files can be installed into the Windows project/agent directories, but copying files does not install them into ChatGPT's hosted runtime. ChatGPT can consult their instructions when those files are available in the conversation or project workspace; the user's local IDE/agent must load the local skill folders after installation and restart.

Run from the repository root on the user's Windows PC:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\install-youtube-skills.ps1
```

The installer clones/updates source repositories under `vendor/youtube-skills/`, installs the Claude YouTube skill to `%USERPROFILE%\.claude\skills\youtube`, and copies the ChatGPT YouTube Agent Skill plus YouTube research skill folders into project-local `.codex\skills\`. The source repositories and their LICENSE files are retained for attribution and audit.

## Selected repositories and how the project will use them

1. **AgriciDaniel/claude-youtube** — use its orchestrator, Shorts, scripting, hooks, strategy, metadata, SEO, and quality-gate references. Its README requires Claude Code for native slash-command use; the project can also consult the Markdown guidance. Optional DataForSEO integration is paid and must remain disabled unless approved.
2. **Jakeschincariol/chatgpt-youtube-agent-skill** — use `yt-script`, `yt-package`, `yt-shorts`, `yt-seo`, `yt-plan`, `yt-edit`, and `yt-retention` for script structure, hook scoring, title packaging, and editing/retention plans. These are creator workflow skills, not a 3D animation engine or publishing service.
3. **ZeroPointRepo/youtube-skills** — use `youtube-full` / focused transcript, search, and channel skills for source research and reference analysis. Its README lists 100 free signup credits and a $5/month starter plan; first use requires TranscriptAPI account/email verification and an API key. Do not sign up, enter credentials, or incur paid charges without user authorization.

## Runtime use in this project

- Use YouTube research skills to gather source material and validate claims.
- Use script/Shorts skills to produce a short-form script with hook, beats, dialogue, visual direction, and ending/loop.
- Use package/SEO skills to create title, description, tags, and hashtags.
- Use edit/retention guidance to build shot timing, pattern interrupts, and review criteria.
- Keep a separate animation renderer requirement: these skills do not create 3D characters, animate scenes, synthesize dialogue, or perform lip-sync.
- Preserve source attribution and MIT license notices when copying code or substantial source material.
- Do not treat example benchmarks in skills as guaranteed algorithm facts; validate current platform rules and actual channel analytics.

## Video quality gate

A sample passes only if it is a real moving video with coherent animated characters and environments, expressive movement, stable character identity, intelligible natural dialogue, and convincing lip-sync where characters speak. A storyboard, sprite sheet, static image montage, or motion-graphics-only video fails. Target final format: 1080×1920 vertical.

## Verification

After running the installer, verify that:
- `vendor/youtube-skills/` contains all three source repositories and their LICENSE files.
- `%USERPROFILE%\.claude\skills\youtube\SKILL.md` exists.
- `.codex\skills\yt-script\SKILL.md`, `.codex\skills\yt-package\SKILL.md`, and `.codex\skills\youtube-full\SKILL.md` exist.
- Restart the selected IDE/agent and confirm its skill discovery panel/list shows the installed skills.

This chat cannot execute PowerShell on the user's Windows PC. Therefore, before the user runs the installer, installation is prepared but not yet verified on that machine.
