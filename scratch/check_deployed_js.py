import urllib.request
import re

url = "https://mayank-af.github.io/portfolio/static/js/main.e1c64cec.js?v=13"
print(f"Fetching {url}...")

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
    print(f"Successfully fetched JS. Length: {len(content)}")
    
    # Search for cover_fake_news
    matches = [m.start() for m in re.finditer('cover_fake_news', content)]
    print(f"Matches for 'cover_fake_news': {len(matches)}")
    for idx in matches:
        start = max(0, idx - 50)
        end = min(len(content), idx + 50)
        print(f"[{idx}]: ...{content[start:end]}...")
        
except Exception as e:
    print(f"Error: {e}")
