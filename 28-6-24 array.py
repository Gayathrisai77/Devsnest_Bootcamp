############## REMOVING DUPLICATES FROM AN ARRAY ##############################

def removing_duplicates(array):
    new_array = []
    seen = set()
    for item in array:
        if item not in seen:
           seen.add(item)     #in set we have to use add not append
           new_array.append(item)
    return sorted(new_array)  #it will sortout the array
    
array = [1,1,2,7,5,9,9,7]
print(removing_duplicates(array))
#seen.add(item): This line adds the current item to the seen set if it hasn't been encountered before. This ensures that duplicates are identified and not added to new_array again.
#----------------------------------------------------------------------------------------
#############REMOVE DUPLICATES FROM AN SORTED ARRAY ######################
def remove_duplicates_sorted(sorted_array):
    if not sorted_array:
        return []
    unique_index = 0 #first value in array(1)
    for i in range(1,len(sorted_array)):
        if sorted_array[i] != sorted_array[unique_index]: # 1 !=  1 not true
           unique_index += 1
           sorted_array[unique_index] = sorted_array[i]
    return sorted_array[:unique_index+1]
    
sorted_array = [1,1,2,3,3,4,5,5,5,5,6,7]
print(remove_duplicates_sorted(sorted_array))

#----------------------------------------------------------------------------------------
########### SEARCH INSERT POSITION ##########################
def search_position(nums):
    new_array = []
    while nums:
        for i,num in enumerate(nums):
            if num == target:
                new_array.append(i)
        return new_array
nums = [1,3,5,6]
target = 5                                        #time complexity = o(n)
print(search_position(nums))
## SEARCH INSERT POSITION:
def insertposition(nums,target):
    while nums:
     for i,num in enumerate (nums):
        if num >= target:
            return i
    return len(nums)
            
nums = [1,3,5,6]
target = 4
print(insertposition(nums,target))
#time complexity :o(n)
#========================================================================================
# With timecomplexity O(logn):
def insertposition(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left+(right-left)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return left
nums = [1,3,5,6]
target = 4
print(insertposition(nums,target))
#----------------------------------------------------------------------------------------
######### SEARCH Insert POSITION in sorted array #################
def insert_position(nums,target):
    left = 0
    right = len(nums)-1
    
    while left <= right:
        mid = left+(right-left)//2
        if  nums[mid] == target:
            return mid
        elif nums[mid] < target:
           left = mid+1
        elif nums[mid] > target:
           right = mid-1
        else:
            print("target is not in nums")
            
nums = [1,4,5,6]
target = 5                                               #time complexity = o(logn)
print(insert_position(nums,target))

