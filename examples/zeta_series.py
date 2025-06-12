#!/usr/bin/env python3
"""
zeta_series.py
==============

Phase: Tohi-2 (Tower) — “Seed of Reflection”

Compute the Riemann zeta function ζ(s) for any complex s with Re s > 1
using the classical Euler series

        ζ(s) = Σ_{n=1..∞} n^(−s).

The script can:

  • evaluate ζ(s) by direct summation (finite N or infinite using mpmath.nsum)
  • compare the partial sum S_N with mpmath.zeta for accuracy
  • give a rigorous upper-bound for the tail R_N  by the integral test
        |R_N| ≤ ∫_{N}^{∞} x^(−Re s) dx = N^(1−Re s)/(Re s −1)
  • optionally plot log₁₀‖ζ(s) − S_N‖ as N grows.
  • compute multiple values from a CSV or text file via the ``compute`` subcommand.

Dependencies
------------
    pip install mpmath matplotlib

Usage notes
-----------
    For ``compute`` mode, provide a file with comma or newline-separated values,
    each parsable as a Python complex number.
"""

import argparse
import csv
import sys
import cmath
import mpmath as mp
from pathlib import Path


# ---------- helpers --------------------------------------------------------- #
def partial_zeta(s: complex, N: int) -> mp.mpf:
    """Return S_N(s) = Σ_{n=1..N} n^(−s)."""
    return mp.nsum(lambda k: k ** (-s), [1, N])


def tail_bound(s: complex, N: int) -> mp.mpf:
    """Integral upper bound for the remainder beyond N (Re s > 1)."""
    sigma = mp.re(s)
    if sigma <= 1:
        raise ValueError("Integral bound only valid for Re(s) > 1")
    return N ** (1 - sigma) / (sigma - 1)


def parse_complex(value: str) -> complex:
    """Parse a string into a complex number using Python syntax."""
    try:
        return complex(eval(value))
    except Exception as e:  # pragma: no cover - error string is user-facing
        raise argparse.ArgumentTypeError(f"Cannot parse '{value}' as complex: {e}")


def compute_single(s: complex, N: int, plot: bool = False) -> None:
    mp.dps = 50
    S_N = partial_zeta(s, N)
    true_zeta = mp.zeta(s)
    remainder_bound = tail_bound(s, N)
    error = abs(true_zeta - S_N)

    print(f"s                : {s}")
    print(f"N                : {N}")
    print(f"S_N              : {S_N}")
    print(f"ζ(s) (mpmath)    : {true_zeta}")
    print(f"|ζ(s)−S_N|       : {error}")
    print(f"Tail bound       : {remainder_bound}")
    print(f"Error ≤ bound?   : {error <= remainder_bound}")

    if plot:
        import matplotlib.pyplot as plt

        Ns, errs = [], []
        for k in (int(10**p) for p in mp.arange(1, mp.log10(N) + 0.1, 0.2)):
            Ns.append(k)
            errs.append(abs(mp.zeta(s) - partial_zeta(s, k)))
        plt.loglog(Ns, errs, marker="o")
        plt.xlabel("N  (log scale)")
        plt.ylabel("|ζ(s) − S_N|")
        plt.title(f"Convergence of Euler series for ζ({s})")
        plt.grid(True, which="both", ls="--", alpha=0.3)
        plt.show()


def compute_from_file(path: Path, N: int) -> None:
    mp.dps = 50
    with open(path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            for cell in row:
                if not cell.strip():
                    continue
                s = parse_complex(cell)
                if mp.re(s) <= 1:
                    print(f"Skipping {s}: Re(s) must be > 1")
                    continue
                print("--")
                compute_single(s, N)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate ζ(s) by Euler series")
    subparsers = parser.add_subparsers(dest="command")

    compute_p = subparsers.add_parser(
        "compute", help="compute ζ(s) for values read from a file"
    )
    compute_p.add_argument("file", type=Path, help="CSV or text file of values")
    compute_p.add_argument(
        "-N", type=int, default=100000, help="terms for partial sum (default: 1e5)"
    )

    parser.add_argument("s", nargs="?", help="complex s with Re(s)>1, e.g. 2.5 or 2+1j")
    parser.add_argument(
        "-N", type=int, default=100000, help="terms for partial sum (default: 1e5)"
    )
    parser.add_argument(
        "--plot", action="store_true", help="plot convergence of |ζ(s)-S_N|"
    )

    args = parser.parse_args()

    if args.command == "compute":
        compute_from_file(args.file, args.N)
    else:
        if args.s is None:
            parser.error("the following arguments are required: s")
        s = parse_complex(args.s)
        if mp.re(s) <= 1:
            sys.exit("Re(s) must be > 1 for Euler series convergence.")
        compute_single(s, args.N, plot=args.plot)


if __name__ == "__main__":
    main()
