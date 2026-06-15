with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for WebGLRenderer in the last part of the file
import re
matches = [m.start() for m in re.finditer(r'WebGLRenderer', content)]
print(f"All WebGLRenderer occurrences: {matches}")

custom_matches = [m for m in matches if m > 800000]
print(f"Custom WebGLRenderer occurrences (index > 800000): {custom_matches}")
for idx in custom_matches:
    start = max(0, idx - 100)
    end = min(len(content), idx + 1500)
    print(f"[{idx}]: ...{content[start:end]}...\n")
