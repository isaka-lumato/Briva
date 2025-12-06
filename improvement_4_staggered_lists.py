with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add staggered animation CSS
staggered_css = '''
        /* ============================================
           STAGGERED LIST ANIMATIONS
        ============================================ */
        .stagger-item {
            opacity: 0;
            transform: translateX(-20px);
            transition: all 0.5s cubic-bezier(0.5, 0, 0, 1);
        }

        .stagger-item.active {
            opacity: 1;
            transform: translateX(0);
        }

        .stagger-item:nth-child(1) { transition-delay: 0.1s; }
        .stagger-item:nth-child(2) { transition-delay: 0.15s; }
        .stagger-item:nth-child(3) { transition-delay: 0.2s; }
        .stagger-item:nth-child(4) { transition-delay: 0.25s; }
        .stagger-item:nth-child(5) { transition-delay: 0.3s; }
        .stagger-item:nth-child(6) { transition-delay: 0.35s; }
        .stagger-item:nth-child(7) { transition-delay: 0.4s; }
        .stagger-item:nth-child(8) { transition-delay: 0.45s; }
'''

# Insert before enhanced specs CSS
content = content.replace(
    '        /* ============================================\n           ENHANCED SPECS',
    staggered_css + '\n        /* ============================================\n           ENHANCED SPECS'
)

# 2. Add stagger class to Applications list items
applications_items = [
    '<li>Gold and precious metal detection</li>',
    '<li>Mineral deposit exploration</li>',
    '<li>Archaeological treasure hunting</li>',
    '<li>Underground cavity detection</li>',
    '<li>Diamond and gemstone prospecting</li>',
    '<li>Subsurface geological mapping</li>'
]

for item in applications_items:
    content = content.replace(item, item.replace('<li>', '<li class="stagger-item">'))

# 3. Add stagger class to What's Included list items
included_items = [
    '<li>Mega Scan Pro main unit</li>',
    '<li>I.M.T.U Probe (Multi Transceiver)</li>',
    '<li>V.S.T Probe (Vertical Signal Transceiver)</li>',
    '<li>Long Range Search Antennas</li>',
    '<li>Rechargeable Li-Ion Battery Pack</li>',
    '<li>Multi Visual Analyzer App</li>',
    '<li>Waterproof Protective Hardcase</li>',
    '<li>Complete User Manual & Training</li>'
]

for item in included_items:
    content = content.replace(item, item.replace('<li>', '<li class="stagger-item">'))

# 4. Add staggered animation JavaScript
stagger_js = '''
    <script>
        // Staggered List Animation
        function animateStaggerItems() {
            const containers = document.querySelectorAll('.features-list');
            
            containers.forEach(container => {
                const rect = container.getBoundingClientRect();
                const items = container.querySelectorAll('.stagger-item:not(.active)');
                
                if (rect.top < window.innerHeight - 100) {
                    items.forEach(item => {
                        item.classList.add('active');
                    });
                }
            });
        }

        window.addEventListener('scroll', animateStaggerItems);
        window.addEventListener('load', animateStaggerItems);
    </script>

    <script>
        // Price Counter Animation'''

content = content.replace(
    '<script>\n        // Price Counter Animation',
    stagger_js
)

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Improvement #4: Staggered List Animations added!")
print("   - Applications items animate in sequence")
print("   - What's Included items animate in sequence")
print("   - Smooth slide-in effect with delays")
