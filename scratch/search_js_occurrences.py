with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's count how many times 'codesense' appears in the file
occurrences = []
start = 0
while True:
    idx = content.find('id:"codesense"', start)
    if idx == -1:
        break
    occurrences.append(idx)
    start = idx + 1

print(f"Found {len(occurrences)} occurrences of 'id:\"codesense\"' in JS bundle:")
for idx in occurrences:
    print(f"Index {idx}:")
    print(content[max(0, idx - 100):min(len(content), idx + 200)])
    print("-" * 40)
