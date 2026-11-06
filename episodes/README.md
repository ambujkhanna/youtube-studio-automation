# Episodes (backlog)

**Created:** 2026-11-02 (Claude Code session)

One folder per episode: `episodes/<id>-<slug>/episode.json`. The daily run publishes the next folder (sorted by id)
whose `"status"` is `"ready"` and that isn't already recorded in `state.json`.

| ID | Title | Length |
|---|---|---|
| ep001 | AI Agent vs Chatbot Explained | pilot (manual upload) |
| ep002 | Why AI Gives Useless Answers | ~68 s |
| ep003 | Why AI Makes Things Up | ~62 s |
| ep004 | How Does ChatGPT Actually Work? | ~63 s |
| ep005 | What Not to Tell AI | ~62 s |
| ep006 | How to Spot a Deepfake | ~61 s |
| ep007 | How AI Makes Pictures From Words | ~63 s |
| ep008 | 3 Smart Ways to Use AI Every Day | ~62 s |

Scripts follow the public YouTube skills used for EP001: question hook in the first 2–3 s, one idea per beat,
a board change every few seconds, a single Subscribe ask (the animated Subscribe / Like / Share end card pops up when "subscribe" is spoken), and a last line that loops back to the hook.

## episode.json format

```json
{
  "id": "ep009", "slug": "my-topic", "status": "ready",
  "title": "≤ 60 chars, keyword first",
  "cover_text": "≤ 3 WORDS",
  "description": "First line = what the viewer gets ... Subscribe: https://www.youtube.com/@AI.nationstudio",
  "hashtags": ["#AI", "#Shorts"], "tags": ["..."],
  "voices": {"DAD": ["am_michael", 0.95], "TEEN": ["af_heart", 1.05]},
  "loop_card": {"text": "Echo of the hook?", "cue": "next", "left": "chat", "right": "robot"},
  "lines": [
    {"who": "DAD",  "text": "Hook question?", "board": {"type": "title", "left": {"icon": "chat", "label": "A"}, "right": {"icon": "robot", "label": "B"}, "subtitle": "..."}},
    {"who": "TEEN", "text": "Answer with a keyword.", "punch": "keyword", "board": {"type": "big", "icon": "bulb", "text": "Key idea", "cue": "keyword"}},
    {"who": "TEEN", "text": "You got it! Subscribe to AI Nation Studio, and share this with a friend! And next time ... echo of the hook?"}
  ]
}
```

- `board` starts a new whiteboard scene (it stays until the next line that has one).
- `cue` = a word **from that line**; the item pops in when that word is spoken (and the teen points at it).
- `punch` = a word that gets a quick camera zoom.
- Scene types: `title`, `big`, `chat`, `steps`, `compare`, `checklist`, `permission`, `summary`.
- Icons: chat, robot, check, sun, train, doc, lock, target, search, calendar, mail, suitcase, warn, x, user,
  bulb, shield, coin, eye, book, globe, brain, phone.
- Say the channel as "AI Nation Studio" in `text` (correct pronunciation); captions show "AInation".
- Aim for 12–14 lines ≈ 60–75 s. Never invent numbers or sources; keep health/money advice general.

Check before committing: `python pipeline/validate_episode.py episodes/*/episode.json`

## New scene types and pictures (2026-11-06)

- **Animated diagrams:** `cycle` (steps in an oval with arrows; e.g. how AI learns), `journey` (stops on a road with a travelling emoji; e.g. question → tokens → answer), `orbit` and `body`. Fields are in `pipeline/diagrams.py`.
- **Big readable boards:** `chat` (up to 3 bubbles), `permission`, `title`, `big`, `steps`, `compare`, `checklist`, `summary`, `gallery`. Keep labels short; text is drawn large and shrinks or wraps if needed.
- **Icons:** the old named icons, any common emoji, or real drawings `img:<Category>/<Author>/<name>` from `assets/IMAGE_INDEX.txt`. Credits are added to the description automatically.
- **Ending:** "Subscribe to AI Nation Studio, and share this with a friend! And next time …?". The Subscribe / Like / Share card appears on "subscribe".
