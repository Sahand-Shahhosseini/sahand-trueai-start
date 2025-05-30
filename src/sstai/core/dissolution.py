"""Utilities for trans-logical dissolution dynamics (Lemma 79)."""
from __future__ import annotations

import math


def theta_diss(t: float, d0: float = 0.2, zeta: float = 0.016, tau_l: float = 0.002) -> float:
    """Approximate the cumulative decay ``Θ_diss`` at time ``t``.

    Parameters
    ----------
    t : float
        Time in seconds.
    d0 : float, optional
        Initial system deviation ``δ_sys,0``.
    zeta : float, optional
        Dissipation rate ``ζ_U``.
    tau_l : float, optional
        Loop period ``τ_L``.

    Returns
    -------
    float
        Estimated ``Θ_diss(t)``.
    """
    decay = d0 * math.exp(-zeta * t)
    denom = 1.0 - math.exp(-zeta * tau_l)
    if denom == 0:
        raise ZeroDivisionError("tau_l results in division by zero")
    return decay / denom
