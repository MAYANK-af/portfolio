import os

js_path = r'e:\New folder\static\js\main.e1c64cec.js'
html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

# 1. Update JS bundle
if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # Check if we have already updated
    if '/portfolio/static/media/' not in js_content:
        updated_js = js_content.replace('static/media/', '/portfolio/static/media/')
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(updated_js)
        print("Updated static/media/ paths in JS bundle to /portfolio/static/media/")
    else:
        print("JS bundle already contains absolute /portfolio/static/media/ paths")
else:
    print(f"Error: JS bundle not found at {js_path}")

# 2. Update HTML files
for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        updated_html = html_content
        # Replace href="static/ and src="static/
        updated_html = updated_html.replace('href="static/', 'href="/portfolio/static/')
        updated_html = updated_html.replace('src="static/', 'src="/portfolio/static/')
        
        if updated_html != html_content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(updated_html)
            print(f"Updated paths in {os.path.basename(html_path)}")
        else:
            print(f"No changes needed or already updated for {os.path.basename(html_path)}")
    else:
        print(f"Error: HTML file not found at {html_path}")
