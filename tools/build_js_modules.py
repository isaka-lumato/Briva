"""Build js/projects.js and js/services.js with live JSON fetch + offline file:// fallback."""
import json
import os

ROOT = os.getcwd()
projects_json = open(os.path.join(ROOT, "data", "projects.json"), encoding="utf-8").read().strip()
services_json = open(os.path.join(ROOT, "data", "services.json"), encoding="utf-8").read().strip()

projects_js = f"""/* ==========================================================================
   BRIVA EXPLORATION & MINING — UNIFIED PROJECTS PORTFOLIO ENGINE
   Drives: index.html (featured), projects.html (filterable), projects-single.html
   Source of truth: data/projects.json (managed via Decap CMS /admin/)
   ========================================================================== */

(function () {{
  'use strict';

  const FALLBACK_DATA = {projects_json};

  function esc(str) {{
    return String(str == null ? '' : str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }}

  function normalizeProjects(raw) {{
    if (raw && Array.isArray(raw.projects)) {{
      return raw.projects;
    }}
    if (raw && typeof raw === 'object') {{
      return Object.keys(raw).map((k) => Object.assign({{ id: k }}, raw[k]));
    }}
    return [];
  }}

  async function getProjects() {{
    try {{
      const res = await fetch('data/projects.json');
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const data = await res.json();
      return normalizeProjects(data);
    }} catch (_e) {{
      return normalizeProjects(FALLBACK_DATA);
    }}
  }}

  function primaryBadge(categoriesStr) {{
    const parts = String(categoriesStr || 'Exploration')
      .split(',')
      .map((s) => s.trim())
      .filter(Boolean);
    return parts[0] || 'Exploration';
  }}

  function matchesCategory(project, filter) {{
    if (!filter || filter === 'all') return true;
    const hay = String(project.categories || '').toLowerCase();
    return hay.includes(filter.toLowerCase());
  }}

  function renderProjectCard(project) {{
    const img = (project.images && project.images[0]) || 'images/projects/Core drilling.jpg';
    const badge = primaryBadge(project.categories);
    const url = 'projects-single.html?project=' + encodeURIComponent(project.id);
    return (
      '<article class="card card--interactive project-card">' +
        '<a class="project-card__media" href="' + esc(url) + '">' +
          '<span class="project-card__badge">' + esc(badge) + '</span>' +
          '<img loading="lazy" src="' + esc(img) + '" alt="' + esc(project.title) + '">' +
        '</a>' +
        '<div class="project-card__body">' +
          '<div>' +
            '<div class="project-card__meta">' +
              '<span>' + esc(project.location) + '</span>' +
              '<span aria-hidden="true">&middot;</span>' +
              '<span>' + esc(project.year || '2024') + '</span>' +
            '</div>' +
            '<h3 class="project-card__title"><a href="' + esc(url) + '">' + esc(project.title) + '</a></h3>' +
            '<p class="project-card__excerpt">' + esc(project.description) + '</p>' +
          '</div>' +
          '<div class="project-card__foot">' +
            '<span>' + esc(project.size || 'Field Survey') + '</span>' +
            '<a class="link-arrow" href="' + esc(url) + '">Case Study ' +
              '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>' +
            '</a>' +
          '</div>' +
        '</div>' +
      '</article>'
    );
  }}

  async function init() {{
    const homeGrid = document.getElementById('featured-projects-grid');
    const catalogGrid = document.getElementById('projects-catalog-grid');
    const detailRoot = document.getElementById('project-detail-root');

    if (!homeGrid && !catalogGrid && !detailRoot) return;
    const projects = await getProjects();

    /* A. Home Featured Grid (3 flagship projects) */
    if (homeGrid) {{
      let featured = projects.filter((p) => p.featured);
      if (featured.length < 3) {{
        const ids = new Set(featured.map((p) => p.id));
        projects.forEach((p) => {{
          if (featured.length < 3 && !ids.has(p.id)) featured.push(p);
        }});
      }} else {{
        featured = featured.slice(0, 3);
      }}
      homeGrid.innerHTML = featured.map(renderProjectCard).join('');
    }}

    /* B. Full Filterable Projects Page */
    if (catalogGrid) {{
      const filterBtns = Array.from(document.querySelectorAll('[data-project-filter]'));
      const countEl = document.getElementById('projects-count');
      const params = new URLSearchParams(window.location.search);
      let activeFilter = (params.get('category') || 'all').toLowerCase();

      function applyFilter(filterKey, pushUrl) {{
        activeFilter = filterKey;
        filterBtns.forEach((btn) => {{
          const isMatch = btn.getAttribute('data-project-filter') === filterKey;
          btn.classList.toggle('is-active', isMatch);
          btn.setAttribute('aria-pressed', String(isMatch));
        }});
        const filtered = projects.filter((p) => matchesCategory(p, filterKey));
        catalogGrid.innerHTML = filtered.map(renderProjectCard).join('');
        if (countEl) {{
          countEl.textContent = filtered.length + (filtered.length === 1 ? ' project' : ' projects');
        }}
        if (pushUrl && window.history && window.history.replaceState) {{
          const url = new URL(window.location.href);
          if (filterKey === 'all') url.searchParams.delete('category');
          else url.searchParams.set('category', filterKey);
          window.history.replaceState({{}}, '', url.toString());
        }}
      }}

      filterBtns.forEach((btn) => {{
        btn.addEventListener('click', () => {{
          applyFilter(btn.getAttribute('data-project-filter') || 'all', true);
        }});
      }});
      applyFilter(activeFilter, false);
    }}

    /* C. Single Project Case Study Page */
    if (detailRoot) {{
      const params = new URLSearchParams(window.location.search);
      const reqId = params.get('project');
      const project =
        projects.find((p) => p.id === reqId) ||
        projects.find((p) => p.id === 'lithium-dodoma') ||
        projects[0];

      if (!project) return;

      document.title = project.title + ' | Briva Exploration & Mining';
      const metaDesc = document.querySelector('meta[name="description"]');
      if (metaDesc && project.description) metaDesc.setAttribute('content', project.description);

      const crumb = document.getElementById('project-breadcrumb-current');
      if (crumb) crumb.textContent = project.title;

      const mainImg = (project.images && project.images[0]) || 'images/projects/Core drilling.jpg';
      const catTags = String(project.categories || 'Exploration')
        .split(',')
        .map((c) => c.trim())
        .filter(Boolean);

      detailRoot.innerHTML =
        '<div class="case-study-grid">' +
          '<div>' +
            '<div class="case-study__media" data-lightbox="' + esc(mainImg) + '" role="button" tabindex="0" aria-label="Enlarge project photograph">' +
              '<img src="' + esc(mainImg) + '" alt="' + esc(project.title) + '">' +
              '<span class="case-study__zoom-hint">Click to enlarge</span>' +
            '</div>' +
            '<div class="mt-8">' +
              '<span class="eyebrow">' + esc(catTags.join(' · ')) + '</span>' +
              '<h1 class="case-study__heading">' + esc(project.title) + '</h1>' +
              '<p class="case-study__desc">' + esc(project.description) + '</p>' +
            '</div>' +
          '</div>' +
          '<aside>' +
            '<div class="spec-table-wrap mb-6">' +
              '<table class="spec-table">' +
                '<tbody>' +
                  '<tr><th scope="row">Client</th><td>' + esc(project.client || 'Confidential') + '</td></tr>' +
                  '<tr><th scope="row">Location</th><td>' + esc(project.location) + ', Tanzania</td></tr>' +
                  '<tr><th scope="row">Area / Scope</th><td>' + esc(project.size || 'Field Survey') + '</td></tr>' +
                  '<tr><th scope="row">Year</th><td>' + esc(project.year || '2024') + '</td></tr>' +
                  '<tr><th scope="row">Disciplines</th><td>' + esc(project.categories) + '</td></tr>' +
                '</tbody>' +
              '</table>' +
            '</div>' +
            '<div class="sidebar-cta">' +
              '<h3>Planning a Similar Survey?</h3>' +
              '<p>Discuss geological mapping, sampling, drilling supervision, or resource evaluation for your licence area.</p>' +
              '<a class="btn btn--primary w-full" href="contact.html?service=geological-exploration">Request a Consultation</a>' +
            '</div>' +
            '<div class="mt-4">' +
              '<a class="link-arrow" href="projects.html">&larr; Back to All Field Projects</a>' +
            '</div>' +
          '</aside>' +
        '</div>';

      const relatedGrid = document.getElementById('related-projects-grid');
      if (relatedGrid) {{
        const mainCat = catTags[0] || 'Exploration';
        let related = projects.filter((p) => p.id !== project.id && matchesCategory(p, mainCat));
        if (related.length < 3) {{
          const used = new Set(related.map((p) => p.id));
          used.add(project.id);
          projects.forEach((p) => {{
            if (related.length < 3 && !used.has(p.id)) related.push(p);
          }});
        }}
        relatedGrid.innerHTML = related.slice(0, 3).map(renderProjectCard).join('');
      }}
    }}
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', init);
  }} else {{
    init();
  }}
}})();
"""

services_js = f"""/* ==========================================================================
   BRIVA EXPLORATION & MINING — DISCIPLINE DETAIL ENGINE
   Drives: service-single.html?service=<slug>
   Source of truth: data/services.json
   ========================================================================== */

(function () {{
  'use strict';

  const FALLBACK_DATA = {services_json};

  function esc(str) {{
    return String(str == null ? '' : str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }}

  async function getServices() {{
    try {{
      const res = await fetch('data/services.json');
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const data = await res.json();
      return (data && data.services) || [];
    }} catch (_e) {{
      return FALLBACK_DATA.services || [];
    }}
  }}

  async function init() {{
    const contentEl = document.getElementById('service-detail-content');
    const navEl = document.getElementById('service-sidebar-nav');
    if (!contentEl) return;

    const services = await getServices();
    if (!services.length) return;

    const params = new URLSearchParams(window.location.search);
    const reqSlug = params.get('service');
    const current = services.find((s) => s.slug === reqSlug) || services[0];

    document.title = current.title + ' | Briva Exploration & Mining';
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc && current.subtitle) metaDesc.setAttribute('content', current.subtitle);

    const heroTitle = document.getElementById('service-hero-title');
    const heroLead = document.getElementById('service-hero-lead');
    const crumb = document.getElementById('service-breadcrumb-current');
    const ctaBtn = document.getElementById('service-sidebar-cta-btn');

    if (heroTitle) heroTitle.textContent = current.title;
    if (heroLead) heroLead.textContent = current.subtitle;
    if (crumb) crumb.textContent = current.shortTitle || current.title;
    if (ctaBtn) ctaBtn.href = 'contact.html?service=' + encodeURIComponent(current.slug);

    if (navEl) {{
      navEl.innerHTML = services
        .map((s) => {{
          const active = s.slug === current.slug ? ' is-active' : '';
          const aria = s.slug === current.slug ? ' aria-current="page"' : '';
          return (
            '<li><a class="sidebar-nav__link' + active + '"' + aria +
            ' href="service-single.html?service=' + esc(s.slug) + '">' +
            '<span>' + esc(s.shortTitle || s.title) + '</span>' +
            '<span class="sidebar-nav__num">' + esc(s.num) + '</span>' +
            '</a></li>'
          );
        }})
        .join('');
    }}

    const checkSvg =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">' +
      '<path d="M20 6L9 17l-5-5"/></svg>';

    const paragraphs = (current.overview || [])
      .map((p) => '<p>' + esc(p) + '</p>')
      .join('');

    const deliverables = (current.deliverables || [])
      .map((d) => '<div class="deliverable-item">' + checkSvg + '<span>' + esc(d) + '</span></div>')
      .join('');

    const steps = (current.methodology || [])
      .map(
        (m) =>
          '<div class="process-step">' +
            '<span class="process-step__num">STEP ' + esc(m.step) + '</span>' +
            '<h3>' + esc(m.title) + '</h3>' +
            '<p>' + esc(m.text) + '</p>' +
          '</div>'
      )
      .join('');

    const faqs = (current.faqs || [])
      .map(
        (f, idx) =>
          '<details class="faq-item"' + (idx === 0 ? ' open' : '') + '>' +
            '<summary>' + esc(f.q) + '</summary>' +
            '<div class="faq-item__body"><p>' + esc(f.a) + '</p></div>' +
          '</details>'
      )
      .join('');

    contentEl.innerHTML =
      '<img class="detail-hero-img" src="' + esc(current.image) + '" alt="' + esc(current.title) + '">' +
      '<span class="eyebrow">Discipline ' + esc(current.num) + '</span>' +
      '<h2>Overview &amp; Technical Scope</h2>' +
      '<div class="prose-overview">' + paragraphs + '</div>' +
      '<h3>Key Technical Deliverables</h3>' +
      '<div class="deliverables-grid mb-10">' + deliverables + '</div>' +
      '<h3>Execution Methodology</h3>' +
      '<div class="grid grid--3 mb-10">' + steps + '</div>' +
      '<h3>Frequently Asked Questions</h3>' +
      '<div class="faq-list">' + faqs + '</div>';
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', init);
  }} else {{
    init();
  }}
}})();
"""

open(os.path.join(ROOT, "js", "projects.js"), "w", encoding="utf-8").write(projects_js)
open(os.path.join(ROOT, "js", "services.js"), "w", encoding="utf-8").write(services_js)
print("Generated js/projects.js and js/services.js successfully.")
