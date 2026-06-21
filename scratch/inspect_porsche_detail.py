with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('porsche:{role:')
if idx != -1:
    print("Found Porsche detailed view start at index:", idx)
    print("Porsche detailed view structure (800 chars):")
    print(content[idx:idx+800])
else:
    print("Could not find porsche:{role: start in JS")
