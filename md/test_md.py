from md import to_plain_text


def test_plain_text_unchanged():
    assert to_plain_text("hello world") == "hello world"


def test_header_stripped():
    assert to_plain_text("# Title") == "Title"
    assert to_plain_text("### Sub heading") == "Sub heading"


def test_bold_and_italic():
    assert to_plain_text("**bold** and *italic*") == "bold and italic"
    assert to_plain_text("__bold__ and _italic_") == "bold and italic"


def test_strikethrough():
    assert to_plain_text("~~gone~~") == "gone"


def test_inline_code():
    assert to_plain_text("use `print()` to debug") == "use print() to debug"


def test_link():
    assert to_plain_text("see [docs](https://example.com)") == "see docs"


def test_image():
    assert to_plain_text("![alt text](image.png)") == "alt text"


def test_list_bullets_and_numbers():
    text = "- one\n- two\n1. first\n2. second"
    assert to_plain_text(text) == "one\ntwo\nfirst\nsecond"


def test_blockquote_marker_removed():
    assert to_plain_text("> quoted\n> line") == "quoted\nline"


def test_horizontal_rule_removed():
    assert to_plain_text("above\n---\nbelow") == "above\n\nbelow"


def test_code_block_preserved_without_fences():
    md = "```python\nprint('hi')\n```"
    assert to_plain_text(md) == "print('hi')"
