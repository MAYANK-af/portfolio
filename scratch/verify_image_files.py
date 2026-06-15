import os
from PIL import Image

media_dir = 'static/media'
images = [
    'cover_fake_news.jpg',
    'cover_health_ai.jpg',
    'cover_asus_tuf.jpg',
    'cover_porsche.jpg',
    'profile_photo.jpeg'
]

print("Verifying image files:")
for img_name in images:
    path = os.path.join(media_dir, img_name)
    if os.path.exists(path):
        try:
            with Image.open(path) as img:
                img.verify()
            print(f"  VALID: {img_name} ({os.path.getsize(path)} bytes, format: {img.format if hasattr(img, 'format') else 'unknown'})")
        except Exception as e:
            print(f"  CORRUPT: {img_name} -> {e}")
    else:
        print(f"  MISSING: {img_name}")
