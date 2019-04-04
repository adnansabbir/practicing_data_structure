from nose.tools import assert_equal


class FindMissingNumber(object):
    def test(self, function):
        assert_equal(function([], []), "Error in Input")
        assert_equal(function([1, 2], []), "Error in Input")
        assert_equal(function([], [1]), "Error in Input")
        assert_equal(function([1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 5, 4, 3, 2, 1]), "6 is the missing number")
        assert_equal(function([1, 2, 3, 4, 5, 6, 6, 7, 8, 9], [9, 8, 7, 5, 6, 4, 3, 2, 1]), "6 is the missing number")
        assert_equal(function([1, 2, 3, 4, 5, 6, 6, 7, 8, 9], [8, 7, 5, 6, 6, 4, 3, 2, 1]), "9 is the missing number")
        print('All Passed')
