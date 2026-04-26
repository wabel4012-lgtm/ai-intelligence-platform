def evaluate_response(response: str):
    result = {
        "correctness": "unknown",
        "reason": "",
        "score": 0.5
    }

    # Rule 1: Basic math validation example
    if "5 + 3 * 2 = 16" in response:
        result["correctness"] = "incorrect"
        result["reason"] = "BODMAS rule violated"
        result["score"] = 0.2

    elif "5 + 3 * 2 = 11" in response:
        result["correctness"] = "correct"
        result["reason"] = "Correct application of BODMAS"
        result["score"] = 1.0

    return result
