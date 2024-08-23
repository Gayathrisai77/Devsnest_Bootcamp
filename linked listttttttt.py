# we have to create two classes one is class node anotherone is class linked list

class node:
    def __init__(self,data):   #intilization method self,data are as parameters
        self.data = data       #user will give data that willbe assigned to it
        self.nref = None       # intially we are pointing to None
        self.prev = None
# now done with node class

# now we have to create doublylinked list class
class doublylinkedlist:    # self parameter is must in every class
    def __init__(self):
        self.head = None         #intially we are taking linked list as empty.if head is pointing to none there is no link in reference it means no linked list
# we are taking some methods
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
                n = n.nref      # here we find the last node "n".we starting printing from it until the first node which is n  
            while n is not None:
                print(n.data,"-->",end =" ")
                n = n.prev
                
    def append(self,data):   #append method name
        new_node = node(data)   #firstly we are creating new node with node class using data parameter
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
            
            
#object name #class name           
dl = doublylinkedlist()
dl.append(10)
dl.append(20)
dl.append(30)
dl.append(40)
dl.append(50)
dl.add_begin(100)
dl.add_end(200)
dl.delete_begin()
dl.delete_end()
dl.display()
print("\n")
#dl.display_reverse()

            
            
            
            
            
            
            
            
            
            
        