"""Average body mass of each penguin species, as a table and a plot.

Run from the project folder (the one that contains `data/` and `code/`):
    uv run code/analysis.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

penguins = pd.read_csv("data/penguins.csv").dropna()

# average body mass (grams) of each species
mass = penguins.groupby("species")["body_mass"].mean().round()
print(f"{len(penguins)} penguins")
print(mass.to_string())

Path("outputs").mkdir(exist_ok=True)
ax = mass.plot.bar(rot=0, color="#3b6ea5")
ax.set_xlabel("Species")
ax.set_ylabel("Average body mass (g)")
plt.tight_layout()
plt.savefig("outputs/body_mass.png", dpi=150)
print("Saved outputs/body_mass.png")
