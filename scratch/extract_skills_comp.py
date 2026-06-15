with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = 897905
start = idx
end = min(len(content), idx + 2500)
print(content[start:end])
