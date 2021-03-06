from nose.tools import assert_equal
from stack import Stack


def balanced_check(s):
    opening_stack = Stack()
    closing_dict = {')': '(', '}': '{', ']': '['}

    for character in list(s):
        if character in closing_dict:
            if opening_stack.isEmpty():
                return False
            elif closing_dict[character] != opening_stack.pop():
                return False
        else:
            opening_stack.push(character)
    if opening_stack.isEmpty():
        return True
    else:
        return False


def test_balanced_check():
    assert_equal(balanced_check('['), False)
    assert_equal(balanced_check('[{('), False)
    assert_equal(balanced_check('[{()}'), False)
    assert_equal(balanced_check('[]'), True)
    assert_equal(balanced_check('[][]'), True)
    assert_equal(balanced_check('()'), True)
    assert_equal(balanced_check('[[[(){}{()}]]]'), True)
    assert_equal(balanced_check('[[[]{}([])]]()'), True)
    assert_equal(balanced_check(')'), False)

    print("All passed")


test_balanced_check()