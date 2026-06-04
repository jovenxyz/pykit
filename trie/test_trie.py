from trie import Trie


def test_insert_and_contains():
    trie = Trie()
    trie.insert("hello")
    trie.insert("hell")
    assert "hello" in trie
    assert "hell" in trie
    assert "help" not in trie


def test_starts_with():
    trie = Trie()
    trie.insert("hello")
    assert trie.starts_with("he")
    assert trie.starts_with("hello")
    assert not trie.starts_with("world")


def test_with_prefix_returns_all_completions():
    trie = Trie()
    for word in ("cat", "car", "cart", "dog"):
        trie.insert(word)
    assert sorted(trie.with_prefix("ca")) == ["car", "cart", "cat"]
    assert sorted(trie.with_prefix("c")) == ["car", "cart", "cat"]
    assert trie.with_prefix("z") == []


def test_with_prefix_includes_the_prefix_itself_when_present():
    trie = Trie()
    trie.insert("foo")
    trie.insert("foobar")
    assert sorted(trie.with_prefix("foo")) == ["foo", "foobar"]


def test_len_counts_unique_words():
    trie = Trie()
    assert len(trie) == 0
    trie.insert("a")
    trie.insert("ab")
    assert len(trie) == 2
    trie.insert("a")  # duplicate
    assert len(trie) == 2


def test_empty_string_insert():
    trie = Trie()
    trie.insert("")
    assert "" in trie
    assert len(trie) == 1
