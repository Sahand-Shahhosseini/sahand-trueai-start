"""Torch-based encoder for EEG windows."""

from __future__ import annotations

try:
    import torch
    import torch.nn as nn
except Exception:  # pragma: no cover - torch may be missing
    torch = None  # type: ignore
    nn = None  # type: ignore


if torch is not None:
    class ElectroCoder(nn.Module):
        """Map EEG signals to latent vectors."""

        def __init__(self, in_channels: int = 32, latent_dim: int = 156):
            super().__init__()
            self.encoder = nn.Sequential(
                nn.Conv1d(in_channels, 64, kernel_size=3, padding=1),
                nn.ReLU(),
                nn.Conv1d(64, 128, kernel_size=3, padding=1),
                nn.ReLU(),
                nn.AdaptiveAvgPool1d(1),
            )
            self.fc = nn.Linear(128, latent_dim)

        def forward(self, x: torch.Tensor) -> torch.Tensor:  # type: ignore[override]
            h = self.encoder(x).squeeze(-1)
            return self.fc(h)
else:  # pragma: no cover - simple placeholder when torch is absent
    class ElectroCoder:  # type: ignore[too-many-instance-attributes]
        def __init__(self, *args, **kwargs) -> None:  # noqa: D401
            """Placeholder raising ImportError when PyTorch is missing."""
            raise ImportError("ElectroCoder requires PyTorch")
