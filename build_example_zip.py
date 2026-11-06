"""Rebuild example-project.zip from the example-project/ folder.

Run from the course folder after changing anything in example-project/:
    python3 build_example_zip.py
"""
import os
import zipfile

SRC = "example-project"
OUT = "example-project.zip"
SKIP_DIRS = {".quarto", ".Rproj.user", "__pycache__"}

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(SRC):
        # skip build caches; sort so the zip order is stable
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            if name == ".DS_Store":
                continue
            path = os.path.join(root, name)
            z.write(path, path)
print(f"Wrote {OUT}")
