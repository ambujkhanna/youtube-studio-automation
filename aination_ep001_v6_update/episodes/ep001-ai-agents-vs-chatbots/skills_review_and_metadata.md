# EP001 — AI Agents vs Chatbots: skills review + publish metadata

**Created:** 2026-11-01 (Claude Code session)
**Skills applied (public, MIT):**
- `agricidaniel/claude-youtube` → `sub-skills/shorts.md` (Shorts package, hook, loop, metadata rules)
- `Jakeschincariol/chatgpt-youtube-agent-skill` → `yt-script`, `yt-shorts`, `yt-package`, `yt-seo`
- Not used: `ZeroPointRepo/youtube-skills` (needs a paid/credit TranscriptAPI key).

**Honesty note:** the skills' Python scorers (`hookscore.py`, `title.py`, `deadair.py`) were **not executed** — the
cloud session's safety policy blocked running downloaded code. The checks below apply the skills' written rules by hand.
Run the scorers locally to get numeric scores:
```bash
python3 skills/yt-script/hookscore.py --hook "Is an AI agent just a fancy chatbot?"
python3 skills/yt-package/title.py --title "AI Agent vs Chatbot Explained" --thumb "ANSWERS vs ACTS"
```

## 1. Review of the rendered pilot (v5, 82.5 s)

| Skill rule | Pilot | Verdict |
|---|---|---|
| Hook lands in the first 1–3 s, opens a curiosity gap (shorts.md step 3) | First words start at 0.9 s; the hook line runs to 5.5 s and opens with filler ("Everyone keeps talking about…") | ⚠️ Too slow |
| On-screen text in first 2 s, different words from the spoken line (yt-shorts) | Title card "CHATBOT vs AI AGENT — What's the difference?" | ✅ |
| No channel intro / "before we start" (yt-script) | None | ✅ |
| Visual change at least every 3 s (shorts.md step 4) | Camera cuts every 2–5 s plus board pops every 1–2 s on long lines | ✅ (two cuts > 4 s; board pops cover them) |
| One idea per beat, payoff delivered explicitly (yt-script) | Yes — chatbot → agent loop → example → safety → recap | ✅ |
| Loop: last line sets up/echoes the first (yt-shorts, shorts.md) | Ends on a CTA, no callback to the opening | ⚠️ Missing loop |
| Close = one ask (yt-script) | "Follow … for more AI, explained simply." | ✅ |
| Length sweet spots ~13 s or ~60 s; avoid long middles (shorts-playbook) | 82.5 s (within Shorts' 3-min limit) | ⚠️ Trade-off: user asked for full explanation; consider a ~60 s cut |
| Never invent numbers/results/sources | Only illustrative example values (train 9:40 AM) | ✅ |
| Music: original sound, no 50 % revenue-share issue (shorts.md step 8) | Original synthesised music | ✅ |

## 2. Hook options (yt-script: write five, keep two)

1. "Is an AI agent just a fancy chatbot?" — question + curiosity gap, 1.8 s spoken. **Recommended.**
2. "A chatbot answers. An agent acts. Here's the difference." — contrast formula; doubles as the loop line.
3. "Stop calling every chatbot an AI agent." — pattern interrupt; slightly confrontational for the Dad/Teen tone.
4. "Why does my teen say ChatGPT isn't an AI agent?" — story/relatable; names a brand (avoid in titles).
5. "Everyone keeps talking about AI agents. Isn't that just a fancy chatbot?" — current; good gap, but 5 s and starts with filler.

**Loop fix:** end with Teen: "So next time someone asks if it's just a fancy chatbot… now you know." → replays into hook 1.

## 3. Package (yt-package: title + thumbnail as one unit)

| Title | Chars | Notes |
|---|---|---|
| **AI Agent vs Chatbot Explained** | 29 | Keyword first, 5 words, inside 40-char mobile limit. **Recommended.** |
| Is an AI Agent Just a Chatbot? | 30 | Question form; matches hook 1 |
| AI Agents Explained by a Teen | 29 | Format hook (Dad/Teen); weaker search intent |

**Cover text (≤3 words, must not repeat the title):** `ANSWERS vs ACTS`
**Cover frame brief:** Teen pointing at the board with "AGENT = ACTS"; Dad surprised; high contrast on the cream wall.

## 4. SEO (yt-seo)

**Query test — the video should win:** "ai agent vs chatbot", "what is an ai agent", "difference between chatbot and ai agent".
Title + first description lines contain these words ✅.

**Description (first 125 chars carry it):**
> AI agent vs chatbot: a chatbot answers your question, an AI agent works toward a goal using tools. Here's the difference.
>
> A dad asks, his teen explains — with a real example (planning a weekend trip), why good agents ask your permission before
> paying or sending emails, and why you should still check their work.
>
> AiNation Studio — AI, explained simply.

**Hashtags (3–5):** #AIAgents #Chatbot #AIExplained #TechExplained #Shorts
**Tags (disambiguation only):** ai agent, ai agents, chatbot, ai agent vs chatbot, what is an ai agent, agentic ai, ai explained
**Category:** Science & Technology · **Made for kids:** No · **Altered/synthetic content disclosure:** review per YouTube's current rules (animated, AI-voiced).

## 5. Changes applied in v6 (rendered 2026-11-01)

1. ✅ Hook replaced with option 1: "Is an AI agent just a fancy chatbot?" (spoken 0.7–4.0 s; title card from 0 s).
2. ✅ Loop ending: Teen — "You got it! Follow AI Nation Studio for more. And next time someone asks... is an AI agent just a fancy chatbot?"
   The board returns to the opening question card, so the replay flows into the first line. One ask (Follow).
3. ✅ Two cuts rendered: **Short 64.6 s** (tighter lines, slightly faster delivery — recommended upload) and **Full 82.5 s**.
   Build: `VARIANT=short python pipeline/tts.py` (or `full`), then `ep_agents.py` and `finish.py` as usual.

**Ship it, or change it?**
