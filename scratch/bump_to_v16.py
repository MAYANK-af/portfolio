import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace JS ?v=15 with ?v=16
        updated = content.replace('main.e1c64cec.js?v=15', 'main.e1c64cec.js?v=16')
        
        # Replace CSS main.ec87ac61.css?v=15 with main.ec87ac61.css?v=16
        updated = updated.replace('main.ec87ac61.css?v=15', 'main.ec87ac61.css?v=16')
        
        if updated != content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Bumped cache busting version to v=16 in {os.path.basename(html_path)}")
        else:
            print(f"No matches found or already bumped in {os.path.basename(html_path)}")
    else:
        print(f"Error: {html_path} not found")
