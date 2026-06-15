import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        updated = content.replace('?v=20', '?v=21')
        if updated != content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Bumped to v=21 in {os.path.basename(html_path)}")
        else:
            print(f"Already at v=21 or no match in {os.path.basename(html_path)}")
    else:
        print(f"Error: {html_path} not found")
