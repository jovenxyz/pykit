from piglatin import translate, translate_word


def test_consonant_cluster_moves_to_end():
    assert translate_word("hello") == "ellohay"
    assert translate_word("string") == "ingstray"


def test_vowel_start_gets_way():
    assert translate_word("egg") == "eggway"
    assert translate_word("apple") == "appleway"


def test_capitalisation_preserved():
    assert translate_word("Hello") == "Ellohay"


def test_empty_word():
    assert translate_word("") == ""


def test_translate_keeps_non_letters():
    assert translate("Hello, World!") == "Ellohay, Orldway!"


def test_y_treated_as_vowel_after_consonant():
    assert translate_word("my") == "ymay"
    assert translate_word("rhythm") == "ythmrhay"


def test_translate_multiple_words():
    assert translate("the quick brown fox") == "ethay uickqay ownbray oxfay"
