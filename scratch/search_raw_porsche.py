with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find occurrences of 'porsche' (case-insensitive or case-sensitive)
occurrences = []
start = 0
while True:
    idx = content.find('porsche', start)
    if idx == -1:
        break
    # Skip the project database definition around index 814953
    if abs(idx - 814953) > 100:
        occurrences.append(idx)
    start = idx + 1

print(f"Found {len(occurrences)} other occurrences of 'porsche' in JS bundle:")
for idx in occurrences:
    print(f"Index {idx}:")
    print(content[max(0, idx - 150):min(len(content), idx + 250)])
    print("-" * 40)
