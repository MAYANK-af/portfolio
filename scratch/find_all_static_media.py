import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.finditer(r'static/media/[a-zA-Z0-9_\-\.]+', content)
print("Occurrences of static/media/ in JS bundle:")
for m in matches:
    print(f"[{m.start()}]: {m.group(0)}")
