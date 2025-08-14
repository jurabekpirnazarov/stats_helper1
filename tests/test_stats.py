import pandas as pd
from stats_helper.stats import mean, median, mode, variance, stddev, correlation_matrix

def test_basic_stats():
    s = pd.Series([1, 2, 2, 3, 4])
    assert mean(s) == 2.4
    assert median(s) == 2.0
    assert mode(s) == 2
    assert round(variance(s), 2) == 1.30  # sample variance
    assert round(stddev(s), 4) == round(variance(s) ** 0.5, 4)

def test_multi_mode():
    s = pd.Series([1, 1, 2, 2, 3])
    m = mode(s)
    assert isinstance(m, list) and set(m) == {1, 2}

def test_correlation_matrix():
    df = pd.DataFrame({
        "a": [1, 2, 3, 4],
        "b": [2, 4, 6, 8],
        "c": ["x", "y", "x", "y"],
    })
    corr = correlation_matrix(df)
    assert set(corr.columns) == {"a", "b"}
    assert corr.loc["a", "b"] == 1.0
