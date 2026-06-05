import random

import pytest

from markov import MarkovChain


def test_invalid_order_raises():
    with pytest.raises(ValueError):
        MarkovChain(order=0)


def test_generate_without_training_raises():
    chain = MarkovChain(order=2)
    with pytest.raises(RuntimeError):
        chain.generate(10)


def test_short_input_is_ignored():
    chain = MarkovChain(order=3)
    chain.train(["a", "b"])    # shorter than order: no error, no state added
    assert chain.starts == []


def test_deterministic_with_seeded_rng():
    chain = MarkovChain(order=1)
    chain.train("the cat sat on the mat".split())
    a = chain.generate(6, rng=random.Random(42))
    b = chain.generate(6, rng=random.Random(42))
    assert a == b


def test_generated_tokens_come_from_training_vocabulary():
    tokens = "the quick brown fox jumps over the lazy dog".split()
    chain = MarkovChain(order=1)
    chain.train(tokens)
    vocab = set(tokens)
    generated = chain.generate(20, rng=random.Random(0))
    assert set(generated) <= vocab


def test_chain_terminates_when_no_continuation():
    chain = MarkovChain(order=1)
    chain.train(["a", "b", "c"])   # transitions: a->b, b->c; c has no follower
    output = chain.generate(20, rng=random.Random(0))
    assert output == ["a", "b", "c"]


def test_order_property():
    assert MarkovChain(order=3).order == 3
