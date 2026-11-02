/* ==========================================================================
   BRIVA EXPLORATION & MINING — CORE UI INTERACTIONS (Vanilla ES6)
   ========================================================================== */

(function () {
  'use strict';

  /* 1. Dynamic Copyright Year */
  document.querySelectorAll('[data-year]').forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });

  /* 2. Sticky Header Shadow on Scroll */
  const header = document.querySelector('.site-header');
  if (header) {
    const syncHeader = () => {
      header.classList.toggle('is-scrolled', window.scrollY > 14);
    };
    window.addEventListener('scroll', syncHeader, { passive: true });
    syncHeader();
  }

  /* 3. Accessible Mobile Navigation Drawer */
  const drawer = document.getElementById('mobile-drawer');
  const openBtn = document.querySelector('[data-nav-open]');
  const closeBtns = document.querySelectorAll('[data-nav-close]');

  function setDrawer(open) {
    if (!drawer || !openBtn) return;
    drawer.classList.toggle('is-open', open);
    drawer.setAttribute('aria-hidden', String(!open));
    openBtn.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('nav-open', open);
  }

  if (openBtn && drawer) {
    openBtn.addEventListener('click', () => setDrawer(true));
    closeBtns.forEach((btn) => btn.addEventListener('click', () => setDrawer(false)));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) {
        setDrawer(false);
        openBtn.focus();
      }
    });
  }

  /* 4. Subtle Scroll Reveal (respects prefers-reduced-motion) */
  const revealEls = document.querySelectorAll('[data-reveal]');
  if (revealEls.length > 0) {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduced || !('IntersectionObserver' in window)) {
      revealEls.forEach((el) => el.classList.add('is-visible'));
    } else {
      const io = new IntersectionObserver(
        (entries, obs) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('is-visible');
              obs.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
      );
      revealEls.forEach((el) => io.observe(el));
    }
  }

  /* 5. Accessible Tabs (Equipment Detail & Technical Panels) */
  document.querySelectorAll('[data-tabs]').forEach((tabRoot) => {
    const buttons = Array.from(tabRoot.querySelectorAll('[role="tab"]'));
    const panels = Array.from(tabRoot.querySelectorAll('[role="tabpanel"]'));

    function activateTab(targetBtn) {
      buttons.forEach((btn) => {
        const active = btn === targetBtn;
        btn.setAttribute('aria-selected', String(active));
        btn.tabIndex = active ? 0 : -1;
      });
      panels.forEach((panel) => {
        panel.hidden = panel.id !== targetBtn.getAttribute('aria-controls');
      });
    }

    buttons.forEach((btn, idx) => {
      btn.addEventListener('click', () => activateTab(btn));
      btn.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
          e.preventDefault();
          const dir = e.key === 'ArrowRight' ? 1 : -1;
          const next = buttons[(idx + dir + buttons.length) % buttons.length];
          next.focus();
          activateTab(next);
        }
      });
    });
  });

  /* 6. Native <dialog> Image Lightbox */
  let dialog = document.getElementById('site-lightbox');
  function openLightbox(src, alt) {
    if (!src) return;
    if (!dialog) {
      dialog = document.createElement('dialog');
      dialog.id = 'site-lightbox';
      dialog.className = 'lightbox-dialog';
      dialog.innerHTML =
        '<div class="lightbox-dialog__inner">' +
        '<button type="button" class="lightbox-dialog__close" aria-label="Close image preview">&times;</button>' +
        '<img src="" alt="">' +
        '</div>';
      document.body.appendChild(dialog);
      dialog.querySelector('.lightbox-dialog__close').addEventListener('click', () => dialog.close());
      dialog.addEventListener('click', (e) => {
        if (e.target === dialog) dialog.close();
      });
    }
    const img = dialog.querySelector('img');
    img.src = src;
    img.alt = alt || 'Image preview';
    if (typeof dialog.showModal === 'function') {
      dialog.showModal();
    }
  }

  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-lightbox]');
    if (!trigger) return;
    e.preventDefault();
    const img = trigger.querySelector('img');
    const src = trigger.getAttribute('data-lightbox') || (img && img.getAttribute('src'));
    const alt = (img && img.getAttribute('alt')) || trigger.getAttribute('aria-label') || '';
    openLightbox(src, alt);
  });

  /* 7. Contact Form Smart Query Prefill & Formspree Submission */
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    const params = new URLSearchParams(window.location.search);
    const product = params.get('product');
    const type = params.get('type');
    const service = params.get('service');
    const subjectSelect = contactForm.querySelector('[name="subject"]');
    const messageField = contactForm.querySelector('[name="message"]');

    const productNames = {
      megascan: 'Mega Scan Pro Geophysical Scanner',
      pinpointer: 'Gold Pin Pointer Detector',
    };
    const serviceNames = {
      'geological-exploration': 'Geological & Exploration Services',
      'resource-estimation': 'Resource Estimation & 3D Modelling',
      'mine-planning': 'Mining Engineering, Planning & Compliance',
      'drilling-supervision': 'Drilling Supervision & Project Management',
      'asm-support': 'Artisanal & Small-Scale Mining (ASM) Support',
      'ma-advisory': 'M&A, Joint Ventures & Economic Advisory',
    };

    if (product && subjectSelect) {
      const pName = productNames[product] || product;
      subjectSelect.value = type === 'rent' ? 'Equipment Rental Enquiry' : 'Equipment Purchase Quote';
      if (messageField && !messageField.value) {
        messageField.value =
          type === 'rent'
            ? `Hello Briva Team, I would like to enquire about rental availability and rates for the ${pName}.`
            : `Hello Briva Team, please share a formal quotation and delivery lead time for purchasing the ${pName}.`;
      }
    } else if (type === 'equipment' && subjectSelect) {
      subjectSelect.value = 'Equipment Purchase Quote';
    } else if (service && subjectSelect) {
      const sName = serviceNames[service] || service;
      const mapOption = {
        'geological-exploration': 'Geological & Exploration Consulting',
        'resource-estimation': 'Resource Estimation & Mine Planning',
        'mine-planning': 'Resource Estimation & Mine Planning',
        'drilling-supervision': 'Drilling Supervision',
        'asm-support': 'ASM Support / M&A Advisory',
        'ma-advisory': 'ASM Support / M&A Advisory',
      };
      if (mapOption[service]) subjectSelect.value = mapOption[service];
      if (messageField && !messageField.value) {
        messageField.value = `Hello Briva Team, we would like to discuss a potential engagement regarding ${sName}.`;
      }
    }

    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const submitBtn = document.getElementById('contact-submit');
      const successBox = document.getElementById('contact-success');
      const errorBox = document.getElementById('contact-error');
      const defaultLabel = submitBtn ? submitBtn.textContent : 'Send Enquiry';

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending Enquiry...';
      }
      if (successBox) successBox.hidden = true;
      if (errorBox) errorBox.hidden = true;

      try {
        const res = await fetch(contactForm.action, {
          method: contactForm.method || 'POST',
          body: new FormData(contactForm),
          headers: { Accept: 'application/json' },
        });
        if (res.ok) {
          contactForm.reset();
          if (successBox) {
            successBox.hidden = false;
            successBox.focus();
          }
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = defaultLabel;
          }
        } else {
          const data = await res.json().catch(() => ({}));
          const msg =
            data && Array.isArray(data.errors)
              ? data.errors.map((err) => err.message).join(', ')
              : 'We could not submit your message right now. Please email info@briva.co.tz or call +255 767 413 950.';
          if (errorBox) {
            errorBox.textContent = msg;
            errorBox.hidden = false;
          }
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = defaultLabel;
          }
        }
      } catch (_err) {
        if (errorBox) {
          errorBox.textContent =
            'Network error while sending your enquiry. Please email info@briva.co.tz or call +255 767 413 950.';
          errorBox.hidden = false;
        }
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = defaultLabel;
        }
      }
    });
  }
})();
