# THE SOUTHERN WIRE - Variant B: Iraq as a wide banner lead, NATO + Gaza paired
# beneath it, brief column on the left at the foot. Layout B direction 2.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from wire import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry_b.png")
img = Image.new("RGB", (1024, 1024), CREAM)
d = ImageDraw.Draw(img)

def card(x, y, w, h, c, lead=False, wide=False):
    num, region, place, head, deck, src, cert, chip, sc = c
    d.rectangle([x, y, x + w, y + h], fill=(255, 253, 248), outline=WINE if lead else SILVERD, width=3 if lead else 1)
    if wide:
        scene(d, x + 3, y + 3, 300, h - 6, sc, num)
        tx = x + 316
        yy = y + 10
        d.text((tx, yy), f"{num}. {region} - {place.upper()}", font=F(ARCH, 12), fill=WINE2)
        yy += 18
        for ln in wrap(d, head, F(ARCH, 22), w - 332)[:3]:
            d.text((tx, yy), ln, font=F(ARCH, 22), fill=INK)
            yy += 27
        yy += 2
        for ln in wrap(d, deck, F(ARCHR, 12), w - 332)[:5]:
            d.text((tx, yy), ln, font=F(ARCHR, 12), fill=(60, 55, 50))
            yy += 15
        d.rectangle([tx, y + h - 24, tx + d.textlength(chip, font=F(ARCH, 10)) + 12, y + h - 7], fill=WINE)
        d.text((tx + 6, y + h - 21), chip, font=F(ARCH, 10), fill=(255, 255, 255))
        st = f"{src} - {cert}"
        d.text((x + w - 10 - d.textlength(st, font=F(ARCHR, 9)), y + h - 21), st, font=F(ARCHR, 9), fill=(90, 85, 80))
        return
    ih = int(h * (0.32 if lead else 0.30))
    scene(d, x + 3, y + 3, w - 6, ih, sc, num)
    yy = y + ih + 8
    d.text((x + 8, yy), f"{num}. {region} - {place.upper()}", font=F(ARCH, 11 if lead else 9), fill=WINE2)
    yy += 15 if lead else 13
    hf = F(ARCH, 16 if lead else 12)
    for ln in wrap(d, head, hf, w - 16)[:3 if lead else 2]:
        d.text((x + 8, yy), ln, font=hf, fill=INK)
        yy += 19 if lead else 15
    yy += 2
    df = F(ARCHR, 11 if lead else 8)
    if not lead:
        deck = deck.split(". ")[0] + "."
    for ln in wrap(d, deck, df, w - 16)[:5 if lead else 2]:
        d.text((x + 8, yy), ln, font=df, fill=(60, 55, 50))
        yy += 13 if lead else 10
    d.rectangle([x + 8, y + h - 22, x + 8 + d.textlength(chip, font=F(ARCH, 9)) + 10, y + h - 6], fill=WINE)
    d.text((x + 13, y + h - 19), chip, font=F(ARCH, 9), fill=(255, 255, 255))
    st = f"{src} - {cert}"
    d.text((x + w - 8 - d.textlength(st, font=F(ARCHR, 8)), y + h - 19), st, font=F(ARCHR, 8), fill=(90, 85, 80))

# header - centred masthead, silver date band
d.rectangle([0, 0, 1024, 40], fill=INK)
k = "EVERY STORY DATED - 37 STORIES CHECKED - 9 REGIONS"
d.text(((1024 - d.textlength(k, font=F(ARCH, 13))) / 2, 12), k, font=F(ARCH, 13), fill=SILVER)
m = "THE SOUTHERN WIRE"
d.text(((1024 - d.textlength(m, font=F(PLAY, 54))) / 2, 50), m, font=F(PLAY, 54), fill=WINE)
d.rectangle([0, 112, 1024, 158], fill=SILVER)
dt = "TUESDAY 25 NOVEMBER 2026"
d.text(((1024 - d.textlength(dt, font=F(ARCH, 34))) / 2, 120), dt, font=F(ARCH, 34), fill=WINE)
# numbers strip on wine
d.rectangle([0, 162, 1024, 196], fill=WINE)
for i, (val, lab) in enumerate(NUMBERS):
    x = 10 + i * 145
    d.text((x, 165), val, font=F(ARCH, 16), fill=GOLD)
    d.text((x, 184), wrap(d, lab, F(ARCHR, 8), 138)[0], font=F(ARCHR, 8), fill=SILVER)
# region strip light
d.rectangle([0, 198, 1024, 224], fill=(238, 232, 220))
x = 12
d.text((x, 205), "REGIONS:", font=F(ARCH, 11), fill=WINE)
x += 74
for name, col in REGIONS:
    tw = int(d.textlength(name, font=F(ARCH, 10))) + 14
    d.rectangle([x, 203, x + tw, 219], fill=col)
    d.text((x + 7, 205), name, font=F(ARCH, 10), fill=(255, 255, 255))
    x += tw + 7
# timeline reversed order emphasis
d.rectangle([0, 226, 1024, 252], fill=SILVER)
x = 12
d.text((x, 233), "TIMELINE:", font=F(ARCH, 11), fill=WINE)
x += 84
for when, what in TIMELINE:
    d.text((x, 230), when, font=F(ARCH, 10), fill=WINE2)
    d.text((x, 242), what, font=F(ARCHR, 8), fill=INK)
    x += 188
# Iraq wide banner lead
card(8, 256, 1008, 132, CARDS[0], lead=True, wide=True)
# NATO + Gaza paired leads
card(8, 396, 500, 156, CARDS[1], lead=True)
card(516, 396, 500, 156, CARDS[2], lead=True)
# grid 5 x 2 compact
for i, c in enumerate(CARDS[3:]):
    r, col = divmod(i, 5)
    card(8 + col * 202, 558 + r * 108, 196, 104, c)
# bottom swapped: also-on left, date check middle, map right
by = 780
d.rectangle([8, by, 448, 968], fill=(255, 253, 248), outline=SILVERD)
d.text((18, by + 6), "ALSO ON THE WIRE - BRIEF 14-37", font=F(ARCH, 11), fill=WINE)
for ci, half in enumerate((BRIEF[:12], BRIEF[12:])):
    bx = 18 + ci * 222
    yy = by + 26
    for num, txt in half:
        for wln in wrap(d, f"{num}. {txt}", F(ARCHR, 8), 214)[:2]:
            d.text((bx, yy), wln, font=F(ARCHR, 8), fill=INK)
            yy += 10
        yy += 3
d.rectangle([464, by, 686, 968], fill=WINE)
d.text((474, by + 6), "DATE CHECK - NOT TODAY", font=F(ARCH, 11), fill=GOLD)
yy = by + 28
for item in DATECHECK:
    for ln in wrap(d, "- " + item, F(ARCHR, 10), 204):
        d.text((474, yy), ln, font=F(ARCHR, 10), fill=SILVER)
        yy += 14
    yy += 6
d.rectangle([694, by, 1016, 968], fill=(233, 228, 218), outline=SILVERD)
d.text((704, by + 6), "DOTTED MAP - PIN = CARD NUMBER", font=F(ARCH, 10), fill=WINE)
for yy2 in range(by + 30, by + 150, 12):
    for xx in range(704, 1008, 12):
        d.ellipse([xx, yy2, xx + 2, yy2 + 2], fill=SILVERD)
pins = [(3, 850, 66), (1, 790, 40), (4, 866, 74), (2, 846, 62), (6, 820, 36), (8, 722, 92), (18, 820, 104), (10, 932, 58), (13, 962, 140), (14, 952, 122), (23, 894, 70), (25, 938, 88), (36, 730, 48)]
for num, px, py in pins:
    d.ellipse([px - 8, by + py - 8, px + 8, by + py + 8], fill=WINE)
    t = str(num)
    d.text((px - d.textlength(t, font=F(ARCH, 8)) / 2, by + py - 5), t, font=F(ARCH, 8), fill=(255, 255, 255))
d.text((704, by + 152), "Legend: pins mark card places - Iraq 3, Poland 1, Gaza 4", font=F(ARCHR, 8), fill=INK)
# footer
d.rectangle([0, 974, 1024, 1024], fill=INK)
d.text((16, 982), "Sources: RFE/RL - Al Jazeera - DW - Starlit Daily - Forbes - wire roundups - science wires - Indian wires", font=F(ARCHR, 10), fill=SILVER)
d.text((16, 998), "Original drawings - flat layered illustrations made for this page. Claims labelled as claims (Hormuz: Iran says).", font=F(ARCHR, 10), fill=SILVER)

img.save(OUT, optimize=True)
print("saved", OUT, os.path.getsize(OUT))
