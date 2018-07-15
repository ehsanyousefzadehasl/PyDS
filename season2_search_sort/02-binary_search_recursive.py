def binary_search(input_array, low, high, value):

	if low < high:
		mid = low + (high - 1)//2

		if input_array[mid] == value:
			return mid
		elif input_array[mid] < value:		
			return binary_search(input_array, mid+1, high, value)
		elif input_array[mid] > value:
			return binary_search(input_array, low, mid-1, value)
		
	return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, 0, len(test_list) - 1, test_val1))
print(binary_search(test_list, 0, len(test_list) - 1, test_val2))