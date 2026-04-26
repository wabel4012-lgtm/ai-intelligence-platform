from fastapi import APIRouter
from app.services.evaluator_service import evaluate_response

router = APIRouter()

@router.post("/evaluate")
def evaluate(data: dict):
    response = data.get("response", "")
    return evaluate_response(response)

@router.post("/pipeline")
def full_pipeline(data: dict):
    response = data.get("response", "")
    
    evaluation = evaluate_response(response)
    
    return {
        "input": response,
        "evaluation": evaluation,
        "status": "processed"
    }

from pydantic import BaseModel

class EvaluateRequest(BaseModel):
    response: str

@router.post("/evaluate")
def evaluate(data: EvaluateRequest):
    return evaluate_response(data.response)

try:
    result = evaluate_response(response)
except Exception as e:
    return {"error": str(e)}
