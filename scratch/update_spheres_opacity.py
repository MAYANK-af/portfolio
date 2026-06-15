import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

new_css = """
/* ========== 3D FLOATING SPHERES IN LAST 3 SECTIONS ========== */
.sphere-3d {
  position: absolute;
  border-radius: 50%;
  /* Boosted opacity for high visual contrast */
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.22) 0%, rgba(255, 255, 255, 0.08) 40%, rgba(255, 255, 255, 0.02) 85%, rgba(255, 255, 255, 0) 100%);
  box-shadow: inset -6px -6px 16px rgba(255, 255, 255, 0.05), inset 4px 4px 12px rgba(255, 255, 255, 0.12), 0 0 30px rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  pointer-events: none;
  z-index: 0;
  animation: float-slow 15s ease-in-out infinite alternate;
}
@keyframes float-slow {
  0% { transform: translate(0, 0) rotate(0deg); }
  50% { transform: translate(25px, -25px) scale(1.05); }
  100% { transform: translate(-15px, 20px) scale(0.95); }
}
@keyframes float-slower {
  0% { transform: translate(0, 0) rotate(0deg); }
  50% { transform: translate(-30px, 30px) scale(0.95); }
  100% { transform: translate(20px, -20px) scale(1.05); }
}
</style>"""

new_js = """
// ===== 10. INJECT 3D FLOATING SPHERES =====
(function() {
  function injectSpheres() {
    var journal = document.getElementById("journal");
    if (journal && !journal.querySelector(".sphere-3d")) {
      var s1 = document.createElement("div");
      s1.className = "sphere-3d w-40 h-40 left-10 top-1/4";
      s1.style.animationDuration = "18s";
      journal.appendChild(s1);
    }
    
    var testimonials = document.getElementById("testimonials");
    if (testimonials && !testimonials.querySelector(".sphere-3d")) {
      var s2 = document.createElement("div");
      s2.className = "sphere-3d w-48 h-48 right-12 top-1/3";
      s2.style.animationDuration = "22s";
      s2.style.animationName = "float-slower";
      testimonials.appendChild(s2);
    }
    
    var contact = document.getElementById("contact");
    if (contact && !contact.querySelector(".sphere-3d")) {
      var s3 = document.createElement("div");
      s3.className = "sphere-3d w-36 h-36 left-[10%] bottom-10";
      s3.style.animationDuration = "16s";
      contact.appendChild(s3);
    }
    
    // Continuous polling handles client-side React re-mounts on route change
    setTimeout(injectSpheres, 1000);
  }
  injectSpheres();
})();
</script>"""

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We need to replace the old CSS spheres block with the new one
        # Let's search for the start of the CSS sphere block
        start_css_marker = '/* ========== 3D FLOATING SPHERES IN LAST 3 SECTIONS ========== */'
        if start_css_marker in content:
            # Find the end of the style tag after the marker
            idx_start = content.find(start_css_marker)
            idx_end = content.find('</style>', idx_start) + len('</style>')
            old_css_block = content[idx_start:idx_end]
            content = content.replace(old_css_block, new_css)
            print(f"Updated CSS block in {os.path.basename(html_path)}")
        else:
            print(f"Could not find old CSS block in {os.path.basename(html_path)}")
            
        # We need to replace the old JS spheres block with the new one
        start_js_marker = '// ===== 10. INJECT 3D FLOATING SPHERES ====='
        if start_js_marker in content:
            idx_start = content.find(start_js_marker)
            idx_end = content.find('</script>', idx_start) + len('</script>')
            old_js_block = content[idx_start:idx_end]
            content = content.replace(old_js_block, new_js)
            print(f"Updated JS block in {os.path.basename(html_path)}")
        else:
            print(f"Could not find old JS block in {os.path.basename(html_path)}")
            
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    else:
        print(f"Error: {html_path} not found")
