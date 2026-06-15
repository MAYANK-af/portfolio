import os

js_path = r'e:\New folder\static\js\main.e1c64cec.js'
if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    
    # 1. Replace section padding: py-32 md:py-48 -> py-20 md:py-32
    # Let's count occurrences
    count_padding = js.count('py-32 md:py-48')
    print(f"Occurrences of 'py-32 md:py-48' found: {count_padding}")
    
    js = js.replace('py-32 md:py-48', 'py-20 md:py-32')
    
    # 2. Add progress bars in Skills list
    # The original fragment:
    # children:[(0,Pe.jsxs)("div",{className:"flex items-baseline justify-between mb-3",children:[(0,Pe.jsx)("span",{className:"font-heading text-xl text-white tracking-tight",children:t})]}),null]}
    # We will replace it with:
    # children:[(0,Pe.jsxs)("div",{className:"flex items-baseline justify-between mb-2",children:[(0,Pe.jsx)("span",{className:"font-heading text-lg text-white tracking-tight",children:t}),(0,Pe.jsx)("span",{className:"font-mono text-xs text-zinc-500",children:n+"%"})]}),(0,Pe.jsx)("div",{className:"w-full h-1 bg-white/10 rounded-full overflow-hidden",children:(0,Pe.jsx)("div",{className:"h-full bg-gradient-to-r from-[#06b6d4] to-[#8b5cf6]",style:{width:n+"%"}})})]}
    
    target_skills = 'children:[(0,Pe.jsxs)("div",{className:"flex items-baseline justify-between mb-3",children:[(0,Pe.jsx)("span",{className:"font-heading text-xl text-white tracking-tight",children:t})]}),null]}'
    replacement_skills = 'children:[(0,Pe.jsxs)("div",{className:"flex items-baseline justify-between mb-2",children:[(0,Pe.jsx)("span",{className:"font-heading text-lg text-white tracking-tight",children:t}),(0,Pe.jsx)("span",{className:"font-mono text-xs text-zinc-500",children:n+"%"})]}),(0,Pe.jsx)("div",{className:"w-full h-1 bg-white/10 rounded-full overflow-hidden",children:(0,Pe.jsx)("div",{className:"h-full bg-gradient-to-r from-[#06b6d4] to-[#8b5cf6]",style:{width:n+"%"}})})]}'
    
    if target_skills in js:
        js = js.replace(target_skills, replacement_skills)
        print("Successfully replaced null with glowing progress bars in Skills component!")
    else:
        print("Error: Target skills rendering pattern not found in JS bundle")
        
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("JS bundle updated successfully!")
else:
    print("Error: JS bundle not found")
