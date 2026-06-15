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
chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

driver = None
try:
    print("Launching headless Chrome...")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(20)
    
    url = "https://mayank-af.github.io/portfolio/"
    driver.get(url)
    time.sleep(3)
    
    # Let's scroll down step by step to trigger any scroll event listeners
    print("Scrolling page to trigger scroll handlers...")
    for y in range(0, 5000, 500):
        driver.execute_script(f"window.scrollTo(0, {y});")
        time.sleep(0.3)
        
    print("\n=== CONSOLE LOGS ===")
    logs = driver.get_log('browser')
    for entry in logs:
        print(f"[{entry['level']}] {entry['message']}")
        
except Exception as e:
    print(f"Error: {e}")
finally:
    if driver:
        driver.quit()
    print("Done.")
