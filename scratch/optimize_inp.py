import os

def optimize_inp():
    # 1. Optimize HTML mousemove event handlers
    html_files = [
        'index.html',
        'mayank-yadav-portfolio.html'
    ]
    
    target_tilt_js = """  var tiltFrame;
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
  }, {passive: true});"""

    replacement_tilt_js = """  var tiltFrame;
  var lastTarget = null;
  document.addEventListener("mousemove", function(e){
    if (isScrolling) return;
    
    var target = e.target;
    if(!target) return;
    
    if (target !== lastTarget) {
      lastTarget = target;
      var newCard = target.closest("article, a[class*='border'][class*='rounded'], button[class*='border'][class*='rounded'], .glass");
      if (currentCard && currentCard !== newCard) {
        resetCard(currentCard);
      }
      currentCard = newCard;
    }
    
    if(!currentCard) return;
    
    if (tiltFrame) cancelAnimationFrame(tiltFrame);
    
    tiltFrame = requestAnimationFrame(function() {
      if(!currentCard) return;
      
      if (currentCard.style.transformStyle !== "preserve-3d") {
        currentCard.style.transformStyle = "preserve-3d";
        currentCard.style.transition = "transform 0.1s cubic-bezier(0.25,0.46,0.45,0.94), box-shadow 0.1s ease";
      }
      
      var rect = currentCard.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      
      currentCard.style.setProperty("--mouse-x", x + "px");
      currentCard.style.setProperty("--mouse-y", y + "px");
      
      var px = x / rect.width;
      var py = y / rect.height;
      var tiltX = (0.5 - py) * 8;
      var tiltY = (px - 0.5) * 8;
      
      currentCard.style.transform = "perspective(1000px) rotateX(" + tiltX + "deg) rotateY(" + tiltY + "deg) scale3d(1.015,1.015,1.015)";
    });
  }, {passive: true});"""

    for filepath in html_files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace('\r\n', '\n')
            
            # Normalize targets
            norm_target = target_tilt_js.replace('\r\n', '\n')
            
            if norm_target in content:
                content = content.replace(norm_target, replacement_tilt_js)
                print(f"Updated mousemove tilt handler in {filepath}")
            else:
                print(f"Warning: Mousemove target not found in {filepath}")
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

    # 2. Optimize Three.js canvas in JS bundle (add IntersectionObserver to pause loop off-screen)
    js_path = 'static/js/main.e1c64cec.js'
    if os.path.exists(js_path):
        with open(js_path, 'r', encoding='utf-8') as f:
            js_content = f.read()
            
        target_three_js = 'const R=new Hd;let C;const N=()=>{const e=R.getDelta(),t=R.getElapsedTime();b.rotation.x+=.2*e,b.rotation.y+=.3*e;const n=1.4*(E.x-.5),r=1*-(E.y-.5);b.position.x+=.05*(n-b.position.x),b.position.y+=.05*(r-b.position.y),[_,w,S].forEach((n,r)=>{n.rotation.x+=e*(.18+.04*r),n.rotation.y+=e*(.22+.05*r),n.position.y+=.0015*Math.sin(.6*t+r)}),g.rotation.y+=.015*e,c.position.x+=.04*(.6*(E.x-.5)-c.position.x),c.position.y+=.04*(.4*-(E.y-.5)-c.position.y),c.lookAt(0,0,0),u.render(l,c),C=requestAnimationFrame(N)};return C=requestAnimationFrame(N),()=>{cancelAnimationFrame(C),window.removeEventListener("mousemove",M),window.removeEventListener("resize",T),A.disconnect(),v.dispose(),y.dispose(),p.dispose(),m.dispose(),[_,w,S].forEach(e=>{e.geometry.dispose(),e.material.dispose()}),u.dispose(),u.domElement.parentNode===t&&t.removeChild(u.domElement)}'
        
        replacement_three_js = 'const R=new Hd;let C;let isThreeCanvasVisible=true;const N=()=>{if(!isThreeCanvasVisible)return;const e=R.getDelta(),t=R.getElapsedTime();b.rotation.x+=.2*e,b.rotation.y+=.3*e;const n=1.4*(E.x-.5),r=1*-(E.y-.5);b.position.x+=.05*(n-b.position.x),b.position.y+=.05*(r-b.position.y),[_,w,S].forEach((n,r)=>{n.rotation.x+=e*(.18+.04*r),n.rotation.y+=e*(.22+.05*r),n.position.y+=.0015*Math.sin(.6*t+r)}),g.rotation.y+=.015*e,c.position.x+=.04*(.6*(E.x-.5)-c.position.x),c.position.y+=.04*(.4*-(E.y-.5)-c.position.y),c.lookAt(0,0,0),u.render(l,c),C=requestAnimationFrame(N)};const threeObserver=new IntersectionObserver(entries=>{entries.forEach(entry=>{isThreeCanvasVisible=entry.isIntersecting;if(isThreeCanvasVisible){if(!C){R.getDelta();N()}}else{if(C){cancelAnimationFrame(C);C=null}}})},{threshold:0});threeObserver.observe(t);return C=requestAnimationFrame(N),()=>{threeObserver.disconnect();if(C)cancelAnimationFrame(C);window.removeEventListener("mousemove",M);window.removeEventListener("resize",T);A.disconnect();v.dispose();y.dispose();p.dispose();m.dispose();[_,w,S].forEach(e=>{e.geometry.dispose(),e.material.dispose()});u.dispose();u.domElement.parentNode===t&&t.removeChild(u.domElement)}'
        
        if target_three_js in js_content:
            js_content = js_content.replace(target_three_js, replacement_three_js)
            print("Successfully injected IntersectionObserver to pause Three.js rendering loop when off-screen")
        else:
            print("Warning: Target Three.js rendering loop pattern not found in JS bundle")
            
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js_content)

if __name__ == '__main__':
    optimize_inp()
