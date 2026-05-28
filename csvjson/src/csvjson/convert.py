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
