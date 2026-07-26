import json
import sys
import os

# Read data from generate_all_content.py
sys.path.append(".")
import generate_all_content as gen

robotics_json = {}
ai_json = {}

for ck in gen.CLASSES:
    robotics_json[ck] = []
    for (num, title, desc, tags) in gen.ROBOTICS_TOPICS[ck]:
        # Read complete markdown content
        filepath = os.path.join(gen.base_dir, ck, "robotics", f"session{num:02d}.md")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                md_content = f.read()
        except:
            md_content = f"# Session {num}: {title}\n\nNo detailed content available."

        robotics_json[ck].append({
            "num": num,
            "t": title,
            "d": desc,
            "tags": tags.split("|"),
            "content": md_content
        })

    ai_json[ck] = []
    for (num, title, desc, tags) in gen.AI_TOPICS[ck]:
        # Read complete markdown content
        filepath = os.path.join(gen.base_dir, ck, "ai", f"session{num:02d}.md")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                md_content = f.read()
        except:
            md_content = f"# Session {num}: {title}\n\nNo detailed content available."

        ai_json[ck].append({
            "num": num,
            "t": title,
            "d": desc,
            "tags": tags.split("|"),
            "content": md_content
        })

# Let's read the current HTML templates
start_marker = "// ─── DYNAMIC DATA START ───"
end_marker = "// ─── DYNAMIC DATA END ───"

js_data = f"""
const ROBOTICS_DATA = {json.dumps(robotics_json, indent=4)};
const AI_DATA = {json.dumps(ai_json, indent=4)};
"""

# Let's replace in both HTML templates
for filename in ["NextGen_Curriculum.html", "index.html"]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        if start_marker in content and end_marker in content:
            parts = content.split(start_marker)
            subparts = parts[1].split(end_marker)
            new_content = parts[0] + start_marker + js_data + end_marker + subparts[1]
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Successfully injected 360 session lists and contents into {filename}!")
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
