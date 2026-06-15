import os

def optimize():
    # 1. Update HTML preloads
    html_files = [
        'index.html',
        'mayank-yadav-portfolio.html'
    ]
    
    target_preload = '<link rel="preload" as="image" href="/portfolio/static/media/cover_codesense.jpg" type="image/jpeg"/>'
    replacement_preloads = """<link rel="preload" as="image" href="/portfolio/static/media/cover_codesense.jpg" type="image/jpeg"/>
<link rel="preload" as="image" href="/portfolio/static/media/cover_fake_news.jpg" type="image/jpeg"/>
<link rel="preload" as="image" href="/portfolio/static/media/cover_health_ai.jpg" type="image/jpeg"/>
<link rel="preload" as="image" href="/portfolio/static/media/cover_asus_tuf.jpg" type="image/jpeg"/>
<link rel="preload" as="image" href="/portfolio/static/media/cover_porsche.jpg" type="image/jpeg"/>"""

    for filepath in html_files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if target_preload in content:
                content = content.replace(target_preload, replacement_preloads)
                print(f"Added cover image preloads to {filepath}")
            else:
                print(f"Warning: Preload target not found in {filepath}")
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

    # 2. Update JS bundle for IntersectionObserver threshold and lazy loading
    js_path = 'static/js/main.e1c64cec.js'
    if os.path.exists(js_path):
        with open(js_path, 'r', encoding='utf-8') as f:
            js_content = f.read()
            
        # Optimize IntersectionObserver threshold for project cards from .15 to .02
        target_observer = 'IntersectionObserver(e=>{e.forEach(e=>{e.isIntersecting&&e.target.classList.add("visible")})},{threshold:.15})'
        replacement_observer = 'IntersectionObserver(e=>{e.forEach(e=>{e.isIntersecting&&e.target.classList.add("visible")})},{threshold:.02})'
        
        if target_observer in js_content:
            js_content = js_content.replace(target_observer, replacement_observer)
            print("Optimized IntersectionObserver threshold to 0.02 in JS bundle")
        else:
            # try finding with spaces or slight variations if any
            print("Warning: Target observer pattern not found exactly in JS bundle")
            
        # Optimize image loading by changing loading:"lazy" to loading:"eager" for project cards
        target_lazy = 'loading:"lazy",className:"w-full h-full object-cover transition-all duration-[1200ms] scale-105 group-hover:scale-100"'
        replacement_eager = 'loading:"eager",className:"w-full h-full object-cover transition-all duration-[1200ms] scale-105 group-hover:scale-100"'
        
        if target_lazy in js_content:
            js_content = js_content.replace(target_lazy, replacement_eager)
            print("Changed project cards loading from lazy to eager in JS bundle")
        else:
            print("Warning: Target lazy loading pattern not found in JS bundle")
            
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
            
if __name__ == '__main__':
    optimize()
