# BrainCheck

BrainCheck is a small Flask quiz application built to demonstrate a basic DevOps workflow.

## Run locally

```powershell
py -m pip install -r requirements.txt
py app.py
```

Open `http://localhost:5000` in a browser.

## Test

```powershell
py -m pytest -q
```

## Run with Docker

```powershell
docker build -t braincheck .
docker run --rm -p 5000:5000 braincheck
```

GitHub Actions runs the test suite on every push and pull request.