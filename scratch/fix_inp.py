import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # 1. Promote gradient-mesh to its own GPU layer with will-change and contain
        content = content.replace(
            '#gradient-mesh{position:fixed;inset:0;z-index:-2;pointer-events:none;opacity:0.45}',
            '#gradient-mesh{position:fixed;inset:0;z-index:-2;pointer-events:none;opacity:0.45;will-change:transform;contain:strict}'
        )
        
        # 2. Promote noise overlay to GPU layer and reduce octaves
        content = content.replace(
            'numOctaves="4"',
            'numOctaves="2"'
        )
        content = content.replace(
            '#noise-overlay{position:fixed;inset:0;z-index:9998;pointer-events:none;opacity:0.035;mix-blend-mode:overlay}',
            '#noise-overlay{position:fixed;inset:0;z-index:9998;pointer-events:none;opacity:0.035;mix-blend-mode:overlay;will-change:transform;contain:strict}'
        )
        
        # 3. Add contain:content to sections for layout isolation
        content = content.replace(
            '.reveal-section{opacity:0;transform:translateY(40px);transition:opacity 0.8s cubic-bezier(0.16,1,0.3,1),transform 0.8s cubic-bezier(0.16,1,0.3,1)}',
            '.reveal-section{opacity:0;transform:translateY(40px);transition:opacity 0.8s cubic-bezier(0.16,1,0.3,1),transform 0.8s cubic-bezier(0.16,1,0.3,1);contain:layout style}'
        )
        
        # 4. Shorten transition durations on cards to reduce presentation delay
        # border-color and box-shadow transitions from 0.3s to 0.15s
        content = content.replace(
            'transition:border-color 0.3s,box-shadow 0.3s;',
            'transition:border-color 0.15s,box-shadow 0.15s;'
        )
        
        # 5. Shorten the spotlight opacity transition from 0.35s to 0.15s  
        content = content.replace(
            'transition: opacity 0.35s ease;',
            'transition: opacity 0.15s ease;'
        )
        
        # 6. Reduce glow-rotate animation from 3s to avoid continuous repainting
        # Instead of animating border gradient on hover, use a simpler static glow
        content = content.replace(
            '  animation:glow-rotate 3s linear infinite;\n  box-shadow:0 0 30px rgba(139,92,246,0.15),0 0 50px rgba(6,182,212,0.1);',
            '  box-shadow:0 0 20px rgba(139,92,246,0.12),0 0 40px rgba(6,182,212,0.08);'
        )
        # Try with \r\n too
        content = content.replace(
            '  animation:glow-rotate 3s linear infinite;\r\n  box-shadow:0 0 30px rgba(139,92,246,0.15),0 0 50px rgba(6,182,212,0.1);',
            '  box-shadow:0 0 20px rgba(139,92,246,0.12),0 0 40px rgba(6,182,212,0.08);'
        )
        
        # 7. Replace the broad attribute selectors with more efficient ones using content-visibility
        # Add content-visibility: auto to the root for offscreen rendering optimization
        content = content.replace(
            '<div id="root"></div>',
            '<div id="root" style="content-visibility:auto"></div>'
        )
        
        if content != original:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Applied INP optimizations to {os.path.basename(html_path)}")
        else:
            print(f"No changes made to {os.path.basename(html_path)}")
    else:
        print(f"Error: {html_path} not found")
