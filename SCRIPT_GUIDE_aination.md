# Make a video from your own script (AInation Studio)

Write a script as a plain text file in this `scripts/` folder. You can also **paste the whole script** into the Run workflow box (see 1b). Then run **Actions → Daily AInation Short → Run workflow** and type its path in **script** (for example `scripts/what-is-a-prompt.txt`). The pipeline checks the script, turns it into an episode, and renders, uploads and posts it like any other video.

**Safe by design:** if anything in the script is wrong, the run **stops before making a video** and the run summary lists every problem with its line number. A broken or half-made video can't be uploaded.

## 1. Create the file (on GitHub, no software needed)
1. Open the repo on github.com and go into the **scripts** folder.
2. Click **Add file → Create new file**.
3. **File name:** lowercase words joined by `-`, ending in `.txt`, with **no spaces**, e.g. `what-is-a-prompt.txt`. Each file becomes **one** video. To post another video, use a **new** file name (a file that was already uploaded won't be uploaded twice).
4. Paste your script (start from `TEMPLATE.txt`), then click **Commit changes**.

## 1b. Or paste the whole script (no file)

In **Run workflow**, paste the complete script (header, `---` and all lines) straight into the **script** box. GitHub turns it into one long line; the pipeline splits it back at every `TITLE:`, `---`, `DAD:` … so the result is the same as a file. Good to know:
- Don't write a character name followed by a colon inside a sentence (e.g. "ask your dad: he knows"), it would start a new line.
- The video's id comes from the title, so the same title won't be uploaded twice. The cleaned-up script is saved in the run's **Artifacts** (`pasted-<title>.txt`).
- The repos are public: anyone can read a run's log, including a pasted script. Use a file if the script is private before it goes live.

## 2. The format

```text
TITLE: What Is a Prompt? 💬 AI Explained Simply
COVER: PROMPT POWER
HASHTAGS: #AI #ChatGPT #Prompting
TITLE_BOARD: 💬 Your words -> 🤖 AI answer
---
DAD: Everyone keeps saying "prompt". What is a prompt?
TEEN: A prompt is simply what you type to an AI.   | 💬 What you type
DAD: So "write me a poem" is a prompt?
...
```

**Header (above the `---` line)**

| Line | Required? | What it is | Rules |
|---|---|---|---|
| `TITLE:` | **yes** | YouTube title | max **70** characters; one emoji at the end is nice |
| `COVER:` | no | 1–3 BIG words on the thumbnail | default: from the title |
| `HASHTAGS:` | no | your topic hashtags, space-separated (most important first) | the channel tag **#AInationstudio** is always added (2nd place). Instagram gets **5** in total, Facebook 10, YouTube 15 (+ `#Shorts`) |
| `DESCRIPTION:` | no | 1–2 sentences for YouTube/Facebook/Instagram | default: the first answer line |
| `TAGS:` | no | YouTube search tags, comma-separated | |
| `TITLE_BOARD:` | no | the opening board: `emoji Word -> emoji Word` | default: a big board with the title question |
| `BOARD:` | no | board look for this video: `hanging`, `display` or `whiteboard` | default: the channel's look (repo variable `BOARD_STYLE`, else `hanging`) |

**Dialogue (below `---`):** one line per spoken line: `NAME: what they say`

| Rule | Value |
|---|---|
| Characters | `DAD` (asks), `TEEN` (explains); use **1 or 2** per video |
| Number of lines | **9–16** (best **11–14**), including the Subscribe line |
| Length of a line | max **230** characters (about 2 sentences); split longer ones |
| Total length | about **110–180 words** ≈ **45–90 seconds** (hard limits: 50–180 words, 20–180 s) |
| First line | a question (it becomes the opening board) |
| Last line | the Subscribe line. If you leave it out, it's added automatically: *"Subscribe to AI Nation Studio, and share this with a friend!"* |

## 3. Pictures on the board (strongly recommended)
Add `|` after a line, then **one emoji** and **up to 5 words** (max 32 characters):
```text
TEEN: Give it context. Who is it for, what style, and how long.   | 🎯 Context ; who, style, length
```
- **When it appears:** the board changes on that line, and the picture pops in when the matching word is spoken.
- **Second line of text:** add `;` then up to 32 characters: `| 🐝 Fan, fan, fan! ; until it's thick`.
- **How often:** add a picture every **2–3 lines** (about 4–6 per video). If you skip some, the pipeline adds a picture by itself when it recognises a word (cat, heart, robot, chat…).
- **What works:** use **one simple emoji**. Combined emoji like 👨‍👩‍👧 don't work.

## 4. Sounds and expressions
| Write | Result |
|---|---|
| `Ha!` / `Ha ha!` / `Hee hee!` | a real laugh or chuckle, with a short pause before and after it |
| `[laugh]` `[chuckle]` `[gasp]` `[sigh]` `[cough]` | the sound, e.g. `[gasp] Whoa! That's huge!` (never shown in subtitles) |
| `Zzz!` | a cartoon snore sound |
| `...` | a small dramatic pause |
Other tags like `[giggle]` are **not** supported, and the check will tell you.

## 5. Run it
**Actions → Daily AInation Short → Run workflow**:
| Field | Value |
|---|---|
| script | `scripts/your-file.txt` |
| action: *Dry run* | ✅ **for the first try**: you get the MP4 in the run's **Artifacts** to watch |
| action: *Next video, publish now* | optional: publish right away instead of the next 17:00–20:00 IST slot |

Then run again with action *Next video (scheduled)* to upload it to YouTube and post it to Facebook and Instagram. The summary shows the links.

## 6. Checklist before you run
- [ ] `TITLE:` present, ≤ 70 characters
- [ ] a `---` line between the header and the dialogue
- [ ] every dialogue line starts with `DAD:` or `TEEN:` and a colon
- [ ] only 1–2 characters, 9–16 lines, about 110–180 words
- [ ] a picture hint (`| emoji words`) every 2–3 lines
- [ ] facts double-checked (it's an explainer: keep it accurate and simple)
- [ ] new file name for a new video, no spaces
