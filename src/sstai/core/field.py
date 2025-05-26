"""Conscious field utilities."""

from __future__ import annotations

try:
    import torch
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    torch = None

def normalize(values):
    total = sum(values)
    if total == 0:
        return [0 for _ in values]
    return [v / total for v in values]


if torch is None:  # pragma: no cover - optional dependency guard
    class ConsciousField:
        """Fallback definition when PyTorch is unavailable."""

        def __init__(self, *_, **__):
            raise ImportError("ConsciousField requires the 'torch' package")
else:
    class ConsciousField(torch.nn.Module):
        r"""
        \u03d5: spacetime field \u2192
        L = \xbd(\u2202_\u03bc\u03d5 \u2202^\u03bc\u03d5) \u2212 V(\u03d5)
        """

        def __init__(self, potential=lambda x: 0.25 * (x**4 - x**2)):
            super().__init__()
            self.potential = potential

        def forward(self, phi: torch.Tensor) -> torch.Tensor:
            grad = torch.autograd.grad(
                phi.sum(), phi, create_graph=True, retain_graph=True
            )[0]
            kinetic = 0.5 * torch.sum(grad**2)
            return kinetic - torch.sum(self.potential(phi))
