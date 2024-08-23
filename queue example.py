
# ### creating a sample queue
# # queue = []
# # #enqueue
# # queue.append("bhagi")
# # queue.append("gaye")
# # queue.append("D")
# # queue.append("mani")
# # queue.append("srav")
# # queue.append("Nazar")
# # remove = queue.pop(0)
# # print("remove",remove)
# # peek = queue[0]
# # length = len(queue)
# # print("length:",length)
# # print("peek:",peek)
# # print("Queue:",queue)

# #### data structures for creating queue we should use queue class#####
# # class queue:
# #     def __init__(self):
# #         self.queue = []
# #     def enqueue(self,element):
# #         self.queue.append(element)
# #     def dequeue(self):
# #         if self.isempty():
# #           return "queue is empty"
# #         return self.queue.pop(0)
# #     def peek(self):
# #         if self.isempty():
# #           return "queue is empty"
# #         return self.queue[0]
# #     def isempty(self):
# #         if len(self.queue)==0:
# #             return True
# #         return False
# #     def size(self):
# #         return len(self.queue)
# # myqueue = queue()
# # myqueue.enqueue("hate")
# # myqueue.enqueue("amma")
# # myqueue.enqueue("appa")
# # myqueue.enqueue("anna")
# # myqueue.enqueue("nenu")
# # print("Queue:",myqueue.queue)
# # print("dequeue:",myqueue.dequeue())
# # print("peek",myqueue.peek())
# # print("is empty",myqueue.isempty())
# # print("length of queue is:",myqueue.size())

# class Queue:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self,element):
#         self.queue.append(element)
#     def dequeue(self):
#         if self.isempty():
#             return "queue is empty"
#         return self.queue.pop(0)
#     def peek(self):
#         if self.isempty():
#             return "queue is empty"
#         return self.queue[0]
#     def isempty(self):
#         if len(self.queue)==0:
#             return True
#         return False
#     def size(self):
#         return len(self.queue)
# # create Queue as a myqueue
# myqueue = Queue()
# myqueue.enqueue("a")
# myqueue.enqueue("b")
# myqueue.enqueue("c")
# myqueue.enqueue("d")
# print("Queue:",myqueue.queue)
# print("dequeue:",myqueue.dequeue())
# print("peek:",myqueue.peek())
# print("isempty:",myqueue.isempty())
# print("length of the queue is:",myqueue.size())


##implementation of dequeue
class Dequeue:
    def __init__(self):
        self.items = []
    def isempty(self):
        if self.items == 0:
            return True
        return False
    def size(self):
        return len(self.items)
    def add_front(self,element):
        self.items.insert(0,element)
    def add_rear(self,element):
        self.items.append(element)
    def remove_front(self):
        return self.items.pop(0)
    def remove_rear(self):
        return self.items.pop()
        
mydq = Dequeue()
mydq.add_front(1)
mydq.add_front(2)
mydq.add_front(3)
mydq.add_rear(4)
mydq.add_rear(5)
mydq.add_rear(6)

print("my dequeue is :",mydq.items)
print("length of the queue is:",mydq.size())
print("is this queue empty:",mydq.isempty())
print("removing from the front:",mydq.remove_front())
print("removing from the rear:",mydq.remove_rear())



######### first non repeating character in a string using queue ###########
from collections import deque,defaultdict   #we have to import the data structure from the collections
def first_nonrepeated_character(string):
    queue = deque()              #we are creating queue to store characters
    frequency = defaultdict(int)  #to store the frequency means count
    for char in string:
        frequency[char] += 1     # it will store the count of each string
        queue.append(char)
        
        while queue and frequency[queue[0]]>1:  #run this loop until queue and count greaterthan 1
            queue.popleft()                     # if count more than 1 then removee it
    if not queue:
        return None                       #if there is no value return none
    else:
        return queue[0]                  # if there is anything return first
string = "aavvbbgeeryy"
result = first_nonrepeated_character(string)
print("first non repeating charcter is:",result)
    
 ##### implementing a queue using two stacks###############
###### doubt#########
class queueusingstacks:
    def __init___(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self,element):
        while self.stack1:
             self.stack2.append(self.stack1.pop())
        self.stack1.append(element)
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    def dequeue(self):
        if not self.stack1:
            return None
        return self.stack1.pop()
    def isempty():
        return len(self.stack1)==0
        
queue = queueusingstacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("queue is:",queue.stack1[::-1])

        
        
        
        
        
        
        
        
        











