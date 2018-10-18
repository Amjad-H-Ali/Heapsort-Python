print("Heapsort!")

# Function to create Max-Heap
# Meaning, the parent node is larger than its children.
# Takes three Params: array, array indx, and array size
def heapify (array, i, size):
	# Assume largest element is the parent node; Initialize largest var to parent indx.
	largest = i

	# Left child node indx.
	l = (i * 2) + 1

	# Right child node indx.
	r = (i * 2) + 2

	# Reinitialize largest var to left child indx if element larger; Make sure indx falls in array first.
	if (l < size and array[l] > array[largest]):
		largest = l

	# Reinitialize largest var to right child indx if element larger; Make sure indx falls in array first.
	if (r < size and array[r] > array[largest]):
		largest = r

	# If largest element was not the parent, then swap elements and use recursion to repeat the whole process.
	if (largest != i):
		swap(array, array[largest], array[i])

		heapify(array, largest, size)

# Simple Swap function
# Swaps given elements in array when called
def swap (array, indx1, indx2):
	temp = array[indx1]
	array[indx1] = array[indx2]
	array[indx2] = temp

# Function that sorts array using the heapify function defined above.
# Takes in one Param: an array to be sorted.
def heapSort (array):
	# Array length
	size = len(array)

	# Loop through each parent node and Max-Heapify
	for indx in range((int(size/2)) - 1, -1, -1):
		heapify(array, indx, size)
	

