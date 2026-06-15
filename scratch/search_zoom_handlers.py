import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for lightbox, modal, zoom, dialog, enlarged or click handlers on images
terms = ['lightbox', 'modal', 'zoom', 'dialog', 'enlarge', 'onClick', 'click']

for term in terms:
    matches = list(re.finditer(term, content, re.IGNORECASE))
    print(f"Matches for '{term}': {len(matches)}")
    # Print the first few matches
    for m in matches[:5]:
        start = max(0, m.start() - 50)
        end = min(len(content), m.end() + 50)
        print(f"  [{m.start()}]: ...{content[start:end]}...")
