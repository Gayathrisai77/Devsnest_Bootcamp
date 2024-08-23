# def fact(n):
#   if (n==0 or n==1):
#     return 1
#   else:
#     return n*fact(n-1)
# x = fact(6)
# print(x)
    



    #lenght of the string using recursion
def length(str):
    if str == "":
        return 0
    else:
        return 1+length(str[1:])
str = "hiihello"
print(length(str))
        
