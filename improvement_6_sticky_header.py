with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add sticky header CSS
sticky_css = '''
        /* ============================================
           STICKY NAVIGATION HEADER
        ============================================ */
        .header-one {
            transition: all 0.3s ease;
        }

        .header-sticky {
            position: fixed !important;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background: #fff;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            animation: slideDown 0.3s ease;
        }

        .header-sticky .bg-white {
            padding: 5px 0;
        }

        .header-sticky .logo img {
            width: 100px;
            height: auto;
        }

        @keyframes slideDown {
            from {
                transform: translateY(-100%);
            }
            to {
                transform: translateY(0);
            }
        }

        /* Add padding to body when header is sticky */
        body.has-sticky-header {
            padding-top: 0;
        }

        /* Hide top bar when sticky */
        .header-sticky + .top-bar,
        body.has-sticky-header .top-bar {
            display: none;
        }
'''

# Insert before lightbox CSS
content = content.replace(
    '        /* ============================================\n           IMAGE LIGHTBOX',
    sticky_css + '\n        /* ============================================\n           IMAGE LIGHTBOX'
)

# 2. Add sticky header JavaScript
sticky_js = '''
    <script>
        // Sticky Navigation Header
        const header = document.querySelector('.header-one');
        const headerOffset = header ? header.offsetTop : 0;

        function handleStickyHeader() {
            if (window.pageYOffset > headerOffset + 100) {
                header.classList.add('header-sticky');
                document.body.classList.add('has-sticky-header');
            } else {
                header.classList.remove('header-sticky');
                document.body.classList.remove('has-sticky-header');
            }
        }

        window.addEventListener('scroll', handleStickyHeader);
    </script>

    <script>
        // Image Lightbox Gallery'''

content = content.replace(
    '<script>\n        // Image Lightbox Gallery',
    sticky_js
)

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Improvement #6: Sticky Navigation Header added!")
print("   - Header becomes fixed when scrolling down")
print("   - Smooth slide-down animation")
print("   - Compact design when sticky")
print("   - Shadow effect for depth")
