# import array
# arr = array.array("i",[1,2,3,4,5,6,7])  #memory effeciency to deal with databases  #i is for integers # f is for floating point numbers
# print(arr)  #type code:to ensure that all elements in the array of same typeprint(arr)
               #2nd array: (iterable) like list,tuple which suits typecode
####Array traversal####
# import array
# arr = array.array("i",[1,2,3,4,5,6,7])
# for i in arr:
#     print(i,end = "")
#####inserting an element########
# def insertelement(arr,element,position):
#     arr.insert(position,element)
#     return arr
# arr = [1,5,3,6,9]
# print("before insertion:",arr)
# element = 11
# position = 2
# new_array = insertelement(arr,element,position)
# print("after insertion:",new_array)
# :::::::::::::deletion in an array:::::::::::::::

# def deleteelement(arr,position):
#     del arr[position]           #() is not appropriate for accesing elements in python.if you use() python will interpet it as trying to call a function named"arr"
#                                   #with the argument"position" which is we dont want                                   
#     return arr
# arr = [4,6,3,8,2,9]
# print("before deletion:",arr)
# position = 1
# new_array = deleteelement(arr,position)
# print("after deletion:",new_array)

###2
# arr = [2,3,4,6,7,8,91,45]
# position = 4
# del arr[position]
# print(arr)
###3
# for removing an element not an index
# arr = [12,4,6,7,8,9]
# element = 4
# arr.remove(element)
# print(arr)
#### searching an element in an array
# def searchingelement(arr,key):
#     for x in arr:
#         if x == key:
#             print("the element is:",x)
#             return x
#     print("the value not even exist")
#     return None
# arr = [8,6,7,3,4,1]
# key = 77
# result = searchingelement(arr,key)
# print(result)

#::::finding the three largest elements in an array:::::::
def find_first_three(arr):
    sorted_arr = list(set(arr))
    sorted_arr.sort(reverse=True)
    if len(sorted_arr)<3:
        return "there is no distinct  values"
    return sorted_arr[:3]
arr = [10,10,5,9,22,31,9]
result = find_first_three(arr)
print(result)


#:::::::finding three largest distinct values:::::::::
import array as arr
def find_three_largest(arr):
    if len(arr)<3:
        return "array length is less than 3"
    first = second = third=float("-inf")  #intizling with negativee firstt
    for num in arr:
        if num > first:     #4 > (-) #7>4        #9 > 7    #11>9  #12>11   #10>12 not
            third = second           #third =(-) #third =4 thir=7#thir=9   
            second = first           #second = 4 second=7  seco=9 sec0=11  
            first = num  #first = 4  #first = 7 #first = 9 first=11 first=12
        elif num > second:  #10 > 11 not so it goes to next elif
            third = second
            seond = num
        elif num > third: # 10 > 9  true
            third = num   #third = 10  now third updated to 10
    return [first,second,third]
arr = [4,7,9,11,12,10]
result = find_three_largest(arr)
print(result)

###finding three lowest values#####
import array as arr
def find_three_lowest(arr):
    new_array = list(set(arr))
    new_array.sort()
    if len(arr)<3:
        return "length of the array is less than 3"
    return new_array[:3]
arr = [7,3,9,2,3,1,4]
result = find_three_lowest(arr)
print(result)
    
###finding second largest number in an array######
import array as arr
def find_second_largest(arr):
    new_array = list(set(arr))
    new_array.sort(reverse = True)
    if len(arr)<2:
        return "the length of the array is less than 2"
    return new_array[1]
arr = [6,9,10,11,56,2,99]
result = find_second_largest(arr)
print(result)


#### Move all zeros to end an array #####
def all_zeros_end(arr):
    nonzero_index = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[nonzero_index]=arr[i]
            nonzero_index +=1
    for i in range(nonzero_index,len(arr)):
        arr[i]=0
    return arr
arr = [0,3,2,1,0,3,0,11,3,0,2]
result = all_zeros_end(arr)
print(result)
