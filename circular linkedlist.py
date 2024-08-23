class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.head:
                break
        print()
        
    def add_begin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:    #if it's not the head node, it means we haven't completed a full loop yet, and the traversal can continue. Once current.next points to self.head, it indicates that we've traversed the entire circular list and have come back to the beginning, so the traversal can stop.
                current = current.next
            current.next = new_node
            new_node.next = self.head
            
    def delete_at_beginning(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        if self.head.next == self.head:  # Only one node in the list
            self.head = None
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next
        
    def delete_at_end(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        if self.head.next == self.head:  # Only one node in the list
            self.head = None
            return
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current             #prev means second last node in linkedlist
            current = current.next
           
        prev.next = self.head     #we update its next pointer to skip the last node. This effectively removes the last node from the list.






# Creating a circular linked list
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.add_begin(100)
cll.add_end(200)
cll.add_begin(300)
cll.delete_at_end()
cll.delete_at_beginning()

# Displaying the circular linked list
cll.display()
