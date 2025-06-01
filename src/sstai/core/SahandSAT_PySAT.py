from .sahand_sat import HAS_PYSAT, SahandSAT


class SahandSATPySAT(SahandSAT):
    """SahandSAT variant that always uses PySAT if available."""

    def solve(self, verbose: bool = False) -> dict:
        if not HAS_PYSAT:
            raise ImportError("PySAT is required for SahandSATPySAT")
        return self._solve_pysat(verbose)


__all__ = ["SahandSATPySAT"]
