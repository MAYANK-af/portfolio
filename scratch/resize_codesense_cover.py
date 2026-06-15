import os
from PIL import Image

path = 'static/media/cover_codesense.jpg'
if os.path.exists(path):
    orig_size = os.path.getsize(path)
    try:
        with Image.open(path) as img:
            print(f"Original dimensions: {img.size}")
            max_width = 800
            if img.width > max_width:
                w_percent = (max_width / float(img.width))
                h_size = int((float(img.height) * float(w_percent)))
                img_resized = img.resize((max_width, h_size), Image.Resampling.LANCZOS)
                print(f"Resized to: {img_resized.size}")
                # Save as progressive JPEG
                img_resized.save(path, 'JPEG', quality=80, optimize=True, progressive=True)
            else:
                img.save(path, 'JPEG', quality=80, optimize=True, progressive=True)
        new_size = os.path.getsize(path)
        reduction = (orig_size - new_size) / orig_size * 100
        print(f"Resized and optimized CodeSense cover! New size: {new_size} bytes, reduction: -{reduction:.1f}%")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("CodeSense cover file not found")
