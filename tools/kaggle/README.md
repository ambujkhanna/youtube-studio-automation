# Kaggle notebook: realistic 3D art for AInation boards (free GPU)

- `art_ain_v1.ipynb`: 21 key visuals for ep023–ep043 (landscape, 2 versions each), FLUX.1-schnell (Apache 2.0), clean white/blue studio look, no text or logos, people only as hands.
- **Why:** the owner prefers realistic 3D art to raw photos (2026-11-22). A `photo` board with `"art": "<name>"` shows `assets/art/<name>_landscape.jpg` when it exists, and the reviewed raw photo only as the fallback (`pipeline/stock.py`).
- **Run:** Kaggle → Import Notebook → GPU T4 x2, Internet On, secret `HF_TOKEN` ticked → **Save Version → Save & Run All** → Output → `art_ain_v1.zip`.
  - If you run it by hand instead, download before stopping (stopping deletes the files).
  - A numpy `_slice` error means: stop the session and start a fresh one.
- **After the run:** the assistant checks every picture (corners, made-up letters, logos), picks the best version and saves it as `assets/art/<name>_landscape.jpg` with a manifest, then adds `"art"` to the matching boards. ep031 (`ain_jobs_ai`) and ep036 (`ain_health_scan`) are already linked.
- The kids channel's notebooks (backgrounds, icons) are in the kids repo's `tools/kaggle/`.
- **Done 2026-11-22:** `art_v3_both.ipynb` (merged run) made the pictures; 20 of 21 are installed in `assets/art/` (`ain_family_rules` rejected: Apple logo and made-up checklist text). `ain_health_scan` has its monitor text softly blurred.
