# Print Right View of a Binary Tree

# Q2) Given a Binary Tree, print the Right view of it.

# Input: 
#           1 
#          /     \ 
#       2       3,


#      /   \     /  \
#   4     5  6    7  8
# Output: Right view of the tree is 1 3 7 8
from collections import deque
class treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def rightview(root):
    q = deque([root])
    # from collections import deque
class treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def rightview(root):
    q = deque([root])
    while q:
        ele = q.pop()
        if ele:
            print(ele.data,end ="")
        if ele.right:
            q.append(ele.right)
            
root = treenode(1)
nodea = treenode(2)
nodeb = treenode(3)
nodec = treenode(4)
noded = treenode(5)
nodee = treenode(6)
nodef = treenode(7)
nodeg = treenode(8)

root = treenode(1)
root.left = nodea
root.right = nodeb
nodea.left = nodec
nodea.right = noded
nodeb.left = nodee
nodeb.right = nodef
nodef.right = nodeg

ans = rightview(root)
root = treenode(1)
nodea = treenode(2)
nodeb = treenode(3)
nodec = treenode(4)
noded = treenode(5)
nodee = treenode(6)
nodef = treenode(7)
nodeg = treenode(8)

root = treenode(1)
root.left = nodea
root.right = nodeb
nodea.left = nodec
nodea.right = noded
nodeb.left = nodee
nodeb.right = nodef
nodef.right = nodeg

ans = rightview(root)

# Input:  1 -> 2 -> 3 -> 4 -> 5 
# Output: 1 -> 5 -> 2 -> 4 -> 3

# class node:
#     def __init__(self,data):
#       self.data = data
#       self.next = None
    
# def reorder(head):
#     if not head or head.next :
#         return
#     # firstly finding the mid
#     slow = fast = head
#     while fast and fast.next :
#         slow = slow.next
#         fast = fast.next
        
#     # reversingg
#     prev = None
#     current = slow
#     while current:
#         temp = current.next
#         current.next = prev
#         prev = current
#         current = temp
        
#     #merging secondhalf
#     first = prev
#     second = head
#     while second:
#         temp1 = first.next
#         temp2 = second.next
        
#         first = second.next
#         second.next = temp1
        
#     temp1 = first
#     temp2 = second
        
        
#     if first:
#         first = first.next
    
# head = node(1)
# head.next = node(2)
# head.next.next = node(3)
# head.next.next.next = node(4)
# head.next.next.next.next = node(5)


# current = head
# while current:
#     print(current.data,"-->",end = " ")
#     current = current.next
# reorder(head)
        

###3
#Output: 1 2 3 4 5 6 7 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# def reorderList(head):
#     if not head or not head.next:
#         return
    
#     # Find the midpoint
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
        
#     # Reverse the second half
#     prev = None
#     current = slow
#     while current:
#         temp = current.next
#         current.next = prev
#         prev = current
#         current = temp
    
#     # Merge the first half with reversed second half
#     first = head
#     second = prev
#     while second:
#         temp1 = first.next
#         temp2 = second.next
        
#         first.next = second
#         second.next = temp1
        
#         first = temp1
#         second = temp2
        
#     # If the length of the original list is odd, the last node of the 
#     if first:
#         first.next = None


# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)

# reorderList(head)
# current = head
# while current:
#     print(current.data, end="-->")
#     current = current.next
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


























