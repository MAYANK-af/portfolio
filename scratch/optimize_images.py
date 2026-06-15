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

print("Optimizing images...")
for img_name in images:
    path = os.path.join(media_dir, img_name)
    if os.path.exists(path):
        orig_size = os.path.getsize(path)
        try:
            with Image.open(path) as img:
                # Save as progressive JPEG with quality=80
                img.save(path, 'JPEG', quality=80, optimize=True, progressive=True)
            new_size = os.path.getsize(path)
            reduction = (orig_size - new_size) / orig_size * 100
            print(f"  OPTIMIZED: {img_name} ({orig_size} -> {new_size} bytes, -{reduction:.1f}%)")
        except Exception as e:
            print(f"  ERROR: {img_name} -> {e}")
    else:
        print(f"  MISSING: {img_name}")
