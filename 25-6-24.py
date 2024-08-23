###############problem on array #####################


# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4
## example 1:
# def maxprofit(prices):
#     max_profit = 0
#     for i in range(1,len(prices)):
#         if prices[i] > prices[i-1]:
#             max_profit += prices[i] - prices[i-1]
#     return max_profit
        
# prices = [7,1,5,3,6,4]
# print(maxprofit(prices))


## example 2:
# def maxprofit(prices):
#     max_profit = 0
#     for i in range(1,len(prices)):
#         if prices[i] > prices[i-1]:
#             max_profit += prices[i] - prices[i-1]
#     return max_profit
    
# prices = [1,2,3,4,5]
# print(maxprofit(prices))
#---------------------------------------------------------------------------------------
def maxprofit(prices):
    l = 0
    r = 1
    max_profit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r]-prices[l]
            max_profit = max(max_profit,profit)
        else:
            l += 1
        r += 1
    return max_profit
    
prices = [7,1,5,3,6,4]
print(maxprofit(prices))
#---------------------------------------------------------------------------------------
#===============Loss==========================================
#example 1:
def minprofit(prices):
    min_profit = 0
    for i in range(1,len(prices)):
        if prices[i] < prices[i-1]:
            min_profit += prices[i] - prices[i-1]
    return min_profit
    
prices = [1,2,3,4,5]
print(minprofit(prices))

#--------------------------------------------------------------------------------------
#example 2:
def loss(prices):
    min_profit = 0
    for i in range(1,len(prices)):
        if prices[i] < prices[i-1]:
          min_profit += prices[i] - prices[i-1]
    return min_profit
    
prices = [7,1,5,3,6,4]
print(loss(prices))

#-------------------------------------------------------------------------------------
        
    
    
    
    
    
    
    
    
    
    
    
    






















