with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add enhanced scroll-to-top CSS
scroll_top_css = '''
        /* ============================================
           ENHANCED SCROLL-TO-TOP BUTTON
        ============================================ */
        #back-to-top {
            position: fixed !important;
            bottom: 30px;
            right: 30px;
            z-index: 999;
            opacity: 0;
            visibility: hidden;
            transform: translateY(20px);
            transition: all 0.3s ease;
        }

        #back-to-top.visible {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }

        #back-to-top .btn {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #ffb600 0%, #ff9500 100%);
            border: none;
            box-shadow: 0 5px 20px rgba(255, 182, 0, 0.4);
            transition: all 0.3s ease;
        }

        #back-to-top .btn:hover {
            transform: translateY(-5px) scale(1.1);
            box-shadow: 0 10px 30px rgba(255, 182, 0, 0.5);
        }

        #back-to-top .btn i {
            font-size: 1.2rem;
            animation: bounce-arrow 1.5s infinite;
        }

        @keyframes bounce-arrow {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-5px);
            }
        }

        /* Progress ring around button */
        .scroll-progress {
            position: absolute;
            top: -5px;
            left: -5px;
            width: 60px;
            height: 60px;
        }

        .scroll-progress svg {
            transform: rotate(-90deg);
        }

        .scroll-progress circle {
            fill: none;
            stroke-width: 3;
            stroke-linecap: round;
        }

        .scroll-progress .bg {
            stroke: rgba(255, 182, 0, 0.2);
        }

        .scroll-progress .progress {
            stroke: #ffb600;
            stroke-dasharray: 176;
            stroke-dashoffset: 176;
            transition: stroke-dashoffset 0.1s linear;
        }
'''

# Insert before sticky header CSS
content = content.replace(
    '        /* ============================================\n           STICKY NAVIGATION',
    scroll_top_css + '\n        /* ============================================\n           STICKY NAVIGATION'
)

# 2. Update the back-to-top button HTML
old_back_to_top = '''<div id="back-to-top" data-spy="affix" data-offset-top="10" class="back-to-top position-fixed">
                        <button class="btn btn-primary" title="Back to Top">
                            <i class="fa fa-angle-double-up"></i>
                        </button>
                    </div>'''

new_back_to_top = '''<div id="back-to-top" class="back-to-top">
                        <div class="scroll-progress">
                            <svg viewBox="0 0 60 60">
                                <circle class="bg" cx="30" cy="30" r="28"></circle>
                                <circle class="progress" id="scrollProgress" cx="30" cy="30" r="28"></circle>
                            </svg>
                        </div>
                        <button class="btn btn-primary" title="Back to Top" onclick="scrollToTop()">
                            <i class="fa fa-angle-double-up"></i>
                        </button>
                    </div>'''

content = content.replace(old_back_to_top, new_back_to_top)

# 3. Add scroll-to-top JavaScript
scroll_top_js = '''
    <script>
        // Enhanced Scroll-to-Top with Progress
        const backToTop = document.getElementById('back-to-top');
        const scrollProgress = document.getElementById('scrollProgress');
        const circumference = 2 * Math.PI * 28; // radius = 28

        function updateScrollProgress() {
            const scrollTop = window.pageYOffset;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPercent = scrollTop / docHeight;
            
            // Show/hide button
            if (scrollTop > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }

            // Update progress ring
            if (scrollProgress) {
                const offset = circumference - (scrollPercent * circumference);
                scrollProgress.style.strokeDashoffset = offset;
            }
        }

        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        window.addEventListener('scroll', updateScrollProgress);
        window.addEventListener('load', updateScrollProgress);
    </script>

    <script>
        // Sticky Navigation Header'''

content = content.replace(
    '<script>\n        // Sticky Navigation Header',
    scroll_top_js
)

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Improvement #7: Enhanced Scroll-to-Top Button added!")
print("   - Circular progress ring showing scroll position")
print("   - Bouncing arrow animation")
print("   - Smooth fade-in on scroll")
print("   - Hover lift effect")
