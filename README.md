# sahand-trueai-start
First GitHub repo by Sahand Shahhosseini – starting point of Sahand True AI journey
---

**Started by Sahand Shahhosseini on May 21, 2025**  
The first step in building Sahand True AI (Layer-77 Fractal Cognitive Framework).

## Sahand Fractal Lemmas

This repository now ships with a dataset of 150 "Sahand Fractal Lemmas". The
lemmas are stored in `src/sstai/data/lemmas.json` and can be loaded at runtime
using `sstai.core.load_lemmas()`.
Fractal results may also be computed directly from lemma codes via the
`compute_fractal_from_codes` helper or the `/lemma-fractal` API endpoint.

## iOS App

A simple SwiftUI application is available under the `ios/` directory. It demonstrates how to connect to the FastAPI backend and compute fractal results on both iPhone and iPad.


## Cross-Platform Usage

The backend runs on Windows, Linux and macOS. See `docs/platform-guide.md` for platform-specific instructions, including example code for .NET and Android clients.

## FractalNet AI Model

This repository now contains a small pure-Python model called **FractalNet**.
It learns to approximate the fractal values associated with the 150 lemma codes.
You can train it using:

```python
from sstai.ai import train_fractal_model, predict_fractal
model = train_fractal_model()
predictions = predict_fractal(model, ["SFL_001", "SFL_002"])
```
