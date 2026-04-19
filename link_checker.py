import os
import re
from urllib.parse import urlparse

def check_links():
    md_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    
    results = []
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            links = link_pattern.findall(content)
            
            for text, link in links:
                if link.startswith("https://mave9055.github.io/wrh-master-curriculum/"):
                    # Treat these as internal links
                    relative_part = link.replace("https://mave9055.github.io/wrh-master-curriculum/", "")
                    target_path = os.path.normpath(os.path.join(".", relative_part))
                    if not os.path.exists(target_path):
                        results.append({
                            "file": md_file,
                            "text": text,
                            "link": link,
                            "resolved": target_path
                        })
                    continue
                elif link.startswith("http"):
                    continue
                if link.startswith("#"):
                    # Skip anchor links
                    continue
                
                # Clean link (remove query params/anchors)
                clean_link = link.split("#")[0].split("?")[0]
                if not clean_link:
                    continue
                
                # Resolve relative path
                dir_path = os.path.dirname(md_file)
                target_path = os.path.normpath(os.path.join(dir_path, clean_link))
                
                # Check if file or directory exists
                exists = os.path.exists(target_path)
                if not exists:
                    # Special case: check if it's a directory missing index.md
                    if os.path.isdir(target_path) and os.path.exists(os.path.join(target_path, "index.md")):
                        exists = True
                
                if not exists:
                    results.append({
                        "file": md_file,
                        "text": text,
                        "link": link,
                        "resolved": target_path
                    })
    
    return results

if __name__ == "__main__":
    broken = check_links()
    if not broken:
        print("No broken internal links found.")
    else:
        print(f"Found {len(broken)} broken internal links:")
        for b in broken:
            print(f"File: {b['file']} | Text: {b['text']} | Link: {b['link']}")
