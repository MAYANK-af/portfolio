import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for WebGLRenderer
matches = [m.start() for m in re.finditer(r'WebGLRenderer', content)]
print(f"Matches for WebGLRenderer: {len(matches)}")
for idx in matches[:10]:
    start = max(0, idx - 150)
    end = min(len(content), idx + 2000)
    print(f"[{idx}]: ...{content[start:end]}...\n")
