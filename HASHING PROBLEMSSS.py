   #3.Given an array of integers, return indices of the two numbers such that they add up to a   specific target.
# def findtarget(nums,target):
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return "pair found:",(nums[i],nums[j])
            
# nums = [2,3,5,1,6,7,1,]
# target = 8
# print(findtarget(nums,target))

#Find longest subsequence formed by consecutive integers::

def findmaxsubseq(A):
    s = set(A)
    maxlength = 0
    
    for e in s:
        if (e-1) not in s:
            len = 1
            while(e+len) in s:
                len += 1
            maxlength = max(maxlength,len)
            
    return maxlength
A =[100,1,4,2,5,200,3,7,6]
print(findmaxsubseq(A))
#longest consective subsequence:
# def longcon(A):
#     s = set(A)
#     maxlength = 0
#     for e in A:
#         if (e-1) not in s:
#             len = 1
#         while (e+len) in s:
#             len += 1
#             maxlength = max(maxlength,len)
#         return maxlength
# A = [1,7,2,9,3,4,199,19]
# print(longcon(A))
# Write a function to rearrange an array such that all negative elements appear before all
# positive elements.
# def rearrange_array(arr):
#     negative_elements = [num for num in arr if num < 0]
#     positive_elements = [num for num in arr if num >= 0]
#     return negative_elements+positive_elements
# arr = [-1,-2,5,7,-3,8,3,-9]
# print(rearrange_array(arr))
# Returns the total number of distinct absolute values in a given input::
def finddistinct(nums):
    s = set([abs(i)for i in nums])
    return len(s)
nums =[-1,-1,-2,-2,6]   #-1 =1 and -2 absolute value of= 2
print(finddistinct(nums))
# Create a hash map to store the frequency of characters..
def char_frequency(s):
    frequency_map = {}
    for char in s:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1
    return frequency_map
s = "helloworld"
frequency_map = char_frequency(s)
for char,frequency in frequency_map.items():
    print(f"'{char}': {frequency}")
# Here is a Python function to find the first non-repeated character in a string and return its index:
# def non_repeated(s):
#     char_count = {}
#     for char in string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1              
#     for index, char in enumerate(string):
#         if char_count[char] == 1:
#             return index
#     return -1
# string = "leetcodel"
# index = non_repeated(string)
# print("index of the first non-repeated:",index)












































