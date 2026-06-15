import os

def optimize():
    html_files = [
        'index.html',
        'mayank-yadav-portfolio.html'
    ]
    
    # Target 1: CSS for gradient mesh blur
    target_blur = '#gradient-mesh::before,#gradient-mesh::after,#gradient-mesh-3{content:"";position:absolute;border-radius:50%;filter:blur(60px);pointer-events:none}'
    replacement_blur = '#gradient-mesh::before,#gradient-mesh::after,#gradient-mesh-3{content:"";position:absolute;border-radius:50%;filter:blur(15px);pointer-events:none}'
    
    # Target 2: Radial gradient definitions (softening them naturally)
    target_gradients = [
        ('rgba(30,27,75,0.75) 0%,transparent 70%', 'rgba(30,27,75,0.5) 0%,rgba(30,27,75,0.15) 50%,transparent 100%'),
        ('rgba(12,74,110,0.75) 0%,transparent 70%', 'rgba(12,74,110,0.5) 0%,rgba(12,74,110,0.15) 50%,transparent 100%'),
        ('rgba(76,29,149,0.45) 0%,transparent 70%', 'rgba(76,29,149,0.3) 0%,rgba(76,29,149,0.08) 50%,transparent 100%')
    ]
    
    # Target 3: Add scroll performance optimizer class rule for backdrop-filter
    scroll_perf_css = """
/* Scroll Performance Optimizer - Temporarily disable backdrop blur during scroll to save GPU repaints */
.disable-hover article,
.disable-hover section [class*="border"][class*="rounded"],
.disable-hover a[class*="border"][class*="rounded"],
.disable-hover .glass {
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  transition: none !important;
}
"""

    for filepath in html_files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = content.replace('\r\n', '\n')
            
            # 1. Update blur
            if target_blur in content:
                content = content.replace(target_blur, replacement_blur)
                print(f"Reduced gradient mesh filter blur in {filepath}")
            else:
                print(f"Warning: target_blur not found in {filepath}")
                
            # 2. Update gradients
            for target_grad, replacement_grad in target_gradients:
                if target_grad in content:
                    content = content.replace(target_grad, replacement_grad)
                    print(f"Optimized radial gradient in {filepath}")
                else:
                    print(f"Warning: gradient target not found in {filepath}")
                    
            # 3. Add scroll performance class rule
            style_end = '</style>'
            if style_end in content:
                content = content.replace(style_end, scroll_perf_css + style_end)
                print(f"Added scroll performance backdrop-filter rules to {filepath}")
            else:
                print(f"Warning: Style end tag not found in {filepath}")
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Finished optimizing {filepath}\n")

if __name__ == '__main__':
    optimize()
