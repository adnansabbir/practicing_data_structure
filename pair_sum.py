from test_pair_sum import TestPair


def pair_sum(list, num):
    pairs = []

    if len(list) < 2:
        return 0
    else:
        list.sort()
        for index, number1 in enumerate(list):
            for number2 in list[index + 1:]:
                if number2 > num:
                    break
                elif number1 + number2 == num:
                    pairs.append([number1, number2])
            if number1 > num:
                break
    return len(pairs)


t = TestPair()
t.test(pair_sum)
# print(pair_sum([1, 1, 3, 2, 3, 5, 6, 8, 94, 5, 9, 8, 5, 4, 58, 9, 4, 5, 9, 6, 5, 4, 8, 9, 5, 4, 9, ], 10))
