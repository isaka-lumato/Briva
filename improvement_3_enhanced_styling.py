with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add enhanced specs styling CSS
enhanced_specs_css = '''
        /* ============================================
           ENHANCED SPECS & FEATURES STYLING
        ============================================ */
        .specs-card {
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
            border: 1px solid rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }

        .specs-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        }

        .specs-card h3 {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .specs-card h3 i {
            color: #ffb600;
            font-size: 1.3rem;
        }

        .spec-item {
            position: relative;
            padding: 15px 0;
            transition: all 0.3s ease;
        }

        .spec-item:hover {
            background: rgba(255, 182, 0, 0.05);
            padding-left: 10px;
            margin-left: -10px;
            margin-right: -10px;
            padding-right: 10px;
            border-radius: 5px;
        }

        .spec-label {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .spec-label::before {
            content: '';
            width: 8px;
            height: 8px;
            background: linear-gradient(135deg, #ffb600, #ff9500);
            border-radius: 50%;
            flex-shrink: 0;
        }

        .spec-value {
            font-weight: 600;
            color: #ffb600;
        }

        /* Features list enhanced styling */
        .features-list li {
            transition: all 0.3s ease;
            border-radius: 5px;
            margin-bottom: 5px;
        }

        .features-list li:hover {
            background: rgba(255, 182, 0, 0.08);
            padding-left: 45px;
            color: #212121;
        }

        .features-list li::before {
            transition: all 0.3s ease;
        }

        .features-list li:hover::before {
            transform: scale(1.2);
        }

        /* Icon badges for Applications section */
        .app-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 35px;
            height: 35px;
            background: linear-gradient(135deg, #ffb600 0%, #ff9500 100%);
            border-radius: 8px;
            margin-right: 12px;
            color: #fff;
            font-size: 1rem;
            flex-shrink: 0;
        }

        /* Floating animation for main product image */
        @keyframes float {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }

        .equipment-main-image {
            animation: float 4s ease-in-out infinite;
        }

        .equipment-main-image:hover {
            animation-play-state: paused;
        }

        /* Thumbnail glow effect */
        .equipment-thumbnail {
            position: relative;
        }

        .equipment-thumbnail::after {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 8px;
            opacity: 0;
            transition: opacity 0.3s ease;
            background: linear-gradient(135deg, rgba(255, 182, 0, 0.3), transparent);
        }

        .equipment-thumbnail:hover::after {
            opacity: 1;
        }
'''

# Insert before scroll reveal CSS
content = content.replace(
    '        /* ============================================\n           SCROLL REVEAL ANIMATIONS',
    enhanced_specs_css + '\n        /* ============================================\n           SCROLL REVEAL ANIMATIONS'
)

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Improvement #3: Enhanced Specs & Features Styling added!")
print("   - Gradient backgrounds on cards")
print("   - Hover effects on spec items and features")
print("   - Floating animation on main product image")
print("   - Glow effect on thumbnails")
print("   - Card lift effect on hover")
