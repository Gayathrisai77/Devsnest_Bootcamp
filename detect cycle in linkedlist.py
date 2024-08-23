class node:
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
               fast = fast.next
            return slow
    return None
  
    
    
node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

cycle_start_node = detect_cycle(node1)
if cycle_start_node:
    print("cycle started at value:",cycle_start_node.data)
else:
    print("no cycle detected!")





class tree:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
def serialize(root):
    if root is None:
        return "null"
    return str(root.data)+","+serialize(root.left)+","+serialize(root.right)
    
node1 = tree(1)
node2 = tree(2)
node3 = tree(3)
node4 = tree(4)
node5 = tree(5)
node6 = tree(6)
node7 = tree(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

print(serialize(node1))