import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        target = 'filter:blur(130px)'
        replacement = 'filter:blur(60px)'
        
        if target in content:
            updated = content.replace(target, replacement)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Optimized CSS blur filter in {os.path.basename(html_path)}")
        else:
            print(f"Target CSS blur filter not found in {os.path.basename(html_path)}")
    else:
        print(f"Error: {html_path} not found")
