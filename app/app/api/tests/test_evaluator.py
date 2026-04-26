from app.services.evaluator_service import evaluate_response

def test_correct_case():
    result = evaluate_response("5 + 3 * 2 = 11")
    assert result["score"] > 0.8

def test_incorrect_case():
    result = evaluate_response("5 + 3 * 2 = 16")
    assert result["score"] < 0.5
