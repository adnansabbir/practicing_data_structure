from nose.tools import assert_equal


def sequential_search_unsorted(arr, elem):
    for i in arr:
        if i == elem:
            return True
    return False


def sequential_search_sorted(arr, elem):
    for i in arr:
        if i == elem:
            return True
        elif i > elem:
            return False
    return False


def test():
    print("Testing Unsorted")
    assert_equal(sequential_search_unsorted([], 0), False)
    assert_equal(sequential_search_unsorted([1, 2, 3, 4, 5], 0), False)
    assert_equal(sequential_search_unsorted([5, 4, 7, 8, 2, 4, 6, 5, 8, 9, 1], 0), False)
    assert_equal(sequential_search_unsorted([4, 5, 6, 2, 1, 7, 8, 9, 6, 5, 4, 5], 6), True)

    print("Testing Sorted")
    assert_equal(sequential_search_sorted([], 0), False)
    assert_equal(sequential_search_sorted([1, 2, 3, 4, 5, 6], 0), False)
    assert_equal(sequential_search_sorted([5, 6, 7, 8, 9, 10], 10), True)
    assert_equal(sequential_search_sorted([1], 1), True)
    print("All Passed")


test()