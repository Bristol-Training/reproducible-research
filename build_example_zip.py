"""Rebuild example-project.zip from the example-project/ folder.

Run from the course folder after changing anything in example-project/:
    python3 build_example_zip.py
"""
import os
import zipfile

SRC = "example-project"
OUT = "example-project.zip"

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _dirs, files in os.walk(SRC):
        for name in sorted(files):
            if name == ".DS_Store":
                continue
            path = os.path.join(root, name)
            z.write(path, path)
print(f"Wrote {OUT}")
