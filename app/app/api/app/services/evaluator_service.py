from app.services.metrics_service import calculate_metrics

def evaluate_response(response: str):
    metrics = calculate_metrics(response)

    # Weighted scoring system
    score = (
        metrics["correctness"] * 0.5 +
        metrics["reasoning"] * 0.3 +
        metrics["clarity"] * 0.2
    )

    # Determine correctness
    correctness = "correct" if metrics["correctness"] == 1 else "incorrect"

    # Confidence level
    if score > 0.8:
        confidence = "high"
    elif score > 0.5:
        confidence = "medium"
    else:
        confidence = "low"

    return {
        "metrics": metrics,
        "score": round(score, 2),
        "correctness": correctness,
        "confidence": confidence
    }
    "correctness": "correct" if score > 0.7 else "incorrect",
    "score": round(score, 2),
    "confidence": "high" if score > 0.8 else "medium",
    "reasoning": feedback
}
