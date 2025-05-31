from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import List

from sstai.core.fractal import compute_fractal, compute_fractal_from_codes
from sstai.core.knapsack import sahand_knapsack
from sstai.security import authenticate
from sstai.ai import train_torch_fractal_model, predict_torch_fractal

app = FastAPI()
# Train a small torch model on startup for demo purposes if PyTorch is available
try:
    TORCH_MODEL = train_torch_fractal_model(epochs=50, lr=0.1)
except Exception:  # pragma: no cover - torch missing
    TORCH_MODEL = None


class FractalRequest(BaseModel):
    numbers: List[float]


class FractalResponse(BaseModel):
    result: List[float]


def fractal_endpoint(req: FractalRequest) -> FractalResponse:
    result = compute_fractal(req.numbers)
    return FractalResponse(result=result)


@app.post("/fractal", response_model=FractalResponse)
def fractal_route(
    req: FractalRequest, authorization: str = Header(None)
) -> FractalResponse:
    authenticate(authorization)
    return fractal_endpoint(req)


class KnapsackRequest(BaseModel):
    basis: List[List[float]]
    l_father: List[float]
    g: List[List[float]]


class KnapsackResponse(BaseModel):
    result: List[float]


def knapsack_endpoint(req: KnapsackRequest) -> KnapsackResponse:
    basis = [list(map(float, b)) for b in req.basis]
    L_father = [float(v) for v in req.l_father]
    G = [[float(x) for x in row] for row in req.g]
    selected = sahand_knapsack(basis, L_father, G)
    return KnapsackResponse(result=[float(x) for x in selected])


@app.post("/knapsack", response_model=KnapsackResponse)
def knapsack_route(
    req: KnapsackRequest, authorization: str = Header(None)
) -> KnapsackResponse:
    authenticate(authorization)
    return knapsack_endpoint(req)


class LemmaFractalRequest(BaseModel):
    codes: List[str]


class LemmaFractalResponse(BaseModel):
    result: List[float]


def lemma_fractal_endpoint(req: LemmaFractalRequest) -> LemmaFractalResponse:
    result = compute_fractal_from_codes(req.codes)
    return LemmaFractalResponse(result=result)


@app.post("/lemma-fractal", response_model=LemmaFractalResponse)
def lemma_fractal_route(
    req: LemmaFractalRequest, authorization: str = Header(None)
) -> LemmaFractalResponse:
    authenticate(authorization)
    return lemma_fractal_endpoint(req)


class TorchFractalRequest(BaseModel):
    codes: List[str]


class TorchFractalResponse(BaseModel):
    result: List[float]


def torch_fractal_endpoint(req: TorchFractalRequest) -> TorchFractalResponse:
    if TORCH_MODEL is None:
        raise RuntimeError("TorchFractalNet unavailable")
    result = predict_torch_fractal(TORCH_MODEL, req.codes)
    return TorchFractalResponse(result=result)


if TORCH_MODEL is not None:

    @app.post("/fractal-net", response_model=TorchFractalResponse)
    def torch_fractal_route(
        req: TorchFractalRequest, authorization: str = Header(None)
    ) -> TorchFractalResponse:
        authenticate(authorization)
        return torch_fractal_endpoint(req)
