"""Line-art room + board frame matching the line-art characters."""
import math
import skia
import kit2d as K
from char_line import P, ell, hexc, INK

W = K.W
BX, BY, BW, BH = K.BX, K.BY, K.BW, K.BH
FLOOR = 1560


def outline_rr(c, x, y, w, h, r, fill, lw=6):
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r)
    c.drawRRect(rr, P(fill)); c.drawRRect(rr, P(INK, lw))


def draw_bg(c, t):
    # wall + floor
    c.drawRect(skia.Rect.MakeLTRB(-600, -600, W + 600, FLOOR), P("#FAF7F0"))
    for i in range(-6, 20):  # faint wallpaper stripes
        c.drawLine(i * 90, -600, i * 90, FLOOR, P("#EFE9DD", 3))
    c.drawRect(skia.Rect.MakeLTRB(-600, FLOOR, W + 600, 2600), P("#E9DFCC"))
    for k in range(-6, 22):  # floorboards
        c.drawLine(k * 110, FLOOR, k * 110 - 140, 2400, P("#DCCFB6", 3))
    c.drawLine(-600, FLOOR, W + 600, FLOOR, P(INK, 6))
    # rug
    c.drawOval(ell(540, 1690, 450, 62), P("#FFE08A")); c.drawOval(ell(540, 1690, 450, 62), P(INK, 5))
    c.drawOval(ell(540, 1690, 400, 46), P("#F2B600", 3))
    # shelf + books (left)
    for i, (w_, h_, col) in enumerate(((28, 96, "#FF6B6B"), (24, 80, "#3A86FF"), (32, 104, "#FFD23F"), (22, 72, "#7BD389"))):
        bx = 26 + sum(v for v in (32, 28, 36, 26)[:i])
        outline_rr(c, bx, 1006 - h_, w_, h_, 4, col, 4)
    outline_rr(c, 6, 1006, 210, 16, 5, "#FFFFFF", 5)
    # clock (right)
    c.drawCircle(990, 960, 50, P("#FFFFFF")); c.drawCircle(990, 960, 50, P(INK, 6))
    for i in range(12):
        a = i * math.pi / 6
        c.drawLine(990 + math.cos(a) * 36, 960 + math.sin(a) * 36, 990 + math.cos(a) * 42, 960 + math.sin(a) * 42, P(INK, 3))
    c.drawLine(990, 960, 990 + math.sin(t * 0.6) * 32, 960 - math.cos(t * 0.6) * 32, P(INK, 4))
    c.drawLine(990, 960, 990 + math.sin(t * 0.05 + 1) * 22, 960 - math.cos(t * 0.05 + 1) * 22, P(INK, 6))
    # plant (left)
    c.save(); c.translate(80, FLOOR)
    for k, (ang, ln) in enumerate(((-30, 250), (-8, 300), (14, 270), (36, 210), (-50, 180))):
        c.save(); c.rotate(ang + math.sin(t * 1.3 + k) * 2.5)
        lp = skia.Path(); lp.moveTo(0, -70); lp.quadTo(-40, -70 - ln * 0.5, 0, -70 - ln); lp.quadTo(40, -70 - ln * 0.5, 0, -70); lp.close()
        c.drawPath(lp, P("#7BD389")); c.drawPath(lp, P(INK, 5)); c.drawLine(0, -80, 0, -60 - ln * 0.9, P(INK, 3))
        c.restore()
    pot = skia.Path(); pot.moveTo(-60, -130); pot.lineTo(60, -130); pot.lineTo(46, 0); pot.lineTo(-46, 0); pot.close()
    c.drawPath(pot, P("#FF8C5A")); c.drawPath(pot, P(INK, 6))
    c.restore()
    # lamp (right)
    c.save(); c.translate(1010, FLOOR)
    c.drawLine(0, 0, 0, -520, P(INK, 8)); c.drawOval(ell(0, 0, 56, 10), P(INK))
    sh = skia.Path(); sh.moveTo(-66, -520); sh.lineTo(66, -520); sh.lineTo(40, -616); sh.lineTo(-40, -616); sh.close()
    c.drawPath(sh, P("#FFD23F")); c.drawPath(sh, P(INK, 6))
    c.restore()
    K.logo(c, 540, 84, 0.95 * (1.0 + (0.18 * math.sin(min(1.0, max(0.0, (t - K.LOGO_T) / 0.5)) * math.pi) if t > K.LOGO_T else 0.0)), tcol="#1D1D1F")


def draw_board_frame(c):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX, BY, BW, BH), 34, 34)
    sh = P("#000000", a=0.10); sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.save(); c.translate(8, 12); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, P("#FFFFFF")); c.drawRRect(r, P(INK, 8))
    inner = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX + 4, BY + 4, BW - 8, BH - 8), 30, 30)
    c.save(); c.clipRRect(inner, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(BX, BY, BW, 66), P("#FFE08A"))
    c.drawLine(BX, BY + 66, BX + BW, BY + 66, P(INK, 5))
    for i, col in enumerate(("#FF6B6B", "#FFD23F", "#7BD389")):
        c.drawCircle(BX + 46 + i * 30, BY + 34, 9, P(col)); c.drawCircle(BX + 46 + i * 30, BY + 34, 9, P(INK, 3))
    K.text(c, "AI EXPLAINED", BX + BW - 36, BY + 34, 24, "#1D1D1F", K.FONT_XB, "r")
