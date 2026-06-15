import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']
preload_tag = '<link rel="preload" as="image" href="/portfolio/static/media/cover_codesense.jpg" type="image/jpeg"/>'

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if we have already added the preload tag
        if 'cover_codesense.jpg' not in content:
            target = '<link rel="preload" as="image" href="/portfolio/static/media/profile_photo.jpeg" type="image/jpeg"/>'
            if target in content:
                updated = content.replace(target, target + "\n" + preload_tag)
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(updated)
                print(f"Preloaded cover_codesense.jpg in {os.path.basename(html_path)}")
            else:
                print(f"Error: Target preload profile_photo tag not found in {os.path.basename(html_path)}")
        else:
            print(f"cover_codesense.jpg preload already present in {os.path.basename(html_path)}")
    else:
        print(f"Error: {html_path} not found")
