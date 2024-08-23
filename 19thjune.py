# class Treenode:
#     def __init__(self,key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None
        
#     def insert(self,data):
#         if self.key is None:
#             self.key = data
#             return 
#         if self.key == data:
#             return
#         if  data < self.key :
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = Treenode(data)
#         elif data > self.key:
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
# #root.insert(20)
# root.preorder()
         
    
    
class bst:
    def __init__(self,key):   #here self is the object itself
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.key is None:
           self.key = data
           return 
        if self.key == data:  # to ignore the duplicatess
            return
        
        if data < self.key:
            if self.lchild:      #if there is a leftchild we have perform whole insertion and find suitable postion
                self.lchild.insert(data)
            else:
                self.lchild = bst(data)   # if there is no leftchild for root then it create a data with lchild and rchild none as in class method
                
        elif data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = bst(data)
    
    def preorder(self):  #self refers root here
        if self.key is None:
            return
        print(self.key,end = "->")
        if self.lchild:     #if lchild is present there then we also perform preorder means we have to make lchild of root as root and perform root-left-right method till it has no left and right childs  recursively
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
            
            
    def inorder(self):
        if self.key is None:
            return 
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end = "->")
        if self.rchild:
            self.rchild.inorder()
            
            
    def postorder(self):
        if self.key is None:
            return
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end = "->")
            
            
root = bst(100)
root.insert(50)
root.insert(20)
root.insert(70)
root.insert(60)
root.insert(10)
root.insert(200)
print("preorder:")
root.preorder()
print("/n")
print("inorder:")
root.inorder()
print("/n")
print("postorder:")
root.postorder()
                
                
        
