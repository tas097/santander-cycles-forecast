# Santander Cycles Forecast

Forecasting daily bike hires for London's Santander Cycles scheme — built as a production-style ML service rather than a notebook.

The modelling is deliberately the smaller half of this project. The focus is the engineering around it: packaging, testing, CI, containerisation, and reproducible environments.

---

## Status

**Phases 0–4 complete.** The service runs, is tested, and ships as a container. It currently serves a small hard-coded sample dataset — real TfL data and the forecasting model land in Phase 5 onwards (see the roadmap below).

```
  ✅ 0  Engineering foundations    git, uv, src layout
  ✅ 1  Python packaging           installable package, entry points
  ✅ 2  Testing & CI               pytest + GitHub Actions on every PR
  ✅ 3  Docker                     portable image, amd64 build for AWS
  ✅ 4  HTTP service               FastAPI endpoints
  ⬜ 5  Experiment tracking        MLflow
  ⬜ 6  Orchestration              scheduled pipeline runs
  ⬜ 7  Cloud deployment           AWS + Terraform
  ⬜ 8  Monitoring                 drift detection
  ⬜ 9  Real data + model          TfL open data, Prophet forecast
```

---

## What's here

```
  src/santander_cycles_forecast/
  ├── __init__.py     wiring + what the package exposes
  ├── data.py         loading hire data
  ├── features.py     reshaping into model-ready form
  └── api.py          HTTP endpoints

  tests/              6 tests, run on every push and PR
  Dockerfile          builds the deployable image
  .github/workflows/  CI: tests + image build
```

---

## Running it

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/tas097/santander-cycles-forecast.git
cd santander-cycles-forecast
uv sync
```

**As a one-off job:**
```bash
uv run santander-cycles-forecast
```

**As a service:**
```bash
uv run uvicorn santander_cycles_forecast.api:app --reload
```
Then visit `http://127.0.0.1:8000/docs` for interactive API documentation.

**In Docker:**
```bash
docker build -t santander-cycles-forecast .
docker run -p 8000:8000 santander-cycles-forecast
```

**Tests:**
```bash
uv run pytest
```

---

## API

| Endpoint | Method | Returns |
|---|---|---|
| `/health` | GET | Service status — used for health checks |
| `/totals` | GET | Total hires per station |
| `/docs` | GET | Interactive API documentation (auto-generated) |

```bash
$ curl http://127.0.0.1:8000/totals
[{"station":"Hyde Park","hires":215},{"station":"Waterloo","hires":750}]
```

---

## Engineering decisions

**Reproducible environments.** `pyproject.toml` records intent (`pandas>=3.0.5`); `uv.lock` records the exact resolved versions; `.python-version` pins the interpreter. Together these mean the environment rebuilds identically on any machine — local, CI, or container.

**src layout.** Code lives in `src/`, so it can only be imported once genuinely installed. This rules out the class of bug where code works only because of which directory you happened to be standing in.

**Separated dependencies.** Test tooling sits in a dev group and is excluded from the production image (`uv sync --no-dev`), so the deployed container carries nothing it doesn't need.

**CI as a gate.** Every pull request runs two independent checks — the test suite, and a Docker image build — on a fresh Ubuntu runner. Nothing merges to `main` without both passing. Testing on Linux rather than macOS matches the eventual deployment target.

**Built for amd64.** Development is on Apple Silicon (arm64) while the deployment target is amd64, so production images are built with `--platform linux/amd64`.

---

## Data

Hire data comes from [TfL's open cycle hire usage statistics](https://cycling.data.tfl.gov.uk/) — publicly available, no credentials required.

---

## Roadmap

**Phase 5 — Experiment tracking.** MLflow for logging runs, parameters and metrics, plus a model registry so a specific trained model can be promoted and served.

**Phase 6 — Orchestration.** Scheduled retraining and data refresh as a managed pipeline rather than manual runs.

**Phase 7 — Cloud deployment.** AWS (ECR, ECS/Fargate, S3) provisioned via Terraform, so the infrastructure is version-controlled alongside the code.

**Phase 8 — Monitoring.** Drift detection on incoming data and prediction quality, with alerting.

**Phase 9 — Real data and model.** Prophet forecast on the full TfL dataset, replacing the current sample data.
