#:::::::::::: SINGLE LINKEDLIST ::::::::::::

#creating class node
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# creating linkedlist class        
class singleLinkedlist:
    def __init__(self):
        self.head = None
        
#Adding element to an linked list        
    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
#adding at begining
    def add_begin(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
# # adding at the end
#     def add_end(self,data):        #it will add new element after head element also removed rest of elements becoz we are taking self.head.next pointing to none
#         new_node = node(data)
#         self.head.next = None     
#         self.head.next = new_node
        
# adding at the end
    def add_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
                n.next = new_node
                
        
# for printing linkedlist
    def print_list(self):
        if self.head is None:
            print( "Linked list is empty")
        else:
            n = self.head
            while n is not None:
              print( n.data," --> ",end = " " )
              n = n.next
              
        
l1 = singleLinkedlist()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.append(60)
l1.append(70)
l1.add_begin(100)
l1.add_end(10)
l1.print_list()
        