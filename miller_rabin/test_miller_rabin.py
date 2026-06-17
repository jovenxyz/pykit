from miller_rabin import is_prime, next_prime


def test_small_primes():
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
    for n in range(2, 50):
        assert is_prime(n) == (n in primes)


def test_negative_and_small_non_primes():
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(-7)


def test_carmichael_number():
    # Miller-Rabin catches Carmichael numbers that fool naive Fermat tests.
    assert not is_prime(561)
    assert not is_prime(1105)
    assert not is_prime(1729)


def test_large_known_primes():
    assert is_prime(982451653)               # 50 millionth prime
    assert is_prime(10 ** 12 + 39)            # 1_000_000_000_039 is prime


def test_large_known_composites():
    assert not is_prime(10 ** 12)
    assert not is_prime(10 ** 12 + 1)


def test_next_prime():
    assert next_prime(10) == 11
    assert next_prime(11) == 13
    assert next_prime(1) == 2
    assert next_prime(0) == 2
    assert next_prime(100) == 101


def test_very_large_prime():
    assert is_prime((1 << 31) - 1)            # Mersenne prime M_31
