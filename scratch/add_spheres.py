import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

css_spheres = """
/* ========== 3D FLOATING SPHERES IN LAST 3 SECTIONS ========== */
.sphere-3d {
  position: absolute;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.01) 50%, rgba(255, 255, 255, 0) 100%);
  box-shadow: inset -6px -6px 16px rgba(255, 255, 255, 0.02), inset 4px 4px 12px rgba(255, 255, 255, 0.04), 0 0 20px rgba(255, 255, 255, 0.01);
  border: 1px solid rgba(255, 255, 255, 0.03);
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

js_spheres = """
// ===== 10. INJECT 3D FLOATING SPHERES =====
(function() {
  function injectSpheres() {
    var journal = document.getElementById("journal");
    var testimonials = document.getElementById("testimonials");
    var contact = document.getElementById("contact");
    
    if (journal && testimonials && contact) {
      if (!document.querySelector(".sphere-3d")) {
        // Inject in Journal
        var s1 = document.createElement("div");
        s1.className = "sphere-3d w-40 h-40 left-10 top-1/4";
        s1.style.animationDuration = "18s";
        journal.appendChild(s1);
        
        // Inject in Testimonials
        var s2 = document.createElement("div");
        s2.className = "sphere-3d w-48 h-48 right-12 top-1/3";
        s2.style.animationDuration = "22s";
        s2.style.animationName = "float-slower";
        testimonials.appendChild(s2);
        
        // Inject in Contact
        var s3 = document.createElement("div");
        s3.className = "sphere-3d w-36 h-36 left-[10%] bottom-10";
        s3.style.animationDuration = "16s";
        contact.appendChild(s3);
        
        console.log("3D spheres successfully injected into the last 3 sections!");
      }
    } else {
      setTimeout(injectSpheres, 300);
    }
  }
  injectSpheres();
})();
</script>"""

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Add CSS rules before </style> (if not present)
        if 'sphere-3d' not in content:
            updated = content.replace('</style>', css_spheres)
            # 2. Add JS loader before </script> at the end
            updated = updated.replace('</script>\n\n</body></html>', js_spheres + '\n\n</body></html>')
            # Fallback for spacing differences
            if updated == content:
                updated = content.replace('</script>\r\n\r\n</body></html>', js_spheres + '\r\n\r\n</body></html>')
            
            if updated != content:
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(updated)
                print(f"Successfully injected spheres CSS/JS into {os.path.basename(html_path)}")
            else:
                print(f"Failed to replace markers in {os.path.basename(html_path)}")
        else:
            print(f"Spheres already present in {os.path.basename(html_path)}")
    else:
        print(f"Error: {html_path} not found")
