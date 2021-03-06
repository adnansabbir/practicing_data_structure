from nose.tools import assert_equal
def min_coin(target, coins):

	if target in coins:
		return 1
	
	if len([c for c in coins if c<=target]) == 0:
		return 0
	
	min_no = 0
	for i in [c for c in coins if c<=target]:
		min = min_coin(target-i, coins)
		if min != 0:
			no_of_coins = 1+min 
			if no_of_coins<min_no or min_no==0:
				min_no = no_of_coins
	return min_no


def test_min_coin():
	assert_equal(min_coin(1,[1]), 1)
	assert_equal(min_coin(10,[1,5,10]), 1)
	assert_equal(min_coin(10,[1,5]), 2)
	assert_equal(min_coin(0,[1]), 0)
	assert_equal(min_coin(5,[6,8,9]), 0)
	assert_equal(min_coin(50,[1,5,10]), 5)
	assert_equal(min_coin(5,[3,3,10]), 0)
	print("All passed")

test_min_coin()