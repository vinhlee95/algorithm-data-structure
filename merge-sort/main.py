def merge_sort(arr):
	"""
	Sort an array by devide-and-conquer design paradigm
	"""
	if len(arr) > 1:
		mid = len(arr) // 2

		# Divide
		first_half = arr[:mid]
		second_half = arr[mid:]

		merge_sort(first_half)
		merge_sort(second_half)

		# Conquer
		# Pointers
		i = j = k = 0

		while i < len(first_half) and j < len(second_half):
			if first_half[i] < second_half[j]:
				arr[k] = first_half[i]
				i += 1
			else:
				arr[k] = second_half[j]
				j += 1
			k += 1

		# Run out of index
		while i < len(first_half):
			arr[k] = first_half[i]
			i += 1
			k += 1

		while j < len(second_half):
			arr[k] = second_half[j]
			j += 1
			k += 1

arr = [101, 18, 3, 7, 5, 2, 9, 4, 8, 6, 13, 11, 45, 27]
merge_sort(arr)
print('Sorted array is', arr)