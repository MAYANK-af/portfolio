import urllib.request
import urllib.error

url = "https://images.pexels.com/photos/4373997/pexels-photo-4373997.jpeg"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        print(f"SUCCESS {response.status}: {url}")
except urllib.error.HTTPError as e:
    print(f"FAILED {e.code}: {url}")
except Exception as e:
    print(f"ERROR: {url} -> {e}")
