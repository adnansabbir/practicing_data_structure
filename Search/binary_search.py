from nose.tools import assert_equal


def binary_search(arr, elem):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == elem:
            return True
        elif elem < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


def rec_binary_search(arr, elem):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == elem:
            return True
        elif elem < arr[mid]:
            return rec_binary_search(arr[:mid], elem)
        else:
            return rec_binary_search(arr[mid + 1:], elem)


bin_tree1 = [1, 3, 5, 6, 9, 10, 15, 80, 99, 150]
bin_tree6 = [1, 3, 5, 6, 9, 10, 15, 80, 99, 150, 160]
bin_tree2 = [0]
bin_tree3 = []
bin_tree4 = [15, 80, 99, 150]
bin_tree5 = [-150, -99, -80, 15]


def test_binary_search():
    print("Testing Binary Search")
    assert_equal(binary_search(bin_tree1, 99), True)
    assert_equal(binary_search(bin_tree1, 100), False)

    assert_equal(binary_search(bin_tree6, 99), True)
    assert_equal(binary_search(bin_tree6, 100), False)

    assert_equal(binary_search(bin_tree2, 0), True)
    assert_equal(binary_search(bin_tree2, 100), False)

    assert_equal(binary_search(bin_tree3, 100), False)

    assert_equal(binary_search(bin_tree4, 15), True)
    assert_equal(binary_search(bin_tree4, 10), False)

    assert_equal(binary_search(bin_tree5, -150), True)
    assert_equal(binary_search(bin_tree5, 100), False)

    print("All passed")


def test_rec_binary_search():
    print("Testing Recursive Binary Search")
    assert_equal(rec_binary_search(bin_tree1, 99), True)
    assert_equal(rec_binary_search(bin_tree1, 100), False)

    assert_equal(rec_binary_search(bin_tree6, 99), True)
    assert_equal(rec_binary_search(bin_tree6, 100), False)

    assert_equal(rec_binary_search(bin_tree2, 0), True)
    assert_equal(rec_binary_search(bin_tree2, 100), False)

    assert_equal(rec_binary_search(bin_tree3, 100), False)

    assert_equal(rec_binary_search(bin_tree4, 15), True)
    assert_equal(rec_binary_search(bin_tree4, 10), False)

    assert_equal(rec_binary_search(bin_tree5, -150), True)
    assert_equal(rec_binary_search(bin_tree5, 100), False)

    print("All passed")


test_binary_search()
test_rec_binary_search()