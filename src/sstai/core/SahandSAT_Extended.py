from .sahand_sat import SahandSAT


class SahandSATExtended(SahandSAT):
    """Extended SahandSAT with convenience helpers."""

    def load_and_solve(self, data, verbose: bool = False):
        self.load_from_json(data)
        return self.solve(verbose)


__all__ = ["SahandSATExtended"]
