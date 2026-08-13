"""
Regenerates dataset.csv for the Tech Trends notebook.

The Stack Overflow Developer Survey 2019 public release (88,883 responses) is
too large to commit to GitHub directly (~190MB combined), so this script
rebuilds it from a public column-chunked mirror on GitHub.

Usage:
    pip install pandas
    python get_dataset.py
    # writes dataset.csv (~190MB) into this folder
"""

import glob
import io
import zipfile
import urllib.request

import pandas as pd

REPO_ZIP_URL = "https://github.com/a1ip/stack_overflow_survey_2019/archive/refs/heads/master.zip"


def main():
    print("Downloading source data...")
    with urllib.request.urlopen(REPO_ZIP_URL) as resp:
        data = resp.read()

    zf = zipfile.ZipFile(io.BytesIO(data))
    chunk_names = [
        n for n in zf.namelist()
        if "survey_results_public_1-" in n and n.endswith(".csv")
    ]
    print(f"Found {len(chunk_names)} column-chunk files")

    dfs = []
    for name in chunk_names:
        with zf.open(name) as f:
            dfs.append(pd.read_csv(f))

    merged = dfs[0]
    for d in dfs[1:]:
        merged = merged.merge(d, on="Respondent", how="outer")

    print("Merged shape:", merged.shape)
    merged.to_csv("dataset.csv", index=False)
    print("Wrote dataset.csv")


if __name__ == "__main__":
    main()
