from app.services.evaluator_service import evaluate_response

def run_benchmark(dataset):
    results = []

    for item in dataset:
        result = evaluate_response(item["input"])
        results.append(result["score"])

    avg_score = sum(results) / len(results) if results else 0

    return {
        "average_score": round(avg_score, 2),
        "samples": len(results)
    }
