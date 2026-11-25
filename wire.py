# THE SOUTHERN WIRE - shared content and drawing helpers for NI25 Akun 15.
# All numbers and stories come only from ni25-pool.md (locked pool).
from PIL import Image, ImageDraw, ImageFont
import textwrap

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

# card: num, region, place, headline, deck, source, certainty, chip, scene
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

def scene(draw, x, y, w, h, kind, seed):
    # flat layered illustration filling the strip
    sky = (222, 214, 200) if seed % 2 == 0 else (208, 216, 224)
    draw.rectangle([x, y, x + w, y + h], fill=sky)
    draw.rectangle([x, y + h * 0.68, x + w, y + h], fill=(168, 158, 140))
    cx, cy = x + w // 2, y + h // 2
    if kind == "oil":
        for i, ox in enumerate(range(x + 8, x + w - 10, max(18, w // 4))):
            draw.rectangle([ox, cy - 14, ox + 5, cy + 16], fill=WINE)
            draw.line([ox - 8, cy - 20, ox + 14, cy - 20], fill=INK, width=3)
            draw.line([ox + 2, cy - 20, ox + 2, cy - 12], fill=INK, width=2)
        draw.ellipse([cx - 12, cy + 6, cx + 12, cy + 18], fill=(40, 40, 40))
    elif kind == "jet":
        draw.polygon([(x + 10, cy + 6), (cx + 10, cy - 16), (x + w - 8, cy + 2), (cx, cy + 10)], fill=BLUE)
        draw.ellipse([cx - 16, cy - 22, cx + 16, cy - 6], fill=SILVERD, outline=INK)
        draw.polygon([(x + 14, cy + 8), (x + 30, cy - 8), (x + 36, cy + 8)], fill=WINE2)
    elif kind == "drone":
        draw.rectangle([cx - 22, cy - 6, cx + 22, cy + 2], fill=INK)
        for dx in (-26, 26):
            draw.ellipse([cx + dx - 9, cy - 16, cx + dx + 9, cy - 8], fill=WINE)
        draw.line([cx, cy + 2, cx, cy + 18], fill=INK, width=2)
        draw.rectangle([x + 8, y + h - 18, x + 40, y + h - 6], fill=(120, 110, 96))
        draw.rectangle([x + w - 44, y + h - 24, x + w - 10, y + h - 6], fill=(120, 110, 96))
    elif kind == "sea":
        draw.rectangle([x, y + h * 0.45, x + w, y + h], fill=TEAL)
        for i in range(3):
            draw.polygon([(x + 20 + i * (w // 3), cy + 4), (x + 44 + i * (w // 3), cy - 18), (x + 68 + i * (w // 3), cy + 4)], fill=(60, 60, 60))
            draw.rectangle([x + 26 + i * (w // 3), cy + 2, x + 62 + i * (w // 3), cy + 10], fill=WINE)
    elif kind == "count":
        for i in range(6):
            bx = x + 10 + i * max(14, w // 7)
            draw.rectangle([bx, cy - 12, bx + 8, cy + 14], fill=INK)
            draw.ellipse([bx, cy - 20, bx + 8, cy - 12], fill=SILVERD)
    elif kind == "bomb":
        draw.rectangle([x + 12, cy + 2, x + 52, cy + 16], fill=RUST)
        draw.ellipse([x + 16, cy + 12, x + 26, cy + 22], fill=INK)
        draw.ellipse([x + 38, cy + 12, x + 48, cy + 22], fill=INK)
        for a in range(0, 360, 45):
            import math
            ex = cx + 26 + int(20 * math.cos(math.radians(a)))
            ey = cy - 8 + int(14 * math.sin(math.radians(a)))
            draw.line([cx + 26, cy - 8, ex, ey], fill=GOLD, width=2)
    elif kind == "trophy":
        draw.polygon([(cx - 14, cy - 18), (cx + 14, cy - 18), (cx + 8, cy + 2), (cx - 8, cy + 2)], fill=GOLD, outline=INK)
        draw.rectangle([cx - 3, cy + 2, cx + 3, cy + 10], fill=INK)
        draw.rectangle([cx - 12, cy + 10, cx + 12, cy + 15], fill=INK)
    elif kind == "plane":
        draw.polygon([(x + 8, cy), (x + w - 20, cy - 10), (x + w - 8, cy), (x + w - 20, cy + 8), (x + 20, cy + 6)], fill=SILVERD, outline=INK)
        draw.polygon([(cx, cy - 2), (cx + 16, cy - 18), (cx + 26, cy - 2)], fill=BLUE)
        draw.polygon([(x + 16, cy), (x + 26, cy - 14), (x + 34, cy)], fill=WINE2)
    elif kind == "coral":
        for i, ox in enumerate(range(x + 12, x + w - 8, max(16, w // 5))):
            draw.line([ox, y + h - 6, ox, cy + 4], fill=RUST, width=3)
            draw.line([ox, cy + 10, ox - 7, cy - 2], fill=RUST, width=2)
            draw.line([ox, cy + 8, ox + 7, cy - 4], fill=(210, 120, 90), width=2)
        draw.rectangle([x, y + h * 0.55, x + w, y + h], fill=(90, 160, 170))
    elif kind == "island":
        draw.rectangle([x, y + h * 0.5, x + w, y + h], fill=(90, 160, 170))
        draw.ellipse([cx - 34, cy + 2, cx + 34, cy + 18], fill=(214, 196, 140))
        draw.line([cx, cy + 4, cx, cy - 16], fill=GREEN, width=3)
        draw.polygon([(cx, cy - 16), (cx - 12, cy - 6), (cx + 12, cy - 6)], fill=GREEN)
        draw.ellipse([x + w - 34, y + 6, x + w - 10, y + 20], fill=(250, 220, 90))
    elif kind == "hands":
        draw.ellipse([cx - 26, cy - 8, cx - 4, cy + 14], fill=(196, 150, 100), outline=INK)
        draw.ellipse([cx + 4, cy - 8, cx + 26, cy + 14], fill=(150, 110, 76), outline=INK)
        draw.rectangle([cx - 8, cy - 2, cx + 8, cy + 8], fill=GOLD)
    elif kind == "flag":
        draw.line([cx - 20, cy - 18, cx - 20, cy + 18], fill=INK, width=3)
        draw.polygon([(cx - 20, cy - 18), (cx + 22, cy - 10), (cx - 20, cy - 2)], fill=(200, 40, 40))
        draw.rectangle([cx - 20, cy - 2, cx + 22, cy + 6], fill=(240, 240, 240))
        draw.rectangle([cx - 20, cy + 6, cx + 22, cy + 14], fill=(30, 30, 30))
    else:  # chart
        pts = [(x + 10, cy + 14), (x + w // 3, cy + 6), (cx, cy + 10), (x + w - 14, cy - 16)]
        draw.line(pts, fill=GREEN, width=3)
        for px, py in pts:
            draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=WINE)
        draw.line([x + 8, y + h - 8, x + w - 8, y + h - 8], fill=INK, width=2)
