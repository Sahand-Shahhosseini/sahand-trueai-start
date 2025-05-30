import numpy as np
from scipy.linalg import eigvalsh


def random_state(n: int) -> np.ndarray:
    psi = np.random.randn(n) + 1j * np.random.randn(n)
    return psi / np.linalg.norm(psi)


def density(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


def entropy(r: np.ndarray) -> float:
    vals = eigvalsh(r)
    vals = vals[vals > 1e-12]
    return float(-np.sum(vals * np.log(vals)))


def collapse(r: np.ndarray, L: np.ndarray) -> np.ndarray:
    P = np.outer(L, L.conj())
    prob = np.real(np.trace(P @ r))
    if prob == 0.0:
        return r
    return (P @ r @ P) / prob


def is_active(r: np.ndarray, L: np.ndarray, tol: float = 1e-9) -> bool:
    return abs(entropy(collapse(r, L)) - entropy(r)) < tol


if __name__ == "__main__":
    L = np.array([1.0, 0.0])
    psi = random_state(2)
    r = density(psi)
    print("H before", entropy(r))
    print("H after ", entropy(collapse(r, L)))
    print("active ", is_active(r, L))
