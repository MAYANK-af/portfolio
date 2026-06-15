import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

for m in re.finditer(r'4373997', content):
    idx = m.start()
    start = max(0, idx - 150)
    end = min(len(content), idx + 150)
    print(f"[{idx}]: ...{content[start:end]}...")
