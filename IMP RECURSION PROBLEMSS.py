         #RECURSIONN
# write a recursive function to generate nth fibonacci
#number
# def fibonacci(n):
#     if n== 0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+(n-2)
# n=3
# for i in range(0,10):
#  result = (i,fibonacci(n))
# print(result)

#program to calculate sum of numbers using recursion
# def my_list(n):
#     if n==0:
#         return 0
#     else:
#         return my_list(n-1)+n
# n = 10
# print(my_list(n))

# write a recusive function to calculate the length of a factorial number.
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n = 7
# print(factorial(n))

#find the length of the string using string
# def length(str):
#     if str == "":
#         return 0
#     else:
#         return 1+length(str[1:])
# str = "hiihello"
# print(length(str))

#vowels counting in recursion
# def vowel_count(string):
#     if not string:
#         return 1
#     if string[0].lower() in "aeiou":
#         return 1+vowel_count(string[1:])
#     else:
#         return vowel_count(string[1:])
# string = "hii baby iam jungkook"
# print(vowel_count(string))

# 1.Given a string containing digits from 2-9 representing a phone number mapping to letters (as in the telephone keypad), return all possible letter combinations that the number could represent. Return the answer in any order.

# Input: digits = "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# def lettercombination(digits):
#     if not digits:
#         return []
#     mapping = {
#         "2" : "abc",
#         "3" : "def",
#         "4" : "ghi",
#         "5" :  "jkl",
#         "6" : "mno",
#         "7" : "pqrs",
#         "8" : "tuv",
#         "9" : "wxyz",
#     }
#     def backtrack(combination,next_digits):
#         if len(next_digits)==0:
#             result.append(combination)
#         else:
#             for letter in mapping[next_digits[0]]:
#                 backtrack(combination+letter,next_digits[1:])
#     result = []
#     backtrack("",digits)
#     return result
# digits ="72"
# print(lettercombination(digits))
# 2.Given an array of distinct integers nums, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example:
# Input: nums = [1,2,3]

# def subsets(nums):
#     def backtrack(start, path):  # current= path
#         res.append(path[:])
#         for i in range(start, len(nums)):
#             path.append(nums[i])
#             backtrack(i + 1, path)
#             path.pop()

#     res = []
#     backtrack(0, [])
#     return res

# nums = [1, 2, 3]
# print(subsets(nums))
#6.Write a recursive function to count the number of digits in a positiveinteger..
# def count_digits(n):
#     if n < 10:
#         return 1
#     else:
#         return 1+ count_digits(n//10)
# n =678902-20
# print(count_digits(n))


# .Implement a recursive function to determine if a given string is a palindrome. The function should ignore spaces and punctuation and should return True if the string is a palindrome, otherwise False.
# def is_palindrome(s):
    #base case:if the string is empty or has only one character,it is pallindrome  after recursing entire sentence it goes to basecase which return true when there is nothing to comparee all are becoming true
#     if len(s) <= 1:
#         return True
#     if s[0].isalnum() and s[-1].isalnum():
#         if s[0].lower() == s[-1].lower():
#             return is_palindrome(s[1:-1])
#         else:
#             return False
#     elif not s[0].isalnum():
#         return is_palindrome(s[1:])
#     elif not s[-1].isalnum():
#         return is_palindrome(s[:-1])

# print(is_palindrome("a man,a plan,a canal,panama"))
#3.Write a recursive function to find the sum of digits of a positive integer.
# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n%10+ sum_of_digits(n//10)
# n = 12345-8
# print(sum_of_digits(n))
#8.Implement a recursive function to merge two sorted arrays into a single sorted array.
# def merge_sorted_arrays(arr1,arr2):
#     if not arr1:
#         return arr2
#     elif not arr2:
#         return arr1
#     elif arr1[0] < arr2[0] :
#         return [arr1[0]]+merge_sorted_arrays(arr1[1:],arr2)
#     else:
#         return [arr2[0]]+merge_sorted_arrays(arr1,arr2[1:])
        
# arr1 = [1,2,7,9,10]
# arr2 = [3,5,7,9,11]
# print(merge_sorted_arrays(arr1,arr2))
# 10.Write a recursive function to find the length of the longest substring with at most k distinct characters in a string




#9.Implement a recursive function to generate all subsets of a set.
# 4.Write a recursive function to find the GCD of two numbers.
# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# a = 48
# b = 18
# print(gcd(a,b))

#  tower of hanoi using recursion
# def tower_of_hanoi(n,source,destination,auxiliary):
#     if n==1:
#         print("move disk 1 from",source,"to",destination)
#         return 
#     tower_of_hanoi(n-1,source,auxiliary,destination)
#     print("move disk", n ,"from",source,"to",destination)
#     tower_of_hanoi(n-1,auxiliary,destination,source)
    
# n = 3
# tower_of_hanoi(n,"a","e","t")








































































    


    
    
    
    
    
    
    
    
    
    
    
    
    




























