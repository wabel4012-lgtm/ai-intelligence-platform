class AIResponseEvaluator:

    def __init__(self):
        self.weights = {
            "correctness": 0.35,
            "reasoning": 0.25,
            "clarity": 0.15,
            "completeness": 0.15,
            "instruction": 0.10
        }

    def score(self, r: dict):
        return sum(r[k] * w for k, w in self.weights.items())


def evaluate_ai_response(payload: dict):
    evaluator = AIResponseEvaluator()
    score = evaluator.score(payload)

    return {
        "score": round(score, 3),
        "grade": "A" if score > 0.85 else "B" if score > 0.7 else "C"
    }
