"""Average body mass of each penguin species (written in 2023).

1. Run with today's latest packages (crashes under NumPy 2.0+):
    uv run --no-project --with pandas --with matplotlib code/analysis.py

2. Rebuild the original 2023 environment from uv.lock and run:
    uv sync
    uv run code/analysis.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Standardise missing values and drop incomplete rows (np.NaN worked in NumPy 1.x!)
penguins = pd.read_csv("data/penguins.csv").fillna(np.NaN).dropna()

# Average body mass (grams) of each species
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
