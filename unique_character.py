from nose.tools import assert_equal


def unique_character(word):
    if len(word) == 0:
        return True

    word = sorted(word)
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return False

    return True


def test_unique_character():
    assert_equal(unique_character('abcd'), True)
    assert_equal(unique_character(''), True)
    assert_equal(unique_character('aa'), False)
    assert_equal(unique_character('abcda'), False)
    assert_equal(unique_character('a1'), True)
    assert_equal(unique_character('aA'), True)

    print("Test Successful")


test_unique_character()