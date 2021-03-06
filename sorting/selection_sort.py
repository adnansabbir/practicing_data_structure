from sorting.test_sorting_algos import TestSorting


def selection_sort(arr):
    for i in range(len(arr) - 1):
        index_of_min = i + find_index_min(arr[i:])
        arr[i], arr[index_of_min] = arr[index_of_min], arr[i]
    return arr


def find_index_min(arr):
    if not len(arr):
        return None

    index_of_min = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[index_of_min]:
            index_of_min = i
    return index_of_min


t = TestSorting()
t.test(selection_sort)