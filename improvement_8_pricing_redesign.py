with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add new pricing section styling
pricing_css = '''
        /* ============================================
           REDESIGNED PRICING SECTION
        ============================================ */
        .pricing-highlight {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
            padding: 60px 40px;
            border-radius: 20px;
            margin: 50px 0;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 182, 0, 0.2);
        }

        .pricing-highlight::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #ffb600, #ff9500, #ffb600);
            background-size: 200% 100%;
            animation: gradient-slide 3s ease infinite;
        }

        @keyframes gradient-slide {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .pricing-highlight h3 {
            font-size: 1.5rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 40px;
        }

        .price-wrapper {
            text-align: center;
        }

        .price-tag {
            font-size: 4rem;
            font-weight: 800;
            color: #fff;
            margin: 0;
            line-height: 1.2;
            position: relative;
            z-index: 1;
        }

        .price-tag sup {
            font-size: 1.5rem;
            font-weight: 600;
            color: #ffb600;
            vertical-align: super;
            margin-right: 5px;
        }

        .price-label {
            color: #ffb600;
            font-size: 1.3rem;
            font-weight: 600;
            margin-top: 10px;
        }

        .price-sublabel {
            color: rgba(255, 255, 255, 0.7);
            font-size: 1.1rem;
            margin-top: 10px;
        }

        .price-sublabel strong {
            color: #ffb600;
        }

        /* Right side - Trust badges instead of ugly logo */
        .trust-badges {
            display: flex;
            flex-direction: column;
            gap: 20px;
            padding: 20px;
        }

        .trust-badge {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 15px 20px;
            background: rgba(255, 182, 0, 0.1);
            border-radius: 12px;
            border: 1px solid rgba(255, 182, 0, 0.2);
            transition: all 0.3s ease;
        }

        .trust-badge:hover {
            background: rgba(255, 182, 0, 0.15);
            transform: translateX(5px);
            border-color: rgba(255, 182, 0, 0.4);
        }

        .trust-badge-icon {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #ffb600, #ff9500);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .trust-badge-icon i {
            font-size: 1.5rem;
            color: #fff;
        }

        .trust-badge-text h5 {
            color: #fff;
            font-size: 1rem;
            margin: 0 0 5px 0;
            font-weight: 600;
        }

        .trust-badge-text p {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.85rem;
            margin: 0;
        }

        .secure-payment {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-top: 30px;
            padding: 15px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }

        .secure-payment i {
            color: #28a745;
            font-size: 1.2rem;
        }

        .secure-payment span {
            color: rgba(255, 255, 255, 0.9);
            font-size: 0.95rem;
        }

        /* ============================================
           CTA BUTTON PULSE ANIMATION
        ============================================ */
        .btn-pulse {
            position: relative;
            animation: btn-pulse-glow 2s ease-in-out infinite;
        }

        @keyframes btn-pulse-glow {
            0%, 100% {
                box-shadow: 0 0 0 0 rgba(255, 182, 0, 0.7);
            }
            50% {
                box-shadow: 0 0 0 15px rgba(255, 182, 0, 0);
            }
        }

        .btn-primary {
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .btn-primary::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(255, 255, 255, 0.3),
                transparent
            );
            transition: left 0.5s ease;
        }

        .btn-primary:hover::before {
            left: 100%;
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(255, 182, 0, 0.4);
        }

        .contact-cta .btn {
            padding: 15px 40px;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 50px;
            margin: 10px;
        }

        .contact-cta .btn-primary {
            background: linear-gradient(135deg, #ffb600 0%, #ff9500 100%);
            border: none;
        }

        .contact-cta .btn-dark {
            background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
            border: 2px solid #ffb600;
        }

        .contact-cta .btn-dark:hover {
            background: linear-gradient(135deg, #ffb600 0%, #ff9500 100%);
            border-color: transparent;
        }
'''

# Insert before scroll-to-top CSS
content = content.replace(
    '        /* ============================================\n           ENHANCED SCROLL-TO-TOP',
    pricing_css + '\n        /* ============================================\n           ENHANCED SCROLL-TO-TOP'
)

# 2. Replace the pricing section HTML
old_pricing_html = '''<!-- Pricing Section -->
                <div class="row" id="pricing">
                    <div class="col-12">
                        <div class="pricing-highlight reveal-scale">
                            <h3>Equipment Rental & Purchase</h3>
                            <div class="row align-items-center">
                                <div class="col-lg-6">
                                    <div class="price-tag">
                                        <sup>TZS</sup> <span class="counter" data-target="450000000">0</span>
                                    </div>
                                    <p style="color: #fff; font-size: 1.2rem;">Purchase Price</p>
                                    <p style="color: rgba(255,255,255,0.8);">or Rent from <strong>TZS
                                            2,500,000/month</strong></p>
                                </div>
                                <div class="col-lg-6">
                                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Tanzania_Shillings.jpg/800px-Tanzania_Shillings.jpg"
                                        alt="Tanzanian Shillings" class="currency-note"
                                        onerror="this.src='images/brivaLogo.png'">
                                    <p style="color: rgba(255,255,255,0.9); margin-top: 15px; font-size: 0.9rem;">
                                        <i class="fas fa-shield-alt"></i> Secure payment options available
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

new_pricing_html = '''<!-- Pricing Section -->
                <div class="row" id="pricing">
                    <div class="col-12">
                        <div class="pricing-highlight reveal-scale">
                            <h3 class="text-center"><i class="fas fa-tags" style="color: #ffb600; margin-right: 10px;"></i>Equipment Rental & Purchase</h3>
                            <div class="row align-items-center">
                                <div class="col-lg-6">
                                    <div class="price-wrapper">
                                        <div class="price-tag">
                                            <sup>TZS</sup> <span class="counter" data-target="450000000">0</span>
                                        </div>
                                        <p class="price-label">Purchase Price</p>
                                        <p class="price-sublabel">or Rent from <strong>TZS 2,500,000/month</strong></p>
                                    </div>
                                    <div class="secure-payment">
                                        <i class="fas fa-shield-alt"></i>
                                        <span>Secure payment options available</span>
                                    </div>
                                </div>
                                <div class="col-lg-6">
                                    <div class="trust-badges">
                                        <div class="trust-badge">
                                            <div class="trust-badge-icon">
                                                <i class="fas fa-certificate"></i>
                                            </div>
                                            <div class="trust-badge-text">
                                                <h5>1 Year Warranty</h5>
                                                <p>Full coverage on all components</p>
                                            </div>
                                        </div>
                                        <div class="trust-badge">
                                            <div class="trust-badge-icon">
                                                <i class="fas fa-truck"></i>
                                            </div>
                                            <div class="trust-badge-text">
                                                <h5>Free Delivery</h5>
                                                <p>Nationwide shipping included</p>
                                            </div>
                                        </div>
                                        <div class="trust-badge">
                                            <div class="trust-badge-icon">
                                                <i class="fas fa-headset"></i>
                                            </div>
                                            <div class="trust-badge-text">
                                                <h5>24/7 Support</h5>
                                                <p>Expert technical assistance</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = content.replace(old_pricing_html, new_pricing_html)

# 3. Add pulse class to CTA buttons
content = content.replace(
    'class="btn btn-primary btn-lg mr-3"',
    'class="btn btn-primary btn-lg mr-3 btn-pulse"'
)

content = content.replace(
    '<a href="#pricing" class="btn btn-primary btn-lg animated fadeInRight">',
    '<a href="#pricing" class="btn btn-primary btn-lg btn-pulse animated fadeInRight">'
)

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Pricing Section Redesigned!")
print("   - Premium dark gradient background")
print("   - Animated gold top border")
print("   - Trust badges replacing ugly logo")
print("   - Better typography and spacing")
print("")
print("✅ CTA Button Pulse Animation added!")
print("   - Pulsing glow effect on primary buttons")
print("   - Shine sweep on hover")
print("   - Lift effect on hover")
