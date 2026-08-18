import pandas as pd


def load_sample_hires() -> pd.DataFrame:
    """Return a small hard-coded sample of hire counts."""
    return pd.DataFrame(
        {
            "station": ["Hyde Park", "Waterloo", "Hyde Park", "Waterloo"],
            "day": ["Mon", "Mon", "Tue", "Tue"],
            "hires": [120, 340, 95, 410],
        }
    )