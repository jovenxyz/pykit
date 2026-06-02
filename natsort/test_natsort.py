from natsort import natural_key


def test_natural_order():
    items = ["file10", "file2", "file1"]
    assert sorted(items, key=natural_key) == ["file1", "file2", "file10"]


def test_mixed_strings_and_numbers():
    items = ["a10", "a2", "a", "b1"]
    assert sorted(items, key=natural_key) == ["a", "a2", "a10", "b1"]


def test_case_insensitive():
    assert natural_key("File2") == natural_key("file2")


def test_pure_numbers():
    items = ["100", "20", "3"]
    assert sorted(items, key=natural_key) == ["3", "20", "100"]


def test_pure_strings():
    items = ["banana", "apple", "cherry"]
    assert sorted(items, key=natural_key) == ["apple", "banana", "cherry"]
