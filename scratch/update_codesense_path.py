import os

js_path = r'e:\New folder\static\js\main.e1c64cec.js'
if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    
    target_url = 'https://images.pexels.com/photos/4373997/pexels-photo-4373997.jpeg'
    local_path = '/portfolio/static/media/cover_codesense.jpg'
    
    if target_url in js:
        js = js.replace(target_url, local_path)
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js)
        print("Successfully updated CodeSense image path in JS bundle!")
    else:
        print("Error: Target remote URL not found in JS bundle (already updated?)")
else:
    print("Error: JS bundle not found")
