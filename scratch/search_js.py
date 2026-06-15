with open(r'e:\New folder\static\js\main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

queries = ['testimonials', 'journal', 'contact', 'section']
for q in queries:
    count = content.lower().count(q)
    print(f"Query '{q}' found {count} times")
    if count > 0:
        idx = content.lower().find(q)
        start = max(0, idx - 50)
        end = min(len(content), idx + 150)
        print(f"  Snippet: {content[start:end]}\n")
