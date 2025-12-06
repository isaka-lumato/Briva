with open('equipment.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Keep lines 0-829 (first 830 lines) + add shuffle script + lines 1024 onwards
shuffle_script = '        <script src="plugins/shuffle/shuffle.min.js" defer></script>\n'
new_lines = lines[:829] + [shuffle_script, '\n'] + lines[1024:]

with open('equipment.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'Fixed! File reduced from {len(lines)} to {len(new_lines)} lines')
