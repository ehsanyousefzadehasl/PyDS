
def quick_sort(input_list):
   quick_sort_helper(input_list, 0, len(input_list) - 1)


def quick_sort_helper(input_list,first,last):
   if first < last:
       split_point = partition(input_list, first, last)
       quick_sort_helper(input_list, first, split_point - 1)
       quick_sort_helper(input_list, split_point + 1, last)


# this function returns the pivot element and changes elements position
# the returned pivot will determine other things and those are two subsets

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first + 1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark




alist = [54,26,93,17,77,31,44,55,20,1,100,200,21]
quick_sort(alist)
print(alist)