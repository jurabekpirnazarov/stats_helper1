"""stats_helper
A simple statistical analysis helper package for CSV datasets.
"""

from .io import load_csv
from .stats import mean, median, mode, variance, stddev, correlation_matrix
from .plots import histogram, boxplot, scatter

__all__ = [
    "load_csv",
    "mean", "median", "mode", "variance", "stddev", "correlation_matrix",
    "histogram", "boxplot", "scatter",
]
