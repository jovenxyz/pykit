from anagrams import are_anagrams, group_anagrams, signature


def test_signature_matches_for_anagrams():
    assert signature("listen") == signature("silent")
    assert signature("Triangle") == signature("integral")


def test_signature_case_sensitive_when_requested():
    assert signature("AB", case_insensitive=False) != signature(
        "ab", case_insensitive=False
    )


def test_are_anagrams():
    assert are_anagrams("listen", "silent")
    assert are_anagrams("Triangle", "Integral")
    assert not are_anagrams("hello", "world")


def test_group_anagrams_basic():
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert groups == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


def test_group_anagrams_preserves_within_group_order():
    assert group_anagrams(["cat", "act", "tac"]) == [["cat", "act", "tac"]]


def test_group_anagrams_case_insensitive():
    assert group_anagrams(["Listen", "silent"]) == [["Listen", "silent"]]


def test_group_anagrams_case_sensitive():
    assert group_anagrams(["AB", "ab"], case_insensitive=False) == [["AB"], ["ab"]]


def test_empty_input():
    assert group_anagrams([]) == []
