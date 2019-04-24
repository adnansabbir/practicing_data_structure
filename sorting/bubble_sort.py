from sorting.test_sorting_algos import TestSorting


def bubble_sort(arr):
	for index in range(len(arr)):
		for index2 in range(1, len(arr)-index):
			if arr[index2-1]>arr[index2]:
				arr[index2],arr[index2-1] = arr[index2-1],arr[index2]
	return arr


t = TestSorting()
t.test(bubble_sort)