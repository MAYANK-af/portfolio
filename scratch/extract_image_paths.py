import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for image:"..." or image:'...'
matches = re.findall(r'image:\s*"([^"]+)"', content)
print("Double quote matches:")
for m in matches:
    print(m)

matches_single = re.findall(r"image:\s*'([^']+)'", content)
print("\nSingle quote matches:")
for m in matches_single:
    print(m)
