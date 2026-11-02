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
          Multidisciplinary mineral exploration, 3D resource modelling, mine planning, drilling supervision, and certified geophysical equipment serving East Africa.
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
          <li><a href="service-single.html?service=ma-advisory">M&amp;A and Joint Ventures</a></li>
        </ul>
      </div>

      <div>
        <h3 class="site-footer__heading">Company</h3>
        <ul class="site-footer__links">
          <li><a href="about.html">About Briva</a></li>
          <li><a href="projects.html">Field Projects</a></li>
          <li><a href="equipment.html">Equipment Catalog</a></li>
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


def render_cta_band(heading="Planning an Exploration Programme or Resource Study?",
                    sub="Speak directly with our senior geologists and mining engineers in Dar es Salaam for technical scoping, licence due diligence, or equipment quotations.",
                    primary_label="Schedule a Consultation",
                    primary_href="contact.html"):
    return f"""
    <section class="cta-band">
      <div class="container cta-band__inner">
        <div>
          <span class="eyebrow eyebrow--light">Advisory &amp; Field Operations</span>
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
          <span class="eyebrow eyebrow--light">Mineral Exploration &amp; Mining Consultancy &middot; Tanzania</span>
          <h1>Technical Precision Across the Mining Value Chain</h1>
          <p class="home-hero__lead">
            Briva partners with mining houses, mineral investors, and cooperatives across East Africa—delivering geological exploration, 3D resource modelling, mine engineering, drilling supervision, and certified geophysical detection systems.
          </p>
          <div class="home-hero__actions">
            <a class="btn btn--primary btn--lg" href="services.html">Explore Our Services {ICONS["arrow"]}</a>
            <a class="btn btn--outline-light btn--lg" href="projects.html">View Field Portfolio</a>
          </div>
        </div>
      </div>
      <div class="capability-strip">
        <div class="container capability-strip__grid">
          <div class="capability-item">
            <span class="capability-item__val tabular">6 Core Disciplines</span>
            <span class="capability-item__label">Grassroots Exploration to M&amp;A Advisory</span>
          </div>
          <div class="capability-item">
            <span class="capability-item__val tabular">14+ Field Programmes</span>
            <span class="capability-item__label">Executed Across Key Tanzanian Mineral Belts</span>
          </div>
          <div class="capability-item">
            <span class="capability-item__val">Multi-Commodity</span>
            <span class="capability-item__label">Gold, Lithium, Graphite, Coal &amp; Base Metals</span>
          </div>
          <div class="capability-item">
            <span class="capability-item__val">Field Instrumentation</span>
            <span class="capability-item__label">Geophysical Scanners — Sales &amp; Field Rental</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split-layout">
        <div data-reveal>
          <span class="eyebrow">About Briva</span>
          <h2>End-to-End Geological &amp; Mining Solutions Built on Field Rigour</h2>
          <p>
            Briva is a multidisciplinary mining and mineral exploration firm headquartered in Dar es Salaam. Backed by seasoned geologists, geophysicists, mining engineers, and financial analysts with over two decades of regional and international leadership, we de-risk mineral assets at every stage of development.
          </p>
          <p>
            Whether advancing a greenfield lithium pegmatite licence in Dodoma, supervising diamond core rigs, or optimizing an active coal face, our work is anchored in verifiable field data and strict regulatory compliance.
          </p>
          <div class="check-grid">
            <div class="check-item">{ICONS["check"]} <span>Local &amp; international geological leadership</span></div>
            <div class="check-item">{ICONS["check"]} <span>QA/QC-governed sampling &amp; core logging</span></div>
            <div class="check-item">{ICONS["check"]} <span>Practical open-pit &amp; underground engineering</span></div>
            <div class="check-item">{ICONS["check"]} <span>Environmental &amp; safety-first site governance</span></div>
          </div>
          <a class="btn btn--outline" href="about.html">Learn More About Briva {ICONS["arrow"]}</a>
        </div>

        <div class="pillar-stack" data-reveal>
          <div class="pillar-box">
            <h3>Our Vision</h3>
            <p>To be the leading mining and exploration solutions provider in Africa, recognized for technical innovation, environmental sustainability, and uncompromising integrity.</p>
          </div>
          <div class="pillar-box">
            <h3>Our Mission</h3>
            <p>To deliver end-to-end, reliable, and cost-effective mining and exploration services through technical excellence, environmental stewardship, and strong community engagement.</p>
          </div>
          <div class="pillar-box">
            <h3>Core Governance</h3>
            <p>Every field programme is governed by six non-negotiable standards: Integrity, Technical Excellence, Innovation, Sustainability, Stakeholder Collaboration, and Zero-Harm Safety.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Technical Capabilities</span>
            <h2>Comprehensive Services Across the Mining Lifecycle</h2>
            <p class="section-lead">Integrated geological, geophysical, engineering, and transaction advisory capabilities tailored to East African mineral tenures.</p>
          </div>
          <a class="btn btn--outline" href="services.html">All 6 Disciplines {ICONS["arrow"]}</a>
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
            <span class="eyebrow">Field Track Record</span>
            <h2>Selected Exploration &amp; Mining Projects</h2>
            <p class="section-lead">Representative geological mapping, geochemical prospecting, core drilling, and mine support programmes delivered across Tanzania.</p>
          </div>
          <a class="btn btn--outline" href="projects.html">View All 14 Projects {ICONS["arrow"]}</a>
        </div>
        <div id="featured-projects-grid" class="grid grid--3"></div>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="equipment-feature" data-reveal>
          <div>
            <span class="eyebrow">Exploration Instrumentation</span>
            <h2>Certified Geophysical Scanners &amp; Precision Detectors</h2>
            <p>
              Alongside consulting, Briva supplies and supports professional subsurface detection instruments for prospecting teams, cooperatives, and field geologists—complete with operator training, nationwide delivery, and a 1-year warranty.
            </p>
            <div class="check-grid">
              <div class="check-item">{ICONS["check"]} <span>Available for purchase or short-term rental</span></div>
              <div class="check-item">{ICONS["check"]} <span>Hands-on operator training included</span></div>
            </div>
            <a class="btn btn--primary" href="equipment.html">Browse Equipment Catalog {ICONS["arrow"]}</a>
          </div>
          <div class="equipment-feature__preview">
            <a class="equipment-mini-card card--interactive" href="equipment-megascan.html">
              <img loading="lazy" src="images/equipment/mega-scan-pro.jpg" alt="Mega Scan Pro Geophysical Scanner">
              <h4>Mega Scan Pro</h4>
              <span class="tabular">TZS 20,000,000 &middot; 50m Depth</span>
            </a>
            <a class="equipment-mini-card card--interactive" href="equipment-pinpointer.html">
              <img loading="lazy" src="images/equipment/gold-pin-pointer.jpg" alt="Gold Pin Pointer Detector">
              <h4>Gold Pin Pointer</h4>
              <span class="tabular">TZS 500,000 &middot; Waterproof</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Client Endorsements</span>
          <h2>Trusted by Mining Operators &amp; Institutional Partners</h2>
        </div>

        <div class="grid grid--3 mb-10">
          <article class="card testimonial-card" data-reveal>
            <p class="testimonial-card__quote">
              &ldquo;Briva has been a trusted partner in our exploration projects. Their team combines technical expertise with professionalism, delivering accurate geological data that has been crucial to our success.&rdquo;
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
              &ldquo;From resource modelling to compliance reporting, Briva exceeded our expectations. Their attention to detail and commitment to sustainability make them stand out in the industry.&rdquo;
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
              &ldquo;Briva’s comprehensive services and strong regulatory knowledge gave us the confidence to invest in new mining ventures. They truly understand the mining lifecycle.&rdquo;
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
    "Briva Exploration & Mining is a Dar es Salaam consultancy providing geological exploration, 3D resource estimation, mine planning, drilling supervision, ASM support, and geophysical scanners across East Africa.",
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
          <span>About Us</span>
        </nav>
        <h1>Multidisciplinary Mining &amp; Geological Expertise</h1>
        <p class="page-hero__lead">Delivering reliable, sustainable, and technically rigorous mineral exploration and engineering solutions across Tanzania and East Africa.</p>
      </div>
    </section>

    <section class="section">
      <div class="container split-layout">
        <div data-reveal>
          <span class="eyebrow">Who We Are</span>
          <h2>Bridging Geological Discovery and Responsible Production</h2>
          <p>
            Briva Exploration &amp; Mining is a Dar es Salaam–headquartered consultancy uniting experienced field geologists, geophysicists, mining engineers, financial analysts, and corporate advisors. Together, our leadership brings more than two decades of hands-on operational experience across East Africa, West Africa, and South Asia.
          </p>
          <p>
            We serve international exploration companies, institutional partners, industrial mineral producers, and Tanzanian Primary Mining Licence (PML) cooperatives—providing accurate subsurface data, practical engineering designs, and transparent transaction advisory.
          </p>
          <div class="pillar-stack mt-8">
            <div class="pillar-box">
              <h3>Our Vision</h3>
              <p>To be the leading mining and exploration solutions provider in Africa, recognized for innovation, sustainability, and uncompromising integrity.</p>
            </div>
            <div class="pillar-box">
              <h3>Our Mission</h3>
              <p>To deliver end-to-end, reliable, and cost-effective mining and exploration services through technical excellence, environmental stewardship, and strong community engagement.</p>
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
          <span class="eyebrow eyebrow--light">Commodity Experience</span>
          <h2>Active Across Tanzania’s Key Mineral Corridors</h2>
          <p class="section-lead">Field-tested across diverse geological terrains—from Archean greenstone gold belts to zoned pegmatites, Karoo coal basins, and Neoproterozoic metamorphic suites.</p>
        </div>
        <div class="grid grid--4">
          <div class="process-step">
            <span class="process-step__num">PRECIOUS METALS</span>
            <h3>Lode &amp; Alluvial Gold</h3>
            <p>Structural shear-zone mapping, channel sampling, and ASM technical support in Tabora and Morogoro.</p>
          </div>
          <div class="process-step">
            <span class="process-step__num">CRITICAL MINERALS</span>
            <h3>Lithium, Graphite &amp; Beryllium</h3>
            <p>Pegmatite and gneiss evaluation across Dodoma, Merelani, and Namtumbo battery-mineral belts.</p>
          </div>
          <div class="process-step">
            <span class="process-step__num">ENERGY MINERALS</span>
            <h3>Thermal &amp; Coking Coal</h3>
            <p>Outcrop correlation, seam cross-section modelling, and active underground/pit face mapping in Liweta.</p>
          </div>
          <div class="process-step">
            <span class="process-step__num">BASE &amp; INDUSTRIAL</span>
            <h3>Cu-Zn, Dolomite &amp; Quartz</h3>
            <p>Polymetallic exploration in Mpanda alongside high-purity dolomite and industrial quartz assessments.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Operating Principles</span>
            <h2>Six Core Values Governing Every Engagement</h2>
          </div>
          <a class="btn btn--outline" href="team.html">Meet Our Leadership Team {ICONS["arrow"]}</a>
        </div>
        <div class="grid grid--3">
          <div class="card value-card" data-reveal>
            <h3>01. Uncompromising Integrity</h3>
            <p>We operate with complete transparency, independent scientific honesty, and strict QA/QC accountability in every assay, log, and report.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>02. Technical Excellence</h3>
            <p>We uphold international geological and engineering standards so clients can make confident capital allocation decisions.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>03. Applied Innovation</h3>
            <p>We combine modern 3D geological modelling, GIS analysis, and multi-system geophysical instrumentation to reduce discovery cost.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>04. Environmental Stewardship</h3>
            <p>We prioritize low-impact exploration practices, drill-pad rehabilitation, and responsible resource extraction.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>05. Stakeholder Collaboration</h3>
            <p>We build constructive, lasting partnerships with licence holders, local communities, regulators, and institutional investors.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>06. Zero-Harm Safety</h3>
            <p>We enforce rigorous health, ground-control, and field safety protocols across every camp, trench, rig site, and mine face.</p>
          </div>
        </div>
      </div>
    </section>
    {render_cta_band()}
"""

render_shell(
    "about.html",
    "About Us — Governance, Commodities & Expertise",
    "Learn about Briva Exploration & Mining—our Dar es Salaam leadership, mission, six core governance values, and multi-commodity track record across East Africa.",
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
        <h1>Geological, Engineering &amp; Advisory Services</h1>
        <p class="page-hero__lead">Six integrated technical disciplines supporting mineral tenures from initial reconnaissance through drilling, 3D resource estimation, mine design, and JV structuring.</p>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Core Disciplines</span>
          <h2>Select a Discipline to View Deliverables &amp; Methodology</h2>
        </div>
        <div class="grid grid--3">
          {render_service_cards()}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Engagement Workflow</span>
          <h2>How We Advance Mineral Assets</h2>
          <p class="section-lead">A staged, decision-gated workflow that controls exploration spend while systematically building geological confidence.</p>
        </div>
        <div class="process-grid">
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 01</span>
            <h3>Tenure &amp; Desktop Study</h3>
            <p>GIS compilation, satellite structural review, historical assay audit, and statutory licence verification.</p>
          </div>
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 02</span>
            <h3>Field Mapping &amp; Sampling</h3>
            <p>Outcrop geological mapping, soil/stream grids, trenching, and ground geophysics to isolate high-tenor anomalies.</p>
          </div>
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 03</span>
            <h3>Drilling Supervision</h3>
            <p>Turnkey DD/RC rig supervision, oriented core logging, RQD measurement, and QA/QC laboratory dispatch.</p>
          </div>
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 04</span>
            <h3>3D Resource &amp; Mine Plan</h3>
            <p>Wireframing, block grade estimation, pit/underground engineering, and production fleet scheduling.</p>
          </div>
          <div class="process-step" data-reveal>
            <span class="process-step__num">STAGE 05</span>
            <h3>Compliance &amp; JV Advisory</h3>
            <p>Statutory technical reporting, DCF economic analysis, and structured joint-venture investor engagement.</p>
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
            <h3>Discuss Your Licence or Project</h3>
            <p>Request a technical scope proposal, field team mobilization schedule, or fee estimate from our Dar es Salaam office.</p>
            <a id="service-sidebar-cta-btn" class="btn btn--primary w-full" href="contact.html?service={s0["slug"]}">Enquire About This Service</a>
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
    "Detailed technical deliverables, methodology, and FAQs for Briva's geological exploration, 3D resource estimation, mine planning, drilling supervision, ASM, and M&A services.",
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
        <h1>Field Exploration &amp; Mining Portfolio</h1>
        <p class="page-hero__lead">Fourteen representative exploration, geological mapping, core drilling, and mine support assignments delivered across Tanzania.</p>
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
          <p class="mt-6">Please enable JavaScript to browse and filter our interactive project catalog, or contact <a href="mailto:info@briva.co.tz">info@briva.co.tz</a> for our corporate credentials dossier.</p>
        </noscript>
      </div>
    </section>
    {render_cta_band(
        heading="Have a Mineral Licence or Deposit to Evaluate?",
        sub="Engage our field geologists for reconnaissance mapping, geochemical sampling, diamond core supervision, or independent technical due diligence."
    )}
"""

render_shell(
    "projects.html",
    "Field Projects Portfolio — Lithium, Gold, Coal, Graphite & Cu-Zn",
    "Explore Briva's portfolio of 14 mineral exploration, geological mapping, diamond core drilling, and mining projects across Dodoma, Mpanda, Morogoro, Merelani, Tabora, Liweta, and Namtumbo.",
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
            <span class="eyebrow">More Field Work</span>
            <h2>Related Projects in Tanzania</h2>
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
    "Detailed field project scope, location, area, and geological outcomes delivered by Briva Exploration & Mining in Tanzania.",
    "projects",
    projects_single_body,
    extra_scripts=["js/projects.js"],
)


# ==============================================================================
# 7. equipment.html (Unified Light Architectural Catalog)
# ==============================================================================
equipment_body = f"""
    <section class="page-hero page-hero--rig">
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>Equipment</span>
        </nav>
        <h1>Field &amp; Geophysical Detection Equipment</h1>
        <p class="page-hero__lead">Certified subsurface scanners and handheld target pinpointers available for outright purchase or field rental—backed by operator training and local warranty support in Tanzania.</p>
      </div>
    </section>

    <section class="section section--subtle">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Instrument Catalog</span>
          <h2>Subsurface Scanners &amp; Precision Detectors</h2>
          <p class="section-lead">Engineered for prospecting teams, small-scale mining operators, and field geologists requiring reliable target discrimination.</p>
        </div>

        <div class="grid grid--2">
          <!-- Product 1: Mega Scan Pro -->
          <article class="card card--interactive equipment-card" data-reveal>
            <a class="equipment-card__studio" href="equipment-megascan.html">
              <span class="equipment-card__tag">Multi-System Scanner</span>
              <img src="images/equipment/mega-scan-pro.jpg" alt="Mega Scan Pro Geophysical Detection System">
            </a>
            <div class="equipment-card__body">
              <div>
                <span class="eyebrow">Geophysical Ground Scanner</span>
                <h3><a href="equipment-megascan.html">Mega Scan Pro</a></h3>
                <p>
                  Multi-purpose geophysical detection system combining 3D ground scanning, long-range locator (LRL) antennas, ionic/bionic sensing, and V.S.T vertical probe analysis for deep mineral and cavity detection.
                </p>
                <div class="equipment-card__specs">
                  <div>
                    <span class="equipment-card__spec-label">Max Detection Depth</span>
                    <span class="equipment-card__spec-val">Up to 50 Metres</span>
                  </div>
                  <div>
                    <span class="equipment-card__spec-label">Horizontal Scan Range</span>
                    <span class="equipment-card__spec-val">Up to 3,000 Metres</span>
                  </div>
                  <div>
                    <span class="equipment-card__spec-label">Search Modes</span>
                    <span class="equipment-card__spec-val">6 Integrated Systems</span>
                  </div>
                  <div>
                    <span class="equipment-card__spec-label">Availability</span>
                    <span class="equipment-card__spec-val">Purchase &amp; Field Rental</span>
                  </div>
                </div>
              </div>
              <div class="equipment-card__footer">
                <div>
                  <span class="price-label">Purchase Price</span>
                  <span class="price-amount"><small>TZS</small>20,000,000</span>
                </div>
                <a class="btn btn--primary" href="equipment-megascan.html">Technical Sheet {ICONS["arrow"]}</a>
              </div>
            </div>
          </article>

          <!-- Product 2: Gold Pin Pointer -->
          <article class="card card--interactive equipment-card" data-reveal>
            <a class="equipment-card__studio" href="equipment-pinpointer.html">
              <span class="equipment-card__tag">Field Ready</span>
              <img src="images/equipment/gold-pin-pointer.jpg" alt="Gold Pin Pointer Precision Handheld Detector">
            </a>
            <div class="equipment-card__body">
              <div>
                <span class="eyebrow">Precision Target Pinpointer</span>
                <h3><a href="equipment-pinpointer.html">Gold Pin Pointer</a></h3>
                <p>
                  Rugged, waterproof 360-degree handheld pinpointing probe built for rapid isolation of fine gold nuggets, mineralized veinlets, and metallic targets in trenches, pits, and crushed ore piles.
                </p>
                <div class="equipment-card__specs">
                  <div>
                    <span class="equipment-card__spec-label">Operating Frequency</span>
                    <span class="equipment-card__spec-val">11.5 kHz High-Sensitivity</span>
                  </div>
                  <div>
                    <span class="equipment-card__spec-label">Environmental Rating</span>
                    <span class="equipment-card__spec-val">IP68 Waterproof (3 m)</span>
                  </div>
                  <div>
                    <span class="equipment-card__spec-label">Detection Field</span>
                    <span class="equipment-card__spec-val">360&deg; Side-Scan + Tip</span>
                  </div>
                  <div>
                    <span class="equipment-card__spec-label">Availability</span>
                    <span class="equipment-card__spec-val">Purchase &amp; Field Rental</span>
                  </div>
                </div>
              </div>
              <div class="equipment-card__footer">
                <div>
                  <span class="price-label">Purchase Price</span>
                  <span class="price-amount"><small>TZS</small>500,000</span>
                </div>
                <a class="btn btn--primary" href="equipment-pinpointer.html">Technical Sheet {ICONS["arrow"]}</a>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Briva Supply Assurance</span>
          <h2>Local Training, Delivery &amp; After-Sales Support</h2>
          <p class="section-lead">Every unit supplied by Briva includes practical calibration guidance from qualified geologists—not box-shifting without support.</p>
        </div>

        <div class="grid grid--4">
          <div class="card value-card" data-reveal>
            <h3>1-Year Warranty</h3>
            <p>Full manufacturer coverage on control units, probes, and electronics with straightforward local support through our Dar es Salaam office.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>Operator Field Training</h3>
            <p>Hands-on instruction covering ground balance, false-mineralization filtering, and scan interpretation included with every purchase.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>Nationwide Delivery</h3>
            <p>Secure, tracked dispatch from Dar es Salaam to regional mining hubs across Dodoma, Mwanza, Geita, Tabora, Mbeya, and Morogoro.</p>
          </div>
          <div class="card value-card" data-reveal>
            <h3>Purchase or Rental</h3>
            <p>Flexible commercial options allowing exploration teams to purchase outright or enquire about supervised short-term field rental.</p>
          </div>
        </div>
      </div>
    </section>
    {render_cta_band(
        heading="Request an Equipment Quotation or Demonstration",
        sub="Contact our Dar es Salaam sales desk to confirm stock availability, schedule an in-office demonstration, or request a formal proforma invoice.",
        primary_label="Contact Equipment Desk",
        primary_href="contact.html?type=equipment"
    )}
"""

render_shell(
    "equipment.html",
    "Geophysical & Mining Equipment — Mega Scan Pro & Gold Pin Pointer",
    "Browse Briva's certified geophysical detection systems and handheld gold pinpointers in Tanzania, including technical specifications, TZS pricing, operator training, and 1-year warranty.",
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
            <img src="images/equipment/mega-scan-pro.jpg" alt="Mega Scan Pro Geophysical Detection System with V.S.T probe, antennas, and case">
          </div>
        </div>

        <div>
          <span class="eyebrow">Multi-System Geophysical Scanner</span>
          <h1>Mega Scan Pro</h1>
          <p class="section-lead">
            Professional 6-system geophysical locator and subsurface scanner engineered for deep metallic mineralization, gold-bearing structures, buried targets, and subterranean cavity detection.
          </p>

          <div class="product-summary__price-box">
            <div>
              <span class="price-label">Standard Kit Price</span>
              <div class="product-summary__price"><small>TZS</small>20,000,000</div>
            </div>
            <span class="equipment-card__tag">1-Year Warranty &amp; Training Included</span>
          </div>

          <div class="product-summary__actions">
            <a class="btn btn--primary btn--lg" href="contact.html?product=megascan&amp;type=buy">Request Purchase Quote {ICONS["arrow"]}</a>
            <a class="btn btn--outline btn--lg" href="contact.html?product=megascan&amp;type=rent">Enquire About Rental</a>
          </div>

          <a class="manual-download" href="downloads/Mega Scan Pro EN.pdf" target="_blank" rel="noopener noreferrer">
            <span class="check-item">{ICONS["file"]} <span>Download Official Manufacturer Manual (PDF)</span></span>
            <span class="link-arrow">Open PDF {ICONS["arrow"]}</span>
          </a>

          <div data-tabs>
            <div class="tabs__nav" role="tablist" aria-label="Mega Scan Pro details">
              <button type="button" class="tabs__btn" role="tab" id="tab-ms-systems" aria-selected="true" aria-controls="panel-ms-systems">Detection Systems</button>
              <button type="button" class="tabs__btn" role="tab" id="tab-ms-kit" aria-selected="false" aria-controls="panel-ms-kit" tabindex="-1">Standard Kit Contents</button>
            </div>

            <div class="tabs__panel" id="panel-ms-systems" role="tabpanel" aria-labelledby="tab-ms-systems">
              <div class="deliverables-grid">
                <div class="deliverable-item">{ICONS["check"]}<span>Long-Range Locator (LRL) with program-specific mineral frequency tuning</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Magnetometer &amp; V.S.T vertical high-sensitivity signal transceiver</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Ionic &amp; Bionic scan modes for long-buried metallic &amp; void anomalies</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>5-inch high-contrast TFT colour telemetry screen with GPS coordinate logging</span></div>
              </div>
            </div>

            <div class="tabs__panel" id="panel-ms-kit" role="tabpanel" aria-labelledby="tab-ms-kit" hidden>
              <div class="deliverables-grid">
                <div class="deliverable-item">{ICONS["check"]}<span>Mega Scan Pro main control unit with 5&Prime; TFT colour display</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>I.M.T.U Intelligent Multi Transceiver Unit</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>V.S.T Vertical High-Sensitivity Signal Transceiver probe</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Pair of telescopic directional search antennas</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>High-capacity lithium-ion battery pack, charger &amp; field headphones</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Shockproof, dust-sealed ABS hard transport case &amp; user documentation</span></div>
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
          <a class="link-arrow" href="equipment.html">&larr; Back to Equipment Catalog</a>
        </div>

        <div class="spec-table-wrap">
          <table class="spec-table">
            <tbody>
              <tr><th scope="row">Microprocessor</th><td>ARM 168 MHz Architecture</td></tr>
              <tr><th scope="row">System Memory</th><td>512 KB Integrated Flash</td></tr>
              <tr><th scope="row">Display</th><td>5.0-inch TFT High-Brightness Colour LCD</td></tr>
              <tr><th scope="row">Maximum Detection Depth</th><td>Up to 50 Metres (target size &amp; ground matrix dependent)</td></tr>
              <tr><th scope="row">Horizontal Scan Range</th><td>Up to 3,000 Metres (Long-Range Locator mode)</td></tr>
              <tr><th scope="row">Integrated Detection Modes</th><td>6 Systems (Auto LRL, Manual LRL, Ionic, Bionic, Magnetometer, V.S.T Pinpoint)</td></tr>
              <tr><th scope="row">Continuous Battery Runtime</th><td>Up to 15 Hours per charge</td></tr>
              <tr><th scope="row">Full Transport Kit Weight</th><td>6.3 kg (in waterproof ABS hard case)</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
    {render_cta_band(
        heading="Order or Rent the Mega Scan Pro in Tanzania",
        sub="Speak with our technical equipment desk in Dar es Salaam for proforma invoicing, rental terms, and included operator field training.",
        primary_label="Request Formal Quote",
        primary_href="contact.html?product=megascan&type=buy"
    )}
"""

render_shell(
    "equipment-megascan.html",
    "Mega Scan Pro — Geophysical Scanner Specifications & Price",
    "Full technical specifications, kit contents, manual download, and TZS pricing for the Mega Scan Pro 6-system geophysical scanner available for purchase or rental from Briva in Dar es Salaam.",
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
            High-sensitivity, IP68 waterproof handheld pinpointing detector engineered to rapidly isolate fine gold nuggets, mineralized veinlets, and metallic targets in trenches, shafts, and alluvial wash.
          </p>

          <div class="product-summary__price-box">
            <div>
              <span class="price-label">Unit Price</span>
              <div class="product-summary__price"><small>TZS</small>500,000</div>
            </div>
            <span class="equipment-card__tag">IP68 Waterproof &middot; In Stock</span>
          </div>

          <div class="product-summary__actions">
            <a class="btn btn--primary btn--lg" href="contact.html?product=pinpointer&amp;type=buy">Request Purchase Quote {ICONS["arrow"]}</a>
            <a class="btn btn--outline btn--lg" href="contact.html?product=pinpointer&amp;type=rent">Enquire About Bulk / Rental</a>
          </div>

          <div data-tabs>
            <div class="tabs__nav" role="tablist" aria-label="Gold Pin Pointer details">
              <button type="button" class="tabs__btn" role="tab" id="tab-pp-features" aria-selected="true" aria-controls="panel-pp-features">Field Capabilities</button>
              <button type="button" class="tabs__btn" role="tab" id="tab-pp-kit" aria-selected="false" aria-controls="panel-pp-kit" tabindex="-1">Package Contents</button>
            </div>

            <div class="tabs__panel" id="panel-pp-features" role="tabpanel" aria-labelledby="tab-pp-features">
              <div class="deliverables-grid">
                <div class="deliverable-item">{ICONS["check"]}<span>360&deg; cylindrical side-scan field plus precision tip pinpointing</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Proportional audio &amp; haptic vibration pulse rate as probe nears target</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>One-touch fast retune to narrow detection field in mineralized soils</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Integrated high-output LED worklight for underground faces &amp; deep pits</span></div>
              </div>
            </div>

            <div class="tabs__panel" id="panel-pp-kit" role="tabpanel" aria-labelledby="tab-pp-kit" hidden>
              <div class="deliverables-grid">
                <div class="deliverable-item">{ICONS["check"]}<span>Gold Pin Pointer sealed handheld probe unit</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Heavy-duty woven belt holster</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>Coiled anti-loss security lanyard</span></div>
                <div class="deliverable-item">{ICONS["check"]}<span>9V alkaline battery &amp; operator quick-start guide</span></div>
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
          <a class="link-arrow" href="equipment.html">&larr; Back to Equipment Catalog</a>
        </div>

        <div class="spec-table-wrap">
          <table class="spec-table">
            <tbody>
              <tr><th scope="row">Operating Frequency</th><td>11.5 kHz Pulse/VLF Tuned Circuitry</td></tr>
              <tr><th scope="row">Ingress Protection</th><td>IP68 Submersible up to 3 Metres (10 ft)</td></tr>
              <tr><th scope="row">Sensitivity Levels</th><td>3 Selectable Sensitivity Tiers + Fast Retune</td></tr>
              <tr><th scope="row">Target Indicators</th><td>Proportional Audio Tone + Haptic Vibration + Signal Readout</td></tr>
              <tr><th scope="row">Operating Temperature</th><td>-20&deg;C to +54&deg;C</td></tr>
              <tr><th scope="row">Power Supply</th><td>Single 9V Battery (up to 30 hours continuous use)</td></tr>
              <tr><th scope="row">Length &amp; Weight</th><td>24 cm length &middot; 200 g (with battery installed)</td></tr>
              <tr><th scope="row">Warranty</th><td>1-Year Briva Local Replacement/Repair Warranty</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
    {render_cta_band(
        heading="Equip Your Field Crew with the Gold Pin Pointer",
        sub="Single-unit and cooperative bulk orders available for immediate dispatch across Tanzania.",
        primary_label="Order Gold Pin Pointer",
        primary_href="contact.html?product=pinpointer&type=buy"
    )}
"""

render_shell(
    "equipment-pinpointer.html",
    "Gold Pin Pointer — Precision Waterproof Detector Specs & Price",
    "Technical specifications, package contents, and TZS 500,000 pricing for the IP68 waterproof Gold Pin Pointer handheld detector supplied by Briva in Tanzania.",
    "equipment",
    pinpointer_body,
)


# ==============================================================================
# 10. team.html (All 7 Members — Restoring Raju Badugu, Head of Geology)
# ==============================================================================
team_body = f"""
    <section class="page-hero page-hero--drill">
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep" aria-hidden="true">/</span>
          <span>Team</span>
        </nav>
        <h1>Executive Leadership &amp; Technical Specialists</h1>
        <p class="page-hero__lead">A multidisciplinary bench of geologists, geophysicists, mining engineers, and corporate advisors combining East African field insight with international operational depth.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Board &amp; Executive Direction</span>
          <h2>Executive Leadership</h2>
        </div>

        <div class="grid grid--2 mb-10">
          <article class="card exec-card" data-reveal>
            <div class="exec-card__avatar">
              <img loading="lazy" src="images/team/Alex S Bashire.jpg" alt="Alex S. Bashire — Chief Executive Officer">
            </div>
            <div>
              <span class="exec-card__role">Chief Executive Officer</span>
              <h3>Alex S. Bashire</h3>
              <p class="exec-card__bio">
                Dynamic and results-driven Chief Executive with over 23 years of senior leadership across mineral exploration, tenure strategy, stakeholder engagement, and mining project development in East Africa.
              </p>
            </div>
          </article>

          <article class="card exec-card" data-reveal>
            <div class="exec-card__avatar">
              <img loading="lazy" src="images/team/K. Sridhar Reddy.png" alt="K. Sridhar Reddy — Non-Executive Director">
            </div>
            <div>
              <span class="exec-card__role">Non-Executive Director</span>
              <h3>K. Sridhar Reddy</h3>
              <p class="exec-card__bio">
                Seasoned mining executive bringing more than 25 years of international experience in large-scale mining operations, capital project execution, and corporate governance.
              </p>
            </div>
          </article>
        </div>

        <div class="section-head mt-10">
          <span class="eyebrow">Technical &amp; Corporate Practice Heads</span>
          <h2>Senior Consultants &amp; Specialists</h2>
        </div>

        <div class="grid grid--3">
          <article class="card team-card" data-reveal>
            <div class="team-card__photo">
              <img loading="lazy" src="images/team/RAJU BADUGU.jpg" alt="Raju Badugu — Head of Geology">
            </div>
            <div class="team-card__body">
              <span class="team-card__role">Head of Geology</span>
              <h3>Raju Badugu</h3>
              <p class="team-card__bio">
                Senior exploration geologist leading litho-structural mapping, geochemical sampling QA/QC, diamond core logging, and deposit evaluation campaigns across diverse mineral belts.
              </p>
            </div>
          </article>

          <article class="card team-card" data-reveal>
            <div class="team-card__photo">
              <img loading="lazy" src="images/team/Dr. Kolipaka Venu.jpg" alt="Dr. Kolipaka Venu — Geophysics Consultant">
            </div>
            <div class="team-card__body">
              <span class="team-card__role">Geophysics Consultant</span>
              <h3>Dr. Kolipaka Venu</h3>
              <p class="team-card__bio">
                Accomplished exploration geophysicist with over 12 years of experience designing and interpreting ground and airborne geophysical surveys across India and Africa.
              </p>
            </div>
          </article>

          <article class="card team-card" data-reveal>
            <div class="team-card__photo">
              <img loading="lazy" src="images/team/SRIRAMA GOPAL YELLAPRAGADA.jpg" alt="Srirama Gopal Yellapragada — Engineering Consultant">
            </div>
            <div class="team-card__body">
              <span class="team-card__role">Engineering Consultant</span>
              <h3>Srirama Gopal Yellapragada</h3>
              <p class="team-card__bio">
                Experienced Mines Manager specializing in open-pit mine planning, production fleet optimization, feasibility scheduling, and operational safety leadership.
              </p>
            </div>
          </article>

          <article class="card team-card" data-reveal>
            <div class="team-card__photo">
              <img loading="lazy" src="images/team/JACKLINE SAYI KIDENDEI.jpg" alt="Jackline Sayi Kidendei — Geologist &amp; Marketing Manager">
            </div>
            <div class="team-card__body">
              <span class="team-card__role">Geologist &amp; Marketing Manager</span>
              <h3>Jackline Sayi Kidendei</h3>
              <p class="team-card__bio">
                Exploration geologist and client engagement lead combining field geological background with commercial partnership development across Tanzania’s mining sector.
              </p>
              <div class="team-card__links">
                <a class="link-arrow" href="https://www.linkedin.com/in/jackline-kidendei-8a8789371" target="_blank" rel="noopener noreferrer">
                  {ICONS["linkedin"]} LinkedIn Profile
                </a>
              </div>
            </div>
          </article>

          <article class="card team-card" data-reveal>
            <div class="team-card__photo">
              <img loading="lazy" src="images/team/Vashty J Nyembera.jpg" alt="Vashty J. Nyembera — HR &amp; Finance Consultant">
            </div>
            <div class="team-card__body">
              <span class="team-card__role">HR &amp; Finance Consultant</span>
              <h3>Vashty J. Nyembera</h3>
              <p class="team-card__bio">
                Corporate advisor overseeing project financial administration, human capital strategy, field workforce compliance, and operational budgeting.
              </p>
            </div>
          </article>
        </div>
      </div>
    </section>
    {render_cta_band(
        heading="Work Directly With Our Senior Specialists",
        sub="Connect with our geology, geophysics, and mine engineering leads to scope your upcoming exploration or operational programme."
    )}
"""

render_shell(
    "team.html",
    "Leadership & Technical Team",
    "Meet Briva's executive directors and specialist consultants in geology, geophysics, open-pit mine engineering, and corporate finance.",
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
        <h1>Contact Our Dar es Salaam Office</h1>
        <p class="page-hero__lead">Request a technical consultation, exploration proposal, joint-venture review, or formal quotation on geophysical detection equipment.</p>
      </div>
    </section>

    <section class="section">
      <div class="container contact-layout">
        <div>
          <span class="eyebrow">Direct Channels</span>
          <h2>Head Office &amp; Enquiries</h2>
          <p class="mb-6">Our consulting and equipment teams are available six days a week for office meetings in Dar es Salaam and rapid mobilization across Tanzania.</p>

          <div class="contact-info-list">
            <div class="card contact-info-card">
              <span class="contact-info-card__icon">{ICONS["pin"]}</span>
              <div>
                <h3>Office Address</h3>
                <p>P.O. Box 11259, Dar es Salaam, Tanzania</p>
              </div>
            </div>

            <div class="card contact-info-card">
              <span class="contact-info-card__icon">{ICONS["phone"]}</span>
              <div>
                <h3>Direct Telephone</h3>
                <p><a class="tabular" href="tel:+255767413950">+255 767 413 950</a></p>
              </div>
            </div>

            <div class="card contact-info-card">
              <span class="contact-info-card__icon">{ICONS["mail"]}</span>
              <div>
                <h3>Corporate Email</h3>
                <p><a href="mailto:info@briva.co.tz">info@briva.co.tz</a></p>
              </div>
            </div>

            <div class="card contact-info-card">
              <span class="contact-info-card__icon">{ICONS["clock"]}</span>
              <div>
                <h3>Office Hours</h3>
                <p class="tabular">Mon – Fri: 10:00 – 16:00 &middot; Saturday: 12:00 – 15:00</p>
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
          <span class="eyebrow">Project &amp; Equipment Desk</span>
          <h2 class="mb-6">Send Us an Enquiry</h2>

          <div id="contact-success" class="form-alert form-alert--success" role="status" tabindex="-1" hidden>
            Thank you—your enquiry has been received by Briva Exploration &amp; Mining. A member of our Dar es Salaam team will respond shortly.
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
                <label class="form-label" for="subject">Enquiry Category *</label>
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
                <label class="form-label" for="message">Project Details or Message *</label>
                <textarea class="form-control" id="message" name="message" required placeholder="Share your mineral commodity, region/licence status, or equipment requirements..."></textarea>
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
    "Contact Us — Dar es Salaam Consulting & Equipment Desk",
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
          <h1>Thank You for Contacting Briva</h1>
          <p>
            Your enquiry has been routed to our Dar es Salaam consulting and equipment desk. If your request is time-sensitive, you can also reach us directly on <a href="tel:+255767413950"><strong>+255 767 413 950</strong></a>.
          </p>
          <div class="status-page__actions">
            <a class="btn btn--primary" href="index.html">Return to Home</a>
            <a class="btn btn--outline" href="projects.html">Explore Field Projects</a>
            <a class="btn btn--outline" href="equipment.html">Equipment Catalog</a>
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
            The page you requested may have moved or no longer exists. Use the links below to explore Briva’s consulting disciplines, field projects, or equipment catalog.
          </p>
          <div class="status-page__actions">
            <a class="btn btn--primary" href="index.html">Back to Home</a>
            <a class="btn btn--outline" href="services.html">Our Services</a>
            <a class="btn btn--outline" href="contact.html">Contact Us</a>
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
