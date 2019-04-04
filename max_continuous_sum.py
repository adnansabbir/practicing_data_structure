def max_continuous_sum(list):
    current_sum = max_sum = 0
    starting_index = ending_index = 0

    for index, num in enumerate(list):
        current_sum += num
        if current_sum < 0:
            starting_index = index + 1
            current_sum = 0
        elif current_sum > max_sum:
            ending_index = index
            max_sum = current_sum

    if max_sum == 0:
        starting_index = ending_index = None
    return starting_index, ending_index, max_sum

# print(max_continuous_sum([1, 2, -10, 3, 4, 10, 10, -10, -50, 100]))
# print(max_continuous_sum([-1]))
from test_max_continuous_sum import MaxContinuousSum
t = MaxContinuousSum()
t.test(max_continuous_sum)