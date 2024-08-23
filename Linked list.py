#::::creating linkedlist ::::::
class Node:       #creating a class node
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:   #creating a linkedlist
    def __init__(self):
        self.head = None
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head      #if self.head is not none then print data and go to the ref as n=n.ref
            while n is not None:
              print(n.data,"--->",end = "")
              n=n.next
              
    def add_begin(self,data):
        new_node = Node(data)   # we are taking it froma above class node# created [data|none]
        new_node.next = self.head  
        self.head = new_node     #the newnode become firstnode of the linkedlist #the reference of first node is stored here
        
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n=n.next
        if n is None:
                print(" node is not  present here")
        else:
          new_node = Node(data)
          new_node.next = n.next
          n.next = new_node
        
l1=linkedlist()
l1.add_begin(8)
l1.add_begin(7)
l1.add_end(10)
l1.add_end(9)
l1.add_begin(6)
l1.print_ll()


#:::::::::::REVERSE A LINKED LIST :::::::

###linked list###
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def print_ll(self):
        if self.head == None:
           print("linked list is empty")
        else:
          n = self.head
          while n is not None:
            print(n.data,"--->",end = "")
            n=n.next
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    def reverse(self):
        prev = None 
        curr = self.head     #10   #20
        while curr is not None: 
            next_node = curr.next   #20    #30
            curr.next = prev #none breaking the linke b/w 10 and 20 # 20 and 30
            prev = curr      #prev pointing to 10       #20
            curr = next_node  #curr pointing to 20    #30
        self.head = prev     #after the loop the head is pointing to prev which is 50 which is new head of the reverse linked list
            
                
            
          
l1 = Linkedlist()
l1.add_begin(30)
l1.add_end(40)
l1.add_end(50)
l1.add_begin(20)
l1.add_begin(10)
l1.reverse()
l1.print_ll()



#if there is no cycle fast point will reach end before the slow point
# if there is cycle fast will catchup slow at some time within cycle
def hascycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   #they both entered the cycle then there is cycle return true otherwise return false
                return True
            return False
            
l1 = Linkedlist()
l1.add_begin(30)
l1.add_end(40)
l1.add_end(50)
l1.add_begin(20)
l1.add_begin(10)
l1.print_ll()
l1.head.next.next.next.next.next=l1.head
if l1.hascycle():
    print("detected the cycle")
else:
    print("no cycle detected")