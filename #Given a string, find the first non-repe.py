#Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
# def my_string(string):
#   for i in string:
#     if string.count(i) == 1:
#       return string.index(i)
#     else:
#       return -1
# string = "hellohello"
# print(my_string(string))

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# my_list = [2,0,2,1,1,0]
# n = len(my_list)
# for i in range(n-1):
#   for j in range(n-i-1):
#     if my_list[j] > my_list[j+1]:
#       my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
# print(my_list)

# 3.Write a recursive function to find the sum of digits of a positive integer.
# def my_sum(n):
#   if n == 0:
#     return 0
#   else:
#     return n%10 + my_sum(n//10)
# n = int(input())
# print(my_sum(n))


def binary_search(l,s,low,high,mid):
    if low<= high:
      mid = (low+high)//2
      if l[mid] == s:
        print(s,"is found at",mid)
      elif l[mid] > s:
        binary_search(l,s,low,mid-1,mid)
      else:
        binary_search(l,s,mid+1,high,mid)
    else:
      print(s, "is not found")
l = list()
n = int(input("enter the number of elements"))
print(n, "enter the elements")
for i in range(n):
 l.append(int(input()))
l.sort()
print("sorting elements")
print(l)
s = int(input("enter the searching element"))
low = 0
high = n-1
mid = 0
binary_search(l,s,0,n-1,0)

# 4.Write a recursive function to find the GCD of two numbers.

  

        
















