import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace JS ?v=18 with ?v=19
        updated = content.replace('main.e1c64cec.js?v=18', 'main.e1c64cec.js?v=19')
        
        # Replace CSS main.ec87ac61.css?v=18 with main.ec87ac61.css?v=19
        updated = updated.replace('main.ec87ac61.css?v=18', 'main.ec87ac61.css?v=19')
        
        if updated != content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Bumped cache busting version to v=19 in {os.path.basename(html_path)}")
        else:
            print(f"No matches found or already bumped in {os.path.basename(html_path)}")
    else:
        print(f"Error: {html_path} not found")
