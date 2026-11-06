# Daily automation — setup guide (AInation Studio)

**Created:** 2026-11-02 (Claude Code session)

The daily run is fully automatic once these one-time steps are done. Nothing here costs money.

## How it works

```text
GitHub Actions (daily 09:15 UTC = 14:45 IST, or "Run workflow" manually)
  → pick next ready episode in episodes/  (skips ones already uploaded)
  → voices (Kokoro, free) → frames → MP4 with captions + music
  → automated QC (1080×1920, 45–180 s, audio level, captions, title/description)
  → upload to YouTube as PRIVATE, scheduled to publish 19:00 IST
  → write result to episodes/state.json + keep the MP4 as a run artifact for 14 days
```

Fail-closed: if any step or QC check fails, nothing is uploaded and the run shows red.
Without YouTube secrets the run still renders + QCs (a "dry run") — download the MP4 from the run's Artifacts.

## Step 1 — Try it without YouTube (5 minutes)

1. GitHub → your repo → **Actions** tab → enable workflows if asked.
2. Click **Daily AInation Short** → **Run workflow** → tick **dry_run** → **Run**.
3. After ~10–15 minutes open the run → **Artifacts** → download the MP4 and watch it.

## Step 2 — Give the workflow permission to upload (one time, ~20 minutes, no Python needed)

1. **Google Cloud project**: https://console.cloud.google.com → create project "AInation Automation".
2. **Enable the API**: APIs & Services → Library → **YouTube Data API v3** → Enable.
3. **OAuth consent screen**: External → app name "AInation Automation" → your email → Save.
   Add your Google account under **Test users**. Then **Publish app** ("In production").
   (If it stays in "Testing", Google expires the refresh token after 7 days.)
4. **Credentials** → Create credentials → **OAuth client ID** → type **Web application** →
   Authorized redirect URI: `https://developers.google.com/oauthplayground` → Create.
   Copy the **Client ID** and **Client secret**.
5. **Get a refresh token** at https://developers.google.com/oauthplayground :
   - Gear icon (top right) → tick **Use your own OAuth credentials** → paste Client ID + secret.
   - Step 1: in "Input your own scopes" paste `https://www.googleapis.com/auth/youtube.upload` → **Authorize APIs**.
   - Sign in with the Google account that owns the channel and **choose the AInation Studio channel**
     (it's a brand account — pick it when asked which account/channel). Accept the "unverified app" warning (it's your own app).
   - Step 2: **Exchange authorization code for tokens** → copy the **Refresh token**.
6. **GitHub secrets**: repo → Settings → Secrets and variables → **Actions** → New repository secret (×3):
   - `YT_CLIENT_ID` = Client ID
   - `YT_CLIENT_SECRET` = Client secret
   - `YT_REFRESH_TOKEN` = Refresh token
   Never paste these into chat, files or commits.

## Step 3 — First real run

Actions → Daily AInation Short → Run workflow (dry_run **unticked**). The run log ends with the video URL.
Check it in YouTube Studio, set the audience/AI-disclosure options if prompted, and publish.

## Important: the YouTube API audit

YouTube locks videos uploaded through a **new, unaudited** API project to **Private** — even with a publish time.
Until the audit is approved, each day's video arrives as a private upload and you click **Public** in YouTube Studio
(about 10 seconds a day). To remove that step, apply for the audit:
https://support.google.com/youtube/contact/yt_api_form (YouTube API Services — Audit and Quota Extension).
Once approved, uploads publish automatically at 19:00 IST with no manual step.

Quota: the default 10,000 units/day is plenty (one upload ≈ 1,600 units).
GitHub Actions: a daily run takes roughly 10–15 minutes; the free tier for private repos (2,000 min/month) covers it.

## Adding episodes

See `episodes/README.md`. Each episode is one JSON file; validate with
`python pipeline/validate_episode.py episodes/*/episode.json` (also safe to skip — the daily run fails closed).
Keep at least a week of `"status": "ready"` episodes in the backlog; the run reports when it's empty.

## Weekly long videos (16:9, 3–8 min) — added 2026-11-06

- **Workflow:** `.github/workflows/weekly-long.yml` runs **once a week**. It takes the next ready script in `long/` (L01, L02, …) and renders a **1920×1080** video. The board or stage is on the left, the characters are on the right, and captions sit under the board.
- **Upload:** it uploads the video like a Short (Private until the API audit, then scheduled in the PUBLISH_WINDOW). YouTube **chapters** are added to the description automatically from the script's `"chapter"` markers, and `#Shorts` is removed. A **16:9 thumbnail** is designed and uploaded.
- **Run time:** a long render takes about 40–60 minutes. One per week per channel fits GitHub's free minutes. To test it, go to Actions → the weekly workflow → Run workflow and tick **dry_run**. The MP4 and thumbnail appear in the run's Artifacts.
- **Scripts:** 8 are ready in `long/`. The format is in `long/README.md`. Check scripts with:
  ```bash
  python pipeline/validate_episode.py long/*/episode.json
  ```
- **Tip:** in YouTube Studio, set each Short's "Related video" to its long version.

## Real illustrations, diagrams and fonts — added 2026-11-06

- **Real science drawings:** any icon can be `img:<Category>/<Author>/<name>`; the full list is in `assets/IMAGE_INDEX.txt`. They come from Bioicons (Servier Medical Art and others), using only licences that allow commercial use. The daily run downloads any missing drawing from GitHub, and the credits required by CC BY are **added to the YouTube description automatically**.
- **Animated diagrams:** `body` (blood, nerve, air and food flows), `cycle`, `journey` and `orbit`. See `episodes/README.md` and `pipeline/diagrams.py`.
- **Fonts** (SIL Open Font License, licence files in `fonts/`): The CurioKids Club uses Fredoka for boards and Lilita One for captions. AInation Studio uses Poppins.
