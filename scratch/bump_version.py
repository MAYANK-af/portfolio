import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace ?v=13 with ?v=14
        updated = content.replace('?v=13', '?v=14')
        
        if updated != content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Bumped cache busting version to v=14 in {os.path.basename(html_path)}")
        else:
            print(f"Could not find ?v=13 in {os.path.basename(html_path)} or already bumped")
    else:
        print(f"Error: {html_path} not found")
