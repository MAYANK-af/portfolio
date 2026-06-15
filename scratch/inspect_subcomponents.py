import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

components = ['dh', 'mh', 'gh', 'yh', 'Dg', 'Og', 'Ug', 'lb', 'db']

for comp in components:
    # Let's search for function comp( or const comp= or function comp_name
    match = re.search(r'\bfunction\s+' + comp + r'\b', content)
    if not match:
        match = re.search(r'\b' + comp + r'\s*=\s*function\b', content)
    
    if match:
        idx = match.start()
        # Print the first 500 characters of the component to see its HTML tags and texts
        print(f"\n=================== Component {comp} at {idx} ===================")
        print(content[idx:idx+800])
    else:
        print(f"Could not find definition for component {comp}")
