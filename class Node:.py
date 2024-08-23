class Node:
    def _init_(self,data,next=None):
        self.data=data
        self.next=next
def linkedlist(head):
    while head:
        print(head.data)
        head=head.next        

def addtwonumbers(l1,l2):
    carry=0
    ans=p=Node(123)
    while l1 or l2 or carry:
        l1data=0
        if l1:
            l1data=l1.data
            l1=l1.next
        l2data=0
        if l2:
            l2data=l2.data
            l2=l2.next 
        sum=carry+l1data+l2data
        p.next=Node(sum%10)
        carry=sum//10
        p=p.next
    return ans.next           
l1=Node(2,Node(4,Node(3)))
l2=Node(5,Node(6,Node(4)))
result=addtwonumbers(l1,l2)
linkedlist(result)