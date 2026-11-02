"""Render the line-art character design sheet (stills only)."""
import skia, char_line as CL
class Ch:
    def __init__(s, name, ph): s.name = name; s.ph = ph
POSE = {"rest": (9, 4, "rest"), "explain": (24, -112, "open"), "palms": (38, 96, "open"), "point": (128, 150, "point"),
        "wave": (128, 168, "open"), "fist": (38, 172, "fist"), "chin": (12, -142, "fist")}
def arms(l, r): return {-1: POSE[l], 1: POSE[r]}
W, H = 2500, 1560
surf = skia.Surface(W, H); c = surf.getCanvas(); c.clear(CL.hexc("#FAF7F0"))
TF = skia.Typeface.MakeFromFile("/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf")
def label(t, x, y, sz=34):
    f = skia.Font(TF, sz); w = f.measureText(t); c.drawString(t, x - w / 2, y, f, CL.P("#1D1D1F"))
dad, teen = Ch("DAD", 0.0), Ch("TEEN", 2.0)
def face(op=0.0, wd=1.0, bl=0.0, bu=0.0, bt=0.0, sm=0.4, yaw=0, pitch=0):
    return {"bounce": 0, "roll": 0, "vals": (yaw, pitch, 0, op, wd, bl, bu, bt, sm)}
poses = [(dad, arms("rest", "rest"), face(), "Dad - neutral"), (dad, arms("rest", "explain"), face(0.6, 1.0, bu=0.4, sm=0.5), "Dad - talking"),
         (dad, arms("rest", "chin"), face(sm=0.2, bu=0.6, bt=0.5, yaw=8, pitch=-6), "Dad - thinking"),
         (teen, arms("rest", "rest"), face(), "Teen - neutral"), (teen, arms("explain", "point"), face(0.7, 1.0, bu=0.5, sm=0.7, yaw=-8, pitch=-8), "Teen - pointing"),
         (teen, arms("wave", "rest"), face(sm=0.95, bu=0.6), "Teen - waving")]
for i, (ch, ar, fc, lab) in enumerate(poses):
    x = 200 + i * 400 + (60 if i >= 3 else 0)
    c.drawLine(x - 170, 1040, x + 170, 1040, CL.P("#D8D2C4", 4))
    CL.draw(c, ch, 0.0, fc, ar, 1.0, x, 1040)
    label(lab, x, 1100)
exprs = [("Happy", face(sm=0.8, bu=0.3)), ("Talking", face(0.65, 1.0, bu=0.3, sm=0.5)), ("Surprised", face(0.75, 0.6, bu=1.0, bt=0.6, sm=0.0)),
         ("Worried", face(0.0, 1.0, bu=-0.5, bt=-0.8, sm=-0.4)), ("Excited", face(0.5, 1.1, sm=0.95, bu=0.6))]
for j, ch in enumerate((dad, teen)):
    for i, (lab, fc) in enumerate(exprs):
        x = 160 + (i + j * 5) * 228; y = 1370
        c.save(); c.translate(x, y); c.scale(0.6, 0.6)
        if ch.name == "TEEN":
            CL.back_hair(c, ch, 0.0, CL.SPEC[ch.name], fc["vals"])
        CL.head(c, ch, 0.0, CL.SPEC[ch.name], fc["vals"]); c.restore()
        label(lab, x, y + 150, 24)
surf.makeImageSnapshot().save("../chars/line_sheet.png", skia.kPNG)
print("ok")
