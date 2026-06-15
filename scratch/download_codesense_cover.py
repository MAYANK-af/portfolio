import urllib.request
import os
from PIL import Image

url = "https://images.pexels.com/photos/4373997/pexels-photo-4373997.jpeg"
local_path = 'static/media/cover_codesense.jpg'

print(f"Downloading CodeSense cover from: {url}...")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = response.read()
    
    with open(local_path, 'wb') as f:
        f.write(data)
    
    print(f"Downloaded! Size: {os.path.getsize(local_path)} bytes")
    
    # Compress and convert to progressive JPEG
    with Image.open(local_path) as img:
        print(f"Original dimensions: {img.size}")
        # Let's save with progressive=True and quality=80
        img.save(local_path, 'JPEG', quality=80, optimize=True, progressive=True)
        
    print(f"Optimized CodeSense cover! New size: {os.path.getsize(local_path)} bytes")
except Exception as e:
    print(f"Error: {e}")
