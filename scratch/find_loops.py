with open(r'e:\New folder\static\js\main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.finditer(r'addeventlistener\s*\(\s*["\']([^"\']+)["\']', content, re.IGNORECASE)
found = set()
for m in matches:
    event_type = m.group(1)
    found.add(event_type)

print("Found event listeners in React bundle:")
for ev in sorted(found):
    print(f"  - {ev}")
