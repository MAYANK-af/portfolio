with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = 961384
start = max(0, idx - 1000)
end = min(len(content), idx + 1000)
print(content[start:end])
