################## NEXT PERUMATATAION #################################
def next_perumation(array):
    n = len(array)
    x = n-2 #second last element
    
    while x>0:
        if array[x] < array[x+1]:
            break
        x -= 1
    if x<0:
        array.reverse()
    else:
        l = n-1
        while l > x:
          if array[l] > array[x]:
            break
          l -= 1
    array[l],array[x] = array[x],array[l]
    array[x+1:] = array[x+1:][::-1]
    return array
    
array = [1,2,3]
print(next_perumation(array))
#--------------------------------------------------------------------------------------

###################### MAXIMUM SUBARRAYS SUM #############################
def max_subarray(array):
    max_sum = array[0]
    curr_sum = 0
    for i in array:
        curr_sum += i
        if max_sum < curr_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum
    
array = [1,2,3]
print(max_subarray(array))

#--------------------------------------------------------------------------------------

######################### LONGEST CONSEQUENCE ###########################

def longestconsequence(nums):
    numset = set(nums)
    for n in nums:
        if (n-1) not in numset:
            length = 0
            while (n+length) in numset:
                length += 1
    return length
    
nums = [0,3,8,9,1,4,2,5,6,7]
print(longestconsequence(nums))

#--------------------------------------------------------------------------------------
##################LARGEST SUM CONSEUTIVE SUBARRAY(KADANE'S ALOGIRITHM)#################

nums = [-2,-3,4,-1,-2,1,5,-3]
global_sum = nums[0]
curr_sum = nums[0]
for n in nums[1:]:
    curr_sum = max(n,curr_sum+n)
    global_sum = max(curr_sum,global_sum)
print(global_sum)

#--------------------------------------------------------------------------------------
################# REMOVE THE ELEMENTS FROM THE ARRAY ##################################
#problem 1:
    
def removing_elements(array,value):
    final_count = 0
    for n in array:
        if n != value:
            final_count += 1
    return final_count
    
array = [2,3,3,5,2,7]
value = 2
print(removing_elements(array,value))

#example 2:
    
def removing_elements(array,value):
    final_count = 0
    new_array = []
    for n in array:
        if n!= value:
            new_array.append(n)
            final_count += 1
    array[:] = new_array #updating newarray to previous array
    return final_count
array = [9,4,5,7,2,2,4,1,2]
print(removing_elements(array,value))
print(array)

#--------------------------------------------------------------------------------------
############## TWO SUM #########################
#Example 1:
def two_sum(nums,target):
    num_to_index = {} #using hashmap to store elements with index
    for i,num in enumerate(nums):  #enumerate for both element and index
        complement = target - num
        if complement in num_to_index:
           return [num_to_index[complement],i]  #gives us the indices of the two numbers that add up to target.
        num_to_index[num] = i        #otherwise add num to num_to_index with its index
    return [] # if no pair is found return []
    
nums = [2,3,1,6,0]
target = 10
print(two_sum(nums,target))
#----------------------------------------------------------------------------------------

#Example 2:
def two_sum(nums,target):
    num_to_index = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement],i]
        num_to_index[num] = i
    return []
    
nums = [2,5,1,8,9]
target = 10
print(two_sum(nums,target))
       
#------------------------------------------------------------------------------------------------------
#########CONTAINER WITH MOST WATER ############################

def solve(n, arr):
    l = 0
    r = len(arr)-1
    max_water = 0
    while l<=r:
        current_water = min(arr[l],arr[r])*(r-l)
        if current_water > max_water:
            max_water = current_water
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return max_water

arr = [1,8,6,2,5,4,8,3,7]
n = 9
print(solve(n,arr))

#----------------------------------------------------------------------------------------



















    
    
    
    
    
    
    
    
    

            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
