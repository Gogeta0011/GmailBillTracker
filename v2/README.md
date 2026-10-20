# GmailBillTracker 2.0

A FastAPI service that stores and lists receipts. Includes JWT auth, MySQL, pytest, Docker, and GitHub Actions.

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run with Docker

```bash
docker build -t receipt-tracker .
docker run -p 8000:8000 receipt-tracker
```

## Tests

```bash
pytest
```
