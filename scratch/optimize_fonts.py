import os

css_path = r'e:\New folder\static\css\main.ec87ac61.css'
html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

# 1. Update CSS file
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    target_import = '@import url(https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,700,500,400&f[]=general-sans@600,500,400,300&f[]=jetbrains-mono@500,400&display=swap);'
    
    if target_import in css_content:
        updated_css = css_content.replace(target_import, '')
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(updated_css)
        print("Removed @import from CSS file")
    else:
        print("Did not find target @import in CSS (already removed or modified)")
else:
    print(f"Error: CSS file not found at {css_path}")

# 2. Update HTML files
font_tags = """<link rel="preconnect" href="https://api.fontshare.com" crossorigin/>
<link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,700,500,400&amp;f[]=general-sans@600,500,400,300&amp;f[]=jetbrains-mono@500,400&amp;display=swap" rel="stylesheet"/>
"""

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Check if we have already added the tags
        if 'api.fontshare.com' not in html_content:
            target_insertion = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@600&display=swap" rel="stylesheet"/>'
            if target_insertion in html_content:
                updated_html = html_content.replace(
                    target_insertion, 
                    target_insertion + "\n" + font_tags
                )
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(updated_html)
                print(f"Injected fontshare tags into {os.path.basename(html_path)}")
            else:
                print(f"Error: Could not find Inter font link target in {os.path.basename(html_path)}")
        else:
            print(f"Fontshare tags already present in {os.path.basename(html_path)}")
    else:
        print(f"Error: HTML file not found at {html_path}")
