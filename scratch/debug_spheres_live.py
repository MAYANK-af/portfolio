from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = None
try:
    print("Launching headless Chrome...")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(20)
    
    url = "https://mayank-af.github.io/portfolio/"
    print(f"Loading URL: {url}")
    driver.get(url)
    
    # Wait for React to mount and our script to inject
    print("Waiting for page load and sphere injection...")
    time.sleep(5)
    
    sections = ["journal", "testimonials", "contact"]
    for sec_id in sections:
        try:
            sec = driver.find_element("id", sec_id)
            print(f"\nSection '{sec_id}': FOUND")
            # Find spheres inside this section
            spheres = sec.find_elements("class name", "sphere-3d")
            print(f"  Number of .sphere-3d elements: {len(spheres)}")
            for idx, sphere in enumerate(spheres):
                # Get styles
                display = sphere.value_of_css_property("display")
                visibility = sphere.value_of_css_property("visibility")
                opacity = sphere.value_of_css_property("opacity")
                z_index = sphere.value_of_css_property("z-index")
                width = sphere.value_of_css_property("width")
                height = sphere.value_of_css_property("height")
                background = sphere.value_of_css_property("background")
                position = sphere.value_of_css_property("position")
                location = sphere.location
                size = sphere.size
                print(f"  Sphere {idx+1}:")
                print(f"    Position: {position} at {location}")
                print(f"    Size: {width} x {height} (rect size: {size})")
                print(f"    Display: {display}, Visibility: {visibility}, Opacity: {opacity}, Z-Index: {z_index}")
                print(f"    Background: {background[:100]}...")
        except Exception as e:
            print(f"\nSection '{sec_id}': NOT FOUND or Error: {e}")
            
except Exception as e:
    print(f"Global Error: {e}")
finally:
    if driver:
        driver.quit()
    print("Done.")
