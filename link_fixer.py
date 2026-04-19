import os
import re

def fix_links():
    md_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    
    # Pattern to match the specific absolute URL
    base_url = "https://mave9055.github.io/wrh-master-curriculum/"
    # We want to catch both the base URL and sub-paths
    pattern = re.compile(r'\(https://mave9055\.github\.io/wrh-master-curriculum/([^)]*)\)')
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        matches = pattern.findall(content)
        
        if matches:
            dir_path = os.path.dirname(md_file)
            # How many levels deep are we?
            # . -> 0
            # ./Part-I -> 1
            depth = 0 if dir_path == "." else len(dir_path.split(os.sep))
            
            for match in matches:
                # If match is empty, it's the home page
                if not match:
                    rel_path = "index.md"
                else:
                    rel_path = match
                    if not rel_path.endswith(".md") and not rel_path.endswith("/") and "." not in rel_path.split("/")[-1]:
                        # It's likely a directory, point to index.md
                        rel_path = os.path.join(rel_path, "index.md")
                    elif rel_path.endswith("/"):
                        rel_path = os.path.join(rel_path, "index.md")
                
                # Calculate the relative prefix
                prefix = "../" * depth if depth > 0 else "./"
                final_rel_link = os.path.normpath(os.path.join(prefix, rel_path))
                
                # Replace the absolute link with the relative one
                abs_link = f"({base_url}{match})"
                rel_link = f"({final_rel_link})"
                new_content = new_content.replace(abs_link, rel_link)
        
        if new_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed links in: {md_file}")

if __name__ == "__main__":
    fix_links()
