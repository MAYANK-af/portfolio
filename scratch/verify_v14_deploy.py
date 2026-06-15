import urllib.request
import re
import time

url = "https://mayank-af.github.io/portfolio/"

# Wait a moment for GitHub Pages deployment to catch up
print("Waiting 10 seconds for Pages to build/redeploy...")
time.sleep(10)

print(f"Fetching {url}...")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
    print(f"Successfully fetched index.html. Length: {len(content)}")
    
    # Search for main.e1c64cec.js
    matches = re.findall(r'<script defer="defer" src="[^"]+"></script>', content)
    print("Script tags found in deployed HTML:")
    for m in matches:
        print(f"  {m}")
        
except Exception as e:
    print(f"Error: {e}")
