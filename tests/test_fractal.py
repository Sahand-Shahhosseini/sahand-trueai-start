import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.api.routes import fractal_endpoint, FractalRequest
from sstai.core.fractal import compute_fractal
from sstai.core.lattice import FractalLattice


def test_fractal_endpoint_direct():
    numbers = [0.1, 0.2, 0.3]
    req = FractalRequest(numbers=numbers)
    resp = fractal_endpoint(req)
    assert resp.result == compute_fractal(numbers)


def test_fractal_lattice_iterate():
    lattice = FractalLattice(seed=0)
    before = lattice.grid.copy()
    lattice.iterate()
    after = lattice.grid
    assert not (before == after).all()
    assert after.shape == (6, 13, 5)


def test_fractal_lattice_as_vector():
    lattice = FractalLattice()
    vec = lattice.as_vector()
    assert vec.size == 6 * 13 * 5
