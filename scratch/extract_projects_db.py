import re

with open('static/js/main.e1c64cec.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for the projects database.
# We know it contains 'healthai' and 'fakenews'.
# Let's search around 'fakenews' and print the context in a large block.
match = re.search(r'\{id:"healthai".*?\}', content)
if match:
    idx = match.start()
    start = max(0, idx - 1500)
    end = min(len(content), idx + 2500)
    print("Project array context:")
    print(content[start:end])
else:
    print("Could not find healthai object in JS")
