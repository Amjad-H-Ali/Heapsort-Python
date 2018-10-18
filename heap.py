print("Heapsort!")

# Function to create Max-Heap
# Takes three Params: array, array indx, and array size
def heapify (array, i, size):
	# Assume largest element is the parent node; Initialize largest var to parent indx.
	largest = i

	# Left child node indx.
	l = (i * 2) + 1

	# Right child node indx.
	r = (i * 2) + 2

	# Reinitialize largest var to left child indx if element larger; Make sure indx falls in array first.
	if (l > size and array[l] > array[largest]):
		largest = l
