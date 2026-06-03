from urlquery import build_query, parse_query


def test_parse_basic():
    assert parse_query("a=1&b=2") == {"a": ["1"], "b": ["2"]}


def test_parse_repeated_keys():
    assert parse_query("a=1&b=2&a=3") == {"a": ["1", "3"], "b": ["2"]}


def test_parse_leading_question_mark():
    assert parse_query("?a=1") == {"a": ["1"]}


def test_parse_empty():
    assert parse_query("") == {}
    assert parse_query("?") == {}


def test_parse_decodes_percent_and_plus():
    assert parse_query("name=Hello%20World") == {"name": ["Hello World"]}
    assert parse_query("name=Hello+World") == {"name": ["Hello World"]}


def test_parse_value_without_equals():
    assert parse_query("flag&a=1") == {"flag": [""], "a": ["1"]}


def test_build_basic():
    assert build_query({"a": "1", "b": "2"}) == "a=1&b=2"


def test_build_url_encodes_values():
    assert build_query({"name": "Hello World"}) == "name=Hello%20World"
    assert build_query({"q": "a&b"}) == "q=a%26b"


def test_build_repeated_keys_from_list():
    assert build_query({"a": ["1", "2"]}) == "a=1&a=2"


def test_build_from_pairs():
    assert build_query([("a", "1"), ("b", "2"), ("a", "3")]) == "a=1&b=2&a=3"


def test_round_trip():
    params = {"name": "Hello World", "tags": ["py", "test"]}
    parsed = parse_query(build_query(params))
    assert parsed["name"] == ["Hello World"]
    assert parsed["tags"] == ["py", "test"]
