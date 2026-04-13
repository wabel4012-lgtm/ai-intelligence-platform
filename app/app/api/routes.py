from fastapi import APIRouter
from app.services.evaluator_service import evaluate_ai_response
from app.services.validation_service import validate_dataset

router = APIRouter()

@router.post("/evaluate")
def evaluate(payload: dict):
    return evaluate_ai_response(payload)

@router.post("/validate-dataset")
def validate(payload: dict):
    return validate_dataset(payload)
