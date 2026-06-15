import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for the pattern and look at the preceding characters
matches = list(re.finditer(r'static/media/[a-zA-Z0-9_\-\.]+', content))
print(f"Total occurrences of static/media/ found: {len(matches)}")
for idx, m in enumerate(matches):
    start_pos = m.start()
    preceding = content[max(0, start_pos - 15):start_pos]
    print(f"Match {idx+1}: preceding content is '{preceding}' -> match is '{m.group(0)}'")
