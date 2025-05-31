"""Example training script for the PyTorch fractal model."""

from sstai.ai import train_torch_fractal_model, predict_torch_fractal

model = train_torch_fractal_model()
print(predict_torch_fractal(model, ["SFL_001", "SFL_002"]))
