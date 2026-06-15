with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = 961384
start = max(0, idx - 4000)
end = idx
print(content[start:end])
