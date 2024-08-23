# # RECURSION PROBLEMS

# # problem 1:
# write a recursive function to calculate the factorial of a number

# def factorial(n):
#   if n == 0 or n == 1:
#     return 1
#   else:
#     return n*factorial(n-1)
# n = 4
# result = factorial(n)
# print(result)

# # problem 2:
# # write a recursive function to generate nth fibonacci
# #number

# def fibonacci(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fibonacci(n-1)+fibonacci(n-2)
# n = 4
# result = fibonacci(n)
# print(result)

# # problem 4:
# # write a recursive function to reverse a string
# # def reverse_string(s):
# #   if len(s) == 0:
# #     return s
# #   else:
# #     return reverse_string(s[1:]) + s[0]
# # print(reverse_string(("devsnest")))
# # problem 5:
# write a recursive function to calculate the power of a number.
# def power(b,e):
#   if e != 0:
#     return b*power(b,e-1)   #5*(5,2-1)
#                             #5*(5,1) = 25
#   else:
#     return 1
# b = 5
# e = 3
# result = power(b,e)
# print(result)

# #problem 6:
# write a recursive funtion to check if a string is a palindrome.
# def ispalindrome(string):
#   if string == string[::-1]:
#     return "the string is palindrome"
#   else:
#     return "the string is not palindrome"
# string = "madam"
# print(ispalindrome(string))
# # problem 7:
# # write a recursive function to find the length of a string.
# # def lenstring(string):
# #   if string == "":
# #     return 0
# #   else:
# #     return 1 + lenstring(string[1:])
# # string = "python"
# # print(lenstring(string))
# # problem 8:
# # write a recursive function to print numbers from 1 to n in increasing order.
# # def printnumber(n):
# #   if n > 0:
# #     printnumber(n-1)
# #     print(n,end = "")        #doubt
# # n = 10
# # print(printnumber(n))
    
# # problem 9:
# # calculate th sum of all elements in an array using recursion.
# def sumarray(arr):
#   if not arr:
#     return 0
#   else:
#     return arr[0] + sumarray(arr[1:])
# arr = [1,2,3,4,5]
# result = sumarray(arr)
# print(result)
# # problem 10:
# # check if a given array is sorted in ascending order using recursion.
# def issorted(arr):
#   if arr == 0 or arr == 1:
#     return True
#   else:
#     return arr[0] < arr[1] and issorted(arr[1:])
# arr = [23,78,56,98,12,45,32,9]
# if issorted(arr):
#   print("yes")
# else:
#   print("no")
# result = issorted(arr)     #optional
# print(result)

# # problem 11:
# # find the maximum element in an array using.
# def maxelement(arr):
#   if len(arr) == 1:
#      return 1
#   else:
#     return max(arr[0],maxelement(arr[1:]))
# arr = [23,78,56,98,12,45,32,9]   #first element is compare to rest of the elements in array found two values and return the maximum value
# print(maxelement(arr))
# problem 12:
# # print the elements of an array in reverse order using recursion.
# def revarray(arr):
#   if len(arr) == 0:
#     return 0
#   else:
#     return arr[::-1]
# arr = [1,2,3,4,5,6,7]
# result = revarray(arr)
# print(result)
    
# # problem 13:
# # find the sum of even numbers in an array using recursion.
# def sumofeven(arr,i,sum):
#   if (i < 0):
#     return 0
#   else:
#     if arr[i] % 2 == 0:          #doubt
#       return arr[i] + sumofeven(arr[i-1])
# arr = [1,2,3,4,5,6,7,8,9]
# print(sumofeven(arr,i))

    

# # RECURSION PROBLEMS [MEDIUM PROBLEMS]


# # problem 1:
# # 1. write a recursive function to perform binary search on a sorted array.


# # problem 2:
# # 2. write a recursive function to find the GCD of two positive integers.
# # problem 3:
# # 3.write a recursion to find the sum of elements in an array.
# # problem 4:
# # 4. find the number of occurences of a digit in a given number using recursion.
# def count_occurences(number,digit):
#   if number == 0:
#     return 0
#   else:
#     if number % 10 == digit:
#       return 1 + count_occurences(number//10,digit)
#     else:
#       return count_occurences(number//10,digit)
# number =  12345674984
# digit = 4
# result = count_occurences(number,digit)
# print(result)
# # problem 5:
# # 5.calculate the nth fibonacci number using recursion.
# # problem 6:
# # 6.write a function to merge two sorted arrays into a single sorted array using recursion.
# def merge_sorted_arrays(arr1,arr2):
#   if not arr1 :
#     return arr2
#   else:
#     return arr1 + arr2.sort()    #doubt
# arr1 = [1,3,5,7]
# arr2 = [2,4,6,8]
# result = merge_sorted_arrays(arr1,arr2)
# print(result)

# # problem 7:
# # 7.Give a string.reverse the order of words.
# def reverse_words(string):
#   words = string.split()
#   reversed_words = words[::-1]
#   return " ".join(reversed_words)
# string = "hello world"
# result = reverse_words(string)
# print(result)
# # problem 8:
# # 8.write a recusive function to find the minimum and and maximum elements in an array.
# def min_max(arr):
#   if len(arr) == 1:
#     return arr[0],arr[0]
#   else:
#     min_val = min(arr)
#     max_val = max(arr)
#     return min_val,max_val
# arr = [1,2,3,4,5,6,7,8,9,10]
# result = min_max(arr)
# print(result)
# # prolem 9:
# # 9.find the power of a number using recursion.
# def power(b,e):
#   if e != 0:
#     return b*power(b,e-1)
#   else:
#     return 1
# b = 4
# e = 3
# result = power(b,e)
# print(result)
    
# # problem 10:
# # 10.check if given number is a power of 2 using recursion.
# def is_power_of_two(n):
#   if n == 0:
#      result0
#   else:
#     return n % 2 == 0 and is_power_of_two(n//2)
# n = 2
# result = is_power_of_two(n)       #doubt
# print(result)







    