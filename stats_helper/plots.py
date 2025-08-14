from __future__ import annotations
import os
import matplotlib.pyplot as plt
import pandas as pd

def _ensure_dir(path: str | None):
    if path:
        os.makedirs(path, exist_ok=True)

def histogram(df: pd.DataFrame, column: str, *, bins: int = 10, out: str | None = None):
    """Generate and optionally save a histogram for a numeric column."""
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found")
    _ensure_dir(os.path.dirname(out) if out else None)
    plt.figure()
    df[column].plot(kind="hist", bins=bins, edgecolor="black")
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    if out:
        plt.savefig(out, bbox_inches="tight")
        plt.close()
    else:
        plt.show()

def boxplot(df: pd.DataFrame, column: str, *, out: str | None = None):
    """Generate and optionally save a boxplot for a numeric column."""
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found")
    _ensure_dir(os.path.dirname(out) if out else None)
    plt.figure()
    df[[column]].boxplot()
    plt.title(f"Boxplot of {column}")
    plt.ylabel(column)
    if out:
        plt.savefig(out, bbox_inches="tight")
        plt.close()
    else:
        plt.show()

def scatter(df: pd.DataFrame, x: str, y: str, *, out: str | None = None):
    """Generate and optionally save a scatter plot between two numeric columns."""
    for col in (x, y):
        if col not in df.columns:
            raise KeyError(f"Column '{col}' not found")
    _ensure_dir(os.path.dirname(out) if out else None)
    plt.figure()
    plt.scatter(df[x], df[y])
    plt.title(f"Scatter: {x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)
    if out:
        plt.savefig(out, bbox_inches="tight")
        plt.close()
    else:
        plt.show()
