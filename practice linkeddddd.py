##sinle linked list
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singleLinkedlist:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
                
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end ="")
                n = n.next
            
l1 = singleLinkedlist()

l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.print_ll()



class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty:")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end ="")
                n = n.next
            
l1 = singlelinkedlist()
l1.append(10)
l1.append(20)
l1.append(30)
l1.print_ll()

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty we cannot delete any nodes")
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("linked list is empty we cant delete any nodes")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    
    
    
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty:")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end ="")
                n = n.next
            
l1 = singlelinkedlist()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.append(60)
l1.delete_begin()
l1.delete_end()
l1.print_ll()
                
          



def delete_end(self):
        if self.head is None:
            print("linked list is empty we cant delete any nodes")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

l1.delete_end()
    
                
            