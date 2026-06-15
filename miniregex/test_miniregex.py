from miniregex import match


def test_literal():
    assert match("abc", "abc")
    assert match("abc", "xabcy")
    assert not match("abc", "abd")


def test_dot():
    assert match("a.c", "abc")
    assert match("a.c", "axc")
    assert not match("a.c", "ac")


def test_star():
    assert match("a*", "")
    assert match("a*", "aaa")
    assert match("a*b", "b")
    assert match("a*b", "aaab")
    assert not match("a*b", "ac")


def test_plus():
    assert match("a+", "a")
    assert match("a+b", "aaab")
    assert not match("a+b", "b")


def test_question():
    assert match("a?b", "b")
    assert match("a?b", "ab")
    # 'a?b' allows zero or one 'a' before 'b'; "aab" matches starting at index 1.
    assert match("a?b", "aab")


def test_dot_star():
    assert match(".*", "anything")
    assert match("a.*z", "abcz")
    assert match("a.*z", "az")


def test_anchors():
    assert match("^abc$", "abc")
    assert not match("^abc$", "xabc")
    assert not match("^abc$", "abcy")
    assert match("^abc", "abcdef")
    assert match("abc$", "xyzabc")


def test_empty_pattern_matches_anywhere():
    assert match("", "")
    assert match("", "anything")


def test_combined():
    assert match("^a+b*c?$", "aaabbb")
    assert match("^a+b*c?$", "abc")
    assert match("^a+b*c?$", "aaaa")
    assert not match("^a+b*c?$", "")
