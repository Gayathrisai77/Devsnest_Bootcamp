class Node:
    def __init__(self,data):
      self.data = data
      self.next = None
def reverse_linked_list(head):
        prev = None
        current = head
        while current:
          next_node = current.next
          current.next = prev
          prev = current
          current = next_node
        return prev
def solve(l1,l2):
        l1 = reverse_linked_list(l1)
        l2 = reverse_linked_list(l2)
    
        carry = 0
        dummy = Node(0)
        ans = dummy
        while l1 or l2 or carry:
            l1data = l1.data if l1 else 0
            l2data = l2.data if l2 else 0
            total = carry+l1data+l2data
            carry = total//10
            digit = total%10
            ans.next = Node(digit)
            if l1:
               l1 = l1.next
            if l2:
                l2 = l2.next
            ans = ans.next
        result = reverse_linked_list(dummy.next)
        output = ""
        while result:
            output += str(result.data)
            result = result.next
        return output
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)
print(solve(l1,l2))
        