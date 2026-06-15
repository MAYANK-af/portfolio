with open(r'e:\New folder\static\js\main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Find occurrences of addEventListener for scroll and wheel
for event in ['scroll', 'wheel']:
    print(f"\n--- OCCURRENCES OF '{event}' ---")
    matches = [m.start() for m in re.finditer(event, content, re.IGNORECASE)]
    print(f"Found {len(matches)} occurrences")
    for idx, pos in enumerate(matches[:15]):
        start = max(0, pos - 80)
        end = min(len(content), pos + 150)
        snippet = content[start:end].replace('\n', ' ')
        print(f"  [{idx+1}] at {pos}: ...{snippet}...")
