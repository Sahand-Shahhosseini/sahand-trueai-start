"""Placeholder for field utilities."""

def normalize(values):
    total = sum(values)
    if total == 0:
        return [0 for _ in values]
    return [v / total for v in values]
