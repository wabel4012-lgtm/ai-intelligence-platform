def validate_dataset(dataset):
    issues = []

    for i, item in enumerate(dataset):
        if "input" not in item or "expected_output" not in item:
            issues.append(f"Missing fields in item {i}")

    return {
        "valid": len(issues) == 0,
        "issues": issues
    }
