# THE SOUTHERN WIRE - v2 shared content + RICH full-scene drawing helpers.
# Rebuild v2 Akun 15: same concept/palette/cards as v1; illustrations redrawn
# as layered full scenes; decks full; source row never covered.
# All numbers and stories come only from ni25-pool.md (locked pool).
from PIL import Image, ImageDraw, ImageFont
import math

FD = "/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
def F(name, size):
    return ImageFont.truetype(FD + name, size)
PLAY = "PlayfairDisplay-Black.ttf"
PLAYB = "PlayfairDisplay-Bold.ttf"
ARCH = "Archivo-Bold.ttf"
ARCHR = "Archivo.ttf"

WINE = (91, 18, 32)
WINE2 = (122, 30, 46)
SILVER = (232, 230, 227)
SILVERD = (176, 178, 182)
CREAM = (247, 243, 236)
INK = (28, 24, 22)
GOLD = (198, 164, 92)
TEAL = (38, 110, 110)
BLUE = (52, 84, 138)
GREEN = (74, 120, 62)
RUST = (176, 92, 44)
PURPLE = (104, 74, 138)
SAND = (214, 196, 140)
SMOKE = (105, 100, 96)

CARDS = [
 (3, "MIDDLE EAST", "Iraq", "Baghdad orders Kurdish oilfields seized",
  "PM Ali al-Zaidi directs federal units to seize oilfields and crossings in Kurdish-run regions. President Barzani: Kurdistan will not submit to unconstitutional decisions.",
  "Starlit / wires", "REPORTED", "OILFIELDS ORDER", "oil"),
 (1, "EUROPE", "Poland", "NATO sends early-warning jets to Poland",
  "NATO plans an AWACS deployment in Poland after Russian missiles landed in Poland during an attack on Ukraine. Chancellor Merz vows complete support, Germany standing with Poland.",
  "Wire reports", "REPORTED", "AWACS TO POLAND", "jet"),
 (4, "MIDDLE EAST", "Gaza", "Drone strikes kill Hamas security chief",
  "Israeli drone strikes across Gaza killed a senior Hamas security official, three policemen and three siblings, one a child. Seven killed in the strikes.",
  "Al Jazeera", "REPORTED", "7 KILLED IN STRIKES", "drone"),
 (2, "MIDDLE EAST", "Strait of Hormuz", "Iran says 3 tankers hit by mines",
  "IRGC Navy claims three oil tankers were hit by naval mines in the Strait of Hormuz. Shipping concerns rise as the claim spreads. This is an Iranian claim, not confirmed.",
  "Iranian claim via wires", "CLAIMED", "3 TANKERS HIT - IRAN SAYS", "sea"),
 (6, "WORLD", "Ukraine", "700,000 Russian dead, new count finds",
  "New analysis finds more than 700000 Russian soldiers killed in the nearly five-year war on Ukraine. The count is an analysis, published by RFE/RL.",
  "RFE/RL", "REPORTED", "700,000+ KILLED", "count"),
 (8, "AMERICAS", "Colombia", "Car bomb injures at least 23 in Colombia",
  "A car bomb in Colombia injured at least 23 people. In Cartagena, armed men hold dozens hostage in a supermarket, a separate scare the same day.",
  "Wire reports", "REPORTED", "23 INJURED", "bomb"),
 (18, "AFRICA", "Senegal", "Senegal's AFCON title restored by CAS",
  "A CAS ruling gives Senegal its 2025 Africa Cup of Nations title back. The AFCON trophy returns after the court decision, ending the dispute.",
  "Wire reports", "REPORTED", "TITLE RESTORED", "trophy"),
 (10, "ASIA", "China", "Xiamen Airlines orders 50 Boeing jets",
  "Xiamen Airlines, a China Southern unit, agreed to acquire 50 Boeing 737-8 jets. The Boeing 737 order is one of the day's biggest deals.",
  "Wire reports", "REPORTED", "50 JETS ORDERED", "plane"),
 (13, "OCEANIA", "Australia", "12 coral species brought back on reef",
  "Great Barrier Reef genetic analysis resurrects 12 Acropora coral species. Reef diversity is wider than known, the science wires report.",
  "Science wires", "REPORTED", "12 SPECIES BACK", "coral"),
 (14, "OCEANIA", "Fiji", "Fiji declares disaster in dry spell",
  "The Fijian government declares a nationwide disaster amid an El Nino dry spell. Fiji braces as the dry spell deepens across the islands.",
  "Wire reports", "REPORTED", "DISASTER DECLARED", "island"),
 (23, "SOUTH ASIA", "Punjab", "Old allies reunite in Punjab alliance",
  "BJP and Shiromani Akali Dal announce an alliance for the 2027 Punjab elections, ending a six-year split. The Akali Dal pact reshapes the race.",
  "Indian wires", "REPORTED", "ALLIANCE AGAIN", "hands"),
 (25, "ASIA-PACIFIC", "Indonesia", "Indonesia's vice-president resigns",
  "Indonesia's Vice-President resigns amid political strain, a single-source report carried by Starlit. Reported as stated, with no added detail.",
  "Starlit", "REPORTED", "VP RESIGNS", "flag"),
 (36, "WORLD", "Nvidia", "Nvidia's $1 trillion Monday surge",
  "Monday close: Nvidia shares rose 31.5%, nearly $1 trillion of market value clawed back as Jensen Huang was reinstated as CEO, +$34 billion in a day (Forbes). Tag: MONDAY CLOSE.",
  "Forbes via wires", "REPORTED", "+31.5% MONDAY", "chart"),
]

BRIEF = [
 (5, "EU unveils new Russia sanctions"),
 (7, "5 Lynx KF41 vehicles reach Ukraine"),
 (9, "Gunmen hold dozens in Cartagena"),
 (11, "Madrid 5-1 PSV: Bellingham, Mbappe brace"),
 (12, "England win T20I; Fraser-McGurk 27 off 13"),
 (15, "Iran pharmacies run dry, doses cut"),
 (16, "Iran winter gas shortage, rationing 22 Nov"),
 (17, "Britain sanctions Houthis leaders"),
 (19, "Rebels pull back in DR Congo"),
 (20, "Nigerian emir suspended"),
 (21, "Sudan RSF commander defects"),
 (22, "Cameroon separatist in Norway court"),
 (24, "Bangladesh opens Guangzhou office"),
 (26, "Solomon Islands eye Australia treaty"),
 (27, "North Korea touts China ties"),
 (28, "Denmark court upholds ghetto law"),
 (29, "Sarkozy faces Libya-case trial"),
 (30, "Black Sea clash at the UN"),
 (31, "Shortwave school for Afghan girls"),
 (32, "Dimorphos shadow crosses Didymos"),
 (33, "PCE report due today - no figure yet"),
 (34, "US targets 7 firms; one Alibaba-owned"),
 (35, "Moscow buys inflatable decoys"),
 (37, "Storms target Thanksgiving travel"),
]

REGIONS = [
 ("EUROPE", BLUE), ("MIDDLE EAST", WINE2), ("AFRICA", RUST),
 ("AMERICAS", TEAL), ("ASIA", PURPLE), ("SOUTH ASIA", GREEN),
 ("ASIA-PACIFIC", (60, 130, 160)), ("OCEANIA", (170, 140, 40)), ("WORLD", INK),
]
NUMBERS = [
 ("700,000+", "Russian dead #6"), ("50", "Boeing jets #10"),
 ("12", "coral species #13"), ("7", "killed in Gaza #4"),
 ("23", "injured Colombia #8"), ("3", "tankers - Iran says #2"),
 ("+31.5%", "Nvidia Monday #36"),
]
TIMELINE = [
 ("22 NOV", "Iran power rationing began"),
 ("MON CLOSE", "Nvidia +31.5%, Huang back"),
 ("TUE 25 NOV", "PCE report due today"),
 ("TUE 25 NOV", "AWACS planned for Poland"),
 ("TUE 25 NOV", "Madrid 5-1 PSV, Mbappe brace"),
]
DATECHECK = [
 "Merkury mission news - 23 Nov, not today",
 "COP31 summit wrap - earlier, not today",
 "Liverpool 4-0 win - earlier, not today",
 "GTA VI launch hype - not news today",
]

def wrap(draw, text, font, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------- rich layered scene helpers ----------
def _sky(d, x, y, w, h, top, mid):
    d.rectangle([x, y, x + w, y + h * 0.55], fill=top)
    d.rectangle([x, y + h * 0.55, x + w, y + h * 0.72], fill=mid)

def _sun(d, cx, cy, r, col=(250, 220, 90)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)

def _cloud(d, cx, cy, s, col=(245, 245, 242)):
    d.ellipse([cx - 14 * s, cy - 5 * s, cx + 2 * s, cy + 5 * s], fill=col)
    d.ellipse([cx - 4 * s, cy - 9 * s, cx + 12 * s, cy + 4 * s], fill=col)
    d.ellipse([cx + 6 * s, cy - 4 * s, cx + 18 * s, cy + 5 * s], fill=col)

def _birds(d, x, y, n=3):
    for i in range(n):
        bx, by = x + i * 16, y + (i % 2) * 4
        d.arc([bx, by, bx + 7, by + 5], 200, 330, fill=INK, width=1)
        d.arc([bx + 6, by, bx + 13, by + 5], 210, 340, fill=INK, width=1)

def _buildings(d, x, y, w, base, col=(120, 110, 96), win=(250, 230, 160)):
    # skyline row sitting on baseline y (bottom), heights vary deterministically
    bx = x
    i = 0
    while bx < x + w - 12:
        bw = 14 + (i * 7) % 12
        bh = 16 + (i * 11) % 20
        d.rectangle([bx, y - bh, bx + bw, y], fill=col)
        for wy in range(int(y - bh) + 4, int(y) - 3, 7):
            for wx in range(int(bx) + 3, int(bx + bw) - 3, 6):
                d.rectangle([wx, wy, wx + 3, wy + 3], fill=win)
        bx += bw + 4
        i += 1

def _windows(d, x, y, w, h, col=(250, 230, 160)):
    for wy in range(int(y) + 4, int(y + h) - 3, 7):
        for wx in range(int(x) + 4, int(x + w) - 3, 7):
            d.rectangle([wx, wy, wx + 3, wy + 3], fill=col)

def scene2(d, x, y, w, h, kind, seed, pano=False):
    """Layered full scene: sky/backdrop -> midground place markers -> foreground subject."""
    gy = y + h * 0.72  # ground line
    if kind == "oil":
        _sky(d, x, y, w, h, (238, 205, 150), (228, 180, 120))
        _sun(d, x + w - 26, y + 14, 9)
        # Kurdish mountains backdrop
        d.polygon([(x, gy), (x + w * 0.3, y + h * 0.3), (x + w * 0.55, gy)], fill=(150, 120, 95))
        d.polygon([(x + w * 0.4, gy), (x + w * 0.75, y + h * 0.36), (x + w, gy)], fill=(165, 135, 105))
        d.rectangle([x, gy, x + w, y + h], fill=(196, 160, 105))
        # storage tanks
        for tx in (x + 8, x + 30):
            d.rectangle([tx, gy - 14, tx + 18, gy], fill=SILVERD, outline=INK)
            d.ellipse([tx, gy - 18, tx + 18, gy - 10], fill=(200, 200, 200), outline=INK)
        # pumpjacks x3 detailed
        for i, px in enumerate((x + w * 0.38, x + w * 0.58, x + w * 0.78)):
            d.polygon([(px, gy + 16), (px + 6, gy - 12), (px + 12, gy + 16)], outline=INK, width=2)
            d.line([px - 12, gy - 16, px + 22, gy - 8], fill=WINE, width=4)
            d.polygon([(px - 14, gy - 20), (px - 4, gy - 18), (px - 6, gy - 10), (px - 14, gy - 12)], fill=INK)
            d.rectangle([px + 16, gy - 10, px + 24, gy + 2], fill=WINE2)
        # pipeline across foreground
        d.rectangle([x + 4, gy + 18, x + w - 4, gy + 22], fill=(90, 90, 95))
        for px in range(int(x + 14), int(x + w - 8), 34):
            d.rectangle([px, gy + 14, px + 4, gy + 26], fill=(90, 90, 95))
        _birds(d, x + 14, y + 8)
    elif kind == "jet":
        _sky(d, x, y, w, h, (170, 200, 232), (200, 218, 238))
        _cloud(d, x + 30, y + 12, 1); _cloud(d, x + w - 44, y + 9, 1)
        d.rectangle([x, gy, x + w, y + h], fill=(140, 145, 150))
        d.rectangle([x, gy + 8, x + w, gy + 11], fill=(240, 240, 240))
        for px in range(int(x + 6), int(x + w - 6), 26):
            d.rectangle([px, gy + 16, px + 12, gy + 18], fill=(240, 240, 240))
        # AWACS: fuselage, radome disc, wings, tail, cockpit
        cx, cy = x + w // 2, y + h * 0.42
        d.ellipse([cx - w * 0.34, cy - 8, cx + w * 0.34, cy + 9], fill=(225, 228, 232), outline=INK)
        d.polygon([(cx + w * 0.30, cy - 6), (cx + w * 0.40, cy - 2), (cx + w * 0.30, cy + 3)], fill=BLUE)
        d.ellipse([cx - 15, cy - 24, cx + 15, cy - 13], fill=(200, 204, 208), outline=INK)
        d.rectangle([cx - 2, cy - 14, cx + 2, cy - 8], fill=INK)
        d.polygon([(cx - 6, cy + 4), (cx - 30, cy + 20), (cx - 14, cy + 20), (cx + 8, cy + 6)], fill=BLUE)
        d.polygon([(cx + 6, cy + 4), (cx + 30, cy + 20), (cx + 14, cy + 20), (cx - 8, cy + 6)], fill=BLUE)
        d.polygon([(cx - w * 0.33, cy - 6), (cx - w * 0.38, cy - 22), (cx - w * 0.30, cy - 20), (cx - w * 0.28, cy - 6)], fill=WINE2)
        for wx in range(int(cx - w * 0.22), int(cx + w * 0.22), 11):
            d.ellipse([wx, cy - 3, wx + 4, cy + 1], fill=INK)
        # radar arcs + ground blocks
        for r in (18, 26):
            d.arc([cx - r, cy - 26 - r // 2, cx + r, cy - 20 + r // 2], 200, 340, fill=WINE2, width=1)
        d.rectangle([x + 10, gy - 10, x + 34, gy], fill=(110, 110, 115))
        _windows(d, x + 10, gy - 10, 24, 10, (200, 220, 240))
        d.rectangle([x + w - 40, gy - 8, x + w - 12, gy], fill=(110, 110, 115))
    elif kind == "drone":
        _sky(d, x, y, w, h, (216, 200, 180), (198, 180, 160))
        _buildings(d, x + 4, gy + 2, w * 0.55, gy, (130, 118, 104))
        _buildings(d, x + w * 0.55, gy + 2, w * 0.42, gy, (112, 102, 92))
        d.rectangle([x, gy, x + w, y + h], fill=(168, 152, 130))
        # sea edge at right
        d.rectangle([x + w * 0.8, gy, x + w, y + h], fill=TEAL)
        # smoke plume from a rooftop
        sx = x + w * 0.3
        for i, r in enumerate((5, 8, 11, 14)):
            d.ellipse([sx - r + i * 3, gy - 34 - i * 9, sx + r + i * 3, gy - 22 - i * 9], fill=SMOKE)
        # drone foreground with 4 rotors + camera
        cx, cy = x + w * 0.62, y + h * 0.3
        d.rectangle([cx - 20, cy - 4, cx + 20, cy + 3], fill=INK)
        for dx in (-24, -9, 9, 24):
            d.line([cx + dx, cy - 4, cx + dx, cy - 9], fill=INK, width=2)
            d.ellipse([cx + dx - 7, cy - 12, cx + dx + 7, cy - 8], fill=WINE)
        d.ellipse([cx - 4, cy + 3, cx + 4, cy + 10], fill=WINE2, outline=INK)
        d.line([cx, cy + 10, cx, cy + 16], fill=INK, width=1)
    elif kind == "sea":
        _sky(d, x, y, w, h, (190, 214, 230), (214, 228, 238))
        _sun(d, x + 22, y + 12, 8)
        # two headlands framing the strait
        d.polygon([(x, y + h * 0.34), (x + w * 0.3, y + h * 0.52), (x, y + h * 0.62)], fill=(150, 128, 96))
        d.polygon([(x + w, y + h * 0.3), (x + w * 0.72, y + h * 0.5), (x + w, y + h * 0.6)], fill=(140, 118, 88))
        d.rectangle([x, y + h * 0.52, x + w, y + h], fill=TEAL)
        for wy in range(int(y + h * 0.58), int(y + h) - 3, 9):
            for wx in range(int(x + 6), int(x + w - 14), 30):
                d.arc([wx, wy, wx + 14, wy + 5], 0, 180, fill=(120, 190, 195), width=1)
        # 3 tankers: hull, deck, bridge tower, containers
        for i, (tx, ty, s) in enumerate(((x + w * 0.14, y + h * 0.6, 1.0), (x + w * 0.44, y + h * 0.68, 1.25), (x + w * 0.74, y + h * 0.58, 0.85))):
            L = int(52 * s)
            d.polygon([(tx, ty), (tx + L, ty), (tx + L - 8, ty + 9 * s), (tx + 6, ty + 9 * s)], fill=(52, 52, 56))
            d.rectangle([tx + 4, ty - 5 * s, tx + L - 14, ty], fill=WINE)
            d.rectangle([tx + L - 13, ty - 13 * s, tx + L - 5, ty], fill=SILVERD, outline=INK)
            for cxp in range(int(tx + 8), int(tx + L - 18), 9):
                d.rectangle([cxp, ty - 5 * s, cxp + 6, ty - 1], fill=(90, 120, 160) if (cxp // 9) % 2 else RUST)
        # naval mines: spiked circles in foreground water
        for mx, my in ((x + w * 0.3, y + h * 0.86), (x + w * 0.58, y + h * 0.9), (x + w * 0.85, y + h * 0.84)):
            d.ellipse([mx - 6, my - 6, mx + 6, my + 6], fill=INK)
            for a in range(0, 360, 45):
                d.line([mx, my, mx + int(9 * math.cos(math.radians(a))), my + int(9 * math.sin(math.radians(a)))], fill=INK, width=2)
        # red buoy
        d.polygon([(x + w * 0.06, y + h * 0.8), (x + w * 0.06 + 8, y + h * 0.8), (x + w * 0.06 + 4, y + h * 0.8 - 10)], fill=(200, 40, 40))
    elif kind == "count":
        _sky(d, x, y, w, h, (196, 198, 205), (214, 212, 205))
        d.rectangle([x, gy - 6, x + w, y + h], fill=(120, 118, 100))
        # rows of helmet markers receding across a field
        for r in range(4):
            ry = gy + 2 + r * (h * 0.07)
            n = 9 - r
            for i in range(n):
                mx = x + 12 + i * ((w - 24) / max(n - 1, 1)) + r * 6
                s = 3 + r
                d.rectangle([mx - 1, ry, mx + 1, ry + s + 3], fill=INK)
                d.arc([mx - s, ry - s, mx + s, ry + s], 180, 360, fill=(70, 74, 60), width=2)
        # distant ruined skyline
        _buildings(d, x + 4, gy - 4, w - 8, gy, (140, 138, 132), (210, 205, 190))
        _birds(d, x + w - 50, y + 7)
    elif kind == "bomb":
        _sky(d, x, y, w, h, (226, 208, 188), (214, 196, 172))
        _buildings(d, x + 4, gy + 2, w * 0.4, gy, (150, 130, 110))
        _buildings(d, x + w * 0.62, gy + 2, w * 0.36, gy, (140, 122, 102))
        d.rectangle([x, gy, x + w, y + h], fill=(110, 105, 100))
        d.rectangle([x, gy + 10, x + w, gy + 12], fill=(230, 230, 225))
        # supermarket block centre-back (Cartagena marker)
        d.rectangle([x + w * 0.42, gy - 22, x + w * 0.62, gy], fill=(235, 232, 225), outline=INK)
        _windows(d, x + w * 0.42, gy - 22, w * 0.2, 22, TEAL)
        d.rectangle([x + w * 0.42, gy - 28, x + w * 0.62, gy - 22], fill=TEAL)
        # damaged car foreground: body, cabin, wheels, cracked glass
        cx, cy = x + w * 0.3, gy + 8
        d.rectangle([cx - 34, cy, cx + 34, cy + 12], fill=RUST, outline=INK)
        d.polygon([(cx - 20, cy), (cx - 10, cy - 11), (cx + 14, cy - 11), (cx + 24, cy)], fill=RUST, outline=INK)
        d.polygon([(cx - 9, cy - 9), (cx - 1, cy - 9), (cx - 1, cy - 1), (cx - 15, cy - 1)], fill=(170, 200, 215))
        d.polygon([(cx + 2, cy - 9), (cx + 12, cy - 9), (cx + 20, cy - 1), (cx + 2, cy - 1)], fill=(170, 200, 215))
        d.line([cx + 2, cy - 9, cx + 12, cy - 1], fill=INK, width=1)
        for wx in (cx - 22, cx + 22):
            d.ellipse([wx - 7, cy + 8, wx + 7, cy + 20], fill=INK)
            d.ellipse([wx - 3, cy + 11, wx + 3, cy + 17], fill=SILVERD)
        # smoke + debris
        for i, r in enumerate((4, 7, 10)):
            d.ellipse([cx + 18 - r, cy - 26 - i * 7, cx + 18 + r, cy - 18 - i * 7], fill=SMOKE)
        for dx in (-40, 44, 52):
            d.polygon([(cx + dx, cy + 16), (cx + dx + 6, cy + 12), (cx + dx + 9, cy + 17)], fill=(90, 85, 80))
    elif kind == "trophy":
        # stadium: stand bands with crowd dots, floodlights, pitch
        d.rectangle([x, y, x + w, y + h * 0.6], fill=(70, 74, 96))
        for ry in range(int(y + 5), int(y + h * 0.55), 7):
            for rx in range(int(x + 4), int(x + w - 4), 7):
                d.ellipse([rx, ry, rx + 2, ry + 2], fill=(220, 190, 90) if (rx + ry) % 3 else (200, 200, 210))
        for fx in (x + 10, x + w - 16):
            d.line([fx + 3, y + h * 0.55, fx + 3, y + 8], fill=SILVERD, width=2)
            d.ellipse([fx - 2, y + 3, fx + 9, y + 10], fill=(250, 240, 180))
        d.rectangle([x, y + h * 0.6, x + w, y + h], fill=GREEN)
        d.line([x, y + h * 0.6, x + w, y + h * 0.6], fill=(240, 240, 240), width=2)
        d.ellipse([x + w / 2 - 16, y + h * 0.62, x + w / 2 + 16, y + h * 0.86], outline=(240, 240, 240), width=2)
        # trophy centre
        cx, cy = x + w // 2, y + h * 0.52
        d.polygon([(cx - 13, cy - 22), (cx + 13, cy - 22), (cx + 8, cy - 2), (cx - 8, cy - 2)], fill=GOLD, outline=INK)
        d.arc([cx - 22, cy - 22, cx - 6, cy - 4], 90, 270, fill=GOLD, width=3)
        d.arc([cx + 6, cy - 22, cx + 22, cy - 4], 270, 90, fill=GOLD, width=3)
        d.rectangle([cx - 3, cy - 2, cx + 3, cy + 6], fill=(150, 120, 50))
        d.rectangle([cx - 11, cy + 6, cx + 11, cy + 11], fill=INK)
        # green-white ribbon + confetti
        d.polygon([(cx - 10, cy - 22), (cx - 4, cy - 22), (cx - 7, cy - 10)], fill=GREEN)
        d.polygon([(cx + 10, cy - 22), (cx + 4, cy - 22), (cx + 7, cy - 10)], fill=(240, 240, 240))
        for i in range(14):
            px = x + 8 + (i * 37) % max(int(w - 16), 1)
            py = y + 6 + (i * 23) % max(int(h * 0.4), 1)
            d.rectangle([px, py, px + 3, py + 2], fill=(230, 120, 90) if i % 2 else GOLD)
    elif kind == "plane":
        _sky(d, x, y, w, h, (176, 206, 234), (206, 226, 242))
        _cloud(d, x + w - 40, y + 10, 1)
        # terminal building with glass band + tower
        d.rectangle([x + 6, gy - 20, x + w * 0.4, gy], fill=(205, 210, 215), outline=INK)
        _windows(d, x + 6, gy - 20, w * 0.4 - 6, 20, (110, 160, 200))
        d.rectangle([x + w * 0.3, gy - 34, x + w * 0.36, gy - 20], fill=(190, 195, 200), outline=INK)
        d.rectangle([x, gy, x + w, y + h], fill=(130, 133, 138))
        d.rectangle([x, gy + 12, x + w, gy + 14], fill=(245, 245, 240))
        # Boeing 737 foreground: fuselage, window row, tail, wing, engines
        cx, cy = x + w * 0.56, gy - 2
        d.ellipse([cx - w * 0.3, cy - 13, cx + w * 0.3, cy + 6], fill=(238, 240, 243), outline=INK)
        d.polygon([(cx + w * 0.24, cy - 10), (cx + w * 0.35, cy - 4), (cx + w * 0.24, cy + 2)], fill=(240, 240, 243), outline=INK)
        d.polygon([(cx - w * 0.28, cy - 10), (cx - w * 0.33, cy - 30), (cx - w * 0.22, cy - 28), (cx - w * 0.18, cy - 10)], fill=BLUE, outline=INK)
        d.polygon([(cx - 4, cy + 2), (cx - 26, cy + 16), (cx - 12, cy + 16), (cx + 14, cy + 4)], fill=SILVERD, outline=INK)
        d.ellipse([cx - 2, cy + 8, cx + 12, cy + 17], fill=(90, 95, 100), outline=INK)
        for wx in range(int(cx - w * 0.2), int(cx + w * 0.2), 10):
            d.ellipse([wx, cy - 7, wx + 4, cy - 3], fill=(60, 90, 130))
        d.rectangle([cx - w * 0.3, cy - 3, cx + w * 0.28, cy], fill=BLUE)
        # jet bridge + luggage cart
        d.rectangle([x + w * 0.42, gy - 16, x + w * 0.5, gy - 10], fill=(180, 182, 186), outline=INK)
        d.rectangle([x + w * 0.78, gy + 8, x + w * 0.78 + 18, gy + 14], fill=GOLD, outline=INK)
        d.ellipse([x + w * 0.78 + 2, gy + 13, x + w * 0.78 + 7, gy + 18], fill=INK)
        d.ellipse([x + w * 0.78 + 11, gy + 13, x + w * 0.78 + 16, gy + 18], fill=INK)
    elif kind == "coral":
        # underwater: surface, light rays, seabed, layered coral garden, fish
        d.rectangle([x, y, x + w, y + h], fill=(70, 150, 175))
        d.rectangle([x, y, x + w, y + 5], fill=(190, 230, 235))
        for i, rx in enumerate((x + w * 0.2, x + w * 0.5, x + w * 0.8)):
            d.polygon([(rx, y + 5), (rx + 8, y + 5), (rx - 4, y + h * 0.6)], fill=(150, 210, 215))
        d.rectangle([x, y + h * 0.8, x + w, y + h], fill=(196, 178, 130))
        cols = [(224, 110, 80), (240, 150, 90), (200, 90, 110), (250, 190, 90)]
        for i, ox in enumerate(range(int(x + 12), int(x + w - 8), max(16, int(w // 6)))):
            col = cols[i % 4]
            base = y + h * 0.92
            d.line([ox, base, ox, base - 20], fill=col, width=4)
            d.line([ox, base - 10, ox - 9, base - 24], fill=col, width=3)
            d.line([ox, base - 13, ox + 9, base - 27], fill=col, width=3)
            d.line([ox - 9, base - 24, ox - 13, base - 32], fill=col, width=2)
            d.line([ox + 9, base - 27, ox + 14, base - 34], fill=col, width=2)
            d.ellipse([ox - 3, base - 36, ox + 3, base - 30], fill=col)
        # brain-coral mounds + fish silhouettes
        for mx in (x + w * 0.3, x + w * 0.66):
            d.ellipse([mx - 12, y + h * 0.8, mx + 12, y + h * 0.94], fill=(170, 130, 160))
            d.arc([mx - 8, y + h * 0.82, mx + 8, y + h * 0.92], 0, 360, fill=(130, 95, 125), width=1)
        for i, (fx, fy) in enumerate(((x + w * 0.24, y + h * 0.3), (x + w * 0.6, y + h * 0.22), (x + w * 0.78, y + h * 0.38))):
            d.ellipse([fx - 6, fy - 3, fx + 6, fy + 3], fill=(250, 200, 80) if i % 2 else (240, 140, 90))
            d.polygon([(fx + 5, fy), (fx + 10, fy - 3), (fx + 10, fy + 3)], fill=(250, 200, 80) if i % 2 else (240, 140, 90))
            d.ellipse([fx - 4, fy - 1, fx - 2, fy + 1], fill=INK)
        for bx in range(int(x + 16), int(x + w - 10), 28):
            d.ellipse([bx, y + h * 0.14, bx + 3, y + h * 0.14 + 3], outline=(220, 245, 248))
    elif kind == "island":
        _sky(d, x, y, w, h, (250, 214, 130), (248, 190, 110))
        _sun(d, x + w - 24, y + 13, 10, (255, 180, 60))
        d.rectangle([x, y + h * 0.55, x + w, y + h], fill=(90, 160, 170))
        for wx in range(int(x + 6), int(x + w - 16), 30):
            d.arc([wx, y + h * 0.86, wx + 14, y + h * 0.86 + 5], 0, 180, fill=(190, 225, 225), width=1)
        # dry island: cracked earth foreground of the sand spit
        d.ellipse([x + w * 0.14, y + h * 0.52, x + w * 0.86, y + h * 0.8], fill=(222, 198, 138))
        d.ellipse([x + w * 0.2, y + h * 0.58, x + w * 0.8, y + h * 0.76], fill=(206, 178, 116))
        for i in range(6):
            sx = x + w * 0.26 + i * w * 0.09
            d.line([sx, y + h * 0.66, sx + 8, y + h * 0.7], fill=(150, 124, 78), width=1)
            d.line([sx + 8, y + h * 0.7, sx + 3, y + h * 0.74], fill=(150, 124, 78), width=1)
        # palms x3, one leaning dry
        for px, lean in ((x + w * 0.34, 0), (x + w * 0.55, 4), (x + w * 0.72, -3)):
            top = (px + lean, y + h * 0.3)
            d.line([px, y + h * 0.62, top[0], top[1]], fill=(120, 92, 55), width=4)
            for a in (-50, -20, 10, 40, 70):
                ex = top[0] + int(15 * math.cos(math.radians(a - 90)))
                ey = top[1] + int(10 * math.sin(math.radians(a - 90))) + 4
                d.line([top[0], top[1], ex, ey], fill=GREEN if lean == 0 else (150, 150, 80), width=2)
            d.ellipse([top[0] - 3, top[1] + 1, top[0] + 2, top[1] + 6], fill=(120, 92, 55))
        # water tank + hut (disaster markers)
        d.rectangle([x + w * 0.06, y + h * 0.44, x + w * 0.16, y + h * 0.58], fill=SILVERD, outline=INK)
        d.rectangle([x + w * 0.82, y + h * 0.46, x + w * 0.95, y + h * 0.6], fill=(235, 228, 210), outline=INK)
        d.polygon([(x + w * 0.8, y + h * 0.46), (x + w * 0.885, y + h * 0.36), (x + w * 0.97, y + h * 0.46)], fill=WINE2)
    elif kind == "hands":
        # hall backdrop: arch + two banner panels (saffron / blue party colours)
        d.rectangle([x, y, x + w, y + h], fill=(238, 230, 214))
        d.rectangle([x, y, x + w * 0.3, y + h], fill=(240, 150, 60))
        d.rectangle([x + w * 0.7, y, x + w, y + h], fill=BLUE)
        d.arc([x + w * 0.3, y + 4, x + w * 0.7, y + h * 0.7], 180, 360, fill=GOLD, width=3)
        d.rectangle([x, y + h * 0.78, x + w, y + h], fill=(206, 190, 160))
        # two forearms in different sleeves meeting in a handshake
        cy = y + h * 0.52
        d.polygon([(x, cy - 12), (x + w * 0.42, cy - 5), (x + w * 0.42, cy + 13), (x, cy + 18)], fill=(250, 248, 244), outline=INK)
        d.polygon([(x + w, cy - 12), (x + w * 0.58, cy - 5), (x + w * 0.58, cy + 13), (x + w, cy + 18)], fill=(60, 60, 66), outline=INK)
        d.ellipse([x + w * 0.4, cy - 9, x + w * 0.56, cy + 10], fill=(196, 150, 100), outline=INK)
        d.ellipse([x + w * 0.46, cy - 6, x + w * 0.62, cy + 13], fill=(150, 110, 76), outline=INK)
        for fx in range(4):
            d.line([x + w * 0.47 + fx * 4, cy + 8, x + w * 0.45 + fx * 4, cy + 15], fill=(150, 110, 76), width=2)
        # gold clasp band + marigold dots
        d.rectangle([x + w * 0.47, cy - 11, x + w * 0.53, cy - 6], fill=GOLD)
        for i in range(8):
            px = x + 10 + (i * 29) % max(int(w - 20), 1)
            d.ellipse([px, y + h * 0.84, px + 4, y + h * 0.84 + 4], fill=(245, 170, 40))
    elif kind == "flag":
        _sky(d, x, y, w, h, (186, 210, 232), (214, 228, 240))
        _cloud(d, x + 26, y + 10, 1)
        _buildings(d, x + 4, gy + 4, w - 8, gy, (150, 155, 165), (220, 230, 240))
        d.rectangle([x, gy, x + w, y + h], fill=(150, 148, 140))
        # podium steps + speaker silhouette
        cx = x + w * 0.34
        d.rectangle([cx - 26, gy + 12, cx + 26, gy + 17], fill=(120, 118, 112))
        d.rectangle([cx - 18, gy + 5, cx + 18, gy + 12], fill=(140, 138, 132))
        d.rectangle([cx - 7, gy - 14, cx + 7, gy + 5], fill=INK)
        d.ellipse([cx - 5, gy - 23, cx + 5, gy - 13], fill=(196, 150, 100))
        d.line([cx + 5, gy - 8, cx + 16, gy - 14], fill=INK, width=3)
        # tall flagpole, waving red-over-white flag
        fx = x + w * 0.68
        d.line([fx, y + 6, fx, gy + 14], fill=INK, width=3)
        d.ellipse([fx - 3, y + 3, fx + 3, y + 9], fill=GOLD)
        wave = [(fx, y + 8), (fx + w * 0.16, y + 5), (fx + w * 0.26, y + 10), (fx + w * 0.26, y + 20), (fx + w * 0.14, y + 17), (fx, y + 20)]
        d.polygon(wave, fill=(240, 240, 240), outline=INK)
        d.polygon(wave[:3] + [(fx + w * 0.14, y + 14), (fx, y + 14)], fill=(205, 40, 45))
        _birds(d, x + w - 52, y + 8)
    else:  # chart - trading floor / office scene
        d.rectangle([x, y, x + w, y + h], fill=(36, 44, 58))
        # window skyline behind glass
        d.rectangle([x + 6, y + 5, x + w - 6, y + h * 0.52], fill=(90, 120, 150))
        _buildings(d, x + 8, y + h * 0.52, w - 16, y, (60, 84, 108), (250, 230, 150))
        # big monitor with candlesticks + rising line
        mx, my, mw, mh = x + w * 0.08, y + h * 0.14, w * 0.52, h * 0.52
        d.rectangle([mx, my, mx + mw, my + mh], fill=(16, 24, 30), outline=SILVERD)
        for i in range(5):
            cxp = mx + 8 + i * (mw - 16) / 4
            top = my + mh - 8 - i * (mh - 18) / 4
            d.line([cxp, top - 6, cxp, top + 10], fill=(90, 220, 130), width=1)
            d.rectangle([cxp - 3, top, cxp + 3, top + 7], fill=(90, 220, 130))
        pts = [(mx + 6, my + mh - 8), (mx + mw * 0.4, my + mh * 0.5), (mx + mw - 8, my + 8)]
        d.line(pts, fill=GOLD, width=2)
        d.polygon([(mx + mw - 14, my + 6), (mx + mw - 4, my + 6), (mx + mw - 6, my + 14)], fill=GOLD)
        # desk, keyboard slab, coin stacks
        d.rectangle([x, y + h * 0.78, x + w, y + h], fill=(70, 54, 40))
        d.rectangle([x + w * 0.16, y + h * 0.84, x + w * 0.5, y + h * 0.9], fill=(24, 24, 26))
        for i, sx in enumerate((x + w * 0.68, x + w * 0.8, x + w * 0.9)):
            for j in range(3 - (i % 2)):
                d.ellipse([sx, y + h * 0.88 - j * 5, sx + 13, y + h * 0.88 - j * 5 + 5], fill=GOLD, outline=(150, 120, 50))
        d.rectangle([x + w * 0.66, y + h * 0.3, x + w * 0.94, y + h * 0.52], fill=(16, 24, 30), outline=SILVERD)
        for i in range(4):
            bx = x + w * 0.69 + i * w * 0.06
            bh = (i + 2) * h * 0.045
            d.rectangle([bx, y + h * 0.5 - bh, bx + w * 0.04, y + h * 0.5], fill=(90, 220, 130) if i > 1 else (220, 110, 90))


# ---------- shared page furniture (same system as v1) ----------
def header_block(d):
    d.rectangle([0, 0, 1024, 40], fill=WINE)
    d.text((16, 12), "37 STORIES CHECKED - 9 REGIONS - EVERY STORY DATED TUESDAY 25 NOVEMBER 2026", font=F(ARCH, 13), fill=SILVER)
    d.text((16, 50), "THE SOUTHERN WIRE", font=F(PLAY, 54), fill=WINE)
    d.text((1024 - 16 - d.textlength("WINE & SILVER EDITION", font=F(ARCH, 12)), 78), "WINE & SILVER EDITION", font=F(ARCH, 12), fill=(110, 105, 100))
    d.rectangle([0, 112, 1024, 158], fill=WINE2)
    d.text((16, 120), "TUESDAY 25 NOVEMBER 2026", font=F(ARCH, 34), fill=(255, 255, 255))
    d.text((1024 - 16 - d.textlength("ONE DAY - ONE FRONT PAGE", font=F(ARCH, 13)), 128), "ONE DAY - ONE FRONT PAGE", font=F(ARCH, 13), fill=SILVER)
    d.rectangle([0, 162, 1024, 196], fill=SILVER)
    for i, (val, lab) in enumerate(NUMBERS):
        x = 10 + i * 145
        d.text((x, 165), val, font=F(ARCH, 16), fill=WINE)
        d.text((x, 184), wrap(d, lab, F(ARCHR, 8), 138)[0], font=F(ARCHR, 8), fill=INK)
    d.rectangle([0, 198, 1024, 224], fill=INK)
    x = 12
    d.text((x, 205), "REGIONS:", font=F(ARCH, 11), fill=SILVER)
    x += 74
    for name, col in REGIONS:
        tw = int(d.textlength(name, font=F(ARCH, 10))) + 14
        d.rectangle([x, 203, x + tw, 219], fill=col)
        d.text((x + 7, 205), name, font=F(ARCH, 10), fill=(255, 255, 255))
        x += tw + 7
    d.rectangle([0, 226, 1024, 252], fill=(238, 232, 220))
    x = 12
    d.text((x, 233), "TIMELINE:", font=F(ARCH, 11), fill=WINE)
    x += 84
    for when, what in TIMELINE:
        d.text((x, 230), when, font=F(ARCH, 10), fill=WINE2)
        d.text((x, 242), what, font=F(ARCHR, 8), fill=INK)
        x += 188

def bottom_block(d, by):
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
    d.rectangle([0, 974, 1024, 1024], fill=WINE)
    d.text((16, 982), "Sources: RFE/RL - Al Jazeera - DW - Starlit Daily - Forbes - wire roundups - science wires - Indian wires", font=F(ARCHR, 10), fill=SILVER)
    d.text((16, 998), "Original drawings - full layered scenes drawn for this page. Claims labelled as claims (Hormuz: Iran says).", font=F(ARCHR, 10), fill=SILVER)
