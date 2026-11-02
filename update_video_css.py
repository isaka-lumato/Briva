with open('equipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Old video container CSS
old_css = '''        .video-container {
            position: relative;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            margin: 40px 0;
            overflow: hidden;
            cursor: pointer;
            transition: all 0.3s ease;
        }'''

# New video container CSS with 16:9 aspect ratio and all thumbnail styles
new_css = '''        .video-container {
            position: relative;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            margin: 40px 0;
            overflow: hidden;
            cursor: pointer;
            transition: all 0.3s ease;
            /* 16:9 Aspect Ratio */
            padding-bottom: 56.25%;
            height: 0;
        }

        .video-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        }

        .video-thumbnail {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            transition: all 0.3s ease;
        }

        .video-container:hover .video-thumbnail {
            transform: scale(1.05);
        }

        .video-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            z-index: 1;
        }

        .video-container:hover .video-overlay {
            background: rgba(0, 0, 0, 0.5);
        }

        .play-button {
            width: 80px;
            height: 80px;
            background: rgba(255, 182, 0, 0.95);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            animation: pulse-play 2s ease-in-out infinite;
            box-shadow: 0 0 0 0 rgba(255, 182, 0, 0.7);
        }

        .video-container:hover .play-button {
            transform: scale(1.1);
            background: rgba(255, 182, 0, 1);
            animation: none;
        }

        .play-button i {
            color: #fff;
            font-size: 32px;
            margin-left: 5px;
        }

        @keyframes pulse-play {
            0% {
                box-shadow: 0 0 0 0 rgba(255, 182, 0, 0.7);
            }
            50% {
                box-shadow: 0 0 0 20px rgba(255, 182, 0, 0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(255, 182, 0, 0);
            }
        }

        .video-badge {
            position: absolute;
            top: 15px;
            left: 15px;
            background: rgba(255, 182, 0, 0.95);
            color: #fff;
            padding: 6px 15px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.85rem;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            z-index: 2;
        }

        .video-duration {
            position: absolute;
            bottom: 15px;
            right: 15px;
            background: rgba(0, 0, 0, 0.8);
            color: #fff;
            padding: 5px 12px;
            border-radius: 5px;
            font-weight: 600;
            font-size: 0.85rem;
            z-index: 2;
        }'''

# Normalize line endings and replace
content = content.replace('\r\n', '\n')
old_css = old_css.replace('\r\n', '\n')
new_css = new_css.replace('\r\n', '\n')

if old_css in content:
    content = content.replace(old_css, new_css)
    print("CSS updated successfully!")
else:
    print("Could not find target CSS")

# Write back
with open('equipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
