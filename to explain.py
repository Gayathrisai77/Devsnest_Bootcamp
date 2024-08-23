

class node:
    def __init__(self,data):   
        self.data = data       
        self.nref = None       
        self.prev = None

class doublylinkedlist:    
    def __init__(self):
        self.head = None
        
    def append(self,data):   
        new_node = node(data)   
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.prev = n
            
    def add_begin(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def add_end(self,data):
        new_node = node(data)
        if self.head is None:
             self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.prev = n
            
            
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        if self.head.nref is None:
            self.head = None
            print("there is no node after deleting this node")
        else:
            self.head = self.head.nref  #we are making second node as head 
            self.head.prev = None
            
            
    def delete_end(self):
        if self.head is None:
            print("linked list is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.prev.nref= None
            
        
    def display(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end = " ")
                n = n.nref
                
    def display_reverse(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head      # 1.last node #2.prev node
            while n.nref is not None:     
                n = n.nref    
            while n is not None:
                print(n.data,"-->",end =" ")
                n = n.prev
                
            
#object name #class name           
dl = doublylinkedlist()
dl.append(10)
dl.append(20)
dl.append(30)
dl.append(40)
dl.append(50)
dl.add_begin(100)
dl.add_end(200)
#dl.delete_begin()
#dl.delete_end()
dl.display()
print("\n")
#dl.display_reverse()

            
            
            
            
            
            
            
            
            
            
        