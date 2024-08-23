# class Treenode:
#     def __init__(self,key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None
        
# # class bst:
# #     def __init__(self):
# #         self.root = None
        
#     def insert(self,data):
#         if self.key is None:
#             self.key = data
#             return 
#         if self.key == data:
#             return 
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = Treenode(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = Treenode(data)
                
#     def preorder(self):
#         print(self.key)
#         if self.lchild:
#             self.lchild.preorder()
#         if self.rchild:
#             self.rchild.preorder()
                
# root = Treenode(10)
# root.insert(20)
# root.insert(5)
# root.insert(50)
# root.insert(30)

# root.preorder()

class bst:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.key is None:
            self.key = data
            return 
        if self.key == data:
          return 
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = bst(data)
        elif self.key < data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = bst(data)
                
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
            
root = bst(100)
root.insert(25)
root.insert(35)
root.insert(46)
root.insert(50)
root.preorder()
        
class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self, data):
        if self.key is None:
            self.key = data
            return 
        
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        elif data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
        # Note: if data == self.key, we can choose to handle it or ignore duplicates
    
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
            
# Test the BST
root = BST(100)
root.insert(25)
root.insert(35)
root.insert(46)
root.insert(50)

root.preorder()

        
        
        
        
                
                
                
                
                
                
        
        