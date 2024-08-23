# Python program to interchange first and last elements in a list:

# def swaplist(newlist):
#     newlist[0],newlist[-1] = newlist[-1],newlist[0]
    
#     return newlist
# newlist = [1,2,3,4,5]
# print(swaplist(newlist)

# Python Program to Swap Two Elements in a List:
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# def newlist(list,pos1=1,pos2=3):
#     list[pos1],list[pos2] = list[pos2],list[pos1]
#     return list
# list = [1,2,3,4,5]
# pos1,pos2 = 1,3
# print(newlist(list,pos1,pos2))                             #pos1-1,pos2-1

# How To Find the Length of a List in Python:
# Input: lst = [10,20,30,40]
# Output: 4
#USING LEN()FUNCTION
# list = [10,20,30,40]
# result = len(list)
# print(result)
#Python | Find elements of a list by indices:
# Input : lst1 = [10, 20, 30, 40, 50]
#         lst2 = [0, 2, 4]
# Output : [10, 30, 50]
# def findelements(list1,list2):
#     return [list1[i] for i in list2] #if the first element in list1 is in list2 then return  it
# list1 = [10,20,30,40,50]
# list2 = [0,2,4]
# print(findelements(list1,list2))

# Python program to find the String in a List:
# list = [1,"gaye","baby","god",77]
# s = "gaye"
# if s in list:
#     print(f'{s} is in it')
# else:
#     print(f'{s} is not in it)