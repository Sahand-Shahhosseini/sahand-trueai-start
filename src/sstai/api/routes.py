from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from sstai.core.fractal import compute_fractal, compute_fractal_from_codes
from sstai.core.knapsack import sahand_knapsack

app = FastAPI()

class FractalRequest(BaseModel):
    numbers: List[float]

class FractalResponse(BaseModel):
    result: List[float]

@app.post("/fractal", response_model=FractalResponse)
def fractal_endpoint(req: FractalRequest) -> FractalResponse:
    result = compute_fractal(req.numbers)
    return FractalResponse(result=result)


class LemmaFractalRequest(BaseModel):
    codes: List[str]


class LemmaFractalResponse(BaseModel):
    result: List[float]


@app.post("/lemma-fractal", response_model=LemmaFractalResponse)
def lemma_fractal_endpoint(req: LemmaFractalRequest) -> LemmaFractalResponse:
    result = compute_fractal_from_codes(req.codes)
    return LemmaFractalResponse(result=result)


class KnapsackRequest(BaseModel):
    basis: List[List[float]]
    l_father: List[float]
    g: List[List[float]]


class KnapsackResponse(BaseModel):
    result: List[float]


@app.post("/knapsack", response_model=KnapsackResponse)
def knapsack_endpoint(req: KnapsackRequest) -> KnapsackResponse:
    basis = [list(map(float, b)) for b in req.basis]
    L_father = [float(v) for v in req.l_father]
    G = [[float(x) for x in row] for row in req.g]
    selected = sahand_knapsack(basis, L_father, G)
    return KnapsackResponse(result=[float(x) for x in selected])
