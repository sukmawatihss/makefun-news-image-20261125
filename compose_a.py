# THE SOUTHERN WIRE - Variant A: lead trio as a top row, grid 5 x 2 below.
# Layout B direction 1. Rendered locally with PIL; entry.png is copied by main.py.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from wire import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry_a.png")
img = Image.new("RGB", (1024, 1024), CREAM)
d = ImageDraw.Draw(img)

def card(x, y, w, h, c, lead=False):
    num, region, place, head, deck, src, cert, chip, sc = c
    d.rectangle([x, y, x + w, y + h], fill=(255, 253, 248), outline=WINE if lead else SILVERD, width=3 if lead else 1)
    ih = int(h * (0.34 if lead else 0.26))
    scene(d, x + 3, y + 3, w - 6, ih, sc, num)
    yy = y + ih + 8
    d.text((x + 8, yy), f"{num}. {region} - {place.upper()}", font=F(ARCH, 11 if lead else 9), fill=WINE2)
    yy += 15 if lead else 13
    hf = F(ARCH, 17 if lead else 12)
    for ln in wrap(d, head, hf, w - 16)[:3]:
        d.text((x + 8, yy), ln, font=hf, fill=INK)
        yy += 20 if lead else 15
    yy += 2
    df = F(ARCHR, 11 if lead else 8)
    if not lead:
        deck = deck.split(". ")[0] + "."
    maxl = 6 if lead else 2
    for ln in wrap(d, deck, df, w - 16)[:maxl]:
        d.text((x + 8, yy), ln, font=df, fill=(60, 55, 50))
        yy += 13 if lead else 10
    # chip + source at bottom
    d.rectangle([x + 8, y + h - 22, x + 8 + d.textlength(chip, font=F(ARCH, 9)) + 10, y + h - 6], fill=WINE)
    d.text((x + 13, y + h - 19), chip, font=F(ARCH, 9), fill=(255, 255, 255))
    st = f"{src} - {cert}"
    d.text((x + w - 8 - d.textlength(st, font=F(ARCHR, 8)), y + h - 19), st, font=F(ARCHR, 8), fill=(90, 85, 80))

# header
d.rectangle([0, 0, 1024, 40], fill=WINE)
d.text((16, 12), "37 STORIES CHECKED - 9 REGIONS - EVERY STORY DATED TUESDAY 25 NOVEMBER 2026", font=F(ARCH, 13), fill=SILVER)
d.text((16, 50), "THE SOUTHERN WIRE", font=F(PLAY, 54), fill=WINE)
d.text((1024 - 16 - d.textlength("WINE & SILVER EDITION", font=F(ARCH, 12)), 78), "WINE & SILVER EDITION", font=F(ARCH, 12), fill=(110, 105, 100))
d.rectangle([0, 112, 1024, 158], fill=WINE2)
d.text((16, 120), "TUESDAY 25 NOVEMBER 2026", font=F(ARCH, 34), fill=(255, 255, 255))
d.text((1024 - 16 - d.textlength("ONE DAY - ONE FRONT PAGE", font=F(ARCH, 13)), 128), "ONE DAY - ONE FRONT PAGE", font=F(ARCH, 13), fill=SILVER)
# numbers strip - fixed columns so labels never collide
d.rectangle([0, 162, 1024, 196], fill=SILVER)
for i, (val, lab) in enumerate(NUMBERS):
    x = 10 + i * 145
    d.text((x, 165), val, font=F(ARCH, 16), fill=WINE)
    d.text((x, 184), wrap(d, lab, F(ARCHR, 8), 138)[0], font=F(ARCHR, 8), fill=INK)
# region strip
d.rectangle([0, 198, 1024, 224], fill=INK)
x = 12
d.text((x, 205), "REGIONS:", font=F(ARCH, 11), fill=SILVER)
x += 74
for name, col in REGIONS:
    tw = int(d.textlength(name, font=F(ARCH, 10))) + 14
    d.rectangle([x, 203, x + tw, 219], fill=col)
    d.text((x + 7, 205), name, font=F(ARCH, 10), fill=(255, 255, 255))
    x += tw + 7
# timeline
d.rectangle([0, 226, 1024, 252], fill=(238, 232, 220))
x = 12
d.text((x, 233), "TIMELINE:", font=F(ARCH, 11), fill=WINE)
x += 84
for when, what in TIMELINE:
    d.text((x, 230), when, font=F(ARCH, 10), fill=WINE2)
    d.text((x, 242), what, font=F(ARCHR, 8), fill=INK)
    x += 188
# lead trio
for i, c in enumerate(CARDS[:3]):
    card(8 + i * 338, 256, 330, 216, c, lead=True)
# grid 5 x 2
for i, c in enumerate(CARDS[3:]):
    r, col = divmod(i, 5)
    card(8 + col * 202, 478 + r * 148, 196, 142, c)
# bottom: map + date check + also on
by = 778
d.rectangle([8, by, 330, 968], fill=(233, 228, 218), outline=SILVERD)
d.text((16, by + 6), "DOTTED MAP - PIN = CARD NUMBER", font=F(ARCH, 10), fill=WINE)
for yy in range(by + 30, by + 180, 12):
    for xx in range(16, 322, 12):
        d.ellipse([xx, yy, xx + 2, yy + 2], fill=SILVERD)
pins = [(3, 180, 70), (1, 120, 44), (4, 196, 78), (2, 176, 66), (6, 150, 40), (8, 52, 96), (18, 150, 108), (10, 262, 62), (13, 292, 148), (14, 282, 128), (23, 224, 74), (25, 268, 92), (36, 60, 52)]
for num, px, py in pins:
    d.ellipse([px - 8, by + py - 8, px + 8, by + py + 8], fill=WINE)
    t = str(num)
    d.text((px - d.textlength(t, font=F(ARCH, 8)) / 2, by + py - 5), t, font=F(ARCH, 8), fill=(255, 255, 255))
d.text((16, by + 168), "Legend: pins mark card places - Iraq 3, Poland 1, Gaza 4, Hormuz 2", font=F(ARCHR, 8), fill=INK)
d.rectangle([338, by, 560, 968], fill=WINE)
d.text((348, by + 6), "DATE CHECK - NOT TODAY", font=F(ARCH, 11), fill=GOLD)
yy = by + 28
for item in DATECHECK:
    for ln in wrap(d, "- " + item, F(ARCHR, 10), 204):
        d.text((348, yy), ln, font=F(ARCHR, 10), fill=SILVER)
        yy += 14
    yy += 6
d.text((348, yy + 4), "Excluded on purpose:", font=F(ARCH, 10), fill=GOLD)
d.text((348, yy + 20), "old stories never dress", font=F(ARCHR, 10), fill=SILVER)
d.text((348, yy + 34), "as today's news.", font=F(ARCHR, 10), fill=SILVER)
d.rectangle([568, by, 1016, 968], fill=(255, 253, 248), outline=SILVERD)
d.text((578, by + 6), "ALSO ON THE WIRE - BRIEF 14-37", font=F(ARCH, 11), fill=WINE)
for ci, half in enumerate((BRIEF[:12], BRIEF[12:])):
    bx = 578 + ci * 222
    yy = by + 26
    for num, txt in half:
        for wln in wrap(d, f"{num}. {txt}", F(ARCHR, 8), 214)[:2]:
            d.text((bx, yy), wln, font=F(ARCHR, 8), fill=INK)
            yy += 10
        yy += 3
# footer
d.rectangle([0, 974, 1024, 1024], fill=WINE)
d.text((16, 982), "Sources: RFE/RL - Al Jazeera - DW - Starlit Daily - Forbes - wire roundups - science wires - Indian wires", font=F(ARCHR, 10), fill=SILVER)
d.text((16, 998), "Original drawings - flat layered illustrations made for this page. Claims labelled as claims (Hormuz: Iran says).", font=F(ARCHR, 10), fill=SILVER)

img.save(OUT, optimize=True)
print("saved", OUT, os.path.getsize(OUT))
