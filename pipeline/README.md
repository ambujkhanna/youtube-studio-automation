# AiNation Studio — 2D episode pipeline (line-art style)

**Created:** 2026-11-01T16:12:09+05:30 (2026-11-01T10:42:09Z) in a Claude Code cloud session.
**Status:** Pilot episode "AI Agents vs Chatbots" (82.5 s, 1080×1920) rendered and approved for initial kick-off.

Script in → voices → phoneme-timed lip-sync → line-art characters + board scenes → captions/music → MP4.
Zero paid services. Runs on CPU (a full 82 s episode renders in about 2–3 minutes on 4 cores).

## Files
| File | Role |
|---|---|
| `tts.py` | Script lines + voices (Kokoro-82M, Apache-2.0). Writes `build/dialogue.wav` and `build/timing.json` with exact per-phoneme timings. |
| `kit2d.py` | Reusable kit: tracks/easing, character acting model (`Char`), board helpers/icons, camera, frame renderer. |
| `char_line.py` | Line-art characters: DAD (40–45, learner) and TEEN (15–16, teacher). Faces, mouths (lip-sync), poses. |
| `bg_line.py` | Line-art room and board frame. |
| `ep_agents.py` | The episode: acting cues per line, board scenes per line, camera shots. Renders PNG frames. |
| `finish.py` | Mixes dialogue + original synthesised music + SFX, builds word-highlight captions (ASS), encodes H.264 MP4. |
| `line_sheet.py` | Renders a character design sheet (stills) for review. |

## Setup (Linux / WSL / macOS; Windows works via WSL)
```bash
python3 -m venv venv && . venv/bin/activate
pip install kokoro-onnx onnxruntime onnx soundfile numpy skia-python
# ffmpeg with libass must be on PATH
```
Voice model (one-time): download the npm packages `kokoro-q8-shards` and `kokoro-local-runtime`
(`npm pack kokoro-q8-shards kokoro-local-runtime`), then:
- concatenate `kokoro-q8.part0..5.bin` → `kokoro-q8.onnx` (sha256 starts `fbae9257`)
- build `voices.bin`: `np.savez` of every `voices/*.bin` reshaped to (510, 1, 256) float32
- create `kokoro-dur.onnx`: add graph output `/encoder/Cast_output_0` (int64) to expose phoneme durations
(see the session notes in CONVERSATION.md for the exact snippet). Place these three files one level above `pipeline/`.

## Run
```bash
python pipeline/tts.py                       # voices + timings
cd pipeline && python ep_agents.py ../frames # render frames
cd .. && python pipeline/finish.py frames 24 episode.mp4
```

## Making a new episode
1. Edit `LINES` in `tts.py` (speaker DAD/TEEN + text) and run it.
2. Copy `ep_agents.py` → `ep_<topic>.py`; edit the `ACT` cues (gestures/expressions by word), the board scenes (`SC` + `el(...)` elements) and `SHOTS`.
3. Render stills first (`python ep_<topic>.py ../frames 300 900`), review, then render all frames and run `finish.py`.

## Known limitations / later improvements
- Free voices: the teen voice is a young-adult voice sped up; a premium voice (e.g. ElevenLabs) would sound more like a teen.
- Board scenes are hand-written per episode; next step is a script+cue JSON format so new topics need no code.
- Name "AiNation Studio": trademark/handle clearance still pending (existing "AI Nation" channels in the same niche).

## Final EP001 look (2026-11-02)
- Characters: line-art Dad + Teen drawn in **doodle style** (`DOODLE=chars`): hand-inked boiling lines, sketch pass, offset marker fill.
- Background: **living room** (`BG=v2`): window with drifting clouds, sofa, sleepy cat mascot, framed pictures, laptop side table; whiteboard + logo unchanged.
- Build the final cut:
  ```bash
  VARIANT=short python pipeline/tts.py          # or VARIANT=full
  cd pipeline && BG=v2 DOODLE=chars python ep_agents.py ../frames && cd ..
  python pipeline/finish.py frames 24 AInation_EP001_short.mp4
  ```
- `DOODLE=1` doodles the whole scene incl. handwritten fonts (`fonts/`, OFL-1.1) — available but not used.
