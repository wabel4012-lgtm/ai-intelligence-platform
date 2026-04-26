from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test():
    return {"message": "API is working"}

@router.post("/evaluate")
def evaluate(data: dict):
    response = data.get("response", "")

    if "5 + 3 * 2 = 16" in response:
        return {
            "correctness": "incorrect",
            "reason": "BODMAS rule violated",
            "score": 0.3
        }

    return {
        "correctness": "unknown",
        "reason": "not evaluated",
        "score": 0.5
    }
