"""Optimize oversized project/hero images and convert non-web TIFF files.
Run from project root:  python tools/optimize_assets.py
"""
import glob
import os
from PIL import Image

ROOT = os.getcwd()

# 1. Convert any .tiff in images/projects to .jpg and remove .tiff
for tiff_path in glob.glob(os.path.join(ROOT, "images", "projects", "*.tif*")):
    base = os.path.splitext(tiff_path)[0]
    jpg_path = base + ".jpg"
    im = Image.open(tiff_path).convert("RGB")
    if im.width > 1600:
        im = im.resize((1600, int(im.height * 1600 / im.width)), Image.LANCZOS)
    im.save(jpg_path, "JPEG", quality=84, optimize=True)
    os.remove(tiff_path)
    print(f"Converted {os.path.basename(tiff_path)} -> {os.path.basename(jpg_path)}")

# 2. Compress oversized JPEGs (>450 KB) in images/projects and images/slider-main
for folder in ["projects", "slider-main"]:
    for path in glob.glob(os.path.join(ROOT, "images", folder, "*.jp*g")):
        size_kb = os.path.getsize(path) / 1024
        if size_kb > 450:
            im = Image.open(path).convert("RGB")
            if im.width > 1600:
                im = im.resize((1600, int(im.height * 1600 / im.width)), Image.LANCZOS)
            im.save(path, "JPEG", quality=83, optimize=True)
            new_kb = os.path.getsize(path) / 1024
            print(f"Optimized {os.path.basename(path)}: {size_kb:.0f}KB -> {new_kb:.0f}KB")
