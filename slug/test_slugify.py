from slugify import slugify


def test_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_collapses_runs_of_non_alnum():
    assert slugify("  multiple   --  spaces  ") == "multiple-spaces"


def test_strips_unicode_accents():
    assert slugify("Cafe Creme") == "cafe-creme"
    assert slugify("Café Crème") == "cafe-creme"


def test_trims_leading_and_trailing_separators():
    assert slugify("---hello---") == "hello"


def test_custom_separator():
    assert slugify("Hello World", separator="_") == "hello_world"


def test_empty_or_all_punctuation_returns_empty():
    assert slugify("") == ""
    assert slugify("!!!") == ""
