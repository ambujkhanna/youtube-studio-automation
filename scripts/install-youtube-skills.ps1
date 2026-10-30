# Install the user-selected YouTube creator skill repositories on Windows.
# Run from the project root in PowerShell 7 or Windows PowerShell 5.1.
# This installs local source copies; it does not install skills into ChatGPT's hosted runtime.
$ErrorActionPreference = "Stop"

$root = (Get-Location).Path
$vendor = Join-Path $root "vendor/youtube-skills"
$codexSkills = Join-Path $root ".codex/skills"
$claudeSkills = Join-Path $env:USERPROFILE ".claude/skills"

New-Item -ItemType Directory -Force -Path $vendor, $codexSkills, $claudeSkills | Out-Null

function Sync-Repo([string]$Name, [string]$Url) {
  $dest = Join-Path $vendor $Name
  if (Test-Path (Join-Path $dest ".git")) {
    git -C $dest pull --ff-only
  } else {
    git clone $Url $dest
  }
  if ($LASTEXITCODE -ne 0) { throw "Failed to clone/update $Name" }
  return $dest
}

# 1) Claude YouTube: install the orchestrator and its references/sub-skills into Claude Code.
$claudeRepo = Sync-Repo "claude-youtube" "https://github.com/AgriciDaniel/claude-youtube.git"
$claudeSource = Join-Path $claudeRepo "skills/claude-youtube"
$claudeTarget = Join-Path $claudeSkills "youtube"
if (!(Test-Path (Join-Path $claudeSource "SKILL.md"))) { throw "Claude YouTube SKILL.md not found" }
if (Test-Path $claudeTarget) { Remove-Item -Recurse -Force $claudeTarget }
Copy-Item -Recurse $claudeSource $claudeTarget

# 2) ChatGPT YouTube Agent Skill: copy its 11 skill folders into the project-local Codex skills folder.
$chatgptRepo = Sync-Repo "chatgpt-youtube-agent-skill" "https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill.git"
$chatgptSource = Join-Path $chatgptRepo "skills"
if (!(Test-Path $chatgptSource)) { throw "ChatGPT YouTube skills directory not found" }
Get-ChildItem $chatgptSource -Directory | ForEach-Object {
  $target = Join-Path $codexSkills $_.Name
  if (Test-Path $target) { Remove-Item -Recurse -Force $target }
  Copy-Item -Recurse $_.FullName $target
}

# 3) YouTube Skills: install the complete research/transcript toolkit locally for Codex.
$researchRepo = Sync-Repo "youtube-skills" "https://github.com/ZeroPointRepo/youtube-skills.git"
$researchSource = Join-Path $researchRepo "skills"
if (!(Test-Path $researchSource)) { throw "YouTube research skills directory not found" }
Get-ChildItem $researchSource -Directory | ForEach-Object {
  $target = Join-Path $codexSkills $_.Name
  if (Test-Path $target) { Remove-Item -Recurse -Force $target }
  Copy-Item -Recurse $_.FullName $target
}

Write-Host "Installed source repositories under: $vendor"
Write-Host "Claude Code skill: $claudeTarget"
Write-Host "Project-local Codex skills: $codexSkills"
Write-Host "Note: TranscriptAPI may require account registration and an API key; its free tier is limited."
Write-Host "Restart your agent/IDE so it discovers the new skill files."
