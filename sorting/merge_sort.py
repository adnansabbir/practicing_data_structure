from sorting.test_sorting_algos import TestSorting
def merge_sort(arr):
	length_of_arr = len(arr)
	if length_of_arr <= 1:
		return arr
	else:
		left = merge_sort(arr[:length_of_arr // 2])
		right = merge_sort(arr[length_of_arr // 2:])

		new_arr = []
		while len(left) > 0 or len(right) > 0:
			if len(left) and len(right):
				if left[0] < right[0]:
					new_arr.append(left.pop(0))
				else:
					new_arr.append(right.pop(0))
			else:
				new_arr = new_arr + left + right
				break
		return new_arr


T = TestSorting()
T.test(merge_sort)