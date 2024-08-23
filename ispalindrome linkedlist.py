class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            lastnode = self.head
            while lastnode.next is not None:
                lastnode = lastnode.next
            lastnode.next = new_node

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True

        # Find the middle of the linked list
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare the original first half with the reversed second half
        first_half = self.head
        second_half = prev
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(2)
l1.append(1)

l1.print_ll()
print("\nIs palindrome:", l1.is_palindrome())
