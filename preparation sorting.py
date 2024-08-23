# def binary_search(nums,target):
#   left = 0
#   right = len(nums)-1
#   while left<right:
#     mid = (left+right)//2
#     if nums[mid]==target:
#       return mid
#     elif nums[mid]<target:
#       low = mid+1
#     else:
#       left = mid-1
#   return -1
# nums = [2,3,4,56,1,8,9]
# target = 56
# print(binary_search(nums,target))

# selection sort alogorithm
# def my_list(list):
#   for i in range(len(list)):
#     min_index = i
#     for j in range(i+1,len(list)):
#       min_index = j
#       if list[i]>list[min_index]:
#         list[i],list[min_index]=list[min_index],list[i]
#   return list
# list = [2,3,4,5,6,7,8,9,1]
# print(my_list(list))
        
#selection sort
# def selection_sort(list):
#   for i in range(len(list)):
#     min_index = i
#     for j in range(i+1,len(list)):
#        min_index = j
#        if list[i]>list[min_index]:
#          list[i],list[min_index] = list[min_index],list[i]
#   return list
# list = [12,56,78,23,12,0]
# print(selection_sort(list))

#insertion sort
# def insertion_sort(list):
#   for index in range(1,len(list)):
#     current_value = list[index]
#     position = index
#     while current_value<list[position-1] and position>0:
#       list[position] = list[position-1]
#       position = position-1
#     list[position] = current_value
#   return list
# list = [12,5,4,6,7,2]
# print(insertion_sort(list))




























