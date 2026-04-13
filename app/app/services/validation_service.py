import pandas as pd

class DatasetIntelligence:

    def detect_nulls(self, df):
        return df.isnull().mean().to_dict()

    def detect_outliers(self, df, column):
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        return df[(df[column] < q1 - 1.5 * iqr) | (df[column] > q3 + 1.5 * iqr)]

def validate_dataset(payload: dict):
    df = pd.DataFrame(payload["data"])

    engine = DatasetIntelligence()

    return {
        "null_report": engine.detect_nulls(df),
        "outliers": len(engine.detect_outliers(df, payload["column"]))
    }
