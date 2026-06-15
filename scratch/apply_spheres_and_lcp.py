import os

def apply_updates():
    html_files = [
        'index.html',
        'mayank-yadav-portfolio.html'
    ]
    
    target_curtain_css = '/* ========== 8. PAGE LOAD TRANSITION ========== */\n#page-curtain{position:fixed;inset:0;z-index:10000;background:#060608;display:flex;align-items:center;justify-content:center;transition:opacity 0.6s cubic-bezier(0.16,1,0.3,1),transform 0.6s cubic-bezier(0.16,1,0.3,1)}'
    replacement_curtain_css = '/* ========== 8. PAGE LOAD TRANSITION ========== */\n#page-curtain{position:fixed;inset:0;z-index:10000;background:#060608;display:flex;align-items:center;justify-content:center;transition:opacity 0.25s cubic-bezier(0.16,1,0.3,1),transform 0.25s cubic-bezier(0.16,1,0.3,1)}\n#academic, #skills, #journal, #testimonials, #contact {\n  content-visibility: auto;\n  contain-intrinsic-size: 800px;\n}'
    
    target_root = '<div id="root" style="content-visibility:auto"></div>'
    replacement_root = '<div id="root"></div>'
    
    target_curtain_js = """// ===== 8. PAGE LOAD TRANSITION =====
(function(){
  function liftCurtain(){
    var curtain=document.getElementById("page-curtain");
    if(!curtain)return;
    var root=document.getElementById("root");
    function check(){
      if(root&&root.children.length>0){
        setTimeout(function(){
          curtain.classList.add("lift");
          setTimeout(function(){curtain.remove()},800);
        },300);
      }else{
        setTimeout(check,100);
      }
    }
    check();
  }"""
  
    replacement_curtain_js = """// ===== 8. PAGE LOAD TRANSITION =====
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
  }"""

    target_spheres_js = """// ===== 10. INJECT 3D FLOATING SPHERES =====
(function() {
  function injectSpheres() {
    var journal = document.getElementById("journal");
    if (journal && !journal.querySelector(".sphere-3d")) {
      var s1 = document.createElement("div");
      s1.className = "sphere-3d";
      s1.style.width = "160px";
      s1.style.height = "160px";
      s1.style.left = "40px";
      s1.style.top = "25%";
      s1.style.animationDuration = "18s";
      journal.appendChild(s1);
    }
    
    var testimonials = document.getElementById("testimonials");
    if (testimonials && !testimonials.querySelector(".sphere-3d")) {
      var s2 = document.createElement("div");
      s2.className = "sphere-3d";
      s2.style.width = "192px";
      s2.style.height = "192px";
      s2.style.right = "48px";
      s2.style.top = "33%";
      s2.style.animationDuration = "22s";
      s2.style.animationName = "float-slower";
      testimonials.appendChild(s2);
    }
    
    var contact = document.getElementById("contact");
    if (contact && !contact.querySelector(".sphere-3d")) {
      var s3 = document.createElement("div");
      s3.className = "sphere-3d";
      s3.style.width = "144px";
      s3.style.height = "144px";
      s3.style.left = "10%";
      s3.style.bottom = "40px";
      s3.style.animationDuration = "16s";
      contact.appendChild(s3);
    }
    
    // Continuous polling handles client-side React re-mounts on route change
    setTimeout(injectSpheres, 1000);
  }
  injectSpheres();
})();"""

    replacement_spheres_js = """// ===== 10. INJECT 3D FLOATING SPHERES =====
(function() {
  function injectSpheres() {
    var journal = document.getElementById("journal");
    if (journal && !journal.querySelector(".sphere-3d")) {
      var s1 = document.createElement("div");
      s1.className = "sphere-3d";
      s1.style.width = "160px";
      s1.style.height = "160px";
      s1.style.left = "40px";
      s1.style.top = "25%";
      s1.style.animationDuration = "18s";
      journal.appendChild(s1);
    }
    
    var testimonials = document.getElementById("testimonials");
    if (testimonials && !testimonials.querySelector(".sphere-3d")) {
      var s2 = document.createElement("div");
      s2.className = "sphere-3d";
      s2.style.width = "192px";
      s2.style.height = "192px";
      s2.style.right = "48px";
      s2.style.top = "33%";
      s2.style.animationDuration = "22s";
      s2.style.animationName = "float-slower";
      testimonials.appendChild(s2);
    }
    
    var contact = document.getElementById("contact");
    if (contact && !contact.querySelector(".sphere-3d")) {
      var s3 = document.createElement("div");
      s3.className = "sphere-3d";
      s3.style.width = "144px";
      s3.style.height = "144px";
      s3.style.left = "10%";
      s3.style.bottom = "40px";
      s3.style.animationDuration = "16s";
      contact.appendChild(s3);
    }
    
    var academic = document.getElementById("academic");
    if (academic && !academic.querySelector(".sphere-3d")) {
      var s4 = document.createElement("div");
      s4.className = "sphere-3d";
      s4.style.width = "180px";
      s4.style.height = "180px";
      s4.style.right = "80px";
      s4.style.top = "15%";
      s4.style.animationDuration = "20s";
      s4.style.animationName = "float-slower";
      academic.appendChild(s4);
    }
    
    var skills = document.getElementById("skills");
    if (skills && !skills.querySelector(".sphere-3d")) {
      var s5 = document.createElement("div");
      s5.className = "sphere-3d";
      s5.style.width = "160px";
      s5.style.height = "160px";
      s5.style.left = "40px";
      s5.style.top = "20%";
      s5.style.animationDuration = "18s";
      skills.appendChild(s5);
      
      var s6 = document.createElement("div");
      s6.className = "sphere-3d";
      s6.style.width = "128px";
      s6.style.height = "128px";
      s6.style.right = "60px";
      s6.style.bottom = "10%";
      s6.style.animationDuration = "15s";
      s6.style.animationName = "float-slower";
      skills.appendChild(s6);
    }
    
    // Continuous polling handles client-side React re-mounts on route change
    setTimeout(injectSpheres, 1000);
  }
  injectSpheres();
})();"""

    for filepath in html_files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Normalize newlines to \n to ensure robust replacements
            content = content.replace('\r\n', '\n')
            
            # 1. Replace curtain CSS
            if target_curtain_css in content:
                content = content.replace(target_curtain_css, replacement_curtain_css)
                print(f"Updated curtain CSS in {filepath}")
            else:
                # Try finding with \r\n normalized
                normalized_target = target_curtain_css.replace('\r\n', '\n')
                if normalized_target in content:
                    content = content.replace(normalized_target, replacement_curtain_css)
                    print(f"Updated curtain CSS (normalized) in {filepath}")
                else:
                    print(f"Warning: Curtain CSS not found in {filepath}")
                    
            # 2. Replace root
            if target_root in content:
                content = content.replace(target_root, replacement_root)
                print(f"Updated root element in {filepath}")
            else:
                print(f"Warning: Root element not found in {filepath}")
                
            # 3. Replace curtain JS
            if target_curtain_js in content:
                content = content.replace(target_curtain_js, replacement_curtain_js)
                print(f"Updated curtain JS in {filepath}")
            else:
                # normalize target_curtain_js newlines
                norm_curtain_js = target_curtain_js.replace('\r\n', '\n')
                if norm_curtain_js in content:
                    content = content.replace(norm_curtain_js, replacement_curtain_js)
                    print(f"Updated curtain JS (normalized) in {filepath}")
                else:
                    print(f"Warning: Curtain JS not found in {filepath}")
                    
            # 4. Replace spheres JS
            if target_spheres_js in content:
                content = content.replace(target_spheres_js, replacement_spheres_js)
                print(f"Updated spheres JS in {filepath}")
            else:
                norm_spheres_js = target_spheres_js.replace('\r\n', '\n')
                if norm_spheres_js in content:
                    content = content.replace(norm_spheres_js, replacement_spheres_js)
                    print(f"Updated spheres JS (normalized) in {filepath}")
                else:
                    print(f"Warning: Spheres JS not found in {filepath}")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Finished updating {filepath}\n")

if __name__ == '__main__':
    apply_updates()
