import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

for m in re.finditer(r'basename', content):
    idx = m.start()
    start = max(0, idx - 100)
    end = min(len(content), idx + 100)
    print(f"[{idx}]: ...{content[start:end]}...")
