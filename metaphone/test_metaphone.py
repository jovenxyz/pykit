import pytest
from metaphone import metaphone


def test_empty_input():
    assert metaphone("") == ""
    assert metaphone("   ") == ""
    assert metaphone("123!!") == ""


def test_drops_silent_initial_letters():
    assert metaphone("knight").startswith("N")
    assert metaphone("gnome").startswith("N")
    assert metaphone("pneumonia").startswith("N")
    assert metaphone("wrist").startswith("R")


def test_initial_x_becomes_s():
    assert metaphone("xenon").startswith("S")


def test_ph_becomes_f():
    assert metaphone("phone") == metaphone("fone")


def test_th_becomes_0():
    assert metaphone("thumb").startswith("0")
    assert metaphone("through").startswith("0")


def test_sh_becomes_x():
    assert metaphone("ship").startswith("X")


def test_ch_becomes_x():
    assert metaphone("chair").startswith("X")


def test_homophones_match():
    assert metaphone("write") == metaphone("right")
    assert metaphone("see") == metaphone("sea")
    assert metaphone("knight") == metaphone("night")


def test_case_insensitive():
    assert metaphone("Thompson") == metaphone("THOMPSON") == metaphone("thompson")


def test_strips_non_alpha():
    assert metaphone("Mc-Donald's") == metaphone("McDonalds")


def test_x_inside_word_becomes_ks():
    assert "KS" in metaphone("box")
