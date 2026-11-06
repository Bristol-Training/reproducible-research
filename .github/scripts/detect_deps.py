"""Work out what the website's code chunks need, for the publish Action.

Reads the pages listed under `project: render:` in _quarto.yml and looks for
code chunks that Quarto runs (```{r} and ```{python}, not displayed-only
blocks like ```{.r} or ```{{r}}). Prints GitHub Actions outputs:

    r=true|false          any R chunks?
    python=true|false     any Python chunks?
    r_packages=...        R packages used in R chunks (library(), require(), pkg::)
    py_packages=...       pip packages imported in Python chunks (import x, from x import y)

Run it locally to check: python3 .github/scripts/detect_deps.py
"""
import os
import re
import sys

QUARTO_YML = "_quarto.yml"

CHUNK = re.compile(r"^\s*```+\s*\{(r|python)[\s,}]", re.IGNORECASE)
FENCE_END = re.compile(r"^\s*```+\s*$")
R_PKG = re.compile(
    r"(?:library|require|requireNamespace)\(\s*[\"']?([A-Za-z][\w.]*)"
    r"|\b([A-Za-z][\w.]*):::?"
)
PY_IMPORT = re.compile(r"^\s*(?:from\s+([A-Za-z_]\w*)[\w.]*\s+import|import\s+(.+))")
# Import names that differ from the name used to install the package
PY_INSTALL_NAME = {
    "sklearn": "scikit-learn", "skimage": "scikit-image", "PIL": "pillow",
    "cv2": "opencv-python", "yaml": "pyyaml", "bs4": "beautifulsoup4",
    "dateutil": "python-dateutil", "docx": "python-docx", "pptx": "python-pptx",
    "Bio": "biopython", "attr": "attrs", "dotenv": "python-dotenv",
    "IPython": "ipython", "OpenSSL": "pyopenssl", "jwt": "pyjwt",
}
BASE_R = {"base", "stats", "utils", "graphics", "grDevices", "methods",
          "datasets", "tools", "grid", "parallel", "splines", "stats4", "tcltk"}


def rendered_files():
    """Files under `project: render:` in _quarto.yml (or every root .qmd)."""
    files, in_render = [], False
    with open(QUARTO_YML) as f:
        for line in f:
            if re.match(r"^\s*render:\s*$", line):
                in_render = True
                continue
            if in_render:
                m = re.match(r"^\s*-\s*(\S+)", line)
                if m:
                    files.append(m.group(1))
                elif line.strip() and not line.lstrip().startswith("#"):
                    break
    return files or sorted(p for p in os.listdir(".") if p.endswith(".qmd"))


def scan(path):
    langs, r_pkgs, py_pkgs, lang = set(), set(), set(), None
    with open(path, encoding="utf-8") as f:
        for line in f:
            if lang is None:
                m = CHUNK.match(line)
                if m:
                    lang = m.group(1).lower()
                    langs.add(lang)
            elif FENCE_END.match(line):
                lang = None
            elif lang == "r":
                code = line.split("#", 1)[0]
                for a, b in R_PKG.findall(code):
                    r_pkgs.add(a or b)
            elif lang == "python":
                m = PY_IMPORT.match(line.split("#", 1)[0])
                if m and m.group(1):
                    py_pkgs.add(m.group(1))
                elif m:
                    # import a, b.c as d  ->  a, b
                    for part in m.group(2).split(","):
                        name = part.strip().split(" ")[0].split(".")[0]
                        if name.isidentifier():
                            py_pkgs.add(name)
    return langs, r_pkgs, py_pkgs


langs, r_pkgs, py_pkgs = set(), set(), set()
for path in rendered_files():
    if os.path.exists(path):
        l, r, py = scan(path)
        langs |= l
        r_pkgs |= r
        py_pkgs |= py

r_pkgs -= BASE_R
py_pkgs = {PY_INSTALL_NAME.get(p, p) for p in py_pkgs
           if p not in sys.stdlib_module_names and p != "__future__"}
outputs = {
    "r": str("r" in langs).lower(),
    "python": str("python" in langs).lower(),
    # knitr and rmarkdown are what Quarto uses to run R chunks
    "r_packages": " ".join(f"any::{p}" for p in sorted(r_pkgs | {"knitr", "rmarkdown"})),
    # jupyter is what Quarto uses to run Python chunks
    "py_packages": " ".join(sorted(py_pkgs | {"jupyter"})),
}

out = os.environ.get("GITHUB_OUTPUT")
with open(out, "a") if out else open(os.devnull, "w") as f:
    for k, v in outputs.items():
        print(f"{k}={v}")
        f.write(f"{k}={v}\n")
