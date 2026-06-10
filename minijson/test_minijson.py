import pytest

from minijson import JSONDecodeError, loads


def test_simple_values():
    assert loads("null") is None
    assert loads("true") is True
    assert loads("false") is False
    assert loads("42") == 42
    assert loads("-3.14") == -3.14
    assert loads('"hello"') == "hello"


def test_array():
    assert loads("[1, 2, 3]") == [1, 2, 3]
    assert loads("[]") == []
    assert loads("[[1], [2, 3]]") == [[1], [2, 3]]


def test_object():
    assert loads('{"a": 1, "b": 2}') == {"a": 1, "b": 2}
    assert loads("{}") == {}


def test_nested():
    assert loads('{"x": [1, {"y": null}], "z": true}') == {
        "x": [1, {"y": None}],
        "z": True,
    }


def test_string_escapes():
    assert loads(r'"a\nb"') == "a\nb"
    assert loads(r'"q\"q"') == 'q"q'
    assert loads(r'"é"') == "é"


def test_whitespace_around_tokens():
    assert loads('  {  "a"  :  1  ,  "b"  :  2  }  ') == {"a": 1, "b": 2}


def test_trailing_data_raises():
    with pytest.raises(JSONDecodeError):
        loads("1 2")


def test_invalid_token_raises():
    with pytest.raises(JSONDecodeError):
        loads("trueish")


def test_unterminated_string_raises():
    with pytest.raises(JSONDecodeError):
        loads('"hello')


def test_number_types():
    assert isinstance(loads("0"), int)
    assert isinstance(loads("0.5"), float)
    assert loads("1e3") == 1000.0
