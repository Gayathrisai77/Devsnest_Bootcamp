# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
def removingallocuurences(nums,value):
    final_count = 0
    new_array = []
    
    for i in range(len(nums)):
        if nums[i]!= value:
            new_array.append(nums[i])
            final_count += 1
        else:
           nums[i]  = "_"
    #return final_count
       
    return new_array
nums = [3,2,2,3]
value = 3
print(removingallocuurences(nums,value))
print(nums)

#----------------------------------------------------------------------------------------------------------------------------------
############# Maxmium profit buying and selling #######
# Example 1:
# Input: prices = [1,2,3,4,5]
# Output: 4
def maxprofit(prices):
    l = 0
    r = 1
    max_profit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit,profit)
        else:
            l += 1
        r += 1
            
    return max_profit
prices = [1,2,3,4,5]
print(maxprofit(prices))

#------------------------------------------------------------------------------------------------------------------------------------------


    
