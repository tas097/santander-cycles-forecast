import pandas as pd


def train(df: pd.DataFrame) -> float:
    """'Train' a model: the average hires per station."""
    return float(df["hires"].mean())


def predict(model: float) -> float:
    """Predict hires — always the trained average."""
    return model