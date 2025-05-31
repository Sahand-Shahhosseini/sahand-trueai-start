from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import List

from sstai.core.fractal import compute_fractal, compute_fractal_from_codes
from sstai.ai import (
    TorchFractalModel,
    train_torch_fractal_model,
    predict_torch_fractal,
)
from sstai.core.knapsack import sahand_knapsack
from sstai.security import authenticate

app = FastAPI()

TORCH_MODEL: TorchFractalModel | None = None


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


class TorchTrainResponse(BaseModel):
    detail: str


@app.post("/torch-train", response_model=TorchTrainResponse)
def torch_train_route(authorization: str = Header(None)) -> TorchTrainResponse:
    authenticate(authorization)
    global TORCH_MODEL
    TORCH_MODEL = train_torch_fractal_model(epochs=50, lr=0.1)
    return TorchTrainResponse(detail="trained")


class TorchPredictRequest(BaseModel):
    codes: List[str]


class TorchPredictResponse(BaseModel):
    result: List[float]


def torch_predict_endpoint(req: TorchPredictRequest) -> TorchPredictResponse:
    if TORCH_MODEL is None:
        raise RuntimeError("model not trained")
    result = predict_torch_fractal(TORCH_MODEL, req.codes)
    return TorchPredictResponse(result=result)


@app.post("/torch-predict", response_model=TorchPredictResponse)
def torch_predict_route(
    req: TorchPredictRequest, authorization: str = Header(None)
) -> TorchPredictResponse:
    authenticate(authorization)
    return torch_predict_endpoint(req)
