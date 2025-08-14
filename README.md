# stats_helper

A clean, reusable Python package for simple statistical analysis and plotting on CSV datasets.

## Features

- Load data from CSV
- Core stats: mean, median, mode, variance, standard deviation
- Correlation matrix across numeric columns
- Plots: histogram, boxplot, scatter (matplotlib)
- Simple CLI to print summary stats and generate plots
- (Bonus) Minimal pytest-based tests

## Installation

### Option 1: Editable install
```bash
pip install -e .
```

### Option 2: Build and install
```bash
python -m build
pip install dist/stats_helper-0.1.0-py3-none-any.whl
```

## Usage

### CLI
```bash
stats-helper data.csv --summary
stats-helper data.csv --hist sepal_length --bins 20
stats-helper data.csv --box petal_width
stats-helper data.csv --scatter sepal_length sepal_width
```

This will save plots into an `outputs/` directory by default.

### Python API
```python
from stats_helper import load_csv, mean, median, mode, variance, stddev, correlation_matrix, histogram

df = load_csv("data.csv")
print(mean(df["col"]))
print(correlation_matrix(df))

histogram(df, "col", bins=20, out="hist_col.png")
```

## Development

Run tests:
```bash
pytest -q
```

## Project Structure

```
stats_helper_pkg/
├─ stats_helper/
│  ├─ __init__.py
│  ├─ io.py
│  ├─ stats.py
│  └─ plots.py
├─ tests/
│  └─ test_stats.py
├─ examples/
│  └─ quickstart.ipynb
├─ pyproject.toml
├─ requirements.txt
└─ README.md
```

## Notes
- Mode returns a scalar if a single mode exists; otherwise a list of modes. If no mode, returns `None`.
- Variance/Stddev default to sample (ddof=1); use pandas directly if you need different behavior.
