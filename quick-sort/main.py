def partition(arr, start, end):
	"""
	Partition an array around a pivot number, which in this case is the first number
	Move 2 pointers, 1 from the start (i) and 1 at the end (j) of the array until they crossed each other (i > j)
	
	During the traversal, if i points to a number greater than the pivot
	and j points to a number less than the pivot
	-> Swap numbers in these pointers
	
	After 2 pointers crossed each other, we need to:
	1. Swap the pivot number with the number at the end pointer
	2. Return the partition index, which is the index of the end pointer.
	We perform quick sort in 2 half of the original array
	divided by this partition index.
	"""
	pivot = arr[start]
	pivot_index = start

	while start < end:
		while start < len(arr) and arr[start] <= pivot:
			start += 1
		while arr[end] > pivot:
			end -= 1
		# Swap if 2 pointers have not crossed each other
		# and those pointers are pointing to 2 elements in 2 sides of the pivot
		# aka start is pointing to an element greater than the pivot
		# and end is pointing to an element less than the pivot
		if start < end:
			arr[start], arr[end] = arr[end], arr[start]

	
	# Swap pivot element with element on end pointer
	# this put pivot on its correct sorted place
	arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

	# Return the end pointer to divide the array into 2
	# before recursively quick sort in each half
	return end

def quick_sort(arr, start, end):
	"""
	Algorithm for sort an array
	"""
	if start < end:
		partition_index = partition(arr, start, end)
		quick_sort(arr, start, partition_index - 1)
		quick_sort(arr, partition_index + 1, end)


arr = [10, 2, 1, 9, 4, 6, 3]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array", arr)