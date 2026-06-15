import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for the definition of Tb
# Usually like 'const Tb=' or 'function Tb(' or 'Tb=function('
patterns = [
    r'\bTb\s*=\s*function\b',
    r'\bconst\s+Tb\s*=\s*',
    r'\bfunction\s+Tb\b',
    r'\bTb\s*=\s*\(\)\s*=>'
]

found = False
for p in patterns:
    match = re.search(p, content)
    if match:
        idx = match.start()
        print(f"Found Tb definition with pattern '{p}' at index {idx}:")
        # Print next 2500 characters
        print(content[idx:idx+2500])
        found = True
        break

if not found:
    print("Could not find Tb definition using patterns.")
