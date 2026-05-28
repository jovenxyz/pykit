import json

from csvjson.convert import (
    csv_to_json,
    csv_to_records,
    json_to_csv,
    records_to_csv,
)


def test_csv_to_records():
    text = "name,age\nalice,30\nbob,25\n"
    assert csv_to_records(text) == [
        {"name": "alice", "age": "30"},
        {"name": "bob", "age": "25"},
    ]


def test_records_round_trip():
    text = "name,age\nalice,30\nbob,25\n"
    records = csv_to_records(text)
    assert csv_to_records(records_to_csv(records)) == records


def test_csv_to_json_is_valid_json():
    assert json.loads(csv_to_json("name,age\nalice,30\n")) == [
        {"name": "alice", "age": "30"}
    ]


def test_json_to_csv_round_trip():
    records = [{"name": "alice", "age": "30"}, {"name": "bob", "age": "25"}]
    csv_text = json_to_csv(json.dumps(records))
    assert csv_to_records(csv_text) == records
