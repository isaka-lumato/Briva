with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add responsive pricing CSS
responsive_pricing_css = '''
        /* ============================================
           RESPONSIVE PRICING FIXES
        ============================================ */
        @media (max-width: 991px) {
            .pricing-highlight {
                padding: 40px 20px;
            }

            .pricing-highlight h3 {
                font-size: 1.2rem;
                letter-spacing: 1px;
            }

            .price-tag {
                font-size: 2.5rem !important;
            }

            .price-tag sup {
                font-size: 1rem !important;
            }

            .price-label {
                font-size: 1rem !important;
            }

            .price-sublabel {
                font-size: 0.9rem !important;
            }

            .trust-badges {
                margin-top: 30px;
            }
        }

        @media (max-width: 575px) {
            .pricing-highlight {
                padding: 30px 15px;
            }

            .pricing-highlight h3 {
                font-size: 1rem;
                letter-spacing: 0.5px;
            }

            .price-tag {
                font-size: 2rem !important;
                word-break: break-all;
            }

            .price-tag sup {
                font-size: 0.85rem !important;
            }

            .price-label {
                font-size: 0.9rem !important;
            }

            .price-sublabel {
                font-size: 0.8rem !important;
            }

            .trust-badge {
                padding: 12px 15px;
            }

            .trust-badge-icon {
                width: 40px;
                height: 40px;
            }

            .trust-badge-icon i {
                font-size: 1.2rem;
            }

            .trust-badge-text h5 {
                font-size: 0.9rem;
            }

            .trust-badge-text p {
                font-size: 0.75rem;
            }

            .secure-payment {
                padding: 12px;
                font-size: 0.85rem;
            }
        }

        /* Ensure price doesn't overflow */
        .price-wrapper {
            overflow: hidden;
            padding: 0 10px;
        }

        .price-tag {
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
'''

# Insert before the closing style tag (find the last occurrence)
# Insert after CTA button pulse animation
content = content.replace(
    '        /* ============================================\n           SCROLL REVEAL ANIMATIONS',
    responsive_pricing_css + '\n        /* ============================================\n           SCROLL REVEAL ANIMATIONS'
)

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Responsive Pricing Fixes added!")
print("   - Price scales down on tablets (2.5rem)")
print("   - Price scales down on mobile (2rem)")
print("   - All text elements responsive")
print("   - Trust badges adjust for mobile")
print("   - Prevents number overflow/trimming")
