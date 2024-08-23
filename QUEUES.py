##################  QUEUE QUESTIONS ##########################

# creating a sample queue
queue = []
#enqueue
queue.append("nazar")
queue.append("gaye")
queue.append("D")
queue.append("mani")
queue.append("srav")
queue.append("bhagi")
remove = queue.pop(0)
print("remove",remove)
peek = queue[0]
length = len(queue)
print("length:",length)
print("peek:",peek)
print("Queue:",queue)

######## Basic implementation of queue using class #############
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,data):
        self.queue.append(data)
        
    def dequeue(self):
        if self. isempty():
            return "queue is empty"
        return self.queue.pop(0)
        
    def peek(self):
        if self.isempty():
            return "queue is empty"
        return self.queue[0]
        
    def isempty(self):
        return len(self.queue) == 0
        
    def size(self):
        return len(self.queue)
        
        
myqueue = Queue()
myqueue.enqueue("1")
myqueue.enqueue("2")
myqueue.enqueue("3")
myqueue.enqueue("4")
print("Queue:",myqueue.queue)
print("dequed element is:",myqueue.dequeue())
print("peek element is :",myqueue.peek())
print("is queue empty:",myqueue.isempty())
print("length of the queue:",myqueue.size())
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
######### FIRST NON REPEATING CHARACTER ##########
from collections import deque,defaultdict  #import these 2 data structures deque for to maintain order and efficiently pop from left #2 one is used store the frequency of char..it is intilize newkey with default 0
def first_non_repeating(string):
    queue = deque()
    frequency = defaultdict(int)
    for char in string:
        frequency[char] += 1
        queue.append(char)
        while queue and frequency[queue[0]] > 1:   #if char frequency is more than 1 means it is already in queue then popthat
            queue.pop()
    if not queue:
        return "there is no non-repeating value"
    else:
        return queue[0]   #finally queue has unique elments only in that we want first one
        
string = "aaddffsggt"
result = first_non_repeating(string)
print("first non repeating character:",result)

#----------------------------------------------------------------------------------------------------------------------------------------------------
######### IMPLEMENTATION OF A DEQUEUE #############
class dequeue:
    def __init__(self):
        self.items = []
        
    def add_front(self,data):
        self.items.insert(0,data)
        
    def add_rear(self,data):
        self.items.append(data)
        
    def delete_front(self):
        return self.items.pop(0)
        
    def delete_rear(self):
        return self.items.pop()
        
    def isempty(self):
        if len(self.items) == 0:
            return True
        return False
        
    def size(self):
        return len(self.items)
        
    def peek(self):
        return self.items[0]
        
mydequeue = dequeue()
mydequeue.add_front(1)
mydequeue.add_front(2)
mydequeue.add_rear(3)
mydequeue.add_front(4)
print("dequeue:",mydequeue.items)
print("delete at end:",mydequeue.delete_rear())
print("delete at begin:",mydequeue.delete_front())
print("is dequeue is empty:",mydequeue.isempty())
print("dequeue:",mydequeue.items)
print("peek elemnt is:",mydequeue.peek())
print("length of the deque is :",mydequeue.size())

#-----------------------------------------------------------------------------------------------------------------------------------------------
###### PAGE REPLACEMENT [OR] LRU {least recently used } #######
def page_replacement(pages,capacity):
    memory = []
    page_count = 0
    for page in pages:
        if not page in memory:
            if len(memory) == capacity:
                memory.pop(0)
            memory.append(page)
            page_count += 1
            print(f" page {page} is caused a page falut at memorypostion{memory}")
        else:
            print(f" page {page} is already in memory at{memory}")
    return page_count
            
pages = [1,4,2,4,5,6]
capacity = 3
print(page_replacement(pages,capacity))
            

#--------------------------------------------------------------------------------------------------------------------------------------------------
############# REVERSE A QUEUE #############

class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,data):
        self.queue.append(data)
        
    def dequeue(self):
        if self. is_empty():
            return "queue is empty"
        return self.queue.pop(0)
        
    def is_empty(self):
        if len(self.queue)== 0:
            return True
        return False
        
    def reverse(self):
        stack = []
        while self.queue:
            stack.append(self.queue.pop(0))
        while stack:
            self.queue.append(stack.pop())
        
        
        
myqueue = Queue()
myqueue.enqueue("1")
myqueue.enqueue("2")
myqueue.enqueue("3")
myqueue.enqueue("4")
print("Queue:",myqueue.queue)

myqueue.reverse()

print("Reversed queue:",myqueue.queue)

#-----------------------------------------------------------------------------------------------------------------------------------
############## merging two sorted arrays using queues ##################
from queue import Queue
def merge_sorted_array(arr1,arr2):
    queue1 = Queue()
    queue2 = Queue()
    merged_queue = Queue()
    
    for elem in arr1:
        queue1.put(elem)
        
    for elem in arr2:
        queue2.put(elem)
        
    while  not queue1.empty() and not queue2.empty():
        if queue1.queue[0] <= queue2.queue[0]:
            merged_queue.put(queue1.get())
        else:
            merged_queue.put(queue2.get())
            
    while  not queue1.empty():
        merged_queue.put(queue1.get())
        
    while not queue2.empty():
        merged_queue.put(queue2.get())
        
    merged_list = list(merged_queue.queue)
    
    return merged_list
    
arr1 = [1,3,5,7]
arr2 = [2,4,6,9]
print(merge_sorted_array(arr1,arr2))

#-----------------------------------------------------------------------------------------------------------------------------------
######## REMOVE AN ELEMENT AN QUEUE ######
from queue import   Queue
def removingelement(arr,k):
    queue = Queue()
    for elem in  arr:
        if elem != k:
            queue.put(elem)
    
    result = list(queue.queue)
    return result
    
arr = [10,20,30,40,50]
k = 30
print(removingelement(arr,k))
            
    
    
    
        
        
        
        
        
        
        
        
        
        
        





