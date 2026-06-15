import os

def bump_photo_version():
    files = [
        'index.html',
        'mayank-yadav-portfolio.html',
        'static/js/main.e1c64cec.js'
    ]
    
    old_str = '/portfolio/static/media/profile_photo.jpeg'
    new_str = '/portfolio/static/media/profile_photo.jpeg?v=22'
    
    for filename in files:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_str in content:
                count = content.count(old_str)
                content = content.replace(old_str, new_str)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {count} occurrences in {filename}")
            else:
                # check if it already has a query parameter or if it was already updated
                if new_str in content:
                    print(f"Already updated in {filename}")
                else:
                    print(f"Warning: String not found in {filename}")

if __name__ == '__main__':
    bump_photo_version()
