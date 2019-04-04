from nose.tools import assert_equal

def factorial(num):
	if num == 0:
		return 1
	else:
		return num*factorial(num-1)

def test_factorial():
	assert_equal(factorial(0),1)
	assert_equal(factorial(1),1)
	assert_equal(factorial(5),120)
	assert_equal(factorial(10),3628800)
	assert_equal(factorial(14),87178291200)
	
	print("All Passed")

test_factorial()