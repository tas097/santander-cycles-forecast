import pandas as pd

from santander_cycles_forecast.features import total_by_station


def test_total_by_station_sums_hires_per_station():
    df = pd.DataFrame(
        {
            "station": ["Hyde Park", "Waterloo", "Hyde Park"],
            "hires": [100, 50, 20],
        }
    )

    result = total_by_station(df)

    assert result.loc[result["station"] == "Hyde Park", "hires"].iloc[0] == 120
    assert len(result) == 2