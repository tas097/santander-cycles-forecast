import pandas as pd


def total_by_station(df: pd.DataFrame) -> pd.DataFrame:
    """Sum hires per station."""
    return df.groupby("station", as_index=False)["hires"].mean()