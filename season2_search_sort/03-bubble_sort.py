def bubble_sort(input_array):
	n = len(input_array)

	for i in range(n):
		for j in range(0, n - i - 1):
			if input_array[j] > input_array[j+1]:
				input_array[j], input_array[j+1] = input_array[j+1], input_array[j]


arr = [64, 34, 25, 12, 22, 11, 90]
 
bubble_sort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 