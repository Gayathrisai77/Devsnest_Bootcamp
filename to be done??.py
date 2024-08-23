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
    
      if data < self.key:
        if self.lchild:
            self.lchild.insert(data)
        else:
            self.lchild = bst(data)
      elif data > self.key:
        if self.rchild:
            self.rchild.insert(data)
        else:
            self.rchild = bst(data)
            
    # def search(self,data):
    #   if self.key == data:
    #     print("node is found!")
    #   if self.key < data:
    #     if self.lchild:
    #         self.lchild.search(data)
    #     else:
    #         print("node is not present in tree!")
            
            
    #   if self.key > data:
    #     if self.rchild:
    #         self.rchild.search(data)
    #     else:
    #         print("node is not present in tree!")
            
            
            
    def preorder(self):  #root-->left--->right
       # if self.key is None:
            #return
        print(self.key,end = " -->")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
              self.rchild.preorder()
              
    # def inorder(self):     #left-->root-->right
    #     if self.key is None:
    #         return
    #     if self.lchild:
    #         self.lchild.inorder()
    #     print(self.key,end = "-->")
    #     if self.rchild:
    #         self.rchild.inorder()
    def inorder(self):
        #if self.key is None:
            #return 
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end = "->")
        
        if self.rchild:
            self.rchild.inorder()
            
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end = " -->")
        
    ##searching a node in tree
    def search(self,data):
        if self.key == data:
            print("Node is found!")
        if data < self.key:
            if self.lchild:
              self.lchild.search(data)
            else:
              print("Node is not present in tree")
        if data > self.key:
            if self.rchild:
              self.rchild.search(data)
            else:
                print("Node is not present in tree")
                
            
            
            
            
root = bst(100)
root.insert(50)
root.insert(40)
root.insert(60)
root.insert(10)
#root.search(10)
#root.search(7)
print("preorder traversal:")
root.preorder()
print("\ninorder traversal:")
root.inorder()
print("\npostorder traversal:")
root.postorder()
print("\nIs node is present:")
root.search(7)
root.search(100)
            
            
            
        