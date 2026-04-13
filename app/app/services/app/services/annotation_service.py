class AnnotationEngine:

    def __init__(self):
        self.store = []

    def annotate(self, item):
        self.store.append(item)

    def confidence_filter(self, threshold=0.7):
        return [x for x in self.store if x["confidence"] < threshold]

def run_annotation_batch(items):
    engine = AnnotationEngine()

    for i in items:
        engine.annotate(i)

    return {
        "total": len(items),
        "low_confidence": engine.confidence_filter()
    }
