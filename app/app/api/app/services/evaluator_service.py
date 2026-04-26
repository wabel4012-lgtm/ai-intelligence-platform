def evaluate_response(response: str):
    score = 0
    feedback = []

    # Correctness check
    if "5 + 3 * 2 = 11" in response:
        score += 0.5
        feedback.append("Correct calculation")

    else:
        feedback.append("Incorrect calculation")

    # Reasoning check
    if "BODMAS" in response or "*" in response:
        score += 0.3
        feedback.append("Proper reasoning applied")

    # Clarity check
    if "=" in response:
        score += 0.2
        feedback.append("Clear answer format")

    return {
        "score": round(score, 2),
        "feedback": feedback
    }
