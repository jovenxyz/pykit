from diff import DiffLine, diff_lines, format_diff


def test_identical_inputs():
    text = "foo\nbar\n"
    assert all(line.tag == " " for line in diff_lines(text, text))


def test_pure_addition():
    assert diff_lines("a\nb", "a\nb\nc") == [
        DiffLine(" ", "a"),
        DiffLine(" ", "b"),
        DiffLine("+", "c"),
    ]


def test_pure_removal():
    assert diff_lines("a\nb\nc", "a\nb") == [
        DiffLine(" ", "a"),
        DiffLine(" ", "b"),
        DiffLine("-", "c"),
    ]


def test_replacement():
    assert diff_lines("a\nb\nc", "a\nz\nc") == [
        DiffLine(" ", "a"),
        DiffLine("-", "b"),
        DiffLine("+", "z"),
        DiffLine(" ", "c"),
    ]


def test_empty_to_text():
    assert diff_lines("", "x\ny") == [DiffLine("+", "x"), DiffLine("+", "y")]


def test_text_to_empty():
    assert diff_lines("x\ny", "") == [DiffLine("-", "x"), DiffLine("-", "y")]


def test_format_diff_renders_with_tags():
    output = format_diff("foo\nbar", "foo\nbaz")
    assert output == "  foo\n- bar\n+ baz"


def test_handles_lines_without_trailing_newline():
    diff = diff_lines("a\nb", "a\nb")
    assert all(line.tag == " " for line in diff)
    assert [line.text for line in diff] == ["a", "b"]
