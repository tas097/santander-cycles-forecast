import pandas as pd


def main() -> None:
    df = pd.DataFrame({"station": ["Hyde Park", "Waterloo"], "hires": [120, 340]})
    print(df)