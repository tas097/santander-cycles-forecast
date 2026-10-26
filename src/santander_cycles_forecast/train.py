import mlflow

from .data import load_sample_hires
from .features import total_by_station
from .model import train


def run_training() -> float:
    """Train the model and log the run to MLflow."""
    mlflow.set_experiment("santander-hires")

    with mlflow.start_run():
        df = load_sample_hires()
        totals = total_by_station(df)

        model = train(totals)

        mlflow.log_param("n_stations", len(totals))
        mlflow.log_metric("mean_hires", model)

        print(f"Trained model: {model}")
        return model