"""Convert between CSV and JSON representations."""
from __future__ import annotations

import csv
import io
import json
from typing import Any, Dict, List


def csv_to_records(text: str) -> List[Dict[str, str]]:
    reader = csv.DictReader(io.StringIO(text))
    return [dict(row) for row in reader]


def records_to_json(records: List[Dict[str, Any]], indent: int = 2) -> str:
    return json.dumps(records, indent=indent)


def csv_to_json(text: str, indent: int = 2) -> str:
    return records_to_json(csv_to_records(text), indent=indent)


def json_to_records(text: str) -> List[Dict[str, Any]]:
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("expected a JSON array of objects")
    return data


def records_to_csv(records: List[Dict[str, Any]]) -> str:
    if not records:
        return ""
    fieldnames = list(records[0].keys())
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for record in records:
        writer.writerow(record)
    return output.getvalue()


def json_to_csv(text: str) -> str:
    return records_to_csv(json_to_records(text))
