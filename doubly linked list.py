############ DOUBLY LINKED LIST #############

#**creating doubly linked list and traversing in forward and backward********

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class doublylinkedlist:
    def __init__(self):
        self.head =None
    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None :   # If we were to use n.next is None, the loop would terminate one node earlier, and the new node would not be appended correctly to the end of the list.it will check each nd every node that node ref is none or not if not it will implement below operations otherwise it will come outof the loop..

                n = n.next
            n.next = new_node
            new_node.prev = n
                
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end = "")
                n = n.next
                
    def print_ll_reverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n= self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data,"<--",end ="")
                n=n.prev


    def add_begin(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n
            
                
                
l2 = doublylinkedlist()
l2.append(10)
l2.append(20)
l2.append(30)
l2.append(40)
l2.add_end(777)
l2.add_begin(700)
l2.add_end(999)

#print("forward:")
l2.print_ll()
# print("\n")
#print("backward:")
l2.add_begin(100)
#l2.print_ll_reverse()

