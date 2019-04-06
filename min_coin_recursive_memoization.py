from nose.tools import assert_equal
from collections import defaultdict


def min_coin(target, coins, min_coin_dict=None):
    if min_coin_dict == None:
        min_coin_dict = defaultdict(int)

    if min_coin_dict[target] != 0:
        return min_coin_dict[target]

    if target in coins:
        min_coin_dict[target] = 1
        return 1

    if len([c for c in coins if c <= target]) == 0:
        return 0

    min_no = 0
    for i in [c for c in coins if c <= target]:
        min = min_coin(target - i, coins, min_coin_dict)
        if min != 0:
            no_of_coins = 1 + min
            if no_of_coins < min_no or min_no == 0:
                min_no = no_of_coins

    min_coin_dict[target] = min_no
    return min_no


def test_min_coin():
    assert_equal(min_coin(1, [1]), 1)
    assert_equal(min_coin(10, [1, 5, 10]), 1)
    assert_equal(min_coin(10, [1, 5]), 2)
    assert_equal(min_coin(0, [1]), 0)
    assert_equal(min_coin(5, [6, 8, 9]), 0)
    assert_equal(min_coin(50, [1, 5, 10]), 5)
    print("All passed")


test_min_coin()