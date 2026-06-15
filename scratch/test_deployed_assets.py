import urllib.request
import urllib.error

urls = [
    "https://mayank-af.github.io/portfolio/static/media/cover_fake_news.jpg",
    "https://mayank-af.github.io/portfolio/static/media/cover_health_ai.jpg",
    "https://mayank-af.github.io/portfolio/static/media/cover_asus_tuf.jpg",
    "https://mayank-af.github.io/portfolio/static/media/cover_porsche.jpg",
    "https://mayank-af.github.io/portfolio/static/media/profile_photo.jpeg",
    "https://mayank-af.github.io/portfolio/static/js/main.e1c64cec.js?v=13"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            print(f"SUCCESS {response.status}: {url}")
    except urllib.error.HTTPError as e:
        print(f"FAILED {e.code}: {url}")
    except Exception as e:
        print(f"ERROR: {url} -> {e}")
