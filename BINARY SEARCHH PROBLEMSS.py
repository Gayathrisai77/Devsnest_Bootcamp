  #BINARY SEARCHH

def binary_search(l, low, high, s):
    if low <= high:
        mid = (low + high) // 2
        if l[mid] == s:
            print(s, "is found at position", mid + 1)
        elif l[mid] > s:
            return binary_search(l, low, mid - 1, s)
        else:
            return binary_search(l, mid + 1, high, s)
    else:
        print(s, "is not found")

l = []
n = int(input("Enter the number of elements to be inserted: "))
print("Enter", n, "number of elements")
for i in range(n):
    l.append(int(input()))
l.sort()
print("After sorting:")
print(l)
low = 0
high = len(l)-1
mid = (low+high)//2
s= int(input("Enter the search element: "))
binary_search(l,low,high,s)



#SEARCH IN  ROTATED SORTED ARRAY
# nums = [4,5,6,7,0,1,2]
# target = 0
def rotated_sorted_array(nums,target):
  left = 0
  right =len(nums)-1
  while left<=right:
    mid = (left+right)//2
    if nums[mid] == target:
      return mid
    if nums[left]<=target<nums[mid]:
         right = mid-1
    else:
          left = mid+1
    if nums[mid]<target<=nums[right]:
        left = mid-1
    else:
          right = mid+1
  return -1
nums = [4,5,6,7,0,1,2]
target = 0
print(rotated_sorted_array(nums,target))




#MINIMUM ELEMENT IN ROTATED ARRAY

def find_minimum(nums):
    left = 0
    right = len(nums)-1
    
    while left<right:
        mid = (left+right)//2
        if nums[mid]> nums[right]:
            left = mid+1
        else:
            right = mid
    return nums[left]
nums = [2,4,3,1,4,5,6,8,0]
print(find_minimum(nums))
      
#FIND A PEAK ELEMENT
def peakelement(nums):
    left = 0
    right = len(nums)-1
    
    while left<right:
        mid = (left+right)//2
        if nums[mid] > nums[right]:
            right = mid
        else:
            left = mid+1
    return left
nums = [1,4,5,2,7,8,3]
print(peakelement(nums))



#SQUARE ROOT OF A NUMBER USING BINARY SEARCHHH
def square_rootof(num,precision=0.00000000000000001):
    if num < 0:
        return None
    if num == 0 or num == 1:
        return num
    low = 0
    high = num
    
    while True:
        guess = (low+high)/2
        square = guess*guess
        if abs(square-num)<precision:
            return guess
        if square > num:
            high = guess
        else:
            low = guess
num = 49
print(square_rootof(num))
          
##########find the target using binary search  in sorted array ###############
def binarysearch(arr,target):
    low = 0
    high = len(arr)-1
    while low<=high:
      mid = (low+high)//2
      if arr[mid]==target:
        return mid
      elif arr[mid]<target:
        low = mid+1
      else:
        high = mid-1
    return -1
arr = [1,2,3,4,5,6,7,8,9,10]
target = 9
print(binarysearch(arr,target))

