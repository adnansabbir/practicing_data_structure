from sorting.test_sorting_algos import TestSorting


def insertion_sort(arr):
	for index in range(1,len(arr)):
		item = arr[index]
		for index2 in range(index-1,-1,-1):
			if item>=arr[index2]:
				arr[index2+1] = item
				break
			else:
				arr[index2],arr[index2+1] = arr[index2+1], arr[index2]
				if index2 == 0:
					arr[index2] = item
	return arr

T = TestSorting()
T.test(insertion_sort)