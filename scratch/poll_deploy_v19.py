import urllib.request
import re
import time

url = "https://mayank-af.github.io/portfolio/"

for i in range(20):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
        
        matches = re.findall(r'<script defer="defer" src="([^"]+)"></script>', content)
        if matches:
            src = matches[0]
            print(f"Iteration {i+1}: Active script tag on live site is '{src}'")
            if 'v=19' in src:
                print("SUCCESS: Deployed version has updated to v=19!")
                break
        else:
            print(f"Iteration {i+1}: Script tag not found")
    except Exception as e:
        print(f"Iteration {i+1}: Error -> {e}")
        
    time.sleep(10)
