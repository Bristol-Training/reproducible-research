"""Reads the raw data, removes incomplete rows, and saves a clean copy.

Run from the project folder: uv run code/01_clean_data.py
"""
import pandas as pd

raw = pd.read_csv("data/raw/penguins.csv")
clean = raw.dropna()
clean.to_csv("data/processed/penguins_clean.csv", index=False)
