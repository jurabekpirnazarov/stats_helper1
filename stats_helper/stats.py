from __future__ import annotations
import numpy as np
import pandas as pd

def _to_series(data, name: str | None = None) -> pd.Series:
    if isinstance(data, pd.Series):
        return data
    if isinstance(data, (list, tuple, np.ndarray)):
        return pd.Series(data, name=name)
    raise TypeError("data must be a pandas Series, list, tuple, or numpy array")

def mean(data) -> float:
    """Compute the arithmetic mean of a numeric column or 1-D array."""
    s = _to_series(data)
    return float(s.mean())

def median(data) -> float:
    """Compute the median of a numeric column or 1-D array."""
    s = _to_series(data)
    return float(s.median())

def mode(data):
    """Return the mode(s) of a column.
    
    Returns:
        If a single mode exists, returns a scalar (float/int/str).
        If multiple modes exist, returns a list of values.
    """
    s = _to_series(data)
    m = s.mode(dropna=True)
    if len(m) == 0:
        return None
    if len(m) == 1:
        return m.iloc[0].item() if hasattr(m.iloc[0], "item") else m.iloc[0]
    return m.tolist()

def variance(data, ddof: int = 1) -> float:
    """Sample variance by default (ddof=1). Set ddof=0 for population variance."""
    s = _to_series(data)
    return float(s.var(ddof=ddof))

def stddev(data, ddof: int = 1) -> float:
    """Sample standard deviation by default (ddof=1)."""
    s = _to_series(data)
    return float(s.std(ddof=ddof))

def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Compute the Pearson correlation matrix for numeric columns only."""
    return df.select_dtypes(include=[np.number]).corr(numeric_only=True)
