import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "three"
matches = [m.start() for m in re.finditer(r'\bthree\b', content, re.IGNORECASE)]
print(f"Matches for 'three': {len(matches)}")
for idx in matches[:10]:
    start = max(0, idx - 100)
    end = min(len(content), idx + 200)
    print(f"[{idx}]: ...{content[start:end]}...")
