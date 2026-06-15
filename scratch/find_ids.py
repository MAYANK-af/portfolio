import os
import re

def main():
    js_path = 'static/js/main.e1c64cec.js'
    if not os.path.exists(js_path):
        print("JS not found")
        return
        
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Search for keys like id: "something" or similar pattern in JS
    id_matches = re.findall(r'id:\s*["\']([^"\']+)["\']', content)
    print("Found id keys in JS:", set(id_matches))
    
    # Search for HTML-like section ids or similar strings in the JS bundle
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', content)
    print("Found HTML section ids in JS:", set(sections))
    
    # Let's search for "toolkit", "experience", "record", "timeline", "achievement"
    keywords = ["toolkit", "skills", "experience", "record", "timeline", "achievement", "timeline", "academic", "journal", "testimonials", "contact"]
    for kw in keywords:
        indices = [m.start() for m in re.finditer(kw, content, re.IGNORECASE)]
        print(f"Keyword '{kw}' matches count: {len(indices)}")
        if indices:
            # print surrounding of first match
            first = indices[0]
            print(f"  First match: {content[first-50:first+50]}")

if __name__ == '__main__':
    main()
