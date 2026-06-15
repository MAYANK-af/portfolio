import urllib.request
import re

url = "https://mayank-af.github.io/portfolio/"
print(f"Fetching {url}...")

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
    print(f"Successfully fetched index.html. Length: {len(content)}")
    
    # Search for main.e1c64cec.js
    matches = re.findall(r'<script defer="defer" src="[^"]+"></script>', content)
    print("Script tags:")
    for m in matches:
        print(m)
        
    # Let's search for any occurrence of e1c64cec
    matches_js = [m.start() for m in re.finditer('e1c64cec', content)]
    for idx in matches_js:
        print(content[idx-50:idx+50])
        
except Exception as e:
    print(f"Error: {e}")
