import os

def apply_app_shell():
    html_files = [
        'index.html',
        'mayank-yadav-portfolio.html'
    ]
    
    # Custom CSS for the responsive app shell grid
    custom_css = """
/* ========== APP SHELL RESPONSIVE GRID ========== */
.lg-grid-cols-12-custom {
  display: grid;
  grid-template-columns: 1fr;
  gap: 48px;
  align-items: center;
}
@media (min-width: 1024px) {
  .lg-grid-cols-12-custom {
    grid-template-columns: repeat(12, minmax(0, 1fr)) !important;
  }
  .lg-col-span-8-custom {
    grid-column: span 8 / span 8 !important;
  }
  .lg-col-span-4-custom {
    grid-column: span 4 / span 4 !important;
  }
}
"""
    
    # CSS targets to remove
    css_targets = [
        '#page-curtain{position:fixed;inset:0;z-index:10000;background:#060608;display:flex;align-items:center;justify-content:center;transition:opacity 0.25s cubic-bezier(0.16,1,0.3,1),transform 0.25s cubic-bezier(0.16,1,0.3,1)}',
        '#page-curtain.lift{opacity:0;transform:translateY(-100%);pointer-events:none}',
        '#page-curtain .loader-ring{width:40px;height:40px;border:2px solid #ffffff15;border-top-color:#8b5cf6;border-radius:50%;animation:loader-spin 0.8s linear infinite}',
        '@keyframes loader-spin{to{transform:rotate(360deg)}}'
    ]
    
    # HTML curtain element to remove
    curtain_html = '<!-- Page Load Curtain -->\n<div id="page-curtain"><div class="loader-ring"></div></div>'
    
    # Prerendered HTML App Shell to insert inside #root
    app_shell_html = """<div id="root"><div style="min-height: 100vh; display: flex; flex-direction: column; justify-content: center; background: #060608; color: #fff; font-family: 'General Sans', 'Cabinet Grotesk', sans-serif;">
    <div style="max-w: 1800px; margin: 0 auto; padding: 24px; width: 100%; box-sizing: border-box;">
      <div class="lg-grid-cols-12-custom">
        <!-- Text Column -->
        <div class="lg-col-span-8-custom">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
            <span style="width: 10px; height: 10px; border-radius: 50%; background: #8b5cf6;"></span>
            <span style="font-family: monospace; font-size: 12px; text-transform: uppercase; letter-spacing: 0.2em; color: #8b5cf6;">Available for roles</span>
          </div>
          <h1 style="font-size: clamp(3rem, 10vw, 7rem); font-family: 'Cabinet Grotesk', sans-serif; font-weight: 800; line-height: 0.95; margin: 0 0 24px 0; color: #fff;">
            MAYANK<br><span style="color: #71717a;">YADAV.</span>
          </h1>
          <p style="font-size: 1.125rem; line-height: 1.6; color: #d4d4d8; max-width: 36rem; margin: 0;">
            Third-year B.Tech CSE (Data Science) student at Manipal University Jaipur. I design and ship production-grade Agentic AI systems and cinematic scroll-driven web experiences.
          </p>
        </div>
        
        <!-- Image Column -->
        <div class="lg-col-span-4-custom" style="max-width: 400px; width: 100%; margin: 0 auto;">
          <div style="background: rgba(11, 11, 14, 0.65); border: 1px solid rgba(255, 255, 255, 0.04); border-radius: 12px; padding: 24px; box-sizing: border-box; backdrop-filter: blur(10px);">
            <p style="font-family: monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 0.22em; color: #71717a; margin: 0 0 16px 0;">Operator</p>
            <div style="aspect-ratio: 3/4; width: 100%; overflow: hidden; border-radius: 8px; position: relative;">
              <img src="/portfolio/static/media/profile_photo.jpeg?v=22" alt="Mayank Yadav" style="width: 100%; height: 100%; object-fit: cover; filter: contrast(1.1);" />
            </div>
            <div style="margin-top: 24px; display: flex; align-items: center; justify-content: space-between;">
              <div>
                <p style="font-size: 1.25rem; font-weight: 700; margin: 0; color: #fff;">Mayank Yadav</p>
                <p style="font-family: monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 0.18em; color: #71717a; margin: 4px 0 0 0;">B.Tech CSE &middot; Data Science</p>
              </div>
              <span style="width: 8px; height: 8px; border-radius: 50%; background: #34d399;"></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div></div>"""

    # JS block to remove
    curtain_js = """// ===== 8. PAGE LOAD TRANSITION =====
(function(){
  function liftCurtain(){
    var curtain=document.getElementById("page-curtain");
    if(!curtain)return;
    var root=document.getElementById("root");
    function check(){
      if(root&&root.children.length>0){
        setTimeout(function(){
          curtain.classList.add("lift");
          setTimeout(function(){curtain.remove()},350);
        },30);
      }else{
        setTimeout(check,50);
      }
    }
    check();
  }
  if(document.readyState==="loading"){
    document.addEventListener("DOMContentLoaded",liftCurtain);
  }else{
    liftCurtain();
  }
})();"""

    for filepath in html_files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = content.replace('\r\n', '\n')
            
            # 1. Add custom CSS inside style block
            style_end = '</style>'
            if style_end in content:
                content = content.replace(style_end, custom_css + style_end)
                print(f"Added custom CSS to {filepath}")
                
            # 2. Remove curtain CSS
            for target in css_targets:
                if target in content:
                    content = content.replace(target, '')
                    print(f"Removed curtain CSS target from {filepath}")
                else:
                    print(f"Warning: CSS target not found in {filepath}: {target[:30]}...")
            
            # 3. Remove curtain HTML
            if curtain_html in content:
                content = content.replace(curtain_html, '')
                print(f"Removed curtain HTML from {filepath}")
            else:
                # normalize and try again
                norm_curtain_html = curtain_html.replace('\n', '\n')
                if norm_curtain_html in content:
                    content = content.replace(norm_curtain_html, '')
                    print(f"Removed curtain HTML (normalized) from {filepath}")
                else:
                    print(f"Warning: Curtain HTML not found in {filepath}")
                    
            # 4. Insert prerendered app shell into #root
            target_root = '<div id="root"></div>'
            if target_root in content:
                content = content.replace(target_root, app_shell_html)
                print(f"Inserted app shell HTML into {filepath}")
            else:
                print(f"Warning: Target root div not found in {filepath}")
                
            # 5. Remove curtain JS
            if curtain_js in content:
                content = content.replace(curtain_js, '')
                print(f"Removed curtain JS from {filepath}")
            else:
                norm_curtain_js = curtain_js.replace('\r\n', '\n')
                if norm_curtain_js in content:
                    content = content.replace(norm_curtain_js, '')
                    print(f"Removed curtain JS (normalized) from {filepath}")
                else:
                    print(f"Warning: Curtain JS not found in {filepath}")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully updated {filepath}\n")

if __name__ == '__main__':
    apply_app_shell()
