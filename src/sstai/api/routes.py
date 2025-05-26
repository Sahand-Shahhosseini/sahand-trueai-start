from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from sstai.core.fractal import compute_fractal

app = FastAPI()

class FractalRequest(BaseModel):
    numbers: List[float]

class FractalResponse(BaseModel):
    result: List[float]

@app.post("/fractal", response_model=FractalResponse)
def fractal_endpoint(req: FractalRequest) -> FractalResponse:
    result = compute_fractal(req.numbers)
    return FractalResponse(result=result)
