def calculate_metrics(response: str):
    metrics = {
        "correctness": 0,
        "reasoning": 0,
        "clarity": 0
    }

    # correctness
    if "11" in response:
        metrics["correctness"] = 1

    # reasoning
    if "*" in response or "BODMAS" in response:
        metrics["reasoning"] = 1

    # clarity
    if "=" in response:
        metrics["clarity"] = 1

    return metrics
