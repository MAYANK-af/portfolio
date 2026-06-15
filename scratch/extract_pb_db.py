import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's extract the definition of pb
match = re.search(r'const pb=\{', content)
if match:
    idx = match.start()
    # Let's print about 4000 characters from the start of pb
    print("pb object definition:")
    print(content[idx:idx+4000])
else:
    # Try case-insensitive or search for 'pb=' or 'pb ='
    match2 = re.search(r'\bpb\s*=\s*\{', content)
    if match2:
        idx = match2.start()
        print("pb definition found:")
        print(content[idx:idx+4000])
    else:
        print("Could not find pb object definition")
