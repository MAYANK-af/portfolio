with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('porsche:{role:')
if idx != -1:
    print(content[idx+600:idx+1200])
