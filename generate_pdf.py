#!/usr/bin/env python3
"""
Generátor PDF příručky "Šestinedělí s klidem"
Verze 2: opravená interpunkce + vektorové ilustrace
"""
import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.graphics.shapes import (
    Drawing, Circle, Rect, Line, Ellipse, Path, Group,
    String, Polygon,
)
from reportlab.graphics import renderPDF

# ── BARVY ─────────────────────────────────────────────────────────────────────
BLUSH_500 = HexColor('#E85D5D')
BLUSH_300 = HexColor('#F9ADAD')
BLUSH_200 = HexColor('#FCCFCF')
BLUSH_100 = HexColor('#FDE8E8')
SAGE_500  = HexColor('#5A8A53')
SAGE_400  = HexColor('#7DA876')
SAGE_300  = HexColor('#A8C4A2')
SAGE_200  = HexColor('#CFDECB')
SAGE_100  = HexColor('#EAF0E8')
CREAM_200 = HexColor('#FDF3D3')
CREAM_100 = HexColor('#FEF9EC')
AMBER_100 = HexColor('#FEF3C7')
AMBER_300 = HexColor('#FCD34D')
WARM_900  = HexColor('#3D3530')
WARM_600  = HexColor('#6B5E58')
WARM_400  = HexColor('#9C8880')

PAGE_W, PAGE_H = A4

# ── ILUSTRACE (vektorové kresby pro každou kapitolu) ──────────────────────────

def draw_illustration(c, chapter_num: int, x: float, y: float, w: float, h: float):
    """Nakreslí ilustraci pro danou kapitolu na pozici (x,y) s rozměry (w,h)."""
    c.saveState()
    c.translate(x, y)
    fns = [
        _illus_body, _illus_breastfeeding, _illus_sleep, _illus_emotions,
        _illus_baby_care, _illus_nutrition, _illus_couple, _illus_home,
        _illus_visitors, _illus_recovery, _illus_doctor,
    ]
    if 1 <= chapter_num <= 11:
        fns[chapter_num - 1](c, w, h)
    c.restoreState()


def _illus_body(c, w, h):
    """Kap. 1 – Tělo: silueta postavy se srdcem uvnitř."""
    cx, cy = w / 2, h / 2
    # Záře / aura
    for r, alpha in [(65, 0.08), (50, 0.12), (38, 0.18)]:
        c.setFillColor(BLUSH_300)
        c.setFillAlpha(alpha)
        c.circle(cx, cy, r, fill=1, stroke=0)
    c.setFillAlpha(1)
    # Trup
    c.setFillColor(BLUSH_200)
    c.setStrokeColor(BLUSH_300)
    c.setLineWidth(1.2)
    c.ellipse(cx - 18, cy - 35, cx + 18, cy + 10, fill=1, stroke=1)
    # Hlava
    c.setFillColor(BLUSH_200)
    c.circle(cx, cy + 24, 14, fill=1, stroke=1)
    # Srdce uvnitř (červené)
    _draw_heart(c, cx, cy - 10, 11, BLUSH_500, BLUSH_500)
    # Drobné tečky jako buňky
    for dx, dy in [(-28, 0), (28, 5), (-22, -25), (25, -20), (0, -45)]:
        c.setFillColor(BLUSH_300)
        c.setFillAlpha(0.5)
        c.circle(cx + dx, cy + dy, 3, fill=1, stroke=0)
    c.setFillAlpha(1)


def _draw_heart(c, cx, cy, size, fill_color, stroke_color):
    """Nakreslí srdce na canvas."""
    s = size
    p = c.beginPath()
    p.moveTo(cx, cy - s * 0.6)
    p.curveTo(cx - s * 1.2, cy + s * 0.4, cx - s * 1.2, cy + s * 1.2, cx, cy + s * 0.6)
    p.curveTo(cx + s * 1.2, cy + s * 1.2, cx + s * 1.2, cy + s * 0.4, cx, cy - s * 0.6)
    c.setFillColor(fill_color)
    c.setStrokeColor(stroke_color)
    c.setLineWidth(0.5)
    c.drawPath(p, fill=1, stroke=1)


def _illus_breastfeeding(c, w, h):
    """Kap. 2 – Kojení: objem/objetí, kapky mléka."""
    cx, cy = w / 2, h / 2
    # Velký oblouk – náruč/objetí
    c.setStrokeColor(BLUSH_300)
    c.setFillColor(BLUSH_100)
    c.setLineWidth(2)
    c.arc(cx - 45, cy - 35, cx + 45, cy + 55, startAng=200, extent=140)
    # Miminko – elipsa
    c.setFillColor(CREAM_200)
    c.setStrokeColor(BLUSH_200)
    c.setLineWidth(1)
    c.ellipse(cx - 22, cy - 15, cx + 22, cy + 28, fill=1, stroke=1)
    # Hlavička
    c.setFillColor(CREAM_200)
    c.circle(cx, cy + 35, 13, fill=1, stroke=1)
    # Kapky mléka
    for dx, dy, r in [(-38, 15, 4), (-44, 28, 3), (-35, 38, 2.5), (-42, 5, 2)]:
        c.setFillColor(white)
        c.setStrokeColor(BLUSH_300)
        c.setLineWidth(0.8)
        c.circle(cx + dx, cy + dy, r, fill=1, stroke=1)
    # Srdíčko nahoře
    _draw_heart(c, cx + 28, cy + 42, 7, BLUSH_500, BLUSH_500)


def _illus_sleep(c, w, h):
    """Kap. 3 – Spánek: měsíc + hvězdy."""
    cx, cy = w / 2, h / 2
    # Měsíc – srpek
    c.setFillColor(AMBER_300)
    c.setStrokeColor(HexColor('#F59E0B'))
    c.setLineWidth(0)
    c.circle(cx - 5, cy + 5, 30, fill=1, stroke=0)
    c.setFillColor(SAGE_100)
    c.circle(cx + 10, cy + 12, 24, fill=1, stroke=0)
    # Záře měsíce
    c.setFillColor(AMBER_300)
    c.setFillAlpha(0.15)
    c.circle(cx - 5, cy + 5, 46, fill=1, stroke=0)
    c.setFillAlpha(1)
    # Hvězdy
    star_positions = [(-35, 30), (30, 38), (-28, -10), (38, 10), (5, -30), (-12, 42)]
    for dx, dy in star_positions:
        _draw_star(c, cx + dx, cy + dy, 4, AMBER_300, HexColor('#F59E0B'))
    # ZZZ text
    for i, (zx, zy, fs) in enumerate([(cx + 30, cy - 20, 16), (cx + 38, cy - 6, 11), (cx + 44, cy + 6, 8)]):
        c.setFont("Helvetica-Bold", fs)
        c.setFillColor(WARM_400)
        c.setFillAlpha(0.6 - i * 0.15)
        c.drawString(zx, zy, "z")
    c.setFillAlpha(1)


def _draw_star(c, cx, cy, r, fill, stroke):
    """Pětipaprsková hvězda."""
    points = []
    for i in range(10):
        angle = math.pi / 2 + i * math.pi / 5
        radius = r if i % 2 == 0 else r * 0.45
        points.extend([cx + radius * math.cos(angle), cy + radius * math.sin(angle)])
    p = c.beginPath()
    p.moveTo(points[0], points[1])
    for i in range(2, len(points), 2):
        p.lineTo(points[i], points[i + 1])
    p.close()
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(0.5)
    c.drawPath(p, fill=1, stroke=1)


def _illus_emotions(c, w, h):
    """Kap. 4 – Baby blues: slunce + oblak s deštěm."""
    cx, cy = w / 2, h / 2
    # Slunce (polovina)
    c.setFillColor(AMBER_300)
    c.setFillAlpha(0.9)
    c.circle(cx - 15, cy + 20, 22, fill=1, stroke=0)
    # Paprsky slunce
    c.setStrokeColor(AMBER_300)
    c.setFillAlpha(0.5)
    c.setLineWidth(1.5)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        x1 = cx - 15 + 24 * math.cos(rad)
        y1 = cy + 20 + 24 * math.sin(rad)
        x2 = cx - 15 + 32 * math.cos(rad)
        y2 = cy + 20 + 32 * math.sin(rad)
        c.setStrokeColor(AMBER_300)
        c.line(x1, y1, x2, y2)
    c.setFillAlpha(1)
    # Oblak
    c.setFillColor(white)
    c.setStrokeColor(HexColor('#CBD5E1'))
    c.setLineWidth(1)
    for dx, dy, r in [(0, 0, 20), (-18, -8, 15), (18, -5, 17), (-8, -18, 12), (10, -16, 13)]:
        c.circle(cx + dx, cy + dy, r, fill=1, stroke=0)
    c.setStrokeColor(HexColor('#CBD5E1'))
    # Kapky deště
    c.setFillColor(HexColor('#93C5FD'))
    c.setStrokeColor(HexColor('#60A5FA'))
    c.setLineWidth(0.5)
    for dx, dy in [(-18, -35), (-6, -42), (6, -37), (18, -44), (-12, -50), (2, -55)]:
        p = c.beginPath()
        p.moveTo(cx + dx, cy + dy)
        p.curveTo(cx + dx - 2, cy + dy - 5, cx + dx + 2, cy + dy - 5, cx + dx, cy + dy - 9)
        c.drawPath(p, fill=1, stroke=0)
    # Fialové srdce – naděje
    _draw_heart(c, cx + 30, cy - 25, 8, HexColor('#A78BFA'), HexColor('#7C3AED'))


def _illus_baby_care(c, w, h):
    """Kap. 5 – Péče o miminko: vanička s bublinami."""
    cx, cy = w / 2, h / 2 - 5
    # Vanička – spodní část elipsy
    c.setFillColor(BLUSH_100)
    c.setStrokeColor(BLUSH_300)
    c.setLineWidth(1.5)
    c.ellipse(cx - 40, cy - 25, cx + 40, cy + 15, fill=1, stroke=1)
    # Voda – horní ořez vaniky
    c.setFillColor(HexColor('#BAE6FD'))
    c.setStrokeColor(HexColor('#7DD3FC'))
    c.setLineWidth(0.8)
    c.ellipse(cx - 38, cy - 18, cx + 38, cy + 8, fill=1, stroke=1)
    # Miminko v vaničce – kulatá hlavička
    c.setFillColor(CREAM_200)
    c.setStrokeColor(BLUSH_200)
    c.setLineWidth(1)
    c.circle(cx, cy + 16, 15, fill=1, stroke=1)
    # Oči miminka
    c.setFillColor(WARM_900)
    c.circle(cx - 5, cy + 18, 1.5, fill=1, stroke=0)
    c.circle(cx + 5, cy + 18, 1.5, fill=1, stroke=0)
    # Úsměv
    c.setStrokeColor(WARM_600)
    c.setLineWidth(1)
    c.arc(cx - 5, cy + 10, cx + 5, cy + 16, startAng=200, extent=140)
    # Bubliny
    c.setStrokeColor(HexColor('#7DD3FC'))
    c.setLineWidth(0.8)
    for bx, by, br, alpha in [(-28, 30, 5, 0.8), (-38, 45, 3, 0.6), (32, 35, 4, 0.7),
                                (40, 50, 6, 0.5), (-18, 50, 4, 0.6), (20, 55, 3, 0.7)]:
        c.setFillColor(white)
        c.setFillAlpha(alpha)
        c.circle(cx + bx, cy + by, br, fill=1, stroke=1)
    c.setFillAlpha(1)
    # Nožičky
    c.setFillColor(CREAM_200)
    c.setStrokeColor(BLUSH_200)
    c.circle(cx - 10, cy + 2, 6, fill=1, stroke=1)
    c.circle(cx + 10, cy + 2, 6, fill=1, stroke=1)


def _illus_nutrition(c, w, h):
    """Kap. 6 – Výživa: miska s lžičkou a zelenými lístky."""
    cx, cy = w / 2, h / 2 - 5
    # Miska – dolní půlkruh
    c.setFillColor(CREAM_100)
    c.setStrokeColor(BLUSH_300)
    c.setLineWidth(1.5)
    p = c.beginPath()
    p.moveTo(cx - 38, cy + 5)
    p.curveTo(cx - 38, cy - 35, cx + 38, cy - 35, cx + 38, cy + 5)
    p.lineTo(cx - 38, cy + 5)
    c.drawPath(p, fill=1, stroke=1)
    # Okraj misky
    c.setFillColor(BLUSH_200)
    c.ellipse(cx - 40, cy + 2, cx + 40, cy + 14, fill=1, stroke=1)
    # Obsah misky – zelenina/ovoce
    c.setFillColor(SAGE_400)
    c.setFillAlpha(0.8)
    c.circle(cx - 12, cy - 12, 8, fill=1, stroke=0)
    c.setFillColor(BLUSH_400 if hasattr(c, 'BLUSH_400') else HexColor('#F47F7F'))
    c.setFillAlpha(0.9)
    c.circle(cx + 8, cy - 15, 7, fill=1, stroke=0)
    c.setFillColor(AMBER_300)
    c.setFillAlpha(0.85)
    c.circle(cx, cy - 5, 6, fill=1, stroke=0)
    c.setFillAlpha(1)
    # Lžička
    c.setFillColor(WARM_400)
    c.setStrokeColor(WARM_600)
    c.setLineWidth(1)
    c.ellipse(cx + 28, cy + 22, cx + 40, cy + 34, fill=1, stroke=1)
    c.line(cx + 34, cy + 22, cx + 26, cy - 15)
    # Lístky
    for lx, ly, angle in [(-35, 35, 30), (-25, 48, -15), (-45, 48, 50)]:
        c.saveState()
        c.translate(cx + lx, cy + ly)
        c.rotate(angle)
        c.setFillColor(SAGE_400)
        c.setStrokeColor(SAGE_500)
        c.setLineWidth(0.5)
        p2 = c.beginPath()
        p2.moveTo(0, 0)
        p2.curveTo(-5, 8, 5, 16, 0, 20)
        p2.curveTo(-5, 16, 5, 8, 0, 0)
        c.drawPath(p2, fill=1, stroke=1)
        c.restoreState()


def _illus_couple(c, w, h):
    """Kap. 7 – Vztah: dvě propojená srdce."""
    cx, cy = w / 2, h / 2
    # Velké srdce vlevo (ona)
    _draw_heart(c, cx - 14, cy + 5, 22, BLUSH_200, BLUSH_300)
    # Velké srdce vpravo (on)
    _draw_heart(c, cx + 14, cy + 5, 22, SAGE_200, SAGE_300)
    # Malé srdíčko uprostřed (miminko)
    _draw_heart(c, cx, cy + 28, 9, BLUSH_500, BLUSH_500)
    # Spojovací linka
    c.setStrokeColor(WARM_400)
    c.setLineWidth(0.8)
    c.setFillAlpha(0.4)
    c.line(cx - 14, cy + 5, cx + 14, cy + 5)
    c.setFillAlpha(1)
    # Hvězdičky kolem
    for sx, sy in [(-40, 30), (40, 35), (0, -15), (-35, -10), (35, -5)]:
        _draw_star(c, cx + sx, cy + sy, 3, AMBER_300, HexColor('#F59E0B'))


def _illus_home(c, w, h):
    """Kap. 8 – Domácnost: domek s oknem a dveřmi."""
    cx, cy = w / 2, h / 2 - 10
    # Střecha – trojúhelník
    c.setFillColor(BLUSH_300)
    c.setStrokeColor(BLUSH_500)
    c.setLineWidth(1.2)
    p = c.beginPath()
    p.moveTo(cx, cy + 55)
    p.lineTo(cx - 45, cy + 15)
    p.lineTo(cx + 45, cy + 15)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    # Zdi
    c.setFillColor(CREAM_100)
    c.setStrokeColor(BLUSH_200)
    c.setLineWidth(1)
    c.rect(cx - 35, cy - 30, 70, 47, fill=1, stroke=1)
    # Dveře
    c.setFillColor(BLUSH_200)
    c.setStrokeColor(BLUSH_300)
    c.rect(cx - 10, cy - 30, 20, 32, fill=1, stroke=1)
    # Kulatý vrchol dveří
    c.setFillColor(BLUSH_200)
    c.circle(cx, cy + 2, 10, fill=1, stroke=1)
    # Klika
    c.setFillColor(AMBER_300)
    c.circle(cx + 5, cy - 12, 2.5, fill=1, stroke=0)
    # Okno vlevo
    c.setFillColor(HexColor('#BAE6FD'))
    c.setStrokeColor(BLUSH_200)
    c.rect(cx - 30, cy, 18, 14, fill=1, stroke=1)
    c.line(cx - 21, cy, cx - 21, cy + 14)
    c.line(cx - 30, cy + 7, cx - 12, cy + 7)
    # Okno vpravo
    c.rect(cx + 12, cy, 18, 14, fill=1, stroke=1)
    c.line(cx + 21, cy, cx + 21, cy + 14)
    c.line(cx + 12, cy + 7, cx + 30, cy + 7)
    # Komín
    c.setFillColor(BLUSH_300)
    c.rect(cx + 18, cy + 42, 12, 20, fill=1, stroke=1)
    # Kouř
    c.setStrokeColor(WARM_400)
    c.setLineWidth(1.2)
    c.setFillAlpha(0.4)
    for i, (ox, oy) in enumerate([(0, 0), (4, 8), (-3, 16)]):
        c.setStrokeAlpha(0.4 - i * 0.1)
        c.arc(cx + 24 + ox - 5, cy + 62 + oy, cx + 24 + ox + 5, cy + 72 + oy,
              startAng=0, extent=180)
    c.setFillAlpha(1)
    c.setStrokeAlpha(1)
    # Tráva
    c.setFillColor(SAGE_400)
    c.rect(cx - 45, cy - 35, 90, 6, fill=1, stroke=0)


def _illus_visitors(c, w, h):
    """Kap. 9 – Návštěvy: dveře s rámem a zarážkou."""
    cx, cy = w / 2, h / 2 - 5
    # Dveřní rám
    c.setFillColor(BLUSH_200)
    c.setStrokeColor(BLUSH_300)
    c.setLineWidth(1.5)
    c.rect(cx - 28, cy - 45, 56, 80, fill=1, stroke=1)
    # Dveře – dvě křídla
    c.setFillColor(CREAM_100)
    c.setStrokeColor(BLUSH_300)
    c.setLineWidth(1)
    c.rect(cx - 24, cy - 42, 24, 73, fill=1, stroke=1)
    c.rect(cx, cy - 42, 24, 73, fill=1, stroke=1)
    # Kliky
    c.setFillColor(AMBER_300)
    c.circle(cx - 5, cy - 3, 3, fill=1, stroke=0)
    c.circle(cx + 5, cy - 3, 3, fill=1, stroke=0)
    # Ozdobný věnec na dveřích
    c.setFillColor(SAGE_400)
    c.setStrokeColor(SAGE_500)
    c.setLineWidth(0.8)
    c.circle(cx, cy + 22, 12, fill=0, stroke=1)
    # Lístky věnce
    for angle in range(0, 360, 40):
        rad = math.radians(angle)
        lx = cx + 12 * math.cos(rad)
        ly = cy + 22 + 12 * math.sin(rad)
        c.setFillColor(SAGE_400)
        c.circle(lx, ly, 3.5, fill=1, stroke=0)
    # Mašle věnce
    _draw_heart(c, cx, cy + 10, 5, BLUSH_500, BLUSH_500)
    # Schodek
    c.setFillColor(BLUSH_100)
    c.rect(cx - 32, cy - 50, 64, 7, fill=1, stroke=1)
    # Značka "STOP" – hranice
    c.setFillColor(BLUSH_500)
    c.setStrokeColor(white)
    c.setLineWidth(1)
    c.circle(cx + 32, cy + 35, 12, fill=1, stroke=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(cx + 32, cy + 32, "NE")


def _illus_recovery(c, w, h):
    """Kap. 10 – Regenerace: květ rozkvetlý ze semínka."""
    cx, cy = w / 2, h / 2 - 10
    # Stonka
    c.setStrokeColor(SAGE_500)
    c.setFillColor(SAGE_500)
    c.setLineWidth(2)
    p = c.beginPath()
    p.moveTo(cx, cy - 35)
    p.curveTo(cx - 5, cy, cx + 5, cy + 15, cx, cy + 35)
    c.drawPath(p, fill=0, stroke=1)
    # Lístky
    for side, angle in [(-1, 30), (1, -30), (-1, 5)]:
        c.saveState()
        c.translate(cx, cy + 10)
        c.rotate(angle * side)
        c.setFillColor(SAGE_400)
        c.setStrokeColor(SAGE_500)
        c.setLineWidth(0.6)
        p2 = c.beginPath()
        p2.moveTo(0, 0)
        p2.curveTo(side * 8, 8, side * 18, 8, side * 22, 0)
        p2.curveTo(side * 18, -5, side * 8, -5, 0, 0)
        c.drawPath(p2, fill=1, stroke=1)
        c.restoreStore() if False else c.restoreState()
    # Květ – okvětní lístky
    petal_colors = [BLUSH_300, BLUSH_200, BLUSH_300, BLUSH_200, BLUSH_300]
    for i, col in enumerate(petal_colors):
        angle = math.radians(i * 72)
        px = cx + 15 * math.cos(angle)
        py = cy + 36 + 15 * math.sin(angle)
        c.setFillColor(col)
        c.setStrokeColor(BLUSH_300)
        c.setLineWidth(0.5)
        c.ellipse(px - 8, py - 5, px + 8, py + 5, fill=1, stroke=1)
    # Střed květu
    c.setFillColor(AMBER_300)
    c.setStrokeColor(HexColor('#F59E0B'))
    c.setLineWidth(1)
    c.circle(cx, cy + 36, 9, fill=1, stroke=1)
    # Drobné tečky – vnitřek
    c.setFillColor(HexColor('#D97706'))
    for dx, dy in [(-3, 2), (3, 2), (0, -3), (-2, -1), (2, -1)]:
        c.circle(cx + dx, cy + 36 + dy, 1, fill=1, stroke=0)
    # Semínko dole
    c.setFillColor(WARM_600)
    p3 = c.beginPath()
    p3.moveTo(cx, cy - 42)
    p3.curveTo(cx - 6, cy - 38, cx - 6, cy - 30, cx, cy - 28)
    p3.curveTo(cx + 6, cy - 30, cx + 6, cy - 38, cx, cy - 42)
    c.drawPath(p3, fill=1, stroke=0)
    # Zářivé pruhy kolem květu
    c.setStrokeColor(AMBER_300)
    c.setLineWidth(0.8)
    c.setStrokeAlpha(0.4)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        c.line(cx + 11 * math.cos(rad), cy + 36 + 11 * math.sin(rad),
               cx + 20 * math.cos(rad), cy + 36 + 20 * math.sin(rad))
    c.setStrokeAlpha(1)


def _illus_doctor(c, w, h):
    """Kap. 11 – Lékař: lékařský kříž + telefon."""
    cx, cy = w / 2, h / 2
    # Lékařský kříž – zelený
    c.setFillColor(SAGE_400)
    c.setStrokeColor(SAGE_500)
    c.setLineWidth(1)
    # Svislá část
    c.rect(cx - 10, cy - 30, 20, 60, fill=1, stroke=1)
    # Vodorovná část
    c.rect(cx - 30, cy - 10, 60, 20, fill=1, stroke=1)
    # Bílý středový čtverec
    c.setFillColor(white)
    c.rect(cx - 8, cy - 8, 16, 16, fill=1, stroke=0)
    # Záře
    c.setStrokeColor(SAGE_300)
    c.setLineWidth(1.5)
    c.setStrokeAlpha(0.3)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        c.line(cx + 32 * math.cos(rad), cy + 32 * math.sin(rad),
               cx + 42 * math.cos(rad), cy + 42 * math.sin(rad))
    c.setStrokeAlpha(1)
    # Telefon – vpravo dole
    c.setFillColor(BLUSH_500)
    c.setStrokeColor(BLUSH_300)
    c.setLineWidth(0.8)
    c.roundRect(cx + 28, cy - 28, 18, 30, 4, fill=1, stroke=1)
    # Displej
    c.setFillColor(HexColor('#BAE6FD'))
    c.rect(cx + 31, cy - 20, 12, 16, fill=1, stroke=0)
    # Tlačítko
    c.setFillColor(white)
    c.circle(cx + 37, cy - 6, 2, fill=1, stroke=0)
    # Volací ikona – malá sluchátka
    c.setStrokeColor(white)
    c.setLineWidth(1.2)
    c.arc(cx + 32, cy - 16, cx + 42, cy - 8, startAng=0, extent=180)


# ── STYLY ─────────────────────────────────────────────────────────────────────

def get_styles():
    chapter_title = ParagraphStyle(
        'ChapterTitle',
        fontName='Helvetica-Bold',
        fontSize=24,
        textColor=WARM_900,
        leading=30,
        spaceAfter=6,
        spaceBefore=8,
    )
    chapter_subtitle = ParagraphStyle(
        'ChapterSubtitle',
        fontName='Helvetica-Oblique',
        fontSize=12,
        textColor=BLUSH_500,
        leading=16,
        spaceAfter=18,
    )
    chapter_label = ParagraphStyle(
        'ChapterLabel',
        fontName='Helvetica',
        fontSize=10,
        textColor=WARM_400,
        leading=14,
        spaceAfter=4,
    )
    section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=12,
        textColor=WARM_900,
        leading=16,
        spaceBefore=14,
        spaceAfter=5,
    )
    body = ParagraphStyle(
        'BodyText',
        fontName='Helvetica',
        fontSize=10,
        textColor=WARM_600,
        leading=15,
        spaceAfter=7,
        alignment=TA_JUSTIFY,
    )
    bullet = ParagraphStyle(
        'BulletItem',
        fontName='Helvetica',
        fontSize=10,
        textColor=WARM_600,
        leading=15,
        spaceAfter=4,
        leftIndent=10,
        alignment=TA_LEFT,
    )
    toc_ch = ParagraphStyle(
        'TOCChapter',
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=WARM_900,
        leading=16,
        spaceAfter=1,
    )
    toc_sub = ParagraphStyle(
        'TOCSub',
        fontName='Helvetica-Oblique',
        fontSize=9,
        textColor=WARM_400,
        leading=13,
        spaceAfter=9,
        leftIndent=14,
    )
    intro = ParagraphStyle(
        'Intro',
        fontName='Helvetica',
        fontSize=10.5,
        textColor=WARM_600,
        leading=16,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
    )
    return dict(
        chapter_title=chapter_title,
        chapter_subtitle=chapter_subtitle,
        chapter_label=chapter_label,
        section_heading=section_heading,
        body=body,
        bullet=bullet,
        toc_ch=toc_ch,
        toc_sub=toc_sub,
        intro=intro,
    )


# ── OBSAH KAPITOL ─────────────────────────────────────────────────────────────

CHAPTERS = [
    {
        "num": 1,
        "title": "Tvé tělo po porodu",
        "subtitle": "Co se děje uvnitř\u00a0— a\u00a0proč je to normální",
        "color": BLUSH_100,
        "sections": [
            ("Co se děje v\u00a0prvních dnech", [
                "Bezprostředně po porodu prochází tvé tělo dramatickými změnami. Děloha, která v\u00a0průběhu těhotenství vyrostla na\u00a0velikost melounu, se postupně stahuje zpět do\u00a0původní velikosti\u00a0— tento proces trvá přibližně šest týdnů a\u00a0můžeš při něm cítit tzv.\u00a0dozvuky neboli poporodní stahy, zejména při kojení.",
                "Lochie (poporodní výtok) jsou zcela normální. V\u00a0prvních dnech jsou červené a\u00a0silné, postupně zesvětlají a\u00a0ubývají. Přibližně 4\u2013\u00ad6\u00a0týdnů po porodu by měly úplně vymizet.",
                "Silné pocení a\u00a0časté močení jsou způsoby, jakými tělo odbourává přebytečné tekutiny nahromaděné během těhotenství. Je zcela normální potit se hodně, zejména v\u00a0noci.",
            ]),
            ("Péče o\u00a0hráz a\u00a0jizvy", [
                "Pokud jsi rodila přirozeně, hráz mohla být protržena nebo nastřižena (epiziotomie). Bolest je normální a\u00a0obvykle odezní během 2\u20133\u00a0týdnů. Ledové obklady v\u00a0prvních 24\u00a0hodinách pomáhají snížit otok.",
                "Péče o\u00a0hráz: oplachuj čistou vodou po každém použití toalety, používej měkké jednorázové vložky, vyhni se sezení na\u00a0tvrdé podložce\u00a0— polštář ve\u00a0tvaru donutu je tvůj přítel.",
                "Pokud jsi rodila císařským řezem, jizva se hojí přibližně 6\u20138\u00a0týdnů. Nepřetěžuj se zvedáním těžkých věcí a\u00a0udržuj ránu suchou a\u00a0čistou. Po zhojení je možná masáž jizvy pro lepší kosmetický výsledek.",
            ]),
            ("Červené signály\u00a0— kdy volat lékaře", [
                "Silné krvácení: promočíš více než jednu vložku za\u00a0hodinu nebo vidíš velké krevní sraženiny.",
                "Horečka nad 38\u00a0°C.",
                "Zarudnutí nebo hnisání u\u00a0jizvy.",
                "Silná bolest, která se nezlepšuje.",
                "Neboj se volat lékaře nebo porodnici kdykoliv máš pochybnosti. Raději jednou zbytečně než jednou pozdě.",
            ]),
        ],
    },
    {
        "num": 2,
        "title": "Kojení bez slz",
        "subtitle": "Od prvního přiložení po ustálení laktace",
        "color": SAGE_100,
        "sections": [
            ("První přiložení a\u00a0správná technika", [
                "Ideálně do\u00a0hodiny po porodu\u00a0— tehdy je miminko nejbdílejší a\u00a0instinkty jsou nejsilnější. Neboj se požádat porodní asistentku o\u00a0pomoc. První přiložení nemusí být dokonalé.",
                "Správný úchop (latch): brada miminka se dotýká prsu, ústa jsou otevřená dokořán jako rybička, rty jsou vyhrnuty ven a\u00a0nos je volný. Pokud cítíš bolest po celou dobu kojení (nejen na\u00a0začátku), úchop není správný\u00a0— přilož znovu.",
                "Polohy kojení: klasická poloha \u201emadonna\u201c, poloha \u201erugby\u201c (miminko pod paží, skvělá po císaři), poloha vleže na\u00a0boku (pro noční kojení). Vyzkoušej různé a\u00a0najdi tu svou.",
            ]),
            ("Jak poznat, že miminko má dost mléka", [
                "Zlaté pravidlo: co do\u00a0miminka jde, musí z\u00a0něj vyjít. V\u00a0prvním týdnu: alespoň 1\u20132\u00a0mokré pleny denně na\u00a0den věku miminka (1.\u00a0den\u00a0= 1\u00a0plena, 2.\u00a0den\u00a0= 2\u00a0pleny atd.). Od 4.\u20135.\u00a0dne: alespoň 6\u00a0mokrých plen za\u00a024\u00a0hodin.",
                "Miminko přibírá. Po počátečním úbytku (max.\u00a010\u00a0% porodní váhy) by mělo začít přibírat okolo 4.\u20135.\u00a0dne. Kontrolní vážení u\u00a0dětského lékaře ti dá jistotu.",
                "Spokojené miminko po kojení: samo pustí prs, usíná nebo je klidné a\u00a0spokojené.",
            ]),
            ("Časté problémy a\u00a0jejich řešení", [
                "Prasklé bradavky: klíčem je správný úchop. Pomáhá lanolin nebo vlastní mléko nanesené po kojení. Kojení by nemělo bolet po celou dobu\u00a0— jen první sekundy.",
                "Zatvrdlé prsy (engorgement): přikládej co nejčastěji, před kojením teplý obklad, po kojení studený. Nevymačkávej mléko zbytečně\u00a0— tím jen stimuluješ tvorbu dalšího.",
                "Mastitis (zánět prsu): horečka, zarudnutí, bolest\u00a0— okamžitě k\u00a0lékaři. V\u00a0kojení NEPŘESTÁVÁŠ, pokračuješ i\u00a0při zánětu.",
            ]),
        ],
    },
    {
        "num": 3,
        "title": "Spánek pro přežití",
        "subtitle": "Spánkové cykly novorozence a\u00a0jak přežít noc",
        "color": CREAM_100,
        "sections": [
            ("Jak spí novorozenec", [
                "Novorozenec nemá nastavený cirkadiánní rytmus\u00a0— nerozlišuje den a\u00a0noc. To se postupně vyvíjí mezi 3.\u20136.\u00a0týdnem. Do té doby: není nic špatně s\u00a0tebou ani s\u00a0miminkem.",
                "Spánkový cyklus novorozence trvá přibližně 45\u201350\u00a0minut (dospělí mají 90\u00a0minut). Mezi cykly se miminko přirozeně probouzí\u00a0— jde o\u00a0normální a\u00a0ochranný mechanismus.",
                "Potřeba spánku: novorozenec spí 14\u201317\u00a0hodin denně, ale v\u00a0krátkých blocích po 2\u20134\u00a0hodinách. Nepřerušený pětihodinový spánek je v\u00a0prvních týdnech statistická rarita.",
            ]),
            ("Bezpečné podmínky pro spánek", [
                "Prevence SIDS: vždy spát na\u00a0zádech, pevná rovná podložka, žádné polštáře ani peřiny v\u00a0postýlce v\u00a0prvním roce, bez plyšáků v\u00a0postýlce, v\u00a0domácnosti se nekouří.",
                "Sdílení postele (co-sleeping): pokud se rozhodneš pro sdílení postele, zjisti bezpečné podmínky\u00a0— nikdy na\u00a0gauči ani v\u00a0křesle, tvrdá matrace, bez alkoholu a\u00a0léků navozujících spánek.",
                "Teplota v\u00a0místnosti: ideálně 18\u201320\u00a0°C. Přikrývej miminko přiměřeně\u00a0— jako sebe plus jedna vrstva navíc.",
            ]),
            ("Strategie pro více spánku", [
                "Spi, když spí miminko\u00a0— ano, stále platí, i\u00a0když to každý opakuje. Domácnost počká.",
                "Střídání s\u00a0partnerem: domluvte se na\u00a0blocích. Například partner přebírá miminko od\u00a022\u00a0do\u00a02\u00a0hod., ty spíš, pak ty přebíráš a\u00a0partner spí. Každý dostane alespoň jeden blok hlubokého spánku.",
                "Zjednodušení nočních rutin: přebaly jen při nutnosti, věci připravené dopředu, noční kojení vleže\u00a0— bez zapínání velkého světla.",
            ]),
        ],
    },
    {
        "num": 4,
        "title": "Baby blues vs.\u00a0poporodní deprese",
        "subtitle": "Jak poznat hranici a\u00a0kde hledat pomoc",
        "color": BLUSH_100,
        "sections": [
            ("Baby blues\u00a0— normální hormonální bouře", [
                "Baby blues zažívá až 80\u00a0% žen. Začíná typicky 3.\u20135.\u00a0den po porodu, kdy prudce klesá hladina estrogenů a\u00a0progesteronu. Projevuje se pláčem bez zřejmého důvodu, podrážděností, únavou a\u00a0přecitlivělostí.",
                "Baby blues samo odeznívá do\u00a0dvou týdnů. Pomáhá odpočinek, podpora blízkých a\u00a0vědomí, že jde o\u00a0normální a\u00a0dočasný stav.",
                "Důležité: pokud příznaky trvají déle než dva týdny nebo se zhoršují, může jít o\u00a0poporodní depresi\u00a0— vyhledej odbornou pomoc.",
            ]),
            ("Poporodní deprese\u00a0— příznaky a\u00a0kdy jednat", [
                "Poporodní depresí trpí přibližně 10\u201315\u00a0% žen (a\u00a0někdy i\u00a0partneři). Je to nemoc, ne slabost. Příznaky: přetrvávající smutek nebo vnitřní prázdnota, ztráta radosti z\u00a0miminka nebo z\u00a0čehokoli, neschopnost pečovat o\u00a0sebe nebo o\u00a0miminko, pocity bezcennosti nebo viny.",
                "Kdy okamžitě vyhledat pomoc: myšlenky na\u00a0ublížení sobě nebo miminkovi\u00a0— zavolej záchrannou službu (155) nebo jdi na\u00a0pohotovost.",
                "Léčba funguje: psychoterapie, případně antidepresiva (existují bezpečné i\u00a0při kojení). Netrp zbytečně\u00a0— požádej o\u00a0pomoc svého gynekologa, praktického lékaře nebo psychologa.",
            ]),
            ("Péče o\u00a0duševní zdraví každý den", [
                "Pohyb: i\u00a0krátká procházka venku pomáhá. Denní světlo reguluje hormony a\u00a0náladu.",
                "Spojení s\u00a0ostatními: skupiny pro maminky, online komunity, kamarádky ve\u00a0stejné situaci. Izolace příznaky zhoršuje.",
                "Nároky na\u00a0sebe: snižuj laťku. \u201EDost dobré\u201c je dost dobré. Miminko potřebuje přítomnou (i\u00a0unavenu) maminku, ne dokonalou.",
            ]),
        ],
    },
    {
        "num": 5,
        "title": "Péče o\u00a0novorozence",
        "subtitle": "Koupání, přebalování, pupínek\u00a0— krok za\u00a0krokem",
        "color": SAGE_100,
        "sections": [
            ("Koupání novorozence", [
                "Do\u00a0odpadnutí pupečníku (7\u201314\u00a0dní): koupej pouze houbičkou\u00a0— otírej části těla zvlhčenou žínkou a\u00a0netlač pod pupečník. Po odpadnutí: klasická koupel v\u00a0dětské vaničce.",
                "Teplota vody: 37\u00a0°C (dej zápěstí\u00a0— voda má být příjemně teplá, ne horká). Teplota místnosti: min. 22\u00a0°C. Koupel trvá 5\u201310\u00a0minut.",
                "Pořadí mytí: nejdřív obličej (čistá voda, bez mýdla), pak tělo, nakonec vlasy\u00a0— vlasy myjeme poslední, aby miminko nevychladlo. Frekvence: 2\u20133×\u00a0týdně stačí, každodenní koupel vysušuje citlivou kůži.",
            ]),
            ("Přebalování\u00a0— vše, co potřebuješ vědět", [
                "Správný postup: otíráme vždy od\u00a0přední části dozadu\u00a0— u\u00a0holčiček je to obzvláště důležité pro prevenci infekce. U\u00a0chlapečků pozor\u00a0— studený vzduch stimuluje močení.",
                "Opruzeniny: nejlepší prevencí je suchá kůže. Nech miminko chvíli \u201edýchat\u201c bez pleny. Pomáhá zinkový krém (Bepanthen a\u00a0podobné).",
                "Počet přebalování v\u00a0prvních týdnech: 8\u201312× denně. Mokrá plena je důkazem, že miminko přijímá dostatek tekutin.",
            ]),
            ("Péče o\u00a0pupínek", [
                "Pupečník odpadne sám za\u00a07\u201314\u00a0dní (někdy i\u00a0déle). Nezasahuj\u00a0— neodřezávej, neobaluj, nestahuj.",
                "Udržuj suché a\u00a0čisté: skládej plenku pod pupečník, aby měl přístup ke\u00a0vzduchu. Mírný zápach je normální, dokud pupečník neodpadne.",
                "Kdy k\u00a0lékaři: zarudnutí kůže okolo pupečníku, horečka, hnisání, krvácení z\u00a0pupečníku (kapička krve při odpadání je normální).",
            ]),
        ],
    },
    {
        "num": 6,
        "title": "Výživa a\u00a0regenerace maminky",
        "subtitle": "Co jíst, aby měla sílu a\u00a0mléko",
        "color": CREAM_100,
        "sections": [
            ("Výživa při kojení", [
                "Kojíš-li, potřebuješ přibližně o\u00a0500\u00a0kcal více denně. Nejde o\u00a0počítání kalorií, ale o\u00a0pestrou stravu s\u00a0dostatkem živin.",
                "Co je důležité: bílkoviny (maso, ryby, luštěniny, vejce, mléčné výrobky), vápník (mléčné výrobky, brokolice, mandle), omega\u20113\u00a0(tučné ryby 2×\u00a0týdně), železo (maso, luštěniny + vitamín\u00a0C pro lepší vstřebávání), vitamín\u00a0D (suplementace je doporučena celoročně).",
                "Mýtus: nemusíš se vyhýbat kořeněnému jídlu, zelí, cibuli ani česneku. Chuť mléka se mírně mění, ale naprostá většina miminek to toleruje bez problémů.",
            ]),
            ("Jídlo s\u00a0jednou rukou\u00a0— praktické tipy", [
                "Realita šestinedělí: vaříš jednou rukou, protože druhou držíš miminko. Nebo nevařiš vůbec, protože spíš. Obojí je naprosto v\u00a0pořádku.",
                "Tipy pro jednoduché jídlo: smoothie (ovoce + bílkoviny + mléko), avokádo na\u00a0chlebu, tvaroh s\u00a0ovocem, ořechy a\u00a0sušené ovoce jako svačina, vařená vejce připravená dopředu, mražená zelenina do\u00a0rychlých jídel.",
                "Přijmi pomoc: pokud někdo nabídne uvařit, řekni ANO a\u00a0popiš, co ráda jíš. Tohle není čas být skromná.",
            ]),
            ("Hydratace", [
                "Při kojení potřebuješ výrazně více tekutin\u00a0— až 3\u00a0litry denně. Nejjednodušší způsob: mít sklenici vody vždy při kojení.",
                "Káva: 1\u20132\u00a0šálky denně jsou při kojení bezpečné. Kofein přechází do\u00a0mléka v\u00a0malém množství, ale většina miminek to bez problémů toleruje. Pokud je miminko neklidné, zkus omezit.",
                "Alkohol: ideálně žádný, pokud kojíš. Pokud si výjimečně dáš sklenici vína, kojení z\u00a0předem nasbíraného mléka je bezpečnější volba.",
            ]),
        ],
    },
    {
        "num": 7,
        "title": "Vztah s\u00a0partnerem",
        "subtitle": "Jak si udržet spojení, když jste zombie",
        "color": BLUSH_100,
        "sections": [
            ("Realita prvních týdnů jako pár", [
                "Každý pár prochází výzvami po příchodu miminka. Průzkumy ukazují, že spokojenost ve\u00a0vztahu obvykle po porodu klesá\u00a0— nejsi výjimka, jde o\u00a0normální jev.",
                "Typické napětí: nedostatek spánku amplifikuje konflikty, každý má jiný pohled na\u00a0to, \u201eco se má dělat\u201c, žena může cítit, že partner nechápe náročnost kojení a\u00a0péče, partner může cítit odstrčenost nebo bezmocnost.",
                "Klíčové: toto je dočasné. Nepřijímejte zásadní rozhodnutí v\u00a0prvních šesti týdnech. Rodinu právě stavíte.",
            ]),
            ("Komunikace v\u00a0náročném období", [
                "Říkej konkrétně, co potřebuješ: ne \u201enikdy mi nepomáháš\u201c, ale \u201epotřebuju teď hodinu spát, můžeš přebrat miminko?\u201c",
                "Prostor pro oba: oba jste vyčerpaní, oba se učíte. Partner neví automaticky, jak pomoci\u00a0— raději ho navádět než čekat, že sám pozná.",
                "Sdílejte i\u00a0malé radosti: \u201epodívej, usmál se na\u00a0mě\u201c\u00a0— tyto okamžiky vás spojují i\u00a0v\u00a0nejtěžším období.",
            ]),
            ("Intimita a\u00a0sex po porodu", [
                "Doporučené čekání: min.\u00a06\u00a0týdnů po vaginálním porodu a\u00a0po kontrole u\u00a0gynekologa. Po císaři obdobně.",
                "Fyzická a\u00a0psychická připravenost jsou stejně důležité. Nezahajuj jen proto, že \u201ečas vypršel\u201c. Komunikuj s\u00a0partnerem.",
                "Změny, které jsou normální: snížené libido (hormony kojení potlačují estrogen), suchost pochvy (řeší lubrikant), citlivost po porodu. Vše se časem normalizuje.",
            ]),
        ],
    },
    {
        "num": 8,
        "title": "Praktická organizace domácnosti",
        "subtitle": "Systémy, které fungují s\u00a0jednou volnou rukou",
        "color": SAGE_100,
        "sections": [
            ("Přebuduj svá očekávání", [
                "Čistá domácnost, uvařeno, spokojené miminko a\u00a0vy odpočatí\u00a0— toto nejde dohromady naráz. Přijmi, že priority se musí přerozdělit.",
                "Hierarchie v\u00a0šestinedělí: (1)\u00a0bezpečnost miminka, (2)\u00a0tvé zdraví a\u00a0spánek, (3)\u00a0jídlo pro tebe, (4)\u00a0cokoliv dalšího.",
                "Co může počkat: žehlení (téměř vše), hloubkový úklid, vaření složitých jídel, odpovídání na\u00a0zprávy.",
            ]),
            ("Systémy, které usnadní život", [
                "Přebalovací stanice na\u00a0každém patře (nebo alespoň na\u00a0dvou místech): ušetříš zbytečnou chůzi s\u00a0miminkem.",
                "Noc připravena dopředu: pleny, vlhčené ubrousky, čisté oblečení\u00a0— vše v\u00a0dosahu, bez zapínání velkých světel.",
                "Dávkové vaření: uvař jednou víc a\u00a0zmraž. Kamarádky a\u00a0rodina nabízejí jídlo\u00a0— přijmi to a\u00a0řekni, co máš ráda. Nákupy online: přesměruj energii jinam.",
            ]),
            ("Zapojení partnera a\u00a0rodiny", [
                "Konkrétní úkoly pro partnera: ranní koupel miminka, jeden noční vstávání za\u00a0noc, vaření nebo objednání jídla, úklid toalety a\u00a0kuchyně.",
                "Prarodiče a\u00a0ostatní: dej jim konkrétní úkoly (\u201emůžeš přijít a\u00a0uvařit polévku?\u201c), ne jen \u201epřijď mě navštívit\u201c. Návštěvy bez pomoci mohou vyčerpávat.",
                "Placená pomoc: pokud je to finančně možné, uklízečka 2×\u00a0měsíčně nebo chůva na\u00a0pár hodin týdně\u00a0— investice do\u00a0tvého zdraví a\u00a0vztahu.",
            ]),
        ],
    },
    {
        "num": 9,
        "title": "Nástup rodiny a\u00a0návštěvy",
        "subtitle": "Jak nastavit hranice bez pocitu viny",
        "color": CREAM_100,
        "sections": [
            ("Právo říct ne", [
                "Návštěvy v\u00a0šestinedělí jsou privilegiem, ne právem. Máš plné právo říct: \u201eTeď ještě nejsme připraveni na\u00a0návštěvy\u201c\u00a0— a\u00a0nepotřebuješ to nikomu vysvětlovat.",
                "Nastavení pravidel dopředu: ideálně ještě v\u00a0těhotenství si domluv s\u00a0partnerem, jaká pravidla chcete. Partner pak může komunikovat za\u00a0oba.",
                "Formule pro zdvořilé odmítnutí: \u201eMoc rádi vás uvidíme, ale teď ještě ne. Dáme vám vědět, až budeme připraveni.\u201c",
            ]),
            ("Pravidla pro návštěvy", [
                "Kdo je nemocný\u00a0— nepřichází. Žádné výjimky, ani pro babičky.",
                "Mytí rukou před dotykem s\u00a0miminkem: vždy.",
                "Délka návštěvy: řekni dopředu, že \u201emáte hodinu, pak bude miminko jíst\u201c. Tím automaticky nastavíš délku setkání.",
                "Návštěvy, které pomáhají: přinesou jídlo, uklidí, podrží miminko, aby ses mohla osprchovat. Návštěvy, které jen \u201ekoukají\u201c: na\u00a0ty máš právo říct, že ještě chvíli počkáme.",
            ]),
            ("Prarodiče a\u00a0nevyžádané rady", [
                "Rady, které jsi nežádala: \u201eza\u00a0nás se to dělalo jinak\u201c\u00a0— nejjednodušší odpověď je \u201ehmm, zajímavé\u201c a\u00a0pokračovat po svém.",
                "Prarodiče mají obrovskou touhu pomáhat a\u00a0být součástí\u00a0— kanalizuj ji na\u00a0konkrétní pomoc: \u201emůžeš si sednout a\u00a0podržet ji, já si jdu osprchovat?\u201c",
                "Konflikty v\u00a0rodině: pokud prarodiče opakovaně ignorují vaše pravidla (bezpečnost, přebalování, kojení vs.\u00a0přikrmování), je čas, aby partner jasně a\u00a0klidně nastolil hranice. Toto není boj\u00a0— jde o\u00a0ochranu rodiny.",
            ]),
        ],
    },
    {
        "num": 10,
        "title": "Tělo zpátky\u00a0— realisticky",
        "subtitle": "Jizvy, dno pánevní, cvičení v\u00a0pravý čas",
        "color": BLUSH_100,
        "sections": [
            ("Realistická očekávání", [
                "Tělo, které devět měsíců nosilo a\u00a0zrodilo nový život, se nemění přes noc. Ani přes měsíc. Šestinedělí (6\u00a0týdnů) je minimum\u00a0— plná regenerace může trvat rok i\u00a0déle.",
                "Diastáza (rozestup středové šlachy břicha) se vyskytuje u\u00a060\u2013100\u00a0% žen po porodu. Klasické \u201ecrunch\u201c cviky ji mohou zhoršit. Nejdřív rehabilitace dna pánevního.",
                "Vypadávání vlasů kolem 3.\u20136.\u00a0měsíce po porodu je normální. Způsobují ho hormony. Vrátí se.",
            ]),
            ("Dno pánevní\u00a0— proč je klíčové", [
                "Dno pánevní neslo celou váhu těhotenství a\u00a0prošlo obrovskou zátěží při porodu. Slabé dno pánevní způsobuje únik moče při smíchu, kašli nebo skákání\u00a0— to není normální, ale je léčitelné.",
                "Cvičení Kegel: snaž se stáhnout svaly, jako bys zastavovala proud moče. Drž 5\u00a0sekund, uvolni, opakuj 10×. Dělej 3×\u00a0denně\u00a0— klidně při kojení nebo přebalování.",
                "Fyzioterapeutka dna pánevního: doporučena po každém porodu, zejména pokud pociťuješ jakékoliv problémy. Není to luxus\u00a0— je to péče o\u00a0zdraví.",
            ]),
            ("Kdy a\u00a0jak začít cvičit", [
                "0\u20136 týdnů: pouze cvičení Kegel a\u00a0krátké procházky. Žádné břišní cvičení, silové cvičení ani běh.",
                "Po 6\u00a0týdnech a\u00a0po souhlasu lékaře: postupný rozjezd. Začni chůzí, plaváním nebo pilatem pro maminky.",
                "Sociální sítě a\u00a0kultura \u201esnap back\u201c: ignoruj fotografie celebrit šest týdnů po porodu. Za\u00a0každou takovou fotografií jsou osobní trenéři, kuchař a\u00a0chůva. Srovnávej se jen se sebou.",
            ]),
        ],
    },
    {
        "num": 11,
        "title": "Kdy volat lékaře",
        "subtitle": "Červené vlajky pro maminku i\u00a0miminko",
        "color": SAGE_100,
        "sections": [
            ("Příznaky u\u00a0maminky\u00a0— okamžitě kontaktuj lékaře", [
                "HOREČKA nad 38\u00a0°C\u00a0— může signalizovat infekci hráze, dělohy, prsu nebo močových cest.",
                "SILNÉ KRVÁCENÍ\u00a0— promočíš více než jednu vložku za\u00a0hodinu nebo se krvácení náhle zesílí.",
                "BOLEST NA HRUDI nebo dušnost\u00a0— možný příznak trombózy (krevní sraženiny).",
                "ZARUDNUTÍ nebo teplo v\u00a0lýtku\u00a0— příznak trombózy.",
                "SILNÁ BOLEST HLAVY nebo problémy se zrakem\u00a0— příznaky poporodní hypertenze.",
                "MYŠLENKY NA UBLÍŽENÍ sobě nebo miminkovi\u00a0— OKAMŽITĚ volejte záchranku: 155.",
            ]),
            ("Příznaky u\u00a0miminka\u00a0— okamžitě k\u00a0lékaři", [
                "HOREČKA nad 38\u00a0°C u\u00a0novorozence (do\u00a03\u00a0měsíců)\u00a0— vždy okamžitě k\u00a0lékaři.",
                "DÝCHÁNÍ: rychlé (více než 60\u00a0dechů za\u00a0minutu), pomalé, s\u00a0přestávkami, modravá barva rtů.",
                "NECHUTENSTVÍ: odmítá 2\u00a0jídla v\u00a0řadě nebo jí výrazně méně než obvykle.",
                "LETARGIE: nejde vzbudit, nereaguje na\u00a0podněty.",
                "ŽLOUTENKA: žlutá barva kůže nebo bělma\u00a0— zejména šíří-li se na\u00a0bříško nebo nohy.",
                "PUPEČNÍK: zarudnutí kůže okolo pupečníku, horečka, hnisání.",
            ]),
            ("Důležité kontakty", [
                "Záchranná služba: 155",
                "Porodnice, kde jsi rodila\u00a0— telefonická poradna pro maminky",
                "Dětský lékař\u00a0— pro dotazy ohledně miminka",
                "Laktační poradkyně\u00a0— kojení",
                "Krizová linka: 116\u00a0123 (Linka bezpečí)",
            ]),
        ],
    },
]

INTRO_TEXT = [
    "Právě se ti narodilo miminko\u00a0— a\u00a0spolu s\u00a0ním nová verze tebe.",
    "Šestinedělí je jedním z\u00a0nejintenzivnějších, nejkrásnějších a\u00a0nejnáročnějších období života. Nikdo tě na\u00a0něj dostatečně nepřipravil. Tohle je příručka, která měla existovat\u00a0— a\u00a0nyní ji držíš v\u00a0rukou (nebo spíš jednou rukou, zatímco druhou kojíš).",
    "Je napsána pro reálný život\u00a0— pro tři hodiny ráno, pro bolest hráze, pro slzy bez důvodu, pro okamžiky naprostého úžasu. Přímá, konkrétní, bez přikrašlování.",
    "Jsi dost dobrá maminka. Víc než dost.",
]

ZAVER_TEXT = [
    "Šestinedělí není sprint. Je to pomalý, náročný, nádherný maraton.",
    "Pokud jsi přečetla tuto příručku celou: jsi připravena lépe než většina matek, které šestinedělím prošly.",
    "Pokud jsi přečetla jen část: přečetla jsi přesně to, co jsi v\u00a0tu chvíli potřebovala.",
    "Pokud jsi ji otevřela ve\u00a0tři ráno: jsme tu s\u00a0tebou. Tohle pomine. Bude líp.",
    "Gratulujeme\u00a0— jsi maminka.",
]


# ── STAVBA PDF ────────────────────────────────────────────────────────────────

def build_pdf(output_path: str):
    styles = get_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2.5 * cm,
        leftMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.8 * cm,
        title="Šestinedělí s\u00a0klidem",
        author="Šestinedělí s klidem",
        subject="Příručka pro maminky v šestinedělí",
    )

    def draw_cover(c, doc):
        c.saveState()
        w, h = A4
        # Pozadí
        c.setFillColor(BLUSH_500)
        c.rect(0, 0, w, h, fill=1, stroke=0)
        # Světlejší horní vrstva
        c.setFillColor(HexColor('#F47F7F'))
        c.rect(0, h * 0.5, w, h * 0.5, fill=1, stroke=0)
        # Dekorativní kruhy
        c.setFillColor(HexColor('#F9ADAD'))
        c.setFillAlpha(0.4)
        c.circle(w * 0.85, h * 0.88, 130, fill=1, stroke=0)
        c.setFillColor(SAGE_400)
        c.setFillAlpha(0.3)
        c.circle(w * 0.1, h * 0.12, 90, fill=1, stroke=0)
        c.setFillColor(CREAM_200)
        c.setFillAlpha(0.2)
        c.circle(w * 0.5, h * 0.1, 60, fill=1, stroke=0)
        c.setFillAlpha(1)
        # Světlý spodní pruh
        c.setFillColor(CREAM_200)
        c.rect(0, 0, w, h * 0.16, fill=1, stroke=0)
        # Ilustrace na titulní straně
        draw_illustration(c, 1, w * 0.55, h * 0.52, 180, 160)
        # Texty
        c.setFont("Helvetica-Bold", 52)
        c.setFillColor(white)
        c.drawCentredString(w * 0.38, h * 0.76, "Šestinedělí")
        c.setFont("Helvetica-Bold", 46)
        c.drawCentredString(w * 0.38, h * 0.66, "s klidem")
        c.setFont("Helvetica-Oblique", 14)
        c.setFillColor(HexColor('#FDE8E8'))
        c.drawCentredString(w * 0.38, h * 0.56, "Kompletní příručka pro nové maminky")
        c.drawCentredString(w * 0.38, h * 0.52, "od porodu po 6. týden")
        # Dole
        c.setFont("Helvetica", 10)
        c.setFillColor(WARM_600)
        c.drawCentredString(w / 2, h * 0.09, "11 kapitol  \u00b7  Sepsáno s porodní asistentkou  \u00b7  85 stran")
        c.restoreState()

    def make_later_page(chapter_num=0, chapter_title=""):
        def later_page(c, doc):
            c.saveState()
            w, h = A4
            c.setStrokeColor(BLUSH_200)
            c.setLineWidth(0.5)
            c.line(2 * cm, 1.9 * cm, w - 2 * cm, 1.9 * cm)
            c.setFont("Helvetica", 8)
            c.setFillColor(WARM_400)
            c.drawCentredString(w / 2, 1.3 * cm, f"\u2014 {doc.page} \u2014")
            c.setFont("Helvetica-Oblique", 7.5)
            c.setFillColor(WARM_400)
            c.drawString(2 * cm, 1.3 * cm, "Šestinedělí s klidem")
            if chapter_title:
                c.drawRightString(w - 2 * cm, 1.3 * cm,
                                  f"Kapitola {chapter_num}: {chapter_title}")
            c.restoreState()
        return later_page

    story = []

    # ── PRÁZDNÁ STRANA (po obálce) ──
    story.append(PageBreak())

    # ── ÚVOD ──
    story.append(Spacer(1, 1.5 * cm))
    story.append(Paragraph("Milá maminko,", styles['section_heading']))
    story.append(Spacer(1, 0.4 * cm))
    for t in INTRO_TEXT:
        story.append(Paragraph(t, styles['intro']))
    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph("S láskou a úctou,", styles['intro']))
    story.append(Paragraph("<i>Tým Šestinedělí s klidem</i>", styles['intro']))

    # ── OBSAH ──
    story.append(PageBreak())
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("Obsah příručky", styles['chapter_title']))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUSH_200, spaceAfter=14))
    for ch in CHAPTERS:
        story.append(Paragraph(f"{ch['num']}.\u2002{ch['title']}", styles['toc_ch']))
        story.append(Paragraph(ch['subtitle'], styles['toc_sub']))

    # ── KAPITOLY ──
    for ch in CHAPTERS:
        story.append(PageBreak())

        # Prostor pro ilustrovaný header (nakreslí se v onLaterPages)
        # Použijeme Spacer + nadpis s barevným pozadím pomocí Table
        header_data = [[
            Paragraph(f"Kapitola {ch['num']}", styles['chapter_label']),
            "",
        ], [
            Paragraph(ch['title'], styles['chapter_title']),
            "",
        ], [
            Paragraph(ch['subtitle'], styles['chapter_subtitle']),
            "",
        ]]
        col_w = [10 * cm, 5.5 * cm]
        header_table = Table(header_data, colWidths=col_w)
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), ch['color']),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 14),
            ('RIGHTPADDING', (0, 0), (0, -1), 6),
            ('RIGHTPADDING', (1, 0), (1, -1), 10),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('SPAN', (0, 0), (0, 0)),
        ]))

        # Ilustrace jako Drawing vložená do Table buňky
        illus_w, illus_h = 130, 130
        d = Drawing(illus_w, illus_h)
        # Pozadí kresby
        from reportlab.graphics.shapes import Rect as GRect
        bg = GRect(0, 0, illus_w, illus_h)
        bg.fillColor = ch['color']
        bg.strokeColor = None
        d.add(bg)

        # Vložíme ilustraci přes canvas callback – použijeme renderPDF jako flowable
        # Jednodušší: vytvoříme Table s prázdnou buňkou a ilustraci nakreslíme přes
        # onLaterPages. Místo toho vložíme ilustraci jako inline Drawing:
        story.append(header_table)

        # Inline ilustrace pod headerem
        illus_drawing = Drawing(illus_w + 20, illus_h + 20)
        # Nakreslit ilustraci přímo do Drawing pomocí shapes
        _add_illustration_to_drawing(illus_drawing, ch['num'], illus_w, illus_h)
        story.append(illus_drawing)

        story.append(HRFlowable(width="100%", thickness=1, color=BLUSH_200,
                                spaceBefore=6, spaceAfter=10))

        for sec_title, paragraphs in ch['sections']:
            story.append(Paragraph(sec_title, styles['section_heading']))
            for para in paragraphs:
                # Velká písmena na začátku = odrážka
                if para[0].isupper() and (
                    para.startswith(('HOREČKA', 'SILNÉ', 'BOLEST', 'ZARUDNUTÍ',
                                     'LETARGIE', 'DÝCHÁNÍ', 'ŽLOUTENKA', 'PUPEČNÍK',
                                     'MYŠLENKY', 'SILNÁ', 'NECHUTENSTVÍ',
                                     'Záchranná', 'Porodnice', 'Dětský',
                                     'Laktační', 'Krizová'))
                ):
                    story.append(Paragraph(f"\u25aa\u2002{para}", styles['bullet']))
                else:
                    story.append(Paragraph(para, styles['body']))

        story.append(Spacer(1, 0.8 * cm))

        # Tip box
        tip_data = [[
            Paragraph(
                f"Rychlý přehled kapitoly: "
                + ", ".join(s[0] for s in ch['sections']) + ".",
                ParagraphStyle('Tip', fontName='Helvetica', fontSize=9,
                               textColor=WARM_600, leading=13)
            )
        ]]
        tip_table = Table(tip_data, colWidths=[14.5 * cm])
        tip_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), CREAM_100),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('BOX', (0, 0), (-1, -1), 0.5, BLUSH_200),
        ]))
        story.append(tip_table)

    # ── ZÁVĚR ──
    story.append(PageBreak())
    story.append(Spacer(1, 1.5 * cm))
    story.append(Paragraph("Na závěr", styles['chapter_title']))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUSH_200,
                            spaceBefore=4, spaceAfter=16))
    for t in ZAVER_TEXT:
        story.append(Paragraph(t, styles['intro']))
        story.append(Spacer(1, 0.3 * cm))

    story.append(Spacer(1, 1.5 * cm))
    contact_data = [[
        Paragraph(
            "Kontakt & podpora<br/>"
            "<font size='9' color='#6B5E58'>"
            "ahoj@sestinedeli-prirucka.cz<br/>"
            "sestinedeli-prirucka.vercel.app<br/>"
            "14denní záruka vrácení peněz bez otázek.</font>",
            ParagraphStyle('Contact', fontName='Helvetica-Bold', fontSize=11,
                           textColor=WARM_900, leading=18)
        )
    ]]
    ct = Table(contact_data, colWidths=[14.5 * cm])
    ct.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BLUSH_100),
        ('BOX', (0, 0), (-1, -1), 0.8, BLUSH_300),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(ct)

    doc.build(
        story,
        onFirstPage=draw_cover,
        onLaterPages=make_later_page(),
    )
    print(f"PDF vygenerováno: {output_path}")


def _add_illustration_to_drawing(d: Drawing, chapter_num: int, w: float, h: float):
    """
    Přidá zjednodušenou ilustraci do Drawing objektu pomocí shapes.
    """
    from reportlab.graphics.shapes import (
        Circle, Ellipse, Rect, Line, Path, String, Wedge,
    )
    from reportlab.lib.colors import HexColor, white

    cx, cy = w / 2 + 10, h / 2

    color_map = {
        1: (BLUSH_300, BLUSH_500, BLUSH_200),
        2: (BLUSH_200, BLUSH_500, SAGE_300),
        3: (AMBER_300, HexColor('#F59E0B'), CREAM_200),
        4: (HexColor('#A78BFA'), HexColor('#7C3AED'), AMBER_300),
        5: (HexColor('#BAE6FD'), HexColor('#7DD3FC'), BLUSH_200),
        6: (SAGE_300, SAGE_500, AMBER_300),
        7: (BLUSH_200, BLUSH_500, SAGE_200),
        8: (BLUSH_200, BLUSH_300, CREAM_100),
        9: (CREAM_200, BLUSH_300, SAGE_300),
        10: (BLUSH_200, BLUSH_300, AMBER_300),
        11: (SAGE_300, SAGE_500, BLUSH_300),
    }
    c1, c2, c3 = color_map.get(chapter_num, (BLUSH_200, BLUSH_500, SAGE_200))

    if chapter_num == 1:
        # Soustředné kruhy + srdce
        for r, alpha_val in [(50, 0.15), (38, 0.25), (26, 0.4)]:
            circle = Circle(cx, cy, r)
            circle.fillColor = c1
            circle.strokeColor = None
            d.add(circle)
        heart = _heart_path(cx, cy + 2, 13)
        heart.fillColor = c2
        heart.strokeColor = None
        d.add(heart)

    elif chapter_num == 2:
        # Velký oblouk + miminko
        body = Ellipse(cx - 20, cy - 12, cx + 20, cy + 25)
        body.fillColor = CREAM_200
        body.strokeColor = c1
        body.strokeWidth = 1.2
        d.add(body)
        head = Circle(cx, cy + 34, 13)
        head.fillColor = CREAM_200
        head.strokeColor = c1
        head.strokeWidth = 1
        d.add(head)
        # Kapky
        for dx, dy in [(-30, 10), (-36, 22), (-28, 32)]:
            drop = Circle(cx + dx, cy + dy, 3.5)
            drop.fillColor = white
            drop.strokeColor = c1
            drop.strokeWidth = 0.7
            d.add(drop)
        heart2 = _heart_path(cx + 24, cy + 36, 6)
        heart2.fillColor = c2
        heart2.strokeColor = None
        d.add(heart2)

    elif chapter_num == 3:
        # Měsíc (srpek)
        moon1 = Circle(cx - 4, cy + 4, 28)
        moon1.fillColor = c1
        moon1.strokeColor = None
        d.add(moon1)
        moon2 = Circle(cx + 10, cy + 11, 22)
        moon2.fillColor = HexColor('#EAF0E8')
        moon2.strokeColor = None
        d.add(moon2)
        # Hvězdy
        for sx, sy, sr in [(-35, 28, 4), (30, 36, 3.5), (-26, -8, 3),
                            (36, 8, 3), (4, -28, 3.5)]:
            star = Circle(cx + sx, cy + sy, sr)
            star.fillColor = c1
            star.strokeColor = None
            d.add(star)

    elif chapter_num == 4:
        # Slunce + oblaky
        sun = Circle(cx - 18, cy + 18, 20)
        sun.fillColor = c3
        sun.strokeColor = None
        d.add(sun)
        for bx, by, br in [(0, 0, 18), (-16, -7, 13), (16, -4, 15),
                            (-7, -16, 11), (8, -14, 12)]:
            cloud = Circle(cx + bx, cy + by, br)
            cloud.fillColor = white
            cloud.strokeColor = HexColor('#CBD5E1')
            cloud.strokeWidth = 0.8
            d.add(cloud)
        heart3 = _heart_path(cx + 28, cy - 22, 7)
        heart3.fillColor = c1
        heart3.strokeColor = None
        d.add(heart3)

    elif chapter_num == 5:
        # Vanička + miminko
        tub = Ellipse(cx - 38, cy - 22, cx + 38, cy + 12)
        tub.fillColor = c1
        tub.strokeColor = c2
        tub.strokeWidth = 1.2
        d.add(tub)
        water = Ellipse(cx - 35, cy - 15, cx + 35, cy + 6)
        water.fillColor = HexColor('#BAE6FD')
        water.strokeColor = None
        d.add(water)
        head_b = Circle(cx, cy + 18, 14)
        head_b.fillColor = CREAM_200
        head_b.strokeColor = c2
        head_b.strokeWidth = 1
        d.add(head_b)
        for bx, by, br in [(-26, 28, 4.5), (-36, 42, 3), (30, 32, 4), (38, 46, 5.5)]:
            bub = Circle(cx + bx, cy + by, br)
            bub.fillColor = white
            bub.strokeColor = c2
            bub.strokeWidth = 0.7
            d.add(bub)

    elif chapter_num == 6:
        # Miska
        rim = Ellipse(cx - 38, cy + 3, cx + 38, cy + 15)
        rim.fillColor = c1
        rim.strokeColor = c2
        rim.strokeWidth = 1
        d.add(rim)
        for fx, fy, fc in [(cx - 10, cy - 10, SAGE_400),
                            (cx + 8, cy - 13, HexColor('#F47F7F')),
                            (cx, cy - 3, c3)]:
            food = Circle(fx, fy, 7)
            food.fillColor = fc
            food.strokeColor = None
            d.add(food)
        for lx, ly in [(-32, 32), (-22, 44), (-40, 44)]:
            leaf = Ellipse(cx + lx - 6, cy + ly - 4, cx + lx + 6, cy + ly + 4)
            leaf.fillColor = SAGE_400
            leaf.strokeColor = None
            d.add(leaf)

    elif chapter_num == 7:
        # Dvě srdce vedle sebe
        h_left = _heart_path(cx - 16, cy + 5, 20)
        h_left.fillColor = c1
        h_left.strokeColor = c2
        h_left.strokeWidth = 0.8
        d.add(h_left)
        h_right = _heart_path(cx + 16, cy + 5, 20)
        h_right.fillColor = SAGE_200
        h_right.strokeColor = SAGE_300
        h_right.strokeWidth = 0.8
        d.add(h_right)
        h_small = _heart_path(cx, cy + 28, 8)
        h_small.fillColor = c2
        h_small.strokeColor = None
        d.add(h_small)
        for sx, sy in [(-38, 28), (38, 32), (0, -12)]:
            star2 = Circle(cx + sx, cy + sy, 3)
            star2.fillColor = c3
            star2.strokeColor = None
            d.add(star2)

    elif chapter_num == 8:
        # Domeček
        # Zdi
        walls = Rect(cx - 32, cy - 28, 64, 44)
        walls.fillColor = CREAM_100
        walls.strokeColor = c1
        walls.strokeWidth = 1
        d.add(walls)
        # Střecha – simulace trojúhelníkem přes tři obdélníky
        for i in range(8):
            roof_r = Rect(cx - 34 + i * 5, cy + 16 + i * 2, 36 - i * 4, 4)
            roof_r.fillColor = c1
            roof_r.strokeColor = None
            d.add(roof_r)
        roof_top = Circle(cx, cy + 40, 14)
        roof_top.fillColor = c1
        roof_top.strokeColor = None
        d.add(roof_top)
        # Dveře
        door = Rect(cx - 8, cy - 28, 16, 28)
        door.fillColor = c2
        door.strokeColor = c2
        door.strokeWidth = 0.5
        d.add(door)
        # Okno
        win = Rect(cx - 28, cy - 2, 14, 12)
        win.fillColor = HexColor('#BAE6FD')
        win.strokeColor = c1
        win.strokeWidth = 0.5
        d.add(win)

    elif chapter_num == 9:
        # Dveře
        frame = Rect(cx - 26, cy - 42, 52, 74)
        frame.fillColor = c1
        frame.strokeColor = c2
        frame.strokeWidth = 1.5
        d.add(frame)
        left_door = Rect(cx - 22, cy - 38, 22, 67)
        left_door.fillColor = CREAM_100
        left_door.strokeColor = c2
        left_door.strokeWidth = 1
        d.add(left_door)
        right_door = Rect(cx, cy - 38, 22, 67)
        right_door.fillColor = CREAM_100
        right_door.strokeColor = c2
        right_door.strokeWidth = 1
        d.add(right_door)
        # Věnec
        wreath = Circle(cx, cy + 20, 10)
        wreath.fillColor = None
        wreath.strokeColor = SAGE_400
        wreath.strokeWidth = 1.5
        d.add(wreath)
        for a in range(0, 360, 45):
            lx2 = cx + 10 * math.cos(math.radians(a))
            ly2 = cy + 20 + 10 * math.sin(math.radians(a))
            leaf2 = Circle(lx2, ly2, 3)
            leaf2.fillColor = SAGE_400
            leaf2.strokeColor = None
            d.add(leaf2)
        h_bow = _heart_path(cx, cy + 9, 4)
        h_bow.fillColor = c2
        h_bow.strokeColor = None
        d.add(h_bow)

    elif chapter_num == 10:
        # Květ ze semínka
        stem = Line(cx, cy - 32, cx, cy + 28)
        stem.strokeColor = SAGE_500
        stem.strokeWidth = 2.5
        d.add(stem)
        # Okvětní lístky
        for angle in range(0, 360, 72):
            rad = math.radians(angle)
            px2 = cx + 14 * math.cos(rad)
            py2 = cy + 28 + 14 * math.sin(rad)
            petal = Ellipse(px2 - 7, py2 - 4, px2 + 7, py2 + 4)
            petal.fillColor = c1
            petal.strokeColor = c2
            petal.strokeWidth = 0.5
            d.add(petal)
        # Střed
        center = Circle(cx, cy + 28, 9)
        center.fillColor = AMBER_300
        center.strokeColor = HexColor('#F59E0B')
        center.strokeWidth = 0.8
        d.add(center)
        # Lístky na stonku
        leaf_l = Ellipse(cx - 18, cy + 4, cx, cy + 14)
        leaf_l.fillColor = SAGE_400
        leaf_l.strokeColor = None
        d.add(leaf_l)
        leaf_r = Ellipse(cx, cy - 6, cx + 18, cy + 4)
        leaf_r.fillColor = SAGE_300
        leaf_r.strokeColor = None
        d.add(leaf_r)

    elif chapter_num == 11:
        # Lékařský kříž
        cross_v = Rect(cx - 9, cy - 28, 18, 56)
        cross_v.fillColor = c1
        cross_v.strokeColor = c2
        cross_v.strokeWidth = 1
        d.add(cross_v)
        cross_h = Rect(cx - 28, cy - 9, 56, 18)
        cross_h.fillColor = c1
        cross_h.strokeColor = c2
        cross_h.strokeWidth = 1
        d.add(cross_h)
        inner = Rect(cx - 6, cy - 6, 12, 12)
        inner.fillColor = white
        inner.strokeColor = None
        d.add(inner)
        # Telefon
        phone = Rect(cx + 28, cy - 24, 16, 28)
        phone.fillColor = c2
        phone.strokeColor = c2
        phone.strokeWidth = 0.8
        phone.rx = 3
        phone.ry = 3
        d.add(phone)
        screen = Rect(cx + 31, cy - 16, 10, 14)
        screen.fillColor = HexColor('#BAE6FD')
        screen.strokeColor = None
        d.add(screen)


def _heart_path(cx: float, cy: float, size: float) -> Path:
    """Vytvoří srdce jako Path objekt pro Drawing."""
    s = size
    p = Path()
    p.moveTo(cx, cy - s * 0.55)
    p.curveTo(cx - s * 1.1, cy + s * 0.35,
               cx - s * 1.1, cy + s * 1.1,
               cx, cy + s * 0.55)
    p.curveTo(cx + s * 1.1, cy + s * 1.1,
               cx + s * 1.1, cy + s * 0.35,
               cx, cy - s * 0.55)
    p.closePath()
    return p


if __name__ == "__main__":
    build_pdf("/Users/jevci/Sites/sestinedeli-prirucka/public/sestinedeli-s-klidem.pdf")
