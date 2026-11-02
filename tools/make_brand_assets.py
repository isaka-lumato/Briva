"""Generate Briva brand assets and browser-tab favicons from images/brivaLogo.png.
Run from project root:  python tools/make_brand_assets.py
"""
import json
import os
import shutil
from PIL import Image

ROOT = os.getcwd()
OUT = os.path.join(ROOT, "images", "brand")
os.makedirs(OUT, exist_ok=True)

INK = (15, 26, 36)  # --ink-900 #0F1A24
src = Image.open(os.path.join(ROOT, "images", "brivaLogo.png")).convert("RGBA")


def is_copper(r, g, b):
    return r > 150 and (r - b) > 60


# 1. Trimmed full-color logo for light header (382x196, zero dead padding)
logo = src.crop(src.getbbox())
logo.save(os.path.join(OUT, "briva-logo.png"), optimize=True)

# 2. Reversed logo for dark #0F1A24 footer (charcoal -> crisp white, copper preserved)
light = logo.copy()
px = light.load()
for y in range(light.height):
    for x in range(light.width):
        r, g, b, a = px[x, y]
        if a and not is_copper(r, g, b):
            px[x, y] = (255, 255, 255, a)
light.save(os.path.join(OUT, "briva-logo-light.png"), optimize=True)

# 3. Isolate Briva emblem (copper gear + mountain diamond + pickaxe) for favicons
X0, Y0, X1, Y1 = 283, 148, 446, 268
mark = src.crop((X0, Y0, X1, Y1))
mp = mark.load()
for y in range(mark.height):
    for x in range(mark.width):
        ax, ay = x + X0, y + Y0
        r, g, b, a = mp[x, y]
        if ay >= 232 and not (372 <= ax <= 402):
            mp[x, y] = (0, 0, 0, 0)
        elif ay >= 250 and a and is_copper(r, g, b):
            mp[x, y] = (0, 0, 0, 0)
mark = mark.crop(mark.getbbox())


def square_icon(img, size, pad_ratio=0.06, bg=(0, 0, 0, 0)):
    side = max(img.width, img.height)
    pad = int(side * pad_ratio)
    canvas = Image.new("RGBA", (side + 2 * pad, side + 2 * pad), bg)
    canvas.paste(img, (pad + (side - img.width) // 2, pad + (side - img.height) // 2), img)
    return canvas.resize((size, size), Image.LANCZOS)


square_icon(mark, 16).save(os.path.join(OUT, "favicon-16x16.png"), optimize=True)
square_icon(mark, 32).save(os.path.join(OUT, "favicon-32x32.png"), optimize=True)
square_icon(mark, 192).save(os.path.join(OUT, "icon-192.png"), optimize=True)
square_icon(mark, 512).save(os.path.join(OUT, "icon-512.png"), optimize=True)
square_icon(mark, 180, pad_ratio=0.14, bg=(255, 255, 255, 255)).convert("RGB").save(
    os.path.join(OUT, "apple-touch-icon.png"), optimize=True
)
square_icon(mark, 256).save(
    os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)]
)
shutil.copyfile(os.path.join(OUT, "favicon-32x32.png"), os.path.join(ROOT, "images", "favicon.png"))

# 4. Web App Manifest
with open(os.path.join(ROOT, "site.webmanifest"), "w", encoding="utf-8") as f:
    json.dump({
        "name": "Briva Exploration & Mining",
        "short_name": "Briva",
        "icons": [
            {"src": "images/brand/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "images/brand/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
        "theme_color": "#0F1A24",
        "background_color": "#FFFFFF",
        "display": "standalone",
    }, f, indent=2)

# 5. Open Graph Social Preview Card (1200x630)
W, H = 1200, 630
bg_path = os.path.join(ROOT, "images", "slider-main", "bg2.jpg")
photo = Image.open(bg_path).convert("RGB")
scale = max(W / photo.width, H / photo.height)
photo = photo.resize((int(photo.width * scale) + 1, int(photo.height * scale) + 1), Image.LANCZOS)
left, top = (photo.width - W) // 2, (photo.height - H) // 2
og = photo.crop((left, top, left + W, top + H)).convert("RGBA")
og = Image.alpha_composite(og, Image.new("RGBA", (W, H), INK + (210,)))
lw = 440
lg = light.resize((lw, int(light.height * lw / light.width)), Image.LANCZOS)
og.paste(lg, ((W - lg.width) // 2, (H - lg.height) // 2), lg)
og.convert("RGB").save(os.path.join(OUT, "og-image.jpg"), quality=86, optimize=True)
print("Generated Briva brand & favicon suite successfully.")
