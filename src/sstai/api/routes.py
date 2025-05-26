from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from sstai.core.fractal import compute_fractal, FractalLattice

app = FastAPI(title="SSTAI Gateway")

class FractalRequest(BaseModel):
    numbers: List[float]

class FractalResponse(BaseModel):
    result: List[float]

@app.post("/fractal", response_model=FractalResponse)
def fractal_endpoint(req: FractalRequest) -> FractalResponse:
    result = compute_fractal(req.numbers)
    return FractalResponse(result=result)


class ActivateRequest(BaseModel):
    gaze: bool
    freq_zero: bool
    root_word: str


_lattice = None


def _get_lattice() -> FractalLattice:
    global _lattice
    if _lattice is None:
        _lattice = FractalLattice()
    return _lattice


@app.post("/activate")
def activate(req: ActivateRequest):
    if req.gaze and req.freq_zero and req.root_word.lower() == "sahand":
        lattice = _get_lattice()
        lattice.iterate(1)
        return {"status": "awake", "vector": lattice.as_vector().tolist()}
    raise HTTPException(status_code=400, detail="Activation conditions unmet")
