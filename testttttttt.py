 #Input: prices = [1,2,3,4,5]
# Output: 4
# def maxprofit(prices):
#     l = 0
#     r = 1
#     max_profit = 0
#     while r < len(prices):
#         if prices[l] < prices[r]:
#             profit = prices[r]-prices[l]
#             max_profit = max(profit,max_profit)
#         else:
#             l += 1
#         r += 1
#     return max_profit
# prices = [1,2,3,4,5]
# print(maxprofit(prices))


###### removing all occurences and print remaining values #####
# def removingvalue(array,value):
#     new_array = []
#     final_count = 0
#     for n in array:
#         if n != value:
#             new_array.append(n)
#             final_count += 1
#             array[:] = new_array
#     return new_array

# array = [3,2,2,3]
# value = 3
# print(removingvalue(array,value))
#print(array)

##########reverse a string ####
# def reverses(string):
#     new_string = ""
#     for i in string:
#         new_string = i + new_string
#     return new_string
# string = "h","e","l","l","o"
# print(reverses(string))

# 2)Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
