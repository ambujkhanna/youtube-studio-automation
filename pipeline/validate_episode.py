"""Validate an episode JSON: schema, scene types, and that every cue word appears in its line."""
import json, re, sys
TYPES = {"title", "chat", "steps", "compare", "checklist", "big", "permission", "summary"}


def cues(sc):
    out = [sc.get("cue"), sc.get("sub_cue"), sc.get("allow_cue")]
    for key in ("items", "rows"):
        out += [it.get("cue") for it in sc.get(key, [])]
    for side in ("left", "right"):
        if isinstance(sc.get(side), dict):
            out += [it.get("cue") for it in sc[side].get("items", [])]
    return [c for c in out if c]


def check(path):
    ep = json.load(open(path)); errs = []
    for k in ("id", "title", "description", "hashtags", "lines"):
        if not ep.get(k): errs.append(f"missing {k}")
    if len(ep.get("title", "")) > 100: errs.append("title > 100 chars")
    for i, l in enumerate(ep["lines"]):
        if l.get("who") not in ("DAD", "TEEN"): errs.append(f"line {i}: who must be DAD or TEEN")
        words = [w.lower().strip(".,!?'\"") for w in l["text"].split()]
        sc = l.get("board")
        if sc and sc.get("type") not in TYPES: errs.append(f"line {i}: unknown board type {sc.get('type')}")
        for c in (cues(sc) if sc else []) + ([l["punch"]] if l.get("punch") else []):
            if not any(w.startswith(c.lower()) for w in words): errs.append(f"line {i}: cue '{c}' not in text")
    last = ep["lines"][-1]["text"].lower()
    if "follow" not in last and "subscribe" not in last: errs.append("last line has no Subscribe/Follow call-to-action")
    if ep.get("loop_card") and ep["loop_card"].get("cue", "next") not in last: errs.append("loop cue not in last line")
    return errs


if __name__ == "__main__":
    bad = 0
    for p in sys.argv[1:]:
        e = check(p); bad += bool(e)
        print(("OK   " if not e else "FAIL ") + p + ("" if not e else "\n  - " + "\n  - ".join(e)))
    sys.exit(1 if bad else 0)
