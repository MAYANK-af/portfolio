import os

html_paths = [r'e:\New folder\index.html', r'e:\New folder\mayank-yadav-portfolio.html']

for html_path in html_paths:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update backdrop-filter: blur(16px) to blur(10px)
        updated = content.replace('backdrop-filter: blur(16px)', 'backdrop-filter: blur(10px)')
        
        # 2. Update .sphere-3d CSS block to include will-change and transform: translate3d(0,0,0)
        old_sphere_css = """.sphere-3d {
  position: absolute;
  border-radius: 50%;
  /* Boosted opacity for high visual contrast */
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.22) 0%, rgba(255, 255, 255, 0.08) 40%, rgba(255, 255, 255, 0.02) 85%, rgba(255, 255, 255, 0) 100%);
  box-shadow: inset -6px -6px 16px rgba(255, 255, 255, 0.05), inset 4px 4px 12px rgba(255, 255, 255, 0.12), 0 0 30px rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  pointer-events: none;
  z-index: 0;
  animation: float-slow 15s ease-in-out infinite alternate;
}"""

        new_sphere_css = """.sphere-3d {
  position: absolute;
  border-radius: 50%;
  /* Boosted opacity for high visual contrast */
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.22) 0%, rgba(255, 255, 255, 0.08) 40%, rgba(255, 255, 255, 0.02) 85%, rgba(255, 255, 255, 0) 100%);
  box-shadow: inset -6px -6px 16px rgba(255, 255, 255, 0.05), inset 4px 4px 12px rgba(255, 255, 255, 0.12), 0 0 30px rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  pointer-events: none;
  z-index: 0;
  will-change: transform;
  transform: translate3d(0, 0, 0);
  animation: float-slow 15s ease-in-out infinite alternate;
}

/* Scroll Performance Optimizer */
.disable-hover, .disable-hover * {
  pointer-events: none !important;
}"""

        updated = updated.replace(old_sphere_css, new_sphere_css)
        
        # 3. Replace section 9 JS with the optimized requestAnimationFrame & scroll hover-disable version
        old_js_block = """// ===== 9. 3D CARD TILT & SPOTLIGHT EFFECT (EVENT DELEGATION) =====
(function(){
  var currentCard = null;
  
  document.addEventListener("mousemove", function(e){
    var target = e.target;
    if(!target) return;
    
    // Find closest card element
    var card = target.closest("article, a[class*='border'][class*='rounded'], button[class*='border'][class*='rounded'], .glass");
    
    if(currentCard && currentCard !== card) {
      resetCard(currentCard);
      currentCard = null;
    }
    
    if(!card) return;
    
    if(currentCard !== card) {
      currentCard = card;
      card.style.transformStyle = "preserve-3d";
      card.style.transition = "transform 0.1s cubic-bezier(0.25,0.46,0.45,0.94), box-shadow 0.1s ease";
    }
    
    var rect = card.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;
    
    card.style.setProperty("--mouse-x", x + "px");
    card.style.setProperty("--mouse-y", y + "px");
    
    var px = x / rect.width;
    var py = y / rect.height;
    var tiltX = (0.5 - py) * 8; // Max 8 degrees tilt
    var tiltY = (px - 0.5) * 8;
    
    card.style.transform = "perspective(1000px) rotateX(" + tiltX + "deg) rotateY(" + tiltY + "deg) scale3d(1.015,1.015,1.015)";
  }, {passive: true});
  
  document.addEventListener("mouseleave", function(e){
    if(currentCard) {
      resetCard(currentCard);
      currentCard = null;
    }
  }, {passive: true});
  
  function resetCard(card) {
    card.style.transition = "transform 0.5s cubic-bezier(0.25,0.46,0.45,0.94), box-shadow 0.5s ease";
    card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1,1,1)";
  }
})();"""

        new_js_block = """// ===== 9. 3D CARD TILT & SPOTLIGHT EFFECT (EVENT DELEGATION) =====
(function(){
  var currentCard = null;
  var isScrolling = false;
  var scrollTimeout;
  
  window.addEventListener("scroll", function() {
    isScrolling = true;
    clearTimeout(scrollTimeout);
    if (!document.body.classList.contains("disable-hover")) {
      document.body.classList.add("disable-hover");
    }
    scrollTimeout = setTimeout(function() {
      isScrolling = false;
      document.body.classList.remove("disable-hover");
    }, 150);
  }, {passive: true});
  
  var tiltFrame;
  document.addEventListener("mousemove", function(e){
    if (isScrolling) return;
    
    var target = e.target;
    if(!target) return;
    
    if (tiltFrame) cancelAnimationFrame(tiltFrame);
    
    tiltFrame = requestAnimationFrame(function() {
      var card = target.closest("article, a[class*='border'][class*='rounded'], button[class*='border'][class*='rounded'], .glass");
      
      if(currentCard && currentCard !== card) {
        resetCard(currentCard);
        currentCard = null;
      }
      
      if(!card) return;
      
      if(currentCard !== card) {
        currentCard = card;
        card.style.transformStyle = "preserve-3d";
        card.style.transition = "transform 0.1s cubic-bezier(0.25,0.46,0.45,0.94), box-shadow 0.1s ease";
      }
      
      var rect = card.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      
      card.style.setProperty("--mouse-x", x + "px");
      card.style.setProperty("--mouse-y", y + "px");
      
      var px = x / rect.width;
      var py = y / rect.height;
      var tiltX = (0.5 - py) * 8;
      var tiltY = (px - 0.5) * 8;
      
      card.style.transform = "perspective(1000px) rotateX(" + tiltX + "deg) rotateY(" + tiltY + "deg) scale3d(1.015,1.015,1.015)";
    });
  }, {passive: true});
  
  document.addEventListener("mouseleave", function(e){
    if(currentCard) {
      resetCard(currentCard);
      currentCard = null;
    }
  }, {passive: true});
  
  function resetCard(card) {
    card.style.transition = "transform 0.5s cubic-bezier(0.25,0.46,0.45,0.94), box-shadow 0.5s ease";
    card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1,1,1)";
  }
})();"""

        updated = updated.replace(old_js_block, new_js_block)
        
        if updated != content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Applied scroll optimizations successfully in {os.path.basename(html_path)}")
        else:
            print(f"No matches found or already optimized in {os.path.basename(html_path)}")
    else:
        print(f"Error: {html_path} not found")
