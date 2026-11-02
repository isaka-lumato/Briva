/* ==========================================================================
   BRIVA EXPLORATION & MINING — UNIFIED PROJECTS PORTFOLIO ENGINE
   Drives: index.html (featured), projects.html (filterable), projects-single.html
   Source of truth: data/projects.json (managed via Decap CMS /admin/)
   ========================================================================== */

(function () {
  'use strict';

  const FALLBACK_DATA = {
  "projects": [
    {
      "id": "lithium-dodoma",
      "title": "Pegmatite Lithium Exploration",
      "location": "Dodoma",
      "size": "45 sq km",
      "client": "Battery Metals Company",
      "year": "2024",
      "categories": "Exploration, Battery Metals",
      "featured": true,
      "images": [
        "images/projects/Pegmatite, lithium exploration In Dodoma.jpg"
      ],
      "description": "Lithium exploration across zoned pegmatite corridors in the Dodoma region, integrating detailed litho-structural mapping, systematic geochemical sampling, and mineralogical prospectivity evaluation."
    },
    {
      "id": "cu-zn-mpanda",
      "title": "Cu-Zn Base Metals Exploration",
      "location": "Mpanda",
      "size": "40 sq km",
      "client": "Mining Corporation",
      "year": "2023",
      "categories": "Exploration, Base Metals",
      "featured": true,
      "images": [
        "images/projects/Cu_zn Exploration_Mpanda.jpg"
      ],
      "description": "Comprehensive copper-zinc polymetallic exploration programme in Mpanda district comprising grid soil geochemistry, bedrock trenching, and ground geophysical surveys to delineate mineralized shear zones."
    },
    {
      "id": "coal-mapping-liweta",
      "title": "Coal Outcrop Structural Mapping",
      "location": "Liweta",
      "size": "8 sq km",
      "client": "Coal Mining Company",
      "year": "2024",
      "categories": "Mapping, Coal",
      "featured": true,
      "images": [
        "images/projects/Coal outcro mapping_Liweta.jpg"
      ],
      "description": "High-resolution geological and stratigraphic mapping of coal seam outcrops in Liweta, Tanzania, delivering seam correlation, structural fault analysis, and coal quality sampling for resource modelling."
    },
    {
      "id": "core-drilling",
      "title": "Diamond Core Drilling Supervision",
      "location": "Multiple Tenures, Tanzania",
      "size": "Multi-Rig Campaigns",
      "client": "Exploration & Mining Clients",
      "year": "2024",
      "categories": "Exploration, Mining",
      "featured": false,
      "images": [
        "images/projects/Core drilling.jpg"
      ],
      "description": "Turnkey diamond core drilling supervision for resource definition and scout exploration, ensuring high core recovery, oriented structural logging, RQD geotechnical recording, and strict QA/QC sampling."
    },
    {
      "id": "gold-mazizi-morogoro",
      "title": "Mazizi Gold Mineralization Study",
      "location": "Mazizi, Morogoro",
      "size": "35 sq km",
      "client": "Gold Exploration Company",
      "year": "2023",
      "categories": "Exploration, Gold",
      "featured": false,
      "images": [
        "images/projects/Gold Mineralization_Mazizi Morogoro.jpg"
      ],
      "description": "Geological investigation of structurally controlled gold mineralization at Mazizi in Morogoro region, encompassing outcrop mapping, channel sampling, and drill target prioritization."
    },
    {
      "id": "face-mapping-coal",
      "title": "Active Coal Mine Face Mapping",
      "location": "Southern Tanzania",
      "size": "Active Mine Operations",
      "client": "Coal Mining Company",
      "year": "2024",
      "categories": "Mapping, Mining",
      "featured": false,
      "images": [
        "images/projects/Face mapping in a coal mine.jpg"
      ],
      "description": "Production face mapping and stratigraphic seam control within active coal mining operations, supporting short-term mine scheduling, roof/wall stability, and ROM coal quality consistency."
    },
    {
      "id": "graphite-merelani",
      "title": "Graphite-Kyanite Gneiss Evaluation",
      "location": "Merelani",
      "size": "18 sq km",
      "client": "Mineral Exploration Company",
      "year": "2023",
      "categories": "Exploration, Industrial Minerals",
      "featured": false,
      "images": [
        "images/projects/Graphite kyanite gneiss_Merelani.jpg"
      ],
      "description": "Geological and mineralogical evaluation of flake graphite and kyanite-bearing gneiss horizons in Merelani, establishing strike continuity and grade distribution."
    },
    {
      "id": "graphite-stockpile-merelani",
      "title": "Graphite Gneiss Stockpile QA/QC",
      "location": "Merelani",
      "size": "Stockpile Assessment",
      "client": "Mining Company",
      "year": "2024",
      "categories": "Mining, Quality Control",
      "featured": false,
      "images": [
        "images/projects/Graphite kyanite gneiss stockpile in Merelani.jpg"
      ],
      "description": "Systematic stockpile volumetric survey, representative sampling, and grade quality verification for graphite-kyanite-gneiss ROM material in Merelani to determine commercial processing viability."
    },
    {
      "id": "beryllium-prospecting-namtumbo",
      "title": "Beryllium Geochemical Prospecting",
      "location": "Namtumbo",
      "size": "30 sq km",
      "client": "Exploration Company",
      "year": "2023",
      "categories": "Exploration, Prospecting",
      "featured": false,
      "images": [
        "images/projects/Beryllium prospecting_ Namtumbo.jpg"
      ],
      "description": "Multi-disciplinary beryllium prospecting campaign in Namtumbo integrating geological traversing, pegmatite zonation mapping, and geochemical sampling."
    },
    {
      "id": "beryllium-namtumbo",
      "title": "Namtumbo Beryllium Assessment",
      "location": "Namtumbo",
      "size": "25 sq km",
      "client": "Private Investor",
      "year": "2023",
      "categories": "Exploration, Geology",
      "featured": false,
      "images": [
        "images/projects/Beryllium Namtumbo.jpg"
      ],
      "description": "Targeted geological assessment and verification sampling of beryllium-bearing occurrences in Namtumbo district to establish licence prospectivity for private investment."
    },
    {
      "id": "dolomite-dodoma",
      "title": "Industrial Dolomite Prospecting",
      "location": "Dodoma",
      "size": "20 sq km",
      "client": "Industrial Minerals Company",
      "year": "2024",
      "categories": "Exploration, Industrial Minerals",
      "featured": false,
      "images": [
        "images/projects/Dolomite prospecting Dodoma.jpg"
      ],
      "description": "Carbonate mapping and chemical purity sampling across dolomite horizons in Dodoma region to evaluate industrial, agricultural, and construction-grade resource potential."
    },
    {
      "id": "quartz-morogoro",
      "title": "High-Purity Quartz Prospecting",
      "location": "Morogoro",
      "size": "22 sq km",
      "client": "Industrial Minerals Company",
      "year": "2024",
      "categories": "Exploration, Industrial Minerals",
      "featured": false,
      "images": [
        "images/projects/Quartz prospecting_Morogoro.jpg"
      ],
      "description": "Field prospecting, vein geometry mapping, and purity assessment of quartz deposits in the Morogoro region for commercial and industrial mineral supply."
    },
    {
      "id": "artisanal-gold-tabora",
      "title": "Artisanal Gold Mining Technical Support",
      "location": "Tabora",
      "size": "15 sq km",
      "client": "Local Mining Cooperative",
      "year": "2024",
      "categories": "Mining, Assessment",
      "featured": false,
      "images": [
        "images/projects/Artisanal gold miners In Tabora.jpg"
      ],
      "description": "Field geological advisory, vein structural tracking, workplace safety assessment, and ore recovery guidance for artisanal gold mining cooperatives in Tabora region."
    },
    {
      "id": "artisanal-miners-morogoro",
      "title": "Small-Scale Mining Advisory & Training",
      "location": "Morogoro",
      "size": "12 sq km",
      "client": "Mining Community",
      "year": "2024",
      "categories": "Mining, Training",
      "featured": false,
      "images": [
        "images/projects/Artisanal miners_Morogoro.jpg"
      ],
      "description": "Technical site assessment and practical operator training for small-scale miners in Morogoro focused on safe benching, geological ore control, and environmental stewardship."
    }
  ]
};

  function esc(str) {
    return String(str == null ? '' : str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function normalizeProjects(raw) {
    if (raw && Array.isArray(raw.projects)) {
      return raw.projects;
    }
    if (raw && typeof raw === 'object') {
      return Object.keys(raw).map((k) => Object.assign({ id: k }, raw[k]));
    }
    return [];
  }

  async function getProjects() {
    try {
      const res = await fetch('data/projects.json');
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const data = await res.json();
      return normalizeProjects(data);
    } catch (_e) {
      return normalizeProjects(FALLBACK_DATA);
    }
  }

  function primaryBadge(categoriesStr) {
    const parts = String(categoriesStr || 'Exploration')
      .split(',')
      .map((s) => s.trim())
      .filter(Boolean);
    return parts[0] || 'Exploration';
  }

  function matchesCategory(project, filter) {
    if (!filter || filter === 'all') return true;
    const hay = String(project.categories || '').toLowerCase();
    return hay.includes(filter.toLowerCase());
  }

  function renderProjectCard(project) {
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
  }

  async function init() {
    const homeGrid = document.getElementById('featured-projects-grid');
    const catalogGrid = document.getElementById('projects-catalog-grid');
    const detailRoot = document.getElementById('project-detail-root');

    if (!homeGrid && !catalogGrid && !detailRoot) return;
    const projects = await getProjects();

    /* A. Home Featured Grid (3 flagship projects) */
    if (homeGrid) {
      let featured = projects.filter((p) => p.featured);
      if (featured.length < 3) {
        const ids = new Set(featured.map((p) => p.id));
        projects.forEach((p) => {
          if (featured.length < 3 && !ids.has(p.id)) featured.push(p);
        });
      } else {
        featured = featured.slice(0, 3);
      }
      homeGrid.innerHTML = featured.map(renderProjectCard).join('');
    }

    /* B. Full Filterable Projects Page */
    if (catalogGrid) {
      const filterBtns = Array.from(document.querySelectorAll('[data-project-filter]'));
      const countEl = document.getElementById('projects-count');
      const params = new URLSearchParams(window.location.search);
      let activeFilter = (params.get('category') || 'all').toLowerCase();

      function applyFilter(filterKey, pushUrl) {
        activeFilter = filterKey;
        filterBtns.forEach((btn) => {
          const isMatch = btn.getAttribute('data-project-filter') === filterKey;
          btn.classList.toggle('is-active', isMatch);
          btn.setAttribute('aria-pressed', String(isMatch));
        });
        const filtered = projects.filter((p) => matchesCategory(p, filterKey));
        catalogGrid.innerHTML = filtered.map(renderProjectCard).join('');
        if (countEl) {
          countEl.textContent = filtered.length + (filtered.length === 1 ? ' project' : ' projects');
        }
        if (pushUrl && window.history && window.history.replaceState) {
          const url = new URL(window.location.href);
          if (filterKey === 'all') url.searchParams.delete('category');
          else url.searchParams.set('category', filterKey);
          window.history.replaceState({}, '', url.toString());
        }
      }

      filterBtns.forEach((btn) => {
        btn.addEventListener('click', () => {
          applyFilter(btn.getAttribute('data-project-filter') || 'all', true);
        });
      });
      applyFilter(activeFilter, false);
    }

    /* C. Single Project Case Study Page */
    if (detailRoot) {
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
      if (relatedGrid) {
        const mainCat = catTags[0] || 'Exploration';
        let related = projects.filter((p) => p.id !== project.id && matchesCategory(p, mainCat));
        if (related.length < 3) {
          const used = new Set(related.map((p) => p.id));
          used.add(project.id);
          projects.forEach((p) => {
            if (related.length < 3 && !used.has(p.id)) related.push(p);
          });
        }
        relatedGrid.innerHTML = related.slice(0, 3).map(renderProjectCard).join('');
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
