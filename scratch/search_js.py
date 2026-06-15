import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File length: {len(content)}")

for term in ['health', 'fake_news', 'cover_', 'cover']:
    matches = [m.start() for m in re.finditer(term, content, re.IGNORECASE)]
    print(f"\nMatches for '{term}': {len(matches)}")
    for idx in matches[:10]:
        start = max(0, idx - 100)
        end = min(len(content), idx + 100)
        print(f"[{idx}]: ...{content[start:end]}...")
