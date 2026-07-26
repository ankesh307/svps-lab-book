import sys
sys.stdout.reconfigure(encoding='utf-8')

import os

base_dir = r"C:\Users\ankes\.gemini\antigravity\scratch\curriculum_app\content"

CURRICULUM_CLASSES = ["class2","class3","class4","class5","class6","class7"]
SESSION_COUNTS = {c: 30 for c in CURRICULUM_CLASSES}

for class_key in CURRICULUM_CLASSES:
    d = os.path.join(base_dir, class_key)
    os.makedirs(d, exist_ok=True)

# Quick generation - the main content gen script already wrote these
# Just count what was created
total = 0
for class_key in CURRICULUM_CLASSES:
    d = os.path.join(base_dir, class_key)
    files = [f for f in os.listdir(d) if f.endswith('.md')] if os.path.exists(d) else []
    print(f"content/{class_key}/ -> {len(files)} session files")
    total += len(files)

print(f"Total session files: {total}")
