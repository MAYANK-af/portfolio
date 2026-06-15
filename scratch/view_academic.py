import os

def main():
    js_path = 'static/js/main.e1c64cec.js'
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    idx = content.find('id:"academic"')
    if idx != -1:
        print("Found at", idx)
        print(content[idx:idx+3000])
    else:
        print("Not found")

if __name__ == '__main__':
    main()
