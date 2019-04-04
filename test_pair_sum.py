from nose.tools import assert_equal


class TestPair(object):
    def test(self, function):
        assert_equal(function([], 5), 0)
        assert_equal(function([1], 5), 0)
        assert_equal(function([1,2,3,4,5,6,7,8,9,10], 5), 2)
        assert_equal(function([0,1,2,3,4,7,8,9,0], 0), 1)
        assert_equal(function([1,3,5,6,8,9], 0), 0)
        print('All Passed')
