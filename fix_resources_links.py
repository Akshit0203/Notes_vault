#!/usr/bin/env python3
from pathlib import Path
import re, os

VAULT_ROOT = Path(".").resolve()

# Matches markdown image links like:
# ![image1](../../../resources/abc123.png)
pattern = re.compile(
    r'!\[(?P<alt>[^\]]*)\]\((?:\.\./)+resources/(?P<file>[^)\s]+?\.(?:png|jpe?g|gif|webp|svg))\)',
    re.IGNORECASE
)

# Use counters stored inside a dict (so no nonlocal/global needed)
stats = {"fixed": 0, "warnings": 0}

print("Indexing files in vault (this may take a moment)...")
file_index = {}

# Index every file by filename
for p in VAULT_ROOT.rglob("*"):
    if p.is_file():
        file_index.setdefault(p.name, []).append(p)

print(f"Indexed {sum(len(v) for v in file_index.values())} files across {len(file_index)} unique filenames.")

files_touched = 0

for md in VAULT_ROOT.rglob("*.md"):
    if ".obsidian" in md.parts:
        continue

    text = md.read_text(encoding="utf-8", errors="ignore")
    original = text

    def replace_link(match):
        alt = match.group("alt")
        fname = match.group("file")

        # find actual file in vault
        candidates = file_index.get(fname, [])
        if not candidates:
            print(f"[WARN] {fname} referenced in {md} not found anywhere.")
            stats["warnings"] += 1
            return match.group(0)

        # choose best candidate (closest relative path)
        best = None
        best_score = None
        for c in candidates:
            rel = os.path.relpath(c, md.parent)
            score = (rel.count(".."), len(rel))
            if best is None or score < best_score:
                best = c
                best_score = score

        relpath = os.path.relpath(best, md.parent).replace(os.sep, "/")
        stats["fixed"] += 1

        return f"![{Path(fname).name}]({relpath})"

    new_text = pattern.sub(replace_link, text)

    if new_text != original:
        md.write_text(new_text, encoding="utf-8")
        files_touched += 1

print("\n---- SUMMARY ----")
print(f"Files modified: {files_touched}")
print(f"Links fixed: {stats['fixed']}")
print(f"Warnings (missing files): {stats['warnings']}")
