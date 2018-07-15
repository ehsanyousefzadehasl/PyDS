def binary_search(input_array, value):
	low = 0
	high = len(input_array) - 1

	while low < high:
		mid = low + (high - 1)//2

		if input_array[mid] == value:
			return mid
		elif input_array[mid] > value:		
			high = mid - 1
		elif input_array[mid] < value:
			low = mid + 1
		
	return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))