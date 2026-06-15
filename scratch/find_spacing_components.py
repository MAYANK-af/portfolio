import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for function dh, function mh, function gh but in the context of their unique content
# Hero section contains "Mayank Yadav" (case-sensitive) or "Architect"
hero_matches = [m.start() for m in re.finditer(r'function\s+[a-zA-Z0-9_$]+\s*\(\)\s*\{[^}]*Mayank Yadav', content)]
print(f"Hero section function candidates: {hero_matches}")

# Let's print around the end of the file where the components are likely defined
# The components in React are usually defined near the end of the bundle.
# Let's do a search for 'py-32 md:py-48'
padding_matches = [m.start() for m in re.finditer(r'py-32\s+md:py-48', content)]
print(f"Matches for 'py-32 md:py-48': {len(padding_matches)}")
for idx in padding_matches:
    start = max(0, idx - 100)
    end = min(len(content), idx + 200)
    print(f"[{idx}]: ...{content[start:end]}...")
