def count_split_inv(array, left, right):
	count = 0
	i = j = 0
	length = len(left) + len(right)
	# sentinal variable
	left.append(float('inf'))
	right.append(float('inf'))

	for k in range(length):
		if left[i] < right[j]:
			array[k] = left[i]
			i += 1
		else:
			array[k] = right[j]
			count += len(left) - 1 - i
			j += 1
	return count


def count_inversion(array):
	print('Count inversion', array)
	"""divide and conquer to count the inversion in an array"""
	if len(array) in [0, 1]:
		return 0
	
	mid = len(array) // 2
	left = array[:mid]
	right = array[mid:]

	a = count_inversion(left)
	b = count_inversion(right)
	c = count_split_inv(array, left, right)
	print(a, b, c)

	return a + b + c

my_arr = [1, 3, 5, 2, 4, 6]
print(count_inversion(my_arr))