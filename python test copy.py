#find the number of occurences of a digit in a given number using recursion.
# def count_occurences(n,digit):
#   if n==0:
#     return 0
#   if n%10==digit:
#     return 1 + count_occurences(n//10,digit)
#   else:
#     return count_occurences(n//10,digit)
# n = 1234567776
# digit = 7
# print(count_occurences(n,digit))


#sort an array of integers using inserstion sort
# def insertion_sort(arr,reverse):
#   for i in range(1,len(arr)):
#     key = arr[i]
#     j = i-1
#     while j>=0 and key<arr[j]:
#       arr[j+1] = arr[j]
#       j-=1
#     arr[j+1] = key
#   return arr
# arr = [5,2,4,6,1,3]
# result = insertion_sort(arr,reverse=True)
# print(result)

# peak element in binary search
# def peakelement(nums):
#   left = 0
#   right = len(nums)-1

#   while left<right:
#     mid = (left+right)//2
#     if nums[mid]>nums[right]:
#       right = mid
#     else:
#       left = mid+1
#   return left
# nums = [1,2,3,4,5]
# print(peakelement(nums))
# find the peak element and return its index..
# def peak_element(nums,target):
#   left= 0
#   right = len(nums)-1
#   while left<right:
#     mid = (left+right)//2
#     if nums[mid]==target:
#       return mid
#     elif nums[mid]<target:
#          low = mid+1
#     else:
#       left = mid-1
#   return -1
# nums = [1,2,3,4]
# target = 2
# print(peak_element(nums,target))



