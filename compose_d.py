# THE SOUTHERN WIRE - Rebuild v2 Variant D: panorama-led scenes.
# Same three fixes as C, different emphasis: taller panoramic lead scenes,
# tighter grid typography. Chip badge sits on the scene; the source +
# certainty row stands alone at the card foot, never covered.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from wire2 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry_d.png")
img = Image.new("RGB", (1024, 1024), CREAM)
d = ImageDraw.Draw(img)

def badge(x, y, w, chip, big=False):
    fnt = F(ARCH, 9 if big else 8)
    cw = d.textlength(chip, font=fnt) + 10
    d.rectangle([x + w - cw - 5, y + 5, x + w - 5, y + (21 if big else 18)], fill=INK)
    d.text((x + w - cw, y + (8 if big else 7)), chip, font=fnt, fill=(255, 255, 255))

def card(x, y, w, h, c, lead=False):
    num, region, place, head, deck, src, cert, chip, sc = c
    d.rectangle([x, y, x + w, y + h], fill=(255, 253, 248), outline=WINE if lead else SILVERD, width=3 if lead else 1)
    ih = 60 if lead else 40
    sub = Image.new("RGB", (w - 6, ih), (255, 255, 255))
    scene2(ImageDraw.Draw(sub), 0, 0, w - 6, ih, sc, num, pano=True)
    img.paste(sub, (x + 3, y + 3))
    badge(x, y, w, chip, big=lead)
    yy = y + ih + 9
    d.text((x + 8, yy), f"{num}. {region} - {place.upper()}", font=F(ARCH, 11 if lead else 10), fill=WINE2)
    yy += 15 if lead else 13
    hf = F(ARCH, 15 if lead else 11)
    for ln in wrap(d, head, hf, w - 16)[:2]:
        d.text((x + 8, yy), ln, font=hf, fill=INK)
        yy += 18 if lead else 13
    yy += 2
    df = F(ARCHR, 10 if lead else 8)
    lh = 12 if lead else 9
    maxl = (y + h - 24 - yy) // lh
    for ln in wrap(d, deck, df, w - 16)[:int(maxl)]:
        d.text((x + 8, yy), ln, font=df, fill=(60, 55, 50))
        yy += lh
    st = f"{src} - {cert}"
    d.text((x + 8, y + h - 16), st, font=F(ARCH, 8), fill=(90, 30, 40))

header_block(d)
for i, c in enumerate(CARDS[:3]):
    card(8 + i * 338, 256, 330, 184, c, lead=True)
for i, c in enumerate(CARDS[3:]):
    r, col = divmod(i, 5)
    card(8 + col * 202, 448 + r * 162, 196, 154, c)
bottom_block(d, 770)

img.save(OUT, optimize=True)
print("saved", OUT, os.path.getsize(OUT))
