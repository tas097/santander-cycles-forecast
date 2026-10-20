import pandas as pd

from santander_cycles_forecast.data import load_sample_hires


def test_load_sample_hires_returns_a_dataframe():
    result = load_sample_hires()
    assert isinstance(result, pd.DataFrame)


def test_load_sample_hires_has_expected_columns():
    result = load_sample_hires()
    assert list(result.columns) == ["station", "day", "hires"]


def test_load_sample_hires_is_not_empty():
    result = load_sample_hires()
    assert len(result) > 0