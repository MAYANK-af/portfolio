import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for path:"/"
match = re.search(r'path:"/"', content)
if match:
    idx = match.start()
    start = max(0, idx - 200)
    end = min(len(content), idx + 1500)
    print("Homepage Route Definition:")
    print(content[start:end])
else:
    print("Could not find path:'/' in JS")
