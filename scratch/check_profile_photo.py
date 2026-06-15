from PIL import Image
import os

img_path = 'static/media/profile_photo.jpeg'
if os.path.exists(img_path):
    with Image.open(img_path) as img:
        print(f"Profile photo dimensions: {img.size} (Width x Height)")
        print(f"Format: {img.format}")
        print(f"File size: {os.path.getsize(img_path)} bytes")
else:
    print("Profile photo not found")
