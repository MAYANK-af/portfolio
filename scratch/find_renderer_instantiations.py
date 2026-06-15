import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for instances of common three.js class calls
# Usually in minified bundles they look like: new e.WebGLRenderer, new r.WebGLRenderer, etc.
# We will search for 'WebGLRenderer' in the bundle and list the characters preceding it.
for m in re.finditer(r'WebGLRenderer', content):
    idx = m.start()
    preceding = content[max(0, idx - 15):idx]
    print(f"Index {idx}: '{preceding}WebGLRenderer'")
