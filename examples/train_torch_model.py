"""Train the TorchFractalNet model and print a few predictions."""

from sstai.ai import train_torch_fractal_model, predict_torch_fractal

if __name__ == "__main__":
    model = train_torch_fractal_model()
    preds = predict_torch_fractal(model, ["SFL_001", "SFL_002"])
    print(preds)
