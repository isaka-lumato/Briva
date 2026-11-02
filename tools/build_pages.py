"""Canonical static site generator for Briva Exploration & Mining.
Generates all 13 production HTML pages with 100% shared header, favicons, and Lumato Tech footer.
Run from project root:  python tools/build_pages.py
"""
import json
import os

ROOT = os.getcwd()
SERVICES = json.load(open(os.path.join(ROOT, "data", "services.json"), encoding="utf-8"))["services"]

ICONS = {
    "arrow": '<svg class="icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>',
    "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
    "compass": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    "mountain": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m8 3 4 8 5-5 5 15H2L8 3z"/></svg>',
    "drill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 2v20M8 6l4 4 4-4M8 12l4 4 4-4"/><circle cx="12" cy="20" r="1.5"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "briefcase": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "file": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><polyline points="9 15 12 18 15 15"/></svg>',
}

SERVICE_ICON_MAP = {
    "geological-exploration": ICONS["compass"],
    "resource-estimation": ICONS["layers"],
    "mine-planning": ICONS["mountain"],
    "drilling-supervision": ICONS["drill"],
    "asm-support": ICONS["shield"],
    "ma-advisory": ICONS["briefcase"],
}

NAV_ITEMS = [
    ("home", "Home", "index.html"),
    ("about", "About", "about.html"),
    ("services", "Services", "services.html"),
    ("projects", "Projects", "projects.html"),
    ("equipment", "Equipment", "equipment.html"),
    ("team", "Team", "team.html"),
]


def render_shell(filename, title, description, active_nav, body_html, extra_scripts=None, include_netlify_identity=False):
    extra_scripts = extra_scripts or []

    desktop_links = []
    mobile_links = []
    for key, label, href in NAV_ITEMS:
        is_current = key == active_nav
        aria = ' aria-current="page"' if is_current else ""
        cls = " is-active" if is_current else ""
        desktop_links.append(f'<a class="site-nav__link{cls}" href="{href}"{aria}>{label}</a>')
        mobile_links.append(f'<a class="mobile-drawer__link{cls}" href="{href}"{aria}><span>{label}</span></a>')

    contact_aria = ' aria-current="page"' if active_nav == "contact" else ""
    mobile_links.append(
        f'<a class="mobile-drawer__link{" is-active" if active_nav == "contact" else ""}" href="contact.html"{contact_aria}><span>Contact</span></a>'
    )

    netlify_block = ""
    if include_netlify_identity:
        netlify_block = """
  <script src="https://identity.netlify.com/v1/netlify-identity-widget.js" defer></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      if (window.netlifyIdentity) {
        window.netlifyIdentity.on('init', function (user) {
          if (!user) {
            window.netlifyIdentity.on('login', function () {
              document.location.href = '/admin/';
            });
          }
        });
      }
    });
  </script>"""

    scripts_html = '\n  '.join(
        ['<script src="js/main.js" defer></script>'] +
        [f'<script src="{s}" defer></script>' for s in extra_scripts]
    )

    html = f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Briva Exploration &amp; Mining</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#0F1A24">

  <!-- Favicons (Authentic Briva Emblem) -->
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="images/brand/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="images/brand/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="images/brand/apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Briva Exploration &amp; Mining">
  <meta property="og:title" content="{title} | Briva Exploration &amp; Mining">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="images/brand/og-image.jpg">

  <!-- Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">

  <!-- Modular Design System -->
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/pages.css">{netlify_block}
</head>

<body>
  <a class="skip-link" href="#main-content">Skip to main content</a>

  <!-- PARTIAL:HEADER:START -->
  <div class="topbar">
    <div class="container topbar__inner">
      <div class="topbar__group">
        <span class="topbar__item">{ICONS["pin"]} 11259 Dar es Salaam, Tanzania</span>
        <span class="topbar__divider" aria-hidden="true"></span>
        <span class="topbar__item">{ICONS["clock"]} Mon–Fri 10:00–16:00 &middot; Sat 12:00–15:00</span>
      </div>
      <div class="topbar__group">
        <a class="topbar__item" href="tel:+255767413950">{ICONS["phone"]} +255 767 413 950</a>
        <span class="topbar__divider" aria-hidden="true"></span>
        <a class="topbar__item" href="mailto:info@briva.co.tz">{ICONS["mail"]} info@briva.co.tz</a>
        <span class="topbar__divider" aria-hidden="true"></span>
        <a class="topbar__item" href="https://www.instagram.com/briva_mining_exploration" target="_blank" rel="noopener noreferrer" aria-label="Briva on Instagram">{ICONS["instagram"]} Instagram</a>
      </div>
    </div>
  </div>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="site-brand" href="index.html" aria-label="Briva Exploration &amp; Mining — Home">
        <img src="images/brand/briva-logo.png" alt="Briva Exploration &amp; Mining" width="148" height="76">
      </a>

      <nav class="site-nav" aria-label="Primary navigation">
        {" ".join(desktop_links)}
      </nav>

      <div class="site-header__actions">
        <a class="btn btn--primary btn--sm site-header__cta" href="contact.html"{contact_aria}>Contact Us</a>
        <button type="button" class="nav-toggle" data-nav-open aria-expanded="false" aria-controls="mobile-drawer" aria-label="Open navigation menu">
          {ICONS["menu"]}
        </button>
      </div>
    </div>
  </header>

  <div class="mobile-drawer" id="mobile-drawer" aria-hidden="true">
    <div class="mobile-drawer__backdrop" data-nav-close></div>
    <div class="mobile-drawer__panel" role="dialog" aria-modal="true" aria-label="Site navigation">
      <div>
        <div class="mobile-drawer__head">
          <img src="images/brand/briva-logo.png" alt="Briva Exploration &amp; Mining" width="128" height="66">
          <button type="button" class="nav-toggle" data-nav-close aria-label="Close navigation menu">
            {ICONS["close"]}
          </button>
        </div>
        <nav class="mobile-drawer__nav" aria-label="Mobile navigation">
          {" ".join(mobile_links)}
        </nav>
      </div>
      <div class="mobile-drawer__foot">
        <div class="mobile-drawer__contact">
          <a href="tel:+255767413950">+255 767 413 950</a>
          <a href="mailto:info@briva.co.tz">info@briva.co.tz</a>
          <span>11259 Dar es Salaam, Tanzania</span>
        </div>
        <a class="btn btn--primary w-full" href="contact.html">Request a Consultation</a>
      </div>
    </div>
  </div>
  <!-- PARTIAL:HEADER:END -->

  <main id="main-content">
{body_html}
  </main>

  <!-- PARTIAL:FOOTER:START -->
  <footer class="site-footer">
    <div class="container site-footer__main">
      <div>
        <a href="index.html" aria-label="Briva Exploration &amp; Mining">
          <img class="site-footer__logo" loading="lazy" src="images/brand/briva-logo-light.png" alt="Briva Exploration &amp; Mining" width="156" height="80">
        </a>
        <p class="site-footer__summary">
          Mineral exploration, 3D resource modelling, mine engineering, drilling supervision, and certified geophysical instruments across East Africa.
        </p>
        <a class="site-footer__social" href="https://www.instagram.com/briva_mining_exploration" target="_blank" rel="noopener noreferrer">
          {ICONS["instagram"]} @briva_mining_exploration
        </a>
      </div>

      <div>
        <h3 class="site-footer__heading">Core Services</h3>
        <ul class="site-footer__links">
          <li><a href="service-single.html?service=geological-exploration">Geological &amp; Exploration</a></li>
          <li><a href="service-single.html?service=resource-estimation">Resource Estimation &amp; Modelling</a></li>
          <li><a href="service-single.html?service=mine-planning">Mining Engineering &amp; Planning</a></li>
          <li><a href="service-single.html?service=drilling-supervision">Drilling Supervision</a></li>
          <li><a href="service-single.html?service=asm-support">Small-Scale &amp; ASM Support</a></li>
          <li><a href="service-single.html?service=ma-advisory">M&amp;A &amp; Joint Ventures</a></li>
        </ul>
      </div>

      <div>
        <h3 class="site-footer__heading">Company</h3>
        <ul class="site-footer__links">
          <li><a href="about.html">About Briva</a></li>
          <li><a href="projects.html">Field Projects</a></li>
          <li><a href="equipment.html">Field Equipment</a></li>
          <li><a href="equipment-megascan.html">Mega Scan Pro</a></li>
          <li><a href="equipment-pinpointer.html">Gold Pin Pointer</a></li>
          <li><a href="team.html">Leadership &amp; Team</a></li>
          <li><a href="contact.html">Contact Office</a></li>
        </ul>
      </div>

      <div>
        <h3 class="site-footer__heading">Dar es Salaam Office</h3>
        <ul class="site-footer__contact-list">
          <li class="site-footer__contact-item">
            {ICONS["pin"]}
            <span>P.O. Box 11259<br>Dar es Salaam, Tanzania</span>
          </li>
          <li class="site-footer__contact-item">
            {ICONS["phone"]}
            <a href="tel:+255767413950">+255 767 413 950</a>
          </li>
          <li class="site-footer__contact-item">
            {ICONS["mail"]}
            <a href="mailto:info@briva.co.tz">info@briva.co.tz</a>
          </li>
          <li class="site-footer__contact-item">
            {ICONS["clock"]}
            <span>Mon–Fri: 10:00 – 16:00<br>Saturday: 12:00 – 15:00</span>
          </li>
        </ul>
      </div>
    </div>

    <div class="site-footer__bottom">
      <div class="container site-footer__bottom-inner">
        <p class="site-footer__copyright">
          &copy; <span data-year>2026</span> Briva Exploration &amp; Mining. All rights reserved.
        </p>
        <p class="site-footer__credit">
          Designed &amp; Developed by <a href="https://lumatotech.netlify.app" target="_blank" rel="noopener noreferrer">Lumato Tech</a>
        </p>
      </div>
    </div>
  </footer>
  <!-- PARTIAL:FOOTER:END -->

  {scripts_html}
</body>

</html>
"""
    open(os.path.join(ROOT, filename), "w", encoding="utf-8").write(html)
    print(f"Built {filename}")


def render_service_cards():
    cards = []
    for s in SERVICES:
        icon = SERVICE_ICON_MAP.get(s["slug"], ICONS["compass"])
        url = f"service-single.html?service={s['slug']}"
        bullets = "".join(f"<li>{h}</li>" for h in s["highlights"])
        cards.append(f"""
        <article class="card card--interactive service-card" data-reveal>
          <div>
            <div class="service-card__top">
              <span class="service-card__icon">{icon}</span>
              <span class="service-card__num">{s["num"]}</span>
            </div>
            <h3 class="service-card__title"><a href="{url}">{s["title"]}</a></h3>
            <p class="service-card__desc">{s["summary"]}</p>
            <ul class="service-card__list">{bullets}</ul>
          </div>
          <a class="link-arrow" href="{url}">Technical Scope {ICONS["arrow"]}</a>
        </article>""")
    return "\n".join(cards)


def render_cta_band(heading="Discuss Your Licence or Programme",
                    sub="Speak directly with our senior geologists and mining engineers in Dar es Salaam.",
                    primary_label="Schedule a Consultation",
                    primary_href="contact.html"):
    return f"""
    <section class="cta-band">
      <div class="container cta-band__inner">
        <div>
          <span class="eyebrow eyebrow--light">Dar es Salaam Advisory</span>
          <h2>{heading}</h2>
          <p>{sub}</p>
        </div>
        <div class="cta-band__actions">
          <a class="btn btn--primary btn--lg" href="{primary_href}">{primary_label} {ICONS["arrow"]}</a>
          <a class="btn btn--outline-light btn--lg" href="tel:+255767413950">{ICONS["phone"]} +255 767 413 950</a>
        </div>
      </div>
    </section>"""


# ==============================================================================
# 1. index.html
# ==============================================================================
home_body = f"""
    <section class="home-hero">
      <div class="container">
        <div class="home-hero__body">
          <span class="eyebrow eyebrow--light">Tanzania &middot; East Africa</span>
          <h1>Precision Exploration.<br>Responsible Mining.</h1>
          <p class="home-hero__lead">
            Geological discovery, 3D resource modelling, mine engineering, and certified geophysical systems.
          </p>
          <div class="home-hero__actions">
            <a class="btn btn--primary btn--lg" href="services.html">Our Services {ICONS["arrow"]}</a>
            <a class="btn btn--outline-light btn--lg" href="projects.html">Field Projects</a>
          </div>
        </div>
      </div>
      <div class="capability-strip">
        <div class="container capability-strip__grid">
          <div class="capability-item">
            <span class="capability-item__val tabular">20+ Yrs</span>
            <span class="capability-item__label">Leadership Experience</span>
          </div>
          <div class="capability-item">
            <span class="capability-item__val tabular">14+</span>
            <span class="capability-item__label">Tanzanian Field Mandates</span>
          </div>
          <div class="capability-item">
            <span class="capability-item__val tabular">6</span>
            <span class="capability-item__label">Technical Disciplines</span>
          </div>
          <div class="capability-item">
            <span class="capability-item__val">Dar es Salaam</span>
            <span class="capability-item__label">Regional Headquarters</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split-layout">
        <div data-reveal>
          <span class="eyebrow">About Briva</span>
          <h2>Field Rigour Across Every Stage of the Asset Lifecycle</h2>
          <p>
            Headquartered in Dar es Salaam, Briva unites senior geologists, geophysicists, mining engineers, and corporate advisors to de-risk mineral tenures across East Africa.
          </p>
          <p>
            From greenfield lithium pegmatites and polymetallic belts to diamond core supervision and active mine planning, every recommendation rests on QA/QC-verified field data.
          </p>
          <div class="check-grid">
            <div class="check-item">{ICONS["check"]} <span>International &amp; local leadership</span></div>
            <div class="check-item">{ICONS["check"]} <span>QA/QC-governed sampling &amp; logging</span></div>
            <div class="check-item">{ICONS["check"]} <span>Open-pit &amp; underground engineering</span></div>
            <div class="check-item">{ICONS["check"]} <span>Zero-harm site governance</span></div>
          </div>
          <a class="btn btn--outline" href="about.html">About the Firm {ICONS["arrow"]}</a>
        </div>

        <div class="pillar-stack" data-reveal>
          <div class="pillar-box">
            <h3>Vision</h3>
            <p>To be Africa’s benchmark mining and exploration consultancy—defined by technical precision, sustainability, and integrity.</p>
          </div>
          <div class="pillar-box">
            <h3>Mission</h3>
            <p>Deliver reliable, cost-disciplined exploration and engineering solutions anchored in environmental stewardship and community partnership.</p>
          </div>
          <div class="pillar-box">
            <h3>Commodities</h3>
            <p>Active track record across Gold, Lithium, Flake Graphite, Copper-Zinc, Coal, Beryllium, Dolomite, and Industrial Quartz.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Capabilities</span>
            <h2>Core Consulting Disciplines</h2>
            <p class="section-lead">Integrated geological, engineering, and transaction advisory services.</p>
          </div>
          <a class="btn btn--outline" href="services.html">All Services {ICONS["arrow"]}</a>
        </div>
        <div class="grid grid--3">
          {render_service_cards()}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Track Record</span>
            <h2>Selected Field Projects</h2>
            <p class="section-lead">Exploration, mapping, and mine support delivered across Tanzania.</p>
          </div>
          <a class="btn btn--outline" href="projects.html">All 14 Projects {ICONS["arrow"]}</a>
        </div>
        <div id="featured-projects-grid" class="grid grid--3"></div>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="equipment-feature" data-reveal>
          <div>
            <span class="eyebrow">Instrumentation</span>
            <h2>Geophysical Scanners &amp; Target Detectors</h2>
            <p>
              Briva supplies certified subsurface detection instruments for outright purchase or field rental—backed by geologist-led operator training and a 1-year local warranty.
            </p>
            <div class="check-grid">
              <div class="check-item">{ICONS["check"]} <span>Purchase or field rental</span></div>
              <div class="check-item">{ICONS["check"]} <span>Operator training included</span></div>
            </div>
            <a class="btn btn--primary" href="equipment.html">View Equipment {ICONS["arrow"]}</a>
          </div>
          <div class="equipment-feature__preview">
            <a class="equipment-mini-card card--interactive" href="equipment-megascan.html">
              <img loading="lazy" src="images/equipment/mega-scan-pro.jpg" alt="Mega Scan Pro Geophysical Scanner">
              <h4>Mega Scan Pro</h4>
              <span class="tabular">TZS 20,000,000 &middot; 50 m</span>
            </a>
            <a class="equipment-mini-card card--interactive" href="equipment-pinpointer.html">
              <img loading="lazy" src="images/equipment/gold-pin-pointer.jpg" alt="Gold Pin Pointer Detector">
              <h4>Gold Pin Pointer</h4>
              <span class="tabular">TZS 500,000 &middot; IP68</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Partners &amp; Endorsements</span>
          <h2>Trusted Across Tanzania’s Mining Sector</h2>
        </div>

        <div class="grid grid--3 mb-10">
          <article class="card testimonial-card" data-reveal>
            <p class="testimonial-card__quote">
              &ldquo;Briva combines technical expertise with field professionalism, delivering accurate geological datasets that have been crucial to our exploration decisions.&rdquo;
            </p>
            <div class="testimonial-card__author">
              <span class="avatar-monogram" aria-hidden="true">EM</span>
              <div>
                <span class="testimonial-card__name">Edward M.</span>
                <span class="testimonial-card__role">Mine Manager</span>
              </div>
            </div>
          </article>

          <article class="card testimonial-card" data-reveal>
            <p class="testimonial-card__quote">
              &ldquo;From 3D resource modelling to statutory compliance reporting, Briva exceeded our expectations with clear, defensible engineering work.&rdquo;
            </p>
            <div class="testimonial-card__author">
              <span class="avatar-monogram" aria-hidden="true">JM</span>
              <div>
                <span class="testimonial-card__name">Joel M.</span>
                <span class="testimonial-card__role">Chief Financial Officer, AIL</span>
              </div>
            </div>
          </article>

          <article class="card testimonial-card" data-reveal>
            <p class="testimonial-card__quote">
              &ldquo;Briva’s technical due diligence and regulatory knowledge gave us the confidence to commit capital to new mining ventures.&rdquo;
            </p>
            <div class="testimonial-card__author">
              <span class="avatar-monogram" aria-hidden="true">PM</span>
              <div>
                <span class="testimonial-card__name">Pendo M.</span>
                <span class="testimonial-card__role">Human Resources, Jitegemee Holdings</span>
              </div>
            </div>
          </article>
        </div>

        <div class="clients-strip" aria-label="Selected client organizations">
          <a class="client-box" href="https://www.stamico.co.tz/" target="_blank" rel="noopener noreferrer" title="STAMICO — State Mining Corporation">
            <img loading="lazy" src="images/clients/stamicoLogo.png" alt="STAMICO — State Mining Corporation">
          </a>
          <div class="client-box"><img loading="lazy" src="images/clients/client1.png" alt="Jitegemee Holdings Co. Ltd"></div>
          <div class="client-box"><img loading="lazy" src="images/clients/client2.png" alt="Client Partner"></div>
          <div class="client-box"><img loading="lazy" src="images/clients/client3.png" alt="Shaz Ventures Co. Ltd"></div>
          <div class="client-box"><img loading="lazy" src="images/clients/client4.png" alt="Client Partner"></div>
          <div class="client-box"><img loading="lazy" src="images/clients/client5.png" alt="Client Partner"></div>
          <div class="client-box"><img loading="lazy" src="images/clients/client6.png" alt="Client Partner"></div>
        </div>
      </div>
    </section>
    {render_cta_band()}
"""

render_shell(
    "index.html",
    "Mineral Exploration, Mining Engineering & Geophysical Equipment",
    "Briva Exploration & Mining provides geological exploration, 3D resource estimation, mine planning, drilling supervision, ASM support, and geophysical scanners across East Africa.",
    "home",
    home_body,
    extra_scripts=["js/projects.js"],
    include_netlify_identity=True,
)


# ==============================================================================
# 2. about.html
# ==============================================================================
about_body = f"""
    <section class="page-hero page-hero--drill">
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>About</span>
        </nav>
        <h1>About Briva</h1>
        <p class="page-hero__lead">Mineral exploration and mining engineering across East Africa.</p>
      </div>
    </section>

    <section class="section">
      <div class="container split-layout">
        <div data-reveal>
          <span class="eyebrow">Firm Profile</span>
          <h2>Bridging Geological Discovery and Responsible Production</h2>
          <p>
            Briva Exploration &amp; Mining is a Dar es Salaam consultancy uniting field geologists, geophysicists, mining engineers, and financial analysts with over two decades of regional and international leadership.
          </p>
          <p>
            We advise international explorers, institutional partners, industrial producers, and Tanzanian Primary Mining Licence (PML) cooperatives—delivering verifiable subsurface data and practical mine designs.
          </p>
          <div class="pillar-stack mt-8">
            <div class="pillar-box">
              <h3>Vision</h3>
              <p>To be Africa’s benchmark mining and exploration solutions provider, recognized for technical innovation, sustainability, and integrity.</p>
            </div>
            <div class="pillar-box">
              <h3>Mission</h3>
              <p>Deliver end-to-end, cost-disciplined exploration and engineering services grounded in technical excellence and community stewardship.</p>
            </div>
          </div>
        </div>

        <div class="about-media-grid" data-reveal>
          <figure>
            <img loading="lazy" src="images/projects/Core drilling.jpg" alt="Diamond core drilling supervision in Tanzania">
            <figcaption>Diamond core drilling &amp; geotechnical logging</figcaption>
          </figure>
          <figure>
            <img loading="lazy" src="images/projects/Coal outcro mapping_Liweta.jpg" alt="Coal seam outcrop mapping in Liweta">
            <figcaption>Stratigraphic &amp; structural outcrop mapping</figcaption>
          </figure>
          <figure>
            <img loading="lazy" src="images/projects/Pegmatite, lithium exploration In Dodoma.jpg" alt="Lithium pegmatite exploration in Dodoma">
            <figcaption>Battery-metal pegmatite exploration, Dodoma</figcaption>
          </figure>
          <figure>
            <img loading="lazy" src="images/resouceEst1.jpeg" alt="3D geological block modelling and resource estimation">
            <figcaption>3D wireframing &amp; block resource estimation</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="section section--dark">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow eyebrow--light">Commodities</span>
          <h2>Active Across Tanzania’s Mineral Belts</h2>
          <p class="section-lead">Field-tested across Archean greenstones, zoned pegmatites, Karoo coal basins, and polymetallic corridors.</p>
        </div>
        <div class="grid grid--4">
          <div class="process-step">
            <span class="process-step__num">PRECIOUS METALS</span>
            <h3>Lode &amp; Alluvial Gold</h3>
            <p>Shear-zone mapping, channel sampling, and ASM advisory in Tabora and Morogoro.</p>
          </div>
          <div class="process-step">
            <span class="process-step__num">CRITICAL MINERALS</span>
            <h3>Lithium, Graphite &amp; Beryllium</h3>
            <p>Pegmatite and gneiss evaluation across Dodoma, Merelani, and Namtumbo.</p>
          </div>
          <div class="process-step">
            <span class="process-step__num">ENERGY MINERALS</span>
            <h3>Thermal &amp; Coking Coal</h3>
            <p>Seam correlation, cross-section modelling, and active face mapping in Liweta.</p>
          </div>
          <div class="process-step">
            <span class="process-step__num">BASE &amp; INDUSTRIAL</span>
            <h3>Cu-Zn, Dolomite &amp; Quartz</h3>
            <p>Polymetallic exploration in Mpanda alongside industrial mineral evaluations.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Governance</span>
            <h2>Operating Principles</h2>
          </div>
          <a class="btn btn--outline" href="team.html">Leadership &amp; Specialists {ICONS["arrow"]}</a>
        </div>
        <div class="grid grid--3">
          <div class="card value-card" data-reveal>
            <h3>01. Integrity</h3>
            <p>Independent scientific honesty and strict QA/QC accountability in every assay, log, and report.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>02. Technical Excellence</h3>
            <p>Rigorous geological and engineering standards enabling confident capital decisions.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>03. Applied Innovation</h3>
            <p>Modern 3D block modelling, GIS synthesis, and multi-sensor geophysics to lower discovery risk.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>04. Environmental Care</h3>
            <p>Low-impact field execution, drill-pad rehabilitation, and responsible extraction design.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>05. Collaboration</h3>
            <p>Constructive alignment across licence holders, host communities, regulators, and investors.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>06. Zero-Harm Safety</h3>
            <p>Disciplined health, ground-control, and rig-site safety protocols on every assignment.</p>
          </div>
        </div>
      </div>
    </section>
    {render_cta_band()}
"""

render_shell(
    "about.html",
    "About Briva — Governance, Commodities & Expertise",
    "Learn about Briva Exploration & Mining—our Dar es Salaam leadership, mission, governance principles, and multi-commodity track record across East Africa.",
    "about",
    about_body,
)


# ==============================================================================
# 3. services.html
# ==============================================================================
services_body = f"""
    <section class="page-hero page-hero--mpanda">
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>Services</span>
        </nav>
        <h1>Services</h1>
        <p class="page-hero__lead">Six integrated disciplines from grassroots discovery to mine design.</p>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Practice Areas</span>
          <h2>Technical &amp; Advisory Disciplines</h2>
        </div>
        <div class="grid grid--3">
          {render_service_cards()}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Methodology</span>
          <h2>Decision-Gated Asset Progression</h2>
          <p class="section-lead">Disciplined stage-gates that control capital spend while building geological confidence.</p>
        </div>
        <div class="process-grid">
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 01</span>
            <h3>Tenure &amp; Desktop</h3>
            <p>GIS compilation, structural interpretation, and statutory licence verification.</p>
          </div>
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 02</span>
            <h3>Field Exploration</h3>
            <p>Outcrop mapping, geochemical grids, trenching, and ground geophysics.</p>
          </div>
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 03</span>
            <h3>Drilling Oversight</h3>
            <p>DD/RC rig supervision, oriented core logging, RQD, and QA/QC dispatch.</p>
          </div>
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 04</span>
            <h3>3D Model &amp; Plan</h3>
            <p>Wireframing, block estimation, pit/underground design, and scheduling.</p>
          </div>
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 05</span>
            <h3>Compliance &amp; JV</h3>
            <p>Statutory reporting, DCF valuation, and structured investor partnerships.</p>
          </div>
        </div>
      </div>
    </section>
    {render_cta_band()}
"""

render_shell(
    "services.html",
    "Services — Exploration, Resource Modelling & Mine Engineering",
    "Explore Briva's six core mining consulting disciplines: geological exploration, 3D resource estimation, mine planning, drilling supervision, ASM support, and M&A advisory.",
    "services",
    services_body,
)


# ==============================================================================
# 4. service-single.html
# ==============================================================================
s0 = SERVICES[0]
s0_nav = "".join(
    f'<li><a class="sidebar-nav__link{" is-active" if i == 0 else ""}" href="service-single.html?service={s["slug"]}">'
    f'<span>{s["shortTitle"]}</span><span class="sidebar-nav__num">{s["num"]}</span></a></li>'
    for i, s in enumerate(SERVICES)
)
s0_paras = "".join(f"<p>{p}</p>" for p in s0["overview"])
s0_deliv = "".join(f'<div class="deliverable-item">{ICONS["check"]}<span>{d}</span></div>' for d in s0["deliverables"])
s0_steps = "".join(
    f'<div class="process-step"><span class="process-step__num">STEP {m["step"]}</span><h3>{m["title"]}</h3><p>{m["text"]}</p></div>'
    for m in s0["methodology"]
)
s0_faqs = "".join(
    f'<details class="faq-item"{" open" if i == 0 else ""}><summary>{f["q"]}</summary><div class="faq-item__body"><p>{f["a"]}</p></div></details>'
    for i, f in enumerate(s0["faqs"])
)

service_single_body = f"""
    <section class="page-hero page-hero--mpanda">
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <a href="services.html">Services</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span id="service-breadcrumb-current">{s0["shortTitle"]}</span>
        </nav>
        <h1 id="service-hero-title">{s0["title"]}</h1>
        <p class="page-hero__lead" id="service-hero-lead">{s0["subtitle"]}</p>
      </div>
    </section>

    <section class="section">
      <div class="container sidebar-layout">
        <aside class="sidebar-sticky">
          <nav class="sidebar-nav" aria-label="All consulting disciplines">
            <div class="sidebar-nav__head">Core Disciplines</div>
            <ul id="service-sidebar-nav">{s0_nav}</ul>
          </nav>

          <div class="sidebar-cta">
            <h3>Scope Your Programme</h3>
            <p>Request a technical proposal, mobilization schedule, or fee estimate from our Dar es Salaam team.</p>
            <a id="service-sidebar-cta-btn" class="btn btn--primary w-full" href="contact.html?service={s0["slug"]}">Request Proposal</a>
          </div>
        </aside>

        <div id="service-detail-content">
          <img class="detail-hero-img" src="{s0["image"]}" alt="{s0["title"]}">
          <span class="eyebrow">Discipline {s0["num"]}</span>
          <h2>Overview &amp; Technical Scope</h2>
          <div class="prose-overview">{s0_paras}</div>
          <h3>Key Technical Deliverables</h3>
          <div class="deliverables-grid mb-10">{s0_deliv}</div>
          <h3>Execution Methodology</h3>
          <div class="grid grid--3 mb-10">{s0_steps}</div>
          <h3>Frequently Asked Questions</h3>
          <div class="faq-list">{s0_faqs}</div>
        </div>
      </div>
    </section>
    {render_cta_band()}
"""

render_shell(
    "service-single.html",
    "Geological & Exploration Services",
    "Technical deliverables, methodology, and FAQs for Briva's geological exploration, 3D resource estimation, mine planning, drilling supervision, ASM, and M&A services.",
    "services",
    service_single_body,
    extra_scripts=["js/services.js"],
)


# ==============================================================================
# 5. projects.html
# ==============================================================================
projects_body = f"""
    <section class="page-hero page-hero--lithium">
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>Projects</span>
        </nav>
        <h1>Field Projects</h1>
        <p class="page-hero__lead">Fourteen exploration, mapping, and mining mandates across Tanzania.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="filter-header">
          <div class="filter-bar" role="toolbar" aria-label="Filter projects by discipline">
            <button type="button" class="filter-btn is-active" data-project-filter="all" aria-pressed="true">All Projects</button>
            <button type="button" class="filter-btn" data-project-filter="exploration" aria-pressed="false">Exploration</button>
            <button type="button" class="filter-btn" data-project-filter="mining" aria-pressed="false">Mining &amp; QA/QC</button>
            <button type="button" class="filter-btn" data-project-filter="mapping" aria-pressed="false">Geological Mapping</button>
          </div>
          <span id="projects-count" class="projects-count">14 projects</span>
        </div>

        <div id="projects-catalog-grid" class="grid grid--3"></div>
        <noscript>
          <p class="mt-6">Enable JavaScript to filter our interactive project catalog, or email <a href="mailto:info@briva.co.tz">info@briva.co.tz</a> for our credentials dossier.</p>
        </noscript>
      </div>
    </section>
    {render_cta_band(
        heading="Evaluate a Mineral Licence or Deposit",
        sub="Engage our field geologists for mapping, geochemical sampling, core supervision, or independent due diligence."
    )}
"""

render_shell(
    "projects.html",
    "Field Projects — Lithium, Gold, Coal, Graphite & Cu-Zn",
    "Explore Briva's portfolio of 14 mineral exploration, geological mapping, diamond core drilling, and mining projects across Tanzania.",
    "projects",
    projects_body,
    extra_scripts=["js/projects.js"],
)


# ==============================================================================
# 6. projects-single.html
# ==============================================================================
projects_single_body = f"""
    <div class="subnav-bar">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <a href="projects.html">Projects</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span id="project-breadcrumb-current">Project Case Study</span>
        </nav>
      </div>
    </div>

    <section class="section">
      <div class="container" id="project-detail-root">
        <p>Loading project case study...</p>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Portfolio</span>
            <h2>Related Mandates</h2>
          </div>
          <a class="btn btn--outline" href="projects.html">All 14 Projects {ICONS["arrow"]}</a>
        </div>
        <div id="related-projects-grid" class="grid grid--3"></div>
      </div>
    </section>
    {render_cta_band()}
"""

render_shell(
    "projects-single.html",
    "Project Case Study",
    "Field project scope, location, area, and geological outcomes delivered by Briva Exploration & Mining in Tanzania.",
    "projects",
    projects_single_body,
    extra_scripts=["js/projects.js"],
)


# ==============================================================================
# 7. equipment.html (Compact Horizontal Desktop Instrument Rows)
# ==============================================================================
equipment_body = f"""
    <section class="page-hero page-hero--rig">
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>Equipment</span>
        </nav>
        <h1>Field Equipment</h1>
        <p class="page-hero__lead">Certified geophysical scanners and target pinpointers — sales and rental.</p>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Instrument Catalog</span>
            <h2>Subsurface Detection Systems</h2>
          </div>
          <a class="btn btn--outline btn--sm" href="contact.html?type=equipment">Request Proforma Invoice {ICONS["arrow"]}</a>
        </div>

        <div class="instrument-list">
          <!-- Instrument 01: Mega Scan Pro -->
          <article class="card card--interactive instrument-card" data-reveal>
            <a class="instrument-card__media" href="equipment-megascan.html" aria-label="View Mega Scan Pro specifications">
              <img src="images/equipment/mega-scan-pro.jpg" alt="Mega Scan Pro Geophysical Detection System" width="156" height="156">
            </a>
            <div class="instrument-card__body">
              <div class="instrument-card__meta">
                <span class="instrument-badge">Multi-System Scanner</span>
                <span class="instrument-avail">Purchase or Supervised Rental</span>
              </div>
              <h3 class="instrument-card__title"><a href="equipment-megascan.html">Mega Scan Pro</a></h3>
              <p class="instrument-card__desc">
                Six-mode geophysical ground scanner integrating Long-Range Locator (LRL), Magnetometer, Ionic/Bionic sensing, and V.S.T vertical probe telemetry.
              </p>
              <div class="instrument-card__specs">
                <div>
                  <span class="instrument-spec__label">Max Depth</span>
                  <span class="instrument-spec__val">Up to 50 m</span>
                </div>
                <div>
                  <span class="instrument-spec__label">Scan Range</span>
                  <span class="instrument-spec__val">Up to 3,000 m</span>
                </div>
                <div>
                  <span class="instrument-spec__label">Architecture</span>
                  <span class="instrument-spec__val">6 Search Modes</span>
                </div>
                <div>
                  <span class="instrument-spec__label">Support</span>
                  <span class="instrument-spec__val">1-Yr Warranty</span>
                </div>
              </div>
            </div>
            <div class="instrument-card__aside">
              <div>
                <span class="price-label">Standard Kit</span>
                <span class="price-amount"><small>TZS</small>20,000,000</span>
              </div>
              <div class="instrument-card__actions">
                <a class="btn btn--primary btn--sm w-full" href="equipment-megascan.html">Specifications {ICONS["arrow"]}</a>
                <a class="btn btn--outline btn--sm w-full" href="contact.html?product=megascan&amp;type=buy">Request Quote</a>
              </div>
            </div>
          </article>

          <!-- Instrument 02: Gold Pin Pointer -->
          <article class="card card--interactive instrument-card" data-reveal>
            <a class="instrument-card__media" href="equipment-pinpointer.html" aria-label="View Gold Pin Pointer specifications">
              <img src="images/equipment/gold-pin-pointer.jpg" alt="Gold Pin Pointer Precision Handheld Detector" width="156" height="156">
            </a>
            <div class="instrument-card__body">
              <div class="instrument-card__meta">
                <span class="instrument-badge">Handheld Probe</span>
                <span class="instrument-avail">In Stock &middot; Single &amp; Bulk Orders</span>
              </div>
              <h3 class="instrument-card__title"><a href="equipment-pinpointer.html">Gold Pin Pointer</a></h3>
              <p class="instrument-card__desc">
                Submersible 360-degree precision pinpointing probe built to isolate fine gold nuggets and mineralized veinlets in trenches, shafts, and crushed ore.
              </p>
              <div class="instrument-card__specs">
                <div>
                  <span class="instrument-spec__label">Frequency</span>
                  <span class="instrument-spec__val">11.5 kHz Tuned</span>
                </div>
                <div>
                  <span class="instrument-spec__label">Protection</span>
                  <span class="instrument-spec__val">IP68 (3 m)</span>
                </div>
                <div>
                  <span class="instrument-spec__label">Detection</span>
                  <span class="instrument-spec__val">360&deg; + Tip</span>
                </div>
                <div>
                  <span class="instrument-spec__label">Support</span>
                  <span class="instrument-spec__val">1-Yr Warranty</span>
                </div>
              </div>
            </div>
            <div class="instrument-card__aside">
              <div>
                <span class="price-label">Unit Price</span>
                <span class="price-amount"><small>TZS</small>500,000</span>
              </div>
              <div class="instrument-card__actions">
                <a class="btn btn--primary btn--sm w-full" href="equipment-pinpointer.html">Specifications {ICONS["arrow"]}</a>
                <a class="btn btn--outline btn--sm w-full" href="contact.html?product=pinpointer&amp;type=buy">Request Quote</a>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Supply Assurance</span>
          <h2>Included With Every Instrument</h2>
        </div>

        <div class="assurance-strip">
          <div class="assurance-item" data-reveal>
            <h3>1-Year Local Warranty</h3>
            <p>Manufacturer coverage supported directly through our Dar es Salaam office.</p>
          </div>
          <div class="assurance-item" data-reveal>
            <h3>Geologist Field Training</h3>
            <p>Hands-on ground balance, calibration, and anomaly interpretation guidance.</p>
          </div>
          <div class="assurance-item" data-reveal>
            <h3>Nationwide Dispatch</h3>
            <p>Tracked delivery to Dodoma, Mwanza, Geita, Tabora, Mbeya, and Morogoro.</p>
          </div>
          <div class="assurance-item" data-reveal>
            <h3>Purchase or Rental</h3>
            <p>Outright acquisition or supervised short-term field deployment options.</p>
          </div>
        </div>
      </div>
    </section>
    {render_cta_band(
        heading="Request an Equipment Quotation or Demo",
        sub="Confirm stock availability, book an in-office demonstration, or request a proforma invoice.",
        primary_label="Contact Equipment Desk",
        primary_href="contact.html?type=equipment"
    )}
"""

render_shell(
    "equipment.html",
    "Field Equipment — Mega Scan Pro & Gold Pin Pointer",
    "Certified geophysical detection systems and handheld gold pinpointers in Tanzania, with technical specifications, TZS pricing, operator training, and 1-year warranty.",
    "equipment",
    equipment_body,
)


# ==============================================================================
# 8. equipment-megascan.html
# ==============================================================================
megascan_body = f"""
    <div class="subnav-bar">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <a href="equipment.html">Equipment</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>Mega Scan Pro</span>
        </nav>
      </div>
    </div>

    <section class="section">
      <div class="container product-sheet">
        <div class="product-gallery">
          <div class="product-gallery__stage" data-lightbox="images/equipment/mega-scan-pro.jpg" role="button" tabindex="0" aria-label="Enlarge Mega Scan Pro studio image">
            <img src="images/equipment/mega-scan-pro.jpg" alt="Mega Scan Pro Geophysical Detection System">
          </div>
        </div>

        <div>
          <span class="eyebrow">Multi-System Geophysical Scanner</span>
          <h1>Mega Scan Pro</h1>
          <p class="section-lead">
            Six-system geophysical locator engineered for deep metallic mineralization, gold-bearing structures, and subsurface cavity detection.
          </p>

          <div class="product-summary__price-box">
            <div>
              <span class="price-label">Standard Kit Price</span>
              <div class="product-summary__price"><small>TZS</small>20,000,000</div>
            </div>
            <span class="instrument-badge">1-Year Warranty &amp; Training</span>
          </div>

          <div class="product-summary__actions">
            <a class="btn btn--primary" href="contact.html?product=megascan&amp;type=buy">Request Purchase Quote {ICONS["arrow"]}</a>
            <a class="btn btn--outline" href="contact.html?product=megascan&amp;type=rent">Enquire About Rental</a>
          </div>

          <a class="manual-download" href="downloads/Mega Scan Pro EN.pdf" target="_blank" rel="noopener noreferrer">
            <span class="check-item">{ICONS["file"]} <span>Official Manufacturer Manual (PDF)</span></span>
            <span class="link-arrow">Download {ICONS["arrow"]}</span>
          </a>

          <div data-tabs>
            <div class="tabs__nav" role="tablist" aria-label="Mega Scan Pro details">
              <button type="button" class="tabs__btn" role="tab" id="tab-ms-systems" aria-selected="true" aria-controls="panel-ms-systems">Detection Systems</button>
              <button type="button" class="tabs__btn" role="tab" id="tab-ms-kit" aria-selected="false" aria-controls="panel-ms-kit" tabindex="-1">Kit Contents</button>
            </div>

            <div class="tabs__panel" id="panel-ms-systems" role="tabpanel" aria-labelledby="tab-ms-systems">
              <div class="deliverables-grid">
                <div class="deliverable-item">{ICONS["check"]}<span>Long-Range Locator (LRL) with mineral frequency tuning</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Magnetometer &amp; V.S.T vertical signal transceiver</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Ionic &amp; Bionic scan modes for metallic &amp; void anomalies</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>5-inch TFT colour display with GPS coordinate logging</span></div>
              </div>
            </div>

            <div class="tabs__panel" id="panel-ms-kit" role="tabpanel" aria-labelledby="tab-ms-kit" hidden>
              <div class="deliverables-grid">
                <div class="deliverable-item">{ICONS["check"]}<span>Mega Scan Pro control unit (5&Prime; TFT display)</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>I.M.T.U Intelligent Multi Transceiver Unit</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>V.S.T High-Sensitivity Vertical Probe</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Directional telescopic search antennas</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Lithium-ion power pack, charger &amp; headphones</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Shockproof ABS transport case &amp; documentation</span></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Engineering Data</span>
            <h2>Technical Specifications</h2>
          </div>
          <a class="link-arrow" href="equipment.html">&larr; Back to Field Equipment</a>
        </div>

        <div class="spec-table-wrap">
          <table class="spec-table">
            <tbody>
              <tr><th scope="row">Microprocessor</th><td>ARM 168 MHz Architecture</td></tr>
              <tr><th scope="row">System Memory</th><td>512 KB Integrated Flash</td></tr>
              <tr><th scope="row">Display</th><td>5.0-inch TFT High-Brightness Colour LCD</td></tr>
              <tr><th scope="row">Maximum Detection Depth</th><td>Up to 50 Metres (target &amp; ground matrix dependent)</td></tr>
              <tr><th scope="row">Horizontal Scan Range</th><td>Up to 3,000 Metres (Long-Range Locator mode)</td></tr>
              <tr><th scope="row">Detection Modes</th><td>6 Systems (Auto LRL, Manual LRL, Ionic, Bionic, Magnetometer, V.S.T)</td></tr>
              <tr><th scope="row">Battery Runtime</th><td>Up to 15 Hours continuous operation</td></tr>
              <tr><th scope="row">Transport Kit Weight</th><td>6.3 kg (in sealed ABS hard case)</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
    {render_cta_band(
        heading="Acquire or Rent the Mega Scan Pro",
        sub="Contact our Dar es Salaam desk for proforma invoicing, rental terms, and operator training.",
        primary_label="Request Formal Quote",
        primary_href="contact.html?product=megascan&type=buy"
    )}
"""

render_shell(
    "equipment-megascan.html",
    "Mega Scan Pro — Specifications & Price",
    "Technical specifications, kit contents, manual download, and TZS pricing for the Mega Scan Pro geophysical scanner supplied by Briva in Tanzania.",
    "equipment",
    megascan_body,
)


# ==============================================================================
# 9. equipment-pinpointer.html
# ==============================================================================
pinpointer_body = f"""
    <div class="subnav-bar">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <a href="equipment.html">Equipment</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>Gold Pin Pointer</span>
        </nav>
      </div>
    </div>

    <section class="section">
      <div class="container product-sheet">
        <div class="product-gallery">
          <div class="product-gallery__stage" data-lightbox="images/equipment/gold-pin-pointer.jpg" role="button" tabindex="0" aria-label="Enlarge Gold Pin Pointer studio image">
            <img src="images/equipment/gold-pin-pointer.jpg" alt="Gold Pin Pointer Waterproof Handheld Metal Detector">
          </div>
        </div>

        <div>
          <span class="eyebrow">Precision Target Pinpointer</span>
          <h1>Gold Pin Pointer</h1>
          <p class="section-lead">
            IP68 waterproof handheld probe engineered for rapid isolation of fine gold nuggets and mineralized veinlets in pits, shafts, and alluvial wash.
          </p>

          <div class="product-summary__price-box">
            <div>
              <span class="price-label">Unit Price</span>
              <div class="product-summary__price"><small>TZS</small>500,000</div>
            </div>
            <span class="instrument-badge">IP68 Waterproof &middot; In Stock</span>
          </div>

          <div class="product-summary__actions">
            <a class="btn btn--primary" href="contact.html?product=pinpointer&amp;type=buy">Request Purchase Quote {ICONS["arrow"]}</a>
            <a class="btn btn--outline" href="contact.html?product=pinpointer&amp;type=rent">Bulk / Cooperative Enquiry</a>
          </div>

          <div data-tabs>
            <div class="tabs__nav" role="tablist" aria-label="Gold Pin Pointer details">
              <button type="button" class="tabs__btn" role="tab" id="tab-pp-features" aria-selected="true" aria-controls="panel-pp-features">Field Capabilities</button>
              <button type="button" class="tabs__btn" role="tab" id="tab-pp-kit" aria-selected="false" aria-controls="panel-pp-kit" tabindex="-1">Package Contents</button>
            </div>

            <div class="tabs__panel" id="panel-pp-features" role="tabpanel" aria-labelledby="tab-pp-features">
              <div class="deliverables-grid">
                <div class="deliverable-item">{ICONS["check"]}<span>360&deg; cylindrical side-scan field plus precision tip detection</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Proportional audio &amp; haptic vibration target proximity pulse</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>One-touch fast retune for mineralized host rock</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Integrated LED worklight for shafts and deep trenches</span></div>
              </div>
            </div>

            <div class="tabs__panel" id="panel-pp-kit" role="tabpanel" aria-labelledby="tab-pp-kit" hidden>
              <div class="deliverables-grid">
                <div class="deliverable-item">{ICONS["check"]}<span>Gold Pin Pointer sealed handheld probe</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Woven duty belt holster</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Coiled anti-loss security lanyard</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>9V battery &amp; operator quick-start guide</span></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Engineering Data</span>
            <h2>Technical Specifications</h2>
          </div>
          <a class="link-arrow" href="equipment.html">&larr; Back to Field Equipment</a>
        </div>

        <div class="spec-table-wrap">
          <table class="spec-table">
            <tbody>
              <tr><th scope="row">Operating Frequency</th><td>11.5 kHz High-Sensitivity Circuitry</td></tr>
              <tr><th scope="row">Ingress Protection</th><td>IP68 Submersible up to 3 Metres (10 ft)</td></tr>
              <tr><th scope="row">Sensitivity Levels</th><td>3 Selectable Tiers + One-Touch Fast Retune</td></tr>
              <tr><th scope="row">Target Indicators</th><td>Proportional Audio + Haptic Vibration + LED</td></tr>
              <tr><th scope="row">Operating Temperature</th><td>-20&deg;C to +54&deg;C</td></tr>
              <tr><th scope="row">Power Supply</th><td>Single 9V Battery (up to 30 hours continuous use)</td></tr>
              <tr><th scope="row">Dimensions &amp; Weight</th><td>24 cm length &middot; 200 g (with battery)</td></tr>
              <tr><th scope="row">Warranty</th><td>1-Year Briva Local Warranty</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
    {render_cta_band(
        heading="Equip Your Crew With the Gold Pin Pointer",
        sub="Single units and cooperative bulk orders ready for dispatch across Tanzania.",
        primary_label="Order Gold Pin Pointer",
        primary_href="contact.html?product=pinpointer&type=buy"
    )}
"""

render_shell(
    "equipment-pinpointer.html",
    "Gold Pin Pointer — Specifications & Price",
    "Technical specifications, package contents, and TZS 500,000 pricing for the IP68 waterproof Gold Pin Pointer supplied by Briva in Tanzania.",
    "equipment",
    pinpointer_body,
)


# ==============================================================================
# 10. team.html (Symmetrical 2-Tier Executive & Practice Architecture)
# ==============================================================================
team_body = f"""
    <section class="page-hero page-hero--drill">
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>Team</span>
        </nav>
        <h1>Leadership &amp; Specialists</h1>
        <p class="page-hero__lead">Senior geologists, geophysicists, mining engineers, and corporate advisors.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Governance</span>
          <h2>Board &amp; Executive Leadership</h2>
        </div>

        <div class="grid grid--2 mb-10">
          <article class="card profile-card" data-reveal>
            <div class="profile-card__media">
              <img loading="lazy" src="images/team/alex-bashire.jpg" alt="Alex S. Bashire — Chief Executive Officer" width="88" height="88">
            </div>
            <div>
              <div class="profile-card__meta">
                <span class="profile-card__role">Chief Executive Officer</span>
                <span class="profile-card__tag">23+ Yrs Experience</span>
              </div>
              <h3 class="profile-card__name">Alex S. Bashire</h3>
              <p class="profile-card__bio">
                Over two decades leading mineral exploration, tenure strategy, stakeholder alignment, and mining project execution across East Africa.
              </p>
            </div>
          </article>

          <article class="card profile-card" data-reveal>
            <div class="profile-card__media profile-card__media--monogram" aria-hidden="true">KR</div>
            <div>
              <div class="profile-card__meta">
                <span class="profile-card__role">Non-Executive Director</span>
                <span class="profile-card__tag">25+ Yrs Experience</span>
              </div>
              <h3 class="profile-card__name">K. Sridhar Reddy</h3>
              <p class="profile-card__bio">
                International mining executive directing large-scale mine operations, capital project delivery, and board governance across Africa and Asia.
              </p>
            </div>
          </article>
        </div>

        <div class="section-head mt-10">
          <span class="eyebrow">Practice Leads</span>
          <h2>Senior Consultants &amp; Advisors</h2>
        </div>

        <div class="grid grid--2">
          <article class="card profile-card" data-reveal>
            <div class="profile-card__media">
              <img loading="lazy" src="images/team/kolipaka-venu.jpg" alt="Dr. Kolipaka Venu — Geophysics Consultant" width="88" height="88">
            </div>
            <div>
              <div class="profile-card__meta">
                <span class="profile-card__role">Geophysics Consultant</span>
                <span class="profile-card__tag">PhD &middot; 12+ Yrs</span>
              </div>
              <h3 class="profile-card__name">Dr. Kolipaka Venu</h3>
              <p class="profile-card__bio">
                Designs and interprets ground and airborne geophysical surveys for subsurface target generation across Africa and India.
              </p>
            </div>
          </article>

          <article class="card profile-card" data-reveal>
            <div class="profile-card__media">
              <img loading="lazy" src="images/team/srirama-yellapragada.jpg" alt="Srirama Gopal Yellapragada — Mining Engineering Consultant" width="88" height="88">
            </div>
            <div>
              <div class="profile-card__meta">
                <span class="profile-card__role">Engineering Consultant</span>
                <span class="profile-card__tag">Mine Operations</span>
              </div>
              <h3 class="profile-card__name">Srirama Gopal Yellapragada</h3>
              <p class="profile-card__bio">
                Experienced Mines Manager specializing in open-pit engineering, fleet optimization, production scheduling, and site safety.
              </p>
            </div>
          </article>

          <article class="card profile-card" data-reveal>
            <div class="profile-card__media">
              <img loading="lazy" src="images/team/jackline-kidendei.jpg" alt="Jackline Sayi Kidendei — Geologist &amp; Commercial Lead" width="88" height="88">
            </div>
            <div>
              <div class="profile-card__meta">
                <span class="profile-card__role">Geologist &amp; Commercial Lead</span>
                <span class="profile-card__tag">Exploration &amp; JVs</span>
              </div>
              <h3 class="profile-card__name">Jackline Sayi Kidendei</h3>
              <p class="profile-card__bio">
                Combines field exploration geology with client advisory and commercial partnership development across Tanzania’s mineral sector.
              </p>
              <div class="profile-card__foot">
                <a class="link-arrow" href="https://www.linkedin.com/in/jackline-kidendei-8a8789371" target="_blank" rel="noopener noreferrer">
                  {ICONS["linkedin"]} LinkedIn Profile
                </a>
              </div>
            </div>
          </article>

          <article class="card profile-card" data-reveal>
            <div class="profile-card__media">
              <img loading="lazy" src="images/team/vashty-nyembera.jpg" alt="Vashty J. Nyembera — HR &amp; Finance Consultant" width="88" height="88">
            </div>
            <div>
              <div class="profile-card__meta">
                <span class="profile-card__role">HR &amp; Finance Consultant</span>
                <span class="profile-card__tag">Corporate Controls</span>
              </div>
              <h3 class="profile-card__name">Vashty J. Nyembera</h3>
              <p class="profile-card__bio">
                Oversees project financial controls, operational budgeting, field workforce compliance, and human capital administration.
              </p>
            </div>
          </article>
        </div>
      </div>
    </section>
    {render_cta_band(
        heading="Engage Our Technical Specialists",
        sub="Connect directly with our geology, geophysics, and mine engineering leads in Dar es Salaam."
    )}
"""

render_shell(
    "team.html",
    "Leadership & Specialists",
    "Meet Briva's executive directors and specialist consultants in geology, geophysics, open-pit mine engineering, and corporate governance.",
    "team",
    team_body,
)


# ==============================================================================
# 11. contact.html (Formspree Preserved + Smart Query Prefill)
# ==============================================================================
contact_body = f"""
    <section class="page-hero page-hero--coal">
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>Contact</span>
        </nav>
        <h1>Contact</h1>
        <p class="page-hero__lead">Technical consultations, project scoping, and equipment quotations in Dar es Salaam.</p>
      </div>
    </section>

    <section class="section">
      <div class="container contact-layout">
        <div>
          <span class="eyebrow">Direct Channels</span>
          <h2>Dar es Salaam Office</h2>
          <p class="mb-6">Available six days a week for executive consultations and rapid field mobilization across Tanzania.</p>

          <div class="contact-info-list">
            <div class="card contact-info-card">
              <span class="contact-info-card__icon">{ICONS["pin"]}</span>
              <div>
                <h3>Address</h3>
                <p>P.O. Box 11259, Dar es Salaam, Tanzania</p>
              </div>
            </div>

            <div class="card contact-info-card">
              <span class="contact-info-card__icon">{ICONS["phone"]}</span>
              <div>
                <h3>Telephone</h3>
                <p><a class="tabular" href="tel:+255767413950">+255 767 413 950</a></p>
              </div>
            </div>

            <div class="card contact-info-card">
              <span class="contact-info-card__icon">{ICONS["mail"]}</span>
              <div>
                <h3>Email</h3>
                <p><a href="mailto:info@briva.co.tz">info@briva.co.tz</a></p>
              </div>
            </div>

            <div class="card contact-info-card">
              <span class="contact-info-card__icon">{ICONS["clock"]}</span>
              <div>
                <h3>Hours</h3>
                <p class="tabular">Mon – Fri: 10:00 – 16:00 &middot; Sat: 12:00 – 15:00</p>
              </div>
            </div>
          </div>

          <div class="map-frame">
            <iframe
              title="Briva Exploration &amp; Mining — Dar es Salaam Location Map"
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d126743.59347895396!2d39.2083!3d-6.7924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x185c4bae169bd6f1%3A0x940f6b26a086a1dd!2sDar%20es%20Salaam%2C%20Tanzania!5e0!3m2!1sen!2sus!4v1633072800000!5m2!1sen!2sus"
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              allowfullscreen></iframe>
          </div>
        </div>

        <div class="card contact-form-card">
          <span class="eyebrow">Enquiry Desk</span>
          <h2 class="mb-6">Send an Enquiry</h2>

          <div id="contact-success" class="form-alert form-alert--success" role="status" tabindex="-1" hidden>
            Thank you—your enquiry has been received by Briva Exploration &amp; Mining. Our Dar es Salaam team will respond shortly.
          </div>
          <div id="contact-error" class="form-alert form-alert--error" role="alert" hidden></div>

          <form id="contact-form" action="https://formspree.io/f/xdkvjwqd" method="POST">
            <input type="text" name="_gotcha" class="sr-only" tabindex="-1" autocomplete="off" aria-hidden="true">

            <div class="form-grid">
              <div>
                <label class="form-label" for="name">Full Name *</label>
                <input class="form-control" type="text" id="name" name="name" required autocomplete="name" placeholder="e.g. John Mwangi">
              </div>

              <div>
                <label class="form-label" for="email">Email Address *</label>
                <input class="form-control" type="email" id="email" name="email" required autocomplete="email" placeholder="name@company.com">
              </div>

              <div>
                <label class="form-label" for="phone">Phone / WhatsApp</label>
                <input class="form-control" type="tel" id="phone" name="phone" autocomplete="tel" placeholder="+255 ...">
              </div>

              <div>
                <label class="form-label" for="subject">Category *</label>
                <select class="form-control" id="subject" name="subject" required>
                  <option value="Geological &amp; Exploration Consulting">Geological &amp; Exploration Consulting</option>
                  <option value="Resource Estimation &amp; Mine Planning">Resource Estimation &amp; Mine Planning</option>
                  <option value="Drilling Supervision">Drilling Supervision</option>
                  <option value="ASM Support / M&amp;A Advisory">ASM Support / M&amp;A Advisory</option>
                  <option value="Equipment Purchase Quote">Equipment Purchase Quote</option>
                  <option value="Equipment Rental Enquiry">Equipment Rental Enquiry</option>
                  <option value="General Enquiry">General Enquiry</option>
                </select>
              </div>

              <div class="form-field--full">
                <label class="form-label" for="message">Brief Scope or Requirement *</label>
                <textarea class="form-control" id="message" name="message" required placeholder="Commodity, region/licence status, or instrument quantity..."></textarea>
              </div>

              <div class="form-field--full">
                <button id="contact-submit" type="submit" class="btn btn--primary btn--lg w-full">
                  Send Enquiry {ICONS["arrow"]}
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </section>
"""

render_shell(
    "contact.html",
    "Contact — Dar es Salaam Consulting & Equipment Desk",
    "Contact Briva Exploration & Mining in Dar es Salaam (+255 767 413 950, info@briva.co.tz) for geological consulting, drilling supervision, resource estimation, or geophysical equipment quotes.",
    "contact",
    contact_body,
)


# ==============================================================================
# 12. thank-you.html
# ==============================================================================
thank_you_body = f"""
    <section class="section section--subtle">
      <div class="container">
        <div class="card status-page">
          <span class="eyebrow">Submission Confirmed</span>
          <h1>Enquiry Received</h1>
          <p>
            Thank you for contacting Briva. Our Dar es Salaam team will respond promptly, or you may call <a href="tel:+255767413950"><strong>+255 767 413 950</strong></a> for immediate assistance.
          </p>
          <div class="status-page__actions">
            <a class="btn btn--primary" href="index.html">Return Home</a>
            <a class="btn btn--outline" href="projects.html">Field Projects</a>
            <a class="btn btn--outline" href="equipment.html">Field Equipment</a>
          </div>
        </div>
      </div>
    </section>
"""

render_shell(
    "thank-you.html",
    "Enquiry Received",
    "Thank you for contacting Briva Exploration & Mining. Our Dar es Salaam team will respond promptly.",
    "",
    thank_you_body,
)


# ==============================================================================
# 13. 404.html
# ==============================================================================
error_404_body = f"""
    <section class="section section--subtle">
      <div class="container">
        <div class="card status-page">
          <span class="status-page__code tabular">404</span>
          <h1>Page Not Found</h1>
          <p>
            The requested page has moved or does not exist. Use the links below to navigate Briva’s services, field projects, or equipment catalog.
          </p>
          <div class="status-page__actions">
            <a class="btn btn--primary" href="index.html">Back to Home</a>
            <a class="btn btn--outline" href="services.html">Services</a>
            <a class="btn btn--outline" href="contact.html">Contact</a>
          </div>
        </div>
      </div>
    </section>
"""

render_shell(
    "404.html",
    "404 — Page Not Found",
    "The requested page could not be found on the Briva Exploration & Mining website.",
    "",
    error_404_body,
)
