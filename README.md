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

## TorchFractalNet

A lightweight PyTorch version, **TorchFractalNet**, is provided for
experimentation. Train and evaluate it via:

```bash
python examples/train_torch_model.py
```

The FastAPI backend exposes this model at the `/fractal-net` endpoint.

## Chat CLI

Create a `.env` file in `examples/` with your `OPENAI_API_KEY`. Then run:

```bash
python examples/chat_cli.py
```

This opens an interactive session with the STAI persona using the OpenAI API.


## Running

Start the server with:

```bash
uvicorn sstai.api.routes:app --reload
```

Run the test suite using:

```bash
pytest -q
```

### راه‌اندازی در پوشه `sstai`

برای اجرای هسته‌ی پروژه می‌توانید مراحل زیر را دنبال کنید:

```bash
# پوشهٔ پروژه
cd sstai

# ساخت محیط مجازی اختیاری
python -m venv .venv
source .venv/bin/activate  # در ویندوز: .venv\Scripts\activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرای هسته
python main.py
```

## Gold Checkpoint

`GOLD_CHECKPOINT.yml` records the commit and test hashes of the most stable
release. Update it after tests pass to track the "Gold" state.

## License

This project is licensed under the [MIT License](LICENSE).
