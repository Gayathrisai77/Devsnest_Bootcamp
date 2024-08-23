# #### Time complexity ###### 
# # problem 1:
# # a = 0                       #O(1)
# # b = 0                       #o(1)
# # for i in range(N):          0(n)
# #   a = a + random()      

# # for i in range(M):          0(m)
# #   b = b + random()       

# ans = O(m+n)
#       order(n)+order(m) = o(m+n)
# ----------------------------------------------------------------------------------------      
# When analyzing nested loops where the inner loop's iterations depend on the current iteration of the outer loop, you multiply the number of iterations of each loop to determine the overall time complexity.
# like this,  
# for i in range(N):
#     for j in range(i):
#         # Constant time operations
# -----------------------------------------------------------------------------------------
# problem 2:
# a = 0
# for i in range(N):    
#   for j in reversed(range(i, N)):   #j = i
#  a = a + i + j 
 
# explanation:
# i = 0 to n-1 so it iterates n times
# i = n-1 to 0,n times & i =1 from n-1 to 1,n-1 times & i=2from n-1 to 2,n-2 iterations it will go unti n-1 to n-1 which is (1)

# N + (N – 1) + (N – 2) + … 1 + 0 
# = N * (N + 1) / 2 
# = 1/2 * N^2 + 1/2 * N 
# output:
# O(N^2) times.
#     a = a + i + j 
# ----------------------------------------------------------------------------------------
# problem 3:
    
# k = 0
# for i in range(n//2, n):
#   for j in range(2, n, pow(2, j)):
#     k = k + n / 2
# explanation:
#     the outer loop iterates from n/2 to n-1 times,n/2 iterations (2).the inner loop runs from j=2 to j<n with increemnt of j with exponential 2 so it beacomes 2j<n applying log with base 2 on both sides which will come as log 2j and log2n
#     by logarithms log(2j) becomes j. and it would be j<log2n (3).now we have n/2 * log2n
#     by dropping constants we wil have output as 0(nlogn)
    
# output:
#     0(n log n)
    
# ----------------------------------------------------------------------------------------
# *******algorithm X is asymptotically more efficient than Y?.*************************
#  X will always be a better choice for large inputs..
#  Explanation: In asymptotic analysis, we consider the growth of the algorithm in terms of input size. An algorithm X is said to be asymptotically better than Y if X takes smaller time than y for all input sizes n larger than a value n0 where n0 > 0.

#  ---------------------------------------------------------------------------------------
# problem 4:
# a = 0
# i = N
# while (i > 0):
#   a += i
#   i //= 2
  
# explanation:
#     i = n and loop has to iterate i>0.withi//2 so after 1 iteration it becomes n/2 and after 2nd iteration it becomes n/4 upto k times n/2power k.the will will stop i<= 0 so i.e n/2power k <= 0 by applying logarithms on both sides we get 0(log )
# ---------------------------------------------------------------------------------------
# the alogarithm which takes less time will occupy less memory or less space also both are imp for to find efficiency of an alogarithm.
# --------------------------------------------------------------------------------------
# problem 5:
# for i in range(n):
#   i=i*k
#  explanation:
#      i = 0 to i = n-1 times so it will take O(n ) times i - i*k take O(1) times.
     
# output:
#     O(n)
# ---------------------------------------------------------------------------------------
# problem 6:
# value = 0;
# for i in range(n):
#   for j in range(i):
#     value=value+1
# explanation:
#     for outer loop from i=0 to n-1,n times and inner loop j=0 to j = i-1 times becoz of value = value+1. we have add each and every element of i 1=2+....+(n-1).sum of first natural numbers is n(n-1)/2.from two loops n(n-1)/2.we take higher quadratic.
    
# output:
#     O(npower of 2)
# --------------------------------------------------------------------------------------
# problem 7:
#     for i in range(n):
#     print(i)
# explanation:
#     for for loop it iterates from 0 to n-1,n timesfor printo(1)
# output:
#     o(n)
# ---------------------------------------------------------------------------------------
# problem 8:
#     for i in range(n):
#     for j in range(n):
#         print(i, j)
# exp:
#     the outer loop iterate o(n) times where inner loop runs each iteration of outerloop o(n).
# output:
#     O(n power 2)
# ---------------------------------------------------------------------------------------
# problem 9:
#     for i in range(n):
#     for j in range(i, n):
#         print(i, j)
# ex:
#     for outer loop O(n).the inner loops runs from n-i times to n-i times.(n−0)+(n−1)+(n−2)+…+(n−(n−1))..This simplifies to:n+(n-1)+(n-2)+......+1.first n natural numbers n(n+1)/2.
    
# ---------------------------------------------------------------------------------------
# problem 10:
#     i = 1
# while i < n:
#     print(i)
#     i = i * 2
# expl:
#     the no.of iteration k can be by solving 2k >= n which is k log base2 n.
# output:
#     O(log n)
# ---------------------------------------------------------------------------------------



#============================== 25-6-24 ============================================#
#########################################################################################
# problem 1:
#     def fun(n,m):
#     for i in range(n):   #O(n)
#         print(i)
#     for i in range(m):    #0(m)
#         print(i)
# output:
#     O(m+n)
# ----------------------------------------------------------------------------------------
# problem 2:
#     import random     #o(1)
# def fun(N):
#     counter=0          #o(1)
#     for i in range(N):        #O(n)
#         counter+=random.randint(1,100)  #o(1)
#     print(counter)     #o(1)
# output:
#     O(n)
# ----------------------------------------------------------------------------------------
# problem 3:
#     def fun(N,M):
#     arr=[]        #o(1)
#     counter=0     #o(1)
#     for i in range(N): #o(n)
#         arr.append(i)
#     for i in range(M):  #o(m)
#         counter+=1
#     print(counter)   #0(1)
    
# output:
#     O(m+n)
# ----------------------------------------------------------------------------------------
# problem 4:
#     def function(N,M):
#     counter=0      #o(1)
#     for i in range(N):   #o(n)
#         for j in range(M):  #o(m)
#             counter+=1
#     print(counter)           #o(1)
    
# output:
#     O(m*n) becoz it is dependent loop that why we are multiplying.
# ----------------------------------------------------------------------------------------
# problem 5:
#     def fun(n):
#     for i in range(n):     #O(n)
#         print(pow(i,n))    #Python's pow function, when used with two arguments, utilizes efficient methods like exponentiation by squaring with O(logn) for positive integer exponents.
# output:
#     O(n log n)
    
# ----------------------------------------------------------------------------------------
# problem 6:
#     def f(n):
#     if n == 0 or n == 1:   #O(1)
#         return 1
#     return f(n - 1) + f(n - 2)
# # Because the number of calls grows exponentially with n, the time complexity of the function f(n) is  2 power n
# output:
#     2 power n
# ----------------------------------------------------------------------------------------
# problem 7:
#     def fun(n,m):
#     arr=[[0]*m for i in range(n)]    
#     for i in range(n):
#         for j in range(m):
#             k=1
#             while k<n*m:
#                 k*=2
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    








