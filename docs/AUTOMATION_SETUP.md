# Daily automation — setup guide (AInation Studio)

**Created:** 2026-11-02 (Claude Code session)

The daily run is fully automatic once these one-time steps are done. Nothing here costs money.

## How it works

```text
GitHub Actions (daily 09:15 UTC = 14:45 IST, or "Run workflow" manually)
  → pick next ready episode in episodes/  (skips ones already uploaded)
  → voices (Chatterbox, with Kokoro as automatic backup) → frames → MP4 with captions, opening hook, end card + music
  → automated QC (1080×1920, 20–180 s, audio level, captions, title/description)
  → upload to YouTube as PRIVATE, scheduled in a random slot 17:00–20:00 IST (repo variable PUBLISH_WINDOW)
  → post to the Facebook Page + Instagram as a Reel (designed cover)
  → write result to episodes/state.json + keep the MP4 as a run artifact for 14 days
```

Fail-closed: if any step or QC check fails, nothing is uploaded and the run shows red.
Without YouTube secrets the run still renders + QCs (a "dry run") — download the MP4 from the run's Artifacts.

## Step 1 — Try it without YouTube (5 minutes)

1. GitHub → your repo → **Actions** tab → enable workflows if asked.
2. Click **Daily AInation Short** → **Run workflow** → set **action** to *Dry run* → **Run**.
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

Actions → Daily AInation Short → Run workflow (action: *Next video*). The run log ends with the video URL.
Check it in YouTube Studio, set the audience/AI-disclosure options if prompted, and publish.

## Important: the YouTube API audit

YouTube locks videos uploaded through a **new, unaudited** API project to **Private** — even with a publish time.
Until the audit is approved, each day's video arrives as a private upload and you click **Public** in YouTube Studio
(about 10 seconds a day). To remove that step, apply for the audit:
https://support.google.com/youtube/contact/yt_api_form (YouTube API Services — Audit and Quota Extension).
Once approved, uploads publish automatically at their scheduled 17:00–20:00 IST slot with no manual step.

Quota: the default 10,000 units/day is plenty (one upload ≈ 1,600 units).
GitHub Actions: a daily run takes roughly 10–15 minutes; the free tier for private repos (2,000 min/month) covers it.

## Adding episodes

See `episodes/README.md`. Each episode is one JSON file; validate with
`python pipeline/validate_episode.py episodes/*/episode.json` (also safe to skip — the daily run fails closed).
Keep at least a week of `"status": "ready"` episodes in the backlog; the run reports when it's empty.

## Weekly long videos (16:9, 3–8 min) — added 2026-11-06

- **Workflow:** `.github/workflows/weekly-long.yml` runs **once a week**. It takes the next ready script in `long/` (L01, L02, …) and renders a **1920×1080** video. The board or stage is on the left, the characters are on the right, and captions sit under the board.
- **Upload:** it uploads the video like a Short (Private until the API audit, then scheduled in the PUBLISH_WINDOW). YouTube **chapters** are added to the description automatically from the script's `"chapter"` markers, and `#Shorts` is removed. A **16:9 thumbnail** is designed and uploaded.
- **Run time:** a long render takes about 40–60 minutes. One per week per channel fits GitHub's free minutes. To test it, go to Actions → the weekly workflow → Run workflow and set **action** to *Dry run*. The MP4 and thumbnail appear in the run's Artifacts.
- **Scripts:** 8 are ready in `long/`. The format is in `long/README.md`. Check scripts with:
  ```bash
  python pipeline/validate_episode.py long/*/episode.json
  ```
- **Tip:** in YouTube Studio, set each Short's "Related video" to its long version.

## Real illustrations, diagrams and fonts — added 2026-11-06

- **Real science drawings:** any icon can be `img:<Category>/<Author>/<name>`; the full list is in `assets/IMAGE_INDEX.txt`. They come from Bioicons (Servier Medical Art and others), using only licences that allow commercial use. The daily run downloads any missing drawing from GitHub, and the credits required by CC BY are **added to the YouTube description automatically**.
- **Animated diagrams:** `body` (blood, nerve, air and food flows), `cycle`, `journey` and `orbit`. See `episodes/README.md` and `pipeline/diagrams.py`.
- **Fonts** (SIL Open Font License, licence files in `fonts/`): The CurioKids Club uses Fredoka for boards and Lilita One for captions. AInation Studio uses Poppins.

## Facebook Page + Instagram (Reels) — added 2026-11-06

After each YouTube upload, the same video is also posted as a **Reel** to the channel's Facebook Page and Instagram (long 16:9 videos go to Facebook only, as a normal video). It does nothing until these GitHub secrets exist:

| Secret | Where it comes from |
|---|---|
| `META_PAGE_ID` | Graph API Explorer → `me/accounts?fields=id,name,access_token,instagram_business_account` → the Page's `id` |
| `META_PAGE_TOKEN` | the Page's `access_token` from that same query, run **with the extended (long) user token**. Check that it says "Expires: Never" |
| `META_IG_USER_ID` | `instagram_business_account.id` from that same query |

**One-time setup:**
1. Create a Facebook Page and an Instagram **Business** account, then link the Instagram account to the Page (Page → Settings → Linked accounts).
2. Create a Meta developer app (Business type). Add the use cases "Manage everything on your Page" and "Manage messaging & content on Instagram (API setup with Facebook login)".
3. Add a **Facebook Login for Business** configuration with these permissions: pages_show_list, pages_read_engagement, pages_manage_posts, instagram_basic, instagram_content_publish and business_management.
4. In the Graph API Explorer, generate a token with that configuration, extend it in the Access Token Debugger, then run the query above.

**How it posts:**
- **When:** right after the YouTube upload. Instagram's API can't schedule.
- **Caption:** the title, the first paragraph of the description, the brand line and the hashtags.
- **Results:** shown in the run summary (Facebook / Instagram: posted or failed). A failure never blocks the YouTube upload.

**Test, or post an older episode:** Actions → daily workflow → Run workflow → set **post_to** to *Facebook + Instagram only* and enter the **episode** id (e.g. `ep002`). It renders that episode and posts it to Facebook and Instagram only.

## Voices: Chatterbox (added 2026-11-08)

- **The voices:** AInation Studio now speaks with **Chatterbox** (MIT licence, by Resemble AI), an expressive open-source voice model that runs on GitHub's computer.
  - Dad and Teen keep their voices: Chatterbox copies the voice in `assets/voices/dad.wav` and `teen.wav`, which were made from the previous voices.
  - To change a voice, replace the file with a clean 6–10 second recording.
- **Style:** natural explainer delivery (exaggeration 0.5, cfg 0.35, set in `VOICE_ENV` in `pipeline/daily.py`). One episode can override this with `"exaggeration"`, `"cfg"` or `"gap"` in its episode.json.
- **Real laughs and reactions:** "Ha!" or "Ha ha!" in a line, and the tags `[laugh]`, `[chuckle]`, `[gasp]`, `[sigh]` and `[cough]`, are performed by **Chatterbox-Turbo**. Tags never show in captions. Set the repo variable `CB_TURBO_LAUGHS` = `0` to switch this off.
- **Lip-sync:** each line is also read silently by Kokoro, and the two readings are matched, so mouths, captions and board pop-ins stay on the right words.
- **Speed:** the first run installs Chatterbox and downloads its model (about 10 extra minutes); later runs use the cache.
- **Safety net:** if Chatterbox fails, or a Short comes out longer than 3 minutes, the run uses the Kokoro voices and still posts. The run summary shows `Voices: chatterbox` or `Voices: kokoro`. Repo variable `TTS_ENGINE` = `kokoro` switches back for good.
- **Saving results:** the "Commit run state" step uses `pipeline/save_state.py`. It merges this run's results with anything other runs saved meanwhile, so queued runs no longer fail with "push rejected".

## Videos from your own script (added 2026-11-08)

Write a script in `scripts/` (a plain text file), then Run workflow → **script**: `scripts/<file>.txt`. Set **action** to *Dry run* the first time to watch the MP4 from Artifacts.
- **Format and limits:** see `scripts/README.md`: header (`TITLE:` and optional `COVER:`, `HASHTAGS:`, `TITLE_BOARD:`), `---`, then `NAME: text | emoji Board text` lines. Use 9–16 lines and about 110–180 words.
- **Problems** stop the run before rendering and are listed in the run summary.
- **One file = one video.** A file that was already uploaded is never uploaded again; save the script under a new name instead.

## Board look (added 2026-11-10)

Repo variable `BOARD_STYLE` (Settings → Secrets and variables → Actions → Variables): `hanging` (default: dark rounded border hanging from two ceiling rods), `display` (3D screen with a thick black bezel) or `whiteboard` (aluminium frame, corner caps, magnets, marker tray). All are original drawings in `pipeline/bg_line.py`.

**Change it for one video only** (the first one that is set wins):
1. **Run workflow → board_style** (`default` / `hanging` / `display` / `whiteboard`): only that run.
2. **In the episode:** `"board_style": "display"` at the top level of `episode.json`, or `BOARD: display` in your script. That video always uses this look.
3. **Repo variable `BOARD_STYLE`:** every video.
4. Nothing set → `hanging`.

A misspelt value is ignored (the validator and the script check report it), and the run log prints `board look: …`.

## Intro, end card and "Find us online" (added 2026-11-11 12:26 IST)

Every video now starts with a 2-second **intro** ("Welcome to" + the animated channel logo + a short original music sting; Hindi videos say "आपका स्वागत है") and ends with a 3.5-second **"Find us online"** card listing the YouTube, Facebook and Instagram links. The links are in `pipeline/hashtags.py` (`LINKS`); the kids logo is `assets/brand/logo.png` (from your `branding/` folder).
- Repo variables `INTRO` = `off` / `OUTRO` = `off` switch them off (default `on`). Shorts never go over 180 s: if the extras would push a Short over, they are left out and the log says so.
- Tip: Shorts lose viewers in the first 2 seconds. If the retention graph in YouTube Studio drops at the start, try `INTRO=off` for a week and compare.
- End card buttons now size to their text (no more text touching the outline); the old "Search … on YouTube, Instagram, Facebook" strip is replaced by the links card.
