# Penguin body mass (Python — 2023 project)

A small analysis written in 2023 that prints the average body mass of each penguin species and saves a bar chart. It is used in **Section 3 (Virtual environments)** for the live demo and the lock file activity.

## Contents

- `data/penguins.csv`: the penguin measurements
- `code/analysis.py`: the 2023 script (uses `np.NaN`, which worked in NumPy 1.x but was removed in NumPy 2.0)
- `pyproject.toml`: lists the two packages the author asked for (`pandas` and `matplotlib`)
- `.python-version`: pins Python 3.12
- `uv.lock`: the lock file recording the exact versions of every package (including hidden sub-packages like `numpy 1.26.4`)

## Activity: peek inside the lock file (no coding needed)

Open `pyproject.toml` and `uv.lock` in any text editor:

1. `pyproject.toml` only asks for **2 packages** (`pandas` and `matplotlib`). Count how many `[[package]]` entries are recorded inside `uv.lock` — why are there so many more?
2. Find `name = "numpy"` inside `uv.lock`. Which exact version was recorded when this project worked?

## Optional: run the live demo yourself (needs uv)

Install [uv](https://docs.astral.sh/uv/), then open a terminal in this folder:

1. **Simulate a colleague installing today's latest packages** (`pip install pandas matplotlib`):
   ```bash
   uv run --no-project --with pandas --with matplotlib code/analysis.py
   ```
   It **crashes** with `AttributeError: 'np.NaN' was removed in the NumPy 2.0 release` — even though nobody edited the code!
2. **Rebuild the original 2023 environment from `uv.lock`:**
   ```bash
   uv sync
   uv run code/analysis.py
   ```
   `uv sync` creates `.venv/` with the exact versions from `uv.lock` (including `numpy 1.26.4`), and the script runs cleanly.

When sharing the project, send the code, data, README, `pyproject.toml`, `.python-version` and `uv.lock`. **Never send `.venv/`.**
