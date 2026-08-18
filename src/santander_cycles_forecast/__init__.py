from .data import load_sample_hires
from .features import total_by_station


def main() -> None:
    df = load_sample_hires()
    print(total_by_station(df))