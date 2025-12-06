with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the price display to have counter animation
# Find and replace the price tag
old_price = '''<div class="price-tag">
                                        <sup>TZS</sup> 450,000,000
                                    </div>'''

new_price = '''<div class="price-tag">
                                        <sup>TZS</sup> <span class="counter" data-target="450000000">0</span>
                                    </div>'''

content = content.replace(old_price, new_price)

# 2. Add counter animation CSS
counter_css = '''
        /* ============================================
           PRICE COUNTER ANIMATION
        ============================================ */
        .counter {
            display: inline-block;
        }

        .price-tag .counter {
            background: linear-gradient(135deg, #fff 0%, #f0f0f0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Animated gradient shimmer on price */
        @keyframes shimmer {
            0% {
                background-position: -200% 0;
            }
            100% {
                background-position: 200% 0;
            }
        }

        .price-shimmer {
            background: linear-gradient(
                90deg,
                #fff 0%,
                #ffb600 25%,
                #fff 50%,
                #ffb600 75%,
                #fff 100%
            );
            background-size: 200% 100%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 3s linear infinite;
        }
    </style>'''

# Insert before existing </style> (which now has scroll reveal before it)
content = content.replace('        /* ============================================\n           SCROLL REVEAL ANIMATIONS', 
                          counter_css.replace('    </style>', '') + '\n        /* ============================================\n           SCROLL REVEAL ANIMATIONS')

# 3. Add counter JavaScript
counter_js = '''
    <script>
        // Price Counter Animation
        function formatNumber(num) {
            return num.toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, ",");
        }

        function animateCounter(element) {
            const target = parseInt(element.getAttribute('data-target'));
            const duration = 2000; // 2 seconds
            const step = target / (duration / 16); // 60fps
            let current = 0;

            const timer = setInterval(() => {
                current += step;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                    // Add shimmer effect after counting finishes
                    element.classList.add('price-shimmer');
                }
                element.textContent = formatNumber(Math.floor(current));
            }, 16);
        }

        // Trigger counter when pricing section is visible
        function checkCounterVisibility() {
            const counters = document.querySelectorAll('.counter:not(.counted)');
            counters.forEach(counter => {
                const rect = counter.getBoundingClientRect();
                if (rect.top < window.innerHeight && rect.bottom > 0) {
                    counter.classList.add('counted');
                    animateCounter(counter);
                }
            });
        }

        window.addEventListener('scroll', checkCounterVisibility);
        window.addEventListener('load', checkCounterVisibility);
    </script>

    <script>'''

# Insert before the scroll reveal script
content = content.replace('<script>\n        // Scroll Reveal Animation', counter_js + '\n        // Scroll Reveal Animation')

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Improvement #2: Price Counter Animation added!")
print("   - Price counts up from 0 to 450,000,000")
print("   - Shimmer effect after counting completes")
print("   - Number formatting with commas")
