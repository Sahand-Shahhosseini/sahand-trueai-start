import importlib.util
import pytest

spec = importlib.util.find_spec('torch')
if spec is None:  # pragma: no cover - torch not installed
    pytest.skip("PyTorch not available", allow_module_level=True)

import torch
from sstai.ai.encoder import ElectroCoder


def test_electrocoder_output_shape():
    model = ElectroCoder(in_channels=32, latent_dim=156)
    x = torch.randn(2, 32, 128)
    out = model(x)
    assert out.shape == (2, 156)
