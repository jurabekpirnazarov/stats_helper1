from __future__ import annotations
import pandas as pd

def load_csv(path: str, *, parse_dates: bool | list[str] | None = None) -> pd.DataFrame:
    """Load a CSV into a pandas DataFrame.
    
    Args:
        path: Path to the CSV file.
        parse_dates: If True or list of column names, attempt to parse dates.
    
    Returns:
        pandas.DataFrame with data types inferred.
    """
    df = pd.read_csv(path, parse_dates=parse_dates)
    return df
