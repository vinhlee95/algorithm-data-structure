# Array inversion
Input: an array A length `n`
There is an inversion at position `i` and `j` of `A` if:
`A[i] > A[j] && i < j`


## Brute force
- Running time: `O(n^n)` - loop within loop
```python
if n == 0 or n == 1:  # base case
	return 0

total_inv = 0
for i in range(0, A):
	for j in range(i+1, A):
		if A[i] > A[j]:
			total_inv += 1
			j+=1
			continue
		else:
			j+=1
	i+=1
```

## High level idea
```python
if n == 0 or n == 1:  # base case
	return 0
# If inversion happens in the first half of the array
left_inv = count_inversion(A[:n])
# If inversion happens in the second half of the array
right_inv = count_inversion(A[n:])
# If inversion happens in 2 sides of the array
split_inv = count_inversion(A)

return left_inv + right_inv + split_inv
```

## Combining with Merge Sort
```python
if n == 0 or n == 1:  # base case
	return 0
# If inversion happens in the first half of the array
L, left_inv = sort_and_count_inv(A[:n])
# If inversion happens in the second half of the array
R, right_inv = sort_and_count_inv(A[n:])
# If inversion happens in 2 sides of the array
split_inv = sort_and_count_inv(L+R)

return left_inv + right_inv + split_inv
```