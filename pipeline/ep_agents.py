"""Episode: "AI Agents vs Chatbots" — data-driven acting, board scenes and shots on top of kit2d.

Usage: python ep_agents.py <out_dir>
"""
import json, math, os, sys
from multiprocessing import Pool
import skia
import kit2d as K
import doodle
from kit2d import (P, rr, ell, text, smooth, back_out, wob, Track, Char, LN, DUR, FPS, NF, B, W,
                   FONT_XB, FONT_B, FONT_SB, appear, fade, scaled, shadow_rrect, bubble, card,
                   icon_chat, icon_robot, icon_check, icon_sun, icon_train, icon_doc, icon_lock,
                   BX, BY, BW, BH, BCX, BCY, hexc)


def wt(i, prefix, nth=0, end=False):
    ws = [w for w in LN[i]["words"] if w[0].lower().strip(".,!?").startswith(prefix.lower())]
    if len(ws) <= nth:  # cue word not in this script variant: fall back to the line edges
        return LN[i]["end"] if end else LN[i]["start"] + 0.1
    return ws[nth][2] if end else ws[nth][1]


def ls(i): return LN[i]["start"]
def le(i): return LN[i]["end"]


# ============================================================ characters
dad = Char("DAD", 296, 0.0)
teen = Char("TEEN", 784, 2.0)
CH = {"DAD": dad, "TEEN": teen}
import random
random.seed(5)
for c in (dad, teen):
    t = random.uniform(0.6, 1.5)
    while t < DUR:
        c.blinks.append(t); t += random.uniform(2.0, 4.0)

VIS = {}
for chars, ov in [("aɑ", (0.95, 1.0)), ("æ", (0.85, 1.05)), ("ʌɐ", (0.65, 0.92)), ("ɛe", (0.6, 1.05)),
                  ("ɪi", (0.4, 1.12)), ("ə", (0.42, 0.9)), ("ɚɝ", (0.42, 0.75)), ("oɔ", (0.72, 0.6)),
                  ("uʊ", (0.36, 0.5)), ("w", (0.24, 0.45)), ("ɹr", (0.36, 0.72)), ("l", (0.38, 0.95)),
                  ("mbp", (0.0, 0.85)), ("fv", (0.12, 0.98)), ("θð", (0.26, 0.98)), ("ʃʒ", (0.32, 0.62)),
                  ("sztdnkgŋhjɡɾʔç", (0.26, 0.97))]:
    for ch in chars: VIS[ch] = ov
for c in (dad, teen):
    c.mo.add(0, 0); c.mw.add(0, 1)
for ln in LN:
    c = CH[ln["speaker"]]
    c.mo.add(ln["start"] - 0.1, 0); c.mw.add(ln["start"] - 0.1, 1)
    for ch, a, b in ln["phonemes"]:
        if ch in VIS:
            o, w = VIS[ch]
            if ch in "mbp":
                c.mo.add(a + 0.01, 0); c.mo.add(b - 0.01, 0); c.mw.add((a + b) / 2, w)
            else:
                c.mo.add((a + b) / 2, o); c.mw.add((a + b) / 2, w)
        elif ch in " ,.!?;:" and b - a > 0.11:
            c.mo.add(a + 0.04, 0.04); c.mo.add(b - 0.03, 0.04)
    c.mo.add(ln["end"] + 0.08, 0); c.mw.add(ln["end"] + 0.08, 1)

# ============================================================ acting (data)
# g: (word, pose, side in/out/both, until_word or None)  e: (word, brow_up, tilt, smile)
ACT = {
    0: dict(g=[("is", "palms", "both", None)], e=[("is", 0.6, 0.4, 0.3), ("fancy", 1.0, 0.6, 0.15)], le=[("fancy", 0.6, 0.3, 0.75)]),
    1: dict(g=[("not", "wag", "in", "quite"), ("chatbot", "explain", "out", "to"), ("ask", "point", "in", "answer")],
            e=[("not", 0.6, 0.3, 0.75)], board=["ask"], nod=["helper", "answer"]),
    2: dict(g=[("like", "explain", "in", None)], e=[("pasta", 0.9, 0.5, 0.75)], le=[("pasta", 0.4, 0.2, 0.8)]),
    3: dict(g=[("exactly", "fist", "in", "exactly"), ("waits", "palms", "both", "message"), ("still", "explain", "out", "work")],
            e=[("exactly", 0.9, 0.4, 0.85), ("still", 0.5, 0.2, 0.5)], board=["waits"], nod=["work"]),
    4: dict(g=[("so", "chin", "in", None)], e=[("differently", 0.8, 0.4, 0.3)]),
    5: dict(g=[("goal", "point", "in", "question"), ("breaks", "explain", "out", "steps"), ("tools", "point", "in", "email"),
               ("checks", "palms", "both", "results")],
            e=[("agent", 0.7, 0.3, 0.7), ("checks", 0.8, 0.3, 0.8)], board=["goal", "tools"], chin=("breaks", "email"), nod=["results"]),
    6: dict(g=[("show", "palms", "both", None)], e=[("real", 0.8, 0.3, 0.75)]),
    7: dict(g=[("say", "explain", "out", "trip"), ("list", "explain", "in", "ideas"), ("weather", "point", "in", "times"),
               ("hotel", "point2", "in", "budget"), ("drafts", "palms", "both", "plan")],
            e=[("agent", 0.8, 0.3, 0.75)], board=["list", "weather", "hotel"], le=[("drafts", 1.0, 0.6, 0.7)], nod=["plan"]),
    8: dict(g=[("wow", "palms", "both", "wow"), ("don't", "wag", "in", "me")],
            e=[("wow", 1.0, 0.8, 0.85), ("but", -0.5, -0.8, 0.0)], le=[("booking", 0.5, 0.3, 0.6)]),
    9: dict(g=[("shouldn't", "wag", "in", "shouldn't"), ("permission", "point", "in", "actions"), ("paying", "explain", "out", "emails"),
               ("control", "fist", "in", None)],
            e=[("and", 0.6, 0.3, 0.7), ("control", 0.8, 0.3, 0.9)], board=["permission"], nod=["control"], le=[("control", 0.5, 0.3, 0.9)]),
    10: dict(g=[("can", "chin", "in", None)], e=[("mistakes", 0.9, 0.6, 0.1)]),
    11: dict(g=[("yes", "explain", "out", "can"), ("check", "point", "in", "work"), ("just", "palms", "both", "assistant")],
             e=[("yes", 0.6, 0.3, 0.6)], board=["check"], nod=["assistant"]),
    12: dict(g=[("chatbot", "explain", "out", "answers"), ("agent", "point", "in", "acts")], e=[("acts", 0.9, 0.4, 0.88)], board=["agent"]),
    13: dict(g=[("got", "fist", "in", "it"), ("next", "explain", "in", None)], e=[("you", 0.9, 0.4, 0.9), ("next", 0.8, 0.4, 0.6)], hop="got"),
}
PARTNER = {"DAD": 20, "TEEN": -20}
BOARD = {"DAD": (12, -12), "TEEN": (-12, -12)}

for i, ln in enumerate(LN):
    sp = CH[ln["speaker"]]; lsn = "TEEN" if ln["speaker"] == "DAD" else "DAD"; li = CH[lsn]
    a, b = ln["start"], ln["end"]
    cfg = ACT.get(i, {})
    sp.look(a - 0.25, 0, 0); li.look(a - 0.1, PARTNER[lsn], 0, 3)
    for (w, pose, side, until) in cfg.get("g", []):
        t0 = wt(i, w) - 0.08; t1 = wt(i, until, end=True) if until else b
        t1 = max(t1, t0 + 0.45)
        sides = {"in": [sp.inner], "out": [-sp.inner], "both": [1, -1]}[side]
        for s in sides:
            sp.gesture(s, pose, t0, t1)
    for (w, up, tl, sm) in cfg.get("e", []):
        sp.brows(wt(i, w) - 0.05, up, tl); sp.smile.add(wt(i, w), sm)
    sp.brows(b + 0.4, 0, 0)
    for (w, up, tl, sm) in cfg.get("le", []):
        li.brows(wt(i, w), up, tl); li.smile.add(wt(i, w), sm); li.brows(b + 0.6, 0, 0)
    for w in cfg.get("board", []):
        tb = wt(i, w)
        sp.look(tb - 0.15, *BOARD[ln["speaker"]]); sp.look(tb + 1.0, 0, 0)
        li.look(tb + 0.05, *BOARD[lsn]); li.look(tb + 1.3, PARTNER[lsn], 0, 3)
    for w in cfg.get("nod", []):
        li.nod(wt(i, w), 9)
    if "chin" in cfg:
        f_, t_ = cfg["chin"]; li.gesture(li.inner, "chin", wt(i, f_), wt(i, t_, end=True))
    if "hop" in cfg:
        th = wt(i, cfg["hop"])
        for dt, v in ((-0.05, 0), (0.12, 46), (0.3, 0), (0.36, -6), (0.44, 0)):
            sp.hop.add(th + dt, v)
    li.nod(b - 0.1, 7)

# finale: both wave + happy eyes
tf = wt(13, "follow")
for c in (teen, dad):
    s = -c.inner
    c.pose(s, "rest", tf - 0.3)
    k = 0
    tw_end = min(DUR - 0.2, wt(13, "next") - 0.2)
    while tf + k * 0.27 < tw_end:
        c.arm[s][0].add(tf + k * 0.27, 128 + (8 if k % 2 else -4))
        c.arm[s][1].add(tf + k * 0.27, 168 + (22 if k % 2 else -18))
        k += 1
    c.hand[s].append((tf - 0.1, "open")); c.hand[s].sort()
    c.pose(s, "rest", tw_end + 0.3)
    c.look(tf - 0.12, 0, -2, 5 if c is dad else -5); c.smile.add(tf, 0.92); c.brows(tf, 0.8, 0.3)

# ============================================================ extra icons
def icon_target(c, x, y, k=1.0):
    for r_, col in ((30, "#FF4D6D"), (21, "#FFFFFF"), (12, "#FF4D6D")):
        c.drawCircle(x, y, r_ * k, P(col))
    c.drawLine(x, y, x + 26 * k, y - 26 * k, P("#1F2D44", 4 * k))


def icon_search(c, x, y, k=1.0):
    c.drawCircle(x - 5 * k, y - 5 * k, 15 * k, P("#0A84FF", 6 * k)); c.drawLine(x + 6 * k, y + 6 * k, x + 18 * k, y + 18 * k, P("#0A84FF", 8 * k))


def icon_cal(c, x, y, k=1.0):
    c.drawRRect(rr(x - 22 * k, y - 20 * k, 44 * k, 42 * k, 8 * k), P("#FFFFFF")); c.drawRRect(rr(x - 22 * k, y - 20 * k, 44 * k, 42 * k, 8 * k), P("#FF4D6D", 3 * k))
    c.drawRect(skia.Rect.MakeXYWH(x - 22 * k, y - 20 * k, 44 * k, 12 * k), P("#FF4D6D"))
    for i in range(3):
        for j in range(2):
            c.drawCircle(x - 12 * k + i * 12 * k, y + 2 * k + j * 10 * k, 3 * k, P("#5B6B80"))


def icon_mail(c, x, y, k=1.0):
    c.drawRRect(rr(x - 24 * k, y - 16 * k, 48 * k, 34 * k, 6 * k), P("#FFC300"))
    p = skia.Path(); p.moveTo(x - 24 * k, y - 14 * k); p.lineTo(x, y + 4 * k); p.lineTo(x + 24 * k, y - 14 * k)
    c.drawPath(p, P("#1F2D44", 3.5 * k))


def icon_suitcase(c, x, y, k=1.0):
    c.drawRRect(rr(x - 14 * k, y - 34 * k, 28 * k, 16 * k, 6 * k), P("#8B4A26", 5 * k))
    c.drawRRect(rr(x - 34 * k, y - 22 * k, 68 * k, 50 * k, 10 * k), P("#FF7A45"))
    c.drawLine(x - 34 * k, y - 2 * k, x + 34 * k, y - 2 * k, P("#E85D2A", 4 * k))


def icon_warn(c, x, y, k=1.0, col="#FFB703"):
    p = skia.Path(); p.moveTo(x, y - 34 * k); p.lineTo(x + 36 * k, y + 28 * k); p.lineTo(x - 36 * k, y + 28 * k); p.close()
    c.drawPath(p, P(col)); c.drawPath(p, P(col, 8 * k))
    c.drawLine(x, y - 10 * k, x, y + 8 * k, P("#1F2D44", 7 * k)); c.drawCircle(x, y + 18 * k, 4 * k, P("#1F2D44"))


def icon_x(c, x, y, k=1.0):
    c.drawCircle(x, y, 20 * k, P("#FF4D6D"))
    c.drawLine(x - 8 * k, y - 8 * k, x + 8 * k, y + 8 * k, P("#FFFFFF", 5 * k)); c.drawLine(x + 8 * k, y - 8 * k, x - 8 * k, y + 8 * k, P("#FFFFFF", 5 * k))


def icon_user(c, x, y, k=1.0):
    c.drawCircle(x, y, 40 * k, P("#FFC300")); c.drawCircle(x, y - 10 * k, 14 * k, P("#1F2D44"))
    c.drawOval(ell(x, y + 22 * k, 23 * k, 14 * k), P("#1F2D44"))


def chip(c, x, y, label, col, icon=None, size=30):
    f = skia.Font(FONT_XB, size); w = f.measureText(label) + (90 if icon else 50)
    r = rr(x - w / 2, y - 32, w, 64, 32); shadow_rrect(c, r, 6, 4, 0.2); c.drawRRect(r, P(col))
    if icon:
        icon(c, x - w / 2 + 40, y, 0.6); text(c, label, x - w / 2 + 74, y, size, "#FFFFFF", FONT_XB, "l")
    else:
        text(c, label, x, y, size, "#FFFFFF")


def row(c, x, y, w, label, icon=None, size=28, col="#DCEBFF"):
    r = rr(x - w / 2, y - 38, w, 76, 22); shadow_rrect(c, r, 6, 4, 0.22); c.drawRRect(r, P(col))
    if icon:
        icon(c, x - w / 2 + 46, y, 0.8); text(c, label, x - w / 2 + 88, y, size, "#1F2D44", FONT_B, "l")
    else:
        text(c, label, x, y, size, "#1F2D44", FONT_B)


# ============================================================ board scenes
ELEMS = []  # (t_in, t_out, fn(c, t, e), anchor)


def el(t_in, t_out, fn, anchor=None, pivot=None):
    ELEMS.append((t_in, t_out, fn, anchor, pivot))


SC = [0.0, wt(1, "chatbot") - 0.1, wt(2, "like") - 0.1, ls(4) - 0.1, wt(5, "goal") - 0.15, ls(6) - 0.1, wt(7, "chatbot") - 0.1,
      ls(8) - 0.1, wt(9, "permission") - 0.15, ls(10) - 0.1, wt(11, "check") - 0.15, ls(12) - 0.1, DUR + 1]
Y0 = BY + 130  # first content row


def S(i): return SC[i], SC[i + 1]


# S0 title
a_, b_ = S(0)
el(0.05, b_, lambda c, t, e: (icon_chat(c, BCX - 250 - (1 - smooth(t / 0.45)) * 300, BCY - 40, 2.0),
                               text(c, "CHATBOT", BCX - 250 - (1 - smooth(t / 0.45)) * 300, BCY + 70, 40, "#0A84FF"),
                               icon_robot(c, BCX + 250 + (1 - smooth(t / 0.45)) * 300, BCY - 30, 2.0),
                               text(c, "AI AGENT", BCX + 250 + (1 - smooth(t / 0.45)) * 300, BCY + 70, 40, "#E91E63")), pivot=(BCX, BCY))
el(0.45, b_, lambda c, t, e: (c.drawCircle(BCX, BCY + 10, 62, P("#FFC93C")), text(c, "VS", BCX, BCY + 10, 52, "#1F2D44")), (BCX, BCY + 10))
el(1.0, b_, lambda c, t, e: text(c, "What's the difference?", BCX, BCY + 180, 38, "#1F2D44", FONT_XB), pivot=(BCX, BCY + 180))
# S1 chatbot = ask -> answer
a_, b_ = S(1)
el(a_, b_, lambda c, t, e: chip(c, BCX, Y0, "CHATBOT", "#0A84FF", lambda c_, x, y, k: icon_chat(c_, x, y, k, "#FFFFFF")), (BCX + 150, Y0))
el(wt(1, "talk"), b_, lambda c, t, e: text(c, "a smart helper you talk to", BCX, Y0 + 70, 30, "#5B6B80", FONT_SB), pivot=(BCX, Y0 + 70))
el(wt(1, "ask"), b_, lambda c, t, e: (icon_user(c, BX + 110, Y0 + 200, 0.9), bubble(c, BX + 380, Y0 + 190, 380, 96, "Your question?", 34)), (BX + 560, Y0 + 190))
el(wt(1, "answer"), b_, lambda c, t, e: (bubble(c, BX + BW - 380, Y0 + 340, 380, 96, "Here's an answer!", 32, col="#CDE7FF", tail="r"),
                                          icon_chat(c, BX + BW - 110, Y0 + 350, 1.2)), (BX + BW - 200, Y0 + 300))
# S2 pasta recipe, waits, you do the work
a_, b_ = S(2)
el(wt(2, "pasta"), b_, lambda c, t, e: (icon_user(c, BX + 110, Y0 + 20, 0.8), bubble(c, BX + 400, Y0 + 10, 440, 90, "A pasta recipe, please!", 30)), (BX + 600, Y0))


def recipe(c, t, e):
    x, y = BX + BW - 300, Y0 + 190
    r = rr(x - 240, y - 80, 480, 170, 24); shadow_rrect(c, r, 8, 5, 0.25); c.drawRRect(r, P("#CDE7FF"))
    text(c, "Recipe:", x - 210, y - 48, 28, "#0A84FF", FONT_XB, "l")
    for k_, s_ in enumerate(("1. Boil pasta", "2. Make sauce", "3. Mix & serve")):
        text(c, s_, x - 210, y - 6 + k_ * 36, 26, "#1F2D44", FONT_B, "l")


el(wt(3, "answers"), b_, recipe, (BX + BW - 120, Y0 + 120))


def waiting(c, t, e):
    x, y = BX + BW - 300, Y0 + 330
    text(c, "waiting for you", x - 30, y, 26, "#5B6B80", FONT_SB, "r")
    for k_ in range(3):
        bb = max(0, math.sin(t * 8 - k_ * 0.8)) * 10
        c.drawCircle(x + 10 + k_ * 26, y - bb, 9, P("#0A84FF"))


el(wt(3, "waits"), b_, waiting, pivot=(BX + BW - 300, Y0 + 330))


def you_work(c, t, e):
    y = Y0 + 395
    r = rr(BX + 50, y - 36, BW - 100, 72, 36); c.drawRRect(r, P("#FFF1B8"))
    text(c, "YOU still: shop  •  cook  •  clean up", BCX, y, 30, "#1F2D44", FONT_XB)


el(wt(3, "still"), b_, you_work, pivot=(BCX, Y0 + 395))
# S3 agent?
a_, b_ = S(3)
el(wt(4, "agent"), b_, lambda c, t, e: (icon_robot(c, BCX - 60, BCY + 10, 3.0), c.drawCircle(BCX + 120, BCY - 60, 50, P("#FFC93C")),
                                         text(c, "?", BCX + 120, BCY - 60, 70, "#1F2D44")), (BCX + 150, BCY - 80))
el(wt(4, "differently"), b_, lambda c, t, e: text(c, "What's different?", BCX, BCY + 190, 40, "#1F2D44"), pivot=(BCX, BCY + 190))
# S4 agent loop
a_, b_ = S(4)
NODES = [("GOAL", icon_target, (BCX - 250, Y0 + 70), ("goal", 0), "#FF4D6D"),
         ("STEPS", lambda c, x, y, k: icon_doc(c, x, y, k * 0.8), (BCX + 250, Y0 + 70), ("steps", 0), "#0A84FF"),
         ("USE TOOLS", None, (BCX + 250, Y0 + 300), ("tools", 0), "#8E44AD"),
         ("CHECK", icon_check, (BCX - 250, Y0 + 300), ("checks", 0), "#2ECC71")]
el(a_, b_, lambda c, t, e: chip(c, BCX, Y0 - 30, "AI AGENT", "#E91E63", lambda c_, x, y, k: icon_robot(c_, x, y + 4, k * 0.8, "#FFFFFF"), 26), (BCX + 140, Y0 - 30))
for j, (lab, ic, (x, y), (w, n), col) in enumerate(NODES):
    def node(c, t, e, lab=lab, ic=ic, x=x, y=y, col=col):
        r = rr(x - 170, y - 60, 340, 120, 30); shadow_rrect(c, r, 8, 5, 0.25); c.drawRRect(r, P("#FFFFFF")); c.drawRRect(r, P(col, 5))
        if ic:
            ic(c, x - 110, y, 1.0); text(c, lab, x - 60, y, 32, col, FONT_XB, "l")
        else:
            text(c, lab, x, y - 26, 30, col, FONT_XB)
    el(wt(5, w, n) - 0.05, b_, node, (x + 170, y - 40), (x, y))
for k_, (w, ic) in enumerate((("search", icon_search), ("calendars", icon_cal), ("email", icon_mail))):
    x, y = BCX + 250 - 90 + k_ * 90, Y0 + 322
    el(wt(5, w), b_, lambda c, t, e, ic=ic, x=x, y=y: ic(c, x, y, 0.85), None, (x, y))


def arrows(c, t, e):
    cols = ("#FF4D6D", "#0A84FF", "#8E44AD")
    segs = [((BCX - 70, Y0 + 70), (BCX + 70, Y0 + 70), wt(5, "steps")), ((BCX + 250, Y0 + 140), (BCX + 250, Y0 + 230), wt(5, "tools")),
            ((BCX + 70, Y0 + 300), (BCX - 70, Y0 + 300), wt(5, "checks")), ((BCX - 250, Y0 + 230), (BCX - 250, Y0 + 140), wt(5, "results"))]
    for k_, ((x0, y0), (x1, y1), ts) in enumerate(segs):
        u = smooth((t - ts) / 0.35)
        if u <= 0: continue
        xe, ye = x0 + (x1 - x0) * u, y0 + (y1 - y0) * u
        c.drawLine(x0, y0, xe, ye, P("#1F2D44", 6))
        if u > 0.95:
            d = math.atan2(y1 - y0, x1 - x0)
            p = skia.Path(); p.moveTo(x1, y1)
            p.lineTo(x1 - 22 * math.cos(d - 0.5), y1 - 22 * math.sin(d - 0.5)); p.lineTo(x1 - 22 * math.cos(d + 0.5), y1 - 22 * math.sin(d + 0.5)); p.close()
            c.drawPath(p, P("#1F2D44"))
    if t > wt(5, "results"):
        text(c, "repeat until done", BCX, Y0 + 210, 26, "#5B6B80", FONT_SB, a=fade(t, wt(5, "results")))


el(wt(5, "steps"), b_, arrows, None, (BCX, Y0 + 200), )
# S5 real example
a_, b_ = S(5)
el(wt(6, "real") - 0.1, b_, lambda c, t, e: chip(c, BCX, Y0 + 40, "REAL EXAMPLE", "#FF7A45"), (BCX + 200, Y0 + 40))
el(wt(7, "weekend") if wt(7, "weekend") < b_ else wt(6, "example"), b_,
   lambda c, t, e: (icon_suitcase(c, BCX, BCY + 30, 2.4), text(c, "Weekend trip", BCX, BCY + 180, 44, "#1F2D44")), (BCX + 120, BCY))
# S6 chatbot list vs agent actions
a_, b_ = S(6)
LX, RX = BCX - 270, BCX + 170
el(a_, b_, lambda c, t, e: (chip(c, LX, Y0 - 20, "CHATBOT", "#0A84FF", None, 26), chip(c, RX, Y0 - 20, "AI AGENT", "#E91E63", None, 26),
                            c.drawLine(BCX - 110, Y0 + 30, BCX - 110, BY + BH - 40, P("#1F2D44", 2, a=0.15))), pivot=(BCX, Y0))
el(wt(7, "list"), b_, lambda c, t, e: (icon_doc(c, LX, Y0 + 170, 2.6, 4), text(c, "a list of ideas", LX, Y0 + 300, 26, "#5B6B80", FONT_SB)), (LX + 80, Y0 + 120))
for j, (w, lab, ic) in enumerate((("weather", "Weather: Sunny", icon_sun), ("train", "Train: 9:40 AM", icon_train),
                                   ("hotel", "Hotel: in budget", lambda c, x, y, k: icon_suitcase(c, x, y + 4, k * 0.7)),
                                   ("drafts", "Plan: Ready!", lambda c, x, y, k: icon_doc(c, x, y, k * 0.8)))):
    y = Y0 + 70 + j * 98
    def act_row(c, t, e, lab=lab, ic=ic, y=y, w=w):
        row(c, RX, y, 440, lab, ic, 27)
        ck = appear(t, wt(7, w) + 0.35)
        if ck:
            scaled(c, RX + 185, y, ck); icon_check(c, RX + 185, y, 1.0); c.restore()
    el(wt(7, w), b_, act_row, (RX + 240, y - 30), (RX, y))
# S7 booking worry
a_, b_ = S(7)


def book_btn(c, t, e):
    r = rr(BCX - 230, BCY - 70, 460, 120, 60); shadow_rrect(c, r, 10, 6, 0.3); c.drawRRect(r, P("#2ECC71"))
    text(c, "BOOK & PAY", BCX, BCY - 10, 50, "#FFFFFF")
    # cursor approaching
    u = smooth((t - wt(8, "booking")) / 1.2)
    cx_, cy_ = BCX + 330 - 200 * u, BCY + 160 - 120 * u
    p = skia.Path(); p.moveTo(cx_, cy_); p.lineTo(cx_ + 14, cy_ + 48); p.lineTo(cx_ + 26, cy_ + 34); p.lineTo(cx_ + 46, cy_ + 50)
    p.lineTo(cx_ + 52, cy_ + 42); p.lineTo(cx_ + 34, cy_ + 26); p.lineTo(cx_ + 50, cy_ + 18); p.close()
    c.drawPath(p, P("#FFFFFF")); c.drawPath(p, P("#1F2D44", 4))


el(wt(8, "booking"), b_, book_btn, (BCX + 240, BCY - 60), (BCX, BCY))
el(wt(8, "asking"), b_, lambda c, t, e: (icon_warn(c, BCX - 300, BCY - 10, 1.5), text(c, "without asking?!", BCX, BCY + 150, 40, "#FF4D6D")), (BCX - 260, BCY - 80))
# S8 permission dialog
a_, b_ = S(8)


def dialog(c, t, e):
    r = rr(BCX - 360, Y0 - 50, 720, 400, 30); shadow_rrect(c, r, 12, 8, 0.3); c.drawRRect(r, P("#FFFFFF")); c.drawRRect(r, P("#0A84FF", 4))
    icon_lock(c, BCX - 290, Y0 + 10, 0.8)
    text(c, "Agent wants to:", BCX - 240, Y0 + 12, 32, "#1F2D44", FONT_XB, "l")


el(a_, b_, dialog, (BCX + 300, Y0 - 40), (BCX, Y0 + 150))
el(wt(9, "paying"), b_, lambda c, t, e: row(c, BCX, Y0 + 100, 600, "Pay for the hotel", lambda c_, x, y, k: icon_suitcase(c_, x, y + 4, k * 0.7), 28, "#FFF1B8"), (BCX + 300, Y0 + 80))
el(wt(9, "sending"), b_, lambda c, t, e: row(c, BCX, Y0 + 190, 600, "Send an email", icon_mail, 28, "#FFF1B8"), (BCX + 300, Y0 + 170))


def allow(c, t, e):
    y = Y0 + 290
    on = smooth((t - wt(9, "control") - 0.1) / 0.3)
    for k_, (lab, col) in enumerate((("DENY", "#B0BEC5"), ("ALLOW", "#2ECC71"))):
        x = BCX - 130 + k_ * 260
        r = rr(x - 110, y - 34, 220, 68, 34)
        hl = on if lab == "ALLOW" else 0
        c.drawRRect(r, P(col, a=0.35 + 0.65 * (hl if lab == "ALLOW" else 0.5)))
        text(c, lab, x, y, 28, "#1F2D44" if lab == "DENY" else "#FFFFFF")
    if on > 0:
        text(c, "You decide.", BCX, Y0 + 400, 36, "#0A84FF", a=on)


el(wt(9, "before"), b_, allow, (BCX + 260, Y0 + 260), (BCX, Y0 + 290))
# S9 mistakes
a_, b_ = S(9)
el(wt(10, "mistakes") - 0.15, b_, lambda c, t, e: (icon_warn(c, BCX, BCY - 70, 2.6), text(c, "Mistakes happen", BCX, BCY + 110, 44, "#1F2D44")), (BCX + 120, BCY - 120))


def wrong(c, t, e):
    row(c, BCX, BCY + 220, 520, "Train: 9:40 PM ?", icon_train, 28, "#FFE1E6")
    icon_x(c, BCX + 230, BCY + 220, 1.0)


el(wt(11, "yes"), b_, wrong, (BCX + 260, BCY + 190), (BCX, BCY + 220))
# S10 check their work
a_, b_ = S(10)
el(a_ + 0.1, b_, lambda c, t, e: (icon_search(c, BCX - 300, Y0 + 30, 2.4), text(c, "Check its work", BCX + 40, Y0 + 30, 46, "#1F2D44")), (BCX + 300, Y0))
for j, (w, lab) in enumerate((("work", "Dates right?"), ("just", "Prices OK?"), ("assistant", "Details correct?"))):
    y = Y0 + 150 + j * 100
    def chk(c, t, e, lab=lab, y=y, w=w):
        row(c, BCX, y, 560, lab, None, 30)
        ck = appear(t, wt(11, w) + 0.3)
        if ck:
            scaled(c, BCX + 240, y, ck); icon_check(c, BCX + 240, y, 1.1); c.restore()
    el(wt(11, w), b_, chk, (BCX + 300, y - 30), (BCX, y))
# S11 summary + follow
a_, b_ = S(11)
el(wt(12, "chatbot") - 0.05, b_, lambda c, t, e: card(c, BCX, Y0 + 60, 720, 110, "CHATBOT  =  ANSWERS", 44, lambda c_, x, y, k: icon_chat(c_, x, y, 0.9), accent="#0A84FF"), (BCX + 360, Y0 + 20))
el(wt(12, "agent") - 0.05, b_, lambda c, t, e: card(c, BCX, Y0 + 200, 720, 110, "AGENT  =  ACTS", 44, lambda c_, x, y, k: icon_robot(c_, x, y + 6, 0.85), accent="#E91E63"), (BCX + 360, Y0 + 160))


def follow(c, t, e):
    r = rr(BCX - 260, Y0 + 300, 520, 80, 40); c.drawRRect(r, P("#FFC300"))
    text(c, "FOLLOW FOR MORE", BCX, Y0 + 340, 38, "#1F2D44")


el(wt(13, "follow") - 0.05, b_, follow, (BCX + 280, Y0 + 300), (BCX, Y0 + 340))


def loop_card(c, t, e):
    r = rr(BX + 30, BY + 80, BW - 60, BH - 110, 26); c.drawRRect(r, P("#FFFFFF"))
    icon_chat(c, BCX - 250, BCY - 30, 2.0); icon_robot(c, BCX + 250, BCY - 20, 2.0)
    c.drawCircle(BCX, BCY, 60, P("#FFC93C")); text(c, "?", BCX, BCY, 70, "#1F2D44")
    text(c, "Just a fancy chatbot?", BCX, BCY + 170, 46, "#1F2D44")


el(wt(13, "next"), DUR + 1, loop_card, (BCX + 300, BCY - 100), (BCX, BCY))


def marker_pen(c, x, y, col="#1F2D44"):
    c.save(); c.translate(x, y); c.rotate(-38)
    body = rr(-12, -150, 24, 120, 10); c.drawRRect(body, P("#3A3F4B")); c.drawRRect(body, P("#1D1D1F", 4))
    c.drawRRect(rr(-13, -160, 26, 30, 8), P(col)); c.drawRRect(rr(-13, -160, 26, 30, 8), P("#1D1D1F", 4))
    tip = skia.Path(); tip.moveTo(-10, -30); tip.lineTo(10, -30); tip.lineTo(3, 0); tip.lineTo(-3, 0); tip.close()
    c.drawPath(tip, P("#C9CDD2")); c.drawPath(tip, P("#1D1D1F", 3.5))
    c.restore()


def draw_board_doodle(c, t):
    K.draw_board_frame(c)
    pen = None
    for (t_in, t_out, fn, anchor, pivot) in ELEMS:
        if t < t_in or (t_out is not None and t > t_out):
            continue
        prog = smooth((t - t_in) / 0.6)
        alpha = 1.0 if t_out is None else max(0.0, min(1.0, (t_out - t) / 0.22))
        px, py = pivot or anchor or (BCX, BCY)
        x_edge = BX + 10 + (BW - 20) * prog
        c.save(); c.clipRect(skia.Rect.MakeLTRB(BX - 60, BY - 60, x_edge, BY + BH + 60))
        if alpha < 1.0:
            c.saveLayerAlpha(None, int(255 * alpha))
        fn(c, t, 1.0)
        if alpha < 1.0:
            c.restore()
        c.restore()
        if prog < 1.0:
            pen = (x_edge, py)
    if pen:
        marker_pen(c, *pen)
    c.restore()


def draw_board(c, t):
    if doodle.ON:
        return draw_board_doodle(c, t)
    K.draw_board_frame(c)
    for (t_in, t_out, fn, anchor, pivot) in ELEMS:
        e = appear(t, t_in, t_out)
        if not e: continue
        px, py = pivot or anchor or (BCX, BCY)
        scaled(c, px, py, e); fn(c, t, e); c.restore()
    c.restore()


# ============================================================ drone path, shots, punches
bit_keys = [(0, (540, 60)), (0.6, (960, 860))]
idle = [(980, 860), (100, 860)]
lastt = 0.6
for (t_in, t_out, fn, anchor, pivot) in sorted(ELEMS, key=lambda e: e[0]):
    if anchor and t_in - lastt > 0.5:
        bit_keys.append((t_in + 0.2, (min(1000, anchor[0] + 40), max(200, anchor[1] - 40))))
        lastt = t_in
for i in range(len(LN)):
    bit_keys.append((LN[i]["end"] + 0.2, idle[i % 2]))
bit_keys.sort()
for tt, (x, y) in bit_keys:
    K.BITX.add(tt, x); K.BITY.add(tt, y)

SHOTS = [(0.0, "wide"), (wt(0, "fancy") - 0.1, "dad"),
         (ls(1) - 0.05, "teen"), (wt(1, "ask") - 0.1, "board"),
         (ls(2) - 0.05, "dad"), (wt(2, "pasta") - 0.1, "wide"),
         (ls(3) - 0.05, "teen"), (wt(3, "waits") - 0.1, "board"),
         (ls(4) - 0.05, "dad"),
         (ls(5) - 0.05, "teen"), (wt(5, "goal") - 0.1, "board"), (wt(5, "checks") - 0.1, "wide"),
         (ls(6) - 0.05, "dad"),
         (ls(7) - 0.05, "teen"), (wt(7, "list") - 0.1, "board"), (wt(7, "drafts") - 0.1, "wide"),
         (ls(8) - 0.05, "dad"), (wt(8, "booking") - 0.1, "board"),
         (ls(9) - 0.05, "teen"), (wt(9, "permission") - 0.1, "board"), (wt(9, "control") - 0.1, "wide"),
         (ls(10) - 0.05, "dad"), (wt(10, "mistakes") - 0.1, "board"),
         (ls(11) - 0.05, "teen"), (wt(11, "check") - 0.1, "board"),
         (ls(12) - 0.05, "wide"), (wt(12, "agent") - 0.1, "board"),
         (ls(13) - 0.05, "teen"), (wt(13, "follow") - 0.1, "wide"), (wt(13, "next") - 0.1, "board")]
CAMS = {"wide": (540, 960, 1.0, 1.05), "dad": (dad.x + 10, 1090, 1.95, 2.05), "teen": (teen.x - 10, 1150, 1.95, 2.05),
        "board": (540, 640, 1.08, 1.13)}
PUNCH = [wt(1, "not"), wt(5, "goal"), wt(8, "wow"), wt(9, "permission"), wt(12, "acts"), wt(13, "got")]

K.CHARS = [dad, teen]; K.SHOTS = SHOTS; K.CAMS = CAMS; K.PUNCH = PUNCH; K.LOGO_T = wt(13, "follow")
K.draw_board = draw_board
import char_line, bg_line
K.CHARMOD = char_line
K.draw_bg = bg_line.draw_bg
K.draw_board_frame = bg_line.draw_board_frame


def worker(args):
    out, fs = args
    for f in fs:
        K.render_frame(f).save(os.path.join(out, f"f{f + 1:04d}.png"), skia.kPNG)
    return len(fs)


if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    a = [x for x in sys.argv[2:]]
    frames = [int(x) for x in a] if a else list(range(NF))
    n = 4
    with Pool(n) as pool:
        print("rendered", sum(pool.map(worker, [(out, frames[i::n]) for i in range(n)])))
    pops = sorted(set(round(e[0], 3) for e in ELEMS if e[0] > 0.3))
    json.dump({"frames": NF, "pops": pops, "shots": [(t_, k) for t_, k in SHOTS]}, open(os.path.join(B, "shots.json"), "w"))
