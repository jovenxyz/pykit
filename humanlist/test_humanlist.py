from humanlist import humanlist


def test_empty():
    assert humanlist([]) == ""


def test_single():
    assert humanlist(["a"]) == "a"


def test_two():
    assert humanlist(["a", "b"]) == "a and b"


def test_three_default_oxford():
    assert humanlist(["a", "b", "c"]) == "a, b, and c"


def test_three_without_oxford():
    assert humanlist(["a", "b", "c"], oxford=False) == "a, b and c"


def test_custom_conjunction():
    assert humanlist(["a", "b", "c"], conjunction="or") == "a, b, or c"
    assert humanlist(["a", "b"], conjunction="or") == "a or b"


def test_non_string_items_are_coerced():
    assert humanlist([1, 2, 3]) == "1, 2, and 3"


def test_generator_input():
    assert humanlist(x for x in ["a", "b", "c"]) == "a, b, and c"


def test_four_items():
    assert humanlist(["red", "green", "blue", "yellow"]) == (
        "red, green, blue, and yellow"
    )
    assert humanlist(
        ["red", "green", "blue", "yellow"], oxford=False
    ) == "red, green, blue and yellow"
