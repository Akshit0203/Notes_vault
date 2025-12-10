#!/usr/bin/env python3
from pathlib import Path
import re
import os

VAULT_ROOT = Path(".").resolve()

# Matches patterns like:
# ![.../attachments/image.png](attachments/.../image.png)
# or ![[.../attachments/image.png]](attachments/.../image.png)
pattern = re.compile(
    r'(!\[\[?(?:[^\]\(]*?/)?attachments/(?P<file>[^)\]\|]+?\.(?:png|jpe?g|gif|webp|svg))\]?\)\(attachments/[^)\n]*?(?P=file)\))'
    , re.IGNORECASE
)

# We'll rebuild matches more robustly below instead of using the whole group replacement.
# Simpler approach: find occurrences that contain "/attachments/<filename>" in alt or wiki part and also have "(attachments/...<filename>)"

# A broader regex to capture alt part and url:
regex = re.compile(
    r'!\[([^\]]*?/attachments/(?P<file1>[^]\s]+?\.(?:png|jpe?g|gif|webp|svg))|[^\]]*?)\]\(attachments/([^\)]*?/)?(?P<file2>[^)\s]+?\.(?:png|jpe?g|gif|webp|svg))\)',
    re.IGNORECASE
)

counts = {"fixed":0, "files":0, "warnings":0}

for md_path in VAULT_ROOT.rglob("*.md"):
    if ".obsidian" in md_path.parts:
        continue

    text = md_path.read_text(encoding="utf-8", errors="ignore")
    original = text
    changed = False

    def repl(m):
        # file might be in group file1 or file2
        file1 = m.group("file1")
        file2 = m.group("file2")
        filename = file2 or file1
        if not filename:
            return m.group(0)

        # Normalize filename (strip any leading path segments)
        filename_only = Path(filename).name

        # Search upward from the note's folder for attachments/filename
        current = md_path.parent
        found = None
        while True:
            candidate = current / "attachments" / filename_only
            if candidate.exists():
                found = candidate
                break
            if current == VAULT_ROOT:
                break
            current = current.parent

        # If not found above, also check root attachments
        if not found:
            root_candidate = VAULT_ROOT / "attachments" / filename_only
            if root_candidate.exists():
                found = root_candidate

        if not found:
            # warn and leave original
            print(f"[WARN] {filename_only} referenced in {md_path} but not found.")
            counts["warnings"] += 1
            return m.group(0)

        # Compute relative path from the md file to the found file
        rel = os.path.relpath(found, md_path.parent).replace(os.sep, "/")
        counts["fixed"] += 1
        return f"![{filename_only}]({rel})"

    new_text = regex.sub(repl, text)

    if new_text != original:
        md_path.write_text(new_text, encoding="utf-8")
        counts["files"] += 1
        changed = True

print(f"Done. Updated {counts['files']} files, fixed {counts['fixed']} links, warnings {counts['warnings']}.")
