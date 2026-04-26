from fastapi import APIRouter
from app.services.evaluator_service import evaluate_response

router = APIRouter()

@router.post("/evaluate")
def evaluate(data: dict):
    response = data.get("response", "")
    return evaluate_response(response)

@router.post("/batch-evaluate")
def batch_evaluate(data: list):
    results = []

    for item in data:
        response = item.get("response", "")
        results.append(evaluate_response(response))

    return {"results": results}
