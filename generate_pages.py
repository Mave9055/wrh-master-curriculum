import os
import re

def parse_markdown_index(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'^# (.*)', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Part Index"
    
    # Extract sessions
    sessions = []
    # Match pattern like - [Session 01 Title](./Filename.md)
    matches = re.finditer(r'- \[(.*?)\]\((.*?)\)', content)
    for match in matches:
        label = match.group(1)
        target = match.group(2)
        # Convert relative target to correct path for HTML in curriculum/
        # Now using session-viewer.html?file=../Part-X/Session_X.md
        part_dir = os.path.basename(os.path.dirname(file_path))
        clean_target = target.lstrip('./')
        final_target = f"session-viewer.html?file=curriculum/../{part_dir}/{clean_target}"
        sessions.append({'label': label, 'target': final_target})
    
    return title, sessions

def generate_html(part_id, title, sessions, output_path):
    # Use the provided template style
    sessions_html = ""
    for session in sessions:
        sessions_html += f"""
                <a href="{session['target']}" class="p-4 bg-zinc-900 border border-zinc-800 rounded-xl hover:border-amber-500 transition-colors flex justify-between items-center group">
                    <span class="text-zinc-300 group-hover:text-white transition-colors text-sm">{session['label']}</span>
                    <svg class="w-4 h-4 text-zinc-600 group-hover:text-amber-500 flex-shrink-0 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                </a>"""

    html_content = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | WRH Master Curriculum</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        dark: '#0a0a0a',
                        zinc: {{ 950: '#09090b', 900: '#18181b', 800: '#27272a' }},
                        amber: {{ 500: '#f59e0b', 600: '#d97706' }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        body {{ font-family: 'Inter', sans-serif; }}
        .sticky-nav {{ backdrop-filter: blur(12px); background-color: rgba(9, 9, 11, 0.8); }}
    </style>
</head>
<body class="bg-zinc-950 text-zinc-300 selection:bg-amber-500/30 selection:text-amber-500">

    <!-- Navigation -->
    <nav class="sticky-nav sticky top-0 z-50 border-b border-zinc-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <div class="flex items-center">
                    <a href="../index.html" class="text-xl font-bold text-white tracking-tight">
                        WRH <span class="text-amber-500">Master</span>
                    </a>
                </div>
                <div class="hidden md:flex space-x-8">
                    <a href="../index.html" class="text-sm font-medium hover:text-white transition-colors">Home</a>
                    <a href="index.html" class="text-sm font-medium text-white hover:text-amber-500 transition-colors">Curriculum</a>
                    <a href="../start-here.html" class="text-sm font-medium hover:text-white transition-colors">Start Here</a>
                    <a href="../pilot-package.html" class="text-sm font-medium hover:text-white transition-colors">Pilot Package</a>
                    <a href="../contact.html" class="text-sm font-medium hover:text-white transition-colors">Contact</a>
                </div>
            </div>
        </div>
    </nav>

    <main class="py-20">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-12">
                <a href="index.html" class="text-sm font-bold text-amber-500 hover:text-amber-400 mb-4 inline-block">&larr; Back to Index</a>
                <h1 class="text-4xl font-extrabold text-white mb-2">{title}</h1>
                <p class="text-lg text-zinc-400">Educational psychointervention focused on system logic and physiological adaptation.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                {sessions_html}
            </div>
        </div>
    </main>

    <footer class="bg-zinc-950 border-t border-zinc-900 py-12 mt-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p class="text-zinc-500 text-sm">
                Proprietary Intellectual Property of Capitol Contracts LLC. All Rights Reserved.<br/>
                UEI: HH77KN5AV5X7 | CAGE: 9ZFJ6
            </p>
        </div>
    </footer>
</body>
</html>
"""
    with open(output_path, 'w') as f:
        f.write(html_content)

mapping = {
    'Part-I': 'part-1.html',
    'Part-II': 'part-2.html',
    'Part-III': 'part-3.html',
    'Part-IV': 'part-4.html'
}

for part, filename in mapping.items():
    md_path = f"{part}/index.md"
    html_path = f"curriculum/{filename}"
    if os.path.exists(md_path):
        title, sessions = parse_markdown_index(md_path)
        generate_html(part, title, sessions, html_path)
        print(f"Generated {html_path}")
