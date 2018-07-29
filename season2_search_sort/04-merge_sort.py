def merge_sort(input_list):

   print("splitting -> ",input_list)

   if len(input_list) > 1:
       mid = len(input_list)//2
       left_half = input_list[:mid]
       right_half = input_list[mid:]

       # recursion
       merge_sort(left_half)
       merge_sort(right_half)


       # merging occurs here
       i=0
       j=0
       k=0

       while i < len(left_half) and j < len(right_half):
           if left_half[i] < right_half[j]:
               input_list[k]=left_half[i]
               i=i+1
           else:
               input_list[k]=right_half[j]
               j=j+1
           k=k+1

       while i < len(left_half):
           input_list[k]=left_half[i]
           i=i+1
           k=k+1

       while j < len(right_half):
           input_list[k]=right_half[j]
           j=j+1
           k=k+1

   print("Merging ",input_list)



in_list = [54,26,93,17,77,31,44,55,20]
merge_sort(in_list)
print(in_list)