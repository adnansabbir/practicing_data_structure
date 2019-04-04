from nose.tools import assert_equal


def string_compression(str):
    if len(str) == 0:
        return None

    previous_character = str[0]
    compressed_string = ""
    continuty = 0

    for character in str:
        if character == previous_character:
            continuty += 1
        else:
            compressed_string += "{}{}".format(previous_character, continuty)
            continuty = 1
            previous_character = character
    compressed_string += "{}{}".format(previous_character, continuty)

    return compressed_string


def test_string_compression():
    assert_equal(string_compression('AAABBaaB'), 'A3B2a2B1')
    assert_equal(string_compression(''), None)
    assert_equal(string_compression('AAAAAAAA'), 'A8')
    assert_equal(string_compression('AaAaAa'), 'A1a1A1a1A1a1')
    assert_equal(string_compression('aaaaaa'), 'a6')

    print("All Passed")


test_string_compression()