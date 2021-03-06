from sorting.test_sorting_algos import TestSorting


def shell_sort(arr):
	gap = len(arr) // 2
	while gap:
		for i in range(gap):
			gap_insertion_sort(arr, i, gap)
		gap = gap // 2
	return arr


def gap_insertion_sort(arr, index, gap):
	for i in range(index + gap, len(arr), gap):
		position = i

		while position >= gap and arr[position - gap] > arr[position]:
			arr[position - gap], arr[position] = arr[position], arr[position - gap]
			position -= gap


T = TestSorting()
T.test(shell_sort)