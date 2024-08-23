################ LINKED LIST QUESTIONS ############
## implentation of a linked list ################

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def print_ll(self):
        if self.head is None:
           print("linked list is empty")
        else:
            n = self.head
            while n is not None:
              print(n.data,"---->",end = "")
              n = n.next
            
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
            
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
               break
            n = n.next
        if n is None:
            print("node is not present")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        
l1 = Linkedlist()
l1.add_begin(10)
l1.add_begin(20)
l1.add_end(40)
l1.add_begin(100)
l1.add_after(70,40)
l1.reverse()
l1.print_ll()

##--------------------------------------------------------------------------------------------------------------------------------
############# DETECT A CYCLE #############
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def detect_cycle(head):
    if not head or not head.next:
        return None
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
        
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return slow
    return None
        
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node2
Node4.next = Node5



cycle_start_at = detect_cycle(Node1)
if cycle_start_at :
    print("cycle detected at:",cycle_start_at.data)
else:
    print("no cycle detected!")

#--------------------------------------------------------------------------------------------------------------------------------------
########## MERGED TWO SORTED LISTS #########33
class listnode:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def merged_sorted_list(list1,list2):
    dummy = listnode(0)
    current = dummy
    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        current.next = list1 if list1 else list2
    return dummy.next
            
node1 = listnode(1)
node2 = listnode(2)
node3 = listnode(4)
node1.next = node2
node2.next = node3

node4 = listnode(3)
node5 = listnode(5)
node6 = listnode(6)

node4.next = node5
node5.next = node6

merged_list = merged_sorted_list(node1,node4)
while merged_list:
    print(merged_list.data,end = "->")
    merged_list = merged_list.next

#--------------------------------------------------------------------------------------------------------
############# Remove nth Node #############
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def removenthnode(head,n):
    current = head
    previous = head
    
    for _ in range (n):
        if current is None:
            return head
        current = current.next
    if current is None:
        return head
    if current is not None:
        return head.next
        
    while current.next is not None:
        current = current.next
        previous = previous.next
    if previous.next is not None:
        previous.next = previous.next.next
    return head
    
head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)

head = removenthnode(head,2)
remove_nth_node = head
while remove_nth_node:
    print(remove_nth_node.data,end = "-->")
    remove_nth_node = remove_nth_node.next

#-------------------------------------------------------------
class ListNode:
    def __init__(self,data=0):
        self.data = data
        self.next = None
        
def addtwonum(l1,l2):
    dummy = ListNode(0)
    ans = dummy
    carry = 0
    while l1 and l2:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0
        total = carry+val1+val2
        carry = total//10
        ans.next = ListNode(total%10)
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        ans = ans.next
    return dummy.next
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node4.next = node5
node5.next = node6


add_sum = addtwonum(node1,node4)
while add_sum:
    print(add_sum.data,end = "-->")
    add_sum = add_sum.next
else:
    print("None")

############# SWAPING NODES IN PAIRS ########
class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def swapingnodes(head):
    if not head or not head.next:
        return head
    new_node = head.next
    head.next = swapingnodes(new_node.next)
    new_node.next = head
    return new_node
    
def print_list(node):
    while node:
        print(node.data,end = "-->")
        node = node.next
    print()
    
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
head.next = node2
node2.next = node3
node3.next = node4

print("orignal list")
print_list(head)
head = swapingnodes(head)
print("swapped list")
print_list(head)











    

                   

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            