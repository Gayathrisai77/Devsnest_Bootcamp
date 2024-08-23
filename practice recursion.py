#1.program to calculate the sum of list of a numbers

# def my_list(num_list):
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         return num_list[0]+(my_list(num_list)[1:])
# x = my_list(2,4,5,6,7)
# print(x)






def my_function(n):
  if n==0:
    return 0
  else:
    return my_function(n-1)+n
n=int(input("enter the number:"))
answer=my_function(n)
print(answer)