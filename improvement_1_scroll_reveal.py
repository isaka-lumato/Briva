with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add scroll reveal CSS styles before </style>
scroll_reveal_css = '''
        /* ============================================
           SCROLL REVEAL ANIMATIONS
        ============================================ */
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s cubic-bezier(0.5, 0, 0, 1);
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }

        .reveal-left {
            opacity: 0;
            transform: translateX(-50px);
            transition: all 0.8s cubic-bezier(0.5, 0, 0, 1);
        }

        .reveal-left.active {
            opacity: 1;
            transform: translateX(0);
        }

        .reveal-right {
            opacity: 0;
            transform: translateX(50px);
            transition: all 0.8s cubic-bezier(0.5, 0, 0, 1);
        }

        .reveal-right.active {
            opacity: 1;
            transform: translateX(0);
        }

        .reveal-scale {
            opacity: 0;
            transform: scale(0.9);
            transition: all 0.8s cubic-bezier(0.5, 0, 0, 1);
        }

        .reveal-scale.active {
            opacity: 1;
            transform: scale(1);
        }

        /* Staggered delay classes */
        .delay-1 { transition-delay: 0.1s; }
        .delay-2 { transition-delay: 0.2s; }
        .delay-3 { transition-delay: 0.3s; }
        .delay-4 { transition-delay: 0.4s; }
        .delay-5 { transition-delay: 0.5s; }
    </style>'''

content = content.replace('    </style>', scroll_reveal_css)

# 2. Add scroll reveal JavaScript before </body>
scroll_reveal_js = '''
    <script>
        // Scroll Reveal Animation
        function revealOnScroll() {
            const reveals = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
            
            reveals.forEach(element => {
                const windowHeight = window.innerHeight;
                const elementTop = element.getBoundingClientRect().top;
                const elementVisible = 150;
                
                if (elementTop < windowHeight - elementVisible) {
                    element.classList.add('active');
                }
            });
        }

        window.addEventListener('scroll', revealOnScroll);
        window.addEventListener('load', revealOnScroll);
    </script>

    </div><!-- Body inner end -->
</body>'''

content = content.replace('    </div><!-- Body inner end -->\n</body>', scroll_reveal_js)

# 3. Add reveal classes to key sections
# Equipment image gallery
content = content.replace(
    '<div class="equipment-image-gallery">',
    '<div class="equipment-image-gallery reveal-left">'
)

# Specs card
content = content.replace(
    '<div class="specs-card">',
    '<div class="specs-card reveal-right">',
    1  # Only first occurrence
)

# Features card (second specs-card)
content = content.replace(
    '<div class="specs-card reveal-right">',
    '<div class="specs-card reveal-right">',
    1
)

# Video section
content = content.replace(
    '<h2 class="section-title-equipment">Equipment in Action</h2>',
    '<h2 class="section-title-equipment reveal">Equipment in Action</h2>'
)

# Pricing section
content = content.replace(
    '<div class="pricing-highlight">',
    '<div class="pricing-highlight reveal-scale">'
)

# Download section
content = content.replace(
    '<div class="download-section">',
    '<div class="download-section reveal">'
)

# Applications title
content = content.replace(
    '<h2 class="section-title-equipment">Applications</h2>',
    '<h2 class="section-title-equipment reveal">Applications</h2>'
)

# What's Included title
content = content.replace(
    '<h2 class="section-title-equipment">What\'s Included</h2>',
    '<h2 class="section-title-equipment reveal">What\'s Included</h2>'
)

# Contact CTA
content = content.replace(
    '<section class="contact-cta">',
    '<section class="contact-cta reveal">'
)

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Improvement #1: Scroll Reveal Animations added!")
print("   - Sections now fade/slide in as you scroll")
print("   - Left/right/scale reveal effects")
print("   - Staggered delay classes available")
