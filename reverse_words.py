from nose.tools import assert_equal


def reverse_words(sentence):
    splited_words = sentence.split(' ')
    words = list(filter(None, splited_words))
    words.reverse()
    return ' '.join(words)


def test_reverse_words():
    assert_equal(reverse_words('Hi There'), 'There Hi')
    assert_equal(reverse_words('  Hi There'), 'There Hi')
    assert_equal(reverse_words('Hello World    '), 'World Hello')
    assert_equal(reverse_words(''), '')
    assert_equal(reverse_words('     '), '')

    print("All test Passed")

test_reverse_words()