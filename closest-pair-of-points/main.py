# A divide and conquer program in Python3
# to find the smallest distance from a
# given set of points.
import math
import copy
# A class to represent a Point in 2D plane
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

# A utility function to find the
# distance between two points
def dist(p1, p2):
	return math.sqrt((p1.x - p2.x) *
					(p1.x - p2.x) +
					(p1.y - p2.y) *
					(p1.y - p2.y))

# A Brute Force method to return the
# smallest distance between two points
# in P[] of size n
def brute_force(P, n):
	min_val = float('inf')
	for i in range(n):
		for j in range(i + 1, n):
			if dist(P[i], P[j]) < min_val:
				min_val = dist(P[i], P[j])

	return min_val

def strip_closest(strip, size, d):
	"""
	A utility function to find the distance beween the closest points of strip of given size. 
	All points in strip[] are sorted according to y coordinate. 
	They all have an upper bound on minimum distance as d.
	Note that this method seems to be a O(n^2) method, but it's a O(n) method as the inner loop runs at most 6 times
	"""
	# Initialize the minimum distance as d
	min_val = d
	
	# Pick all points one by one and
	# try the next points till the difference
	# between y coordinates is smaller than d.
	# This is a proven fact that this loop
	# runs at most 6 times
	for i in range(size):
		j = i + 1
		while j < size and (strip[j].y -
							strip[i].y) < min_val:
			min_val = dist(strip[i], strip[j])
			j += 1

	return min_val


def closest_until(P, Q, n):
	"""
	A recursive function to find the
	smallest distance

	:param P the original list containing all points, sorted by x coordinate
	:param Q a deep copy of P, sorted by y coordinate
	"""
	# If there are 2 or 3 points,
	# then use brute force
	if n <= 3:
		return brute_force(P, n)

	# Find the middle point
	mid = n // 2
	midPoint = P[mid]

	# Left and Right half of the original list
	L = P[:mid]
	R = P[mid:]

	# Find the closest distance in left half and right half
	d = min(closest_until(L, Q, mid), closest_until(R, Q, n - mid))

	# Find Cross-middleline pairs
	# Build an array strip[] that contains points close (closer than d)
	# to the line passing through the middle point
	stripP = []
	stripQ = []

	for i in range(n):
		if abs(P[i].x - midPoint.x) < d:
			stripP.append(P[i])
		if abs(Q[i].x - midPoint.x) < d:
			stripQ.append(Q[i])

	stripP.sort(key = lambda point: point.y) #<-- REQUIRED
	print("stripP", stripP)
	print("stripQ", stripQ)
	min_a = min(d, strip_closest(stripP, len(stripP), d))
	print("min_a", min_a)
	min_b = min(d, strip_closest(stripQ, len(stripQ), d))
	print("min_b", min_b)	
	
	# Find the self.closest points in strip.
	# Return the minimum of d and self.closest
	# distance is strip[]
	return min(min_a, min_b)

def closest(P):
	"""
	The main function that finds
	the smallest distance.
	This method mainly uses closest_until()

	:param P the input array containing all points
	"""
	# Px sorted by x coordinates
	P.sort(key = lambda point: point.x)
	# Py sorted by y coordinates
	Q = copy.deepcopy(P)
	Q.sort(key = lambda point: point.y)

	return closest_until(P, Q, len(P))

# Driver code
P = [Point(2, 3), Point(12, 30),
	Point(40, 50), Point(5, 1),
	Point(12, 10), Point(3, 4)]
print("The smallest distance is", closest(P))

