"""Generate dialogue audio with Kokoro and exact per-phoneme timings."""
import json, os, re
import numpy as np, onnxruntime as ort, soundfile as sf
from kokoro_onnx import Kokoro

S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(S, "prod", "build"); os.makedirs(OUT, exist_ok=True)
SR, HOP = 24000, 600

VOICES = {"DAD": ("am_michael", 0.95), "TEEN": ("af_heart", 1.08)}
LINES = [
    ("DAD",  "Everyone keeps talking about AI agents. Isn't that just a fancy chatbot?"),
    ("TEEN", "Not quite! A chatbot is like a smart helper you talk to. You ask a question, and it gives you an answer."),
    ("DAD",  "Like when I ask it for a pasta recipe?"),
    ("TEEN", "Exactly. It answers, and then it waits for your next message. You still do all the work."),
    ("DAD",  "So what does an agent do differently?"),
    ("TEEN", "An agent gets a goal, not just a question. It breaks the goal into steps, uses tools like search, calendars, or email, and then checks its own results."),
    ("DAD",  "Show me with a real example."),
    ("TEEN", "Say you want a weekend trip. A chatbot gives you a list of ideas. An agent checks the weather, compares train times, finds a hotel in your budget, and drafts the whole plan."),
    ("DAD",  "Wow. But I don't want it booking anything without asking me!"),
    ("TEEN", "And it shouldn't. Good agents ask your permission before important actions, like paying or sending emails. You stay in control."),
    ("DAD",  "Can agents make mistakes?"),
    ("TEEN", "Yes, they can. So always check their work, just like you would with a new assistant."),
    ("DAD",  "So, a chatbot answers. An agent acts."),
    ("TEEN", "You got it! Follow AI Nation Studio for more AI, explained simply."),
]
GAP = 0.32  # seconds between lines
LEAD = 0.45  # silence before first line

k = Kokoro(os.path.join(S, "kokoro-q8.onnx"), os.path.join(S, "voices.bin"))
sess = ort.InferenceSession(os.path.join(S, "kokoro-dur.onnx"))
vocab = k.tokenizer.vocab

audio = [np.zeros(int(LEAD * SR), np.float32)]
t = LEAD
lines = []
for spk, text in LINES:
    voice, speed = VOICES[spk]
    ph = k.tokenizer.phonemize(text, "en-us")
    chars = [c for c in ph if c in vocab]
    toks = [vocab[c] for c in chars]
    style = k.get_voice_style(voice)[len(toks)]
    wav, dur = sess.run(None, {"input_ids": np.array([[0, *toks, 0]], np.int64),
                               "style": style, "speed": np.array([speed], np.float32)})
    wav = wav.ravel().astype(np.float32); dur = np.array(dur).ravel()
    assert abs(wav.size - dur.sum() * HOP) < HOP, (wav.size, dur.sum())
    # trim: keep BOS silence partly, it's natural lead-in
    edges = np.concatenate([[0], np.cumsum(dur)]) * HOP / SR
    phon = [(chars[i], t + edges[i + 1], t + edges[i + 2]) for i in range(len(chars))]
    # words: split phoneme string on spaces, align with text words
    words_txt = text.split()
    groups, cur = [], []
    for c, a, b in phon:
        if c == " ":
            if cur: groups.append(cur); cur = []
        else:
            cur.append((c, a, b))
    if cur: groups.append(cur)
    # drop groups that are only punctuation
    groups = [g for g in groups if any(re.match(r"\w", c) or c not in ".,!?;:…—\"'" for c, _, _ in g)]
    if len(groups) != len(words_txt):
        print("WARN word mismatch", spk, len(groups), len(words_txt), ph)
        n = len(words_txt); a0, b0 = phon[0][1], phon[-1][2]
        words = [(w, a0 + (b0 - a0) * i / n, a0 + (b0 - a0) * (i + 1) / n) for i, w in enumerate(words_txt)]
    else:
        words = [(w, g[0][1], g[-1][2]) for w, g in zip(words_txt, groups)]
    peak = np.abs(wav).max(); wav = wav / peak * 0.85
    start, end = t + edges[1], t + edges[-2]
    lines.append(dict(speaker=spk, text=text, start=start, end=end, phonemes=phon, words=words, ipa=ph))
    audio.append(wav); t += wav.size / SR
    audio.append(np.zeros(int(GAP * SR), np.float32)); t += GAP
    print(f"{spk:5s} {start:6.2f}-{end:6.2f} {text}")

audio.append(np.zeros(int(0.8 * SR), np.float32))
full = np.concatenate(audio)
sf.write(os.path.join(OUT, "dialogue.wav"), full, SR)
json.dump(dict(duration=full.size / SR, lines=lines), open(os.path.join(OUT, "timing.json"), "w"), indent=1)
print("total", full.size / SR)
