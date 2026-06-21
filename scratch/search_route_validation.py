with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's count occurrences of 'porsche' as a raw string or reference
occurrences = []
start = 0
while True:
    idx = content.find('"porsche"', start)
    if idx == -1:
        break
    occurrences.append(idx)
    start = idx + 1

print(f"Found {len(occurrences)} occurrences of '\"porsche\"' in JS bundle:")
for idx in occurrences:
    print(f"Index {idx}:")
    print(content[max(0, idx - 150):min(len(content), idx + 250)])
    print("-" * 40)
