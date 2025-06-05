#!/usr/bin/env python3
"""
zeta_series.py
===============

Phase: Tohi-2 (Tower) — “Seed of Reflection”

Compute the Riemann zeta function ζ(s) for any complex s with Re s > 1
using the classical Euler series

        ζ(s) = Σ_{n=1..∞} n^(−s).

The script can:

  • evaluate ζ(s) by direct summation (finite N or infinite using mpmath.nsum)
  • compare the partial sum S_N with mpmath.zeta for accuracy
  • give a rigorous upper-bound for the tail R_N  by the integral test
        |R_N| ≤ ∫_{N}^{∞} x^(−Re s) dx = N^(1−Re s)/(Re s −1)
  • optionally plot log₁₀ |ζ(s) − S_N| as N grows.

Dependencies
------------
    pip install mpmath matplotlib
"""

from __future__ import annotations

import argparse
import cmath
import sys
from typing import Iterable

import mpmath as mp


# ---------- helpers --------------------------------------------------------- #
def partial_zeta(s: complex, N: int) -> mp.mpf:
    """Return S_N(s) = Σ_{n=1..N} n^(−s)."""
    return mp.nsum(lambda k: k ** (-s), [1, N])


def tail_bound(s: complex, N: int) -> mp.mpf:
    """Integral upper bound for the remainder beyond ``N``."""
    re_s = mp.re(s)
    if re_s <= 1:
        raise ValueError("Re(s) must be > 1 for convergence")
    return N ** (1 - re_s) / (re_s - 1)


def parse_complex(text: str) -> complex:
    """Parse a complex number from ``text``."""
    try:
        return complex(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid complex number: {text}") from exc


def error_series(s: complex, ns: Iterable[int]) -> list[float]:
    """Return log10 error for each ``n`` in ``ns``."""
    exact = mp.zeta(s)
    return [mp.log10(abs(exact - partial_zeta(s, n))) for n in ns]


# ---------- cli ------------------------------------------------------------ #
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate the Riemann zeta series")
    parser.add_argument("s", type=parse_complex, help="complex argument s with Re(s)>1")
    parser.add_argument(
        "-N",
        "--partial",
        type=int,
        default=None,
        help="compute direct sum up to N (otherwise use infinite mpmath.nsum)",
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="plot log10|zeta(s)-S_N| for N from 1..N",
    )
    args = parser.parse_args(argv)

    s = args.s
    if args.partial is None:
        result = mp.nsum(lambda k: k ** (-s), [1, mp.inf])
        print(f"zeta({s}) ≈ {result}")
        return 0

    N = args.partial
    exact = mp.zeta(s)
    partial = partial_zeta(s, N)
    bound = tail_bound(s, N)
    err = abs(exact - partial)

    print(f"S_{N}({s}) = {partial}")
    print(f"zeta({s}) = {exact}")
    print(f"|error| = {err}")
    print(f"tail bound ≤ {bound}")

    if args.plot:
        import matplotlib.pyplot as plt

        ns = range(1, N + 1)
        errs = error_series(s, ns)
        plt.plot(ns, errs)
        plt.xlabel("N")
        plt.ylabel("log10 |zeta(s) - S_N|")
        plt.title(f"Convergence of partial sums for zeta({s})")
        plt.show()

    return 0


if __name__ == "__main__":
    sys.exit(main())
