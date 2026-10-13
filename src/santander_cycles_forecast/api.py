from fastapi import FastAPI

from .data import load_sample_hires
from .features import total_by_station

app = FastAPI(title="Santander Cycles Forecast")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "santander-cycles-forecast"}


@app.get("/totals")
def totals() -> list[dict]:
    df = total_by_station(load_sample_hires())
    return df.to_dict(orient="records")