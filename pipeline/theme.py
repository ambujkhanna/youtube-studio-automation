"""AInation look (repo variable THEME):
  classic       the original living room (default until the owner picks a studio look)
  studio_light  clean studio: soft grey-white wall, no room props, white board card, one blue accent
  studio_dark   the same in deep navy, with a soft glow behind the white board card
  studio_open   light studio without any board frame (content directly on the wall)

Only AInation uses this; The CurioKids Club never sets THEME.
"""
import os

THEME = os.environ.get("THEME", "classic").strip().lower()
STUDIO = THEME in ("studio_light", "studio_dark", "studio_open")
DARK = THEME == "studio_dark"
OPEN = THEME == "studio_open"   # light studio with no board frame: content sits on the wall, like an infographic

ACCENT = "#2F6BFF"        # the one accent colour
ACCENT_2 = "#7C5CFF"      # a quieter second accent (used sparingly)
INK = "#1B2437"           # text on the white board
MUTED = "#6B778C"
CARD = "#FFFFFF"
CARD_LINE = "#E3E8F0"

# backgrounds
WALL = ("#0F1934", "#0A1024") if DARK else ("#F7F9FC", "#E9EEF6")
FLOOR = ("#0B1226", "#080D1C") if DARK else ("#E4E9F2", "#D9E0EB")
DOTS = "#3E5BA8" if DARK else "#1B2437"
LOGO_TEXT = "#FFFFFF" if DARK else "#1B2437"

# caption highlight per speaker (ASS colours are &HAABBGGRR)
HL = {"DAD": "&H00FF8C3C&", "TEEN": "&H00FFC879&"} if STUDIO else None   # blue / light blue


def pill_colour(col):
    """Studio looks use one accent for every pill; classic keeps the board's own colour."""
    return ACCENT if STUDIO else col


def tint(col):
    """Studio looks draw cards white (with a hairline border) instead of pastel tints."""
    return CARD if STUDIO else col
