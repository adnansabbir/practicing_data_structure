from nose.tools import assert_equal

class MaxContinuousSum(object):
	def test(self,function):
		assert_equal(function([]), (None, None, 0))
		assert_equal(function([1]), (0, 0, 1))
		assert_equal(function([-1]), (None, None, 0))
		assert_equal(function([1, 2, 3, 4, 5, 6, 7, 8, 9]), (0, 8, 45))
		assert_equal(function([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]), (1, 9, 45))
		assert_equal(function([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, -2]), (1, 9, 45))
		assert_equal(function([1, 2, 3, -10, 8]), (4, 4, 8))
		print("All Passed")