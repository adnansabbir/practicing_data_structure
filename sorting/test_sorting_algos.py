from nose.tools import assert_equal


class TestSorting(object):

	def test(self, function):
		arr = []
		assert_equal(function(arr), sorted(arr))
		arr = [0,0,0,0]
		assert_equal(function(arr), sorted(arr))
		arr = [1,1,1,1,1]
		assert_equal(function(arr), sorted(arr))
		arr = [10,9,8,7,6,5,4]
		assert_equal(function(arr), sorted(arr))
		arr = [4,5,6,7,8,9]
		assert_equal(function(arr), sorted(arr))
		arr = [2,4,6,3,7,1]
		assert_equal(function(arr), sorted(arr))
		arr = [0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
		assert_equal(function(arr), sorted(arr))
		print("All Passed")