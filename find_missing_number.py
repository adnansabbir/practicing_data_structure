from test_find_missing_number import FindMissingNumber


def find_missing(list1, list2):
    if len(list1) != (len(list2) + 1):
        return "Error in Input"

    list1.sort()
    list2.sort()

    for i in range(len(list1) - 1):
        if list1[i] != list2[i]:
            return "{} is the missing number".format(list1[i])
    return "{} is the missing number".format(list1[-1])


# arr = [1,2,3,4,5]
# print(arr[-1])
t = FindMissingNumber()
t.test(find_missing)
# print(find_missing([1, 2, 3, 4, 5, 6, 7], [7, 6, 4, 3, 2, 1]))
