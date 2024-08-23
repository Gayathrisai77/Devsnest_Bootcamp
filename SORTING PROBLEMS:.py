def bubble_sort(arr):
   n = len(arr)
   for i in range(n):
       for j in range(0,n-i-1):
           if arr[j] > arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
arr = [64,34,25,12,22,11]
print(bubble_sort(arr))

# sorting in ascending order

numbers = [12,3,4,46,98,12]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# sorting in descending order
numbers = [2,5,3,7,8,1,90,7,3]
sorted_numbers = sorted(numbers,reverse = True)
print(sorted_numbers)
#SELECTION SORT
def selection_sort(array):
    for pos in range(len(array)-1):
        min = pos
        for i in range(pos+1,len(array)):
            if array[i] < array[min]:
                min = i
        array[pos],array[min]=array[min],array[pos]
        return array
array = [2,3,1,4,5,6,23,12]
print(selection_sort(array))
