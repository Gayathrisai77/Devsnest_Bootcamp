 #insertion sort
def insertion_sort(my_list):
    for index in range(1,len(my_list)):
        current_element = my_list[index]
        position = index
        while current_element<my_list[position-1] and position> 0:
            my_list[position] = my_list[position-1]
            position = position-1
        my_list[position] = current_element
my_list =[2,4,3,7,8,9]
insertion_sort(my_list)
print(my_list)
        
        
    
#BINARY SEARCHHH
# def binary_search(nums,target):
#     left = 0
#     right = len(nums)-1
#     while left<right:
#         mid = (left+right)//2
#         if nums[mid]==target:
#             return mid
#         elif nums[mid]<target:
#             left = mid+1
#         else:
#             right = mid-1
#     return -1
# nums =[1,2,3,4,5,6,7,8,9]
# target = 7
# print(binary_search(nums,target))
# insertion sort

            
# Given a string, reverse it using a stack.
# Input: A string, e.g., "hello".
# Output: The reversed string, e.g., "olleh".

# def reverse_string(string):
#     stack = []
#     for i in string:
#         stack.append(i)
#     rev = " "
#     while len(stack) != 0:
#         rev += stack.pop()
#     return rev
# string = "hello"
# print(reverse_string(string))

# stack = []
# maxsize = 4
# def push(x):
#     if len(stack)==maxsize:
#         print("stack is overflow")
#     else:
#         stack.append(x)
#         return x
# def pop():
#     if len(stack)==0:
#         print("stack is underflow")
#     else:
#         stack.pop()
# def peek():
#     if len(stack)==0:
#         print("stack is underflow")
#     else:
#         print(stack[-1])

# print(push(3))
# print(push(4))
# print(peek())
# print(pop())

# def sorted_stack(stack):
#     aux_stack = []
#     # while len(stack)>0:
#         smallest = stack[-1]
#     for i in range(len(stack())):
#        if stack[i]<smallest:
#            smallest = stack[i]
#            aux_stack.append(smallest)
#            stack.remove(smallest)
#     return aux_stack
# stack = [5,3,1,4,2]
# print(sorted_stack(stack))
       
# # 3.Add Two Numbers Represented by Linked Lists:

# # Input:    List 1: 2 -> 4 -> 3 (represents the number 342)
# #              List 2: 5 -> 6 -> 4 (represents the number 465)
# # Output:  342+465 (807)
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# def reverse_linked_list(head):
#     prev = None
#     current = head
#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
#     return prev
# def solve(l1,l2):
#     l1 = reverse_linked_list(l1)
#     l2 = reverse_linked_list(l2)

#     carry = 0
#     dummy = Node(0)
#     ans = dummy
#     while l1 or l2 or carry:
#         l1data = l1.data if l1 else 0
#         l2data = l2.data if l2 else 0
#         total = carry+l1data+l2data
#         carry = total//10
#         digit = total%10
#         ans.next = Node(digit)
#         if l1:
#             l1 = l1.next
#         if l2:
#             l2 = l2.next
#         ans = ans.next
#     result = reverse_linked_list(dummy.next)
#     output = ""
#     while result:
#         output += str(result.data)
#         result = result.next
#     return output
# l1 = Node(2)
# l1.next = Node(4)
# l1.next.next = Node(3)
# l2 = Node(5)
# l2.next = Node(6)
# l2.next.next = Node(4)
# print(solve(l1,l2))

# 2.Remove Nth Node From End of List:

# Given a linked list, remove the nth node from the end of the list and return its head. 

# Input:  Linked List: 1 -> 2 -> 3 -> 4 -> 5
# Output:  Updated Linked List: 1 -> 2 -> 3 -> 5
# class Node:
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
# class linkedlist:
#     def removenthnode(self,head:Node,n:int):
#         dummy = Node(0)
#         left = dummy
#         right = head
#         while n>0 and right:
#           right = right.next
#           n -= 1
#         while right:
#           left = left.next
#           right = right.next
#         left.next = left.next.next
#         return dummy.next

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# l1 = linkedlist()
# result = l1.removenthnode(head,5)
# while result:
#     print(result.val,end="")
#     result = result.next

































