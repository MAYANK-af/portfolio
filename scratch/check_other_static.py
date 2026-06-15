import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

matches = list(re.finditer(r'(?<!/portfolio/)static/[a-zA-Z0-9_\-\./]+', content))
print(f"Occurrences of static/ not preceded by /portfolio/ in JS bundle: {len(matches)}")
for m in matches:
    print(m.group(0))
