# Penguin body mass (Python)

The average body mass of each penguin species, as a table and a bar chart.

This project has **no environment yet**. It is for the Section 3 demo, where you set one up with [uv](https://docs.astral.sh/uv/).

## Contents

- `data/penguins.csv`: the penguin measurements
- `code/analysis.py`: prints the average body mass of each species, and saves a chart to `outputs/`
- `finished/`: the files uv makes during the demo (`pyproject.toml`, `uv.lock` and `.python-version`), in case the demo doesn't work

## Demo: set up an environment with uv

Copy this folder somewhere first, so the original stays without an environment. Then, in a terminal in the copy:

1. **Try to run it.** `python code/analysis.py` fails, because pandas and matplotlib aren't installed. This is the "it works on my laptop" problem.
2. **Start a project:** `uv init --no-package`. This makes `pyproject.toml` (the list of what the project needs) and `.python-version` (the Python version). It also makes a starter `main.py`, which you can delete, and (if the folder isn't already in git) a git repository.
3. **Add the packages:** `uv add pandas matplotlib`. uv makes the environment (`.venv/`), installs the packages into it, and records them in `pyproject.toml` and the lock file, `uv.lock`.
4. **Run it in the environment:** `uv run code/analysis.py`. It prints the results and saves `outputs/body_mass.png`.
5. **Delete the environment:** delete the `.venv/` folder. Running `uv run code/analysis.py` again would just rebuild it, so for the demo, rebuild it yourself:
6. **Rebuild it from the lock file:** `uv sync`. This is what a colleague runs when you send them the project. They get the same packages, at the same versions.

Send the code, the data, this README, `pyproject.toml`, `uv.lock` and `.python-version`. Don't send `.venv/`.
