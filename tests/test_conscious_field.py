import pytest

torch = pytest.importorskip('torch')

from sstai.core import ConsciousField


def test_conscious_field_simple():
    phi = torch.tensor([1.0], requires_grad=True)
    field = ConsciousField()
    out = field(phi)
    assert out.item() == pytest.approx(0.5)
