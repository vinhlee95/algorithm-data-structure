"""
Quick Select (Randomised selection) algorithm
to find the k-th smallest element in an unordered list

Example:
Input: A = [12, 4, 1, 9, 8, 5, 7]; k = 2
Output: 4
"""
def partition(arr, start, end):
	"""
	Partition an array around a pivot
	Would be best to have the pivot randomly chose
	"""
	pivot = arr[start]
	pivot_index = start
	while start < end:
		while start < len(arr) and arr[start] <= pivot:
			start += 1
		while arr[end] > pivot:
			end -= 1
		if start < end:
			arr[start], arr[end] = arr[end], arr[start]
	
	arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
	return end

def quick_select(arr, start, end, k):
	"""
	Quick select algorithm to select the k-th smallest number
	of an array
	"""
	# Base case
	if len(arr) == 1:
		return arr[0]

	while k > 0 and k <= len(arr) -1:
		# New index of k in the partitioned array
		index = partition(arr, start, end)

		if index - start == k - 1:
			return arr[index]

		# If position is more, recur for left subarray
		if (index - start > k - 1):
			return quick_select(arr, start, index - 1, k)

		# Else recur for right subarray
		return quick_select(arr, index + 1, end, k - index + start - 1)

arr = [12, 4, 1, 9, 8, 5, 7]
print(quick_select(arr, 0, len(arr) - 1, 2))