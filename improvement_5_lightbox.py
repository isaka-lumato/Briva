with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add lightbox CSS
lightbox_css = '''
        /* ============================================
           IMAGE LIGHTBOX GALLERY
        ============================================ */
        .lightbox-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            z-index: 9999;
            display: none;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .lightbox-overlay.active {
            display: flex;
            opacity: 1;
        }

        .lightbox-content {
            max-width: 90%;
            max-height: 90%;
            position: relative;
        }

        .lightbox-image {
            max-width: 100%;
            max-height: 85vh;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            transform: scale(0.9);
            transition: transform 0.3s ease;
        }

        .lightbox-overlay.active .lightbox-image {
            transform: scale(1);
        }

        .lightbox-close {
            position: absolute;
            top: -50px;
            right: 0;
            width: 40px;
            height: 40px;
            background: #ffb600;
            border: none;
            border-radius: 50%;
            color: #fff;
            font-size: 24px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }

        .lightbox-close:hover {
            background: #ff9500;
            transform: rotate(90deg);
        }

        .lightbox-caption {
            text-align: center;
            color: #fff;
            margin-top: 20px;
            font-size: 1.1rem;
        }

        /* Make thumbnails clickable */
        .equipment-thumbnail,
        .equipment-main-image {
            cursor: zoom-in;
        }
'''

# Insert before staggered CSS
content = content.replace(
    '        /* ============================================\n           STAGGERED LIST',
    lightbox_css + '\n        /* ============================================\n           STAGGERED LIST'
)

# 2. Add lightbox HTML before </body>
lightbox_html = '''
    <!-- Lightbox Overlay -->
    <div class="lightbox-overlay" id="lightboxOverlay">
        <div class="lightbox-content">
            <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
            <img src="" alt="" class="lightbox-image" id="lightboxImage">
            <p class="lightbox-caption" id="lightboxCaption"></p>
        </div>
    </div>

    <script>
        // Staggered List Animation'''

content = content.replace(
    '<script>\n        // Staggered List Animation',
    lightbox_html
)

# 3. Add lightbox JavaScript
lightbox_js = '''
    <script>
        // Image Lightbox Gallery
        function openLightbox(src, alt) {
            const overlay = document.getElementById('lightboxOverlay');
            const image = document.getElementById('lightboxImage');
            const caption = document.getElementById('lightboxCaption');
            
            image.src = src;
            caption.textContent = alt;
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeLightbox() {
            const overlay = document.getElementById('lightboxOverlay');
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }

        // Close on overlay click
        document.getElementById('lightboxOverlay').addEventListener('click', function(e) {
            if (e.target === this) {
                closeLightbox();
            }
        });

        // Close on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeLightbox();
            }
        });

        // Make all equipment images clickable
        document.querySelectorAll('.equipment-main-image, .equipment-thumbnail').forEach(img => {
            img.addEventListener('click', function() {
                openLightbox(this.src, this.alt);
            });
        });
    </script>

    <!-- Lightbox Overlay -->'''

content = content.replace(
    '<!-- Lightbox Overlay -->',
    lightbox_js
)

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Improvement #5: Image Lightbox Gallery added!")
print("   - Click any product image to open fullscreen")
print("   - Smooth zoom animation")
print("   - Close with X button, click outside, or Escape key")
print("   - Image captions from alt text")
