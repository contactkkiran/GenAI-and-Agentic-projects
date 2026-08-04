# Phase 1 Python Projects

This folder contains Python practice projects focused on basic FastAPI examples and introductory agent concepts.

## Contents

- `fastapi/` — Sample FastAPI application with endpoints and request models.
- `python 01_basics.py` — Python fundamentals and early RAG or agent experiments.
- `llm_models.txt` — Notes or lists of LLM models.
- `sample.txt` — Example content or references.

## Running the FastAPI sample

Start the FastAPI application using Uvicorn:

```bash
cd "phase 1 - python"
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pydantic
uvicorn fastapi.main:api --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

## Notes

- `fastapi/main.py` demonstrates GET and POST endpoints using Pydantic models.
- This folder is useful for learning how to build simple API services in Python.
