# Problem & Solution

# Problem

Input: array A with `n` distinct numbers and a number `i in [1, 2, ..., n]`

Output: the `ith` - smallest element of A 

```python
Example: A = [1, 3, 5, 7]
If i = 2 → the output is 3. Because 3 is the 2nd smallest element of A
```

# Reduction to Sorting

`O(nlogn)` algorithm:

- Apply MergeSort to `A`
    - `B = MergeSort(A)`
- Return the `ith` element of *the sorted array*
    - `return B[i]`

# Randomised Selection

`RSelect(array A, length n, order statistics i)`

Order statistics: the `ith` smallest element of A

- Base case: `if n = 1 -> return A[0]`
- Choose pivot `p` from A, *uniformly at random*
- Partition A around pivot `p`
    - |  < p  |   p   |  >  p  |
    - let `j` = new index of `p`
- Luck: `if j = i -> return p`
- if j > i → `return RSelect(left part of A, j-1, i)`
- if j < i → `return RSelect(right part of A, n-j, i-j)`

## Properties of RSelect

**Running time**: depends on the *quality* of the chosen pivot

**Worst case**: $O(n^2)$ 

- Suppose `i = n/2`
- Suppose chose pivot = minimum *every time*

Key: find pivot giving *balance* split

Best pivot: **the median**

→ Would get recurrence `T(n) <= T(n/2) + O(n)`

→ `T(n) = O(n)` (case 2 of master method)