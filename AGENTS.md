# Agent Guidelines

This repository contains a FastAPI backend with fractal utilities and simple ML models. Codex agents should follow these guidelines when making changes.

## Required Tasks
1. Add a PyTorch-based model with API integration and an example training script.
2. Modernize lemma loading by using `importlib.resources.files` instead of deprecated APIs.
3. Introduce an open-source license file and reference it in `README.md`.
4. Clarify usage of `GOLD_CHECKPOINT.yml` or remove it if unnecessary.
5. Expand the README with instructions for running the server, tests, and example scripts.

## Contribution Rules
- Keep code Pythonic and adhere to PEP8. Use `black` for formatting.
- Add unit tests for new functionality and ensure all tests pass by running `pytest` before committing.
- Update documentation for any new modules or APIs.
