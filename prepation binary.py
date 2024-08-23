# #implementation  a function to find the lowest common ancestor(LCA) of two nodes in a binary tree

# class Treenode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
        
# def lowest_common_ancestor(root,l,r):
#     if not root:
#         return None
#     if root.data == l or root.data == r :
#         return root
        
#     left_lca = lowest_common_ancestor(root.left,l,r)
#     right_lca = lowest_common_ancestor(root.right,l,r)
    
#     if left_lca and right_lca:
#         return root
        
#     return left_lca if left_lca else right_lca
    
    
# root = Treenode(3)
# root.left = Treenode(5)
# root.right = Treenode(1)
# root.left.left = Treenode(6)
# root.left.right = Treenode(2)
# root.right.left = Treenode(0)
# root.right.right = Treenode(8)
# root.left.right.left = Treenode(7)
# root.left.right.right = Treenode(4)

# result = lowest_common_ancestor(root,5,1)
# print("lowest common ancestor is :",result.data)




# ####2
#implement a level order traversal of a binary tree
from collections import deque
class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def level_order_traversal(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data,end = " ")
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
            
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.right = Tree(6)
print("level order traversal of this binary tree is:")
level_order_traversal(root)
#print("level order traversal of this binary tree is:",result)


##finding k largest elements in ascending order

import heapq

def find_k_largest(nums,k):
    min_heap = []
    for num in nums:
     if len(min_heap) < k:
        heapq.heappush(min_heap,num)
     else:
        if num > min_heap[0]:
            heapq.heapreplace(min_heap,num)
    result = sorted(min_heap)
    
    return result
    
nums = [3,2,5,4,1]
k = 3
result = find_k_largest(nums,k)
print(result)