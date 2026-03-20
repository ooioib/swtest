# tests/data_loader.py
import csv
import ast
from pathlib import Path


def load_test_data(filename):
    cases = []

    filepath = Path(__file__).resolve().parents[0] / "data" / filename

    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            a = ast.literal_eval(row["a"])
            b = ast.literal_eval(row["b"])
            expected_result = row["expected_result"]

            if expected_result == "TypeError":
                expected = TypeError
            else:
                expected = ast.literal_eval(expected_result)
            cases.append((a, b, expected))
            # print(cases)

    return cases
