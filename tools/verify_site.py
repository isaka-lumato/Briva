"""Automated QA & architectural compliance gate for the refactored Briva website."""
import os
import re
import sys

PAGES = [
    "index.html", "about.html", "services.html", "service-single.html",
    "projects.html", "projects-single.html", "equipment.html",
    "equipment-megascan.html", "equipment-pinpointer.html",
    "team.html", "contact.html", "thank-you.html", "404.html",
]

BANNED_PATTERNS = [
    r"Constra",
    r"Themefisher",
    r"Construction Html5 Template",
    r"Lorem ipsum",
    r"3 wolf moon",
    r"Weldon Cash",
    r"Developed by\s*<a[^>]*>\s*Briva",
    r"<style[\s>]",
    r'\sstyle="',
    r"plugins/jQuery",
    r"plugins/bootstrap",
    r"plugins/slick",
    r"images/banner/banner1\.jpg",
]

REQUIRED_SNIPPETS = [
    'href="favicon.ico"',
    'href="images/brand/favicon-32x32.png"',
    'href="images/brand/apple-touch-icon.png"',
    'href="css/tokens.css"',
    'href="css/base.css"',
    'href="css/components.css"',
    'href="css/pages.css"',
    'href="https://lumatotech.netlify.app"',
    "Lumato Tech",
]

errors = []

for required_asset in [
    "favicon.ico", "site.webmanifest", "robots.txt", "sitemap.xml", "_headers",
    "images/brand/briva-logo.png", "images/brand/briva-logo-light.png",
    "images/brand/favicon-32x32.png", "images/brand/apple-touch-icon.png",
    "images/brand/og-image.jpg",
    "images/equipment/mega-scan-pro.jpg", "images/equipment/gold-pin-pointer.jpg",
    "images/team/alex-bashire.jpg", "images/team/kolipaka-venu.jpg",
    "images/team/srirama-yellapragada.jpg", "images/team/jackline-kidendei.jpg",
    "images/team/vashty-nyembera.jpg",
    "data/projects.json", "data/services.json",
]:
    if not os.path.exists(required_asset):
        errors.append(f"MISSING ASSET: {required_asset}")

footer_hashes = set()
header_hashes = set()

for page in PAGES:
    if not os.path.exists(page):
        errors.append(f"MISSING PAGE: {page}")
        continue
    html = open(page, encoding="utf-8").read()

    for pat in BANNED_PATTERNS:
        if re.search(pat, html, flags=re.IGNORECASE):
            errors.append(f"{page}: contains banned pattern '{pat}'")

    for snip in REQUIRED_SNIPPETS:
        if snip not in html:
            errors.append(f"{page}: missing required snippet '{snip}'")

    # Verify canonical header & footer partial parity across all 13 pages
    hm = re.search(r"<!-- PARTIAL:HEADER:START -->(.*?)<!-- PARTIAL:HEADER:END -->", html, re.S)
    fm = re.search(r"<!-- PARTIAL:FOOTER:START -->(.*?)<!-- PARTIAL:FOOTER:END -->", html, re.S)
    if not hm or not fm:
        errors.append(f"{page}: missing PARTIAL:HEADER or PARTIAL:FOOTER markers")
    else:
        norm_header = re.sub(r'\s+aria-current="page"|\s+is-active', "", hm.group(1))
        header_hashes.add(norm_header)
        footer_hashes.add(fm.group(1))

    # Verify all local src/href assets exist on disk
    for attr_val in re.findall(r'(?:src|href)="([^"#?]+)', html):
        if attr_val.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "/")):
            continue
        if not os.path.exists(attr_val):
            errors.append(f"{page}: broken local link/asset '{attr_val}'")

if len(header_hashes) != 1:
    errors.append(f"Header partial drift detected across pages ({len(header_hashes)} variants)")
if len(footer_hashes) != 1:
    errors.append(f"Footer partial drift detected across pages ({len(footer_hashes)} variants)")

# Verify team directory contains only the 5 approved clean portraits and team.html has 6 profile cards
expected_team_imgs = {
    "alex-bashire.jpg", "kolipaka-venu.jpg", "srirama-yellapragada.jpg",
    "jackline-kidendei.jpg", "vashty-nyembera.jpg",
}
actual_team_imgs = set(os.listdir("images/team"))
if actual_team_imgs != expected_team_imgs:
    errors.append(f"images/team mismatch: {actual_team_imgs ^ expected_team_imgs}")
if os.path.exists("team.html"):
    card_count = len(re.findall(r'class="card profile-card"', open("team.html", encoding="utf-8").read()))
    if card_count != 6:
        errors.append(f"team.html: expected 6 profile cards, found {card_count}")

if errors:
    print(f"QA FAILED ({len(errors)} issues):")
    for e in errors:
        print("  -", e)
    sys.exit(1)

print(f"QA PASSED: All {len(PAGES)} pages verified clean, unified, branded, zero inline styles, and credited to Lumato Tech (https://lumatotech.netlify.app).")

# Additional deep checks: JSON asset existence + CSS custom property integrity
import json

for p in json.load(open("data/projects.json", encoding="utf-8"))["projects"]:
    for im in p["images"]:
        assert os.path.exists(im), f"Missing project image: {im}"

for s in json.load(open("data/services.json", encoding="utf-8"))["services"]:
    assert os.path.exists(s["image"]), f"Missing service image: {s['image']}"

defined_vars = set()
for cf in ["css/tokens.css", "css/base.css", "css/components.css", "css/pages.css"]:
    defined_vars.update(re.findall(r"(--[a-zA-Z0-9_-]+)\s*:", open(cf, encoding="utf-8").read()))

for cf in ["css/base.css", "css/components.css", "css/pages.css"]:
    txt = open(cf, encoding="utf-8").read()
    for m in re.finditer(r"var\(\s*(--[a-zA-Z0-9_-]+)\s*\)", txt):
        assert m.group(1) in defined_vars, f"{cf}: undefined CSS variable {m.group(1)}"

print("DEEP CHECKS PASSED: All JSON image paths exist and all CSS custom properties are defined.")
