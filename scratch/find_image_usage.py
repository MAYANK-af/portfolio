import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for occurrences of .image or image in the context of JSX elements
# E.g. .image, image:
for m in re.finditer(r'\bimage\b', content):
    idx = m.start()
    start = max(0, idx - 150)
    end = min(len(content), idx + 150)
    print(f"[{idx}]: ...{content[start:end]}...\n")
