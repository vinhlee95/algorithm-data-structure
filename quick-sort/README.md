# Quick Sort

Works in-place → minimal extra memory needed

Running time: `O(nlogn)`

# Problem

```python
Input: 2, 4, 1, 0
Output: 0, 1, 2, 4
```

# Key idea

Partition array around a **pivot element**

Re-arrange (Partition) the array so that:

- Left of pivot → less than pivot
- Right of pivot → greater than pivot

# Steps

- Pick a pivot element
- Rearrange the array based on chosen pivot element
    - Left of pivot → less than pivot
    - Right of pivot → greater than pivot
- Get the index where the partition is done. This index will be used to divide the array into 2
- Recursively call quick sort function for 2 half of the array divided by the index

# Code

## Partition

```python
def partition(arr, start, end):
	pivot = arr[start]
	pivot_index = start

	while start < end:
		while start < len(arr) and arr[start] < pivot:
			start += 1
		while arr[end] > pivot:
			end += 1
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
```

## Quick sort

```python
def quick_sort(arr, start, end):
	if start < end:
		partition_index = partition(arr, start, end)
		quick_sort(arr, start, partition_index - 1)
		quick_sort(arr, partition_index + 1, end)
```
