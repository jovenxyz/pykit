import pytest

from pluralize import pluralize, quantity


@pytest.mark.parametrize("word,plural", [
    ("cat", "cats"),
    ("dog", "dogs"),
    ("bus", "buses"),
    ("box", "boxes"),
    ("buzz", "buzzes"),
    ("church", "churches"),
    ("dish", "dishes"),
    ("city", "cities"),
    ("baby", "babies"),
    ("boy", "boys"),       # vowel before y -> just add s
    ("day", "days"),
    ("leaf", "leaves"),
    ("knife", "knives"),
])
def test_regular_rules(word, plural):
    assert pluralize(word) == plural


def test_irregular_plurals():
    assert pluralize("man") == "men"
    assert pluralize("woman") == "women"
    assert pluralize("child") == "children"
    assert pluralize("foot") == "feet"
    assert pluralize("person") == "people"


def test_uncountable_words():
    assert pluralize("fish") == "fish"
    assert pluralize("sheep") == "sheep"
    assert pluralize("data") == "data"


def test_count_one_returns_singular():
    assert pluralize("cat", count=1) == "cat"
    assert pluralize("man", count=1) == "man"


def test_case_preserved_for_irregulars():
    assert pluralize("Child") == "Children"
    assert pluralize("MAN") == "MEN"


def test_quantity():
    assert quantity(1, "cat") == "1 cat"
    assert quantity(2, "cat") == "2 cats"
    assert quantity(0, "cat") == "0 cats"
    assert quantity(3, "child") == "3 children"


def test_quantity_custom_plural():
    assert quantity(2, "cactus", "cacti") == "2 cacti"
    assert quantity(1, "cactus", "cacti") == "1 cactus"
