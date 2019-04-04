from nose.tools import assert_equal


def recursive_reverse(s):
    if len(s) < 1:
        return s
    return s[-1] + recursive_reverse(s[:len(s) - 1])


def test_recursive_reverse():
    assert_equal(recursive_reverse(''), ''[::-1])
    assert_equal(recursive_reverse('Hello World'), 'Hello World'[::-1])
    assert_equal(recursive_reverse('0123456789'), '0123456789'[::-1])
    assert_equal(recursive_reverse('0'), '0'[::-1])
    assert_equal(recursive_reverse('a'), 'a'[::-1])
    assert_equal(recursive_reverse('a.-'), 'a.-'[::-1])
    assert_equal(recursive_reverse(' . . . - \    '), ' . . . - \    '[::-1])
    assert_equal(recursive_reverse('    '), '    '[::-1])
    print("All test passed")


test_recursive_reverse()